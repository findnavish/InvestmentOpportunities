#!/usr/bin/env python3
"""Single-stock deep dive applying the Bodie-Kane-Marcus "Investments" toolkit.

Usage:  python deep_dive.py AMD [--offline]      (one ticker)
        python deep_dive.py --all                 (every ticker in config.json)

Writes docs/deep-dives/<ticker>/index.md and charts.  Qualitative context (PEST, catalysts)
lives in notes/<TICKER>.md and is embedded verbatim.  --offline re-uses the cached raw pull.
"""
import json
import pickle
import re
import signal
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.optimize import brentq
from scipy.stats import norm

warnings.filterwarnings("ignore")
signal.alarm(7200)

HERE = Path(__file__).parent
REPO = HERE.parents[1]
CFG = json.load(open(HERE / "config.json"))
XLSX = REPO / "docs" / "silicon-supply-chain" / "Silicon_Supply_Chain_Analysis.xlsx"
MRP, GT, SHRINK = CFG["mrp"], CFG["terminal_growth"], CFG["alpha_shrink"]
SUMD = HERE / "summaries"
plt.rcParams.update({"figure.dpi": 130, "font.size": 9, "axes.grid": True, "grid.alpha": 0.3})


# ---------------- formatting (no "$": arithmatex would treat it as math) ----------------
def pct(x, d=1, sign=False):
    if x is None or not np.isfinite(x):
        return "n/a"
    return f"{x * 100:+.{d}f}%" if sign else f"{x * 100:.{d}f}%"


def num(x, d=2):
    return "n/a" if x is None or not np.isfinite(x) else f"{x:,.{d}f}"


def bn(x, d=1):
    return "n/a" if x is None or not np.isfinite(x) else f"{x / 1e9:,.{d}f}bn"


def usd(x, d=2):
    return "n/a" if x is None or not np.isfinite(x) else f"USD {x:,.{d}f}"


def fnum(x):
    try:
        x = float(x)
        return x if np.isfinite(x) else np.nan
    except (TypeError, ValueError):
        return np.nan


def row(df, name, i=0):
    if df is None or name not in getattr(df, "index", []) or df.shape[1] <= i:
        return np.nan
    return fnum(df.loc[name].iloc[i])


def ttm(df, name):
    if df is None or name not in df.index:
        return np.nan
    v = pd.to_numeric(df.loc[name].iloc[:4], errors="coerce")
    return float(v.sum()) if v.notna().sum() == 4 else np.nan


# ---------------- data ----------------
SECTOR_ETF = {"Technology": "XLK", "Communication Services": "XLC", "Consumer Cyclical": "XLY", "Healthcare": "XLV",
              "Industrials": "XLI", "Energy": "XLE", "Consumer Defensive": "XLP", "Financial Services": "XLF",
              "Utilities": "XLU", "Real Estate": "XLRE", "Basic Materials": "XLB"}
PEER_KEYS = ["forwardPE", "priceToSalesTrailing12Months", "enterpriseToEbitda", "freeCashflow", "marketCap", "revenueGrowth",
             "grossMargins", "operatingMargins", "returnOnEquity", "targetMeanPrice", "currentPrice", "regularMarketPrice", "financialCurrency", "currency"]
_PEER_CACHE = {}


def pick_etf(C, info):
    if C.get("sector_etf"):
        return C["sector_etf"]
    if "semiconductor" in str(info.get("industry", "")).lower():
        return "SOXX"
    return SECTOR_ETF.get(info.get("sector"), "SPY")


def fetch(T, C, raw):
    import yfinance as yf
    tk = yf.Ticker(T)
    R = {}
    try:
        R["info"] = tk.info or {}
    except Exception:
        R["info"] = {}
    etf = pick_etf(C, R["info"])
    syms = list(dict.fromkeys([T, "SPY", etf, *C.get("peers", []), "^IRX"]))
    R["px"] = yf.download(syms, start="2014-01-01", auto_adjust=True, progress=False)["Close"]
    fc, qc_ = R["info"].get("financialCurrency"), R["info"].get("currency", "USD")
    R["fx"] = 1.0
    if fc and qc_ and fc != qc_:   # foreign filer (e.g. an ADR reporting in CNY): statements -> quote currency
        try:
            r_ = yf.download(f"{fc}{qc_}=X", period="5d", progress=False)["Close"].dropna()
            R["fx"] = float(np.ravel(r_.values)[-1])
        except Exception:
            R["fx"] = np.nan
    for a in ["quarterly_income_stmt", "quarterly_balance_sheet", "quarterly_cashflow", "income_stmt",
              "balance_sheet", "cashflow", "earnings_estimate", "revenue_estimate", "eps_trend",
              "eps_revisions", "earnings_history", "upgrades_downgrades", "recommendations",
              "insider_transactions", "institutional_holders", "major_holders", "calendar"]:
        try:
            R[a] = getattr(tk, a)
        except Exception:
            R[a] = None
    try:
        R["edates"] = tk.get_earnings_dates(limit=24)
    except Exception:
        R["edates"] = None
    chains = {}
    try:
        exps = tk.options
    except Exception:
        exps = []
    for e in exps:
        if (pd.Timestamp(e) - pd.Timestamp.today()).days > 400:
            break
        try:
            oc = tk.option_chain(e)
            chains[e] = (oc.calls, oc.puts)
        except Exception:
            pass
    R["chains"] = chains
    R["peer_info"] = {}
    for p_ in C.get("peers", []):
        if p_ not in _PEER_CACHE:
            try:
                inf = yf.Ticker(p_).info or {}
                _PEER_CACHE[p_] = {k_: inf.get(k_) for k_ in PEER_KEYS}
            except Exception:
                _PEER_CACHE[p_] = {}
        R["peer_info"][p_] = _PEER_CACHE[p_]
    R["fetched_utc"] = str(pd.Timestamp.now(tz="UTC").floor("min"))
    raw.parent.mkdir(exist_ok=True)
    pickle.dump(R, open(raw, "wb"))
    return R


def cell(df, r, c):
    try:
        return fnum(df.loc[r, c])
    except Exception:
        return np.nan


def clip(x, lo, hi):
    return float(min(max(x, lo), hi))


def mult(x, d=1):
    return "n/m" if x is None or not np.isfinite(x) or x <= 0 else f"{x:.{d}f}x"


FF_DIR = REPO / "analyses" / "silicon-supply-chain" / "data"


def load_ff(fname):
    lines = (FF_DIR / fname).read_text().splitlines()
    start = next(i for i, l in enumerate(lines) if (l.strip().startswith(",") and "RF" in l) or l.strip().startswith(",Mom"))
    rows = []
    for l in lines[start + 1:]:
        p = [x.strip() for x in l.split(",")]
        if len(p[0]) != 6 or not p[0].isdigit():
            break
        rows.append(p)
    cols = [c.strip() for c in lines[start].split(",")[1:]]
    return pd.DataFrame([r[1:] for r in rows], index=pd.to_datetime([r[0] for r in rows], format="%Y%m") + pd.offsets.MonthEnd(0),
                        columns=cols).astype(float) / 100


def ff_regress(r_m):
    try:
        ff = load_ff("F-F_Research_Data_5_Factors_2x3_CSV.txt").join(load_ff("F-F_Momentum_Factor_CSV.txt"), how="inner")
    except Exception:
        return None
    ff.columns = [c.strip() for c in ff.columns]
    fac = ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "Mom"]
    d = pd.concat([r_m - ff["RF"].reindex(r_m.index), ff[fac].reindex(r_m.index)], axis=1).dropna()
    d.columns = ["y"] + fac
    if len(d) < 24:
        return None
    f = sm.OLS(d.y, sm.add_constant(d[fac])).fit()
    out = {"months": len(d), "last": d.index[-1], "ff_alpha_ann": f.params["const"] * 12, "ff_alpha_t": f.tvalues["const"], "R2": f.rsquared}
    for k_ in fac:
        out[k_], out[k_ + "_t"] = f.params[k_], f.tvalues[k_]
    return out


def xl(sheet):
    try:
        return pd.read_excel(XLSX, sheet_name=sheet, index_col=0)
    except Exception:
        return None


def xl_row(sheet, T, key="ticker"):
    d = xl(sheet)
    if d is None:
        return None
    if key in d.columns:
        d = d.set_index(key)
    return d.loc[T] if T in d.index else None


# ---------------- Black-Scholes (ch21) ----------------
def bs(S, K, T, r, s, cp):
    d1 = (np.log(S / K) + (r + s * s / 2) * T) / (s * np.sqrt(T))
    d2 = d1 - s * np.sqrt(T)
    if cp == "c":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


def bs_iv(price, S, K, T, r, cp):
    intrinsic = max(0.0, S - K * np.exp(-r * T)) if cp == "c" else max(0.0, K * np.exp(-r * T) - S)
    if not np.isfinite(price) or price <= intrinsic + 1e-4:
        return np.nan
    try:
        return brentq(lambda s: bs(S, K, T, r, s, cp) - price, 1e-3, 6)
    except ValueError:
        return np.nan


def mid(r):
    b, a = fnum(r.get("bid")), fnum(r.get("ask"))
    return (b + a) / 2 if b > 0 and a > 0 else fnum(r.get("lastPrice"))


