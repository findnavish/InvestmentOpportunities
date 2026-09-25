---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-09-25 09:08 UTC (Fri Sep 25, 05:08 AM ET) · refreshes hourly · weekly model inputs as of 2026-09-24
**Markets:** NYSE/Nasdaq 🔴 closed (Fri 05:08) · Tokyo 🔴 closed (Fri 18:08) · Korea 🔴 closed (Fri 18:08) · Hong Kong 🔴 closed (Fri 17:08) · Xetra 🟢 open (Fri 11:08) · Euronext Amsterdam 🟢 open (Fri 11:08)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,001,345** | $899,994 (90%) | $101,350 (10%) | +0.13% | -0.00% | 🟢 Risk-on (+26.6%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,001,345), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

| Action | Ticker | Company | Quantity (shares) | Price (local) | Value (USD) | Status | Rationale |
|---|---|---|---|---|---|---|---|
| BUY (new) | TSM | TSMC | 222 | 451.05 USD | $100,133 | Queued: NYSE/Nasdaq closed | **BUY (new) 222 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 vs 451.05 USD (+22%, 20 analysts); de-biased α -1.5% vs CAPM hurdle 10.9%. Uptrend +18% vs 200-day avg; 12-1 mom +50%; RSI 63. Quality z +0.58 (ROE 35%). |
| BUY (new) | 005930.KS | Samsung Electronics | 477 | 284,250.00 KRW | $100,098 | Queued: Korea closed | **BUY (new) 477 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 478,627.88 vs 284,250.00 KRW (+68%, 36 analysts); de-biased α +9.8% vs CAPM hurdle 11.4%. Uptrend +27% vs 200-day avg; 12-1 mom +265%; RSI 61. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18). |
| BUY (new) | AMAT | Applied Materials | 211 | 474.09 USD | $100,033 | Queued: NYSE/Nasdaq closed | **BUY (new) 211 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 640.89 vs 474.09 USD (+35%, 35 analysts); de-biased α +1.4% vs CAPM hurdle 11.7%. Uptrend +13% vs 200-day avg; 12-1 mom +139%; RSI 52. Quality z +0.03 (ROE 36%). |
| BUY (new) | NVDA | NVIDIA | 445 | 224.54 USD | $99,920 | Queued: NYSE/Nasdaq closed | **BUY (new) 445 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 vs 224.54 USD (+46%, 59 analysts); de-biased α +3.4% vs CAPM hurdle 14.0%. Uptrend +13% vs 200-day avg; 12-1 mom +19%; RSI 55. Quality z +0.48 (ROE 101%). |
| BUY (new) | 000660.KS | SK hynix | 73 | 1,853,000.00 KRW | $99,863 | Queued: Korea closed | **BUY (new) 73 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 3,184,025.50 vs 1,853,000.00 KRW (+72%, 37 analysts); de-biased α +9.8% vs CAPM hurdle 14.4%. Uptrend +33% vs 200-day avg; 12-1 mom +457%; RSI 57. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size. |
| BUY (new) | MU | Micron Technology | 92 | 1,078.62 USD | $99,233 | Queued: NYSE/Nasdaq closed | **BUY (new) 92 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 1,515.54 vs 1,078.62 USD (+41%, 46 analysts); de-biased α +2.1% vs CAPM hurdle 14.1%. Uptrend +63% vs 200-day avg; 12-1 mom +481%; RSI 63. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18). |
| BUY (new) | 6857.T | Advantest | 400 | 33,890.00 JPY | $85,803 | Queued: Tokyo closed | **BUY (new) 400 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 42,138.09 vs 33,890.00 JPY (+24%, 21 analysts); de-biased α -1.8% vs CAPM hurdle 13.3%. Uptrend +26% vs 200-day avg; 12-1 mom +172%; RSI 55. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF). |
| BUY (new) | 6146.T | Disco Corp | 200 | 54,400.00 JPY | $68,866 | Queued: Tokyo closed | **BUY (new) 200 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 83,130.00 vs 54,400.00 JPY (+53%, 20 analysts); de-biased α +6.0% vs CAPM hurdle 11.6%. Downtrend -16% vs 200-day avg; 12-1 mom +64%; RSI 45. Quality z +0.07 (ROE 25%). |

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

