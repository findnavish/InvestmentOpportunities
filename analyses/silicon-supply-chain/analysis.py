"""Silicon supply chain analysis applying Bodie-Kane-Marcus 'Investments' (13e) methods.

Chapters applied: 5 (return/risk stats), 6-7 (capital allocation, efficient diversification), 8 (single-index model),
9 (CAPM/SML), 10/13 (Fama-French multifactor), 11-12 (momentum/technicals, EMH caveats), 17 (operating leverage,
cyclicality), 18 (DDM/PVGO/implied growth/two-stage FCF), 19 (DuPont & earnings quality), 21 (implied vs realized vol),
24 (Sharpe/Treynor/Jensen/IR/M2), 25 (currency decomposition), 27 (Treynor-Black with shrunk alphas).
"""
import json, warnings
from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.optimize import minimize
import yfinance as yf
from universe import UNIVERSE, FX

warnings.filterwarnings("ignore")
ROOT = Path(__file__).parent
DATA, OUT = ROOT / "data", ROOT / "output"
OUT.mkdir(exist_ok=True)

# ---------------- Assumptions (stated explicitly; see report) ----------------
MRP = 0.055            # forward-looking equity market risk premium (BKM ch5/9: US hist. arithmetic ~8%, forward est. lower)
G_TERMINAL = 0.04      # long-run nominal growth for terminal values (ch18: g should not exceed nominal economy growth)
ALPHA_SHRINK = 0.25    # ch27: shrink analyst-implied alphas toward 0 for forecast imprecision
FADE_YEARS = 10        # two-stage FCF: fade stage-1 growth linearly to terminal over N years
WIN = 60               # months

px = pd.read_csv(DATA / "prices_daily.csv", index_col=0, parse_dates=True).sort_index()
_patch = json.load(open(DATA / "last_us_prices.json"))
AS_OF = pd.offsets.BDay().rollback(pd.Timestamp(_patch["date"]))  # weekend runs -> last weekday session
END = (AS_OF.to_period("M") - 1).to_timestamp(how="end").normalize()  # last complete month for stat windows
px = px.loc[:AS_OF]                                   # drop next-day Asian intraday bars
if AS_OF not in px.index:
    px.loc[AS_OF] = np.nan
for t, p in _patch["prices"].items():                 # fill lagging US close for the as-of session
    if pd.isna(px.at[AS_OF, t]):
        px.at[AS_OF, t] = p
info = json.load(open(DATA / "info.json"))
stmts = json.load(open(DATA / "statements.json"))
ivs = json.load(open(DATA / "implied_vol.json"))
tick = list(UNIVERSE)

# ---------------- FX: convert to USD (ch25) ----------------
fxcache = DATA / "twd.csv"
if not fxcache.exists() or pd.read_csv(fxcache, index_col=0, parse_dates=True).index.max() < AS_OF - pd.Timedelta(days=7):
    yf.download("TWD=X", period="6y", auto_adjust=True, progress=False)["Close"].to_csv(fxcache)
twd = pd.read_csv(fxcache, index_col=0, parse_dates=True).iloc[:, 0]


def usd_per(ccy, series=False):
    """USD value of one unit of ccy (spot, or daily series)."""
    if ccy == "USD":
        return 1.0 if not series else pd.Series(1.0, index=px.index)
    if ccy == "TWD":
        s = 1 / twd
    else:
        sym, kind = FX[ccy]
        s = px[sym] if kind == "usd_per" else 1 / px[sym]
    s = s.reindex(px.index).ffill()
    return s if series else float(s.dropna().iloc[-1])


px_usd = pd.DataFrame({t: px[t] * usd_per(UNIVERSE[t][3], True) for t in tick})
fx_series = {t: usd_per(UNIVERSE[t][3], True) for t in tick if UNIVERSE[t][3] != "USD"}
for b in ("SPY", "SOXX", "ACWI"):
    px_usd[b] = px[b]
px_usd = px_usd.ffill(limit=5)

# ---------------- Price over time ----------------
last = AS_OF
px_usd = px_usd.loc[:last]


def ret_since(s, days=None, date=None):
    s = s.dropna()
    if s.empty: return np.nan
    ref = s.loc[:date] if date is not None else s.loc[:s.index[-1] - pd.Timedelta(days=days)]
    return s.iloc[-1] / ref.iloc[-1] - 1 if len(ref) else np.nan


