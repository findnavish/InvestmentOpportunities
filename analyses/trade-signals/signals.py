"""Hourly trade signals for a paper model portfolio of the silicon supply chain Top 30.

Pipeline (BKM chapter references):
  live prices -> analyst-implied expected return vs CAPM hurdle (ch.9) -> de-biased, shrunk alpha (ch.27)
  + momentum / trend / RSI (ch.11-12) + quality z-score from DuPont & earnings quality (ch.19)
  -> composite score -> rating -> Treynor-Black style sizing w ~ score / sigma(e) (ch.8, 27) with name/group caps
  -> equity budget set by a SOXX 200-day trend regime (ch.6 capital allocation) -> orders vs current paper holdings.
"""
import csv, json, math, signal, warnings
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm

warnings.filterwarnings("ignore")
HERE = Path(__file__).parent
STATE = HERE / "state"
DOCS = HERE.parents[1] / "docs" / "trade-signals"
DOCS.mkdir(parents=True, exist_ok=True)
CFG = json.load(open(HERE / "config.json"))
INP = json.load(open(STATE / "model_inputs.json"))
T = INP["tickers"]
tick = list(T)
NOW = datetime.now(timezone.utc)
signal.alarm(int(CFG.get("max_runtime_sec", 600)))   # hard deadline: never hang a scheduled run on a stalled data feed

FX = {"KRW": ("KRW=X", False), "JPY": ("JPY=X", False), "HKD": ("HKD=X", False), "EUR": ("EURUSD=X", True)}
LOT = {".T": 100, ".HK": 500}  # board lots (Tokyo 100 shares, SMIC 500 shares)
EXCH = {"US": ("NYSE/Nasdaq", "America/New_York", (9, 30), (16, 0)), ".T": ("Tokyo", "Asia/Tokyo", (9, 0), (15, 30)),
        ".KS": ("Korea", "Asia/Seoul", (9, 0), (15, 30)), ".HK": ("Hong Kong", "Asia/Hong_Kong", (9, 30), (16, 0)),
        ".DE": ("Xetra", "Europe/Berlin", (9, 0), (17, 30)), ".AS": ("Euronext Amsterdam", "Europe/Amsterdam", (9, 0), (17, 30))}
US_HOLIDAYS = {"2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25", "2026-06-19", "2026-07-03", "2026-09-07",
               "2026-11-26", "2026-12-25", "2027-01-01", "2027-01-18", "2027-02-15", "2027-03-26", "2027-05-31", "2027-06-18",
               "2027-07-05", "2027-09-06", "2027-11-25", "2027-12-24"}


SHORT = {"005930.KS": "Samsung", "000660.KS": "SK hynix", "0981.HK": "SMIC", "IFX.DE": "Infineon", "8035.T": "Tokyo Electron",
         "ASM.AS": "ASMI", "6857.T": "Advantest", "6146.T": "Disco", "4063.T": "Shin-Etsu"}


def nm(t):
    return SHORT.get(t, t)


def suffix(t):
    return next((s for s in EXCH if s != "US" and t.endswith(s)), "US")


def lot(t):
    return LOT.get(suffix(t), 1)


# ---------------- data ----------------
syms = tick + ["SOXX"] + [v[0] for v in FX.values()]
hist = yf.download(syms, period="15mo", interval="1d", auto_adjust=True, progress=False, threads=True, timeout=30)["Close"]
intra = yf.download(syms, period="5d", interval="5m", auto_adjust=True, progress=False, threads=True, timeout=30)["Close"]
live = {}
for s in syms:   # latest 5-minute print (covers Yahoo's lagging daily bar); fall back to the daily close
    col = intra[s].dropna() if s in intra else pd.Series(dtype=float)
    live[s] = float(col.iloc[-1]) if len(col) else float(hist[s].dropna().iloc[-1])


def usd_per(ccy):
    if ccy == "USD":
        return 1.0
    sym, direct = FX[ccy]
    return live[sym] if direct else 1 / live[sym]


