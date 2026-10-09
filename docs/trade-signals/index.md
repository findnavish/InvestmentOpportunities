---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-09 09:06 UTC (Fri Oct 09, 05:06 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Fri 05:06) · Tokyo 🔴 closed (Fri 18:06) · Korea 🔴 closed (Fri 18:06) · Hong Kong 🔴 closed (Fri 17:06) · Xetra 🟢 open (Fri 11:06) · Euronext Amsterdam 🟢 open (Fri 11:06)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,020,601** | $149,339 (15%) | $871,262 (85%) | +2.06% | -0.41% | 🟢 Risk-on (+22.3%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,020,601), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **Infineon**<br><small>IFX.DE</small> | 437 | 59.90 EUR | $29,382 | Executed (paper) | analyst α +0.27 · trend -0.10 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.40 | **SK hynix**<br><small>000660.KS</small> | 1,699,000 KRW | +85% | +13.7% | +395% | +18% | 45 | +0.62 | 9.2% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.21 | **MU**<br><small>Micron Technology</small> | 1,035.42 USD | +47% | +4.2% | +398% | +48% | 51 | +0.12 | 9.3% → 10.0% | – | momentum +0.53 · analyst α +0.31 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.62 | **Samsung**<br><small>005930.KS</small> | 264,000 KRW | +81% | +13.6% | +223% | +15% | 49 | -0.26 | 9.4% → 10.0% | – | analyst α +0.66 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.62 | **AMAT**<br><small>Applied Materials</small> | 509.76 USD | +25% | -0.4% | +110% | +18% | 56 | +0.03 | 8.0% → 9.4% | – | momentum +0.12 · analyst α +0.12 |
| 🟢 Buy | +0.45 | **NVDA**<br><small>NVIDIA</small> | 230.57 USD | +42% | +3.1% | +16% | +14% | 55 | +0.47 | 8.4% → 8.0% | – | analyst α +0.23 · quality +0.21 |
| 🟢 Buy | +0.45 | **TSM**<br><small>TSMC</small> | 458.05 USD | +21% | -1.3% | +42% | +17% | 55 | +0.58 | 8.4% → 9.5% | – | quality +0.28 · momentum -0.12 |
| 🟢 Buy | +0.42 | **ASX**<br><small>ASE Technology</small> | 45.25 USD | +13% | -1.8% | +239% | +45% | 59 | -0.68 | 6.7% → 7.0% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.37 | **Infineon**<br><small>IFX.DE</small> | 59.90 EUR | +45% | +3.9% | +76% | +7% | 51 | -0.04 | 6.4% → 6.4% | TRIM 437 | analyst α +0.27 · trend -0.10 |
| ⚪ Hold | +0.22 | **KLAC**<br><small>KLA Corp</small> | 196.76 USD | +19% | -1.9% | +68% | +10% | 56 | +0.51 | 5.1% → 5.1% | – | quality +0.24 · trend -0.07 |
| ⚪ Hold | +0.20 | **AVGO**<br><small>Broadcom</small> | 360.15 USD | +48% | +5.3% | +5% | -2% | 49 | +0.26 | 4.7% → 4.7% | – | analyst α +0.41 · momentum -0.30 |
| ⚪ Hold | +0.15 | **ASML**<br><small>ASML Holding</small> | 1,770.29 USD | +18% | -2.3% | +72% | +14% | 51 | +0.42 | 0.0% → 0.0% | – | quality +0.18 · analyst α -0.08 |
| ⚪ Hold | +0.13 | **Tokyo Electron**<br><small>8035.T</small> | 12,430 JPY | +23% | -1.2% | +105% | +27% | 63 | -0.28 | 4.6% → 4.6% | – | quality -0.18 · trend +0.12 |
| ⚪ Hold | -0.02 | **GFS**<br><small>GlobalFoundries</small> | 49.40 USD | +54% | +6.5% | +28% | -9% | 55 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.21 |
| ⚪ Hold | -0.04 | **Advantest**<br><small>6857.T</small> | 41,560 JPY | +3% | -6.6% | +130% | +49% | 71 | +0.33 | 5.1% → 5.1% | – | analyst α -0.55 · trend +0.21 · ⚠️ rich valuation |
| ⚪ Hold | -0.10 | **ASMI**<br><small>ASM.AS</small> | 897.00 EUR | +26% | -0.7% | +53% | +12% | 56 | -0.10 | 0.0% → 0.0% | – | analyst α +0.08 · quality -0.06 |
| ⚪ Hold | -0.12 | **LRCX**<br><small>Lam Research</small> | 320.74 USD | +17% | -2.8% | +110% | +15% | 52 | +0.02 | 0.0% → 0.0% | – | analyst α -0.15 · momentum +0.10 |
| ⚪ Hold | -0.23 | **MRVL**<br><small>Marvell Technology</small> | 274.61 USD | +7% | -5.7% | +146% | +60% | 61 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.25 · ⚠️ rich valuation |
| 🔴 Sell | -0.35 | **Disco**<br><small>6146.T</small> | 61,250 JPY | +33% | +1.7% | +15% | -6% | 58 | +0.06 | 0.0% → 0.0% | – | momentum -0.23 · analyst α +0.19 |
| 🔴 Sell | -0.39 | **TXN**<br><small>Texas Instruments</small> | 288.24 USD | +13% | -3.0% | +46% | +15% | 61 | +0.24 | 0.0% → 0.0% | – | analyst α -0.23 · quality +0.10 |
| 🔴 Sell | -0.45 | **QCOM**<br><small>Qualcomm</small> | 176.03 USD | +10% | -3.9% | +8% | +5% | 45 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · analyst α -0.27 |
| 🔴 Sell | -0.53 | **INTC**<br><small>Intel</small> | 107.14 USD | +9% | -5.3% | +168% | +29% | 46 | -0.62 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.54 | **TER**<br><small>Teradyne</small> | 398.94 USD | +12% | -4.0% | +157% | +17% | 51 | -0.31 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.23 |
| 🔴 Sell | -0.57 | **AMKR**<br><small>Amkor Technology</small> | 51.00 USD | +50% | +5.1% | +74% | -11% | 47 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.36 |
| 🔴 Sell | -0.58 | **Shin-Etsu**<br><small>4063.T</small> | 6,110 JPY | +27% | +0.5% | +25% | -2% | 55 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · trend -0.16 |
| 🔴🔴 Strong Sell | -0.81 | **ENTG**<br><small>Entegris</small> | 162.24 USD | +7% | -4.9% | +46% | +21% | 62 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.10 |
| 🔴🔴 Strong Sell | -0.90 | **SMIC**<br><small>0981.HK</small> | 57.65 HKD | +67% | +10.8% | -15% | -17% | 34 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.35 |
| 🔴🔴 Strong Sell | -0.98 | **CDNS**<br><small>Cadence Design Systems</small> | 348.86 USD | +16% | -2.4% | -19% | +7% | 64 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -0.99 | **AMD**<br><small>Advanced Micro Devices</small> | 620.73 USD | -0% | -7.7% | +114% | +61% | 61 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.19 | **ARM**<br><small>Arm Holdings</small> | 275.43 USD | +5% | -7.7% | +52% | +25% | 47 | +0.04 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.44 | **SNPS**<br><small>Synopsys</small> | 497.84 USD | +14% | -2.9% | -19% | +12% | 72 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · analyst α -0.19 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.40"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,699,000 KRW (+85%, 38 analysts); de-biased α +13.7% vs CAPM hurdle 14.3%. Uptrend +18% vs 200-day avg; 12-1 mom +395%; RSI 45. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.21"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 1,035.42 USD (+47%, 46 analysts); de-biased α +4.2% vs CAPM hurdle 14.0%. Uptrend +48% vs 200-day avg; 12-1 mom +398%; RSI 51. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.62"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 264,000 KRW (+81%, 36 analysts); de-biased α +13.6% vs CAPM hurdle 11.3%. Uptrend +15% vs 200-day avg; 12-1 mom +223%; RSI 49. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.62"
    Within rebalance band of target 9.4%: no trade. Analyst target 638.94 USD vs 509.76 USD (+25%, 36 analysts); de-biased α -0.4% vs CAPM hurdle 11.6%. Uptrend +18% vs 200-day avg; 12-1 mom +110%; RSI 56. Quality z +0.03 (ROE 36%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.45"
    Within rebalance band of target 8.0%: no trade. Analyst target 327.70 USD vs 230.57 USD (+42%, 59 analysts); de-biased α +3.1% vs CAPM hurdle 13.9%. Uptrend +14% vs 200-day avg; 12-1 mom +16%; RSI 55. Quality z +0.47 (ROE 101%).

??? success "TSM (TSM) — 🟢 Buy, score +0.45"
    Within rebalance band of target 9.5%: no trade. Analyst target 552.26 USD vs 458.05 USD (+21%, 20 analysts); de-biased α -1.3% vs CAPM hurdle 10.8%. Uptrend +17% vs 200-day avg; 12-1 mom +42%; RSI 55. Quality z +0.58 (ROE 35%).

??? success "ASX (ASX) — 🟢 Buy, score +0.42"
    Within rebalance band of target 7.0%: no trade. Analyst target 51.00 USD vs 45.25 USD (+13%, 1 analysts); de-biased α -1.8% vs CAPM hurdle 11.9%. Uptrend +45% vs 200-day avg; 12-1 mom +239%; RSI 59. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.37"
    **TRIM 437 sh** → target 6.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 59.90 EUR (+45%, 23 analysts); de-biased α +3.9% vs CAPM hurdle 14.1%. Uptrend +7% vs 200-day avg; 12-1 mom +76%; RSI 51. Quality z -0.04 (ROE 6%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 196.76 USD (+19%, 26 analysts); de-biased α -1.9% vs CAPM hurdle 11.1%. Uptrend +10% vs 200-day avg; 12-1 mom +68%; RSI 56. Quality z +0.51 (ROE 87%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.20"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 360.15 USD (+48%, 47 analysts); de-biased α +5.3% vs CAPM hurdle 11.2%. Downtrend -2% vs 200-day avg; 12-1 mom +5%; RSI 49. Quality z +0.26 (ROE 31%).

??? note "ASML (ASML) — ⚪ Hold, score +0.15"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,770.29 USD (+18%, 16 analysts); de-biased α -2.3% vs CAPM hurdle 12.3%. Uptrend +14% vs 200-day avg; 12-1 mom +72%; RSI 51. Quality z +0.42 (ROE 50%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.13"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 12,430 JPY (+23%, 23 analysts); de-biased α -1.2% vs CAPM hurdle 12.8%. Uptrend +27% vs 200-day avg; 12-1 mom +105%; RSI 63. Quality z -0.28 (ROE 29%).

??? note "GFS (GFS) — ⚪ Hold, score -0.02"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 49.40 USD (+54%, 22 analysts); de-biased α +6.5% vs CAPM hurdle 12.4%. Downtrend -9% vs 200-day avg; 12-1 mom +28%; RSI 55. Quality z -0.21 (ROE 8%).

??? note "Advantest (6857.T) — ⚪ Hold, score -0.04"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 41,560 JPY (+3%, 21 analysts); de-biased α -6.6% vs CAPM hurdle 13.4%. Uptrend +49% vs 200-day avg; 12-1 mom +130%; RSI 71. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 897.00 EUR (+26%, 19 analysts); de-biased α -0.7% vs CAPM hurdle 13.2%. Uptrend +12% vs 200-day avg; 12-1 mom +53%; RSI 56. Quality z -0.10 (ROE 19%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 320.74 USD (+17%, 31 analysts); de-biased α -2.8% vs CAPM hurdle 12.6%. Uptrend +15% vs 200-day avg; 12-1 mom +110%; RSI 52. Quality z +0.02 (ROE 65%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 274.61 USD (+7%, 43 analysts); de-biased α -5.7% vs CAPM hurdle 14.1%. Uptrend +60% vs 200-day avg; 12-1 mom +146%; RSI 61. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 81,730 JPY vs 61,250 JPY (+33%, 20 analysts); de-biased α +1.7% vs CAPM hurdle 11.5%. Downtrend -6% vs 200-day avg; 12-1 mom +15%; RSI 58. Quality z +0.06 (ROE 25%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.39"
    Avoid: not owned. Analyst target 324.71 USD vs 288.24 USD (+13%, 31 analysts); de-biased α -3.0% vs CAPM hurdle 10.8%. Uptrend +15% vs 200-day avg; 12-1 mom +46%; RSI 61. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.45"
    Avoid: not owned. Analyst target 194.13 USD vs 176.03 USD (+10%, 30 analysts); de-biased α -3.9% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +8%; RSI 45. Quality z +0.70 (ROE 23%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.53"
    Avoid: not owned. Analyst target 116.37 USD vs 107.14 USD (+9%, 43 analysts); de-biased α -5.3% vs CAPM hurdle 14.0%. Uptrend +29% vs 200-day avg; 12-1 mom +168%; RSI 46. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "TER (TER) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 446.47 USD vs 398.94 USD (+12%, 15 analysts); de-biased α -4.0% vs CAPM hurdle 12.3%. Uptrend +17% vs 200-day avg; 12-1 mom +157%; RSI 51. Quality z -0.31 (ROE 20%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 76.40 USD vs 51.00 USD (+50%, 10 analysts); de-biased α +5.1% vs CAPM hurdle 14.0%. Downtrend -11% vs 200-day avg; 12-1 mom +74%; RSI 47. Quality z -1.00 (ROE 9%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,110 JPY (+27%, 17 analysts); de-biased α +0.5% vs CAPM hurdle 10.8%. Downtrend -2% vs 200-day avg; 12-1 mom +25%; RSI 55. Quality z -0.20 (ROE 10%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.81"
    Avoid: not owned. Analyst target 173.36 USD vs 162.24 USD (+7%, 11 analysts); de-biased α -4.9% vs CAPM hurdle 11.0%. Uptrend +21% vs 200-day avg; 12-1 mom +46%; RSI 62. Quality z -0.02 (ROE 6%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.90"
    Avoid: not owned. Analyst target 95.99 HKD vs 57.65 HKD (+67%, 21 analysts); de-biased α +10.8% vs CAPM hurdle 7.3%. Downtrend -17% vs 200-day avg; 12-1 mom -15%; RSI 34. Quality z -0.99 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.98"
    Avoid: not owned. Analyst target 405.47 USD vs 348.86 USD (+16%, 26 analysts); de-biased α -2.4% vs CAPM hurdle 10.0%. Uptrend +7% vs 200-day avg; 12-1 mom -19%; RSI 64. Quality z +0.31 (ROE 22%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 619.51 USD vs 620.73 USD (-0%, 50 analysts); de-biased α -7.7% vs CAPM hurdle 14.9%. Uptrend +61% vs 200-day avg; 12-1 mom +114%; RSI 61. Quality z -0.15 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.19"
    Avoid: not owned. Analyst target 288.70 USD vs 275.43 USD (+5%, 40 analysts); de-biased α -7.7% vs CAPM hurdle 19.6%. Uptrend +25% vs 200-day avg; 12-1 mom +52%; RSI 47. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.44"
    Avoid: not owned. Analyst target 569.78 USD vs 497.84 USD (+14%, 26 analysts); de-biased α -2.9% vs CAPM hurdle 10.3%. Uptrend +12% vs 200-day avg; 12-1 mom -19%; RSI 72. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 005930.KS | Samsung Electronics | 485 | 264,000 KRW | $95,453 | 9.4% | Strong Buy |
| MU | Micron Technology | 92 | 1,035.42 USD | $95,259 | 9.3% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,699,000 KRW | $93,727 | 9.2% | Strong Buy |
| TSM | TSMC | 187 | 458.05 USD | $85,655 | 8.4% | Buy |
| NVDA | NVIDIA | 371 | 230.57 USD | $85,541 | 8.4% | Buy |
| AMAT | Applied Materials | 160 | 509.76 USD | $81,562 | 8.0% | Buy |
| ASX | ASE Technology | 1,509 | 45.25 USD | $68,282 | 6.7% | Buy |
| IFX.DE | Infineon Technologies | 974 | 59.90 EUR | $65,487 | 6.4% | Buy |
| 6857.T | Advantest | 200 | 41,560 JPY | $52,548 | 5.1% | Hold |
| KLAC | KLA Corp | 266 | 196.76 USD | $52,338 | 5.1% | Hold |
| AVGO | Broadcom | 134 | 360.15 USD | $48,260 | 4.7% | Hold |
| 8035.T | Tokyo Electron | 600 | 12,430 JPY | $47,149 | 4.6% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-09 09:06 UTC | TRIM | IFX.DE | -437 | 59.90 | $29,382 |
| 2026-10-08 16:29 UTC | ADD | AMAT | 32 | 522.02 | $16,705 |
| 2026-10-08 08:59 UTC | ADD | IFX.DE | 479 | 59.28 | $31,780 |
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 15.9%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