perf = []
for t in tick + ["SPY", "SOXX", "ACWI"]:
    s, sl = px_usd[t].dropna(), px[t].dropna().loc[:last]
    row = {"ticker": t, "local_price": sl.iloc[-1], "usd_price": s.iloc[-1]}
    for lab, d in (("1M", 30), ("3M", 91), ("6M", 182), ("1Y", 365), ("3Y", 1095), ("5Y", 1826)):
        row[f"ret_{lab}_usd"] = ret_since(s, d) if (s.index[-1] - s.index[0]).days >= d - 5 else np.nan
    row["ret_YTD_usd"] = ret_since(s, date=pd.Timestamp(f"{last.year - 1}-12-31"))
    row["ret_1Y_local"] = ret_since(sl, 365)
    row["ret_5Y_local"] = ret_since(sl, 1826) if (sl.index[-1] - sl.index[0]).days >= 1820 else np.nan
    y1 = s.loc[s.index[-1] - pd.Timedelta(days=365):]
    row["52w_high_usd"], row["52w_low_usd"] = y1.max(), y1.min()
    row["pct_from_52w_high"] = s.iloc[-1] / y1.max() - 1
    row["max_drawdown_5y"] = (s / s.cummax() - 1).min()
    perf.append(row)
perf = pd.DataFrame(perf).set_index("ticker")

# ---------------- Monthly returns & risk-free (ch5) ----------------
m_px = px_usd.resample("M").last()
m_ret = m_px.pct_change().loc[:END].iloc[-WIN:]
rf_m = (px["^IRX"].resample("M").last().shift(1) / 100 / 12).reindex(m_ret.index)
ex = m_ret.sub(rf_m, axis=0)
RF_NOW = float(px["^IRX"].dropna().iloc[-1]) / 100
RF_LONG = float(px["^TNX"].dropna().iloc[-1]) / 100

stats = []
for t in tick + ["SPY", "SOXX", "ACWI"]:
    r = m_ret[t].dropna()
    e = ex[t].dropna()
    n = len(r)
    var5 = r.quantile(0.05)
    down = e[e < 0]
    stats.append({
        "ticker": t, "months": n,
        "arith_mean_ann": (1 + r.mean()) ** 12 - 1,        # EAR of arithmetic monthly mean (comparable to geo)
        "geo_mean_ann": (1 + r).prod() ** (12 / n) - 1,
        "sd_ann": r.std() * np.sqrt(12),
        "excess_mean_ann": e.mean() * 12,
        "sharpe": e.mean() / r.std() * np.sqrt(12),
        "sortino": e.mean() * 12 / (np.sqrt((down ** 2).sum() / len(e)) * np.sqrt(12)),
        "skew": r.skew(), "excess_kurtosis": r.kurt(),
        "VaR5_monthly": var5, "ES5_monthly": r[r <= var5].mean(),
        "realized_vol_1y_daily": px_usd[t].pct_change().iloc[-252:].std() * np.sqrt(252),
    })
stats = pd.DataFrame(stats).set_index("ticker")

# ---------------- Single-index model vs SPY (ch8) + CAPM/SML (ch9) ----------------
idx = []
for t in tick + ["SOXX"]:
    d = pd.concat([ex[t], ex["SPY"], ex["SOXX"], ex["ACWI"]], axis=1, keys=["y", "m", "s", "w"]).dropna()
    fit = sm.OLS(d.y, sm.add_constant(d.m)).fit()
    b = fit.params["m"]
    beta_soxx = sm.OLS(d.y, sm.add_constant(d.s)).fit().params["s"]
    beta_acwi = sm.OLS(d.y, sm.add_constant(d.w)).fit().params["w"]
    resid_var = fit.resid.var() * 12
    tot_var = d.y.var() * 12
    idx.append({"ticker": t, "alpha_ann": fit.params["const"] * 12, "alpha_t": fit.tvalues["const"],
                "beta_spy": b, "beta_t": fit.tvalues["m"], "R2": fit.rsquared,
                "resid_sd_ann": np.sqrt(resid_var), "systematic_share": b ** 2 * d.m.var() * 12 / tot_var,
                "beta_adj_blume": 2 / 3 * b + 1 / 3, "beta_soxx": beta_soxx, "beta_acwi": beta_acwi})
