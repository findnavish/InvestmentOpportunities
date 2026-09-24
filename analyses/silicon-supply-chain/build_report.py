"""Build REPORT.md from analysis results."""
from pathlib import Path
import numpy as np
import pandas as pd
from universe import UNIVERSE

ROOT = Path(__file__).parent
OUT = ROOT / "output"
SITE = ROOT.parents[1] / "docs" / "silicon-supply-chain"   # MkDocs page for this analysis
REVIEWED = "2026-09-23"   # date the interpretive commentary was last reviewed by hand
R = pd.read_pickle(OUT / "results.pkl")
S = R["sheets"]
tick = list(UNIVERSE)
A = S["Assumptions"]["value"]

ROLE = {
    "NVDA": "Dominant AI accelerator (GPU + CUDA + NVLink); largest single consumer of CoWoS & HBM",
    "AVGO": "Custom AI ASICs (TPU-class XPUs) for hyperscalers + Ethernet/switch silicon",
    "AMD": "#2 merchant AI GPU (Instinct) and x86 CPU share gainer",
    "QCOM": "Mobile SoC/modem leader; edge-AI, auto and PC (Arm) diversification",
    "MRVL": "Custom ASICs, electro-optics/DSPs for AI data-center interconnect",
    "ARM": "Instruction-set/IP licensor in ~all mobile and a rising share of data-center CPUs",
    "SNPS": "EDA + interface IP duopolist (post-Ansys: simulation); no chip gets designed without it",
    "CDNS": "EDA duopolist (analog/custom, verification hardware, system analysis)",
    "TSM": "~70%+ foundry share, ~all leading-edge (N3/N2/A16) logic + CoWoS packaging — the system's chokepoint",
    "005930.KS": "Memory #1-2 (DRAM/NAND/HBM) + #2 foundry; Korea's national champion",
    "INTC": "x86 IDM rebuilding foundry (18A/14A); US-government equity stake; CHIPS flagship",
    "GFS": "Largest US-HQ specialty/mature-node foundry (RF, FD-SOI, silicon photonics)",
    "0981.HK": "China's largest foundry; spearhead of Chinese self-sufficiency under export controls",
    "TXN": "Analog/embedded leader with 300mm US fabs; industrial/auto bellwether",
    "IFX.DE": "#1 power semis (SiC/GaN) & auto MCUs; Europe's anchor for AI data-center power",
    "MU": "Only US memory maker; HBM3E/HBM4 supplier; CHIPS-funded US DRAM fabs",
    "000660.KS": "HBM leader (primary HBM supplier to NVIDIA); DRAM #1-2",
    "ASML": "Monopoly in EUV (and High-NA EUV) lithography — irreplaceable chokepoint",
    "AMAT": "Largest WFE vendor: deposition, etch, implant, GAA/backside-power tooling",
    "LRCX": "Etch/deposition leader; critical for 3D NAND, HBM TSVs, GAA",
    "KLAC": "Process control/inspection near-monopoly; yield is its product",
    "8035.T": "Coater/developer monopoly on EUV tracks + etch/deposition; Japan's WFE champion",
    "ASM.AS": "ALD and epitaxy leader — key to GAA transistors",
    "6857.T": "SoC/HBM test leader (AI GPU test is its growth engine)",
    "6146.T": "Dicing/grinding/polishing near-monopoly; essential for HBM stacking & advanced packaging",
    "TER": "SoC/memory test #2; robotics; AI compute test exposure",
    "4063.T": "#1 silicon wafer supplier + photoresists/photomask blanks",
    "ENTG": "Ultra-pure materials, filtration, CMP — contamination control for advanced nodes",
    "ASX": "#1 OSAT (ASE/SPIL); CoWoS-like advanced packaging & test overflow for TSMC",
    "AMKR": "#2 OSAT; building the first large US advanced-packaging site (Arizona)",
}


def pct(x, d=0):
    return "–" if pd.isna(x) else f"{x * 100:,.{d}f}%"


def num(x, d=2):
    return "–" if pd.isna(x) else f"{x:,.{d}f}"


def md(df):
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for _, r in df.iterrows():
        out.append("| " + " | ".join(str(v) for v in r.values) + " |")
    return "\n".join(out)


perf, st, idx, ff = S["Price_Performance"], S["Return_Risk_Ch5"], S["Index_Model_CAPM_Ch8_9"], S["FamaFrench_Ch10"]
pe, cur, f, v = S["Performance_Ch24"], S["Currency_Ch25"], S["Fundamentals_DuPont_Ch19"], S["Valuation_Ch18"]
tech, opt, tb, tbs = S["Technicals_Ch11_12"], S["Options_IV_Ch21"], S["TreynorBlack_Ch27"], S["TB_Summary"]["value"]
ports, pst, cal, div, sc = S["Portfolios_Ch7"], S["Portfolio_Stats"], S["Capital_Alloc_Ch6"], S["Diversification_Ch7"], S["Scorecard"]
name = lambda t: UNIVERSE[t][0]

SHORT = {"005930.KS": "Samsung", "000660.KS": "SK hynix", "0981.HK": "SMIC", "IFX.DE": "Infineon", "8035.T": "Tokyo Electron",
         "ASM.AS": "ASMI", "6857.T": "Advantest", "6146.T": "Disco", "4063.T": "Shin-Etsu"}
nm = lambda t: SHORT.get(t, t)


def names(ts):
    ts = list(ts)
    return "none" if not ts else ", ".join(nm(t) for t in ts[:-1]) + (" and " if len(ts) > 1 else "") + nm(ts[-1])


def rng(sr, d=0):
    return f"{pct(sr.min(), d)}–{pct(sr.max(), d)}"


