---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-09-26 19:52 UTC (Sat Sep 26, 03:52 PM ET) · refreshes hourly · weekly model inputs as of 2026-09-25
**Markets:** NYSE/Nasdaq 🔴 closed (Sat 15:52) · Tokyo 🔴 closed (Sun 04:52) · Korea 🔴 closed (Sun 04:52) · Hong Kong 🔴 closed (Sun 03:52) · Xetra 🔴 closed (Sat 21:52) · Euronext Amsterdam 🔴 closed (Sat 21:52)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,002,737** | $527,221 (53%) | $475,516 (47%) | +0.27% | +1.24% | 🟢 Risk-on (+27.8%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,002,737), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **Samsung**<br><small>005930.KS</small> | 478 | 284,250 KRW | $100,253 | Queued · Korea closed | analyst α +0.66 · momentum +0.35 · ⚠️ cycle-peak P/E |
| BUY (new) | **SK hynix**<br><small>000660.KS</small> | 73 | 1,853,000 KRW | $99,809 | Queued · Korea closed | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| BUY (new) | **Advantest**<br><small>6857.T</small> | 400 | 33,890 JPY | $86,242 | Queued · Tokyo closed | quality +0.16 · momentum +0.12 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.45 | **SK hynix**<br><small>000660.KS</small> | 1,853,000 KRW | +72% | +10.1% | +457% | +33% | 57 | +0.63 | 0.0% → 10.0% | BUY 73 | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.04 | **MU**<br><small>Micron Technology</small> | 1,081.69 USD | +40% | +2.2% | +497% | +63% | 63 | +0.06 | 9.9% → 10.0% | – | momentum +0.53 · trend +0.25 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.91 | **Samsung**<br><small>005930.KS</small> | 284,250 KRW | +68% | +10.1% | +265% | +27% | 61 | -0.25 | 0.0% → 10.0% | BUY 478 | analyst α +0.66 · momentum +0.35 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.56 | **Advantest**<br><small>6857.T</small> | 33,890 JPY | +26% | -1.2% | +163% | +25% | 54 | +0.33 | 0.0% → 10.0% | BUY 400 | quality +0.16 · momentum +0.12 · ⚠️ rich valuation |
| 🟢 Buy | +0.42 | **NVDA**<br><small>NVIDIA</small> | 225.08 USD | +46% | +3.6% | +28% | +13% | 55 | +0.48 | 10.0% → 10.0% | – | analyst α +0.27 · momentum -0.23 |
| 🟢 Buy | +0.35 | **AMAT**<br><small>Applied Materials</small> | 485.05 USD | +32% | +0.9% | +143% | +15% | 56 | +0.03 | 8.6% → 10.0% | – | analyst α +0.08 · momentum +0.07 |
| 🟢 Buy | +0.31 | **Infineon**<br><small>IFX.DE</small> | 57.08 EUR | +52% | +5.3% | +74% | +4% | 49 | -0.04 | 10.1% → 10.0% | – | analyst α +0.31 · trend -0.09 |
| ⚪ Hold | +0.22 | **Tokyo Electron**<br><small>8035.T</small> | 56,480 JPY | +36% | +1.9% | +167% | +14% | 56 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.15 · ⚠️ rich valuation |
| ⚪ Hold | +0.21 | **KLAC**<br><small>KLA Corp</small> | 187.91 USD | +24% | -0.9% | +74% | +7% | 54 | +0.51 | 8.8% → 8.8% | – | quality +0.24 · trend -0.07 |
| ⚪ Hold | +0.17 | **TSM**<br><small>TSMC</small> | 450.58 USD | +23% | -1.2% | +56% | +18% | 62 | +0.58 | 0.0% → 0.0% | – | quality +0.28 · momentum -0.12 |
| ⚪ Hold | +0.12 | **AVGO**<br><small>Broadcom</small> | 352.82 USD | +51% | +5.8% | +11% | -4% | 44 | +0.27 | 0.0% → 0.0% | – | analyst α +0.36 · momentum -0.30 |
| ⚪ Hold | +0.12 | **Disco**<br><small>6146.T</small> | 54,400 JPY | +52% | +6.0% | +57% | -16% | 45 | +0.07 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.32 |
| ⚪ Hold | +0.05 | **ASML**<br><small>ASML Holding</small> | 1,742.50 USD | +22% | -1.8% | +84% | +14% | 54 | +0.42 | 0.0% → 0.0% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.05 | **ASX**<br><small>ASE Technology</small> | 44.31 USD | +15% | -1.7% | +243% | +48% | 64 | -0.68 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.01 | **GFS**<br><small>GlobalFoundries</small> | 48.99 USD | +55% | +6.4% | +41% | -9% | 55 | -0.21 | 0.0% → 0.0% | – | analyst α +0.55 · trend -0.25 |
| ⚪ Hold | -0.12 | **MRVL**<br><small>Marvell Technology</small> | 261.89 USD | +10% | -5.2% | +189% | +60% | 63 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.23 · ⚠️ rich valuation |
| ⚪ Hold | -0.14 | **AMD**<br><small>Advanced Micro Devices</small> | 630.35 USD | -2% | -8.5% | +196% | +72% | 73 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| ⚪ Hold | -0.24 | **ASMI**<br><small>ASM.AS</small> | 848.00 EUR | +33% | +0.7% | +60% | +8% | 54 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · trend -0.06 |
| 🔴 Sell | -0.30 | **LRCX**<br><small>Lam Research</small> | 315.29 USD | +19% | -2.8% | +150% | +16% | 56 | +0.03 | 0.0% → 0.0% | – | analyst α -0.27 · momentum +0.10 |
| 🔴 Sell | -0.61 | **TER**<br><small>Teradyne</small> | 398.32 USD | +12% | -4.4% | +180% | +21% | 58 | -0.31 | 0.0% → 0.0% | – | analyst α -0.36 · quality -0.21 |
| 🔴 Sell | -0.62 | **TXN**<br><small>Texas Instruments</small> | 278.01 USD | +17% | -2.3% | +50% | +13% | 60 | +0.24 | 0.0% → 0.0% | – | analyst α -0.23 · momentum -0.14 |
| 🔴 Sell | -0.64 | **SMIC**<br><small>0981.HK</small> | 63.35 HKD | +49% | +6.1% | +13% | -9% | 43 | -0.98 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.33 |
| 🔴 Sell | -0.66 | **CDNS**<br><small>Cadence Design Systems</small> | 326.16 USD | +24% | -0.7% | -1% | +0% | 61 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · quality +0.13 |
| 🔴 Sell | -0.70 | **Shin-Etsu**<br><small>4063.T</small> | 5,887 JPY | +32% | +1.5% | +39% | -5% | 47 | -0.19 | 0.0% → 0.0% | – | momentum -0.20 · trend -0.16 |
| 🔴 Sell | -0.74 | **AMKR**<br><small>Amkor Technology</small> | 53.63 USD | +42% | +2.9% | +78% | -6% | 55 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.23 |
| 🔴🔴 Strong Sell | -0.79 | **ENTG**<br><small>Entegris</small> | 151.90 USD | +14% | -3.4% | +59% | +16% | 60 | -0.02 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.07 |
| 🔴🔴 Strong Sell | -0.82 | **QCOM**<br><small>Qualcomm</small> | 201.95 USD | -4% | -7.9% | -1% | +20% | 68 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.11 | **INTC**<br><small>Intel</small> | 122.96 USD | -5% | -9.2% | +171% | +54% | 67 | -0.62 | 0.0% → 0.0% | – | analyst α -0.66 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.16 | **SNPS**<br><small>Synopsys</small> | 425.76 USD | +30% | +0.6% | -12% | -4% | 60 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · trend -0.14 |
| 🔴🔴 Strong Sell | -1.33 | **ARM**<br><small>Arm Holdings</small> | 310.55 USD | -7% | -11.1% | +81% | +46% | 61 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.14 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.45"
    **BUY (new) 73 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 3,184,026 KRW vs 1,853,000 KRW (+72%, 37 analysts); de-biased α +10.1% vs CAPM hurdle 14.4%. Uptrend +33% vs 200-day avg; 12-1 mom +457%; RSI 57. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.04"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,515.54 USD vs 1,081.69 USD (+40%, 46 analysts); de-biased α +2.2% vs CAPM hurdle 14.1%. Uptrend +63% vs 200-day avg; 12-1 mom +497%; RSI 63. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.91"
    **BUY (new) 478 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 478,628 KRW vs 284,250 KRW (+68%, 36 analysts); de-biased α +10.1% vs CAPM hurdle 11.4%. Uptrend +27% vs 200-day avg; 12-1 mom +265%; RSI 61. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.56"
    **BUY (new) 400 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 42,567 JPY vs 33,890 JPY (+26%, 21 analysts); de-biased α -1.2% vs CAPM hurdle 13.3%. Uptrend +25% vs 200-day avg; 12-1 mom +163%; RSI 54. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.42"
    Within rebalance band of target 10.0%: no trade. Analyst target 327.70 USD vs 225.08 USD (+46%, 59 analysts); de-biased α +3.6% vs CAPM hurdle 14.0%. Uptrend +13% vs 200-day avg; 12-1 mom +28%; RSI 55. Quality z +0.48 (ROE 101%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.35"
    Within rebalance band of target 10.0%: no trade. Analyst target 640.89 USD vs 485.05 USD (+32%, 35 analysts); de-biased α +0.9% vs CAPM hurdle 11.7%. Uptrend +15% vs 200-day avg; 12-1 mom +143%; RSI 56. Quality z +0.03 (ROE 36%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.31"
    Within rebalance band of target 10.0%: no trade. Analyst target 86.74 EUR vs 57.08 EUR (+52%, 23 analysts); de-biased α +5.3% vs CAPM hurdle 14.1%. Uptrend +4% vs 200-day avg; 12-1 mom +74%; RSI 49. Quality z -0.04 (ROE 6%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.22"
    Hold zone: not owned, no entry. Analyst target 76,939 JPY vs 56,480 JPY (+36%, 23 analysts); de-biased α +1.9% vs CAPM hurdle 12.7%. Uptrend +14% vs 200-day avg; 12-1 mom +167%; RSI 56. Quality z -0.28 (ROE 29%). ⚠️ price implies 72% stage-1 growth (reverse DCF).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.21"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 187.91 USD (+24%, 26 analysts); de-biased α -0.9% vs CAPM hurdle 11.2%. Uptrend +7% vs 200-day avg; 12-1 mom +74%; RSI 54. Quality z +0.51 (ROE 87%).

??? note "TSM (TSM) — ⚪ Hold, score +0.17"
    Hold zone: not owned, no entry. Analyst target 552.26 USD vs 450.58 USD (+23%, 20 analysts); de-biased α -1.2% vs CAPM hurdle 10.9%. Uptrend +18% vs 200-day avg; 12-1 mom +56%; RSI 62. Quality z +0.58 (ROE 35%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.12"
    Hold zone: not owned, no entry. Analyst target 531.85 USD vs 352.82 USD (+51%, 47 analysts); de-biased α +5.8% vs CAPM hurdle 11.2%. Downtrend -4% vs 200-day avg; 12-1 mom +11%; RSI 44. Quality z +0.27 (ROE 31%).

??? note "Disco (6146.T) — ⚪ Hold, score +0.12"
    Hold zone: not owned, no entry. Analyst target 82,580 JPY vs 54,400 JPY (+52%, 20 analysts); de-biased α +6.0% vs CAPM hurdle 11.6%. Downtrend -16% vs 200-day avg; 12-1 mom +57%; RSI 45. Quality z +0.07 (ROE 25%).

??? note "ASML (ASML) — ⚪ Hold, score +0.05"
    Hold zone: not owned, no entry. Analyst target 2,123.54 USD vs 1,742.50 USD (+22%, 16 analysts); de-biased α -1.8% vs CAPM hurdle 12.4%. Uptrend +14% vs 200-day avg; 12-1 mom +84%; RSI 54. Quality z +0.42 (ROE 50%).

??? note "ASX (ASX) — ⚪ Hold, score +0.05"
    Hold zone: not owned, no entry. Analyst target 51.00 USD vs 44.31 USD (+15%, 1 analysts); de-biased α -1.7% vs CAPM hurdle 12.1%. Uptrend +48% vs 200-day avg; 12-1 mom +243%; RSI 64. Quality z -0.68 (ROE 12%). ⚠️ price implies 67% stage-1 growth (reverse DCF).

??? note "GFS (GFS) — ⚪ Hold, score +0.01"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.99 USD (+55%, 22 analysts); de-biased α +6.4% vs CAPM hurdle 12.5%. Downtrend -9% vs 200-day avg; 12-1 mom +41%; RSI 55. Quality z -0.21 (ROE 8%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 289.11 USD vs 261.89 USD (+10%, 43 analysts); de-biased α -5.2% vs CAPM hurdle 14.2%. Uptrend +60% vs 200-day avg; 12-1 mom +189%; RSI 63. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? note "AMD (AMD) — ⚪ Hold, score -0.14"
    Hold zone: not owned, no entry. Analyst target 618.51 USD vs 630.35 USD (-2%, 50 analysts); de-biased α -8.5% vs CAPM hurdle 15.0%. Uptrend +72% vs 200-day avg; 12-1 mom +196%; RSI 73. Quality z -0.15 (ROE 7%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 1,125.89 EUR vs 848.00 EUR (+33%, 19 analysts); de-biased α +0.7% vs CAPM hurdle 13.2%. Uptrend +8% vs 200-day avg; 12-1 mom +60%; RSI 54. Quality z -0.10 (ROE 19%).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.30"
    Avoid: not owned. Analyst target 373.77 USD vs 315.29 USD (+19%, 31 analysts); de-biased α -2.8% vs CAPM hurdle 12.7%. Uptrend +16% vs 200-day avg; 12-1 mom +150%; RSI 56. Quality z +0.03 (ROE 65%).

??? failure "TER (TER) — 🔴 Sell, score -0.61"
    Avoid: not owned. Analyst target 446.47 USD vs 398.32 USD (+12%, 15 analysts); de-biased α -4.4% vs CAPM hurdle 12.5%. Uptrend +21% vs 200-day avg; 12-1 mom +180%; RSI 58. Quality z -0.31 (ROE 20%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.62"
    Avoid: not owned. Analyst target 324.71 USD vs 278.01 USD (+17%, 31 analysts); de-biased α -2.3% vs CAPM hurdle 10.8%. Uptrend +13% vs 200-day avg; 12-1 mom +50%; RSI 60. Quality z +0.24 (ROE 30%).

??? failure "SMIC (0981.HK) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 94.39 HKD vs 63.35 HKD (+49%, 22 analysts); de-biased α +6.1% vs CAPM hurdle 7.4%. Downtrend -9% vs 200-day avg; 12-1 mom +13%; RSI 43. Quality z -0.98 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴 Sell, score -0.66"
    Avoid: not owned. Analyst target 405.47 USD vs 326.16 USD (+24%, 26 analysts); de-biased α -0.7% vs CAPM hurdle 10.1%. Uptrend +0% vs 200-day avg; 12-1 mom -1%; RSI 61. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.70"
    Avoid: not owned. Analyst target 7,775 JPY vs 5,887 JPY (+32%, 17 analysts); de-biased α +1.5% vs CAPM hurdle 10.8%. Downtrend -5% vs 200-day avg; 12-1 mom +39%; RSI 47. Quality z -0.19 (ROE 10%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.74"
    Avoid: not owned. Analyst target 76.40 USD vs 53.63 USD (+42%, 10 analysts); de-biased α +2.9% vs CAPM hurdle 14.1%. Downtrend -6% vs 200-day avg; 12-1 mom +78%; RSI 55. Quality z -1.00 (ROE 9%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.79"
    Avoid: not owned. Analyst target 173.36 USD vs 151.90 USD (+14%, 11 analysts); de-biased α -3.4% vs CAPM hurdle 10.9%. Uptrend +16% vs 200-day avg; 12-1 mom +59%; RSI 60. Quality z -0.02 (ROE 6%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 194.13 USD vs 201.95 USD (-4%, 30 analysts); de-biased α -7.9% vs CAPM hurdle 12.1%. Uptrend +20% vs 200-day avg; 12-1 mom -1%; RSI 68. Quality z +0.70 (ROE 23%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -1.11"
    Avoid: not owned. Analyst target 116.37 USD vs 122.96 USD (-5%, 43 analysts); de-biased α -9.2% vs CAPM hurdle 14.1%. Uptrend +54% vs 200-day avg; 12-1 mom +171%; RSI 67. Quality z -0.62 (ROE -0%). ⚠️ price implies 87% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.16"
    Avoid: not owned. Analyst target 553.77 USD vs 425.76 USD (+30%, 25 analysts); de-biased α +0.6% vs CAPM hurdle 10.4%. Downtrend -4% vs 200-day avg; 12-1 mom -12%; RSI 60. Quality z +0.14 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.33"
    Avoid: not owned. Analyst target 288.70 USD vs 310.55 USD (-7%, 40 analysts); de-biased α -11.1% vs CAPM hurdle 20.0%. Uptrend +46% vs 200-day avg; 12-1 mom +81%; RSI 61. Quality z +0.04 (ROE 12%). ⚠️ price implies 115% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| IFX.DE | Infineon Technologies | 1,552 | 57.08 EUR | $100,921 | 10.1% | Buy |
| NVDA | NVIDIA | 447 | 225.08 USD | $100,611 | 10.0% | Buy |
| MU | Micron Technology | 92 | 1,081.69 USD | $99,515 | 9.9% | Strong Buy |
| KLAC | KLA Corp | 469 | 187.91 USD | $88,130 | 8.8% | Hold |
| AMAT | Applied Materials | 178 | 485.05 USD | $86,339 | 8.6% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-09-25 14:37 UTC | BUY (new) | KLAC | 469 | 186.53 | $87,480 |
| 2026-09-25 14:37 UTC | BUY (new) | NVDA | 447 | 223.82 | $100,048 |
| 2026-09-25 14:37 UTC | BUY (new) | AMAT | 178 | 479.88 | $85,419 |
| 2026-09-25 14:37 UTC | BUY (new) | MU | 92 | 1,083.05 | $99,641 |
| 2026-09-24 08:59 UTC | BUY (new) | IFX.DE | 1,552 | 56.56 | $99,956 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 4.07%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 17.2%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