def market_open(t):
    name, tz, o, c = EXCH[suffix(t)]
    loc = NOW.astimezone(ZoneInfo(tz))
    if loc.weekday() >= 5 or not (o <= (loc.hour, loc.minute) < c):
        return False
    if suffix(t) == "US":
        return str(loc.date()) not in US_HOLIDAYS
    last_bar = hist[t].dropna().index[-1].date()   # non-US holidays: no bar for today => closed
    return last_bar == loc.date()


def series_with_live(t):
    """Daily closes with today's bar replaced (or appended) by the live price."""
    s = hist[t].dropna().copy()
    today = NOW.astimezone(ZoneInfo(EXCH[suffix(t)][1])).date()
    if s.index[-1].date() == today:
        s.iloc[-1] = live[t]
    elif abs(live[t] / s.iloc[-1] - 1) > 1e-9:
        s.loc[pd.Timestamp(today)] = live[t]
    return s


def rsi(s, n=14):
    d = s.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return float(100 - 100 / (1 + up.iloc[-1] / dn.iloc[-1]))


def z(x):
    """Rank-based normal score: robust to extreme outliers (e.g. +450% memory momentum)."""
    x = pd.Series(x, dtype=float)
    r = x.rank()
    return pd.Series(norm.ppf((r - 0.5) / r.count()), index=x.index).fillna(0)


def std(x):
    return (x - x.mean()) / x.std()


# ---------------- signals ----------------
rf, mrp = INP["rf_1y"], INP["mrp"]
rows = {}
for t in tick:
    m = T[t]
    s = series_with_live(t)
    px = live[t]
    tgt = m["target_mean"]
    up = tgt / px - 1 if tgt else np.nan
    if not (-0.6 < up < 1.5):          # stale/split-affected target -> ignore
        up = np.nan
    k = rf + (m["beta_adj"] or 1) * mrp
    rows[t] = {
        "px": px, "px_usd": px * usd_per(m["ccy"]), "up": up, "er": up + m["div_yield"], "k": k,
        "mom": s.iloc[-22] / s.iloc[-253] - 1 if len(s) > 253 else np.nan,
        "trend": px / s.iloc[-200:].mean() - 1, "rsi": rsi(s), "q": m["quality_z"], "sd_e": m["resid_sd"],
        "n": m["n_analysts"] or 0, "open": market_open(t),
    }
D = pd.DataFrame(rows).T
for c in D.columns:
    D[c] = D[c].astype(bool) if c == "open" else pd.to_numeric(D[c])
D["alpha_raw"] = D.er - D.k
bias = D.alpha_raw.mean()
conf = np.where(D.n >= CFG["min_analysts_full_weight"], 1.0, 0.5)
D["alpha"] = ((D.alpha_raw - bias) * CFG["alpha_shrink"] * conf).fillna(0)
W = CFG["score_weights"]
COMP = {"analyst α": ("alpha", W["alpha"]), "momentum": ("mom", W["momentum"]), "quality": ("q", W["quality"]), "trend": ("trend", W["trend"])}
for lbl, (col, wt) in COMP.items():
    D["c_" + col] = wt * z(D[col])
D["score"] = (std(D[["c_" + c for c, _ in COMP.values()]].sum(axis=1))
              - CFG["overbought_penalty"] * (D.rsi > CFG["overbought_rsi"]))
th = CFG["rating_thresholds"]
D["rating"] = pd.cut(D.score, [-np.inf, th["strong_sell"], th["sell"], th["buy"], th["strong_buy"], np.inf],
                     labels=["Strong Sell", "Sell", "Hold", "Buy", "Strong Buy"]).astype(str)

soxx = hist["SOXX"].dropna()
soxx_trend = live["SOXX"] / soxx.iloc[-200:].mean() - 1
bull = soxx_trend > 0
budget = CFG["equity_budget_bull"] if bull else CFG["equity_budget_bear"]

