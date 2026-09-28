---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-09-28 15:29 UTC (Mon Sep 28, 11:29 AM ET) · refreshes hourly · weekly model inputs as of 2026-09-25
**Markets:** NYSE/Nasdaq 🟢 open (Mon 11:29) · Tokyo 🔴 closed (Tue 00:29) · Korea 🔴 closed (Tue 00:29) · Hong Kong 🔴 closed (Mon 23:29) · Xetra 🟢 open (Mon 17:29) · Euronext Amsterdam 🟢 open (Mon 17:29)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$988,693** | $140,605 (14%) | $848,088 (86%) | -1.13% | -1.90% | 🟢 Risk-on (+23.5%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $988,693), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **AVGO**<br><small>Broadcom</small> | 282 | 349.88 USD | $98,666 | Executed (paper) | analyst α +0.41 · momentum -0.26 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.07 | **SK hynix**<br><small>000660.KS</small> | 1,780,000 KRW | +79% | +11.1% | +465% | +27% | 51 | +0.63 | 9.8% → 10.0% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.28 | **Samsung**<br><small>005930.KS</small> | 271,500 KRW | +76% | +11.3% | +267% | +21% | 54 | -0.25 | 9.8% → 10.0% | – | analyst α +0.85 · momentum +0.35 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.13 | **MU**<br><small>Micron Technology</small> | 1,041.95 USD | +45% | +2.8% | +497% | +57% | 57 | +0.06 | 9.7% → 10.0% | – | momentum +0.53 · trend +0.25 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.45 | **Advantest**<br><small>6857.T</small> | 33,900 JPY | +26% | -2.0% | +163% | +25% | 54 | +0.33 | 8.7% → 10.0% | – | quality +0.16 · analyst α -0.15 · ⚠️ rich valuation |
| 🟢 Buy | +0.44 | **NVDA**<br><small>NVIDIA</small> | 230.17 USD | +42% | +2.1% | +28% | +15% | 60 | +0.48 | 10.4% → 10.0% | – | momentum -0.23 · quality +0.21 |
| 🟢 Buy | +0.31 | **Infineon**<br><small>IFX.DE</small> | 56.58 EUR | +53% | +4.9% | +74% | +3% | 48 | -0.04 | 10.1% → 10.0% | – | analyst α +0.31 · trend -0.09 |
| 🟢 Buy | +0.31 | **AVGO**<br><small>Broadcom</small> | 349.88 USD | +52% | +5.3% | +11% | -5% | 42 | +0.27 | 10.0% → 10.0% | BUY 282 | analyst α +0.41 · momentum -0.26 |
| 🟢 Buy | +0.30 | **AMAT**<br><small>Applied Materials</small> | 475.26 USD | +35% | +0.8% | +143% | +13% | 52 | +0.03 | 8.6% → 10.0% | – | analyst α +0.08 · momentum +0.07 |
| 🟢 Buy | +0.28 | **KLAC**<br><small>KLA Corp</small> | 184.43 USD | +27% | -1.1% | +74% | +5% | 51 | +0.51 | 8.7% → 10.0% | – | quality +0.24 · trend -0.07 |
| ⚪ Hold | +0.23 | **Tokyo Electron**<br><small>8035.T</small> | 56,610 JPY | +36% | +1.0% | +167% | +15% | 56 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.14 · ⚠️ rich valuation |
| ⚪ Hold | +0.20 | **TSM**<br><small>TSMC</small> | 446.46 USD | +24% | -1.7% | +56% | +17% | 59 | +0.58 | 0.0% → 0.0% | – | quality +0.28 · momentum -0.12 |
| ⚪ Hold | +0.19 | **ASX**<br><small>ASE Technology</small> | 42.96 USD | +19% | -1.6% | +243% | +44% | 59 | -0.68 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.12 | **ASML**<br><small>ASML Holding</small> | 1,747.63 USD | +22% | -2.7% | +84% | +15% | 55 | +0.42 | 0.0% → 0.0% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.01 | **Disco**<br><small>6146.T</small> | 54,670 JPY | +51% | +5.0% | +57% | -16% | 46 | +0.07 | 0.0% → 0.0% | – | analyst α +0.36 · trend -0.32 |
| ⚪ Hold | +0.01 | **GFS**<br><small>GlobalFoundries</small> | 46.96 USD | +62% | +7.3% | +41% | -13% | 49 | -0.21 | 0.0% → 0.0% | – | analyst α +0.55 · trend -0.25 |
| ⚪ Hold | -0.12 | **MRVL**<br><small>Marvell Technology</small> | 250.19 USD | +16% | -4.7% | +189% | +53% | 56 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.23 · ⚠️ rich valuation |
| ⚪ Hold | -0.14 | **AMD**<br><small>Advanced Micro Devices</small> | 600.19 USD | +3% | -8.1% | +196% | +64% | 63 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.27 | **LRCX**<br><small>Lam Research</small> | 307.56 USD | +22% | -2.8% | +150% | +13% | 53 | +0.03 | 0.0% → 0.0% | – | analyst α -0.23 · momentum +0.10 |
| 🔴 Sell | -0.31 | **ASMI**<br><small>ASM.AS</small> | 847.40 EUR | +33% | -0.1% | +60% | +8% | 54 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · trend -0.06 |
| 🔴 Sell | -0.61 | **TER**<br><small>Teradyne</small> | 386.96 USD | +15% | -4.3% | +180% | +17% | 54 | -0.31 | 0.0% → 0.0% | – | analyst α -0.36 · quality -0.21 |
| 🔴 Sell | -0.63 | **Shin-Etsu**<br><small>4063.T</small> | 5,816 JPY | +34% | +1.1% | +39% | -6% | 43 | -0.19 | 0.0% → 0.0% | – | momentum -0.20 · trend -0.16 |
| 🔴 Sell | -0.66 | **AMKR**<br><small>Amkor Technology</small> | 52.12 USD | +47% | +3.2% | +78% | -8% | 51 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.27 |
| 🔴 Sell | -0.71 | **TXN**<br><small>Texas Instruments</small> | 275.82 USD | +18% | -2.8% | +50% | +13% | 58 | +0.24 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.14 |
| 🔴 Sell | -0.72 | **SMIC**<br><small>0981.HK</small> | 61.05 HKD | +55% | +6.7% | +4% | -12% | 38 | -0.98 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.33 |
| 🔴 Sell | -0.73 | **CDNS**<br><small>Cadence Design Systems</small> | 326.70 USD | +24% | -1.6% | -1% | +0% | 62 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · quality +0.13 |
| 🔴🔴 Strong Sell | -0.93 | **ENTG**<br><small>Entegris</small> | 146.00 USD | +19% | -3.0% | +59% | +12% | 54 | -0.02 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.07 |
| 🔴🔴 Strong Sell | -0.95 | **QCOM**<br><small>Qualcomm</small> | 189.09 USD | +3% | -7.0% | -1% | +13% | 56 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.09 | **SNPS**<br><small>Synopsys</small> | 419.99 USD | +32% | +0.3% | -5% | -6% | 57 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · trend -0.14 |
| 🔴🔴 Strong Sell | -1.11 | **INTC**<br><small>Intel</small> | 115.08 USD | +1% | -8.3% | +171% | +45% | 58 | -0.62 | 0.0% → 0.0% | – | analyst α -0.66 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.34 | **ARM**<br><small>Arm Holdings</small> | 284.20 USD | +2% | -9.7% | +81% | +34% | 52 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.14 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.07"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,184,026 KRW vs 1,780,000 KRW (+79%, 37 analysts); de-biased α +11.1% vs CAPM hurdle 14.4%. Uptrend +27% vs 200-day avg; 12-1 mom +465%; RSI 51. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.28"
    Within rebalance band of target 10.0%: no trade. Analyst target 478,628 KRW vs 271,500 KRW (+76%, 36 analysts); de-biased α +11.3% vs CAPM hurdle 11.4%. Uptrend +21% vs 200-day avg; 12-1 mom +267%; RSI 54. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18).

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.13"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,515.54 USD vs 1,041.95 USD (+45%, 46 analysts); de-biased α +2.8% vs CAPM hurdle 14.1%. Uptrend +57% vs 200-day avg; 12-1 mom +497%; RSI 57. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.45"
    Within rebalance band of target 10.0%: no trade. Analyst target 42,567 JPY vs 33,900 JPY (+26%, 21 analysts); de-biased α -2.0% vs CAPM hurdle 13.3%. Uptrend +25% vs 200-day avg; 12-1 mom +163%; RSI 54. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.44"
    Within rebalance band of target 10.0%: no trade. Analyst target 327.70 USD vs 230.17 USD (+42%, 59 analysts); de-biased α +2.1% vs CAPM hurdle 14.0%. Uptrend +15% vs 200-day avg; 12-1 mom +28%; RSI 60. Quality z +0.48 (ROE 101%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.31"
    Within rebalance band of target 10.0%: no trade. Analyst target 86.74 EUR vs 56.58 EUR (+53%, 23 analysts); de-biased α +4.9% vs CAPM hurdle 14.1%. Uptrend +3% vs 200-day avg; 12-1 mom +74%; RSI 48. Quality z -0.04 (ROE 6%).

??? success "AVGO (AVGO) — 🟢 Buy, score +0.31"
    **BUY (new) 282 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 531.85 USD vs 349.88 USD (+52%, 47 analysts); de-biased α +5.3% vs CAPM hurdle 11.2%. Downtrend -5% vs 200-day avg; 12-1 mom +11%; RSI 42. Quality z +0.27 (ROE 31%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.30"
    Within rebalance band of target 10.0%: no trade. Analyst target 640.89 USD vs 475.26 USD (+35%, 35 analysts); de-biased α +0.8% vs CAPM hurdle 11.7%. Uptrend +13% vs 200-day avg; 12-1 mom +143%; RSI 52. Quality z +0.03 (ROE 36%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.28"
    Within rebalance band of target 10.0%: no trade. Analyst target 233.77 USD vs 184.43 USD (+27%, 26 analysts); de-biased α -1.1% vs CAPM hurdle 11.2%. Uptrend +5% vs 200-day avg; 12-1 mom +74%; RSI 51. Quality z +0.51 (ROE 87%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.23"
    Hold zone: not owned, no entry. Analyst target 76,939 JPY vs 56,610 JPY (+36%, 23 analysts); de-biased α +1.0% vs CAPM hurdle 12.7%. Uptrend +15% vs 200-day avg; 12-1 mom +167%; RSI 56. Quality z -0.28 (ROE 29%). ⚠️ price implies 72% stage-1 growth (reverse DCF).

??? note "TSM (TSM) — ⚪ Hold, score +0.20"
    Hold zone: not owned, no entry. Analyst target 552.26 USD vs 446.46 USD (+24%, 20 analysts); de-biased α -1.7% vs CAPM hurdle 10.9%. Uptrend +17% vs 200-day avg; 12-1 mom +56%; RSI 59. Quality z +0.58 (ROE 35%).

??? note "ASX (ASX) — ⚪ Hold, score +0.19"
    Hold zone: not owned, no entry. Analyst target 51.00 USD vs 42.96 USD (+19%, 1 analysts); de-biased α -1.6% vs CAPM hurdle 12.1%. Uptrend +44% vs 200-day avg; 12-1 mom +243%; RSI 59. Quality z -0.68 (ROE 12%). ⚠️ price implies 67% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score +0.12"
    Hold zone: not owned, no entry. Analyst target 2,123.54 USD vs 1,747.63 USD (+22%, 16 analysts); de-biased α -2.7% vs CAPM hurdle 12.4%. Uptrend +15% vs 200-day avg; 12-1 mom +84%; RSI 55. Quality z +0.42 (ROE 50%).

??? note "Disco (6146.T) — ⚪ Hold, score +0.01"
    Hold zone: not owned, no entry. Analyst target 82,580 JPY vs 54,670 JPY (+51%, 20 analysts); de-biased α +5.0% vs CAPM hurdle 11.6%. Downtrend -16% vs 200-day avg; 12-1 mom +57%; RSI 46. Quality z +0.07 (ROE 25%).

??? note "GFS (GFS) — ⚪ Hold, score +0.01"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 46.96 USD (+62%, 22 analysts); de-biased α +7.3% vs CAPM hurdle 12.5%. Downtrend -13% vs 200-day avg; 12-1 mom +41%; RSI 49. Quality z -0.21 (ROE 8%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 289.11 USD vs 250.19 USD (+16%, 43 analysts); de-biased α -4.7% vs CAPM hurdle 14.2%. Uptrend +53% vs 200-day avg; 12-1 mom +189%; RSI 56. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? note "AMD (AMD) — ⚪ Hold, score -0.14"
    Hold zone: not owned, no entry. Analyst target 618.51 USD vs 600.19 USD (+3%, 50 analysts); de-biased α -8.1% vs CAPM hurdle 15.0%. Uptrend +64% vs 200-day avg; 12-1 mom +196%; RSI 63. Quality z -0.15 (ROE 7%).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 373.77 USD vs 307.56 USD (+22%, 31 analysts); de-biased α -2.8% vs CAPM hurdle 12.7%. Uptrend +13% vs 200-day avg; 12-1 mom +150%; RSI 53. Quality z +0.03 (ROE 65%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.31"
    Avoid: not owned. Analyst target 1,125.89 EUR vs 847.40 EUR (+33%, 19 analysts); de-biased α -0.1% vs CAPM hurdle 13.2%. Uptrend +8% vs 200-day avg; 12-1 mom +60%; RSI 54. Quality z -0.10 (ROE 19%).

??? failure "TER (TER) — 🔴 Sell, score -0.61"
    Avoid: not owned. Analyst target 446.47 USD vs 386.96 USD (+15%, 15 analysts); de-biased α -4.3% vs CAPM hurdle 12.5%. Uptrend +17% vs 200-day avg; 12-1 mom +180%; RSI 54. Quality z -0.31 (ROE 20%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.63"
    Avoid: not owned. Analyst target 7,775 JPY vs 5,816 JPY (+34%, 17 analysts); de-biased α +1.1% vs CAPM hurdle 10.8%. Downtrend -6% vs 200-day avg; 12-1 mom +39%; RSI 43. Quality z -0.19 (ROE 10%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.66"
    Avoid: not owned. Analyst target 76.40 USD vs 52.12 USD (+47%, 10 analysts); de-biased α +3.2% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +78%; RSI 51. Quality z -1.00 (ROE 9%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.71"
    Avoid: not owned. Analyst target 324.71 USD vs 275.82 USD (+18%, 31 analysts); de-biased α -2.8% vs CAPM hurdle 10.8%. Uptrend +13% vs 200-day avg; 12-1 mom +50%; RSI 58. Quality z +0.24 (ROE 30%).

??? failure "SMIC (0981.HK) — 🔴 Sell, score -0.72"
    Avoid: not owned. Analyst target 94.39 HKD vs 61.05 HKD (+55%, 22 analysts); de-biased α +6.7% vs CAPM hurdle 7.4%. Downtrend -12% vs 200-day avg; 12-1 mom +4%; RSI 38. Quality z -0.98 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴 Sell, score -0.73"
    Avoid: not owned. Analyst target 405.47 USD vs 326.70 USD (+24%, 26 analysts); de-biased α -1.6% vs CAPM hurdle 10.1%. Uptrend +0% vs 200-day avg; 12-1 mom -1%; RSI 62. Quality z +0.31 (ROE 22%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.93"
    Avoid: not owned. Analyst target 173.36 USD vs 146.00 USD (+19%, 11 analysts); de-biased α -3.0% vs CAPM hurdle 10.9%. Uptrend +12% vs 200-day avg; 12-1 mom +59%; RSI 54. Quality z -0.02 (ROE 6%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.95"
    Avoid: not owned. Analyst target 194.13 USD vs 189.09 USD (+3%, 30 analysts); de-biased α -7.0% vs CAPM hurdle 12.1%. Uptrend +13% vs 200-day avg; 12-1 mom -1%; RSI 56. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.09"
    Avoid: not owned. Analyst target 553.77 USD vs 419.99 USD (+32%, 25 analysts); de-biased α +0.3% vs CAPM hurdle 10.4%. Downtrend -6% vs 200-day avg; 12-1 mom -5%; RSI 57. Quality z +0.14 (ROE 7%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -1.11"
    Avoid: not owned. Analyst target 116.37 USD vs 115.08 USD (+1%, 43 analysts); de-biased α -8.3% vs CAPM hurdle 14.1%. Uptrend +45% vs 200-day avg; 12-1 mom +171%; RSI 58. Quality z -0.62 (ROE -0%). ⚠️ price implies 87% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size.

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.34"
    Avoid: not owned. Analyst target 288.70 USD vs 284.20 USD (+2%, 40 analysts); de-biased α -9.7% vs CAPM hurdle 20.0%. Uptrend +34% vs 200-day avg; 12-1 mom +81%; RSI 52. Quality z +0.04 (ROE 12%). ⚠️ price implies 115% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| NVDA | NVIDIA | 447 | 230.17 USD | $102,886 | 10.4% | Buy |
| IFX.DE | Infineon Technologies | 1,552 | 56.58 EUR | $99,877 | 10.1% | Buy |
| AVGO | Broadcom | 282 | 349.88 USD | $98,666 | 10.0% | Buy |
| 000660.KS | SK hynix | 74 | 1,780,000 KRW | $96,797 | 9.8% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 271,500 KRW | $96,766 | 9.8% | Strong Buy |
| MU | Micron Technology | 92 | 1,041.95 USD | $95,859 | 9.7% | Strong Buy |
| KLAC | KLA Corp | 469 | 184.43 USD | $86,498 | 8.7% | Buy |
| 6857.T | Advantest | 400 | 33,900 JPY | $86,142 | 8.7% | Buy |
| AMAT | Applied Materials | 178 | 475.26 USD | $84,596 | 8.6% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-09-28 15:29 UTC | BUY (new) | AVGO | 282 | 349.88 | $98,666 |
| 2026-09-28 00:48 UTC | BUY (new) | 005930.KS | 485 | 280,750.00 | $100,255 |
| 2026-09-28 00:48 UTC | BUY (new) | 6857.T | 400 | 34,870.00 | $88,422 |
| 2026-09-28 00:48 UTC | BUY (new) | 000660.KS | 74 | 1,818,500.00 | $99,080 |
| 2026-09-25 14:37 UTC | BUY (new) | KLAC | 469 | 186.53 | $87,480 |
| 2026-09-25 14:37 UTC | BUY (new) | NVDA | 447 | 223.82 | $100,048 |
| 2026-09-25 14:37 UTC | BUY (new) | AMAT | 178 | 479.88 | $85,419 |
| 2026-09-25 14:37 UTC | BUY (new) | MU | 92 | 1,083.05 | $99,641 |
| 2026-09-24 08:59 UTC | BUY (new) | IFX.DE | 1,552 | 56.56 | $99,956 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 4.07%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 20.3%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
