---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-09-25 09:24 UTC (Fri Sep 25, 05:24 AM ET) · refreshes hourly · weekly model inputs as of 2026-09-24
**Markets:** NYSE/Nasdaq 🔴 closed (Fri 05:24) · Tokyo 🔴 closed (Fri 18:24) · Korea 🔴 closed (Fri 18:24) · Hong Kong 🔴 closed (Fri 17:24) · Xetra 🟢 open (Fri 11:24) · Euronext Amsterdam 🟢 open (Fri 11:24)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,001,303** | $899,994 (90%) | $101,309 (10%) | +0.13% | -0.00% | 🟢 Risk-on (+26.6%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,001,303), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **Samsung**<br><small>005930.KS</small> | 477 | 284,250 KRW | $100,129 | Queued · Korea closed | analyst α +0.66 · momentum +0.35 · ⚠️ cycle-peak P/E |
| BUY (new) | **AMAT**<br><small>Applied Materials</small> | 211 | 474.09 USD | $100,033 | Queued · NYSE/Nasdaq closed | analyst α +0.12 · momentum +0.07 |
| BUY (new) | **NVDA**<br><small>NVIDIA</small> | 445 | 224.54 USD | $99,920 | Queued · NYSE/Nasdaq closed | analyst α +0.27 · momentum -0.23 |
| BUY (new) | **SK hynix**<br><small>000660.KS</small> | 73 | 1,853,000 KRW | $99,894 | Queued · Korea closed | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| BUY (new) | **TSM**<br><small>TSMC</small> | 221 | 451.05 USD | $99,682 | Queued · NYSE/Nasdaq closed | quality +0.28 · momentum -0.10 |
| BUY (new) | **MU**<br><small>Micron Technology</small> | 92 | 1,078.62 USD | $99,233 | Queued · NYSE/Nasdaq closed | momentum +0.53 · trend +0.25 · ⚠️ cycle-peak P/E |
| BUY (new) | **Advantest**<br><small>6857.T</small> | 400 | 33,890 JPY | $85,865 | Queued · Tokyo closed | analyst α -0.19 · quality +0.16 · ⚠️ rich valuation |
| BUY (new) | **Disco**<br><small>6146.T</small> | 200 | 54,400 JPY | $68,915 | Queued · Tokyo closed | analyst α +0.48 · trend -0.32 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.41 | **SK hynix**<br><small>000660.KS</small> | 1,853,000 KRW | +72% | +9.8% | +457% | +33% | 57 | +0.63 | 0.0% → 10.0% | BUY 73 | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.02 | **MU**<br><small>Micron Technology</small> | 1,078.62 USD | +41% | +2.1% | +481% | +63% | 63 | +0.06 | 0.0% → 10.0% | BUY 92 | momentum +0.53 · trend +0.25 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.89 | **Samsung**<br><small>005930.KS</small> | 284,250 KRW | +68% | +9.8% | +265% | +27% | 61 | -0.25 | 0.0% → 10.0% | BUY 477 | analyst α +0.66 · momentum +0.35 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.46 | **NVDA**<br><small>NVIDIA</small> | 224.54 USD | +46% | +3.4% | +19% | +13% | 55 | +0.48 | 0.0% → 10.0% | BUY 445 | analyst α +0.27 · momentum -0.23 |
| 🟢 Buy | +0.43 | **Infineon**<br><small>IFX.DE</small> | 57.28 EUR | +51% | +4.9% | +76% | +4% | 49 | -0.04 | 10.1% → 10.0% | – | analyst α +0.31 · trend -0.09 |
| 🟢 Buy | +0.39 | **Advantest**<br><small>6857.T</small> | 33,890 JPY | +24% | -1.8% | +172% | +26% | 55 | +0.33 | 0.0% → 10.0% | BUY 400 | analyst α -0.19 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.34 | **AMAT**<br><small>Applied Materials</small> | 474.09 USD | +35% | +1.4% | +139% | +13% | 52 | +0.03 | 0.0% → 10.0% | BUY 211 | analyst α +0.12 · momentum +0.07 |
| 🟢 Buy | +0.33 | **TSM**<br><small>TSMC</small> | 451.05 USD | +22% | -1.5% | +50% | +18% | 63 | +0.58 | 0.0% → 10.0% | BUY 221 | quality +0.28 · momentum -0.10 |
| 🟢 Buy | +0.33 | **Disco**<br><small>6146.T</small> | 54,400 JPY | +53% | +6.0% | +64% | -16% | 45 | +0.07 | 0.0% → 10.0% | BUY 200 | analyst α +0.48 · trend -0.32 |
| ⚪ Hold | +0.25 | **Tokyo Electron**<br><small>8035.T</small> | 56,480 JPY | +36% | +1.5% | +167% | +15% | 56 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.15 · ⚠️ rich valuation |
| ⚪ Hold | +0.21 | **KLAC**<br><small>KLA Corp</small> | 186.90 USD | +25% | -1.0% | +72% | +7% | 53 | +0.51 | 0.0% → 0.0% | – | quality +0.24 · trend -0.07 |
| ⚪ Hold | +0.12 | **AVGO**<br><small>Broadcom</small> | 350.27 USD | +52% | +5.8% | +5% | -5% | 42 | +0.27 | 0.0% → 0.0% | – | analyst α +0.36 · momentum -0.30 |
| ⚪ Hold | +0.12 | **ASX**<br><small>ASE Technology</small> | 43.49 USD | +17% | -1.5% | +220% | +47% | 65 | -0.68 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | -0.00 | **ASML**<br><small>ASML Holding</small> | 1,722.52 USD | +23% | -1.8% | +82% | +13% | 53 | +0.42 | 0.0% → 0.0% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | -0.05 | **GFS**<br><small>GlobalFoundries</small> | 47.05 USD | +62% | +7.8% | +39% | -13% | 49 | -0.21 | 0.0% → 0.0% | – | analyst α +0.55 · trend -0.25 |
| ⚪ Hold | -0.11 | **MRVL**<br><small>Marvell Technology</small> | 258.89 USD | +12% | -5.2% | +207% | +59% | 62 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.26 · ⚠️ rich valuation |
| ⚪ Hold | -0.21 | **AMD**<br><small>Advanced Micro Devices</small> | 629.02 USD | -2% | -8.8% | +199% | +72% | 73 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.28 | **ASMI**<br><small>ASM.AS</small> | 846.80 EUR | +33% | +0.5% | +63% | +8% | 54 | -0.10 | 0.0% → 0.0% | – | momentum -0.07 · quality -0.06 |
| 🔴 Sell | -0.35 | **LRCX**<br><small>Lam Research</small> | 307.16 USD | +22% | -2.2% | +140% | +14% | 53 | +0.03 | 0.0% → 0.0% | – | analyst α -0.27 · momentum +0.10 |
| 🔴 Sell | -0.44 | **TXN**<br><small>Texas Instruments</small> | 270.59 USD | +20% | -1.8% | +47% | +11% | 54 | +0.24 | 0.0% → 0.0% | – | analyst α -0.15 · momentum -0.12 |
| 🔴 Sell | -0.68 | **TER**<br><small>Teradyne</small> | 387.65 USD | +15% | -3.9% | +172% | +18% | 56 | -0.31 | 0.0% → 0.0% | – | analyst α -0.36 · quality -0.21 |
| 🔴 Sell | -0.70 | **QCOM**<br><small>Qualcomm</small> | 194.25 USD | -0% | -7.1% | -4% | +16% | 64 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴 Sell | -0.71 | **Shin-Etsu**<br><small>4063.T</small> | 5,887 JPY | +32% | +1.2% | +40% | -5% | 47 | -0.19 | 0.0% → 0.0% | – | momentum -0.17 · trend -0.16 |
| 🔴🔴 Strong Sell | -0.76 | **SMIC**<br><small>0981.HK</small> | 63.35 HKD | +49% | +5.8% | +13% | -9% | 43 | -0.98 | 0.0% → 0.0% | – | analyst α +0.41 · quality -0.33 |
| 🔴🔴 Strong Sell | -0.79 | **CDNS**<br><small>Cadence Design Systems</small> | 322.49 USD | +25% | -0.8% | -9% | -1% | 59 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -0.81 | **AMKR**<br><small>Amkor Technology</small> | 52.63 USD | +45% | +3.4% | +65% | -7% | 53 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.23 |
| 🔴🔴 Strong Sell | -0.92 | **ENTG**<br><small>Entegris</small> | 148.54 USD | +17% | -3.0% | +46% | +14% | 57 | -0.02 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.14 |
| 🔴🔴 Strong Sell | -0.98 | **INTC**<br><small>Intel</small> | 127.36 USD | -9% | -10.3% | +183% | +61% | 73 | -0.62 | 0.0% → 0.0% | – | analyst α -0.66 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.14 | **SNPS**<br><small>Synopsys</small> | 424.87 USD | +28% | -0.1% | -17% | -5% | 59 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · trend -0.14 |
| 🔴🔴 Strong Sell | -1.36 | **ARM**<br><small>Arm Holdings</small> | 306.43 USD | -6% | -11.0% | +74% | +45% | 60 | +0.04 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.14 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.41"
    **BUY (new) 73 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 3,184,026 KRW vs 1,853,000 KRW (+72%, 37 analysts); de-biased α +9.8% vs CAPM hurdle 14.4%. Uptrend +33% vs 200-day avg; 12-1 mom +457%; RSI 57. Quality z +0.63 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.02"
    **BUY (new) 92 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 1,515.54 USD vs 1,078.62 USD (+41%, 46 analysts); de-biased α +2.1% vs CAPM hurdle 14.1%. Uptrend +63% vs 200-day avg; 12-1 mom +481%; RSI 63. Quality z +0.06 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 6.8 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.89"
    **BUY (new) 477 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 478,628 KRW vs 284,250 KRW (+68%, 36 analysts); de-biased α +9.8% vs CAPM hurdle 11.4%. Uptrend +27% vs 200-day avg; 12-1 mom +265%; RSI 61. Quality z -0.25 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 4.0 (ch.17-18).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.46"
    **BUY (new) 445 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 224.54 USD (+46%, 59 analysts); de-biased α +3.4% vs CAPM hurdle 14.0%. Uptrend +13% vs 200-day avg; 12-1 mom +19%; RSI 55. Quality z +0.48 (ROE 101%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.43"
    Within rebalance band of target 10.0%: no trade. Analyst target 86.59 EUR vs 57.28 EUR (+51%, 22 analysts); de-biased α +4.9% vs CAPM hurdle 14.1%. Uptrend +4% vs 200-day avg; 12-1 mom +76%; RSI 49. Quality z -0.04 (ROE 6%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.39"
    **BUY (new) 400 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 42,138 JPY vs 33,890 JPY (+24%, 21 analysts); de-biased α -1.8% vs CAPM hurdle 13.3%. Uptrend +26% vs 200-day avg; 12-1 mom +172%; RSI 55. Quality z +0.33 (ROE 58%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.34"
    **BUY (new) 211 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 640.89 USD vs 474.09 USD (+35%, 35 analysts); de-biased α +1.4% vs CAPM hurdle 11.7%. Uptrend +13% vs 200-day avg; 12-1 mom +139%; RSI 52. Quality z +0.03 (ROE 36%).

??? success "TSM (TSM) — 🟢 Buy, score +0.33"
    **BUY (new) 221 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 451.05 USD (+22%, 20 analysts); de-biased α -1.5% vs CAPM hurdle 10.9%. Uptrend +18% vs 200-day avg; 12-1 mom +50%; RSI 63. Quality z +0.58 (ROE 35%).

??? success "Disco (6146.T) — 🟢 Buy, score +0.33"
    **BUY (new) 200 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 83,130 JPY vs 54,400 JPY (+53%, 20 analysts); de-biased α +6.0% vs CAPM hurdle 11.6%. Downtrend -16% vs 200-day avg; 12-1 mom +64%; RSI 45. Quality z +0.07 (ROE 25%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.25"
    Hold zone: not owned, no entry. Analyst target 76,809 JPY vs 56,480 JPY (+36%, 23 analysts); de-biased α +1.5% vs CAPM hurdle 12.7%. Uptrend +15% vs 200-day avg; 12-1 mom +167%; RSI 56. Quality z -0.28 (ROE 29%). ⚠️ price implies 71% stage-1 growth (reverse DCF).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.21"
    Hold zone: not owned, no entry. Analyst target 233.77 USD vs 186.90 USD (+25%, 26 analysts); de-biased α -1.0% vs CAPM hurdle 11.2%. Uptrend +7% vs 200-day avg; 12-1 mom +72%; RSI 53. Quality z +0.51 (ROE 87%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.12"
    Hold zone: not owned, no entry. Analyst target 531.85 USD vs 350.27 USD (+52%, 47 analysts); de-biased α +5.8% vs CAPM hurdle 11.2%. Downtrend -5% vs 200-day avg; 12-1 mom +5%; RSI 42. Quality z +0.27 (ROE 31%).

??? note "ASX (ASX) — ⚪ Hold, score +0.12"
    Hold zone: not owned, no entry. Analyst target 51.00 USD vs 43.49 USD (+17%, 1 analysts); de-biased α -1.5% vs CAPM hurdle 12.1%. Uptrend +47% vs 200-day avg; 12-1 mom +220%; RSI 65. Quality z -0.68 (ROE 12%). ⚠️ price implies 66% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score -0.00"
    Hold zone: not owned, no entry. Analyst target 2,119.85 USD vs 1,722.52 USD (+23%, 16 analysts); de-biased α -1.8% vs CAPM hurdle 12.4%. Uptrend +13% vs 200-day avg; 12-1 mom +82%; RSI 53. Quality z +0.42 (ROE 50%).

??? note "GFS (GFS) — ⚪ Hold, score -0.05"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 47.05 USD (+62%, 22 analysts); de-biased α +7.8% vs CAPM hurdle 12.5%. Downtrend -13% vs 200-day avg; 12-1 mom +39%; RSI 49. Quality z -0.21 (ROE 8%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.11"
    Hold zone: not owned, no entry. Analyst target 289.11 USD vs 258.89 USD (+12%, 43 analysts); de-biased α -5.2% vs CAPM hurdle 14.2%. Uptrend +59% vs 200-day avg; 12-1 mom +207%; RSI 62. Quality z -0.12 (ROE 19%). ⚠️ price implies 76% stage-1 growth (reverse DCF).

??? note "AMD (AMD) — ⚪ Hold, score -0.21"
    Hold zone: not owned, no entry. Analyst target 616.51 USD vs 629.02 USD (-2%, 50 analysts); de-biased α -8.8% vs CAPM hurdle 15.0%. Uptrend +72% vs 200-day avg; 12-1 mom +199%; RSI 73. Quality z -0.15 (ROE 7%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.28"
    Avoid: not owned. Analyst target 1,125.89 EUR vs 846.80 EUR (+33%, 19 analysts); de-biased α +0.5% vs CAPM hurdle 13.2%. Uptrend +8% vs 200-day avg; 12-1 mom +63%; RSI 54. Quality z -0.10 (ROE 19%).

??? failure "LRCX (LRCX) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 373.77 USD vs 307.16 USD (+22%, 31 analysts); de-biased α -2.2% vs CAPM hurdle 12.7%. Uptrend +14% vs 200-day avg; 12-1 mom +140%; RSI 53. Quality z +0.03 (ROE 65%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 324.71 USD vs 270.59 USD (+20%, 31 analysts); de-biased α -1.8% vs CAPM hurdle 10.8%. Uptrend +11% vs 200-day avg; 12-1 mom +47%; RSI 54. Quality z +0.24 (ROE 30%).

??? failure "TER (TER) — 🔴 Sell, score -0.68"
    Avoid: not owned. Analyst target 446.47 USD vs 387.65 USD (+15%, 15 analysts); de-biased α -3.9% vs CAPM hurdle 12.4%. Uptrend +18% vs 200-day avg; 12-1 mom +172%; RSI 56. Quality z -0.31 (ROE 20%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.70"
    Avoid: not owned. Analyst target 194.13 USD vs 194.25 USD (-0%, 30 analysts); de-biased α -7.1% vs CAPM hurdle 12.1%. Uptrend +16% vs 200-day avg; 12-1 mom -4%; RSI 64. Quality z +0.70 (ROE 23%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.71"
    Avoid: not owned. Analyst target 7,775 JPY vs 5,887 JPY (+32%, 17 analysts); de-biased α +1.2% vs CAPM hurdle 10.8%. Downtrend -5% vs 200-day avg; 12-1 mom +40%; RSI 47. Quality z -0.19 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.76"
    Avoid: not owned. Analyst target 94.39 HKD vs 63.35 HKD (+49%, 22 analysts); de-biased α +5.8% vs CAPM hurdle 7.4%. Downtrend -9% vs 200-day avg; 12-1 mom +13%; RSI 43. Quality z -0.98 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.79"
    Avoid: not owned. Analyst target 403.38 USD vs 322.49 USD (+25%, 27 analysts); de-biased α -0.8% vs CAPM hurdle 10.1%. Downtrend -1% vs 200-day avg; 12-1 mom -9%; RSI 59. Quality z +0.31 (ROE 22%).

??? failure "AMKR (AMKR) — 🔴🔴 Strong Sell, score -0.81"
    Avoid: not owned. Analyst target 76.40 USD vs 52.63 USD (+45%, 10 analysts); de-biased α +3.4% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +65%; RSI 53. Quality z -1.00 (ROE 9%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 173.36 USD vs 148.54 USD (+17%, 11 analysts); de-biased α -3.0% vs CAPM hurdle 10.9%. Uptrend +14% vs 200-day avg; 12-1 mom +46%; RSI 57. Quality z -0.02 (ROE 6%).

??? failure "INTC (INTC) — 🔴🔴 Strong Sell, score -0.98"
    Avoid: not owned. Analyst target 116.37 USD vs 127.36 USD (-9%, 43 analysts); de-biased α -10.3% vs CAPM hurdle 14.1%. Uptrend +61% vs 200-day avg; 12-1 mom +183%; RSI 73. Quality z -0.62 (ROE -0%). ⚠️ price implies 88% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 61% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.14"
    Avoid: not owned. Analyst target 545.55 USD vs 424.87 USD (+28%, 26 analysts); de-biased α -0.1% vs CAPM hurdle 10.4%. Downtrend -5% vs 200-day avg; 12-1 mom -17%; RSI 59. Quality z +0.14 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.36"
    Avoid: not owned. Analyst target 288.70 USD vs 306.43 USD (-6%, 40 analysts); de-biased α -11.0% vs CAPM hurdle 20.0%. Uptrend +45% vs 200-day avg; 12-1 mom +74%; RSI 60. Quality z +0.04 (ROE 12%). ⚠️ price implies 114% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| IFX.DE | Infineon Technologies | 1,552 | 57.28 EUR | $101,309 | 10.1% | Buy |

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