# ---------------- portfolio state ----------------
pf_path = STATE / "portfolio.json"
if pf_path.exists():
    pf = json.load(open(pf_path))
else:
    pf = {"inception": NOW.isoformat(timespec="minutes"), "start_nav": CFG["start_nav_usd"], "cash": CFG["start_nav_usd"],
          "holdings": {}, "soxx_start": live["SOXX"]}
hold = {t: pf["holdings"].get(t, 0) for t in tick}
nav = pf["cash"] + sum(hold[t] * D.at[t, "px_usd"] for t in tick)
cur_w = {t: hold[t] * D.at[t, "px_usd"] / nav for t in tick}

# ---------------- target weights ----------------
buys = D.index[D.rating.isin(["Buy", "Strong Buy"])]
holds = [t for t in D.index[D.rating == "Hold"] if hold[t] > 0]
tw = pd.Series(0.0, index=tick)
for t in holds:
    tw[t] = min(cur_w[t], CFG["max_weight_per_name"])
free = max(budget - tw.sum(), 0)
raw = (D.loc[buys, "score"] / D.loc[buys, "sd_e"]).clip(lower=0)
groups = pd.Series({t: T[t]["group"] for t in tick})
gcap = {g: max(CFG["max_weight_per_group"] - tw[[t for t in holds if groups[t] == g]].sum(), 0) for g in groups.unique()}
w = pd.Series(0.0, index=raw.index)
active, remaining = set(raw.index[raw > 0]), free
for _ in range(50):          # allocate, cap names and segments, redistribute the excess to uncapped names; leftover = cash
    if remaining < 1e-9 or not active:
        break
    r = raw[list(active)]
    w[r.index] += r / r.sum() * remaining
    over = w[w > CFG["max_weight_per_name"]]
    excess = (over - CFG["max_weight_per_name"]).sum()
    w[over.index] = CFG["max_weight_per_name"]
    active -= set(over.index)
    for g in groups[raw.index].unique():
        gi = [t for t in raw.index if groups[t] == g]
        gs = w[gi].sum()
        if gs > gcap[g] + 1e-12:
            excess += gs - gcap[g]
            w[gi] *= gcap[g] / gs
        if gs >= gcap[g] - 1e-12:
            active -= set(gi)
    remaining = excess
tw[w.index] = w

# ---------------- orders ----------------
orders, cost = [], CFG["cost_bps"] / 1e4
band_abs, band_rel = CFG["rebalance_band_abs_nav"] * nav, CFG["rebalance_band_rel_target"]
for t in tick:
    pxu, L = D.at[t, "px_usd"], lot(t)
    cur_v, tgt_v = hold[t] * pxu, tw[t] * nav
    delta = tgt_v - cur_v
    if D.at[t, "rating"] in ("Sell", "Strong Sell") and hold[t] > 0:
        qty, act = -hold[t], "SELL (exit)"
    elif t in buys and (hold[t] == 0 or abs(delta) > max(band_abs, band_rel * tgt_v)):
        qty = int(math.floor(abs(delta) / (pxu * L))) * L * (1 if delta > 0 else -1)
        act = ("BUY (new)" if hold[t] == 0 else "ADD") if qty > 0 else "TRIM"
    elif t in holds and hold[t] * pxu > CFG["max_weight_per_name"] * nav * (1 + band_rel):
        qty = -int(math.floor((cur_v - CFG["max_weight_per_name"] * nav) / (pxu * L))) * L
        act = "TRIM"
    else:
        continue
    if qty != 0:
        orders.append({"ticker": t, "action": act, "qty": qty, "px": D.at[t, "px"], "px_usd": pxu, "value_usd": qty * pxu})