idx = pd.DataFrame(idx).set_index("ticker")
idx["capm_k"] = RF_LONG + idx.beta_adj_blume * MRP           # required return for valuation (ch9/18)
SIG_M = ex["SPY"].std() * np.sqrt(12)
ER_M_EX = ex["SPY"].mean() * 12

# ---------------- Fama-French 5 + Momentum (ch10/13) ----------------
def load_ff(fname):
    lines = (DATA / fname).read_text().splitlines()
    start = next(i for i, l in enumerate(lines) if l.strip().startswith(",") and "RF" in l or l.strip().startswith(",Mom") or l.strip().startswith(",Mom "))
    rows = []
    for l in lines[start + 1:]:
        p = [x.strip() for x in l.split(",")]
        if len(p[0]) != 6 or not p[0].isdigit(): break
        rows.append(p)
    cols = [c.strip() for c in lines[start].split(",")[1:]]
    df = pd.DataFrame([r[1:] for r in rows], index=pd.to_datetime([r[0] for r in rows], format="%Y%m") + pd.offsets.MonthEnd(0), columns=cols).astype(float) / 100
    return df


ff = load_ff("F-F_Research_Data_5_Factors_2x3_CSV.txt").join(load_ff("F-F_Momentum_Factor_CSV.txt"), how="inner")
ff.columns = [c.strip() for c in ff.columns]
fac = ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "Mom"]
ffres = []
for t in tick:
    d = pd.concat([m_ret[t] - ff["RF"].reindex(m_ret.index), ff[fac].reindex(m_ret.index)], axis=1).dropna()
    d.columns = ["y"] + fac
    if len(d) < 24: continue
    f = sm.OLS(d.y, sm.add_constant(d[fac])).fit()
    row = {"ticker": t, "months": len(d), "ff_alpha_ann": f.params["const"] * 12, "ff_alpha_t": f.tvalues["const"], "R2": f.rsquared}
    for k in fac:
        row[k], row[k + "_t"] = f.params[k], f.tvalues[k]
    ffres.append(row)
ffres = pd.DataFrame(ffres).set_index("ticker")
FF_LAST = ff.index[-1].strftime("%Y-%m")

# ---------------- Performance evaluation (ch24) ----------------
pe = pd.DataFrame(index=tick + ["SOXX"])
pe["sharpe"] = stats.sharpe
pe["treynor"] = stats.excess_mean_ann / idx.beta_spy
pe["jensen_alpha"] = idx.alpha_ann
pe["info_ratio"] = idx.alpha_ann / idx.resid_sd_ann
pe["M2"] = (stats.sharpe - stats.loc["SPY", "sharpe"]) * SIG_M
pe.loc["SPY", ["sharpe", "treynor", "jensen_alpha", "info_ratio", "M2"]] = [stats.loc["SPY", "sharpe"], ER_M_EX, 0, np.nan, 0]

# ---------------- Currency decomposition (ch25) ----------------
cur = []
for t, fxs in fx_series.items():
    sl = px[t].dropna().loc[:last]
    for lab, d in (("1Y", 365), ("5Y", 1826)):
        if (sl.index[-1] - sl.index[0]).days < d - 5: continue
        d0 = sl.loc[:sl.index[-1] - pd.Timedelta(days=d)].index[-1]
        rl = sl.iloc[-1] / sl.loc[d0] - 1
        rfx = fxs.loc[:last].iloc[-1] / fxs.loc[d0] - 1          # change in USD value of 1 unit of local ccy
        cur.append({"ticker": t, "window": lab, "ccy": UNIVERSE[t][3], "local_ret": rl, "fx_ret_vs_usd": rfx,
                    "usd_ret": (1 + rl) * (1 + rfx) - 1, "fx_contribution": (1 + rl) * (1 + rfx) - 1 - rl})
cur = pd.DataFrame(cur)

# ---------------- Fundamentals: DuPont & quality (ch19), operating leverage (ch17) ----------------
def stmt_vals(t, key, row, n=2):
    s = stmts.get(t, {}).get(key, {})
    dates = sorted(s, reverse=True)
    return [s[d].get(row) for d in dates[:n]], dates[:n]


