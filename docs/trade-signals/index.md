---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-02 05:39 UTC (Fri Oct 02, 01:39 AM ET) · refreshes hourly · weekly model inputs as of 2026-09-25
**Markets:** NYSE/Nasdaq 🔴 closed (Fri 01:39) · Tokyo 🟢 open (Fri 14:39) · Korea 🟢 open (Fri 14:39) · Hong Kong 🟢 open (Fri 13:39) · Xetra 🔴 closed (Fri 07:39) · Euronext Amsterdam 🔴 closed (Fri 07:39)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,030,849** | $115,091 (11%) | $915,758 (89%) | +3.08% | +1.92% | 🟢 Risk-on (+27.2%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,030,849), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **Advantest**<br><small>6857.T</small> | 100 | 38,710 JPY | $24,524 | Executed (paper) | analyst α -0.31 · momentum +0.17 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.06 | **SK hynix**<br><small>000660.KS</small> | 1,844,000 KRW | +73% | +11.1% | +388% | +30% | 56 | +0.63 | 9.8% → 10.0% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.09 | **Samsung**<br><small>005930.KS</small> | 275,250 KRW | +74% | +12.2% | +233% | +22% | 55 | -0.25 | 9.6% → 10.0% | – | analyst α +0.85 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.07 | **MU**<br><small>Micron Technology</small> | 1,097.68 USD | +38% | +2.5% | +426% | +61% | 64 | +0.06 | 9.8% → 10.0% | – | momentum +0.53 · trend +0.25 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.57 | **TSM**<br><small>TSMC</small> | 459.27 USD | +20% | -1.0% | +45% | +19% | 66 | +0.58 | 8.3% → 10.0% | – | quality +0.28 · momentum -0.05 |
| 🟢 Buy | +0.48 | **NVDA**<br><small>NVIDIA</small> | 230.96 USD | +42% | +3.5% | +20% | +15% | 60 | +0.48 | 8.3% → 8.0% | – | analyst α +0.27 · momentum -0.23 |
| 🟢 Buy | +0.43 | **Infineon**<br><small>IFX.DE</small> | 59.60 EUR | +46% | +4.5% | +64% | +8% | 55 | -0.04 | 7.8% → 7.2% | – | analyst α +0.36 · trend -0.12 |
| 🟢 Buy | +0.42 | **ASX**<br><small>ASE Technology</small> | 44.74 USD | +14% | -1.4% | +237% | +47% | 63 | -0.68 | 6.5% → 6.9% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.36 | **AVGO**<br><small>Broadcom</small> | 343.70 USD | +55% | +7.6% | +11% | -6% | 40 | +0.27 | 5.7% → 6.4% | – | analyst α +0.48 · momentum -0.26 |
| 🟢 Buy | +0.32 | **AMAT**<br><small>Applied Materials</small> | 529.07 USD | +21% | -1.1% | +102% | +24% | 67 | +0.03 | 4.7% → 4.7% | – | momentum +0.07 · trend +0.06 |
| 🟢 Buy | +0.30 | **Advantest**<br><small>6857.T</small> | 38,710 JPY | +10% | -4.3% | +144% | +41% | 68 | +0.33 | 4.8% → 3.4% | TRIM 100 | analyst α -0.31 · momentum +0.17 · ⚠️ rich valuation |
| 🟢 Buy | +0.29 | **Tokyo Electron**<br><small>8035.T</small> | 12,045 JPY | – | +0.0% | +137% | +25% | 64 | -0.28 | 4.4% → 4.3% | – | quality -0.18 · momentum +0.12 · ⚠️ rich valuation |
| ⚪ Hold | +0.15 | **ASML**<br><small>ASML Holding</small> | 1,808.57 USD | +17% | -2.1% | +69% | +17% | 60 | +0.42 | 0.0% → 0.0% | – | quality +0.18 · analyst α -0.15 |
| ⚪ Hold | +0.13 | **KLAC**<br><small>KLA Corp</small> | 200.33 USD | +17% | -2.0% | +59% | +13% | 63 | +0.51 | 9.1% → 9.1% | – | quality +0.24 · analyst α -0.08 |
| ⚪ Hold | -0.12 | **TXN**<br><small>Texas Instruments</small> | 281.20 USD | +15% | -1.8% | +45% | +14% | 62 | +0.24 | 0.0% → 0.0% | – | quality +0.10 · momentum -0.07 |
| ⚪ Hold | -0.14 | **AMD**<br><small>Advanced Micro Devices</small> | 615.64 USD | +0% | -7.2% | +179% | +64% | 67 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| ⚪ Hold | -0.18 | **Disco**<br><small>6146.T</small> | 60,050 JPY | +38% | +3.2% | +29% | -7% | 61 | +0.07 | 0.0% → 0.0% | – | analyst α +0.23 · trend -0.21 |
| ⚪ Hold | -0.24 | **ASMI**<br><small>ASM.AS</small> | 898.00 EUR | +25% | -0.4% | +43% | +14% | 62 | -0.10 | 0.0% → 0.0% | – | momentum -0.10 · analyst α +0.08 |
| 🔴 Sell | -0.28 | **LRCX**<br><small>Lam Research</small> | 339.85 USD | +10% | -4.1% | +103% | +24% | 65 | +0.03 | 0.0% → 0.0% | – | analyst α -0.27 · momentum +0.10 |
| 🔴 Sell | -0.31 | **MRVL**<br><small>Marvell Technology</small> | 268.01 USD | +8% | -5.1% | +147% | +61% | 63 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.21 · ⚠️ rich valuation |
| 🔴 Sell | -0.33 | **GFS**<br><small>GlobalFoundries</small> | 48.68 USD | +56% | +7.5% | +23% | -10% | 54 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.25 |
| 🔴 Sell | -0.49 | **Shin-Etsu**<br><small>4063.T</small> | 6,017 JPY | +29% | +1.6% | +35% | -3% | 55 | -0.19 | 0.0% → 0.0% | – | analyst α +0.15 · momentum -0.14 |
| 🔴 Sell | -0.62 | **AMKR**<br><small>Amkor Technology</small> | 52.92 USD | +44% | +4.2% | +61% | -7% | 53 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.31 |
| 🔴 Sell | -0.65 | **QCOM**<br><small>Qualcomm</small> | 182.03 USD | +7% | -4.4% | +4% | +8% | 50 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · analyst α -0.36 |
| 🔴 Sell | -0.72 | **ENTG**<br><small>Entegris</small> | 158.62 USD | +9% | -3.8% | +40% | +20% | 64 | -0.02 | 0.0% → 0.0% | – | analyst α -0.23 · momentum -0.12 |
| 🔴🔴 Strong Sell | -0.83 | **TER**<br><small>Teradyne</small> | 415.79 USD | +7% | -4.7% | +144% | +25% | 62 | -0.31 | 0.0% → 0.0% | – | analyst α -0.41 · quality -0.21 |
| 🔴🔴 Strong Sell | -0.90 | **SMIC**<br><small>0981.HK</small> | 60.35 HKD | +56% | +8.7% | -7% | -13% | 36 | -0.98 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.01 | **INTC**<br><small>Intel</small> | 119.96 USD | -3% | -7.8% | +151% | +48% | 61 | -0.62 | 0.0% → 0.0% | – | analyst α -0.66 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.01 | **CDNS**<br><small>Cadence Design Systems</small> | 350.71 USD | +16% | -2.1% | -13% | +8% | 71 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -1.38 | **ARM**<br><small>Arm Holdings</small> | 292.34 USD | -1% | -8.8% | +66% | +36% | 54 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.12 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.47 | **SNPS**<br><small>Synopsys</small> | 490.53 USD | +13% | -2.9% | -15% | +10% | 74 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · analyst α -0.19 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.06"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,184,026 KRW vs 1,844,000 KRW (+73%, 37 analysts); de-biased α +11.1% vs CAPM hurdle 14.4%. Uptrend +30% vs 200-day avg; 12-1 mom +388%; RSI 56. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.09"
    Within rebalance band of target 10.0%: no trade. Analyst target 478,628 KRW vs 275,250 KRW (+74%, 36 analysts); de-biased α +12.2% vs CAPM hurdle 11.4%. Uptrend +22% vs 200-day avg; 12-1 mom +233%; RSI 55. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18).

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.07"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,515.54 USD vs 1,097.68 USD (+38%, 46 analysts); de-biased α +2.5% vs CAPM hurdle 14.1%. Uptrend +61% vs 200-day avg; 12-1 mom +426%; RSI 64. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18).

