"""Charts for the silicon supply chain report."""
import warnings
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from universe import UNIVERSE

warnings.filterwarnings("ignore")
OUT = Path(__file__).parent / "output"
CH = OUT / "charts"
CH.mkdir(exist_ok=True)
R = pd.read_pickle(OUT / "results.pkl")
S = R["sheets"]
px, tick = R["px_usd"], list(UNIVERSE)
plt.rcParams.update({"figure.dpi": 130, "font.size": 9, "axes.grid": True, "grid.alpha": 0.3})

GROUPS = {
    "Fabless & IP/EDA": ["NVDA", "AVGO", "AMD", "QCOM", "MRVL", "ARM", "SNPS", "CDNS"],
    "Foundry & IDM": ["TSM", "005930.KS", "INTC", "GFS", "0981.HK", "TXN", "IFX.DE"],
    "Memory": ["MU", "000660.KS"],
    "Equipment (WFE) & Test": ["ASML", "AMAT", "LRCX", "KLAC", "8035.T", "ASM.AS", "6857.T", "6146.T", "TER"],
    "Materials & OSAT": ["4063.T", "ENTG", "ASX", "AMKR"],
}
GCOL = dict(zip(GROUPS, ["#1f77b4", "#d62728", "#9467bd", "#2ca02c", "#ff7f0e"]))
grp_of = {t: g for g, ts in GROUPS.items() for t in ts}
lab = lambda t: f"{UNIVERSE[t][0]} ({t})"

# 1. Price over time by segment (USD, rebased, log)
fig, axes = plt.subplots(3, 2, figsize=(13, 12))
start = px.index[-1] - pd.Timedelta(days=1826)
for ax, (g, ts) in zip(axes.flat, GROUPS.items()):
    for t in ts:
        s = px[t].loc[start:].dropna()
        ax.plot(s / s.iloc[0] * 100, lw=1.2, label=t)
    for b, st in (("SPY", "k--"), ("SOXX", "k:")):
        s = px[b].loc[start:].dropna(); ax.plot(s / s.iloc[0] * 100, st, lw=1.2, label=b)
    ax.set_yscale("log"); ax.set_title(f"{g}: USD price, rebased to 100 (5Y, log scale)"); ax.legend(fontsize=7, ncol=3)
ax = axes.flat[-1]
for t in ["SPY", "SOXX", "ACWI"]:
    s = px[t].loc[start:].dropna(); ax.plot(s / s.iloc[0] * 100, label=t)
ax.set_yscale("log"); ax.set_title("Benchmarks"); ax.legend()
plt.tight_layout(); plt.savefig(CH / "01_price_history_by_segment.png"); plt.close()

# 2. Trailing returns bar
perf = S["Price_Performance"]
fig, axes = plt.subplots(1, 3, figsize=(15, 8), sharey=False)
for ax, col, title in zip(axes, ["ret_YTD_usd", "ret_1Y_usd", "ret_3Y_usd"], ["YTD", "1-Year", "3-Year"]):
    d = perf.loc[tick, col].sort_values()
    ax.barh([f"{t}" for t in d.index], d.values * 100, color=[GCOL[grp_of[t]] for t in d.index])
    for b, c in (("SPY", "k"), ("SOXX", "grey")):
        ax.axvline(perf.loc[b, col] * 100, color=c, ls="--", lw=1, label=f"{b} {perf.loc[b, col]:.0%}")
    ax.set_title(f"{title} total return (USD, %)"); ax.legend(fontsize=7)
handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in GCOL.values()]
fig.legend(handles, GCOL.keys(), loc="lower center", ncol=5)
plt.tight_layout(rect=(0, 0.04, 1, 1)); plt.savefig(CH / "02_trailing_returns.png"); plt.close()

# 3. SML (ch9): realized mean excess return vs beta
idx, st = S["Index_Model_CAPM_Ch8_9"], S["Return_Risk_Ch5"]
fig, ax = plt.subplots(figsize=(10, 7))
for t in tick:
    ax.scatter(idx.loc[t, "beta_spy"], st.loc[t, "excess_mean_ann"] * 100, color=GCOL[grp_of[t]], s=40)
    ax.annotate(t, (idx.loc[t, "beta_spy"], st.loc[t, "excess_mean_ann"] * 100), fontsize=7, xytext=(3, 3), textcoords="offset points")