def g(v, i=0):
    return v[i] if len(v) > i and v[i] is not None else np.nan


fund = []
for t in tick:
    I = info[t]
    fc = I.get("financialCurrency") or UNIVERSE[t][3]
    u_fin, u_lst = usd_per(fc), usd_per(I.get("currency") or UNIVERSE[t][3])
    rev, dts = stmt_vals(t, "inc", "Total Revenue")
    ni, _ = stmt_vals(t, "inc", "Net Income")
    pti, _ = stmt_vals(t, "inc", "Pretax Income")
    ebit, _ = stmt_vals(t, "inc", "EBIT")
    oi, _ = stmt_vals(t, "inc", "Operating Income")
    gp, _ = stmt_vals(t, "inc", "Gross Profit")
    intx, _ = stmt_vals(t, "inc", "Interest Expense")
    rnd, _ = stmt_vals(t, "inc", "Research And Development")
    ta, _ = stmt_vals(t, "bal", "Total Assets")
    eq, _ = stmt_vals(t, "bal", "Stockholders Equity")
    debt, _ = stmt_vals(t, "bal", "Total Debt")
    cash, _ = stmt_vals(t, "bal", "Cash And Cash Equivalents")
    ocf, _ = stmt_vals(t, "cf", "Operating Cash Flow")
    capex, _ = stmt_vals(t, "cf", "Capital Expenditure")
    fcf, _ = stmt_vals(t, "cf", "Free Cash Flow")
    avg_ta = np.nanmean([g(ta, 0), g(ta, 1)])
    avg_eq = np.nanmean([g(eq, 0), g(eq, 1)])
    E = g(ebit) if not np.isnan(g(ebit)) else g(oi)
    E1 = g(ebit, 1) if not np.isnan(g(ebit, 1)) else g(oi, 1)
    mcap_usd = (I.get("marketCap") or np.nan) * u_lst
    nz = lambda x: np.nan if x is None else float(x)
    fcf_ttm = nz(I.get("freeCashflow")) if I.get("freeCashflow") is not None else g(fcf)
    fcf_usd = fcf_ttm * u_fin
    rev_ttm = nz(I.get("totalRevenue")) if I.get("totalRevenue") else g(rev)
    ni_ttm = nz(I.get("netIncomeToCommon")) if I.get("netIncomeToCommon") else g(ni)
    debt_ttm, cash_ttm = nz(I.get("totalDebt")) if I.get("totalDebt") is not None else g(debt), nz(I.get("totalCash")) if I.get("totalCash") is not None else g(cash)
    ev_usd = mcap_usd + (np.nan_to_num(debt_ttm) - np.nan_to_num(cash_ttm)) * u_fin
    ebitda_ttm = nz(I.get("ebitda"))
    tpe_, pay_ = I.get("trailingPE"), I.get("payoutRatio") or 0.0
    dy = pay_ / tpe_ if tpe_ else (I.get("dividendYield") or 0) / 100
    row = {
        "ticker": t, "fiscal_year_end": dts[0] if dts else None, "fin_ccy": fc,
        "market_cap_usd_bn": mcap_usd / 1e9, "revenue_usd_bn": g(rev) * u_fin / 1e9,
        "revenue_growth_fy": g(rev) / g(rev, 1) - 1,
        "gross_margin": g(gp) / g(rev), "ebit_margin": E / g(rev), "net_margin": g(ni) / g(rev),
        "rnd_intensity": g(rnd) / g(rev), "capex_intensity": -g(capex) / g(rev),
        # 5-factor DuPont: ROE = (NI/PTI)(PTI/EBIT)(EBIT/Sales)(Sales/Assets)(Assets/Equity)
        "tax_burden": g(ni) / g(pti), "interest_burden": g(pti) / E, "asset_turnover": g(rev) / avg_ta,
        "leverage": avg_ta / avg_eq, "roe_dupont": g(ni) / avg_eq, "roa": g(ni) / avg_ta,
        "interest_coverage": E / g(intx) if g(intx) and g(intx) > 0 else np.nan,
        "debt_to_equity": g(debt) / g(eq), "net_cash_usd_bn": (g(cash) - g(debt)) * u_fin / 1e9,
        "fcf_fy_usd_bn": g(fcf) * u_fin / 1e9, "fcf_conversion_fy": g(fcf) / g(ni) if g(ni) > 0 else np.nan,
        "fcf_yield_fy": g(fcf) * u_fin / mcap_usd,
        "fcf_ttm_usd_bn": fcf_usd / 1e9, "fcf_conversion_ttm": fcf_ttm / ni_ttm if ni_ttm and ni_ttm > 0 else np.nan,
        "revenue_ttm_usd_bn": rev_ttm * u_fin / 1e9, "net_income_ttm_usd_bn": ni_ttm * u_fin / 1e9,
        "accruals_ratio": (g(ni) - g(ocf)) / avg_ta,          # ch19 earnings-quality flag (high = low quality)
        "DOL": ((E / E1 - 1) / (g(rev) / g(rev, 1) - 1)) if g(rev, 1) and abs(g(rev) / g(rev, 1) - 1) > 0.02 else np.nan,
        "fcf_yield": fcf_usd / mcap_usd,
        "ps_ratio_ttm": mcap_usd / (rev_ttm * u_fin), "pb_ratio": mcap_usd / (g(eq) * u_fin),
        "trailing_pe": I.get("trailingPE"), "forward_pe": I.get("forwardPE"),
        "ev_usd_bn": ev_usd / 1e9, "ev_ebitda_ttm": ev_usd / (ebitda_ttm * u_fin) if ebitda_ttm and ebitda_ttm > 0 else np.nan,
        "div_yield": dy, "payout": pay_,
        "roe_ttm": I.get("returnOnEquity"),
        "analyst_target_upside": (I.get("targetMeanPrice") / I.get("currentPrice") - 1) if I.get("targetMeanPrice") and I.get("currentPrice") else np.nan,
        "n_analysts": I.get("numberOfAnalystOpinions"), "rating": I.get("recommendationKey"),
    }
    fund.append(row)