# execute sells first (frees cash), then buys limited by cash; only where the listing's market is open
executed = []
for o in sorted(orders, key=lambda o: o["qty"]):
    t = o["ticker"]
    if not D.at[t, "open"]:
        o["status"] = f"Queued: {EXCH[suffix(t)][0]} closed"
        continue
    if o["qty"] > 0:
        L = lot(t)
        afford = int(math.floor(pf["cash"] / (o["px_usd"] * (1 + cost) * L))) * L
        o["qty"] = min(o["qty"], afford)
        o["value_usd"] = o["qty"] * o["px_usd"]
        if o["qty"] == 0:
            o["status"] = "Skipped: insufficient cash"
            continue
    pf["cash"] -= o["value_usd"] + abs(o["value_usd"]) * cost
    pf["holdings"][t] = pf["holdings"].get(t, 0) + o["qty"]
    if pf["holdings"][t] == 0:
        pf["holdings"].pop(t)
    o["status"] = "Executed (paper)"
    executed.append(o)
hold = {t: pf["holdings"].get(t, 0) for t in tick}
nav = pf["cash"] + sum(hold[t] * D.at[t, "px_usd"] for t in tick)
json.dump(pf, open(pf_path, "w"), indent=1)

stamp = NOW.strftime("%Y-%m-%d %H:%M UTC")
tl = STATE / "trades.csv"
new = not tl.exists()
with open(tl, "a", newline="") as fh:
    wr = csv.writer(fh)
    if new:
        wr.writerow(["time_utc", "ticker", "action", "qty", "price_local", "price_usd", "value_usd"])
    for o in executed:
        wr.writerow([stamp, o["ticker"], o["action"], o["qty"], round(o["px"], 4), round(o["px_usd"], 4), round(o["value_usd"], 2)])

navp = DOCS / "nav.json"
navh = json.load(open(navp)) if navp.exists() else []
navh.append({"t": NOW.isoformat(timespec="minutes"), "nav": round(nav / pf["start_nav"] * 100, 3),
             "soxx": round(live["SOXX"] / pf["soxx_start"] * 100, 3)})
json.dump(navh, open(navp, "w"))


# ---------------- rationale ----------------
def pct(x, d=0, sign=False):
    return "–" if pd.isna(x) else f"{x * 100:{'+' if sign else ''},.{d}f}%"


def rationale(t, o=None):
    m, r = T[t], D.loc[t]
    p = []
    if o:
        p.append(f"**{o['action']} {abs(o['qty']):,} sh** → target {pct(tw[t], 1)} of NAV (sized ∝ score ÷ σ(e), cap {pct(CFG['max_weight_per_name'])}).")
    elif r.rating in ("Buy", "Strong Buy"):
        p.append(f"Within rebalance band of target {pct(tw[t], 1)}: no trade.")
    elif r.rating == "Hold":
        p.append("Hold zone: keep any existing position, no new money." if hold[t] else "Hold zone: not owned, no entry.")
    else:
        p.append("Avoid: not owned." if not hold[t] else "Exit signalled.")
    if not pd.isna(r.up):
        p.append(f"Analyst target {fpx(t, m['target_mean'])} vs {fpx(t, r.px)} ({pct(r.up, 0, True)}, {int(r.n)} analysts); "
                 f"de-biased α {pct(r.alpha, 1, True)} vs CAPM hurdle {pct(r.k, 1)}.")
    else:
        p.append("No reliable analyst target: α set to 0.")
    p.append(f"{'Uptrend' if r.trend > 0 else 'Downtrend'} {pct(r.trend, 0, True)} vs 200-day avg; 12-1 mom {pct(r.mom, 0, True)}; RSI {r.rsi:.0f}.")
    p.append(f"Quality z {r.q:+.2f}" + (f" (ROE {pct(m['roe'])})." if m["roe"] is not None else "."))
    flags = []
    if r.rsi > CFG["overbought_rsi"]:
        flags.append("overbought (RSI penalty applied)")
    if r.rsi < 30:
        flags.append("oversold")
    if m["group"] == "Memory" or t == "005930.KS":
        if m["fwd_pe"] and m["fwd_pe"] < 9:
            flags.append(f"cyclical-peak risk: fwd P/E {m['fwd_pe']:.1f} (ch.17-18)")
    if m["implied_g"] and m["implied_g"] > 0.6:
        flags.append(f"price implies {pct(m['implied_g'])} stage-1 growth (reverse DCF)")
    if r.sd_e > 0.6:
        flags.append(f"high firm-specific risk σ(e) {pct(r.sd_e)} → smaller size")
    if flags:
        p.append("⚠️ " + "; ".join(flags) + ".")
    return " ".join(p)