mrp_hist = st.loc["SPY", "excess_mean_ann"] * 100
bb = np.linspace(0, 4, 10)
ax.plot(bb, bb * mrp_hist, "k--", label=f"Ex-post SML: E(R)=β×{mrp_hist:.1f}% (SPY hist. excess)")
ax.plot(bb, bb * 5.5, "g:", label="Ex-ante SML: β×5.5% MRP")
ax.set_xlabel("Beta vs S&P 500 (60m)"); ax.set_ylabel("Avg annual excess return, % (60m)")
ax.set_title("Security Market Line (BKM ch.9): points above the line = positive Jensen's alpha"); ax.legend()
fig.legend(handles, GCOL.keys(), loc="lower right", ncol=1, fontsize=7, bbox_to_anchor=(0.9, 0.12))
plt.tight_layout(); plt.savefig(CH / "03_security_market_line.png"); plt.close()

# 4. Ex-ante efficient frontier (ch7) with CAL (ch6)
fr = np.array(R["frontier"]); mu, C, rf = R["mu"], R["cov"].values, R["rf"]
ports, ps = S["Portfolios_Ch7"], S["Portfolio_Stats"]
fig, ax = plt.subplots(figsize=(10, 7))
sd_i = np.sqrt(np.diag(C))
for i, t in enumerate(tick):
    ax.scatter(sd_i[i] * 100, mu[i] * 100, color=GCOL[grp_of[t]], s=25); ax.annotate(t, (sd_i[i] * 100, mu[i] * 100), fontsize=6)
if len(fr): ax.plot(fr[:, 0] * 100, fr[:, 1] * 100, "b-", lw=2, label="Long-only frontier (≤10%/name)")
for c, m in (("GMV_longonly_cap10", "s"), ("MaxSharpe_longonly_cap10", "*"), ("EqualWeight", "o")):
    ax.scatter(ps.loc["sd", c] * 100, ps.loc["exp_return", c] * 100, marker=m, s=160, color="k", label=c)
x = np.linspace(0, 0.6, 10)
ax.plot(x * 100, (rf + ps.loc["sharpe", "MaxSharpe_longonly_cap10"] * x) * 100, "r--", label="CAL through tangency")
ax.set_xlabel("Ex-ante σ (%, single-index covariance)"); ax.set_ylabel("Ex-ante E(r) (%, CAPM + shrunk alpha)")
ax.set_title("Efficient frontier & optimal CAL (BKM ch.6-8)"); ax.legend(fontsize=7)
plt.tight_layout(); plt.savefig(CH / "04_efficient_frontier.png"); plt.close()

# 5. Correlation heatmap
cor = S["Correlation"].loc[sum(GROUPS.values(), []), sum(GROUPS.values(), [])]
fig, ax = plt.subplots(figsize=(11, 9.5))
im = ax.imshow(cor.values, cmap="RdYlGn_r", vmin=0, vmax=1)
ax.set_xticks(range(len(cor))); ax.set_xticklabels(cor.columns, rotation=90, fontsize=7)
ax.set_yticks(range(len(cor))); ax.set_yticklabels(cor.index, fontsize=7)
plt.colorbar(im, fraction=0.046); ax.set_title("Monthly USD return correlations (60m) — grouped by segment"); ax.grid(False)
plt.tight_layout(); plt.savefig(CH / "05_correlation_heatmap.png"); plt.close()

# 6. DuPont (ch19): margin vs turnover, bubble = ROE
f = S["Fundamentals_DuPont_Ch19"]
fig, ax = plt.subplots(figsize=(10, 7))
for t in tick:
    m, at, roe = f.loc[t, "ebit_margin"], f.loc[t, "asset_turnover"], f.loc[t, "roe_dupont"]
    if pd.isna(m) or pd.isna(at): continue
    ax.scatter(at, m * 100, s=max(roe, 0.02) * 900, color=GCOL[grp_of[t]], alpha=0.55, edgecolor="k")
    ax.annotate(f"{t}\nROE {roe:.0%}", (at, m * 100), fontsize=6, ha="center")