fund = pd.DataFrame(fund).set_index("ticker")

# ---------------- Valuation models (ch18) ----------------
val = pd.DataFrame(index=tick)
k = idx.capm_k.reindex(tick)
val["capm_k"] = k
roe = fund.roe_ttm.astype(float).fillna(fund.roe_dupont)
b = (1 - fund.payout.astype(float)).clip(0, 1)
val["plowback_b"] = b
val["sustainable_g"] = roe * b                                          # g = ROE x b
fpe = fund.forward_pe.astype(float)
_tpe = fund.trailing_pe.astype(float)
val["forward_pe_data_flag"] = fpe > 2 * _tpe                           # e.g. unit errors in forward EPS feed
fpe = fpe.where(~val.forward_pe_data_flag, _tpe)
val["forward_pe"] = fpe
val["no_growth_pe"] = 1 / k                                             # P/E if PVGO = 0 (E1/k)
val["PVGO_share_of_price"] = 1 - 1 / (fpe * k)                          # PVGO/P = 1 - (E1/P)/k
val["model_pe_const_growth"] = np.where((k - roe * b > 0.02) & (b < 0.999), (1 - b) / (k - roe * b), np.nan)  # (1-b)/(k-ROE*b); NaN if g>=k-2%
y = fund.fcf_yield.astype(float)
val["implied_perpetual_g_from_fcf"] = np.where(y > 0, (k - y) / (1 + y), np.nan)  # P = FCF0(1+g)/(k-g)
conv = fund.fcf_conversion_fy.astype(float).fillna(fund.fcf_conversion_ttm.astype(float)).clip(0.3, 1.0).fillna(0.6)
E1_usd = fund.market_cap_usd_bn / fpe                                  # aggregate forward earnings (USD bn)
val["forward_earnings_usd_bn"] = E1_usd
val["cash_conversion_used"] = conv
g1 = val.sustainable_g.clip(0.0, 0.25)
val["stage1_growth"] = g1


def two_stage_value(cf1, g1, k, gT=G_TERMINAL, n=FADE_YEARS):
    """PV of CF1 growing at g1 fading linearly to gT by year n, then Gordon terminal value (ch18)."""
    if not (cf1 > 0) or k <= gT: return np.nan
    v, cf = 0.0, cf1
    for t in range(1, n + 1):
        if t > 1:
            cf *= 1 + g1 + (gT - g1) * (t - 2) / (n - 2)
        v += cf / (1 + k) ** t
    return v + cf * (1 + gT) / (k - gT) / (1 + k) ** n