# ---------------- page ----------------
def fpx(t, x):
    return f"{x:,.0f} {T[t]['ccy']}" if T[t]["ccy"] in ("KRW", "JPY") else f"{x:,.2f} {T[t]['ccy']}"


def money(x):
    return f"${x:,.0f}"


def mkt_status():
    out = []
    for sfx, (name, tz, o, c) in EXCH.items():
        rep = next((t for t in tick if suffix(t) == sfx), None)
        loc = NOW.astimezone(ZoneInfo(tz))
        out.append(f"{name} {'🟢 open' if rep and D.at[rep, 'open'] else '🔴 closed'} ({loc:%a %H:%M})")
    return " · ".join(out)


inv = nav - pf["cash"]
ret = nav / pf["start_nav"] - 1
soxx_ret = live["SOXX"] / pf["soxx_start"] - 1
order_rows = sorted(orders, key=lambda o: -abs(o["value_usd"]))
badge = {"Strong Buy": "🟢🟢 Strong Buy", "Buy": "🟢 Buy", "Hold": "⚪ Hold", "Sell": "🔴 Sell", "Strong Sell": "🔴🔴 Strong Sell"}
adm = {"Strong Buy": "success", "Buy": "success", "Hold": "note", "Sell": "failure", "Strong Sell": "failure"}


def label(t):
    return f"**{nm(t)}**<br><small>{t}</small>" if nm(t) != t else f"**{t}**<br><small>{T[t]['name']}</small>"


def drivers(t):
    """Top two score contributions plus compact risk flags."""
    c = sorted(((lbl, D.at[t, "c_" + col]) for lbl, (col, _) in COMP.items()), key=lambda x: -abs(x[1]))[:2]
    txt = " · ".join(f"{lbl} {v:+.2f}" for lbl, v in c)
    r, m = D.loc[t], T[t]
    flags = [f for f, ok in (("overbought", r.rsi > CFG["overbought_rsi"]), ("oversold", r.rsi < 30),
                             ("cycle-peak P/E", (m["group"] == "Memory") and bool(m["fwd_pe"]) and (m["fwd_pe"] or 99) < 9),
                             ("rich valuation", (m["implied_g"] or 0) > 0.6), ("high σ(e)", r.sd_e > 0.6)) if ok]
    return txt + (" · ⚠️ " + ", ".join(flags) if flags else "")


ord_md = "\n".join(
    f"| {o['action']} | {label(o['ticker'])} | {abs(o['qty']):,} | {fpx(o['ticker'], o['px'])} | "
    f"{money(abs(o['value_usd']))} | {o['status'].replace('Queued: ', 'Queued · ')} | {drivers(o['ticker'])} |" for o in order_rows) \
    or "| – | No trades this hour | | | | | All positions are within their rebalance bands. |"

ordmap = {o["ticker"]: o for o in orders}
sig = D.sort_values("score", ascending=False)
sig_md = "\n".join(
    f"| {badge[r.rating]} | {r.score:+.2f} | {label(t)} | {fpx(t, r.px)} | {pct(r.up, 0, True)} | {pct(r.alpha, 1, True)} | "
    f"{pct(r.mom, 0, True)} | {pct(r.trend, 0, True)} | {r.rsi:.0f} | {r.q:+.2f} | {pct(hold[t] * r.px_usd / nav, 1)} → {pct(tw[t], 1)} | "
    f"{(ordmap[t]['action'].split(' ')[0] + ' ' + format(abs(ordmap[t]['qty']), ',')) if t in ordmap else '–'} | {drivers(t)} |"
    for t, r in sig.iterrows())