| Rating | Score | Ticker | Company | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | σ(e) | Shares held | Weight now | Target weight | Order | Rationale |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 🟢🟢 Strong Buy | +3.41 | **000660.KS** | SK hynix | 1,853,000.00 KRW | +72% | +9.8% | +457% | +33% | 57 | +0.63 | 60% | 0 | 0.0% | 10.0% | BUY (new) 73 | **BUY (new) 73 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 3,184,025.50 vs 1,853,000.00 KRW (+72%, 37 analysts); de-biased α +9.8% vs CAPM hurdle 14.4%. Uptrend +33% vs 200-day avg; 12-1 mom +457%; RSI 57. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size. |
| 🟢🟢 Strong Buy | +2.02 | **MU** | Micron Technology | 1,078.62 USD | +41% | +2.1% | +481% | +63% | 63 | +0.06 | 58% | 0 | 0.0% | 10.0% | BUY (new) 92 | **BUY (new) 92 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 1,515.54 vs 1,078.62 USD (+41%, 46 analysts); de-biased α +2.1% vs CAPM hurdle 14.1%. Uptrend +63% vs 200-day avg; 12-1 mom +481%; RSI 63. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18). |
| 🟢🟢 Strong Buy | +1.89 | **005930.KS** | Samsung Electronics | 284,250.00 KRW | +68% | +9.8% | +265% | +27% | 61 | -0.25 | 41% | 0 | 0.0% | 10.0% | BUY (new) 477 | **BUY (new) 477 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 478,627.88 vs 284,250.00 KRW (+68%, 36 analysts); de-biased α +9.8% vs CAPM hurdle 11.4%. Uptrend +27% vs 200-day avg; 12-1 mom +265%; RSI 61. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18). |
| 🟢 Buy | +0.46 | **NVDA** | NVIDIA | 224.54 USD | +46% | +3.4% | +19% | +13% | 55 | +0.48 | 36% | 0 | 0.0% | 10.0% | BUY (new) 445 | **BUY (new) 445 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 vs 224.54 USD (+46%, 59 analysts); de-biased α +3.4% vs CAPM hurdle 14.0%. Uptrend +13% vs 200-day avg; 12-1 mom +19%; RSI 55. Quality z +0.48 (ROE 101%). |
| 🟢 Buy | +0.43 | **IFX.DE** | Infineon Technologies | 57.31 EUR | +51% | +4.8% | +76% | +4% | 49 | -0.04 | 37% | 1,552 | 10.1% | 10.0% | – | Within rebalance band of target 10.0%: no trade. Analyst target 86.59 vs 57.31 EUR (+51%, 22 analysts); de-biased α +4.8% vs CAPM hurdle 14.1%. Uptrend +4% vs 200-day avg; 12-1 mom +76%; RSI 49. Quality z -0.04 (ROE 6%). |
| 🟢 Buy | +0.39 | **6857.T** | Advantest | 33,890.00 JPY | +24% | -1.8% | +172% | +26% | 55 | +0.33 | 54% | 0 | 0.0% | 10.0% | BUY (new) 400 | **BUY (new) 400 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 42,138.09 vs 33,890.00 JPY (+24%, 21 analysts); de-biased α -1.8% vs CAPM hurdle 13.3%. Uptrend +26% vs 200-day avg; 12-1 mom +172%; RSI 55. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF). |
| 🟢 Buy | +0.34 | **AMAT** | Applied Materials | 474.09 USD | +35% | +1.4% | +139% | +13% | 52 | +0.03 | 42% | 0 | 0.0% | 10.0% | BUY (new) 211 | **BUY (new) 211 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 640.89 vs 474.09 USD (+35%, 35 analysts); de-biased α +1.4% vs CAPM hurdle 11.7%. Uptrend +13% vs 200-day avg; 12-1 mom +139%; RSI 52. Quality z +0.03 (ROE 36%). |
| 🟢 Buy | +0.33 | **TSM** | TSMC | 451.05 USD | +22% | -1.5% | +50% | +18% | 63 | +0.58 | 30% | 0 | 0.0% | 10.0% | BUY (new) 222 | **BUY (new) 222 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 vs 451.05 USD (+22%, 20 analysts); de-biased α -1.5% vs CAPM hurdle 10.9%. Uptrend +18% vs 200-day avg; 12-1 mom +50%; RSI 63. Quality z +0.58 (ROE 35%). |
| 🟢 Buy | +0.33 | **6146.T** | Disco Corp | 54,400.00 JPY | +53% | +6.0% | +64% | -16% | 45 | +0.07 | 44% | 0 | 0.0% | 10.0% | BUY (new) 200 | **BUY (new) 200 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 83,130.00 vs 54,400.00 JPY (+53%, 20 analysts); de-biased α +6.0% vs CAPM hurdle 11.6%. Downtrend -16% vs 200-day avg; 12-1 mom +64%; RSI 45. Quality z +0.07 (ROE 25%). |
| ⚪ Hold | +0.25 | **8035.T** | Tokyo Electron | 56,480.00 JPY | +36% | +1.5% | +167% | +15% | 56 | -0.28 | 42% | 0 | 0.0% | 0.0% | – | Hold zone: not owned, no entry. Analyst target 76,808.70 vs 56,480.00 JPY (+36%, 23 analysts); de-biased α +1.5% vs CAPM hurdle 12.7%. Uptrend +15% vs 200-day avg; 12-1 mom +167%; RSI 56. Quality z -0.28 (ROE 29%). ⚠️ price implies 71% stage-1 growth (reverse DCF). |
| ⚪ Hold | +0.21 | **KLAC** | KLA Corp | 186.90 USD | +25% | -1.0% | +72% | +7% | 53 | +0.51 | 39% | 0 | 0.0% | 0.0% | – | Hold zone: not owned, no entry. Analyst target 233.77 vs 186.90 USD (+25%, 26 analysts); de-biased α -1.0% vs CAPM hurdle 11.2%. Uptrend +7% vs 200-day avg; 12-1 mom +72%; RSI 53. Quality z +0.51 (ROE 87%). |
| ⚪ Hold | +0.12 | **AVGO** | Broadcom | 350.27 USD | +52% | +5.8% | +5% | -5% | 42 | +0.27 | 35% | 0 | 0.0% | 0.0% | – | Hold zone: not owned, no entry. Analyst target 531.85 vs 350.27 USD (+52%, 47 analysts); de-biased α +5.8% vs CAPM hurdle 11.2%. Downtrend -5% vs 200-day avg; 12-1 mom +5%; RSI 42. Quality z +0.27 (ROE 31%). |
| ⚪ Hold | +0.12 | **ASX** | ASE Technology | 43.49 USD | +17% | -1.5% | +220% | +47% | 65 | -0.68 | 38% | 0 | 0.0% | 0.0% | – | Hold zone: not owned, no entry. Analyst target 51.00 vs 43.49 USD (+17%, 1 analysts); de-biased α -1.5% vs CAPM hurdle 12.1%. Uptrend +47% vs 200-day avg; 12-1 mom +220%; RSI 65. Quality z -0.68 (ROE 12%). ⚠️ price implies 66% stage-1 growth (reverse DCF). |
| ⚪ Hold | -0.00 | **ASML** | ASML Holding | 1,722.52 USD | +23% | -1.8% | +82% | +13% | 53 | +0.42 | 32% | 0 | 0.0% | 0.0% | – | Hold zone: not owned, no entry. Analyst target 2,119.85 vs 1,722.52 USD (+23%, 16 analysts); de-biased α -1.8% vs CAPM hurdle 12.4%. Uptrend +13% vs 200-day avg; 12-1 mom +82%; RSI 53. Quality z +0.42 (ROE 50%). |
| ⚪ Hold | -0.05 | **GFS** | GlobalFoundries | 47.05 USD | +62% | +7.8% | +39% | -13% | 49 | -0.21 | 47% | 0 | 0.0% | 0.0% | – | Hold zone: not owned, no entry. Analyst target 76.00 vs 47.05 USD (+62%, 22 analysts); de-biased α +7.8% vs CAPM hurdle 12.5%. Downtrend -13% vs 200-day avg; 12-1 mom +39%; RSI 49. Quality z -0.21 (ROE 8%). |
| ⚪ Hold | -0.11 | **MRVL** | Marvell Technology | 258.89 USD | +12% | -5.2% | +207% | +59% | 62 | -0.12 | 55% | 0 | 0.0% | 0.0% | – | Hold zone: not owned, no entry. Analyst target 289.11 vs 258.89 USD (+12%, 43 analysts); de-biased α -5.2% vs CAPM hurdle 14.2%. Uptrend +59% vs 200-day avg; 12-1 mom +207%; RSI 62. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF). |
| ⚪ Hold | -0.21 | **AMD** | Advanced Micro Devices | 629.02 USD | -2% | -8.8% | +199% | +72% | 73 | -0.15 | 56% | 0 | 0.0% | 0.0% | – | Hold zone: not owned, no entry. Analyst target 616.51 vs 629.02 USD (-2%, 50 analysts); de-biased α -8.8% vs CAPM hurdle 15.0%. Uptrend +72% vs 200-day avg; 12-1 mom +199%; RSI 73. Quality z -0.15 (ROE 7%). |
| 🔴 Sell | -0.28 | **ASM.AS** | ASM International | 847.20 EUR | +33% | +0.5% | +63% | +8% | 54 | -0.10 | 39% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 1,125.89 vs 847.20 EUR (+33%, 19 analysts); de-biased α +0.5% vs CAPM hurdle 13.2%. Uptrend +8% vs 200-day avg; 12-1 mom +63%; RSI 54. Quality z -0.10 (ROE 19%). |
| 🔴 Sell | -0.35 | **LRCX** | Lam Research | 307.16 USD | +22% | -2.2% | +140% | +14% | 53 | +0.03 | 39% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 373.77 vs 307.16 USD (+22%, 31 analysts); de-biased α -2.2% vs CAPM hurdle 12.7%. Uptrend +14% vs 200-day avg; 12-1 mom +140%; RSI 53. Quality z +0.03 (ROE 65%). |
| 🔴 Sell | -0.44 | **TXN** | Texas Instruments | 270.59 USD | +20% | -1.8% | +47% | +11% | 54 | +0.24 | 27% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 324.71 vs 270.59 USD (+20%, 31 analysts); de-biased α -1.8% vs CAPM hurdle 10.8%. Uptrend +11% vs 200-day avg; 12-1 mom +47%; RSI 54. Quality z +0.24 (ROE 30%). |
| 🔴 Sell | -0.68 | **TER** | Teradyne | 387.65 USD | +15% | -3.9% | +172% | +18% | 56 | -0.31 | 41% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 446.47 vs 387.65 USD (+15%, 15 analysts); de-biased α -3.9% vs CAPM hurdle 12.4%. Uptrend +18% vs 200-day avg; 12-1 mom +172%; RSI 56. Quality z -0.31 (ROE 20%). |
| 🔴 Sell | -0.70 | **QCOM** | Qualcomm | 194.25 USD | -0% | -7.1% | -4% | +16% | 64 | +0.70 | 36% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 194.13 vs 194.25 USD (-0%, 30 analysts); de-biased α -7.1% vs CAPM hurdle 12.1%. Uptrend +16% vs 200-day avg; 12-1 mom -4%; RSI 64. Quality z +0.70 (ROE 23%). |
| 🔴 Sell | -0.71 | **4063.T** | Shin-Etsu Chemical | 5,887.00 JPY | +32% | +1.2% | +40% | -5% | 47 | -0.19 | 25% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 7,774.71 vs 5,887.00 JPY (+32%, 17 analysts); de-biased α +1.2% vs CAPM hurdle 10.8%. Downtrend -5% vs 200-day avg; 12-1 mom +40%; RSI 47. Quality z -0.19 (ROE 10%). |
| 🔴🔴 Strong Sell | -0.76 | **0981.HK** | SMIC | 63.35 HKD | +49% | +5.8% | +13% | -9% | 43 | -0.98 | 50% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 94.39 vs 63.35 HKD (+49%, 22 analysts); de-biased α +5.8% vs CAPM hurdle 7.4%. Downtrend -9% vs 200-day avg; 12-1 mom +13%; RSI 43. Quality z -0.98 (ROE 3%). |
| 🔴🔴 Strong Sell | -0.79 | **CDNS** | Cadence Design Systems | 322.49 USD | +25% | -0.8% | -9% | -1% | 59 | +0.31 | 24% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 403.38 vs 322.49 USD (+25%, 27 analysts); de-biased α -0.8% vs CAPM hurdle 10.1%. Downtrend -1% vs 200-day avg; 12-1 mom -9%; RSI 59. Quality z +0.31 (ROE 22%). |
| 🔴🔴 Strong Sell | -0.81 | **AMKR** | Amkor Technology | 52.63 USD | +45% | +3.4% | +65% | -7% | 53 | -1.00 | 44% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 76.40 vs 52.63 USD (+45%, 10 analysts); de-biased α +3.4% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +65%; RSI 53. Quality z -1.00 (ROE 9%). |
| 🔴🔴 Strong Sell | -0.92 | **ENTG** | Entegris | 148.54 USD | +17% | -3.0% | +46% | +14% | 57 | -0.02 | 43% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 173.36 vs 148.54 USD (+17%, 11 analysts); de-biased α -3.0% vs CAPM hurdle 10.9%. Uptrend +14% vs 200-day avg; 12-1 mom +46%; RSI 57. Quality z -0.02 (ROE 6%). |
| 🔴🔴 Strong Sell | -0.98 | **INTC** | Intel | 127.36 USD | -9% | -10.3% | +183% | +61% | 73 | -0.62 | 61% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 116.37 vs 127.36 USD (-9%, 43 analysts); de-biased α -10.3% vs CAPM hurdle 14.1%. Uptrend +61% vs 200-day avg; 12-1 mom +183%; RSI 73. Quality z -0.62 (ROE -0%). ⚠️ price implies 88% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size. |
| 🔴🔴 Strong Sell | -1.14 | **SNPS** | Synopsys | 424.87 USD | +28% | -0.1% | -17% | -5% | 59 | +0.14 | 29% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 545.55 vs 424.87 USD (+28%, 26 analysts); de-biased α -0.1% vs CAPM hurdle 10.4%. Downtrend -5% vs 200-day avg; 12-1 mom -17%; RSI 59. Quality z +0.14 (ROE 7%). |
| 🔴🔴 Strong Sell | -1.36 | **ARM** | Arm Holdings | 306.43 USD | -6% | -11.0% | +74% | +45% | 60 | +0.04 | 78% | 0 | 0.0% | 0.0% | – | Avoid: not owned. Analyst target 288.70 vs 306.43 USD (-6%, 40 analysts); de-biased α -11.0% vs CAPM hurdle 20.0%. Uptrend +45% vs 200-day avg; 12-1 mom +74%; RSI 60. Quality z +0.04 (ROE 12%). ⚠️ price implies 114% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size. |

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| IFX.DE | Infineon Technologies | 1,552 | 57.31 EUR | $101,350 | 10.1% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-09-24 08:59 UTC | BUY (new) | IFX.DE | 1,552 | 56.56 | $99,956 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 4.07%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 18.3%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
