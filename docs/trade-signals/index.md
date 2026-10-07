---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-07 21:59 UTC (Wed Oct 07, 05:59 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Wed 17:59) · Tokyo 🔴 closed (Thu 06:59) · Korea 🔴 closed (Thu 06:59) · Hong Kong 🔴 closed (Thu 05:59) · Xetra 🔴 closed (Wed 23:59) · Euronext Amsterdam 🔴 closed (Wed 23:59)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,040,208** | $168,480 (16%) | $871,728 (84%) | +4.02% | +3.06% | 🟢 Risk-on (+26.9%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,040,208), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **Infineon**<br><small>IFX.DE</small> | 318 | 60.80 EUR | $21,653 | Queued · Xetra closed | analyst α +0.31 · trend -0.10 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.34 | **SK hynix**<br><small>000660.KS</small> | 1,729,000 KRW | +82% | +13.6% | +371% | +20% | 47 | +0.62 | 9.2% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.20 | **MU**<br><small>Micron Technology</small> | 1,087.83 USD | +40% | +3.2% | +424% | +57% | 60 | +0.12 | 9.6% → 10.0% | – | momentum +0.53 · analyst α +0.27 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.66 | **Samsung**<br><small>005930.KS</small> | 270,000 KRW | +77% | +13.2% | +210% | +18% | 52 | -0.26 | 9.4% → 10.0% | – | analyst α +0.66 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.50 | **TSM**<br><small>TSMC</small> | 472.15 USD | +17% | -1.5% | +46% | +22% | 65 | +0.58 | 8.5% → 10.0% | – | quality +0.28 · momentum -0.07 |
| 🟢 Buy | +0.48 | **NVDA**<br><small>NVIDIA</small> | 237.36 USD | +38% | +2.8% | +22% | +18% | 64 | +0.47 | 8.5% → 8.7% | – | analyst α +0.23 · quality +0.21 |
| 🟢 Buy | +0.48 | **AMAT**<br><small>Applied Materials</small> | 520.65 USD | +23% | -0.4% | +112% | +21% | 60 | +0.03 | 6.4% → 7.4% | – | momentum +0.10 · analyst α +0.08 |
| 🟢 Buy | +0.46 | **Infineon**<br><small>IFX.DE</small> | 60.80 EUR | +43% | +4.0% | +78% | +9% | 53 | -0.04 | 6.1% → 8.2% | ADD 318 | analyst α +0.31 · trend -0.10 |
| 🟢 Buy | +0.36 | **ASX**<br><small>ASE Technology</small> | 45.77 USD | +11% | -1.6% | +253% | +48% | 61 | -0.68 | 6.6% → 6.1% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.31 | **KLAC**<br><small>KLA Corp</small> | 196.78 USD | +19% | -1.3% | +67% | +10% | 56 | +0.51 | 5.0% → 5.2% | – | quality +0.24 · trend -0.07 |
| ⚪ Hold | +0.22 | **ASML**<br><small>ASML Holding</small> | 1,804.70 USD | +16% | -2.2% | +70% | +16% | 56 | +0.42 | 0.0% → 0.0% | – | quality +0.18 · analyst α -0.08 |
| ⚪ Hold | +0.17 | **AVGO**<br><small>Broadcom</small> | 376.27 USD | +41% | +4.4% | +10% | +3% | 59 | +0.26 | 4.8% → 4.8% | – | analyst α +0.36 · momentum -0.26 |
| ⚪ Hold | +0.09 | **Tokyo Electron**<br><small>8035.T</small> | 12,570 JPY | +22% | -0.8% | +99% | +29% | 65 | -0.28 | 4.6% → 4.6% | – | quality -0.18 · trend +0.10 |
| ⚪ Hold | +0.08 | **Advantest**<br><small>6857.T</small> | 41,340 JPY | +3% | -5.8% | +116% | +49% | 72 | +0.33 | 5.0% → 5.0% | – | analyst α -0.41 · trend +0.18 · ⚠️ rich valuation |
| ⚪ Hold | -0.10 | **GFS**<br><small>GlobalFoundries</small> | 48.06 USD | +58% | +8.2% | +26% | -11% | 51 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.25 |
| ⚪ Hold | -0.11 | **ASMI**<br><small>ASM.AS</small> | 899.00 EUR | +26% | -0.1% | +59% | +13% | 57 | -0.10 | 0.0% → 0.0% | – | analyst α +0.12 · quality -0.06 |
| ⚪ Hold | -0.16 | **LRCX**<br><small>Lam Research</small> | 329.33 USD | +14% | -2.9% | +116% | +19% | 57 | +0.02 | 0.0% → 0.0% | – | analyst α -0.23 · momentum +0.14 |
| ⚪ Hold | -0.17 | **MRVL**<br><small>Marvell Technology</small> | 284.73 USD | +3% | -6.0% | +154% | +68% | 68 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.25 · ⚠️ rich valuation |
| 🔴 Sell | -0.35 | **Disco**<br><small>6146.T</small> | 61,290 JPY | +33% | +2.4% | +13% | -6% | 58 | +0.06 | 0.0% → 0.0% | – | momentum -0.23 · analyst α +0.19 |
| 🔴 Sell | -0.38 | **TXN**<br><small>Texas Instruments</small> | 288.95 USD | +12% | -2.4% | +46% | +16% | 62 | +0.24 | 0.0% → 0.0% | – | analyst α -0.15 · momentum -0.10 |
| 🔴 Sell | -0.47 | **AMKR**<br><small>Amkor Technology</small> | 52.30 USD | +46% | +4.9% | +67% | -9% | 50 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.41 |
| 🔴 Sell | -0.52 | **TER**<br><small>Teradyne</small> | 411.53 USD | +8% | -4.2% | +152% | +22% | 55 | -0.31 | 0.0% → 0.0% | – | analyst α -0.31 · quality -0.21 |
| 🔴 Sell | -0.53 | **QCOM**<br><small>Qualcomm</small> | 177.12 USD | +10% | -3.4% | +5% | +5% | 46 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · momentum -0.30 |
| 🔴 Sell | -0.55 | **AMD**<br><small>Advanced Micro Devices</small> | 645.83 USD | -4% | -8.0% | +148% | +69% | 71 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.59 | **Shin-Etsu**<br><small>4063.T</small> | 6,264 JPY | +24% | +0.4% | +25% | +1% | 63 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · trend -0.16 |
| 🔴🔴 Strong Sell | -0.82 | **INTC**<br><small>Intel</small> | 113.06 USD | +3% | -6.0% | +186% | +37% | 53 | -0.62 | 0.0% → 0.0% | – | analyst α -0.55 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.86 | **ENTG**<br><small>Entegris</small> | 166.23 USD | +4% | -4.9% | +41% | +25% | 68 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.12 |
| 🔴🔴 Strong Sell | -0.91 | **SMIC**<br><small>0981.HK</small> | 60.90 HKD | +58% | +9.3% | -11% | -12% | 39 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.17 | **SNPS**<br><small>Synopsys</small> | 502.51 USD | +13% | -2.5% | -18% | +13% | 75 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -1.24 | **CDNS**<br><small>Cadence Design Systems</small> | 356.23 USD | +14% | -2.3% | -20% | +9% | 71 | +0.31 | 0.0% → 0.0% | – | momentum -0.53 · quality +0.13 |
| 🔴🔴 Strong Sell | -1.44 | **ARM**<br><small>Arm Holdings</small> | 294.41 USD | -2% | -8.7% | +67% | +35% | 53 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.12 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.34"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,729,000 KRW (+82%, 38 analysts); de-biased α +13.6% vs CAPM hurdle 14.3%. Uptrend +20% vs 200-day avg; 12-1 mom +371%; RSI 47. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.20"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 1,087.83 USD (+40%, 46 analysts); de-biased α +3.2% vs CAPM hurdle 14.0%. Uptrend +57% vs 200-day avg; 12-1 mom +424%; RSI 60. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.66"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 270,000 KRW (+77%, 36 analysts); de-biased α +13.2% vs CAPM hurdle 11.3%. Uptrend +18% vs 200-day avg; 12-1 mom +210%; RSI 52. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "TSM (TSM) — 🟢 Buy, score +0.50"
    Within rebalance band of target 10.0%: no trade. Analyst target 552.26 USD vs 472.15 USD (+17%, 20 analysts); de-biased α -1.5% vs CAPM hurdle 10.8%. Uptrend +22% vs 200-day avg; 12-1 mom +46%; RSI 65. Quality z +0.58 (ROE 35%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.48"
    Within rebalance band of target 8.7%: no trade. Analyst target 327.70 USD vs 237.36 USD (+38%, 59 analysts); de-biased α +2.8% vs CAPM hurdle 13.9%. Uptrend +18% vs 200-day avg; 12-1 mom +22%; RSI 64. Quality z +0.47 (ROE 101%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.48"
    Within rebalance band of target 7.4%: no trade. Analyst target 638.94 USD vs 520.65 USD (+23%, 36 analysts); de-biased α -0.4% vs CAPM hurdle 11.6%. Uptrend +21% vs 200-day avg; 12-1 mom +112%; RSI 60. Quality z +0.03 (ROE 36%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.46"
    **ADD 318 sh** → target 8.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 60.80 EUR (+43%, 23 analysts); de-biased α +4.0% vs CAPM hurdle 14.1%. Uptrend +9% vs 200-day avg; 12-1 mom +78%; RSI 53. Quality z -0.04 (ROE 6%).

??? success "ASX (ASX) — 🟢 Buy, score +0.36"
    Within rebalance band of target 6.1%: no trade. Analyst target 51.00 USD vs 45.77 USD (+11%, 1 analysts); de-biased α -1.6% vs CAPM hurdle 11.9%. Uptrend +48% vs 200-day avg; 12-1 mom +253%; RSI 61. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.31"
    Within rebalance band of target 5.2%: no trade. Analyst target 233.77 USD vs 196.78 USD (+19%, 26 analysts); de-biased α -1.3% vs CAPM hurdle 11.1%. Uptrend +10% vs 200-day avg; 12-1 mom +67%; RSI 56. Quality z +0.51 (ROE 87%).

??? note "ASML (ASML) — ⚪ Hold, score +0.22"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,804.70 USD (+16%, 16 analysts); de-biased α -2.2% vs CAPM hurdle 12.3%. Uptrend +16% vs 200-day avg; 12-1 mom +70%; RSI 56. Quality z +0.42 (ROE 50%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.17"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 376.27 USD (+41%, 47 analysts); de-biased α +4.4% vs CAPM hurdle 11.2%. Uptrend +3% vs 200-day avg; 12-1 mom +10%; RSI 59. Quality z +0.26 (ROE 31%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.09"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 12,570 JPY (+22%, 23 analysts); de-biased α -0.8% vs CAPM hurdle 12.8%. Uptrend +29% vs 200-day avg; 12-1 mom +99%; RSI 65. Quality z -0.28 (ROE 29%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 41,340 JPY (+3%, 21 analysts); de-biased α -5.8% vs CAPM hurdle 13.4%. Uptrend +49% vs 200-day avg; 12-1 mom +116%; RSI 72. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "GFS (GFS) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.06 USD (+58%, 22 analysts); de-biased α +8.2% vs CAPM hurdle 12.4%. Downtrend -11% vs 200-day avg; 12-1 mom +26%; RSI 51. Quality z -0.21 (ROE 8%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.11"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 899.00 EUR (+26%, 19 analysts); de-biased α -0.1% vs CAPM hurdle 13.2%. Uptrend +13% vs 200-day avg; 12-1 mom +59%; RSI 57. Quality z -0.10 (ROE 19%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.16"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 329.33 USD (+14%, 31 analysts); de-biased α -2.9% vs CAPM hurdle 12.6%. Uptrend +19% vs 200-day avg; 12-1 mom +116%; RSI 57. Quality z +0.02 (ROE 65%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.17"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 284.73 USD (+3%, 43 analysts); de-biased α -6.0% vs CAPM hurdle 14.1%. Uptrend +68% vs 200-day avg; 12-1 mom +154%; RSI 68. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 81,730 JPY vs 61,290 JPY (+33%, 20 analysts); de-biased α +2.4% vs CAPM hurdle 11.5%. Downtrend -6% vs 200-day avg; 12-1 mom +13%; RSI 58. Quality z +0.06 (ROE 25%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 324.71 USD vs 288.95 USD (+12%, 31 analysts); de-biased α -2.4% vs CAPM hurdle 10.8%. Uptrend +16% vs 200-day avg; 12-1 mom +46%; RSI 62. Quality z +0.24 (ROE 30%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.47"
    Avoid: not owned. Analyst target 76.40 USD vs 52.30 USD (+46%, 10 analysts); de-biased α +4.9% vs CAPM hurdle 14.0%. Downtrend -9% vs 200-day avg; 12-1 mom +67%; RSI 50. Quality z -1.00 (ROE 9%).

??? failure "TER (TER) — 🔴 Sell, score -0.52"
    Avoid: not owned. Analyst target 446.47 USD vs 411.53 USD (+8%, 15 analysts); de-biased α -4.2% vs CAPM hurdle 12.3%. Uptrend +22% vs 200-day avg; 12-1 mom +152%; RSI 55. Quality z -0.31 (ROE 20%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.53"
    Avoid: not owned. Analyst target 194.13 USD vs 177.12 USD (+10%, 30 analysts); de-biased α -3.4% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +5%; RSI 46. Quality z +0.70 (ROE 23%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 619.51 USD vs 645.83 USD (-4%, 50 analysts); de-biased α -8.0% vs CAPM hurdle 14.9%. Uptrend +69% vs 200-day avg; 12-1 mom +148%; RSI 71. Quality z -0.15 (ROE 7%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,264 JPY (+24%, 17 analysts); de-biased α +0.4% vs CAPM hurdle 10.8%. Uptrend +1% vs 200-day avg; 12-1 mom +25%; RSI 63. Quality z -0.20 (ROE 10%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 116.37 USD vs 113.06 USD (+3%, 43 analysts); de-biased α -6.0% vs CAPM hurdle 14.0%. Uptrend +37% vs 200-day avg; 12-1 mom +186%; RSI 53. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.86"
    Avoid: not owned. Analyst target 173.36 USD vs 166.23 USD (+4%, 11 analysts); de-biased α -4.9% vs CAPM hurdle 11.0%. Uptrend +25% vs 200-day avg; 12-1 mom +41%; RSI 68. Quality z -0.02 (ROE 6%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 95.99 HKD vs 60.90 HKD (+58%, 21 analysts); de-biased α +9.3% vs CAPM hurdle 7.3%. Downtrend -12% vs 200-day avg; 12-1 mom -11%; RSI 39. Quality z -0.99 (ROE 3%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.17"
    Avoid: not owned. Analyst target 569.78 USD vs 502.51 USD (+13%, 26 analysts); de-biased α -2.5% vs CAPM hurdle 10.3%. Uptrend +13% vs 200-day avg; 12-1 mom -18%; RSI 75. Quality z +0.14 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.24"
    Avoid: not owned. Analyst target 405.47 USD vs 356.23 USD (+14%, 26 analysts); de-biased α -2.3% vs CAPM hurdle 10.0%. Uptrend +9% vs 200-day avg; 12-1 mom -20%; RSI 71. Quality z +0.31 (ROE 22%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.44"
    Avoid: not owned. Analyst target 288.70 USD vs 294.41 USD (-2%, 40 analysts); de-biased α -8.7% vs CAPM hurdle 19.6%. Uptrend +35% vs 200-day avg; 12-1 mom +67%; RSI 53. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 92 | 1,087.83 USD | $100,081 | 9.6% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 270,000 KRW | $97,771 | 9.4% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,729,000 KRW | $95,528 | 9.2% | Strong Buy |
| TSM | TSMC | 187 | 472.15 USD | $88,292 | 8.5% | Buy |
| NVDA | NVIDIA | 371 | 237.36 USD | $88,061 | 8.5% | Buy |
| ASX | ASE Technology | 1,509 | 45.77 USD | $69,067 | 6.6% | Buy |
| AMAT | Applied Materials | 128 | 520.65 USD | $66,643 | 6.4% | Buy |
| IFX.DE | Infineon Technologies | 932 | 60.80 EUR | $63,462 | 6.1% | Buy |
| KLAC | KLA Corp | 266 | 196.78 USD | $52,343 | 5.0% | Buy |
| 6857.T | Advantest | 200 | 41,340 JPY | $52,327 | 5.0% | Hold |
| AVGO | Broadcom | 134 | 376.27 USD | $50,420 | 4.8% | Hold |
| 8035.T | Tokyo Electron | 600 | 12,570 JPY | $47,732 | 4.6% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-07 16:29 UTC | TRIM | KLAC | -184 | 195.46 | $35,964 |
| 2026-10-06 17:12 UTC | ADD | KLAC | 189 | 198.10 | $37,441 |
| 2026-10-06 17:12 UTC | TRIM | AVGO | -36 | 377.64 | $13,595 |
| 2026-10-06 10:19 UTC | ADD | IFX.DE | 316 | 63.45 | $22,554 |
| 2026-10-05 16:01 UTC | TRIM | KLAC | -208 | 203.82 | $42,395 |
| 2026-10-02 18:25 UTC | ADD | AMAT | 37 | 538.40 | $19,921 |
| 2026-10-02 12:37 UTC | TRIM | IFX.DE | -589 | 62.56 | $41,458 |
| 2026-10-02 05:39 UTC | TRIM | 6857.T | -100 | 38,710.00 | $24,524 |
| 2026-10-01 19:32 UTC | BUY (new) | ASX | 1,509 | 44.67 | $67,415 |
| 2026-10-01 05:56 UTC | TRIM | 6857.T | -100 | 37,090.00 | $23,417 |
| 2026-10-01 05:56 UTC | TRIM | 8035.T | -100 | 12,505.00 | $7,895 |
| 2026-09-30 19:21 UTC | TRIM | NVDA | -76 | 230.81 | $17,541 |
| 2026-09-30 13:45 UTC | TRIM | IFX.DE | -347 | 59.55 | $23,474 |
| 2026-09-30 00:28 UTC | BUY (new) | 8035.T | 700 | 11,900.00 | $52,952 |
| 2026-09-29 15:53 UTC | BUY (new) | TSM | 187 | 457.37 | $85,528 |
| 2026-09-29 15:53 UTC | TRIM | AMAT | -87 | 501.81 | $43,657 |
| 2026-09-29 15:53 UTC | TRIM | AVGO | -112 | 357.74 | $40,067 |
| 2026-09-28 15:29 UTC | BUY (new) | AVGO | 282 | 349.88 | $98,666 |
| 2026-09-28 00:48 UTC | BUY (new) | 005930.KS | 485 | 280,750.00 | $100,255 |
| 2026-09-28 00:48 UTC | BUY (new) | 6857.T | 400 | 34,870.00 | $88,422 |
| 2026-09-28 00:48 UTC | BUY (new) | 000660.KS | 74 | 1,818,500.00 | $99,080 |
| 2026-09-25 14:37 UTC | BUY (new) | KLAC | 469 | 186.53 | $87,480 |
| 2026-09-25 14:37 UTC | BUY (new) | NVDA | 447 | 223.82 | $100,048 |
| 2026-09-25 14:37 UTC | BUY (new) | AMAT | 178 | 479.88 | $85,419 |
| 2026-09-25 14:37 UTC | BUY (new) | MU | 92 | 1,083.05 | $99,641 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 13.1%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
