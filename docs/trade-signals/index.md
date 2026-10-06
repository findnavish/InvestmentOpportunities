---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-06 17:12 UTC (Tue Oct 06, 01:12 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Tue 13:12) · Tokyo 🔴 closed (Wed 02:12) · Korea 🔴 closed (Wed 02:12) · Hong Kong 🔴 closed (Wed 01:12) · Xetra 🔴 closed (Tue 19:12) · Euronext Amsterdam 🔴 closed (Tue 19:12)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,054,951** | $132,534 (13%) | $922,416 (87%) | +5.50% | +4.61% | 🟢 Risk-on (+29.2%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,054,951), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **KLAC**<br><small>KLA Corp</small> | 189 | 198.10 USD | $37,441 | Executed (paper) | quality +0.24 · trend -0.09 |
| TRIM | **AVGO**<br><small>Broadcom</small> | 36 | 377.64 USD | $13,595 | Executed (paper) | analyst α +0.41 · momentum -0.26 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.98 | **SK hynix**<br><small>000660.KS</small> | 1,780,000 KRW | +76% | +12.9% | +385% | +25% | 51 | +0.62 | 9.3% → 10.0% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.37 | **MU**<br><small>Micron Technology</small> | 1,062.65 USD | +43% | +4.6% | +442% | +54% | 57 | +0.12 | 9.3% → 10.0% | – | momentum +0.53 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.02 | **Samsung**<br><small>005930.KS</small> | 272,000 KRW | +76% | +13.5% | +224% | +20% | 53 | -0.26 | 9.3% → 10.0% | – | analyst α +0.85 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.55 | **KLAC**<br><small>KLA Corp</small> | 198.10 USD | +18% | -0.9% | +69% | +11% | 57 | +0.51 | 8.5% → 8.5% | ADD 189 | quality +0.24 · trend -0.09 |
| 🟢 Buy | +0.51 | **NVDA**<br><small>NVIDIA</small> | 239.89 USD | +37% | +3.0% | +23% | +19% | 68 | +0.47 | 8.4% → 8.6% | – | analyst α +0.27 · quality +0.21 |
| 🟢 Buy | +0.48 | **AMAT**<br><small>Applied Materials</small> | 532.29 USD | +20% | -0.5% | +110% | +24% | 65 | +0.03 | 6.5% → 6.8% | – | analyst α +0.12 · momentum +0.07 |
| 🟢 Buy | +0.47 | **ASX**<br><small>ASE Technology</small> | 46.83 USD | +9% | -1.6% | +242% | +52% | 66 | -0.68 | 6.7% → 7.4% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.40 | **TSM**<br><small>TSMC</small> | 483.17 USD | +14% | -1.6% | +48% | +25% | 73 | +0.58 | 8.6% → 8.1% | – | quality +0.28 · momentum -0.07 |
| 🟢 Buy | +0.37 | **Infineon**<br><small>IFX.DE</small> | 64.69 EUR | +34% | +2.5% | +83% | +16% | 64 | -0.04 | 6.4% → 6.2% | – | analyst α +0.23 · trend -0.06 |
| 🟢 Buy | +0.28 | **AVGO**<br><small>Broadcom</small> | 377.64 USD | +41% | +4.9% | +6% | +3% | 60 | +0.26 | 4.8% → 4.8% | TRIM 36 | analyst α +0.41 · momentum -0.26 |
| ⚪ Hold | +0.14 | **Tokyo Electron**<br><small>8035.T</small> | 12,905 JPY | +18% | -1.0% | +111% | +33% | 70 | -0.28 | 4.6% → 4.6% | – | quality -0.18 · trend +0.10 |
| ⚪ Hold | +0.04 | **ASML**<br><small>ASML Holding</small> | 1,848.14 USD | +13% | -2.3% | +67% | +19% | 62 | +0.42 | 0.0% → 0.0% | – | quality +0.18 · analyst α -0.15 |
| ⚪ Hold | -0.04 | **Advantest**<br><small>6857.T</small> | 41,820 JPY | +2% | -5.5% | +117% | +52% | 74 | +0.33 | 5.0% → 5.0% | – | analyst α -0.48 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | -0.10 | **MRVL**<br><small>Marvell Technology</small> | 282.37 USD | +4% | -5.2% | +160% | +67% | 68 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | -0.12 | **LRCX**<br><small>Lam Research</small> | 332.76 USD | +13% | -2.6% | +112% | +20% | 59 | +0.02 | 0.0% → 0.0% | – | analyst α -0.19 · momentum +0.12 |
| ⚪ Hold | -0.15 | **GFS**<br><small>GlobalFoundries</small> | 48.79 USD | +56% | +8.2% | +26% | -10% | 53 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.25 |
| 🔴 Sell | -0.29 | **ASMI**<br><small>ASM.AS</small> | 949.00 EUR | +19% | -1.2% | +58% | +19% | 69 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · momentum -0.05 |
| 🔴 Sell | -0.35 | **Disco**<br><small>6146.T</small> | 65,300 JPY | +25% | +0.9% | +17% | +0% | 71 | +0.06 | 0.0% → 0.0% | – | momentum -0.23 · analyst α +0.19 |
| 🔴 Sell | -0.36 | **AMD**<br><small>Advanced Micro Devices</small> | 654.40 USD | -5% | -7.7% | +190% | +73% | 73 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.46 | **TXN**<br><small>Texas Instruments</small> | 297.46 USD | +9% | -2.6% | +47% | +20% | 72 | +0.24 | 0.0% → 0.0% | – | analyst α -0.23 · momentum -0.10 |
| 🔴 Sell | -0.53 | **Shin-Etsu**<br><small>4063.T</small> | 6,318 JPY | +23% | +0.8% | +29% | +2% | 67 | -0.20 | 0.0% → 0.0% | – | trend -0.16 · analyst α +0.15 |
| 🔴 Sell | -0.53 | **QCOM**<br><small>Qualcomm</small> | 180.89 USD | +7% | -3.3% | +2% | +8% | 49 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · momentum -0.30 |
| 🔴 Sell | -0.64 | **TER**<br><small>Teradyne</small> | 428.67 USD | +4% | -4.7% | +146% | +27% | 61 | -0.31 | 0.0% → 0.0% | – | analyst α -0.36 · quality -0.21 |
| 🔴 Sell | -0.72 | **AMKR**<br><small>Amkor Technology</small> | 54.22 USD | +41% | +4.2% | +64% | -5% | 54 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.31 |
| 🔴🔴 Strong Sell | -0.79 | **ENTG**<br><small>Entegris</small> | 168.16 USD | +3% | -4.6% | +41% | +27% | 70 | -0.02 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.12 |
| 🔴🔴 Strong Sell | -0.88 | **INTC**<br><small>Intel</small> | 114.08 USD | +2% | -5.7% | +160% | +39% | 54 | -0.62 | 0.0% → 0.0% | – | analyst α -0.55 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.90 | **SMIC**<br><small>0981.HK</small> | 61.55 HKD | +56% | +9.5% | -12% | -11% | 41 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.01 | **CDNS**<br><small>Cadence Design Systems</small> | 360.01 USD | +13% | -2.0% | -16% | +10% | 74 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -1.47 | **ARM**<br><small>Arm Holdings</small> | 302.70 USD | -5% | -8.7% | +65% | +39% | 57 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.12 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.50 | **SNPS**<br><small>Synopsys</small> | 502.51 USD | +13% | -1.9% | -16% | +13% | 76 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · analyst α -0.08 · ⚠️ overbought |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +2.98"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,780,000 KRW (+76%, 38 analysts); de-biased α +12.9% vs CAPM hurdle 14.3%. Uptrend +25% vs 200-day avg; 12-1 mom +385%; RSI 51. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.37"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 1,062.65 USD (+43%, 46 analysts); de-biased α +4.6% vs CAPM hurdle 14.0%. Uptrend +54% vs 200-day avg; 12-1 mom +442%; RSI 57. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.02"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 272,000 KRW (+76%, 36 analysts); de-biased α +13.5% vs CAPM hurdle 11.3%. Uptrend +20% vs 200-day avg; 12-1 mom +224%; RSI 53. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.55"
    **ADD 189 sh** → target 8.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 233.77 USD vs 198.10 USD (+18%, 26 analysts); de-biased α -0.9% vs CAPM hurdle 11.1%. Uptrend +11% vs 200-day avg; 12-1 mom +69%; RSI 57. Quality z +0.51 (ROE 87%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.51"
    Within rebalance band of target 8.6%: no trade. Analyst target 327.70 USD vs 239.89 USD (+37%, 59 analysts); de-biased α +3.0% vs CAPM hurdle 13.9%. Uptrend +19% vs 200-day avg; 12-1 mom +23%; RSI 68. Quality z +0.47 (ROE 101%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.48"
    Within rebalance band of target 6.8%: no trade. Analyst target 638.94 USD vs 532.29 USD (+20%, 36 analysts); de-biased α -0.5% vs CAPM hurdle 11.6%. Uptrend +24% vs 200-day avg; 12-1 mom +110%; RSI 65. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.47"
    Within rebalance band of target 7.4%: no trade. Analyst target 51.00 USD vs 46.83 USD (+9%, 1 analysts); de-biased α -1.6% vs CAPM hurdle 11.9%. Uptrend +52% vs 200-day avg; 12-1 mom +242%; RSI 66. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.40"
    Within rebalance band of target 8.1%: no trade. Analyst target 552.26 USD vs 483.17 USD (+14%, 20 analysts); de-biased α -1.6% vs CAPM hurdle 10.8%. Uptrend +25% vs 200-day avg; 12-1 mom +48%; RSI 73. Quality z +0.58 (ROE 35%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.37"
    Within rebalance band of target 6.2%: no trade. Analyst target 86.74 EUR vs 64.69 EUR (+34%, 23 analysts); de-biased α +2.5% vs CAPM hurdle 14.1%. Uptrend +16% vs 200-day avg; 12-1 mom +83%; RSI 64. Quality z -0.04 (ROE 6%).

??? success "AVGO (AVGO) — 🟢 Buy, score +0.28"
    **TRIM 36 sh** → target 4.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 531.31 USD vs 377.64 USD (+41%, 47 analysts); de-biased α +4.9% vs CAPM hurdle 11.2%. Uptrend +3% vs 200-day avg; 12-1 mom +6%; RSI 60. Quality z +0.26 (ROE 31%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 12,905 JPY (+18%, 23 analysts); de-biased α -1.0% vs CAPM hurdle 12.8%. Uptrend +33% vs 200-day avg; 12-1 mom +111%; RSI 70. Quality z -0.28 (ROE 29%).

??? note "ASML (ASML) — ⚪ Hold, score +0.04"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,848.14 USD (+13%, 16 analysts); de-biased α -2.3% vs CAPM hurdle 12.3%. Uptrend +19% vs 200-day avg; 12-1 mom +67%; RSI 62. Quality z +0.42 (ROE 50%).

??? note "Advantest (6857.T) — ⚪ Hold, score -0.04"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 41,820 JPY (+2%, 21 analysts); de-biased α -5.5% vs CAPM hurdle 13.4%. Uptrend +52% vs 200-day avg; 12-1 mom +117%; RSI 74. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 282.37 USD (+4%, 43 analysts); de-biased α -5.2% vs CAPM hurdle 14.1%. Uptrend +67% vs 200-day avg; 12-1 mom +160%; RSI 68. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 332.76 USD (+13%, 31 analysts); de-biased α -2.6% vs CAPM hurdle 12.6%. Uptrend +20% vs 200-day avg; 12-1 mom +112%; RSI 59. Quality z +0.02 (ROE 65%).

??? note "GFS (GFS) — ⚪ Hold, score -0.15"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.79 USD (+56%, 22 analysts); de-biased α +8.2% vs CAPM hurdle 12.4%. Downtrend -10% vs 200-day avg; 12-1 mom +26%; RSI 53. Quality z -0.21 (ROE 8%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.29"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 949.00 EUR (+19%, 19 analysts); de-biased α -1.2% vs CAPM hurdle 13.2%. Uptrend +19% vs 200-day avg; 12-1 mom +58%; RSI 69. Quality z -0.10 (ROE 19%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 81,730 JPY vs 65,300 JPY (+25%, 20 analysts); de-biased α +0.9% vs CAPM hurdle 11.5%. Uptrend +0% vs 200-day avg; 12-1 mom +17%; RSI 71. Quality z +0.06 (ROE 25%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 619.51 USD vs 654.40 USD (-5%, 50 analysts); de-biased α -7.7% vs CAPM hurdle 14.9%. Uptrend +73% vs 200-day avg; 12-1 mom +190%; RSI 73. Quality z -0.15 (ROE 7%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.46"
    Avoid: not owned. Analyst target 324.71 USD vs 297.46 USD (+9%, 31 analysts); de-biased α -2.6% vs CAPM hurdle 10.8%. Uptrend +20% vs 200-day avg; 12-1 mom +47%; RSI 72. Quality z +0.24 (ROE 30%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.53"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,318 JPY (+23%, 17 analysts); de-biased α +0.8% vs CAPM hurdle 10.8%. Uptrend +2% vs 200-day avg; 12-1 mom +29%; RSI 67. Quality z -0.20 (ROE 10%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.53"
    Avoid: not owned. Analyst target 194.13 USD vs 180.89 USD (+7%, 30 analysts); de-biased α -3.3% vs CAPM hurdle 11.9%. Uptrend +8% vs 200-day avg; 12-1 mom +2%; RSI 49. Quality z +0.70 (ROE 23%).

??? failure "TER (TER) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 446.47 USD vs 428.67 USD (+4%, 15 analysts); de-biased α -4.7% vs CAPM hurdle 12.3%. Uptrend +27% vs 200-day avg; 12-1 mom +146%; RSI 61. Quality z -0.31 (ROE 20%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.72"
    Avoid: not owned. Analyst target 76.40 USD vs 54.22 USD (+41%, 10 analysts); de-biased α +4.2% vs CAPM hurdle 14.0%. Downtrend -5% vs 200-day avg; 12-1 mom +64%; RSI 54. Quality z -1.00 (ROE 9%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.79"
    Avoid: not owned. Analyst target 173.36 USD vs 168.16 USD (+3%, 11 analysts); de-biased α -4.6% vs CAPM hurdle 11.0%. Uptrend +27% vs 200-day avg; 12-1 mom +41%; RSI 70. Quality z -0.02 (ROE 6%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -0.88"
    Avoid: not owned. Analyst target 116.37 USD vs 114.08 USD (+2%, 43 analysts); de-biased α -5.7% vs CAPM hurdle 14.0%. Uptrend +39% vs 200-day avg; 12-1 mom +160%; RSI 54. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.90"
    Avoid: not owned. Analyst target 95.99 HKD vs 61.55 HKD (+56%, 21 analysts); de-biased α +9.5% vs CAPM hurdle 7.3%. Downtrend -11% vs 200-day avg; 12-1 mom -12%; RSI 41. Quality z -0.99 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 405.47 USD vs 360.01 USD (+13%, 26 analysts); de-biased α -2.0% vs CAPM hurdle 10.0%. Uptrend +10% vs 200-day avg; 12-1 mom -16%; RSI 74. Quality z +0.31 (ROE 22%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.47"
    Avoid: not owned. Analyst target 288.70 USD vs 302.70 USD (-5%, 40 analysts); de-biased α -8.7% vs CAPM hurdle 19.6%. Uptrend +39% vs 200-day avg; 12-1 mom +65%; RSI 57. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.50"
    Avoid: not owned. Analyst target 569.78 USD vs 502.51 USD (+13%, 26 analysts); de-biased α -1.9% vs CAPM hurdle 10.3%. Uptrend +13% vs 200-day avg; 12-1 mom -16%; RSI 76. Quality z +0.14 (ROE 7%). ⚠️ overbought (RSI penalty applied).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 005930.KS | Samsung Electronics | 485 | 272,000 KRW | $98,591 | 9.3% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,780,000 KRW | $98,442 | 9.3% | Strong Buy |
| MU | Micron Technology | 92 | 1,062.65 USD | $97,764 | 9.3% | Strong Buy |
| TSM | TSMC | 187 | 483.17 USD | $90,352 | 8.6% | Buy |
| KLAC | KLA Corp | 450 | 198.10 USD | $89,145 | 8.5% | Buy |
| NVDA | NVIDIA | 371 | 239.89 USD | $88,999 | 8.4% | Buy |
| ASX | ASE Technology | 1,509 | 46.83 USD | $70,666 | 6.7% | Buy |
| AMAT | Applied Materials | 128 | 532.29 USD | $68,134 | 6.5% | Buy |
| IFX.DE | Infineon Technologies | 932 | 64.69 EUR | $67,888 | 6.4% | Buy |
| 6857.T | Advantest | 200 | 41,820 JPY | $52,879 | 5.0% | Hold |
| AVGO | Broadcom | 134 | 377.64 USD | $50,604 | 4.8% | Buy |
| 8035.T | Tokyo Electron | 600 | 12,905 JPY | $48,953 | 4.6% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-09-24 08:59 UTC | BUY (new) | IFX.DE | 1,552 | 56.56 | $99,956 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 10.7%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