tsv, sens = [], []
for t in tick:
    f0 = E1_usd[t] * conv[t]
    v = two_stage_value(f0, g1[t], k[t])
    tsv.append(v)
    sens.append({"ticker": t, **{f"k{dk:+.0%}_gT{gt:.0%}": two_stage_value(f0, g1[t], k[t] + dk, gt) / fund.loc[t, "market_cap_usd_bn"] - 1
                                 for dk in (-0.01, 0, 0.01) for gt in (0.03, 0.04, 0.05)}})
val["two_stage_fcf_value_usd_bn"] = tsv
val["market_cap_usd_bn"] = fund.market_cap_usd_bn
val["two_stage_upside"] = val.two_stage_fcf_value_usd_bn / val.market_cap_usd_bn - 1
from scipy.optimize import brentq
imp = {}
for t in tick:
    cf1, mc = E1_usd[t] * conv[t], val.market_cap_usd_bn[t]
    f = lambda gg: two_stage_value(cf1, gg, k[t]) - mc
    try:
        imp[t] = brentq(f, -0.3, 1.5) if cf1 > 0 else np.nan
    except ValueError:
        imp[t] = np.nan
val["implied_stage1_growth"] = pd.Series(imp)   # reverse DCF: growth (fading to gT over 10y) needed to justify price
sens = pd.DataFrame(sens).set_index("ticker")

# ---------------- Technicals & momentum (ch11-12) ----------------
tech = []
for t in tick + ["SOXX", "SPY"]:
    s = px_usd[t].dropna()
    d = s.diff()
    up, dn = d.clip(lower=0).ewm(alpha=1 / 14).mean(), (-d.clip(upper=0)).ewm(alpha=1 / 14).mean()
    mom = m_px[t].dropna()
    tech.append({"ticker": t, "mom_12_1": mom.iloc[-2] / mom.iloc[-13] - 1 if len(mom) > 13 else np.nan,
                 "px_vs_50dma": s.iloc[-1] / s.iloc[-50:].mean() - 1, "px_vs_200dma": s.iloc[-1] / s.iloc[-200:].mean() - 1,
                 "golden_cross": bool(s.iloc[-50:].mean() > s.iloc[-200:].mean()),
                 "RSI14": 100 - 100 / (1 + up.iloc[-1] / dn.iloc[-1]),
                 "rel_strength_vs_SOXX_6M": ret_since(s, 182) - ret_since(px_usd["SOXX"], 182)})
tech = pd.DataFrame(tech).set_index("ticker")

# ---------------- Options: implied vs realized vol (ch21) ----------------
opt = []
for t, v in ivs.items():
    if "call" not in v: continue
    iv = (v["call"] + v["put"]) / 2
    rv = stats.loc[t, "realized_vol_1y_daily"]
    opt.append({"ticker": t, "atm_iv": iv, "expiry": v["expiry"], "realized_vol_1y": rv, "iv_rv_ratio": iv / rv,
                "implied_1m_1sd_move": iv * np.sqrt(21 / 252)})
opt = pd.DataFrame(opt).set_index("ticker")

# ---------------- Portfolio construction (ch7, ch8 index-model covariance, ch27 Treynor-Black) ----------------
betas, rv_ = idx.beta_spy.reindex(tick), idx.resid_sd_ann.reindex(tick) ** 2
cov_im = np.outer(betas, betas) * SIG_M ** 2 + np.diag(rv_)             # Cov = b_i b_j sM^2 + diag(s2(e))
cov_im = pd.DataFrame(cov_im, index=tick, columns=tick)
corr_sample = m_ret[tick].corr()