MEM = ["005930.KS", "000660.KS", "MU"]
nonmem = [t for t in tick if t not in MEM]
r1y = perf.loc[tick, "ret_1Y_usd"].sort_values()
ig = v.loc[nonmem, "implied_stage1_growth"].dropna().sort_values(ascending=False)
sig_capm = idx.loc[tick][idx.loc[tick, "alpha_t"] >= 1.96].index
sig_ff = ff.loc[[t for t in ff.index if t in tick]].query("ff_alpha_t >= 1.96").sort_values("ff_alpha_t", ascending=False)
dd_ok = perf.loc[tick][perf.loc[tick, "max_drawdown_5y"] > -0.4].index
off52 = perf.loc[tick, "pct_from_52w_high"].sort_values().head(4)
m2 = pe.loc[[t for t in pe.index if t in tick], "M2"].sort_values(ascending=False)
ivrv = opt["iv_rv_ratio"].dropna()
mem_pe0 = 1 / idx.loc[MEM, "capm_k"]
tbw_t = tb.final_weight_in_risky_portfolio.sort_values(ascending=False)
capm_txt = ", ".join(f"{nm(t)} (t={num(idx.loc[t, 'alpha_t'])})" for t in sig_capm) or "none"
ff_alpha_txt = ", ".join(f"{nm(t)} {pct(r.ff_alpha_ann)} (t={num(r.ff_alpha_t)})" for t, r in sig_ff.iterrows()) or "none"

# ---------- tables ----------
t_univ = md(pd.DataFrame([{"#": i + 1, "Company": name(t), "Ticker": t, "Segment": UNIVERSE[t][1], "HQ": UNIVERSE[t][2],
                           "Mkt cap (USD bn)": num(f.loc[t, "market_cap_usd_bn"], 0), "Why it's crucial": ROLE[t]} for i, t in enumerate(tick)]))

t_perf = md(pd.DataFrame([{"Ticker": t, "Local px": num(perf.loc[t, "local_price"], 2) + f" {UNIVERSE[t][3] if t in UNIVERSE else 'USD'}",
                           "1M": pct(perf.loc[t, "ret_1M_usd"]), "YTD": pct(perf.loc[t, "ret_YTD_usd"]), "1Y": pct(perf.loc[t, "ret_1Y_usd"]),
                           "3Y": pct(perf.loc[t, "ret_3Y_usd"]), "5Y": pct(perf.loc[t, "ret_5Y_usd"]),
                           "vs 52w high": pct(perf.loc[t, "pct_from_52w_high"]), "Max DD (5Y)": pct(perf.loc[t, "max_drawdown_5y"])}
                          for t in tick + ["SOXX", "SPY", "ACWI"]]))

t_risk = md(pd.DataFrame([{"Ticker": t, "Arith. mean": pct(st.loc[t, "arith_mean_ann"]), "Geo. mean": pct(st.loc[t, "geo_mean_ann"]),
                           "σ (ann.)": pct(st.loc[t, "sd_ann"]), "Sharpe": num(st.loc[t, "sharpe"]), "Sortino": num(st.loc[t, "sortino"]),
                           "Skew": num(st.loc[t, "skew"]), "Ex. kurt": num(st.loc[t, "excess_kurtosis"]),
                           "VaR 5% (1m)": pct(st.loc[t, "VaR5_monthly"], 1), "ES 5% (1m)": pct(st.loc[t, "ES5_monthly"], 1)}
                          for t in tick + ["SOXX", "SPY"]]))

t_idx = md(pd.DataFrame([{"Ticker": t, "β (SPY)": num(idx.loc[t, "beta_spy"]), "Adj. β": num(idx.loc[t, "beta_adj_blume"]),
                          "β (SOXX)": num(idx.loc[t, "beta_soxx"]), "α (ann.)": pct(idx.loc[t, "alpha_ann"], 1), "t(α)": num(idx.loc[t, "alpha_t"]),
                          "R²": num(idx.loc[t, "R2"]), "σ(e)": pct(idx.loc[t, "resid_sd_ann"]), "CAPM k": pct(idx.loc[t, "capm_k"], 1)}
                         for t in tick + ["SOXX"]]))

t_ff = md(pd.DataFrame([{"Ticker": t, "FF α (ann.)": pct(ff.loc[t, "ff_alpha_ann"], 1), "t(α)": num(ff.loc[t, "ff_alpha_t"]),
                         "Mkt": num(ff.loc[t, "Mkt-RF"]), "SMB": num(ff.loc[t, "SMB"]), "HML": num(ff.loc[t, "HML"]),
                         "RMW": num(ff.loc[t, "RMW"]), "CMA": num(ff.loc[t, "CMA"]), "MOM": num(ff.loc[t, "Mom"]), "R²": num(ff.loc[t, "R2"])}
                        for t in ff.index]))

t_pe = md(pd.DataFrame([{"Ticker": t, "Sharpe": num(pe.loc[t, "sharpe"]), "Treynor": pct(pe.loc[t, "treynor"], 1),
                         "Jensen α": pct(pe.loc[t, "jensen_alpha"], 1), "Info ratio": num(pe.loc[t, "info_ratio"]), "M²": pct(pe.loc[t, "M2"], 1)}
                        for t in pe.sort_values("M2", ascending=False).index]))

t_cur = md(pd.DataFrame([{"Ticker": r.ticker, "Window": r.window, "Ccy": r.ccy, "Local return": pct(r.local_ret),
                          "FX vs USD": pct(r.fx_ret_vs_usd, 1), "USD return": pct(r.usd_ret), "FX contribution": pct(r.fx_contribution)}
                         for r in cur.itertuples()]))

t_dup = md(pd.DataFrame([{"Ticker": t, "FY": str(f.loc[t, "fiscal_year_end"])[:7], "Gross m.": pct(f.loc[t, "gross_margin"]),
                          "EBIT m.": pct(f.loc[t, "ebit_margin"]), "Tax burden": num(f.loc[t, "tax_burden"]),
                          "Int. burden": num(f.loc[t, "interest_burden"]), "Asset turn": num(f.loc[t, "asset_turnover"]),
                          "Leverage": num(f.loc[t, "leverage"]), "ROE": pct(f.loc[t, "roe_dupont"]), "R&D/Sales": pct(f.loc[t, "rnd_intensity"]),
                          "Capex/Sales": pct(f.loc[t, "capex_intensity"]), "FCF/NI": num(f.loc[t, "fcf_conversion_fy"]),
                          "Accruals": num(f.loc[t, "accruals_ratio"], 3), "DOL": num(f.loc[t, "DOL"], 1),
                          "Int. cover": num(f.loc[t, "interest_coverage"], 0), "Net cash (USD bn)": num(f.loc[t, "net_cash_usd_bn"], 1)}
                         for t in tick]))