def run(T, offline=False):
    C = CFG["tickers"].get(T, {})
    slug = T.lower().replace(".", "-")
    OUTD = REPO / "docs" / "deep-dives" / slug
    CH = OUTD / "charts"
    CH.mkdir(parents=True, exist_ok=True)
    raw = HERE / "data" / f"{slug}.pkl"
    R = pickle.load(open(raw, "rb")) if offline and raw.exists() else fetch(T, C, raw)
    info = R["info"] or {}
    BENCH = pick_etf(C, info)
    NAME = C.get("name") or info.get("longName") or info.get("shortName") or T
    FX = fnum(R.get("fx", 1.0))
    FX = FX if np.isfinite(FX) else 1.0
    for a_ in ["quarterly_income_stmt", "quarterly_balance_sheet", "quarterly_cashflow", "income_stmt", "balance_sheet", "cashflow"]:
        df_ = R.get(a_)
        if FX != 1.0 and df_ is not None and len(df_):
            df_ = df_.apply(pd.to_numeric, errors="coerce")
            keep = [i_ for i_ in df_.index if "EPS" in i_ or "Shares" in i_ or "Rate" in i_]
            R[a_] = df_.mul(pd.Series(np.where(df_.index.isin(keep), 1.0, FX), index=df_.index), axis=0)

    px = R["px"].copy()
    px.index = pd.to_datetime(px.index).tz_localize(None)
    PEERS = [p_ for p_ in C.get("peers", []) if p_ in px and px[p_].notna().sum() > 60]
    s = px[T].dropna()
    ASOF = s.index[-1]
    P = float(s.iloc[-1])
    rf = float(px["^IRX"].dropna().iloc[-1]) / 100
    END = (ASOF.to_period("M") - 1).to_timestamp(how="end").normalize()

    # ---------- price over time ----------
    def ret_since(x, days=None, date=None):
        x = x.dropna()
        base = x.loc[:date] if date is not None else x.loc[:x.index[-1] - pd.Timedelta(days=days)]
        return x.iloc[-1] / base.iloc[-1] - 1 if len(base) else np.nan
    periods = [("1M", 30), ("3M", 91), ("6M", 182), ("YTD", None), ("1Y", 365), ("3Y", 1095), ("5Y", 1826), ("10Y", 3652)]
    ret_rows = []
    for sym in [T, BENCH, "SPY", *PEERS]:
        if sym not in px:
            continue
        x = px[sym].loc[:ASOF]
        r = [ret_since(x, date=pd.Timestamp(ASOF.year - 1, 12, 31)) if d is None else ret_since(x, d) for _, d in periods]
        cagr10 = (1 + r[-1]) ** (1 / 10) - 1 if np.isfinite(r[-1]) else np.nan
        ret_rows.append((sym, r, cagr10))
    hi52, lo52 = s.iloc[-252:].max(), s.iloc[-252:].min()
    dd = s / s.cummax() - 1
    maxdd, cur_dd = dd.loc[ASOF - pd.Timedelta(days=1826):].min(), dd.iloc[-1]
    maxdd_date = dd.loc[ASOF - pd.Timedelta(days=1826):].idxmin()
    dlog = np.log(s).diff().dropna()
    rv20, rv60, rv252 = (dlog.iloc[-n:].std() * np.sqrt(252) for n in (20, 60, 252))
    big = dlog.iloc[-1260:].abs().sort_values(ascending=False).head(5)

    # ---------- ch5 monthly return statistics ----------
    mpx = px.resample("ME").last()
    mret = mpx.pct_change().loc[:END]
    rfm = (px["^IRX"].resample("ME").mean() / 1200).shift(1).reindex(mret.index).ffill()
    W = mret[T].dropna().iloc[-60:].index
    r_m = mret.loc[W, T]
    ex = mret.loc[W].sub(rfm.loc[W], axis=0)
    n = len(r_m)
    am, sd = r_m.mean() * 12, r_m.std() * np.sqrt(12)
    gm = (1 + r_m).prod() ** (12 / n) - 1
    sk, ku = r_m.skew(), r_m.kurt()
    var5 = r_m.quantile(0.05)
    es5 = r_m[r_m <= var5].mean()
    var5n = r_m.mean() - 1.645 * r_m.std()
    ex_ann = ex[T].mean() * 12
    sharpe = ex_ann / sd
    down = ex[T].clip(upper=0)
    sortino = ex_ann / (np.sqrt((down ** 2).mean()) * np.sqrt(12))
    spy_ex, spy_sd = ex["SPY"].mean() * 12, mret.loc[W, "SPY"].std() * np.sqrt(12)
    spy_sharpe = spy_ex / spy_sd

    # ---------- ch8 index model, ch9 CAPM ----------
    def reg(y, x):
        d = pd.concat([y, x], axis=1).dropna()
        m = sm.OLS(d.iloc[:, 0], sm.add_constant(d.iloc[:, 1])).fit()
        return dict(alpha=m.params.iloc[0] * 12, alpha_t=m.tvalues.iloc[0], beta=m.params.iloc[1],
                    beta_t=m.tvalues.iloc[1], r2=m.rsquared, resid=m.resid.std() * np.sqrt(12))
    im = {b: reg(ex[T], ex[b]) for b in ["SPY", BENCH]}
    beta = im["SPY"]["beta"]
    beta_blume = 2 / 3 * beta + 1 / 3
    k_raw, k_blume = rf + beta * MRP, rf + beta_blume * MRP
    sys_var, firm_var = beta ** 2 * spy_sd ** 2, im["SPY"]["resid"] ** 2
    exall = mret.sub(rfm, axis=0)
    roll = {}
    for b in ["SPY", BENCH]:
        cov = exall[T].rolling(36).cov(exall[b])
        roll[b] = (cov / exall[b].rolling(36).var()).dropna()

    # ---------- ch7 correlations / diversification ----------
    corr = mret.loc[W, [c for c in [BENCH, "SPY", *PEERS] if c in mret]].corrwith(r_m)
    rho = corr.get("SPY", np.nan)
    sd_5050 = np.sqrt(0.25 * sd ** 2 + 0.25 * spy_sd ** 2 + 0.5 * rho * sd * spy_sd)

    # ---------- ch10 Fama-French (weekly pipeline) ----------
    ff = ff_regress(mret[T].dropna())

    # ---------- ch24 performance evaluation ----------
    treynor = ex_ann / beta
    jensen = im["SPY"]["alpha"]
    ir = jensen / im["SPY"]["resid"]
    m2 = (sharpe - spy_sharpe) * spy_sd

    # ---------- ch19 financial statements ----------
    qi, qb, qc = R.get("quarterly_income_stmt"), R.get("quarterly_balance_sheet"), R.get("quarterly_cashflow")
    qcols = list(qi.columns[:5])[::-1] if qi is not None and len(qi) and "Total Revenue" in qi.index else []
    qcols = [c for c in qcols if np.isfinite(fnum(qi.loc["Total Revenue", c]))]
    qtab = []
    for c in qcols:
        rev, cogs = fnum(qi[c].get("Total Revenue", np.nan)), fnum(qi[c].get("Cost Of Revenue", np.nan))
        gp, op, ni = (fnum(qi[c].get(k, np.nan)) for k in ("Gross Profit", "Operating Income", "Net Income"))
        rd, eps, amort = (fnum(qi[c].get(k, np.nan)) for k in ("Research And Development", "Diluted EPS", "Amortization Of Intangibles Income Statement"))
        ocf = fnum(qc[c].get("Operating Cash Flow", np.nan)) if qc is not None and c in qc else np.nan
        capex = fnum(qc[c].get("Capital Expenditure", np.nan)) if qc is not None and c in qc else np.nan
        fcf = fnum(qc[c].get("Free Cash Flow", np.nan)) if qc is not None and c in qc else np.nan
        sbc = fnum(qc[c].get("Stock Based Compensation", np.nan)) if qc is not None and c in qc else np.nan
        ar = fnum(qb[c].get("Accounts Receivable", np.nan)) if qb is not None and c in qb else np.nan
        inv = fnum(qb[c].get("Inventory", np.nan)) if qb is not None and c in qb else np.nan
        sh = fnum(qi[c].get("Diluted Average Shares", np.nan))
        qtab.append(dict(q=c, rev=rev, gm=gp / rev, opm=op / rev, nm=ni / rev, rd=rd / rev, eps=eps, ocf=ocf,
                         capex=capex, fcf=fcf, fcfm=fcf / rev, sbc=sbc / rev, amort=amort, dso=ar / rev * 91,
                         dio=inv / cogs * 91 if cogs else np.nan, sh=sh))
    ai_, ab_, ac_ = R.get("income_stmt"), R.get("balance_sheet"), R.get("cashflow")

    def ttm_or_fy(qdf, adf, name):
        v = ttm(qdf, name)
        return v if np.isfinite(v) else row(adf, name)
    rev_ttm, ni_ttm = ttm_or_fy(qi, ai_, "Total Revenue"), ttm_or_fy(qi, ai_, "Net Income")
    op_ttm, amort_ttm = ttm_or_fy(qi, ai_, "Operating Income"), ttm(qi, "Amortization Of Intangibles Income Statement")
    fcf_ttm, ocf_ttm = ttm_or_fy(qc, ac_, "Free Cash Flow"), ttm_or_fy(qc, ac_, "Operating Cash Flow")
    sbc_ttm = ttm_or_fy(qc, ac_, "Stock Based Compensation")
    sbc_ttm = sbc_ttm if np.isfinite(sbc_ttm) else 0.0
    buyback_ttm = ttm(qc, "Repurchase Of Capital Stock")

    def bal_avg(name):
        for df_ in (qb, ab_):
            if df_ is not None and name in df_.index:
                v = pd.to_numeric(df_.loc[name].iloc[:5], errors="coerce").mean()
                if np.isfinite(v):
                    return v
        return np.nan
    ta, te = bal_avg("Total Assets"), bal_avg("Stockholders Equity")
    dupont = dict(nm=ni_ttm / rev_ttm, at=rev_ttm / ta, lev=ta / te, roe=ni_ttm / te, roa=ni_ttm / ta)
    accruals = (ni_ttm - ocf_ttm) / ta
    cash = fnum(info.get("totalCash")) * FX
    debt = fnum(info.get("totalDebt")) * FX
    cash = cash if np.isfinite(cash) else row(qb, "Cash Cash Equivalents And Short Term Investments")
    debt = debt if np.isfinite(debt) else (row(qb, "Total Debt") if np.isfinite(row(qb, "Total Debt")) else 0.0)
    net_cash = cash - debt
    if "net_cash_override" in C:
        net_cash = float(C["net_cash_override"])
    shares = fnum(info.get("sharesOutstanding")) or np.nan
    if not np.isfinite(shares) or shares <= 0:
        shares = fnum(info.get("marketCap")) / P
    if not np.isfinite(shares) or shares <= 0:
        shares = row(qi, "Diluted Average Shares")
    mcap = P * shares
    ev = mcap - net_cash
    burn = -(fcf_ttm - sbc_ttm * 0) if np.isfinite(fcf_ttm) and fcf_ttm < 0 else np.nan
    runway = cash / burn if np.isfinite(burn) and burn > 0 else np.nan
    # ch17 degree of operating leverage from the last two fiscal years: %chg EBIT / %chg sales
    dol = np.nan
    r0_, r1_, e0_, e1_ = row(ai_, "Total Revenue", 0), row(ai_, "Total Revenue", 1), row(ai_, "Operating Income", 0), row(ai_, "Operating Income", 1)
    if all(np.isfinite([r0_, r1_, e0_, e1_])) and e1_ > 0 and abs(r0_ / r1_ - 1) > 0.02:
        dol = (e0_ / e1_ - 1) / (r0_ / r1_ - 1)
    sh_series = pd.to_numeric(qb.loc["Ordinary Shares Number"], errors="coerce").dropna() if qb is not None and "Ordinary Shares Number" in qb.index else pd.Series(dtype=float)
    dil_1y = sh_series.iloc[0] / sh_series.iloc[min(4, len(sh_series) - 1)] - 1 if len(sh_series) > 1 else np.nan

    # ---------- estimates ----------
    ee, re_ = R.get("earnings_estimate"), R.get("revenue_estimate")
    eps0, eps1 = cell(ee, "0y", "avg"), cell(ee, "+1y", "avg")
    if not np.isfinite(eps0):
        eps0 = fnum(info.get("trailingEps"))
    if not np.isfinite(eps1):
        eps1 = fnum(info.get("forwardEps"))
    eps_ya = cell(ee, "0y", "yearAgoEps")
    rev0 = cell(re_, "0y", "avg") * FX
    rev1 = {k: cell(re_, "+1y", k) * FX for k in ("low", "avg", "high")}
    est_note = ""
    if not (np.isfinite(rev0) and rev0 > 0):
        rev0 = rev_ttm
        est_note = "no consensus revenue estimates were available, so the path starts from TTM revenue"
    if not (np.isfinite(rev1["avg"]) and rev1["avg"] > 0):
        g_ = fnum(info.get("revenueGrowth"))
        g_ = clip(g_, -0.10, 0.60) if np.isfinite(g_) else 0.03
        rev1 = {"avg": rev0 * (1 + g_), "low": rev0 * (1 + g_) * 0.85, "high": rev0 * (1 + g_) * 1.15}
        est_note = est_note or "no next-year consensus was available, so next-year revenue uses the latest reported growth rate ±15%"
    for k_ in ("low", "high"):
        if not np.isfinite(rev1[k_]):
            rev1[k_] = rev1["avg"] * (0.9 if k_ == "low" else 1.1)
    rev_ya = cell(re_, "0y", "yearAgoRevenue") * FX
    fy_end = pd.Timestamp(info.get("lastFiscalYearEnd", 0), unit="s") if info.get("lastFiscalYearEnd") else pd.Timestamp(ASOF.year - 1, 12, 31)
    FY0 = fy_end.year + 1
    tgt = {k: fnum(info.get(f"target{k}Price")) for k in ("Low", "Median", "Mean", "High")}
    n_an = info.get("numberOfAnalystOpinions")
    rec = R.get("recommendations")
    rec0 = rec.iloc[0] if rec is not None and len(rec) and "strongBuy" in rec.columns else None
    trend = R.get("eps_trend")
    revs = R.get("eps_revisions")

    # ---------- ch18 valuation ----------
    xprem = float(C.get("risk_premium_add", 0.0))
    k = max(k_blume, GT + 0.02, rf + 0.02) + xprem
    pe_tr, pe_f0, pe_f1 = P / fnum(info.get("trailingEps")), P / eps0, P / eps1
    pe_tr, pe_f0, pe_f1 = (x if np.isfinite(x) and x > 0 else np.nan for x in (pe_tr, pe_f0, pe_f1))
    eps_g = eps1 / eps0 - 1
    peg = pe_f1 / (eps_g * 100) if eps_g > 0 else np.nan
    pvgo = P - eps1 / k
    nogrowth_pe = 1 / k
    fcf_y = fcf_ttm / mcap
    implied_g = k - (fcf_ttm - sbc_ttm) * (1 + GT) / ev  # ch18 constant growth on owner FCF (after SBC)
    ownr_m = (fcf_ttm - sbc_ttm) / rev_ttm
    cash_burner = not (np.isfinite(ownr_m) and ownr_m > 0.02)
    op_m = op_ttm / rev_ttm if np.isfinite(op_ttm) and rev_ttm else np.nan
    loss_maker = cash_burner and not (np.isfinite(op_m) and op_m > 0.05)   # FCF negative only because of capex is not "loss-making"
    if not np.isfinite(ownr_m):
        ownr_m = 0.0
    ownr_m = max(ownr_m, -1.5)   # cap the starting cash burn for pre-revenue names
    asof_t = ASOF
    ramp_years = CFG["margin_ramp_years"] + (2 if cash_burner else 0)

    def dcf(rev_next, g_after, margin, kk=k, years=CFG["fade_years"], ramp=ramp_years, per_share=True):
        revs_, t_, fcf_ = [rev0, rev_next], [], []
        g = g_after
        for i in range(years):
            revs_.append(revs_[-1] * (1 + g))
            g = g_after + (GT - g_after) * (i + 1) / years
        pv = 0.0
        for j, rv in enumerate(revs_[1:], start=1):
            yr = FY0 + j
            m = ownr_m + (margin - ownr_m) * min(1, j / ramp)
            tt = max(0.05, (pd.Timestamp(yr, 7, 1) - asof_t).days / 365.25)
            f = rv * m
            pv += f / (1 + kk) ** tt
            t_.append(tt)
            fcf_.append(f)
        tv = fcf_[-1] * (1 + GT) / (kk - GT)
        pv += tv / (1 + kk) ** t_[-1]
        eq = pv + net_cash
        return eq / shares if per_share else dict(ev=pv, tv_share=tv / (1 + kk) ** t_[-1] / pv if pv > 0 else np.nan, rev_end=revs_[-1], yr_end=FY0 + len(revs_) - 1)

    cfg_sc = C.get("scenarios") or {}
    if True:   # generic scenarios anchored on consensus growth and today's owner-FCF margin; config.json may override any field
        g_cons = clip(rev1["avg"] / rev0 - 1, -0.10, 0.60) if rev0 > 0 else 0.05
        gb = clip(0.6 * g_cons + 0.02, 0.02, 0.30)
        gm_ = fnum(info.get("grossMargins"))
        if loss_maker:
            mb = clip(0.3 * max(gm_ if np.isfinite(gm_) else 0.25, 0.25), 0.05, 0.12)
        elif cash_burner:   # profitable but investing heavily: anchor on 60% of the operating margin
            mb = clip(0.6 * op_m, 0.03, 0.40)
        else:
            mb = clip(ownr_m, 0.03, 0.45)
        scenarios = {"Bear": {"rev_next": "low", "g_after": round(max(0.0, gb * 0.5), 3), "fcf_margin": round(0.03 if loss_maker else mb * 0.75, 3)},
                     "Base": {"rev_next": "avg", "g_after": round(gb, 3), "fcf_margin": round(mb, 3)},
                     "Bull": {"rev_next": "high", "g_after": round(min(0.40, gb * 1.4 + 0.01), 3), "fcf_margin": round(mb * 1.6 if loss_maker else min(0.55, mb * 1.25), 3)}}
        scen_src = "generic (derived from consensus growth and today's owner-FCF margin)"
    if cfg_sc:
        fields = {f_ for v_ in cfg_sc.values() for f_ in v_}
        scenarios = {nm_: {**scenarios[nm_], **cfg_sc.get(nm_, {})} for nm_ in scenarios}
        scen_src = ("hand-set in config.json" if {"g_after", "fcf_margin"} <= fields else
                    "generic growth with hand-set steady-state margins (" + C.get("scenario_reason", "see config.json") + ")")
    scen = {}
    for nm_, sc in scenarios.items():
        rn = rev1[sc["rev_next"]]
        v = dcf(rn, sc["g_after"], sc["fcf_margin"])
        d = dcf(rn, sc["g_after"], sc["fcf_margin"], per_share=False)
        scen[nm_] = dict(rev_next=rn, g=sc["g_after"], m=sc["fcf_margin"], v=v, up=v / P - 1, **d)
    base = scenarios["Base"]
    try:
        need_m = brentq(lambda m: dcf(rev1["avg"], base["g_after"], m) - P, 0.01, 2.0)
    except ValueError:
        need_m = np.nan
    try:
        need_g = brentq(lambda g: dcf(rev1["avg"], g, base["fcf_margin"]) - P, -0.2, 2.0)
    except ValueError:
        need_g = np.nan
    try:
        need_k = brentq(lambda kk: dcf(rev1["avg"], base["g_after"], base["fcf_margin"], kk=kk) - P, GT + 0.005, 0.5)
    except ValueError:
        need_k = np.nan
    k_grid = [k - 0.03, k - 0.02, k - 0.01, k, k + 0.01]
    m_grid = sorted({round(max(0.01, base["fcf_margin"] * f_), 2) for f_ in (0.6, 0.8, 1.0, 1.2, 1.4)})
    sens = [[dcf(rev1["avg"], base["g_after"], m, kk=kk) for m in m_grid] for kk in k_grid]
    dil = C.get("potential_dilution")
    pe_grid = [20, 25, 30, 35, 40, 45]
    def mrow(inf, is_self=False):
        pr = fnum(inf.get("currentPrice")) if np.isfinite(fnum(inf.get("currentPrice"))) else fnum(inf.get("regularMarketPrice"))
        fx_ = FX if is_self else 1.0
        return {"forward_pe": fnum(inf.get("forwardPE")), "ps_ratio_ttm": fnum(inf.get("priceToSalesTrailing12Months")),
                "ev_ebitda_ttm": fnum(inf.get("enterpriseToEbitda")),
                "fcf_yield": fnum(inf.get("freeCashflow")) * fx_ / fnum(inf.get("marketCap")) if inf.get("financialCurrency") in (None, inf.get("currency")) or is_self else np.nan,
                "revenue_growth_fy": fnum(inf.get("revenueGrowth")), "gross_margin": fnum(inf.get("grossMargins")),
                "ebit_margin": fnum(inf.get("operatingMargins")), "roe_ttm": fnum(inf.get("returnOnEquity")),
                "analyst_target_upside": fnum(inf.get("targetMeanPrice")) / pr - 1}
    peers_tab = pd.DataFrame({T: mrow(info, True), **{p_: mrow(R.get("peer_info", {}).get(p_, {})) for p_ in PEERS}}).T
    peers_tab.loc[T, "forward_pe"] = pe_f1 if np.isfinite(pe_f1) else peers_tab.loc[T, "forward_pe"]
    pf = pd.to_numeric(peers_tab.drop(index=T)["forward_pe"], errors="coerce")
    med_fpe = pf[pf > 0].median() if (pf > 0).sum() else np.nan

    # ---------- ch27 Treynor-Black ----------
    tb_sum = xl("TB_Summary")
    bias = fnum(tb_sum.loc["analyst_optimism_bias_removed", "value"]) if tb_sum is not None and "analyst_optimism_bias_removed" in tb_sum.index else 0.0
    exp_an = tgt["Mean"] / P - 1
    capm_1y = rf + beta * MRP
    a_raw = exp_an - capm_1y
    a_db = a_raw - bias
    a_sh = a_db * SHRINK
    w0 = (a_sh / im["SPY"]["resid"] ** 2) / (MRP / spy_sd ** 2)
    w_star = w0 / (1 + (1 - beta) * w0)

    # ---------- ch6 capital allocation ----------
    alloc = []
    for A in (2, 3, 4, 6):
        alloc.append((A, (k_raw - rf) / (A * sd ** 2), (k_raw + a_sh - rf) / (A * sd ** 2)))

    # ---------- ch11 event study around earnings ----------
    ed = R.get("edates")
    events = []
    if ed is not None and len(ed):
        ed = ed.copy()
        ed.index = pd.to_datetime(ed.index)
        rets = px[[T, "SPY"]].pct_change()
        for ts, rr in ed.sort_index().iterrows():
            if pd.isna(rr.get("Reported EPS")):
                continue
            d0 = ts.tz_localize(None).normalize() if ts.tzinfo else ts.normalize()
            after = ts.hour >= 12
            idx = rets.index
            pos = idx.searchsorted(d0, side="right" if after else "left")
            if pos >= len(idx) or pos < 260 or pos + 20 >= len(idx):
                continue
            est = rets.iloc[pos - 260:pos - 10].dropna()
            mm = sm.OLS(est[T], sm.add_constant(est["SPY"])).fit()
            win = rets.iloc[pos - 5:pos + 21]
            ar = win[T] - (mm.params.iloc[0] + mm.params.iloc[1] * win["SPY"])
            ar.index = range(-5, -5 + len(ar))
            events.append(dict(date=d0.date(), react=idx[pos].date(), eps=rr.get("Reported EPS"), est=rr.get("EPS Estimate"),
                               surp=rr.get("Surprise(%)"), ar0=ar.loc[0], car11=ar.loc[-1:1].sum(), drift=ar.loc[2:20].sum(), ar=ar))
        events = events[-12:]
    if events:
        ev_df = pd.DataFrame([{k_: v for k_, v in e.items() if k_ != "ar"} for e in events])
        car_path = pd.DataFrame({i: e["ar"] for i, e in enumerate(events)}).cumsum()
        hit = np.mean([np.sign(e["surp"]) == np.sign(e["ar0"]) for e in events if pd.notna(e["surp"])])
        mean_abs_ar0 = np.mean([abs(e["ar0"]) for e in events])
        drift_corr = np.corrcoef(ev_df["car11"], ev_df["drift"])[0, 1] if len(ev_df) > 3 else np.nan
    cal = R.get("calendar")
    cal = cal if isinstance(cal, dict) else {}
    ne_ = cal.get("Earnings Date") or [None]
    next_earn = ne_[0] if isinstance(ne_, (list, tuple)) else ne_
    if next_earn is not None and pd.Timestamp(next_earn) < ASOF:
        next_earn = None

    # ---------- ch12 technicals & behavioural ----------
    d_ = s.diff()
    up, dn = d_.clip(lower=0).ewm(alpha=1 / 14).mean(), (-d_.clip(upper=0)).ewm(alpha=1 / 14).mean()
    rsi = float(100 - 100 / (1 + up.iloc[-1] / dn.iloc[-1]))
    ma50, ma200 = s.rolling(50).mean(), s.rolling(200).mean()
    mom = s.iloc[-22] / s.iloc[-253] - 1 if len(s) > 253 else np.nan
    rel6 = (s.iloc[-1] / s.iloc[-127]) / (px[BENCH].dropna().iloc[-1] / px[BENCH].dropna().iloc[-127]) - 1 if len(s) > 127 else np.nan
    ins = R.get("insider_transactions")
    ins_sales = ins_buys = np.nan
    if ins is not None and len(ins) and {"Start Date", "Text", "Value"} <= set(ins.columns):
        ins = ins.copy()
        ins["dt"] = pd.to_datetime(ins["Start Date"])
        recent = ins[ins["dt"] >= ASOF - pd.Timedelta(days=182)]
        txt = recent["Text"].fillna("")
        ins_sales = recent.loc[txt.str.contains("Sale"), "Value"].sum()
        ins_buys = recent.loc[txt.str.contains("Purchase"), "Value"].sum()
    ud = R.get("upgrades_downgrades")
    ud90 = None
    if ud is not None and len(ud) and {"priceTargetAction", "currentPriceTarget"} <= set(ud.columns):
        ud = ud.copy()
        ud.index = pd.to_datetime(ud.index)
        ud90 = ud[ud.index >= ASOF - pd.Timedelta(days=90)]

    # ---------- ch20-21 options ----------
    opt_rows, cc_rows = [], []
    ev_move = None
    chains_ = R.get("chains") or {}
    _all = pd.concat([c_ for pair in chains_.values() for c_ in pair]) if chains_ else pd.DataFrame({"bid": [], "openInterest": []})
    live_quotes = (_all["bid"] > 0).mean() > 0.5  # Yahoo zeroes quotes/OI outside market hours
    has_oi = (_all["openInterest"].fillna(0) > 0).mean() > 0.5
    close_dt = ASOF + pd.Timedelta(hours=16)
    for e, (calls, puts) in chains_.items():
        Tm = ((pd.Timestamp(e) + pd.Timedelta(hours=16)) - close_dt).total_seconds() / (365.25 * 86400)
        if Tm < 4 / 365 or len(calls) < 3 or len(puts) < 3:
            continue
        F = P * np.exp(rf * Tm)
        ivs = []
        for df_, cp in ((calls, "c"), (puts, "p")):
            dd_ = df_.iloc[(df_["strike"] - F).abs().argsort()[:2]]
            for _, r_ in dd_.iterrows():
                ivs.append(bs_iv(mid(r_), P, r_["strike"], Tm, rf, cp))
        atm = np.nanmean(ivs) if np.isfinite(ivs).any() else np.nan

        def iv_at(df_, K, cp):
            r_ = df_.iloc[(df_["strike"] - K).abs().argsort()[:1]].iloc[0]
            return bs_iv(mid(r_), P, r_["strike"], Tm, rf, cp)
        skew = iv_at(puts, 0.9 * P, "p") - iv_at(calls, 1.1 * P, "c")
        Katm = calls.iloc[(calls["strike"] - P).abs().argsort()[:1]]["strike"].iloc[0]
        cm = mid(calls[calls.strike == Katm].iloc[0])
        pm_ = mid(puts[puts.strike == Katm].iloc[0]) if (puts.strike == Katm).any() else np.nan
        parity_gap = (cm - pm_) - (P - Katm * np.exp(-rf * Tm))
        opt_rows.append(dict(exp=e, T=Tm, atm=atm, skew=skew, move=atm * np.sqrt(Tm), parity=parity_gap, K=Katm))
    opt = pd.DataFrame(opt_rows)
    if len(opt):
        opt = opt[opt["atm"].notna()].reset_index(drop=True)
    e_cc, cc_why = None, ""
    if len(opt) and next_earn is not None:
        ne = pd.Timestamp(next_earn)
        pre = opt[pd.to_datetime(opt["exp"]) < ne]
        post = opt[pd.to_datetime(opt["exp"]) > ne + pd.Timedelta(days=1)]
        if len(pre) and len(post):
            a_, b_ = pre.iloc[-1], post.iloc[0]
            var_e = b_["T"] * (b_["atm"] ** 2 - a_["atm"] ** 2)
            if var_e > 0:
                ev_move = dict(pre=a_["exp"], post=b_["exp"], iv_pre=a_["atm"], iv_post=b_["atm"], sd=np.sqrt(var_e), mad=np.sqrt(var_e) * np.sqrt(2 / np.pi))
        if len(pre) and pre.iloc[-1]["T"] * 365.25 >= 7:
            e_cc, cc_why = pre.iloc[-1]["exp"], "the last expiry before earnings"
    if len(opt) and e_cc is None:
        e_cc = opt.iloc[(opt["T"] * 365.25 - 35).abs().argsort()[:1]].iloc[0]["exp"]
        cc_why = "the expiry closest to 35 days" + (" (no expiry falls before the next earnings date)" if next_earn is not None else "")
    if e_cc is not None:
        calls, puts = R["chains"][e_cc]
        Tm = float(opt.loc[opt["exp"] == e_cc, "T"].iloc[0])
        for df_, cp in ((calls, "c"), (puts, "p")):
            for _, r_ in df_.iterrows():
                K, m_ = r_["strike"], mid(r_)
                v = bs_iv(m_, P, K, Tm, rf, cp)
                if not np.isfinite(v):
                    continue
                d1 = (np.log(P / K) + (rf + v * v / 2) * Tm) / (v * np.sqrt(Tm))
                d2 = d1 - v * np.sqrt(Tm)
                delta = norm.cdf(d1) if cp == "c" else norm.cdf(d1) - 1
                potm = norm.cdf(-d2) if cp == "c" else norm.cdf(d2)
                if 0.12 <= abs(delta) <= 0.32 and (not has_oi or fnum(r_.get("openInterest")) >= 100):
                    base_ = P if cp == "c" else K
                    cc_rows.append(dict(exp=e_cc, type="Call" if cp == "c" else "Put", K=K, bid=fnum(r_["bid"]), ask=fnum(r_["ask"]), mid=m_, iv=v,
                                        delta=delta, potm=potm, otm=K / P - 1, yld=m_ / base_, ann=m_ / base_ / Tm, oi=fnum(r_["openInterest"])))

    # ---------- signals page (hourly model) ----------
    sig = None
    sp = REPO / "docs" / "trade-signals" / "index.md"
    if sp.exists():
        m_ = re.search(r"^\| ([^|]+?) \| ([-+\d.]+) \| \*\*" + re.escape(T) + r"\*\*", sp.read_text(), re.M)
        if m_:
            sig = (m_.group(1).strip(), float(m_.group(2)))
        m2_ = re.search(r"Last updated:\*\* ([^·\n]+?UTC)", sp.read_text())
        sig_time = m2_.group(1) if m2_ else ""

    # =================== charts ===================
    fig, ax = plt.subplots(2, 1, figsize=(12, 8.5), gridspec_kw={"height_ratios": [3, 2]})
    s10 = s.loc[ASOF - pd.Timedelta(days=3652):]
    ax[0].plot(s10, lw=1.1, label=f"{T} close")
    ax[0].plot(ma50.loc[s10.index], lw=0.9, label="50-day MA")
    ax[0].plot(ma200.loc[s10.index], lw=0.9, label="200-day MA")
    ax[0].set_yscale("log")
    ax[0].set_title(f"{NAME} ({T}): price over 10 years (USD, log scale, split/dividend adjusted)")
    ax[0].legend()
    st = ASOF - pd.Timedelta(days=1826)
    for sym, sty in [(T, "-"), (BENCH, "k:"), ("SPY", "k--"), *[(p_, "-") for p_ in PEERS]]:
        if sym in px:
            x = px[sym].loc[st:].dropna()
            ax[1].plot(x / x.iloc[0] * 100, sty, lw=2 if sym == T else 0.9, label=sym, alpha=1 if sym in (T, BENCH, "SPY") else 0.6)
    ax[1].set_yscale("log")
    ax[1].set_title("5-year total return vs sector ETF, S&P 500 and peers (rebased to 100, log)")
    ax[1].legend(ncol=5, fontsize=7)
    fig.tight_layout()
    fig.savefig(CH / "price_history.png")
    plt.close(fig)

    fig, ax = plt.subplots(1, 2, figsize=(12, 3.8))
    ax[0].fill_between(dd.loc[st:].index, dd.loc[st:] * 100, 0, color="tab:red", alpha=0.4)
    ax[0].set_title("Drawdown from running peak (%), 5Y")
    x = np.linspace(r_m.min(), r_m.max(), 200)
    ax[1].hist(r_m, bins=20, density=True, alpha=0.6, label="monthly returns")
    ax[1].plot(x, norm.pdf(x, r_m.mean(), r_m.std()), "k--", label="normal, same mean/sd")
    ax[1].axvline(var5, color="tab:red", lw=1, label="historical 5% VaR")
    ax[1].set_title(f"Monthly return distribution, {n}m (skew {sk:.2f}, excess kurtosis {ku:.2f})")
    ax[1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(CH / "risk.png")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(12, 3.6))
    for b in roll:
        ax.plot(roll[b].loc["2017":], label=f"beta vs {b}")
    ax.axhline(1, color="k", lw=0.7)
    ax.set_title("Rolling 36-month beta (index model, monthly excess returns)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(CH / "rolling_beta.png")
    plt.close(fig)

    if qtab:
        q = pd.DataFrame(qtab)
        fig, ax = plt.subplots(figsize=(12, 3.8))
        lbl = [pd.Timestamp(c).strftime("%Y-%m") for c in q["q"]]
        ax.bar(lbl, q["rev"] / 1e9, color="tab:blue", alpha=0.6, label="Revenue (USD bn)")
        ax.set_ylabel("USD bn")
        a2 = ax.twinx()
        for col, lab_ in (("gm", "Gross margin"), ("opm", "GAAP operating margin"), ("fcfm", "FCF margin")):
            a2.plot(lbl, q[col] * 100, marker="o", label=lab_)
        a2.set_ylabel("%")
        a2.grid(False)
        h1, l1 = ax.get_legend_handles_labels()
        h2, l2 = a2.get_legend_handles_labels()
        ax.legend(h1 + h2, l1 + l2, fontsize=7, loc="upper left")
        ax.set_title("Quarterly revenue and margins")
        fig.tight_layout()
        fig.savefig(CH / "fundamentals.png")
        plt.close(fig)

    if len(opt):
        fig, ax = plt.subplots(figsize=(12, 3.6))
        ax.plot(pd.to_datetime(opt["exp"]), opt["atm"] * 100, marker="o", label="ATM implied vol (BS, from mid prices)")
        for v, lab_, sty in ((rv20, "20d realized", "--"), (rv60, "60d realized", ":"), (rv252, "1y realized", "-.")):
            ax.axhline(v * 100, ls=sty, color="gray", label=lab_)
        if next_earn is not None:
            ax.axvline(pd.Timestamp(next_earn), color="tab:red", lw=1, label=f"earnings {next_earn}")
        ax.set_title("Implied-volatility term structure vs realized volatility (%)")
        ax.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(CH / "iv_term.png")
        plt.close(fig)

    if events:
        fig, ax = plt.subplots(figsize=(12, 3.6))
        for c_ in car_path:
            ax.plot(car_path.index, car_path[c_] * 100, color="gray", alpha=0.35, lw=0.8)
        ax.plot(car_path.index, car_path.mean(axis=1) * 100, color="tab:blue", lw=2, label="average CAR")
        ax.axvline(0, color="tab:red", lw=1)
        ax.set_xlabel("trading days relative to first reaction day")
        ax.set_title(f"Event study: cumulative abnormal return around the last {len(events)} earnings releases (market model vs SPY), %")
        ax.legend()
        fig.tight_layout()
        fig.savefig(CH / "event_study.png")
        plt.close(fig)

    dv = [max(0.0, v["v"]) if np.isfinite(v["v"]) else np.nan for v in scen.values()]
    bars = [("52-week range", lo52, hi52), ("Analyst targets (low-high)", tgt["Low"], tgt["High"]),
            (f"{pe_grid[0]}-{pe_grid[-1]}x FY{FY0 + 1}E EPS", pe_grid[0] * eps1, pe_grid[-1] * eps1),
            ("DCF bear-bull (floored at 0)", np.nanmin(dv), np.nanmax(dv))]
    bars = [b_ for b_ in bars if np.isfinite(b_[1]) and np.isfinite(b_[2]) and b_[2] > 0]
    fig, ax = plt.subplots(figsize=(12, 3.4))
    fmt_ = (lambda x: f"{x:,.0f}") if P >= 20 else (lambda x: f"{x:,.2f}")
    for i, (lab_, lo, hi) in enumerate(bars):
        ax.barh(i, max(hi - lo, P * 0.004), left=lo, color="tab:blue", alpha=0.5)
        ax.text(hi, i, f"  {fmt_(lo)} - {fmt_(hi)}", va="center", fontsize=8)
    if bars and bars[-1][0].startswith("DCF"):
        for k_, v in scen.items():
            ax.plot(max(0.0, v["v"]), len(bars) - 1, "k|", ms=18)
            ax.text(max(0.0, v["v"]), len(bars) - 1 + 0.35, k_, ha="center", fontsize=7)
    ax.axvline(P, color="tab:red", lw=1.5, label=f"price {P:,.2f}")
    ax.set_xlim(left=max(0.0, min([b_[1] for b_ in bars] + [P]) * 0.8), right=max([b_[2] for b_ in bars] + [P]) * 1.2)
    ax.set_ylim(-0.6, len(bars) - 0.2)
    ax.set_yticks(range(len(bars)), [b[0] for b in bars])
    ax.set_title("Valuation summary (USD per share)")
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(CH / "valuation.png")
    plt.close(fig)

    # =================== verdict (rule-based, transparent) ===================
    rev_yoy = qtab[-1]["rev"] / qtab[0]["rev"] - 1 if len(qtab) >= 5 else (r0_ / r1_ - 1 if np.isfinite(r0_) and np.isfinite(r1_) and r1_ else np.nan)
    rev_up = bool(rev_yoy > 0)
    checks = [
        ("Valuation: base-case DCF at or above price", bool(scen["Base"]["v"] >= P), f"base DCF {usd(scen['Base']['v'], 0)} vs price {usd(P, 0)}"),
        ("Relative value: forward P/E at most 1.2x the peer median", bool(pe_f1 <= 1.2 * med_fpe), f"{mult(pe_f1)} FY{FY0 + 1}E vs peer median {mult(med_fpe)}"),
        ("Street: de-biased, shrunk analyst alpha > 0 (ch27)", bool(a_sh > 0), f"{pct(a_sh, 1, True)}"),
        ("Momentum: 12-1 month return > 0 (ch11)", bool(mom > 0), pct(mom, 0, True)),
        ("Trend: price above 200-day MA (ch12)", bool(P > ma200.iloc[-1]), f"{pct(P / ma200.iloc[-1] - 1, 0, True)} vs 200DMA"),
        ("Not overbought: RSI(14) below 70", rsi < 70, f"RSI {rsi:.0f}"),
        ("Fundamentals: revenue growing and FCF positive", bool(rev_up and fcf_ttm > 0), f"revenue {pct(rev_yoy, 0, True)} y/y, TTM FCF {bn(fcf_ttm)}"),
        ("Balance sheet: net cash", bool(net_cash > 0), f"net cash {bn(net_cash)}"),
    ]
    passed = sum(c[1] for c in checks)
    val_pass = checks[0][1] + checks[1][1] + checks[2][1]
    if passed >= 7:
        verdict = "Buy"
    elif passed >= 5 and val_pass >= 1:
        verdict = "Accumulate on weakness"
    elif passed >= 4:
        verdict = "Hold"
    else:
        verdict = "Reduce / Avoid"
    if val_pass == 0 and passed >= 4 and checks[6][1]:
        verdict = "Hold (solid business, price already discounts it)"
    if loss_maker and verdict in ("Buy", "Accumulate on weakness") and not net_cash > 0:
        verdict = "Hold (speculative: cash-burning and net debt)"

    # =================== page ===================
    L = []
    w = L.append
    notes_p = HERE / "notes" / f"{T}.md"
    notes = notes_p.read_text() if notes_p.exists() else "_No qualitative notes yet._"
    w(f"# {NAME} ({T}) — Deep Dive\n")
    w(f"*Prices as of the **{ASOF:%a %d %b %Y}** close · data pulled {R['fetched_utc']} · refreshed weekly · "
      f"[methodology](../../methodology.md)*\n")
    w('!!! warning "Not investment advice"\n    Educational analysis built from public data (Yahoo Finance, Kenneth French Data Library) '
      'and explicit model assumptions. Numbers update automatically; the qualitative notes are dated.\n')
    if C.get("net_cash_reason"):
        w(f'!!! note "Balance-sheet adjustment"\n    {C["net_cash_reason"]}\n')
    if C.get("data_warning"):
        w(f'!!! danger "Data caveat"\n    {C["data_warning"]}\n')
    w(f'!!! abstract "Verdict: {verdict} — {passed}/{len(checks)} checks pass"\n')
    prof = ("profitable on an owner-FCF basis" if not cash_burner else
            "profitable at the operating line but free-cash-flow negative after capex and stock compensation" if not loss_maker else
            "not yet free-cash-flow positive after stock compensation")
    bsheet = f"net cash of USD {bn(net_cash)}" if net_cash > 0 else f"net debt of USD {bn(-net_cash)}"
    grow = (f"consensus revenue of {bn(rev0)} for FY{FY0} and {bn(rev1['avg'])} for FY{FY0 + 1} ({pct(rev1['avg'] / rev0 - 1, 0, True)})"
            if not est_note else f"TTM revenue of {bn(rev_ttm)} ({pct(rev_yoy, 0, True)} y/y)")
    if scen["Base"]["v"] >= P:
        val_s = (f"At {usd(P)} the base-case DCF of {usd(scen['Base']['v'], 2 if P < 20 else 0)} ({pct(scen['Base']['up'], 0, True)}) sits above the price; "
                 f"on the base growth path the price needs only a **{pct(need_m, 0)} owner-FCF margin** (base case {pct(base['fcf_margin'], 0)}).")
    else:
        val_s = (f"At {usd(P)} the market prices in **{pct(need_g, 0)} a year revenue growth after FY{FY0 + 1}** (fading to {pct(GT, 0)}) at a "
                 f"{pct(base['fcf_margin'], 0)} owner-FCF margin, or a **{pct(need_m, 0)} margin** on the base growth path. "
                 f"The base-case DCF is {usd(scen['Base']['v'], 2 if P < 20 else 0)} ({pct(scen['Base']['up'], 0, True)}).")
    w(f"    {NAME} is {prof}, with {bsheet} and {grow}. {val_s}"
      + (f" Cash runway at the current burn: about **{runway:.1f} years**." if np.isfinite(runway) else ""))
    if sig:
        w(f"    Our hourly signal model currently rates it **{sig[0]}** (score {sig[1]:+.2f}).")
    w("")
    w("| Check | Pass | Evidence |\n|---|:---:|---|")
    for c_, ok, evd in checks:
        w(f"| {c_} | {'✅' if ok else '❌'} | {evd} |")
    w("")

    w("## Snapshot\n")
    w("| Metric | Value | Metric | Value |\n|---|---|---|---|")
    snap = [("Price", usd(P)), ("Market cap", "USD " + bn(mcap)), ("Enterprise value", "USD " + bn(ev)), ("Net cash", "USD " + bn(net_cash)),
            ("52-week range", f"{lo52:,.2f} – {hi52:,.2f}"), ("From 52w high", pct(P / hi52 - 1, 1, True)),
            ("Trailing P/E (GAAP)", mult(pe_tr)), (f"Forward P/E FY{FY0} / FY{FY0 + 1}", f"{mult(pe_f0)} / {mult(pe_f1)}"),
            ("PEG (FY+1 P/E ÷ EPS growth)", num(peg)), ("EV / TTM revenue", mult(ev / rev_ttm)),
            ("TTM revenue", "USD " + bn(rev_ttm)), ("TTM FCF / after SBC", f"{bn(fcf_ttm)} / {bn(fcf_ttm - sbc_ttm)}"),
            ("Beta vs SPY (raw / Blume)", f"{beta:.2f} / {beta_blume:.2f}"), ("Realized vol 20d / 1y", f"{pct(rv20, 0)} / {pct(rv252, 0)}"),
            ("Analysts / mean target", f"{n_an} / {usd(tgt['Mean'], 0)} ({pct(exp_an, 1, True)})"),
            ("Next earnings", str(next_earn) if next_earn else "n/a"),
            ("Shares out (diluted proxy)", f"{shares / 1e9:.3f}bn"), ("Short interest (% float)", pct(fnum(info.get('shortPercentOfFloat')), 1)),
            ("Sector ETF benchmark", BENCH), ("Cash runway (cash ÷ FCF burn)", f"{runway:.1f} years" if np.isfinite(runway) else "n/a (FCF positive)"),
            ("Institutions / insiders", f"{pct(fnum(info.get('heldPercentInstitutions')), 0)} / {pct(fnum(info.get('heldPercentInsiders')), 2)}"),
            ("Dividend", "none" if not info.get("dividendRate") else usd(fnum(info.get("dividendRate"))))]
    for i in range(0, len(snap), 2):
        a_, b_ = snap[i], snap[i + 1]
        w(f"| {a_[0]} | {a_[1]} | {b_[0]} | {b_[1]} |")
    w("")

    w("## 1. Price over time\n")
    w("![Price history](charts/price_history.png)\n")
    w("| Ticker | " + " | ".join(p_[0] for p_ in periods) + " | 10Y CAGR |")
    w("|---|" + "---:|" * (len(periods) + 1))
    for sym, r, cg in ret_rows:
        nm_ = f"**{sym}**" if sym == T else sym
        w(f"| {nm_} | " + " | ".join(pct(v, 0, True) for v in r) + f" | {pct(cg, 1)} |")
    w(f"\nLargest one-day moves in the last 5 years: " +
      ", ".join(f"{d:%d %b %Y} {pct(np.exp(dlog.loc[d]) - 1, 1, True)}" for d in big.index) + ".\n")

    w("## 2. Return and risk (ch.5)\n")
    w(f"Statistics use the {n} complete months to {END:%b %Y}.\n")
    w("| Statistic | Value | What it means |\n|---|---:|---|")
    w(f"| Arithmetic mean (annualized) | {pct(am)} | Expected one-period return if the past repeats |")
    w(f"| Geometric mean (CAGR) | {pct(gm)} | What a buy-and-hold investor actually earned; the gap ≈ σ²/2 is volatility drag |")
    w(f"| Standard deviation (annualized) | {pct(sd)} | {sd / spy_sd:.1f}× the S&P 500's {pct(spy_sd)} |")
    w(f"| Skewness / excess kurtosis | {sk:.2f} / {ku:.2f} | {'Right-skewed' if sk > 0 else 'Left-skewed'}, {'fat' if ku > 0 else 'thin'} tails vs normal |")
    w(f"| 5% monthly VaR: historical / normal | {pct(var5)} / {pct(var5n)} | One month in 20 loses at least this much |")
    w(f"| 5% monthly expected shortfall | {pct(es5)} | Average loss in that worst 5% of months |")
    w(f"| Sharpe ratio (S&P 500) | {sharpe:.2f} ({spy_sharpe:.2f}) | Excess return per unit of total risk |")
    w(f"| Sortino ratio | {sortino:.2f} | Excess return per unit of downside risk |")
    w(f"| Max drawdown, 5y | {pct(maxdd)} (trough {maxdd_date:%b %Y}) | Currently {pct(cur_dd, 1)} from the peak |")
    w("\n![Risk](charts/risk.png)\n")

    w("## 3. Index model, CAPM and factors (ch.8–10)\n")
    w("| Regression (60m excess returns) | Alpha (ann.) | t(α) | Beta | t(β) | R² | Residual σ |\n|---|---:|---:|---:|---:|---:|---:|")
    for b, v in im.items():
        w(f"| vs {b} | {pct(v['alpha'], 1, True)} | {v['alpha_t']:.2f} | {v['beta']:.2f} | {v['beta_t']:.2f} | {v['r2']:.2f} | {pct(v['resid'])} |")
    w(f"\n- **Risk decomposition (ch.8):** systematic variance β²σ²(M) = {pct(sys_var)} vs firm-specific σ²(e) = {pct(firm_var)}, "
      f"so **{pct(sys_var / (sys_var + firm_var), 0)} of the risk is market-driven** and {pct(firm_var / (sys_var + firm_var), 0)} is diversifiable.")
    w(f"- **CAPM required return (ch.9):** k = r_f + β × MRP = {pct(rf, 2)} + {beta:.2f} × {pct(MRP)} = **{pct(k_raw)}** "
      f"(Blume-adjusted β {beta_blume:.2f} → **{pct(k_blume)}**, used as the DCF discount rate).")
    w(f"- **Historical alpha** of {pct(jensen, 1, True)} a year has a t-stat of {im['SPY']['alpha_t']:.2f}: "
      f"{'statistically significant' if abs(im['SPY']['alpha_t']) > 2 else 'not statistically distinguishable from zero'} (ch.11: past alpha is a weak guide).")
    if ff is not None:
        fac = ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "Mom"]
        style = []
        style.append("small-cap" if ff["SMB"] > 0.2 else "large-cap" if ff["SMB"] < -0.2 else "size-neutral")
        style.append("value" if ff["HML"] > 0.2 else "growth" if ff["HML"] < -0.2 else "style-neutral")
        style.append("low-profitability" if ff["RMW"] < -0.2 else "high-profitability" if ff["RMW"] > 0.2 else "average-profitability")
        w(f"- **Fama-French 5 factors + momentum (ch.10, {ff['months']} months to {ff['last']:%b %Y}):** R² {ff['R2']:.2f}, alpha {pct(ff['ff_alpha_ann'], 1, True)} (t {ff['ff_alpha_t']:.2f}). Loadings: " +
          ", ".join(f"{f_} {ff[f_]:+.2f} (t {ff[f_ + '_t']:.1f})" for f_ in fac) +
          f". The loadings describe a **{', '.join(style)}** return profile (SMB > 0 small-cap, HML < 0 growth, RMW < 0 weak profitability, CMA < 0 aggressive investment).")
    w("\n![Rolling beta](charts/rolling_beta.png)\n")

    w("## 4. Portfolio fit: allocation and diversification (ch.6–7)\n")
    w(f"Correlation of monthly returns with {T} ({n}m): " + ", ".join(f"{c_} {v:.2f}" for c_, v in corr.items()) + ".\n")
    w(f"- A 50/50 mix with SPY would have had volatility of {pct(sd_5050)} vs {pct(0.5 * sd + 0.5 * spy_sd)} for the weighted average of the two, a diversification benefit because ρ = {rho:.2f} < 1.")
    w(f"- **Optimal risky share y\\* = [E(r) − r_f] / (A·σ²)**, holding {T} alone against T-bills (σ = {pct(sd)}):\n")
    w("| Risk aversion A | y\\* with CAPM E(r) | y\\* with E(r) + Street α |\n|---|---:|---:|")
    for A, y1, y2 in alloc:
        w(f"| {A} | {pct(y1, 0)} | {pct(y2, 0)} |")
    w(f"\nEven a risk-tolerant investor would put only a modest share in a single stock this volatile. Ch.7–8 say the efficient "
      f"choice is the market portfolio plus a Treynor-Black tilt (section 9), not a concentrated position.\n")

    w("## 5. Financial statements: quality of earnings (ch.19)\n")
    if qtab:
        w("| Quarter | Revenue | Q/Q | Gross m. | Op. m. (GAAP) | Net m. | R&D % | SBC % | Diluted EPS | FCF | FCF m. | DSO (days) | DIO (days) |")
        w("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        for i, q in enumerate(qtab):
            qq = q["rev"] / qtab[i - 1]["rev"] - 1 if i else np.nan
            w(f"| {pd.Timestamp(q['q']):%Y-%m} | {bn(q['rev'])} | {pct(qq, 0, True)} | {pct(q['gm'])} | {pct(q['opm'])} | {pct(q['nm'])} | {pct(q['rd'])} | "
              f"{pct(q['sbc'])} | {num(q['eps'])} | {bn(q['fcf'], 2)} | {pct(q['fcfm'])} | {num(q['dso'], 0)} | {num(q['dio'], 0)} |")
    w("\n![Fundamentals](charts/fundamentals.png)\n")
    if est_note:
        w(f"*Note: {est_note}.*\n")
    drv = max([("net margin", dupont["nm"] / 0.10 if np.isfinite(dupont["nm"]) else 0), ("asset turnover", dupont["at"] / 0.8 if np.isfinite(dupont["at"]) else 0),
               ("leverage", dupont["lev"] / 2.0 if np.isfinite(dupont["lev"]) else 0)], key=lambda x: x[1])[0]
    w(f"- **DuPont, TTM:** ROE {pct(dupont['roe'])} = net margin {pct(dupont['nm'])} × asset turnover {num(dupont['at'])} × leverage {num(dupont['lev'])}. "
      + ("Net income is negative, so ROE is negative; the business is not yet earning its cost of equity." if not dupont['nm'] > 0 else
         f"Relative to typical levels (10% margin, 0.8 turnover, 2.0 leverage) the biggest driver is **{drv}**"
         + (", so part of the ROE comes from financial risk rather than operations." if drv == "leverage" else ".")))
    if np.isfinite(amort_ttm) and amort_ttm > 0.02 * abs(ni_ttm):
        w(f"- **GAAP vs economic earnings:** TTM amortization of acquired intangibles was {bn(amort_ttm)}, a non-cash charge that depresses GAAP EPS, "
          f"so the trailing P/E ({mult(pe_tr, 0)}) overstates the multiple; cash flow tells the clearer story.")
    w(f"- **Cash conversion:** TTM operating cash flow {bn(ocf_ttm)} vs net income {bn(ni_ttm)}. The accruals ratio of {pct(accruals, 1, True)} of assets is "
      f"{'negative (cash earnings exceed accounting earnings), a sign of high-quality earnings' if accruals < 0 else 'positive, so watch the earnings quality'}.")
    w(f"- **Stock-based compensation** of {bn(sbc_ttm)} TTM ({pct(sbc_ttm / rev_ttm)} of revenue) is a real cost to shareholders. The valuation below uses FCF *after* SBC "
      f"(owner FCF margin {pct(ownr_m)}). Buybacks were {bn(-buyback_ttm if np.isfinite(buyback_ttm) else np.nan)}; share count changed {pct(dil_1y, 1, True)} over the year.")
    if np.isfinite(dol):
        w(f"- **Operating leverage (ch.17):** degree of operating leverage {num(dol)} (last two fiscal years): each 1% change in sales moved EBIT by about {num(dol, 1)}%.")
    else:
        w("- **Operating leverage (ch.17):** not meaningful: EBIT was negative or sales barely moved between the last two fiscal years.")
    w("")

    dp = 2 if P < 20 else 0
    w("## 6. Valuation (ch.18)\n")
    w("![Valuation](charts/valuation.png)\n")
    w(f"**Multiples vs peers** (Yahoo Finance, TTM and next-year; peers chosen by hand in config.json):\n")
    if len(peers_tab) > 1:
        cols = [("forward_pe", "Fwd P/E", "x"), ("ps_ratio_ttm", "P/S TTM", "x"), ("ev_ebitda_ttm", "EV/EBITDA", "x"), ("fcf_yield", "FCF yield", "%"),
                ("revenue_growth_fy", "Rev. growth FY", "%"), ("gross_margin", "Gross m.", "%"), ("ebit_margin", "EBIT m.", "%"), ("roe_ttm", "ROE TTM", "%"), ("analyst_target_upside", "Target upside", "%")]
        w("| Ticker | " + " | ".join(c_[1] for c_ in cols) + " |\n|---|" + "---:|" * len(cols))
        for t_ in [T, *[p_ for p_ in PEERS if p_ in peers_tab.index]]:
            if t_ not in peers_tab.index:
                continue
            rr = peers_tab.loc[t_]
            w(f"| {'**' + t_ + '**' if t_ == T else t_} | " + " | ".join(
                (f"{fnum(rr[c_]):.1f}x" if u == "x" else pct(fnum(rr[c_]), 0)) if np.isfinite(fnum(rr[c_])) else "n/a" for c_, _, u in cols) + " |")
        med = peers_tab.drop(index=T)[[c_[0] for c_ in cols]].apply(pd.to_numeric, errors="coerce").median()
        w("| *Peer median* | " + " | ".join((f"{med[c_]:.1f}x" if u == "x" else pct(med[c_], 0)) for c_, _, u in cols) + " |")
    if eps1 > 0:
        w(f"\n**Growth embedded in the price (PVGO).** With FY{FY0 + 1}E EPS of {usd(eps1)} and k = {pct(k)}, the no-growth value E₁/k is "
          f"{usd(eps1 / k)}. **PVGO = {usd(pvgo)}, which is {pct(pvgo / P, 0)} of the price**"
          + (f", so most of the value depends on growth beyond FY{FY0 + 1}." if pvgo / P > 0.5 else ", so the price leans mostly on existing earnings power." if pvgo > 0 else
             ": the price is *below* the no-growth value, so the market expects earnings to shrink or doubts their durability.")
          + f" No-growth P/E = 1/k = {nogrowth_pe:.1f}x vs the actual {mult(pe_f1)}.\n")
    else:
        w(f"\n**Growth embedded in the price (PVGO).** Next-year EPS is expected to be negative ({usd(eps1)}), so the whole price is PVGO: "
          f"it rests entirely on future profits that do not exist yet.\n")
    w(f"**Constant-growth check.** On TTM owner FCF, P = FCF₁/(k − g) implies a perpetual growth rate of **{pct(implied_g)}**, "
      f"{'above' if implied_g > GT else 'below'} the {pct(GT, 0)} long-run nominal-GDP ceiling the book recommends for g.\n")
    if xprem:
        w(f"*The discount rate includes an extra {pct(xprem, 1)} premium on top of CAPM: {C.get('risk_premium_reason', 'company-specific risk')}.*\n")
    w(f"**Scenario DCF (owner FCF, k = {pct(k)}, terminal g = {pct(GT, 0)}).** The revenue path is FY{FY0} ({bn(rev0)}), then the FY{FY0 + 1} "
      f"low/avg/high estimate, then growth that fades linearly to {pct(GT, 0)} over {CFG['fade_years']} years. Owner-FCF margin ramps from today's {pct(ownr_m)} "
      f"to the scenario margin over {ramp_years} years. Scenario assumptions are {scen_src}.\n")
    w(f"| Scenario | FY{FY0 + 1} revenue | Growth after | Owner-FCF margin | FY{scen['Base']['yr_end']} revenue | Terminal value share | Value / share | vs price |")
    w("|---|---:|---:|---:|---:|---:|---:|---:|")
    for nm_, v in scen.items():
        w(f"| {nm_} | {bn(v['rev_next'])} | {pct(v['g'], 0)} | {pct(v['m'], 0)} | {bn(v['rev_end'], 0)} | {pct(v['tv_share'], 0)} | **{usd(v['v'], dp)}** | {pct(v['up'], 0, True)} |")
    if dil:
        w(f"\nIf the {dil['label']} fully vests, per-share values fall by about {pct(1 - shares / (shares + dil['shares']), 1)} "
          f"(base case {usd(scen['Base']['v'] * shares / (shares + dil['shares']), 0)}).\n")
    w(f"\n**Reverse DCF: what today's price assumes.** On the base revenue path the price requires a steady-state owner-FCF margin of **{pct(need_m, 0)}**. "
      f"At the base {pct(base['fcf_margin'], 0)} margin it requires "
      + (f"**{pct(need_g, 0)} growth after FY{FY0 + 1}**" if np.isfinite(need_g) else "revenue to *shrink* by more than 20% a year after FY" + str(FY0 + 1))
      + (f", or a discount rate of **{pct(need_k, 1)}** (vs the model's {pct(k)})." if np.isfinite(need_k) else ".") + "\n")
    w(f"**Sensitivity:** base revenue path, value per share by discount rate (rows) and steady-state owner-FCF margin (columns).\n")
    w("| k \\ margin | " + " | ".join(pct(m, 0) for m in m_grid) + " |\n|---|" + "---:|" * len(m_grid))
    for kk, rw in zip(k_grid, sens):
        w(f"| {pct(kk)} | " + " | ".join(f"{v:,.{dp}f}" for v in rw) + " |")
    if eps1 > 0:
        w(f"\n**Earnings-multiple cross-check:** FY{FY0 + 1}E EPS {usd(eps1)} × " + ", ".join(f"{m}x = {m * eps1:,.{dp}f}" for m in pe_grid) +
          f". The price implies {mult(pe_f1, 0)}. The FY{FY0 + 1} EPS range across analysts is {num(cell(ee, '+1y', 'low'))}–{num(cell(ee, '+1y', 'high'))}.\n")

    w("## 7. Market efficiency and earnings reactions (ch.11)\n")
    if events:
        w(f"Market-model abnormal returns (vs SPY, estimated over the 250 days before each event) for the last {len(events)} releases:\n")
        w("| Announced | Reaction day | EPS vs est. | Surprise | AR day 0 | CAR [−1,+1] | Drift CAR [+2,+20] |\n|---|---|---|---:|---:|---:|---:|")
        for e in events[::-1]:
            w(f"| {e['date']} | {e['react']} | {num(fnum(e['eps']))} vs {num(fnum(e['est']))} | {num(fnum(e['surp']), 1)}% | {pct(e['ar0'], 1, True)} | {pct(e['car11'], 1, True)} | {pct(e['drift'], 1, True)} |")
        w(f"\n- Average absolute day-0 abnormal move: **{pct(mean_abs_ar0, 1)}**. The sign of the EPS surprise matched the sign of the reaction "
          f"{pct(hit, 0)} of the time, which is " + ("close to a coin flip: guidance and commentary matter more than the headline EPS beat." if hit < 0.7 else "fairly consistent: the headline surprise does move the stock."))
        w(f"- Post-announcement drift: the correlation between the initial reaction and the next-20-day drift is {num(drift_corr)}. "
          f"{'A positive value hints at under-reaction (PEAD, ch.11–12), though with only ' + str(len(events)) + ' events the evidence is weak.' if drift_corr > 0.3 else 'There is no reliable post-earnings drift, consistent with semi-strong efficiency.'}")
        w("\n![Event study](charts/event_study.png)\n")

    w("## 8. Technicals and behavioural signals (ch.12)\n")
    w("| Indicator | Value | Read |\n|---|---:|---|")
    w(f"| Price vs 50-day / 200-day MA | {pct(P / ma50.iloc[-1] - 1, 0, True)} / {pct(P / ma200.iloc[-1] - 1, 0, True)} | {'Golden cross (50 > 200)' if ma50.iloc[-1] > ma200.iloc[-1] else 'Death cross (50 < 200)'} |")
    w(f"| RSI(14) | {rsi:.0f} | {'Overbought (>70)' if rsi > 70 else 'Oversold (<30)' if rsi < 30 else 'Neutral'} |")
    w(f"| 12-1 month momentum | {pct(mom, 0, True)} | {'Strong' if mom > 0.3 else 'Positive' if mom > 0 else 'Negative'} (Jegadeesh-Titman) |")
    w(f"| 6-month relative strength vs {BENCH} | {pct(rel6, 0, True)} | {'Leader' if rel6 > 0 else 'Laggard'} |")
    if np.isfinite(ins_sales):
        w(f"| Insider sales / purchases, last 6m | USD {bn(ins_sales, 2)} / USD {bn(ins_buys, 2)} | {'Net selling, often planned 10b5-1 sales; insider *buying* is the informative signal (ch.11)' if ins_sales > ins_buys else 'Net insider buying: an informative signal (ch.11)' if ins_buys > 0 else 'No meaningful insider activity'} |")
    if ud90 is not None and len(ud90):
        raises = (ud90["priceTargetAction"] == "Raises").sum()
        w(f"| Analyst actions, last 90 days | {len(ud90)} actions, {raises} target raises | {'Targets chasing the price is a sign of anchoring and herding (ch.12)' if raises > len(ud90) / 2 else 'Few target raises: the Street is not chasing the stock'} |")
        below = (pd.to_numeric(ud90["currentPriceTarget"], errors="coerce") < P).mean()
        w(f"| Recent targets below current price | {pct(below, 0)} | {'Upside in the consensus has been used up' if below > 0.4 else 'Most targets still sit above the price'} |")
    if rec0 is not None:
        w(f"| Ratings (strong buy / buy / hold / sell) | {rec0['strongBuy']} / {rec0['buy']} / {rec0['hold']} / {rec0['sell'] + rec0['strongSell']} | {'Near-unanimous bullishness is crowded positioning' if (rec0['strongBuy'] + rec0['buy']) > 0.8 * max(1, rec0[['strongBuy', 'buy', 'hold', 'sell', 'strongSell']].sum()) else 'Mixed views: less crowded positioning'} |")
    if trend is not None and revs is not None and np.isfinite(cell(trend, "+1y", "90daysAgo")) and np.isfinite(cell(revs, "+1y", "upLast30days")):
        w(f"| FY{FY0 + 1} EPS estimate: now vs 90 days ago | {num(fnum(trend.loc['+1y', 'current']))} vs {num(fnum(trend.loc['+1y', '90daysAgo']))} | "
          f"{pct(cell(trend, '+1y', 'current') / cell(trend, '+1y', '90daysAgo') - 1 if cell(trend, '+1y', '90daysAgo') else np.nan, 0, True)} revision; up/down revisions in the last 30 days: {int(fnum(revs.loc['+1y', 'upLast30days']))}/{int(fnum(revs.loc['+1y', 'downLast30days']))} |")
    w("")

    w("## 9. Treynor-Black: should an active manager overweight it? (ch.27)\n")
    w("| Step | Value |\n|---|---:|")
    w(f"| Analyst-implied 12m return (mean target / price − 1) | {pct(exp_an, 1, True)} |")
    w(f"| CAPM 1-year required return (raw β) | {pct(capm_1y)} |")
    w(f"| Raw alpha | {pct(a_raw, 1, True)} |")
    w(f"| Minus average analyst optimism bias (Top-30 cross-section) | {pct(-bias, 1, True)} |")
    w(f"| Shrunk alpha (× {SHRINK}, for forecast imprecision) | **{pct(a_sh, 1, True)}** |")
    w(f"| Residual variance σ²(e) | {pct(im['SPY']['resid'] ** 2)} |")
    w(f"| Initial active weight w₀ = [α/σ²(e)] / [E(R_M)/σ²_M] | {pct(w0, 1, True)} |")
    w(f"| Beta-adjusted weight w\\* = w₀ / [1 + (1 − β)w₀] | **{pct(w_star, 1, True)}** |")
    w(f"\n{'A negative weight means an active manager would **underweight** it relative to the index.' if w_star < 0 else 'A positive weight means an active manager would hold **more** than its index weight.'}"
      + (f" The weekly Top-30 pipeline, which uses the same method, gives {pct(fnum(xl_row('TreynorBlack_Ch27', T)['final_weight_in_risky_portfolio']), 1, True)} "
         "in the combined 30-stock active portfolio." if xl_row('TreynorBlack_Ch27', T) is not None else "") + "\n")

    w("## 10. Options market view (ch.20–21)\n")
    if len(opt):
        w("![IV term structure](charts/iv_term.png)\n")
        w("| Expiry | Days | ATM IV | Implied ±1σ move to expiry | 90% put − 110% call IV (skew) |\n|---|---:|---:|---:|---:|")
        for _, o in opt.iterrows():
            w(f"| {o['exp']} | {o['T'] * 365.25:.0f} | {pct(o['atm'], 0)} | ±{pct(o['move'], 1)} (±{P * o['move']:,.{dp}f}) | {pct(o['skew'], 1, True)} |")
        if ev_move:
            w(f"\n- **Earnings-implied move:** the jump in variance from the {ev_move['pre']} expiry (IV {pct(ev_move['iv_pre'], 0)}) to {ev_move['post']} "
              f"(IV {pct(ev_move['iv_post'], 0)}) prices an earnings-day move of **±{pct(ev_move['sd'], 1)} (1σ)**, or about ±{pct(ev_move['mad'], 1)} in absolute terms "
              f"(≈ ±{P * ev_move['mad']:,.{dp}f}). Compare the historical average absolute reaction of {pct(mean_abs_ar0, 1) if events else 'n/a'} in section 7.")
        near = opt.iloc[(opt["T"] - 30 / 365).abs().argsort()[:1]].iloc[0]
        w(f"- **Implied vs realized:** the ~1-month ATM IV is {pct(near['atm'], 0)} vs realized {pct(rv20, 0)} (20d) / {pct(rv60, 0)} (60d) / {pct(rv252, 0)} (1y). "
          f"{'Options are cheap relative to recent realized volatility, so buying protection is relatively inexpensive.' if near['atm'] < rv60 else 'Options are rich relative to realized volatility, which favours premium sellers (covered calls, cash-secured puts).'}")
        w(f"- **Put-call parity (ch.20):** at the ATM strike for {near['exp']}, C − P − (S − PV(K)) = {near['parity']:+.2f} per share. "
          f"{'Close to zero, as parity requires.' if abs(near['parity']) < 0.01 * P else 'A small gap reflects bid/ask spreads, the hard-to-borrow cost and early-exercise value of American options.'}")
        if not live_quotes:
            w("- *Quotes were unavailable when the data was pulled (outside market hours), so implied vols use each contract's last trade price. "
              "Treat them as approximate; illiquid strikes can be stale.*")
        if cc_rows:
            cc = pd.DataFrame(cc_rows)
            pick = []
            for ty, g_ in cc.groupby("type"):
                for tgt_d in (0.15, 0.20, 0.25, 0.30):
                    pick.append(g_.iloc[(g_["delta"].abs() - tgt_d).abs().argsort()[:1]].index[0])
            cc = cc.loc[sorted(set(pick))].sort_values(["type", "K"])
            w(f"\n**Premium-selling menu for holders: {cc_why} ({cc['exp'].iloc[0]}), about 0.15/0.20/0.25/0.30 delta"
              + (", open interest ≥ 100" if has_oi else "") + ".**\n")
            w("| Type | Strike | Bid / Ask | Price | IV | Delta | P(expires OTM) | Distance | Yield | Annualized | OI |\n|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|")
            for _, c_ in cc.iterrows():
                ba = f"{c_['bid']:.2f} / {c_['ask']:.2f}" if c_["bid"] > 0 else "–"
                oi_s = f"{c_['oi']:,.0f}" if c_["oi"] > 0 else "–"
                w(f"| {c_['type']} | {c_['K']:,.{0 if c_['K'] >= 20 else 1}f} | {ba} | {c_['mid']:.2f} | {pct(c_['iv'], 0)} | {c_['delta']:+.2f} | {pct(c_['potm'], 0)} | "
                  f"{pct(c_['otm'], 1, True)} | {pct(c_['yld'], 2)} | {pct(c_['ann'], 0)} | {oi_s} |")
            w("\nCalls = covered calls on shares you own (yield on the share price); puts = cash-secured puts (yield on the strike). Prices are " +
              ("bid/ask mids" if live_quotes else "last trades") + " at the data pull and indicative only; check live quotes before trading.\n")
    w("")

    w("## 11. Our hourly signal model\n")
    if sig:
        w(f"The [Hourly Trade Signals](../../trade-signals/index.md) engine rates {T} **{sig[0]}** with a composite score of **{sig[1]:+.2f}** "
          f"(as of {sig_time}). It combines the de-biased analyst alpha (40%), 12-1 momentum (25%), quality (20%) and trend (15%), with a penalty when RSI exceeds 75.\n")
    else:
        w(f"{T} is not in the Top-30 signal universe.\n")

    w("## 12. Qualitative analysis: business, PEST, catalysts and risks\n")
    w(notes)
    w("\n---\n*Generated by `analyses/deep-dives/deep_dive.py`. Quantitative sections refresh weekly; the qualitative notes carry their own review date.*")
    (OUTD / "index.md").write_text("\n".join(L) + "\n")
    summ = dict(ticker=T, slug=slug, name=NAME, sector=info.get("sector"), industry=info.get("industry"), etf=BENCH, asof=str(ASOF.date()),
                price=P, mcap=mcap, verdict=verdict, passed=int(passed), n_checks=len(checks), checks=[bool(c[1]) for c in checks],
                base_dcf=scen["Base"]["v"], bear_dcf=scen["Bear"]["v"], bull_dcf=scen["Bull"]["v"], dcf_upside=scen["Base"]["up"],
                need_g=need_g, need_m=need_m, pe_f1=pe_f1, peer_fpe=med_fpe, beta=beta, beta_blume=beta_blume, k=k, sd=sd, sharpe=sharpe,
                mom=mom, rsi=rsi, vs200=P / ma200.iloc[-1] - 1, alpha_shrunk=a_sh, w_star=w_star, target_upside=exp_an, net_cash=net_cash,
                fcf_ttm=fcf_ttm, owner_margin=ownr_m, runway=runway, loss_maker=bool(loss_maker), rv252=rv252, maxdd5=maxdd,
                ret_1y=[r for sym, r, _ in ret_rows if sym == T][0][4], div_yield=fnum(info.get("dividendYield")),
                next_earn=str(next_earn) if next_earn else None, signal=sig[0] if sig else None, signal_score=sig[1] if sig else None,
                ff={k_: ff[k_] for k_ in ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "Mom", "R2"]} if ff else None)
    SUMD.mkdir(exist_ok=True)
    json.dump({k_: (None if isinstance(v, float) and not np.isfinite(v) else v) for k_, v in summ.items()}, open(SUMD / f"{T}.json", "w"), indent=1, default=float)
    print(f"{T}: wrote {OUTD / 'index.md'} | verdict {verdict} ({passed}/{len(checks)}) | base DCF {scen['Base']['v']:.0f} vs {P:.2f}")