why_md = "\n\n".join(
    f'??? {adm[r.rating]} "{nm(t)} ({t}) — {badge[r.rating]}, score {r.score:+.2f}"\n    {rationale(t, ordmap.get(t))}'
    for t, r in sig.iterrows())

pos = [(t, hold[t]) for t in tick if hold[t]]
pos_md = "\n".join(f"| {t} | {T[t]['name']} | {q:,} | {fpx(t, D.at[t, 'px'])} | {money(q * D.at[t, 'px_usd'])} | {pct(q * D.at[t, 'px_usd'] / nav, 1)} | {D.at[t, 'rating']} |"
                   for t, q in sorted(pos, key=lambda x: -x[1] * D.at[x[0], 'px_usd'])) or "| – | Portfolio is all cash | | | | | |"

tr = pd.read_csv(tl) if tl.exists() else pd.DataFrame()
tr_md = "\n".join(f"| {r.time_utc} | {r.action} | {r.ticker} | {int(r.qty):,} | {r.price_local:,.2f} | {money(abs(r.value_usd))} |"
                  for r in tr.tail(25).iloc[::-1].itertuples()) if len(tr) else "| – | No trades yet | | | | |"

page = f"""---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** {stamp} ({NOW.astimezone(ZoneInfo('America/New_York')):%a %b %d, %I:%M %p ET}) · refreshes hourly · weekly model inputs as of {INP['as_of']}
**Markets:** {mkt_status()}

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **{money(nav)}** | {money(pf['cash'])} ({pct(pf['cash'] / nav)}) | {money(inv)} ({pct(inv / nav)}) | {pct(ret, 2, True)} | {pct(soxx_ret, 2, True)} | {'🟢 Risk-on' if bull else '🔴 Risk-off'} ({pct(soxx_trend, 1, True)}) | {pct(budget)} |

Inception {pf['inception'][:16].replace('T', ' ')} UTC with {money(pf['start_nav'])} of paper cash. **Scaling quantities:** multiply by (your capital ÷ {money(nav)}), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
{ord_md}

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with {CFG['cost_bps']} bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
{sig_md}

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

{why_md}

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
{pos_md}

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
{tr_md}

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \\text{{target}}/P - 1 + \\text{{dividend yield}}$ at the live price. The CAPM hurdle is $k = r_f + \\beta_{{adj}} \\times MRP$ ($r_f$ = {pct(rf, 2)}, MRP = {pct(mrp, 1)}, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently {pct(bias, 1)}) is subtracted, and the remainder is shrunk ×{CFG['alpha_shrink']} (×half again if fewer than {CFG['min_analysts_full_weight']} analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −{CFG['overbought_penalty']} penalty when RSI(14) > {CFG['overbought_rsi']}.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $({W['alpha']}\\,z_\\alpha + {W['momentum']}\\,z_{{mom}} + {W['quality']}\\,z_{{quality}} + {W['trend']}\\,z_{{trend}})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ {th['strong_buy']}, Buy ≥ {th['buy']}, Hold, Sell ≤ {th['sell']}, Strong Sell ≤ {th['strong_sell']}.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \\propto \\text{{score}}_i / \\sigma(e_i)$. This is Treynor-Black $\\alpha/\\sigma^2(e)$ with Grinold's $\\alpha = IC \\cdot \\sigma \\cdot z$. Caps: {pct(CFG['max_weight_per_name'])} per name and {pct(CFG['max_weight_per_group'])} per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is {pct(CFG['equity_budget_bull'])} of NAV when SOXX is above its 200-day average and {pct(CFG['equity_budget_bear'])} when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max({pct(CFG['rebalance_band_abs_nav'], 1)} of NAV, {pct(CFG['rebalance_band_rel_target'])} of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
"""
(DOCS / "index.md").write_text(page)
print(f"signals: NAV {nav:,.0f}, {len(orders)} orders ({len(executed)} executed), regime {'bull' if bull else 'bear'}")