t_val = md(pd.DataFrame([{"Ticker": t, "Trail P/E": num(f.loc[t, "trailing_pe"], 1), "Fwd P/E": num(v.loc[t, "forward_pe"], 1) + ("*" if v.loc[t, "forward_pe_data_flag"] else ""),
                          "EV/EBITDA": num(f.loc[t, "ev_ebitda_ttm"], 1), "P/S": num(f.loc[t, "ps_ratio_ttm"], 1), "P/B": num(f.loc[t, "pb_ratio"], 1),
                          "FCF yld": pct(f.loc[t, "fcf_yield"], 1), "Div yld": pct(f.loc[t, "div_yield"], 2),
                          "k (CAPM)": pct(v.loc[t, "capm_k"], 1), "g=ROE×b": pct(min(v.loc[t, "sustainable_g"], 9.99)),
                          "PVGO/P": pct(v.loc[t, "PVGO_share_of_price"]), "Implied g (stage 1)": pct(v.loc[t, "implied_stage1_growth"]),
                          "2-stage DCF vs px": pct(v.loc[t, "two_stage_upside"]), "Street tgt upside": pct(f.loc[t, "analyst_target_upside"])}
                         for t in tick]))

t_tech = md(pd.DataFrame([{"Ticker": t, "12-1 mom.": pct(tech.loc[t, "mom_12_1"]), "vs 50DMA": pct(tech.loc[t, "px_vs_50dma"]),
                           "vs 200DMA": pct(tech.loc[t, "px_vs_200dma"]), "50>200 (golden)": "✅" if tech.loc[t, "golden_cross"] else "❌",
                           "RSI(14)": num(tech.loc[t, "RSI14"], 0), "6M RS vs SOXX": pct(tech.loc[t, "rel_strength_vs_SOXX_6M"])}
                          for t in tick]))

t_opt = md(pd.DataFrame([{"Ticker": t, "ATM IV": pct(opt.loc[t, "atm_iv"]), "Realized σ (1Y)": pct(opt.loc[t, "realized_vol_1y"]),
                          "IV/RV": num(opt.loc[t, "iv_rv_ratio"]), "Implied ±1σ 1-month move": pct(opt.loc[t, "implied_1m_1sd_move"], 1),
                          "Expiry": opt.loc[t, "expiry"]} for t in opt.index]))

tbw = tb.final_weight_in_risky_portfolio.sort_values(ascending=False)
t_tb = md(pd.DataFrame([{"Ticker": t, "Raw analyst α": pct(tb.loc[t, "alpha_raw"]), "De-biased & shrunk α": pct(tb.loc[t, "alpha_shrunk"], 1),
                         "σ(e)": pct(np.sqrt(tb.loc[t, "resid_var"])), "Weight in optimal risky portfolio": pct(tbw[t], 1)}
                        for t in list(tbw.index[:8]) + list(tbw.index[-6:])]))

pw = ports[(ports[["GMV_longonly_cap10", "MaxSharpe_longonly_cap10"]] > 0.005).any(axis=1)]
t_port = md(pd.DataFrame([{"Ticker": t, "Global min-variance": pct(pw.loc[t, "GMV_longonly_cap10"], 1), "Max-Sharpe (tangency)": pct(pw.loc[t, "MaxSharpe_longonly_cap10"], 1)}
                          for t in pw.sort_values("MaxSharpe_longonly_cap10", ascending=False).index]))
t_pst = md(pd.DataFrame([{"Portfolio": c, "E(r)": pct(pst.loc["exp_return", c], 1), "σ": pct(pst.loc["sd", c], 1),
                          "Sharpe": num(pst.loc["sharpe", c]), "β": num(pst.loc["beta", c])} for c in pst.columns]))
t_cal = md(pd.DataFrame([{"Risk aversion A": int(r.A), "y* in semis tangency portfolio": pct(r.y_star_in_semis_portfolio),
                          "Complete-portfolio E(r)": pct(r.complete_port_exp_ret, 1), "Complete-portfolio σ": pct(r.complete_port_sd, 1)} for r in cal.itertuples()]))
t_div = md(pd.DataFrame([{"# stocks (equal-wt)": int(r.n), "Portfolio σ": pct(r.sd_equal_weight, 1)} for r in div.itertuples()]))
t_sc = md(pd.DataFrame([{"Rank": int(sc.loc[t, "Rank"]), "Ticker": t, "Company": name(t), **{c: num(sc.loc[t, c]) for c in ["Quality", "Valuation", "Risk (low=good)", "Momentum", "Risk-adj. perf", "Composite"]}} for t in sc.index]))