??? success "TSM (TSM) — 🟢 Buy, score +0.57"
    Within rebalance band of target 10.0%: no trade. Analyst target 552.26 USD vs 459.27 USD (+20%, 20 analysts); de-biased α -1.0% vs CAPM hurdle 10.9%. Uptrend +19% vs 200-day avg; 12-1 mom +45%; RSI 66. Quality z +0.58 (ROE 35%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.48"
    Within rebalance band of target 8.0%: no trade. Analyst target 327.70 USD vs 230.96 USD (+42%, 59 analysts); de-biased α +3.5% vs CAPM hurdle 14.0%. Uptrend +15% vs 200-day avg; 12-1 mom +20%; RSI 60. Quality z +0.48 (ROE 101%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.43"
    Within rebalance band of target 7.2%: no trade. Analyst target 86.74 EUR vs 59.60 EUR (+46%, 23 analysts); de-biased α +4.5% vs CAPM hurdle 14.1%. Uptrend +8% vs 200-day avg; 12-1 mom +64%; RSI 55. Quality z -0.04 (ROE 6%).

??? success "ASX (ASX) — 🟢 Buy, score +0.42"
    Within rebalance band of target 6.9%: no trade. Analyst target 51.00 USD vs 44.74 USD (+14%, 1 analysts); de-biased α -1.4% vs CAPM hurdle 12.1%. Uptrend +47% vs 200-day avg; 12-1 mom +237%; RSI 63. Quality z -0.68 (ROE 12%). ⚠️ price implies 67% stage-1 growth (reverse DCF).

??? success "AVGO (AVGO) — 🟢 Buy, score +0.36"
    Within rebalance band of target 6.4%: no trade. Analyst target 531.85 USD vs 343.70 USD (+55%, 47 analysts); de-biased α +7.6% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom +11%; RSI 40. Quality z +0.27 (ROE 31%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.32"
    Within rebalance band of target 4.7%: no trade. Analyst target 640.89 USD vs 529.07 USD (+21%, 35 analysts); de-biased α -1.1% vs CAPM hurdle 11.7%. Uptrend +24% vs 200-day avg; 12-1 mom +102%; RSI 67. Quality z +0.03 (ROE 36%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.30"
    **TRIM 100 sh** → target 3.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 42,567 JPY vs 38,710 JPY (+10%, 21 analysts); de-biased α -4.3% vs CAPM hurdle 13.3%. Uptrend +41% vs 200-day avg; 12-1 mom +144%; RSI 68. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.29"
    Within rebalance band of target 4.3%: no trade. No reliable analyst target: α set to 0. Uptrend +25% vs 200-day avg; 12-1 mom +137%; RSI 64. Quality z -0.28 (ROE 29%). ⚠️ price implies 72% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score +0.15"
    Hold zone: not owned, no entry. Analyst target 2,123.54 USD vs 1,808.57 USD (+17%, 16 analysts); de-biased α -2.1% vs CAPM hurdle 12.4%. Uptrend +17% vs 200-day avg; 12-1 mom +69%; RSI 60. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.13"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 200.33 USD (+17%, 26 analysts); de-biased α -2.0% vs CAPM hurdle 11.2%. Uptrend +13% vs 200-day avg; 12-1 mom +59%; RSI 63. Quality z +0.51 (ROE 87%).

??? note "TXN (TXN) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 324.71 USD vs 281.20 USD (+15%, 31 analysts); de-biased α -1.8% vs CAPM hurdle 10.8%. Uptrend +14% vs 200-day avg; 12-1 mom +45%; RSI 62. Quality z +0.24 (ROE 30%).

??? note "AMD (AMD) — ⚪ Hold, score -0.14"
    Hold zone: not owned, no entry. Analyst target 618.51 USD vs 615.64 USD (+0%, 50 analysts); de-biased α -7.2% vs CAPM hurdle 15.0%. Uptrend +64% vs 200-day avg; 12-1 mom +179%; RSI 67. Quality z -0.15 (ROE 7%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 82,580 JPY vs 60,050 JPY (+38%, 20 analysts); de-biased α +3.2% vs CAPM hurdle 11.6%. Downtrend -7% vs 200-day avg; 12-1 mom +29%; RSI 61. Quality z +0.07 (ROE 25%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 1,125.89 EUR vs 898.00 EUR (+25%, 19 analysts); de-biased α -0.4% vs CAPM hurdle 13.2%. Uptrend +14% vs 200-day avg; 12-1 mom +43%; RSI 62. Quality z -0.10 (ROE 19%).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.28"
    Avoid: not owned. Analyst target 373.77 USD vs 339.85 USD (+10%, 31 analysts); de-biased α -4.1% vs CAPM hurdle 12.7%. Uptrend +24% vs 200-day avg; 12-1 mom +103%; RSI 65. Quality z +0.03 (ROE 65%).

??? failure "MRVL (MRVL) — 🔴 Sell, score -0.31"
    Avoid: not owned. Analyst target 289.11 USD vs 268.01 USD (+8%, 43 analysts); de-biased α -5.1% vs CAPM hurdle 14.2%. Uptrend +61% vs 200-day avg; 12-1 mom +147%; RSI 63. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? failure "GFS (GFS) — 🔴 Sell, score -0.33"
    Avoid: not owned. Analyst target 76.00 USD vs 48.68 USD (+56%, 22 analysts); de-biased α +7.5% vs CAPM hurdle 12.5%. Downtrend -10% vs 200-day avg; 12-1 mom +23%; RSI 54. Quality z -0.21 (ROE 8%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 7,775 JPY vs 6,017 JPY (+29%, 17 analysts); de-biased α +1.6% vs CAPM hurdle 10.8%. Downtrend -3% vs 200-day avg; 12-1 mom +35%; RSI 55. Quality z -0.19 (ROE 10%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.62"
    Avoid: not owned. Analyst target 76.40 USD vs 52.92 USD (+44%, 10 analysts); de-biased α +4.2% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +61%; RSI 53. Quality z -1.00 (ROE 9%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.65"
    Avoid: not owned. Analyst target 194.13 USD vs 182.03 USD (+7%, 30 analysts); de-biased α -4.4% vs CAPM hurdle 12.1%. Uptrend +8% vs 200-day avg; 12-1 mom +4%; RSI 50. Quality z +0.70 (ROE 23%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.72"
    Avoid: not owned. Analyst target 173.36 USD vs 158.62 USD (+9%, 11 analysts); de-biased α -3.8% vs CAPM hurdle 10.9%. Uptrend +20% vs 200-day avg; 12-1 mom +40%; RSI 64. Quality z -0.02 (ROE 6%).

??? failure "TER (TER) — 🔴🔴 Strong Sell, score -0.83"
    Avoid: not owned. Analyst target 446.47 USD vs 415.79 USD (+7%, 15 analysts); de-biased α -4.7% vs CAPM hurdle 12.5%. Uptrend +25% vs 200-day avg; 12-1 mom +144%; RSI 62. Quality z -0.31 (ROE 20%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.90"
    Avoid: not owned. Analyst target 94.39 HKD vs 60.35 HKD (+56%, 22 analysts); de-biased α +8.7% vs CAPM hurdle 7.4%. Downtrend -13% vs 200-day avg; 12-1 mom -7%; RSI 36. Quality z -0.98 (ROE 3%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 116.37 USD vs 119.96 USD (-3%, 43 analysts); de-biased α -7.8% vs CAPM hurdle 14.1%. Uptrend +48% vs 200-day avg; 12-1 mom +151%; RSI 61. Quality z -0.62 (ROE -0%). ⚠️ price implies 87% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size.

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 405.47 USD vs 350.71 USD (+16%, 26 analysts); de-biased α -2.1% vs CAPM hurdle 10.1%. Uptrend +8% vs 200-day avg; 12-1 mom -13%; RSI 71. Quality z +0.31 (ROE 22%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.38"
    Avoid: not owned. Analyst target 288.70 USD vs 292.34 USD (-1%, 40 analysts); de-biased α -8.8% vs CAPM hurdle 20.0%. Uptrend +36% vs 200-day avg; 12-1 mom +66%; RSI 54. Quality z +0.04 (ROE 12%). ⚠️ price implies 115% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.47"
    Avoid: not owned. Analyst target 553.77 USD vs 490.53 USD (+13%, 25 analysts); de-biased α -2.9% vs CAPM hurdle 10.4%. Uptrend +10% vs 200-day avg; 12-1 mom -15%; RSI 74. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 92 | 1,097.68 USD | $100,986 | 9.8% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,844,000 KRW | $100,856 | 9.8% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 275,250 KRW | $98,668 | 9.6% | Strong Buy |
| KLAC | KLA Corp | 469 | 200.33 USD | $93,955 | 9.1% | Hold |
| TSM | TSMC | 187 | 459.27 USD | $85,883 | 8.3% | Buy |
| NVDA | NVIDIA | 371 | 230.96 USD | $85,686 | 8.3% | Buy |
| IFX.DE | Infineon Technologies | 1,205 | 59.60 EUR | $80,812 | 7.8% | Buy |
| ASX | ASE Technology | 1,509 | 44.74 USD | $67,505 | 6.5% | Buy |
| AVGO | Broadcom | 170 | 343.70 USD | $58,429 | 5.7% | Buy |
| 6857.T | Advantest | 200 | 38,710 JPY | $49,047 | 4.8% | Buy |
| AMAT | Applied Materials | 91 | 529.07 USD | $48,145 | 4.7% | Buy |
| 8035.T | Tokyo Electron | 600 | 12,045 JPY | $45,785 | 4.4% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 4.07%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 14.0%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