def build_index():
    rows = [json.load(open(f)) for f in sorted(SUMD.glob("*.json"))]
    if not rows:
        return
    order = {"Buy": 0, "Accumulate on weakness": 1, "Hold": 2, "Hold (solid business, price already discounts it)": 3,
             "Hold (speculative: cash-burning and net debt)": 4, "Reduce / Avoid": 5}
    rows.sort(key=lambda r: (order.get(r["verdict"], 9), -r["passed"], r["ticker"]))
    f_ = lambda x, d=0, sg=True: pct(x if x is not None else np.nan, d, sg)
    L = ["# Stock Deep Dives\n",
         "*One page per stock, each applying the full Bodie-Kane-Marcus toolkit: return and risk statistics (ch.5), index model, CAPM and Fama-French "
         "factors (ch.8–10), capital allocation (ch.6–7), earnings quality (ch.19), DCF / reverse DCF / PVGO (ch.18), earnings event studies (ch.11), "
         "technicals (ch.12), Treynor-Black (ch.27) and the options market (ch.20–21), plus a hand-written PEST analysis. Refreshed weekly.*\n",
         '!!! warning "Not investment advice"\n    Rule-based, educational verdicts from public data. Read the individual page for the reasoning and caveats.\n',
         "## Scoreboard\n",
         "The verdict counts eight checks: base DCF ≥ price, forward P/E ≤ 1.2× peers, de-biased analyst alpha > 0, 12-1 momentum > 0, "
         "price > 200-day MA, RSI < 70, revenue growing with positive FCF, and net cash.\n",
         "| Stock | Sector | Price | Verdict | Checks | Base DCF vs price | Growth the price needs | Fwd P/E (peers) | Beta | 1Y return | Max DD 5Y | Hourly signal |",
         "|---|---|---:|---|:---:|---:|---:|---:|---:|---:|---:|---|"]
    for r in rows:
        L.append(f"| [**{r['ticker']}**]({r['slug']}/index.md) {r['name'][:28]} | {r.get('sector') or 'n/a'} | {r['price']:,.2f} | {r['verdict']} | {r['passed']}/{r['n_checks']} | "
                 f"{f_(r['dcf_upside'])} | {f_(r['need_g'], 0, False)} | {mult(r['pe_f1'] or np.nan)} ({mult(r['peer_fpe'] or np.nan)}) | {num(r['beta'] or np.nan)} | "
                 f"{f_(r['ret_1y'])} | {f_(r['maxdd5'])} | {r['signal'] or '–'} |")
    L.append(f"\n*Last rebuilt {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC. 'Growth the price needs' is the reverse-DCF revenue growth after next year at the base-case margin.*\n")
    (REPO / "docs" / "deep-dives" / "index.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    tickers = list(CFG["tickers"]) if "--all" in sys.argv or not args else [a.upper() for a in args]
    failed = []
    for t in tickers:
        try:
            run(t, offline="--offline" in sys.argv)
        except Exception as e:
            import traceback
            traceback.print_exc()
            failed.append(t)
            print(f"{t}: FAILED ({e}); the previous page, if any, is kept", flush=True)
    build_index()
    if failed:
        print("failed:", failed)