# Analyst-implied expected return -> raw alpha vs CAPM (using short rf & market premium consistent with 1Y horizon)
er_analyst = fund.analyst_target_upside.astype(float) + fund.div_yield.astype(float)
capm_1y = RF_NOW + idx.beta_spy.reindex(tick) * MRP
alpha_raw = er_analyst - capm_1y
OPTIMISM_BIAS = alpha_raw.mean()                                       # sell-side targets are systematically optimistic
alpha_f = ((alpha_raw - OPTIMISM_BIAS) * ALPHA_SHRINK).fillna(0)       # ch27: de-bias, then shrink toward 0
tb = pd.DataFrame({"analyst_exp_return": er_analyst, "capm_1y": capm_1y, "alpha_raw": alpha_raw,
                   "alpha_debiased": alpha_raw - OPTIMISM_BIAS, "alpha_shrunk": alpha_f,
                   "resid_var": rv_, "beta": betas})
tb["alpha_over_resvar"] = tb.alpha_shrunk / tb.resid_var
tb["w_active_rel"] = tb.alpha_over_resvar / tb.alpha_over_resvar.sum()
aA = (tb.w_active_rel * tb.alpha_shrunk).sum()
bA = (tb.w_active_rel * tb.beta).sum()
s2eA = (tb.w_active_rel ** 2 * tb.resid_var).sum()
ERM = MRP
w0 = (aA / s2eA) / (ERM / SIG_M ** 2)
wA = w0 / (1 + (1 - bA) * w0)
S_M = ERM / SIG_M
IR_A = aA / np.sqrt(s2eA)
tb_summary = {"alpha_A": aA, "beta_A": bA, "resid_sd_A": np.sqrt(s2eA), "w_A0": w0, "w_A_star": wA, "w_M_star": 1 - wA,
              "Sharpe_market_ex_ante": S_M, "IR_active": IR_A, "Sharpe_optimal": np.sqrt(S_M ** 2 + IR_A ** 2),
              "sum_abs_active_weights": tb.w_active_rel.abs().sum(), "analyst_optimism_bias_removed": OPTIMISM_BIAS}
tb["final_weight_in_risky_portfolio"] = tb.w_active_rel * wA

# Long-only constrained frontier (ch7) on expected returns = CAPM + shrunk alpha, index-model covariance
mu = (capm_1y + alpha_f).values
C = cov_im.values
n = len(tick)
cons = [{"type": "eq", "fun": lambda w: w.sum() - 1}]
bnds = [(0, 0.10)] * n


def opt_port(obj):
    return minimize(obj, np.ones(n) / n, bounds=bnds, constraints=cons, method="SLSQP", options={"maxiter": 500}).x


w_gmv = opt_port(lambda w: w @ C @ w)
w_tan = opt_port(lambda w: -(w @ mu - RF_NOW) / np.sqrt(w @ C @ w))
w_eq = np.ones(n) / n
frontier = []
for target in np.linspace(w_gmv @ mu, mu.max() * 0.98, 25):
    c2 = cons + [{"type": "eq", "fun": lambda w, tg=target: w @ mu - tg}]
    r = minimize(lambda w: w @ C @ w, w_gmv, bounds=bnds, constraints=c2, method="SLSQP")
    if r.success: frontier.append((np.sqrt(r.x @ C @ r.x), target))
ports = pd.DataFrame({"GMV_longonly_cap10": w_gmv, "MaxSharpe_longonly_cap10": w_tan, "EqualWeight": w_eq}, index=tick)
port_stats = {}
for c in ports:
    w = ports[c].values
    port_stats[c] = {"exp_return": w @ mu, "sd": np.sqrt(w @ C @ w), "sharpe": (w @ mu - RF_NOW) / np.sqrt(w @ C @ w),
                     "beta": w @ betas.values}

# Capital allocation (ch6): optimal risky share y* = (E(rp)-rf)/(A sigma^2) for several risk-aversion levels
wt = ports["MaxSharpe_longonly_cap10"].values
erp_t, sd_t = wt @ mu - RF_NOW, np.sqrt(wt @ C @ wt)
cal = pd.DataFrame({"A": [2, 3, 4, 6, 8]})
cal["y_star_in_semis_portfolio"] = erp_t / (cal.A * sd_t ** 2)
cal["complete_port_exp_ret"] = RF_NOW + cal.y_star_in_semis_portfolio * erp_t
cal["complete_port_sd"] = cal.y_star_in_semis_portfolio * sd_t

