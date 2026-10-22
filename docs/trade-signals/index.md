---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-22 10:12 UTC (Thu Oct 22, 06:12 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Thu 06:12) · Tokyo 🔴 closed (Thu 19:12) · Korea 🔴 closed (Thu 19:12) · Hong Kong 🔴 closed (Thu 18:12) · Xetra 🟢 open (Thu 12:12) · Euronext Amsterdam 🟢 open (Thu 12:12)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$901,699** | $124,394 (14%) | $777,305 (86%) | -9.83% | -9.78% | 🟢 Risk-on (+8.5%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $901,699), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| – | No trades this hour | | | | | All positions are within their rebalance bands. |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.95 | **MU**<br><small>Micron Technology</small> | 913.62 USD | +66% | +5.2% | +430% | +25% | 40 | +0.12 | 9.3% → 10.0% | – | momentum +0.53 · analyst α +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.00 | **Samsung**<br><small>005930.KS</small> | 215,000 KRW | +122% | +19.9% | +170% | -8% | 36 | -0.26 | 8.7% → 10.0% | – | analyst α +0.85 · momentum +0.20 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.52 | **SK hynix**<br><small>000660.KS</small> | 1,223,000 KRW | – | +0.0% | +309% | -17% | 29 | +0.62 | 10.1% → 9.9% | – | momentum +0.41 · quality +0.33 · ⚠️ oversold, cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +1.02 | **Infineon**<br><small>IFX.DE</small> | 51.21 EUR | +69% | +6.0% | +77% | -10% | 36 | -0.04 | 8.3% → 10.0% | – | analyst α +0.48 · trend -0.10 |
| 🟢 Buy | +0.71 | **AMAT**<br><small>Applied Materials</small> | 408.60 USD | +56% | +3.3% | +111% | -7% | 31 | +0.03 | 7.1% → 6.6% | – | analyst α +0.19 · momentum +0.12 |
| 🟢 Buy | +0.64 | **NVDA**<br><small>NVIDIA</small> | 221.87 USD | +48% | +0.5% | +25% | +9% | 48 | +0.47 | 7.2% → 7.0% | – | quality +0.21 · momentum -0.17 |
| 🟢 Buy | +0.56 | **ASX**<br><small>ASE Technology</small> | 42.42 USD | +20% | -2.8% | +250% | +31% | 48 | -0.68 | 6.3% → 5.7% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.53 | **TSM**<br><small>TSMC</small> | 431.82 USD | +28% | -3.5% | +53% | +9% | 46 | +0.58 | 7.4% → 7.0% | – | quality +0.28 · trend +0.12 |
| 🟢 Buy | +0.51 | **Advantest**<br><small>6857.T</small> | 32,630 JPY | +31% | -3.6% | +68% | +14% | 40 | +0.33 | 2.3% → 3.7% | – | quality +0.16 · trend +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.43 | **KLAC**<br><small>KLA Corp</small> | 163.35 USD | +43% | +0.1% | +65% | -10% | 31 | +0.51 | 3.8% → 4.3% | – | quality +0.24 · trend -0.12 |
| 🟢 Buy | +0.36 | **Tokyo Electron**<br><small>8035.T</small> | 9,499 JPY | +61% | +4.3% | +71% | -5% | 35 | -0.28 | 3.4% → 3.4% | – | analyst α +0.31 · quality -0.18 |
| ⚪ Hold | +0.23 | **LRCX**<br><small>Lam Research</small> | 260.81 USD | +44% | -0.1% | +117% | -8% | 32 | +0.02 | 3.0% → 3.0% | – | momentum +0.14 · trend -0.06 |
| ⚪ Hold | +0.05 | **ASML**<br><small>ASML Holding</small> | 1,675.94 USD | +25% | -4.6% | +71% | +6% | 44 | +0.42 | 5.6% → 5.6% | – | analyst α -0.27 · quality +0.18 |
| ⚪ Hold | +0.03 | **AVGO**<br><small>Broadcom</small> | 337.72 USD | +57% | +3.8% | +4% | -8% | 41 | +0.26 | 3.7% → 3.7% | – | momentum -0.26 · analyst α +0.23 |
| ⚪ Hold | -0.12 | **MRVL**<br><small>Marvell Technology</small> | 244.67 USD | +20% | -6.4% | +210% | +37% | 47 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · momentum +0.26 · ⚠️ rich valuation |
| 🔴 Sell | -0.25 | **Disco**<br><small>6146.T</small> | 50,910 JPY | +61% | +4.5% | -4% | -22% | 36 | +0.06 | 0.0% → 0.0% | – | analyst α +0.36 · momentum -0.30 |
| 🔴 Sell | -0.32 | **AMKR**<br><small>Amkor Technology</small> | 43.72 USD | +75% | +7.4% | +67% | -24% | 37 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 |
| 🔴 Sell | -0.35 | **TER**<br><small>Teradyne</small> | 345.51 USD | +29% | -3.7% | +172% | -0% | 41 | -0.31 | 0.0% → 0.0% | – | momentum +0.23 · quality -0.21 |
| 🔴 Sell | -0.40 | **ASMI**<br><small>ASM.AS</small> | 714.80 EUR | +58% | +3.3% | +52% | -12% | 31 | -0.10 | 0.0% → 0.0% | – | analyst α +0.15 · trend -0.14 |
| 🔴 Sell | -0.41 | **GFS**<br><small>GlobalFoundries</small> | 47.69 USD | +59% | +3.9% | +31% | -13% | 50 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.16 |
| 🔴 Sell | -0.42 | **INTC**<br><small>Intel</small> | 92.90 USD | +25% | -5.1% | +222% | +8% | 36 | -0.62 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.55 | **ARM**<br><small>Arm Holdings</small> | 226.57 USD | +27% | -6.0% | +96% | +0% | 36 | +0.04 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.96 | **QCOM**<br><small>Qualcomm</small> | 177.83 USD | +9% | -8.2% | +19% | +6% | 50 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.99 | **TXN**<br><small>Texas Instruments</small> | 284.85 USD | +14% | -6.7% | +55% | +12% | 56 | +0.24 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.14 |
| 🔴🔴 Strong Sell | -1.00 | **Shin-Etsu**<br><small>4063.T</small> | 5,821 JPY | +33% | -1.9% | +12% | -7% | 41 | -0.20 | 0.0% → 0.0% | – | momentum -0.23 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.05 | **ENTG**<br><small>Entegris</small> | 147.68 USD | +17% | -6.3% | +63% | +8% | 47 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.07 |
| 🔴🔴 Strong Sell | -1.08 | **CDNS**<br><small>Cadence Design Systems</small> | 326.10 USD | +24% | -4.4% | -7% | -0% | 49 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.14 | **AMD**<br><small>Advanced Micro Devices</small> | 552.70 USD | +12% | -8.6% | +158% | +38% | 45 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.23 | **SNPS**<br><small>Synopsys</small> | 451.11 USD | +26% | -4.0% | -10% | +1% | 49 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -1.30 | **SMIC**<br><small>0981.HK</small> | 46.84 HKD | +105% | +16.5% | -18% | -32% | 18 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 · ⚠️ oversold |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.95"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 913.62 USD (+66%, 46 analysts); de-biased α +5.2% vs CAPM hurdle 14.0%. Uptrend +25% vs 200-day avg; 12-1 mom +430%; RSI 40. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.00"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 215,000 KRW (+122%, 36 analysts); de-biased α +19.9% vs CAPM hurdle 11.3%. Downtrend -8% vs 200-day avg; 12-1 mom +170%; RSI 36. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.52"
    Within rebalance band of target 9.9%: no trade. No reliable analyst target: α set to 0. Downtrend -17% vs 200-day avg; 12-1 mom +309%; RSI 29. Quality z +0.62 (ROE 44%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Infineon (IFX.DE) — 🟢🟢 Strong Buy, score +1.02"
    Within rebalance band of target 10.0%: no trade. Analyst target 86.74 EUR vs 51.21 EUR (+69%, 23 analysts); de-biased α +6.0% vs CAPM hurdle 14.1%. Downtrend -10% vs 200-day avg; 12-1 mom +77%; RSI 36. Quality z -0.04 (ROE 6%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.71"
    Within rebalance band of target 6.6%: no trade. Analyst target 638.94 USD vs 408.60 USD (+56%, 36 analysts); de-biased α +3.3% vs CAPM hurdle 11.6%. Downtrend -7% vs 200-day avg; 12-1 mom +111%; RSI 31. Quality z +0.03 (ROE 36%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.64"
    Within rebalance band of target 7.0%: no trade. Analyst target 327.70 USD vs 221.87 USD (+48%, 59 analysts); de-biased α +0.5% vs CAPM hurdle 13.9%. Uptrend +9% vs 200-day avg; 12-1 mom +25%; RSI 48. Quality z +0.47 (ROE 101%).

??? success "ASX (ASX) — 🟢 Buy, score +0.56"
    Within rebalance band of target 5.7%: no trade. Analyst target 51.00 USD vs 42.42 USD (+20%, 1 analysts); de-biased α -2.8% vs CAPM hurdle 11.9%. Uptrend +31% vs 200-day avg; 12-1 mom +250%; RSI 48. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.53"
    Within rebalance band of target 7.0%: no trade. Analyst target 552.26 USD vs 431.82 USD (+28%, 20 analysts); de-biased α -3.5% vs CAPM hurdle 10.8%. Uptrend +9% vs 200-day avg; 12-1 mom +53%; RSI 46. Quality z +0.58 (ROE 35%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.51"
    Within rebalance band of target 3.7%: no trade. Analyst target 42,686 JPY vs 32,630 JPY (+31%, 21 analysts); de-biased α -3.6% vs CAPM hurdle 13.4%. Uptrend +14% vs 200-day avg; 12-1 mom +68%; RSI 40. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.43"
    Within rebalance band of target 4.3%: no trade. Analyst target 233.77 USD vs 163.35 USD (+43%, 26 analysts); de-biased α +0.1% vs CAPM hurdle 11.1%. Downtrend -10% vs 200-day avg; 12-1 mom +65%; RSI 31. Quality z +0.51 (ROE 87%).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.36"
    Within rebalance band of target 3.4%: no trade. Analyst target 15,275 JPY vs 9,499 JPY (+61%, 23 analysts); de-biased α +4.3% vs CAPM hurdle 12.8%. Downtrend -5% vs 200-day avg; 12-1 mom +71%; RSI 35. Quality z -0.28 (ROE 29%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.23"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 260.81 USD (+44%, 31 analysts); de-biased α -0.1% vs CAPM hurdle 12.6%. Downtrend -8% vs 200-day avg; 12-1 mom +117%; RSI 32. Quality z +0.02 (ROE 65%).

??? note "ASML (ASML) — ⚪ Hold, score +0.05"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,675.94 USD (+25%, 16 analysts); de-biased α -4.6% vs CAPM hurdle 12.3%. Uptrend +6% vs 200-day avg; 12-1 mom +71%; RSI 44. Quality z +0.42 (ROE 50%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.03"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 337.72 USD (+57%, 47 analysts); de-biased α +3.8% vs CAPM hurdle 11.2%. Downtrend -8% vs 200-day avg; 12-1 mom +4%; RSI 41. Quality z +0.26 (ROE 31%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 244.67 USD (+20%, 43 analysts); de-biased α -6.4% vs CAPM hurdle 14.1%. Uptrend +37% vs 200-day avg; 12-1 mom +210%; RSI 47. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.25"
    Avoid: not owned. Analyst target 81,730 JPY vs 50,910 JPY (+61%, 20 analysts); de-biased α +4.5% vs CAPM hurdle 11.5%. Downtrend -22% vs 200-day avg; 12-1 mom -4%; RSI 36. Quality z +0.06 (ROE 25%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 76.40 USD vs 43.72 USD (+75%, 10 analysts); de-biased α +7.4% vs CAPM hurdle 14.0%. Downtrend -24% vs 200-day avg; 12-1 mom +67%; RSI 37. Quality z -1.00 (ROE 9%).

??? failure "TER (TER) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 446.47 USD vs 345.51 USD (+29%, 15 analysts); de-biased α -3.7% vs CAPM hurdle 12.3%. Downtrend -0% vs 200-day avg; 12-1 mom +172%; RSI 41. Quality z -0.31 (ROE 20%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.40"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 714.80 EUR (+58%, 19 analysts); de-biased α +3.3% vs CAPM hurdle 13.2%. Downtrend -12% vs 200-day avg; 12-1 mom +52%; RSI 31. Quality z -0.10 (ROE 19%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.41"
    Avoid: not owned. Analyst target 76.00 USD vs 47.69 USD (+59%, 22 analysts); de-biased α +3.9% vs CAPM hurdle 12.4%. Downtrend -13% vs 200-day avg; 12-1 mom +31%; RSI 50. Quality z -0.21 (ROE 8%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.42"
    Avoid: not owned. Analyst target 116.37 USD vs 92.90 USD (+25%, 43 analysts); de-biased α -5.1% vs CAPM hurdle 14.0%. Uptrend +8% vs 200-day avg; 12-1 mom +222%; RSI 36. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "ARM (ARM) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 288.70 USD vs 226.57 USD (+27%, 40 analysts); de-biased α -6.0% vs CAPM hurdle 19.6%. Uptrend +0% vs 200-day avg; 12-1 mom +96%; RSI 36. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.96"
    Avoid: not owned. Analyst target 194.13 USD vs 177.83 USD (+9%, 30 analysts); de-biased α -8.2% vs CAPM hurdle 11.9%. Uptrend +6% vs 200-day avg; 12-1 mom +19%; RSI 50. Quality z +0.70 (ROE 23%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 324.71 USD vs 284.85 USD (+14%, 31 analysts); de-biased α -6.7% vs CAPM hurdle 10.8%. Uptrend +12% vs 200-day avg; 12-1 mom +55%; RSI 56. Quality z +0.24 (ROE 30%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.00"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,821 JPY (+33%, 17 analysts); de-biased α -1.9% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +12%; RSI 41. Quality z -0.20 (ROE 10%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.05"
    Avoid: not owned. Analyst target 173.36 USD vs 147.68 USD (+17%, 11 analysts); de-biased α -6.3% vs CAPM hurdle 11.0%. Uptrend +8% vs 200-day avg; 12-1 mom +63%; RSI 47. Quality z -0.02 (ROE 6%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.08"
    Avoid: not owned. Analyst target 405.47 USD vs 326.10 USD (+24%, 26 analysts); de-biased α -4.4% vs CAPM hurdle 10.0%. Downtrend -0% vs 200-day avg; 12-1 mom -7%; RSI 49. Quality z +0.31 (ROE 22%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.14"
    Avoid: not owned. Analyst target 619.51 USD vs 552.70 USD (+12%, 50 analysts); de-biased α -8.6% vs CAPM hurdle 14.9%. Uptrend +38% vs 200-day avg; 12-1 mom +158%; RSI 45. Quality z -0.15 (ROE 7%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.23"
    Avoid: not owned. Analyst target 569.78 USD vs 451.11 USD (+26%, 26 analysts); de-biased α -4.0% vs CAPM hurdle 10.3%. Uptrend +1% vs 200-day avg; 12-1 mom -10%; RSI 49. Quality z +0.14 (ROE 7%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.30"
    Avoid: not owned. Analyst target 95.99 HKD vs 46.84 HKD (+105%, 21 analysts); de-biased α +16.5% vs CAPM hurdle 7.3%. Downtrend -32% vs 200-day avg; 12-1 mom -18%; RSI 18. Quality z -0.99 (ROE 3%). ⚠️ oversold.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,223,000 KRW | $90,656 | 10.1% | Strong Buy |
| MU | Micron Technology | 92 | 913.62 USD | $84,053 | 9.3% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 215,000 KRW | $78,872 | 8.7% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 51.21 EUR | $74,791 | 8.3% | Strong Buy |
| TSM | TSMC | 154 | 431.82 USD | $66,500 | 7.4% | Buy |
| NVDA | NVIDIA | 294 | 221.87 USD | $65,230 | 7.2% | Buy |
| AMAT | Applied Materials | 156 | 408.60 USD | $63,742 | 7.1% | Buy |
| ASX | ASE Technology | 1,332 | 42.42 USD | $56,497 | 6.3% | Buy |
| ASML | ASML Holding | 30 | 1,675.94 USD | $50,278 | 5.6% | Hold |
| KLAC | KLA Corp | 211 | 163.35 USD | $34,467 | 3.8% | Buy |
| AVGO | Broadcom | 100 | 337.72 USD | $33,772 | 3.7% | Hold |
| 8035.T | Tokyo Electron | 500 | 9,499 JPY | $30,268 | 3.4% | Buy |
| LRCX | Lam Research | 105 | 260.81 USD | $27,385 | 3.0% | Hold |
| 6857.T | Advantest | 100 | 32,630 JPY | $20,795 | 2.3% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-21 19:21 UTC | ADD | TSM | 37 | 430.88 | $15,943 |
| 2026-10-21 15:16 UTC | TRIM | KLAC | -68 | 164.22 | $11,167 |
| 2026-10-20 17:08 UTC | BUY (new) | LRCX | 105 | 263.68 | $27,686 |
| 2026-10-20 17:08 UTC | TRIM | AVGO | -34 | 334.29 | $11,366 |
| 2026-10-20 17:08 UTC | TRIM | NVDA | -77 | 216.83 | $16,696 |
| 2026-10-19 15:37 UTC | TRIM | TSM | -25 | 426.75 | $10,669 |
| 2026-10-19 15:37 UTC | TRIM | ASX | -465 | 41.40 | $19,251 |
| 2026-10-19 01:19 UTC | TRIM | 8035.T | -100 | 10,325.00 | $6,537 |
| 2026-10-16 17:25 UTC | ADD | ASX | 558 | 39.86 | $22,242 |
| 2026-10-16 17:25 UTC | TRIM | TSM | -45 | 412.93 | $18,582 |
| 2026-10-16 12:26 UTC | TRIM | IFX.DE | -293 | 52.84 | $17,423 |
| 2026-10-15 15:02 UTC | ADD | ASX | 339 | 41.52 | $14,077 |
| 2026-10-15 15:02 UTC | TRIM | KLAC | -93 | 172.43 | $16,036 |
| 2026-10-15 04:41 UTC | BUY (new) | 6857.T | 100 | 34,860.00 | $22,075 |
| 2026-10-15 04:41 UTC | ADD | 000660.KS | 24 | 1,270,000.00 | $22,625 |
| 2026-10-14 00:21 UTC | SELL (exit) | 6857.T | -200 | 40,990.00 | $51,779 |
| 2026-10-13 16:00 UTC | BUY (new) | ASML | 30 | 1,699.05 | $50,972 |
| 2026-10-13 16:00 UTC | TRIM | AMAT | -45 | 464.47 | $20,901 |
| 2026-10-13 16:00 UTC | TRIM | ASX | -609 | 47.11 | $28,690 |
| 2026-10-13 07:43 UTC | ADD | IFX.DE | 620 | 54.55 | $37,861 |
| 2026-10-12 17:56 UTC | ADD | KLAC | 153 | 190.68 | $29,174 |
| 2026-10-12 17:56 UTC | ADD | AMAT | 41 | 497.22 | $20,386 |
| 2026-10-09 16:14 UTC | TRIM | KLAC | -47 | 196.81 | $9,250 |
| 2026-10-09 09:06 UTC | TRIM | IFX.DE | -437 | 59.90 | $29,382 |
| 2026-10-08 16:29 UTC | ADD | AMAT | 32 | 522.02 | $16,705 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 31.8%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