ax.set_xlabel("Asset turnover (Sales / avg assets)"); ax.set_ylabel("EBIT margin, %")
ax.set_title("DuPont map (BKM ch.19): ROE = margin × turnover × leverage × burdens (bubble = ROE)")
plt.tight_layout(); plt.savefig(CH / "06_dupont_map.png"); plt.close()

# 7. Valuation (ch18): implied stage-1 growth vs sustainable growth; PVGO share
v = S["Valuation_Ch18"]
fig, axes = plt.subplots(1, 2, figsize=(15, 7))
ax = axes[0]
for t in tick:
    a, b_ = v.loc[t, "sustainable_g"], v.loc[t, "implied_stage1_growth"]
    if pd.isna(a) or pd.isna(b_): continue
    a = min(a, 1.2)
    ax.scatter(a * 100, b_ * 100, color=GCOL[grp_of[t]], s=40); ax.annotate(t, (a * 100, b_ * 100), fontsize=7)
ax.plot([-20, 120], [-20, 120], "k--", lw=1, label="implied = sustainable")
ax.set_xlabel("Sustainable growth g = ROE × b (%, capped at 120)"); ax.set_ylabel("Market-implied stage-1 growth (%, reverse 2-stage DCF)")
ax.set_title("What growth is priced in? (above line = price needs more growth than ROE×b supports)"); ax.legend()
ax = axes[1]
d = v.loc[tick, "PVGO_share_of_price"].sort_values()
ax.barh(d.index, d.values * 100, color=[GCOL[grp_of[t]] for t in d.index])
ax.set_title("PVGO as % of price: 1 − (E1/P)/k  (negative = market expects earnings to fall)"); ax.axvline(0, color="k")
plt.tight_layout(); plt.savefig(CH / "07_valuation_growth.png"); plt.close()

# 8. Drawdowns
fig, ax = plt.subplots(figsize=(12, 5))
for t in ["SOXX", "SPY", "NVDA", "TSM", "ASML", "MU", "INTC"]:
    s = px[t].loc[start:].dropna(); ax.plot((s / s.cummax() - 1) * 100, lw=1, label=t)
ax.set_title("Drawdown from running peak (%), 5Y — tail risk (BKM ch.5)"); ax.legend(ncol=7, fontsize=7)
plt.tight_layout(); plt.savefig(CH / "08_drawdowns.png"); plt.close()

# 9. Scorecard
sc = S["Scorecard"]
fig, ax = plt.subplots(figsize=(11, 9))
cols = ["Quality", "Valuation", "Risk (low=good)", "Momentum", "Risk-adj. perf"]
left = np.zeros(len(sc)); lpos = np.zeros(len(sc))
for c, colr in zip(cols, ["#4c72b0", "#55a868", "#c44e52", "#8172b2", "#ccb974"]):
    vals = sc[c].values / len(cols)
    pos = np.where(vals > 0, vals, 0); neg = np.where(vals < 0, vals, 0)
    ax.barh(sc.index[::-1], pos[::-1], left=lpos[::-1], color=colr, label=c)
    ax.barh(sc.index[::-1], neg[::-1], left=left[::-1], color=colr)
    lpos += pos; left += neg
ax.scatter(sc.Composite[::-1], sc.index[::-1], color="k", zorder=5, label="Composite")
ax.axvline(0, color="k"); ax.set_title("Composite scorecard (equal-weight z-scores; contributions stacked)"); ax.legend(fontsize=7)
plt.tight_layout(); plt.savefig(CH / "09_scorecard.png"); plt.close()

# 10. Implied vs realized vol
o = S["Options_IV_Ch21"].sort_values("atm_iv")
fig, ax = plt.subplots(figsize=(11, 5))
xx = np.arange(len(o))
ax.bar(xx - 0.2, o.atm_iv * 100, 0.4, label="ATM implied vol (~1M)")
ax.bar(xx + 0.2, o.realized_vol_1y * 100, 0.4, label="Realized vol (1Y daily)")
ax.set_xticks(xx); ax.set_xticklabels(o.index, rotation=45); ax.legend(); ax.set_title("Option-implied vs realized volatility (BKM ch.21), %")
plt.tight_layout(); plt.savefig(CH / "10_implied_vs_realized_vol.png"); plt.close()
print("charts:", sorted(p.name for p in CH.glob("*.png")))