# Diversification curve (ch7): equal-weight SD as function of n using average var/cov
V = m_ret[tick].cov().values * 12
avg_var, avg_cov = np.nanmean(np.diag(V)), np.nanmean(V[~np.eye(n, dtype=bool)])
div_curve = pd.DataFrame({"n": [1, 2, 5, 10, 20, 30]})
div_curve["sd_equal_weight"] = np.sqrt(avg_var / div_curve.n + (1 - 1 / div_curve.n) * avg_cov)

# ---------------- Composite scorecard ----------------
def z(s, higher_better=True):
    s = s.astype(float)
    zz = (s - s.mean()) / s.std()
    return (zz if higher_better else -zz).clip(-2.5, 2.5).fillna(0)


score = pd.DataFrame(index=tick)
score["Quality"] = (z(fund.ebit_margin) + z(fund.roe_dupont.clip(-0.5, 1.5)) + z(fund.fcf_conversion_ttm.clip(-1, 2)) + z(fund.accruals_ratio, False)) / 4
score["Valuation"] = (z(val.PVGO_share_of_price, False) + z(fund.fcf_yield) + z(val.implied_perpetual_g_from_fcf, False) + z(fpe, False)) / 4
score["Risk (low=good)"] = (z(idx.beta_spy.reindex(tick), False) + z(stats.sd_ann.reindex(tick), False) + z(perf.max_drawdown_5y.reindex(tick))) / 3
score["Momentum"] = (z(tech.mom_12_1.reindex(tick)) + z(tech.rel_strength_vs_SOXX_6M.reindex(tick))) / 2
score["Risk-adj. perf"] = (z(pe.sharpe.reindex(tick)) + z(pe.info_ratio.reindex(tick))) / 2
score["Composite"] = score[["Quality", "Valuation", "Risk (low=good)", "Momentum", "Risk-adj. perf"]].mean(axis=1)
score = score.sort_values("Composite", ascending=False)
score["Rank"] = range(1, len(score) + 1)

# ---------------- Save ----------------
meta = pd.DataFrame({"ticker": tick, "company": [UNIVERSE[t][0] for t in tick], "segment": [UNIVERSE[t][1] for t in tick],
                     "country": [UNIVERSE[t][2] for t in tick], "listing_ccy": [UNIVERSE[t][3] for t in tick]}).set_index("ticker")
assump = pd.DataFrame({"value": {"price_date": str(last.date()), "stats_window": f"{m_ret.index[0]:%Y-%m}..{m_ret.index[-1]:%Y-%m} ({WIN}m)",
                                  "rf_13w_tbill": RF_NOW, "rf_10y_treasury": RF_LONG, "market_risk_premium": MRP,
                                  "terminal_growth": G_TERMINAL, "alpha_shrink": ALPHA_SHRINK, "fade_years": FADE_YEARS,
                                  "SPY_sd_ann": SIG_M, "SPY_hist_excess_ret_ann": ER_M_EX, "FF_factors_through": FF_LAST}})
sheets = {"Assumptions": assump, "Universe": meta, "Price_Performance": perf, "Return_Risk_Ch5": stats,
          "Index_Model_CAPM_Ch8_9": idx, "FamaFrench_Ch10": ffres, "Performance_Ch24": pe, "Currency_Ch25": cur,
          "Fundamentals_DuPont_Ch19": fund, "Valuation_Ch18": val, "DCF_Sensitivity": sens, "Technicals_Ch11_12": tech,
          "Options_IV_Ch21": opt, "TreynorBlack_Ch27": tb, "TB_Summary": pd.Series(tb_summary).to_frame("value"),
          "Portfolios_Ch7": ports, "Portfolio_Stats": pd.DataFrame(port_stats), "Capital_Alloc_Ch6": cal,
          "Diversification_Ch7": div_curve, "Correlation": corr_sample, "Scorecard": score}
with pd.ExcelWriter(OUT / "Silicon_Supply_Chain_Analysis.xlsx") as xw:
    for nm, df in sheets.items():
        df.to_excel(xw, sheet_name=nm[:31])
pd.to_pickle({"sheets": sheets, "px_usd": px_usd, "m_ret": m_ret, "frontier": frontier, "mu": mu, "cov": cov_im,
              "rf": RF_NOW, "rf_long": RF_LONG, "sig_m": SIG_M}, OUT / "results.pkl")
print("saved; last price date", last.date())