report = f"""# Silicon Supply Chain — Top 30 Key Players
### Price history, textbook-grade analysis (Bodie-Kane-Marcus *Investments* 13e) and PEST

**Prices as of:** {A['price_date']} close (USD unless noted; foreign listings converted at spot FX) · **Statistics window:** {A['stats_window']} monthly USD returns · **Risk-free:** 13-wk T-bill {pct(A['rf_13w_tbill'], 2)}, 10-yr UST {pct(A['rf_10y_treasury'], 2)} · **Assumed MRP:** {pct(A['market_risk_premium'], 1)}

> ⚠️ Educational analysis, not investment advice. Data from Yahoo Finance and the Kenneth French Data Library; some fundamental fields from data vendors contain errors (flagged where detected). Past returns are noisy estimates of expected returns (BKM ch.5).

**Downloads & code:** [📊 Excel workbook (21 sheets, every number on this page)](Silicon_Supply_Chain_Analysis.xlsx) · [source code](https://github.com/findnavish/InvestmentOpportunities/tree/main/analyses/silicon-supply-chain)

!!! info "Freshness"
    Prices, statistics, tables, charts and the highlighted lists refresh automatically every week (last data update: **{A['price_date']}**). The interpretive commentary and PEST analysis were last reviewed by hand on **{REVIEWED}**, so check the tables if a sentence and a number disagree.

---

## 1. Executive summary

1. **The AI capex supercycle has turned the whole chain into a high-beta, momentum-driven asset class.** SOXX gained **{pct(perf.loc['SOXX','ret_1Y_usd'])} in 1Y / {pct(perf.loc['SOXX','ret_5Y_usd'])} in 5Y** vs SPY {pct(perf.loc['SPY','ret_1Y_usd'])} / {pct(perf.loc['SPY','ret_5Y_usd'])}. Memory had the biggest gains: SK hynix **{pct(perf.loc['000660.KS','ret_5Y_usd'])}**, Micron **{pct(perf.loc['MU','ret_5Y_usd'])}** over 5Y in USD. The five weakest over 1Y: {', '.join(f'{nm(t)} {pct(x)}' for t, x in r1y.head(5).items())}.
2. **Risk is dominated by firm-specific risk, not market risk (ch.8).** Betas vs the S&P 500 range from {num(idx.loc[tick,'beta_spy'].min())} (SMIC) to {num(idx.loc[tick,'beta_spy'].max())} (Arm), but the median R² is only {num(idx.loc[tick,'R2'].median())}. Most volatility is idiosyncratic, so diversifying *within* the chain has real value (σ falls from {pct(div.sd_equal_weight.iloc[0])} for a single stock to {pct(div.sd_equal_weight.iloc[-1])} for 30 names). It cannot fall below the sector's common-factor floor, though.
3. **Jensen's alphas look huge but are mostly not statistically significant (ch.9, 11, 24).** Against the CAPM, only {capm_txt} clear t≈2. Against Fama-French 5 factors plus momentum, only {names(sig_ff.index)} do. Five years of data is too short to separate skill or structural advantage from luck.
4. **Valuation mostly prices in growth rather than current earnings (ch.18).** Outside memory, {rng(v.loc[nonmem,'PVGO_share_of_price'])} of each price is PVGO (present value of growth opportunities). The reverse DCF says the market needs stage-1 cash-flow growth of {rng(ig)} p.a. The most demanding: {', '.join(f'{nm(t)} (~{pct(x)})' for t, x in ig.head(4).items())}. NVIDIA needs only ~{pct(v.loc['NVDA','implied_stage1_growth'])} despite ROE×b above 100%, and Broadcom ~{pct(v.loc['AVGO','implied_stage1_growth'])}.
5. **Memory shows the classic cyclical-peak signature (ch.17–18).** Samsung trades at a forward P/E of {num(v.loc['005930.KS','forward_pe'],1)}, SK hynix at {num(v.loc['000660.KS','forward_pe'],1)} and MU at {num(v.loc['MU','forward_pe'],1)}, against a no-growth P/E of 1/k ≈ {num(mem_pe0.min(),1)}–{num(mem_pe0.max(),1)}. That means PVGO is negative: the market is pricing a fall in peak HBM/DRAM earnings. A low P/E at the top of the cycle is a trap unless the cycle turns out to be structurally longer.
6. **Political risk is now a first-order return driver (PEST).** Three dates matter: Section 232 chip tariffs (in force since 15 Jan 2026), the expiry of China's gallium/germanium export-control suspension on 27 Nov 2026, and the CHIPS tax-credit sunset for fab starts after 31 Dec 2026. The US government is also now an Intel shareholder.

---

## 2. The Top 30: who they are and why they matter

The chain runs **design IP/EDA → fabless → foundry/IDM (+ memory) ← equipment ← materials → packaging & test (OSAT)**. The universe covers every chokepoint:

{t_univ}

*Omitted for size or data reasons, but important:* Nexperia, Kioxia, Lasertec, BESI (hybrid bonding), Ibiden (substrates), SUMCO, Soitec, Linde and Air Liquide (gases), JSR/TOK (resists), Zeiss (EUV optics, private), UMC, Rapidus (private), Hua Hong, Naura/AMEC (China WFE).

---

## 3. Price over time

![Price history](charts/01_price_history_by_segment.png)
![Trailing returns](charts/02_trailing_returns.png)

{t_perf}

**Reading the tape**
- **Leadership rotated.** In 2023–24 the story was "GPU + TSMC". In 2025–26 the gains broadened to **memory (HBM)**, **Samsung**, **test (Advantest, Teradyne)**, **OSAT (ASE)** and a speculative **Intel/AMD/Arm** rally. Broadcom and EDA lagged.
- **Drawdowns are brutal (ch.5 tail risk).** Every name except {names(dd_ok)} lost more than 40% peak-to-trough within the last 5 years. Intel lost {pct(perf.loc['INTC','max_drawdown_5y'])}, NVIDIA {pct(perf.loc['NVDA','max_drawdown_5y'])} and SOXX {pct(perf.loc['SOXX','max_drawdown_5y'])}. The April-2025 tariff shock is visible across all panels.
- **Distance from 52-week highs** shows the summer-2026 correction: SOXX is {pct(perf.loc['SOXX','pct_from_52w_high'])} from its high, with {names(off52.index)} {pct(-off52.max())}–{pct(-off52.min())} off.

![Drawdowns](charts/08_drawdowns.png)

---

## 4. Risk & return statistics (BKM ch.5)

{t_risk}

- **Arithmetic > geometric** means everywhere. The gap is roughly σ²/2, so high-volatility names (INTC, AMD, MRVL, ARM) lose the most to volatility drag. Intel's arithmetic mean is {pct(st.loc['INTC','arith_mean_ann'])}, but it compounded at only {pct(st.loc['INTC','geo_mean_ann'])}.
- **Non-normality.** Returns are mostly *positively* skewed (a "lottery-like" right tail) with fat tails; Intel's excess kurtosis is {num(st.loc['INTC','excess_kurtosis'],1)}. So VaR/ES are more informative than σ alone. A 1-in-20 bad month (VaR 5%) costs {pct(-st.loc[tick,'VaR5_monthly'].max())}–{pct(-st.loc[tick,'VaR5_monthly'].min())}.
- **Sharpe ratios:** Broadcom {num(st.loc['AVGO','sharpe'])}, NVIDIA {num(st.loc['NVDA','sharpe'])}, Micron and SK hynix ~{num(st.loc['MU','sharpe'])} vs SPY {num(st.loc['SPY','sharpe'])}. Ex post, the sector's risk was well paid, but that is the *realized* outcome of a boom, not an ex-ante expectation.

---

## 5. Single-index model & CAPM (BKM ch.8–9)

$R_i = \\alpha_i + \\beta_i R_M + e_i$ (monthly excess returns vs SPY), Blume-adjusted $\\beta_{{adj}} = \\tfrac{{2}}{{3}}\\hat\\beta + \\tfrac{{1}}{{3}}$, and $k = r_f^{{10y}} + \\beta_{{adj}} \\times MRP$.

{t_idx}

![SML](charts/03_security_market_line.png)

**Takeaways**
- **Cost of equity is high: 8–21%, mostly 12–21%.** A 5.1% 10-year yield combined with β_adj of 0.6 (SMIC) to 2.9 (Arm) gives k = 8–21%. That is why long-duration growth names (ARM, AMD, MRVL) are so sensitive to rates.
- **Systematic share of variance (R²)** is only 2–48% (median {num(idx.loc[tick,'R2'].median())}). SMIC's R² of {num(idx.loc['0981.HK','R2'])} shows **market segmentation (ch.25)**: its price is driven by China policy, not the US market.
- Nearly every name plots **above the ex-post SML** (positive Jensen α), but t-stats are mostly below 2. Per ch.11/13 this is consistent with a *sector-specific* shock (AI demand) that CAPM does not price, not with persistent mispricing.
- **β vs SOXX** is the right hedge ratio for sector-relative trades: MU {num(idx.loc['MU','beta_soxx'])}, SK hynix {num(idx.loc['000660.KS','beta_soxx'])}, AMD {num(idx.loc['AMD','beta_soxx'])}, while Synopsys and Cadence are ~0.5. EDA works as a *defensive* sleeve inside semis.

---

## 6. Multifactor exposures — Fama-French 5 + Momentum (BKM ch.10, 13)

Factors through {A['FF_factors_through']}; coefficients are loadings.

{t_ff}

- **HML strongly negative** for NVDA, AVGO, ARM and Advantest: these are pure *growth* exposures that suffer when value rallies.
- **RMW negative** for memory, SMIC, Samsung, Intel and ARM: returns co-move with *unprofitable* firms, a signature of cyclicality and speculation.
- **Momentum loadings** are significant for KLAC, Disco, GFS and Intel. Momentum crashes (ch.12) are therefore a real portfolio risk.
- Alphas that **survive** 6 factors: {ff_alpha_txt}. These are the AI-bottleneck owners (GPU, custom ASIC, HBM, HBM/GPU test).

---

## 7. Performance evaluation (BKM ch.24)

Sharpe (total risk), Treynor (β risk), Jensen α, Information ratio = α/σ(e), and M² = (S_p − S_M)·σ_M, a return-equivalent at market volatility.

{t_pe}

**Which measure to use (ch.24):** use **Sharpe/M²** if the stock *is* your whole risky portfolio, **Treynor/Jensen** if it is one of many holdings in a diversified portfolio, and the **information ratio** for an active satellite added to an index core. By M², the leaders are {names(m2.index[:6])} and the laggards are {names(m2.index[-5:][::-1])}.

---

## 8. Currency decomposition for foreign listings (BKM ch.25)

$1 + r_{{USD}} = (1 + r_{{local}})(1 + r_{{FX}})$

{t_cur}

- **Yen weakness (−30% vs USD over 5Y)** cost US investors a lot: Advantest made +{pct(cur[(cur.ticker=='6857.T')&(cur.window=='5Y')].local_ret.iloc[0])} in yen but only +{pct(cur[(cur.ticker=='6857.T')&(cur.window=='5Y')].usd_ret.iloc[0])} in USD, and Shin-Etsu's +53% in yen became +6%.
- KRW fell 12.5% over 5Y but *helped* over the last year (+2.9%). Currency exposure is a separate bet (ch.25): hedge it with forwards (interest-rate parity, ch.23) if you want pure equity exposure.

---

## 9. Financial statement analysis — DuPont & earnings quality (BKM ch.19)

$ROE = \\underbrace{{\\tfrac{{NI}}{{PTI}}}}_{{\\text{{tax}}}} \\times \\underbrace{{\\tfrac{{PTI}}{{EBIT}}}}_{{\\text{{interest}}}} \\times \\underbrace{{\\tfrac{{EBIT}}{{Sales}}}}_{{\\text{{margin}}}} \\times \\underbrace{{\\tfrac{{Sales}}{{Assets}}}}_{{\\text{{turnover}}}} \\times \\underbrace{{\\tfrac{{Assets}}{{Equity}}}}_{{\\text{{leverage}}}}$ (latest fiscal year)

{t_dup}

![DuPont](charts/06_dupont_map.png)

**Quality of ROE**
- **NVIDIA's ~{pct(f.loc['NVDA','roe_dupont'])} ROE is high-quality.** It comes from a {pct(f.loc['NVDA','ebit_margin'])} EBIT margin and 1.36× asset turnover with low leverage (1.35×). **KLAC's {pct(f.loc['KLAC','roe_dupont'])}** leans on 3.1× leverage from buybacks and debt, a less durable source of ROE.
- **The accruals ratio** (NI − OCF)/assets flags NVIDIA ({num(f.loc['NVDA','accruals_ratio'],3)}), LRCX, KLAC and Advantest: earnings running ahead of cash (receivables/inventory build). That is typical in a hyper-growth year but worth monitoring (ch.19 quality of earnings).
- **Capital intensity splits the chain.** Foundry/memory/IDM spend 11–90% of sales on capex (SMIC {pct(f.loc['0981.HK','capex_intensity'])}, MU {pct(f.loc['MU','capex_intensity'])}, TSMC {pct(f.loc['TSM','capex_intensity'])}, Intel {pct(f.loc['INTC','capex_intensity'])}). Fabless, EDA and equipment spend 1–10% but 9–56% on R&D. Capex-heavy models have higher operating leverage.
- **Operating leverage (ch.17)**, DOL = %ΔEBIT / %ΔSales: Micron {num(f.loc['MU','DOL'],1)}×, AVGO 3.6×, AMAT 3.1×, AMD 3.1×. Memory profits amplify revenue swings roughly 10×, in both directions.
- **Intel** has near-zero ROE with an interest burden of 0.59; **SMIC** has negative FCF (FCF/NI −7.6); **ASE and Amkor** have negative TTM FCF because of the packaging capex race.

---

## 10. Valuation (BKM ch.18)

- **PVGO/P** $= 1 - (E_1/P)/k$: the share of price that depends on future growth opportunities.
- **Sustainable growth** $g = ROE \\times b$.
- **Constant-growth P/E** $= (1-b)/(k - ROE \\cdot b)$ fails (k ≤ g) for almost all of these names. That is itself a signal that a **multistage model** is needed.
- **Two-stage DCF:** CF₁ = forward earnings × FCF conversion (0.3–1.0). Growth g₁ = min(ROE·b, 25%) for year 2, fading linearly to 4% by year 10, then a Gordon terminal value at k (CAPM).
- **Implied g (stage 1):** the starting growth rate that makes the model value equal today's market cap (reverse DCF).

{t_val}

\\* Advantest's forward P/E from the data feed (140×) is inconsistent with its trailing P/E, so the trailing P/E is used instead.

![Valuation](charts/07_valuation_growth.png)

**Interpretation**
- **Least demanding relative to fundamentals:** NVIDIA (implied g ≈ {pct(v.loc['NVDA','implied_stage1_growth'])} vs ROE·b >100%, forward P/E {num(v.loc['NVDA','forward_pe'],1)}), Broadcom ({pct(v.loc['AVGO','implied_stage1_growth'])}), Qualcomm ({pct(v.loc['QCOM','implied_stage1_growth'])}), Synopsys ({pct(v.loc['SNPS','implied_stage1_growth'])}). Also Samsung and SK hynix, but only if HBM earnings prove durable (see the cyclical-peak caveat).
- **Most demanding:** Arm ({pct(v.loc['ARM','implied_stage1_growth'])} implied growth, {pct(v.loc['ARM','PVGO_share_of_price'])} PVGO, forward P/E {num(v.loc['ARM','forward_pe'],0)}×), Intel ({pct(v.loc['INTC','implied_stage1_growth'])}, a turnaround option on 18A/14A plus government backing), Marvell, Advantest, Tokyo Electron and ASE.
- **Equipment** (ASML, AMAT, LRCX, KLAC) needs 35–46% stage-1 growth: plausible only if WFE stays at records through 2027–28.
- **Street targets** imply +{pct(f.loc[tick,'analyst_target_upside'].mean())} upside on average (median {pct(f.loc[tick,'analyst_target_upside'].median())}). Sell-side optimism is well documented (ch.12/27), so treat these as relative, not absolute, signals.

---

## 11. Momentum & technicals (BKM ch.11–12)

{t_tech}

- **Momentum** (12-1-month; Jegadeesh-Titman, ch.11) is extreme in memory (MU {pct(tech.loc['MU','mom_12_1'])}, SK hynix {pct(tech.loc['000660.KS','mom_12_1'])}), Samsung, ASE, AMD, Intel and Marvell.
- **Overbought (RSI > 70):** {names(tech.loc[tick][tech.loc[tick,'RSI14'] > 70].index)}. **Oversold (RSI < 30):** {names(tech.loc[tick][tech.loc[tick,'RSI14'] < 30].index)}.
- **Below the 200-day average:** {names(tech.loc[tick][tech.loc[tick,'px_vs_200dma'] < 0].index)}. These are candidates for mean reversion (DeBondt-Thaler) *if* fundamentals hold.
- **EMH caveat:** these signals are weak-form information. Ch.12 supports momentum as a behavioral anomaly (underreaction, then overreaction), but momentum crashes after sharp reversals are its known failure mode.

---

## 12. Options market view (BKM ch.21)

{t_opt}

- Implied vol is **below** trailing realized vol for {(ivrv < 1).sum()} of {len(ivrv)} US-listed names (NVDA IV/RV {num(opt.loc['NVDA','iv_rv_ratio'])}, MU {num(opt.loc['MU','iv_rv_ratio'])}). Options are relatively cheap for hedging concentrated gains, e.g. protective puts or collars (ch.20).
- The implied ±1σ one-month move is ±9–21% (NVDA ±{pct(opt.loc['NVDA','implied_1m_1sd_move'],0)}, INTC ±{pct(opt.loc['INTC','implied_1m_1sd_move'],0)}). Use these to size positions.
- IV > RV for {names(ivrv[ivrv > 1].index)}: the market is pricing event risk (export controls, China, earnings).

![IV vs RV](charts/10_implied_vs_realized_vol.png)

---

## 13. Portfolio construction (BKM ch.6–8, 27)

**Correlation & diversification (ch.7)**
![Correlation](charts/05_correlation_heatmap.png)

{t_div}

Diversification within semis stops at ~{pct(div.sd_equal_weight.iloc[-1])} σ, roughly 2.4× SPY. The remaining covariance is the *sector factor*, which can only be diversified away across sectors, or hedged with SOXX/NQ futures (ch.23).

**Efficient frontier.** Expected returns = CAPM + de-biased, shrunk analyst alpha. The covariance matrix is single-index (ch.8), long-only, ≤10% per name.

![Frontier](charts/04_efficient_frontier.png)

{t_pst}

{t_port}

**Capital allocation (ch.6):** $y^* = [E(r_P) - r_f]/(A\\sigma_P^2)$ applied to the tangency portfolio:

{t_cal}

**Treynor-Black active portfolio (ch.27).** Alphas are 12-month analyst-implied returns minus CAPM. The average optimism bias ({pct(tbs['analyst_optimism_bias_removed'])}) is removed, and the remainder is shrunk by {A['alpha_shrink']}. The active portfolio is then combined with SPY:

- Active weight $w_A^* =$ {pct(tbs['w_A_star'])}; index weight {pct(tbs['w_M_star'])}; active β {num(tbs['beta_A'])}; IR {num(tbs['IR_active'])}.
- Ex-ante Sharpe improves from {num(tbs['Sharpe_market_ex_ante'])} (index alone) to {num(tbs['Sharpe_optimal'])}, using $S_P^2 = S_M^2 + IR^2$.

{t_tb}

The largest positive tilts are {names(tbw_t.index[:5])} (the Street sees the most upside relative to their risk). The largest underweights/shorts are {names(tbw_t.index[-4:][::-1])} (priced above consensus targets). The unconstrained Treynor-Black portfolio is long/short and leveraged. Ch.27 recommends constraining tracking risk, so prefer the long-only max-Sharpe portfolio above for implementation.

---

## 14. Composite scorecard

Equal-weight z-scores:
- **Quality:** EBIT margin, ROE, FCF conversion, low accruals.
- **Valuation:** low PVGO/P, high FCF yield, low implied perpetual g, low forward P/E.
- **Risk:** low β, low σ, shallow drawdown.
- **Momentum:** 12-1 momentum, 6M relative strength vs SOXX.
- **Risk-adjusted performance:** Sharpe, information ratio.

{t_sc}

![Scorecard](charts/09_scorecard.png)

> **Caveat:** memory ranks at the top partly because its forward P/E is low, which is exactly the ch.17 peak-earnings trap. Read the composite together with sections 9–10, not in isolation.

---

## 15. PEST analysis — global semiconductor supply chain (Sept 2026)

### P — Political / legal
| Factor | Current state | Who is exposed (+/−) |
|---|---|---|
| **US Section 232 chip tariffs** | 25% tariff on certain imported advanced semis & tools since 15 Jan 2026; exemptions for US data centers/R&D/domestic-capacity use with end-use certification | − importers without US fabs; + US-fab owners (INTC, TXN, MU, GFS), TSMC Arizona, AMKR Arizona |
| **US–Taiwan deal (Jan 2026)** | Tariff relief for Taiwanese firms expanding US capacity | + TSM, ASX (US build-outs); cost headwind to margins |
| **Export controls on China** | AI-chip licenses moved to case-by-case review with strict certifications; re-export within China largely prohibited; tool controls persist | − NVDA/AMD China revenue, AMAT/LRCX/KLAC/TEL/ASML China share (was 30–45% of WFE sales); + SMIC domestic substitution |
| **China critical-mineral controls** | Gallium (~98% of global refined supply), germanium, rare earths; the suspension of US-directed controls **expires 27 Nov 2026** | − compound semis/RF/power (IFX, QCOM RF), wafer/polishing chem; + ex-China material suppliers |
| **Industrial policy** | US CHIPS: USD 30.9bn of 52.7bn awarded to 19 firms across 40 projects; **US government equity stake in Intel**; CHIPS investment tax credit **sunsets for fab starts after 31 Dec 2026**. EU Chips Act 2.0 (materials focus); Japan (Rapidus 2nm, TSMC Kumamoto) | + INTC, MU, TXN, GFS, Samsung Taylor, TSM Arizona; equipment demand pulled forward into 2026 |
| **Taiwan Strait** | Persistent tail risk; ~90% of leading-edge logic and most CoWoS is in Taiwan | Systemic, for TSM and all of its customers; the core reason for "China+1 / US-onshore" |

### E — Economic
| Factor | Current state | Implication (BKM link) |
|---|---|---|
| **AI capex supercycle** | Hyperscaler capex ~USD 600bn in 2026 (+~70% YoY); semis revenue forecast ~USD 975bn–1.3tn | Demand shock ⇒ output, prices and margins up together (ch.17); highest DOL names benefit most |
| **Memory/HBM** | HBM market ~USD 55bn (+58%); DRAM ASPs up sharply; capacity shifting from commodity DRAM to HBM | Classic cyclical: peak margins, low P/E, negative PVGO; the watch-item is capacity additions in 2027 |
| **Bottlenecks** | CoWoS sold out for 2026 (~1m wafers; NVIDIA ~60%); N2 booked into 2028 | Pricing power for TSM/ASX/Disco/Advantest; volume risk if AI demand pauses |
| **Rates & discount rates** | 13-wk bill {pct(A['rf_13w_tbill'],2)}, 10-yr {pct(A['rf_10y_treasury'],2)}; inflation above target | High k (11–21%) ⇒ long-duration growth equity is rate-sensitive (ch.18); a 1% change in k moves DCF value 10–25% (see DCF_Sensitivity sheet) |
| **FX** | Weak yen; KRW recently firmer | Japanese exporters gain local earnings, but USD investors lose on translation (ch.25) |
| **Concentration** | AI is ~half of chip revenue but a sliver of units; top-3 customers hold 85% of CoWoS | High customer concentration raises σ(e); consumer, auto and industrial (TXN, IFX, QCOM) are late-cycle recovery options |

### S — Social
| Factor | Current state | Implication |
|---|---|---|
| **Talent shortage** | ~50k additional US technicians and engineers needed by 2030; fab timelines slipping | Execution risk for greenfield fabs (INTC Ohio, TSM/Samsung/MU US sites); wage inflation |
| **Energy & water (ESG)** | Fab permits increasingly tied to grid upgrades and clean-power mandates; water recycling in Arizona | Capex creep; opportunity for power semis (IFX SiC/GaN) and efficiency |
| **Consumer electronics affordability** | Memory reallocation to AI raises PC and phone costs | Weaker unit demand for QCOM and consumer MCU; supports memory pricing |
| **Public attitudes to AI** | Enthusiasm plus "AI bubble" narratives; retail options activity | Behavioral finance (ch.12): extrapolation, overconfidence, momentum; crash risk if narratives flip |

### T — Technological
| Factor | Current state | Winners / risk |
|---|---|---|
| **2nm GAA + backside power** | TSMC N2 in volume with five fabs ramping in 2026; A16 (backside power) in 2H26; Intel 18A/14A | + ASM (ALD/epi), AMAT, LRCX, KLAC (process control intensity rises); TSM lead widens |
| **High-NA EUV** | In use at Intel; TSMC adopting post-A16 | + ASML (ASP roughly 2× low-NA), Tokyo Electron (tracks), Lasertec |
| **Advanced packaging (CoWoS, SoIC, hybrid bonding, glass substrates)** | CoWoS capacity growing ~80% CAGR, still the binding constraint | + TSM, ASX, AMKR, Disco, Advantest/TER, BESI, Ibiden |
| **HBM3E → HBM4 (logic base die)** | SK hynix leads, then Samsung and Micron; HBM4 base die made at TSMC | + SK hynix, MU; test intensity rises (Advantest) |
| **Custom silicon (ASICs)** | Hyperscalers' in-house XPUs | + AVGO, MRVL, ARM (IP), SNPS/CDNS (more tape-outs); a relative threat to NVDA's share |
| **China domestic tools/nodes** | Push toward sub-7nm self-sufficiency by ~2028 | + SMIC, Naura/AMEC; − long-run China share for Western WFE |
| **AI-driven EDA & chiplets (UCIe)** | Design complexity rising exponentially | + SNPS, CDNS (secular, less cyclical); ARM chiplet ecosystems |

---

## 16. Putting it together — segment verdicts

| Segment | Life-cycle stage (ch.17) | Cyclicality / β | What the numbers say | Key PEST sensitivity |
|---|---|---|---|---|
| **AI fabless (NVDA, AVGO, MRVL, AMD)** | Rapid growth | β 1.4–2.5 | Best risk-adjusted performance (NVDA/AVGO); NVDA/AVGO are the *least* stretched relative to fundamentals; AMD/MRVL price in far more | Export controls, custom-ASIC substitution, hyperscaler capex |
| **IP/EDA (ARM, SNPS, CDNS)** | Mature-growth "toll roads" | β(SPY) 1.1–1.2 (ARM 3.9); SNPS/CDNS ~0.5 to SOXX | SNPS/CDNS de-rated and below 200DMA, a defensive sleeve; ARM is the most expensive stock in the universe | China licensing, AI-EDA adoption |
| **Foundry/IDM (TSM, Samsung, INTC, GFS, SMIC, TXN, IFX)** | Mixed | β 0.4–2.2 | TSM: top quality with moderate implied growth; INTC: turnaround option; TXN/IFX: early-recovery analog/power | Tariffs, Taiwan risk, CHIPS subsidies |
| **Memory (MU, SK hynix, Samsung)** | Cyclical at a (possibly structural) peak | β 2.2–2.3; highest DOL | Top momentum and alpha, but negative PVGO: the market expects mean reversion | 2027 capacity, HBM4 share, China DRAM |
| **Equipment (ASML, AMAT, LRCX, KLAC, TEL, ASMI, Disco, Advantest, TER)** | Growth tied to capex cycle | β 1.4–2.0 | Implied 35–75% stage-1 growth; KLAC/LRCX best Sharpe; Disco and TEL lagging | China WFE share, High-NA timing, the CHIPS 2026 cliff |
| **Materials & OSAT (Shin-Etsu, ENTG, ASX, AMKR)** | Mature / capacity build | β 1.3–2.2 | ASE is the momentum winner (CoWoS overflow); Shin-Etsu/ENTG lag; OSATs burn FCF on capex | Gallium/germanium controls, US onshoring |

### How to use this (ch.28 investment-policy framing)
1. **Core–satellite.** Treat semis as a *satellite* to a diversified core. Their σ (~38% historically for an equal-weight basket) and 25–70% drawdowns matter here. Even if semis were your *only* risky asset, y* would be just 23–46% for A = 4–8 (see the capital-allocation table). Alongside a diversified core, a 10–25% allocation is a reasonable range for moderate risk aversion.
2. **Within the satellite:** spread across chokepoints (the correlation matrix shows EDA, analog and China foundry diversify the AI-heavy core). Size positions by σ(e) using Treynor-Black logic, and cap single names at about 10%.
3. **Hedge the factor, not the stock:** use SOXX puts/collars (IV currently below RV) or index futures (ch.22–23) to neutralize the sector beta while keeping stock-specific views.
4. **Monitor:** Nov-27 critical-minerals deadline, Dec-31 CHIPS credit sunset, CoWoS/N2 capacity announcements, HBM contract pricing, hyperscaler capex guidance, 10-year yield (drives k), USD/JPY and USD/KRW.

---

## Appendix — Methodology & assumptions
| Item | Choice | Book reference |
|---|---|---|
| Returns | Monthly total returns (adjusted close), converted to USD daily at spot FX; window {A['stats_window']} (ARM since its 2023 IPO, GFS since 2021) | ch.5, 25 |
| Risk-free | Lagged 13-wk T-bill (monthly); 10-yr UST for cost of equity | ch.5, 9 |
| Market | SPY for CAPM/index model; SOXX sector β; ACWI global β in the xlsx | ch.8–9 |
| MRP | {pct(A['market_risk_premium'],1)} forward-looking (hist. US arithmetic ≈8%; SPY 5Y realized {pct(A['SPY_hist_excess_ret_ann'],1)}) | ch.5, 9 |
| Betas | OLS on 60m excess returns; Blume adjustment | ch.8 |
| Factors | Fama-French 5 + momentum (Ken French library, through {A['FF_factors_through']}) | ch.10, 13 |
| Valuation | Forward P/E, PVGO, ROE×b, constant-growth P/E, two-stage FCF with 10-yr fade to {pct(A['terminal_growth'],0)}, reverse-DCF implied growth, ±1% k / 3–5% g sensitivity | ch.18 |
| Fundamentals | Latest fiscal-year statements (DuPont), TTM from the vendor for FCF/EBITDA; FX-converted where reporting ≠ listing currency (TSM/ASX TWD, ASML EUR, SMIC USD) | ch.19 |
| Active portfolio | Analyst-target alpha, de-biased by the cross-sectional mean, shrunk ×{A['alpha_shrink']}; Treynor-Black; long-only max-Sharpe with 10% caps on single-index covariance | ch.7–8, 27 |
| Limitations | 5 years includes an extreme AI regime (non-stationary); vendor fundamentals have errors; forward EPS is consensus; DCFs are illustrative, not price targets; survivorship (today's winners chosen *ex post*) inflates historical Sharpe/α | ch.11–13, 24 |
"""
import shutil
SITE.mkdir(parents=True, exist_ok=True)
shutil.copytree(OUT / "charts", SITE / "charts", dirs_exist_ok=True)
shutil.copy(OUT / "Silicon_Supply_Chain_Analysis.xlsx", SITE / "Silicon_Supply_Chain_Analysis.xlsx")
(SITE / "index.md").write_text(report)
print("site page written", len(report.split()), "words")
