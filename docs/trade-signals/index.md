---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-15 09:56 UTC (Thu Oct 15, 05:56 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Thu 05:56) · Tokyo 🔴 closed (Thu 18:56) · Korea 🔴 closed (Thu 18:56) · Hong Kong 🔴 closed (Thu 17:56) · Xetra 🟢 open (Thu 11:56) · Euronext Amsterdam 🟢 open (Thu 11:56)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$913,901** | $76,719 (8%) | $837,182 (92%) | -8.61% | -8.15% | 🟢 Risk-on (+11.6%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $913,901), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **AMAT**<br><small>Applied Materials</small> | 56 | 446.48 USD | $25,003 | Queued · NYSE/Nasdaq closed | analyst α +0.12 · momentum +0.07 |
| TRIM | **ASML**<br><small>ASML Holding</small> | 9 | 1,649.85 USD | $14,849 | Queued · NYSE/Nasdaq closed | quality +0.18 · analyst α -0.12 |
| TRIM | **NVDA**<br><small>NVIDIA</small> | 66 | 221.50 USD | $14,619 | Queued · NYSE/Nasdaq closed | quality +0.21 · momentum -0.20 |
| ADD | **ASX**<br><small>ASE Technology</small> | 259 | 44.32 USD | $11,479 | Queued · NYSE/Nasdaq closed | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.61 | **MU**<br><small>Micron Technology</small> | 913.91 USD | +66% | +6.3% | +396% | +28% | 36 | +0.12 | 9.2% → 10.0% | – | analyst α +0.41 · momentum +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.05 | **Samsung**<br><small>005930.KS</small> | 206,500 KRW | +131% | +23.3% | +227% | -11% | 27 | -0.26 | 8.2% → 10.0% | – | analyst α +0.85 · momentum +0.30 · ⚠️ oversold, cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.88 | **SK hynix**<br><small>000660.KS</small> | 1,251,000 KRW | – | +0.0% | +452% | -14% | 25 | +0.62 | 10.0% → 10.0% | – | momentum +0.53 · quality +0.33 · ⚠️ oversold, cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.91 | **Infineon**<br><small>IFX.DE</small> | 51.23 EUR | +69% | +7.1% | +67% | -9% | 35 | -0.04 | 10.0% → 10.0% | – | analyst α +0.48 · trend -0.12 |
| 🟢 Buy | +0.58 | **NVDA**<br><small>NVIDIA</small> | 221.50 USD | +48% | +1.7% | +19% | +9% | 44 | +0.47 | 9.0% → 7.4% | TRIM 66 | quality +0.21 · momentum -0.20 |
| 🟢 Buy | +0.56 | **KLAC**<br><small>KLA Corp</small> | 178.80 USD | +31% | -1.8% | +64% | -1% | 39 | +0.51 | 7.3% → 6.6% | – | quality +0.24 · trend -0.06 |
| 🟢 Buy | +0.55 | **Advantest**<br><small>6857.T</small> | 34,350 JPY | +24% | -4.0% | +132% | +22% | 44 | +0.33 | 2.4% → 4.7% | – | analyst α -0.23 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.53 | **TSM**<br><small>TSMC</small> | 430.08 USD | +28% | -2.2% | +43% | +9% | 41 | +0.58 | 8.8% → 8.1% | – | quality +0.28 · momentum -0.10 |
| 🟢 Buy | +0.47 | **ASX**<br><small>ASE Technology</small> | 44.32 USD | +15% | -2.9% | +239% | +39% | 52 | -0.68 | 4.4% → 5.6% | ADD 259 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.45 | **AMAT**<br><small>Applied Materials</small> | 446.48 USD | +43% | +1.2% | +91% | +2% | 36 | +0.03 | 7.6% → 4.8% | TRIM 56 | analyst α +0.12 · momentum +0.07 |
| 🟢 Buy | +0.36 | **Tokyo Electron**<br><small>8035.T</small> | 10,340 JPY | +48% | +2.2% | +102% | +5% | 40 | -0.28 | 4.3% → 4.0% | – | analyst α +0.19 · quality -0.18 |
| 🟢 Buy | +0.25 | **ASML**<br><small>ASML Holding</small> | 1,649.85 USD | +27% | -3.0% | +64% | +5% | 38 | +0.42 | 5.4% → 3.6% | TRIM 9 | quality +0.18 · analyst α -0.12 |
| ⚪ Hold | +0.11 | **AVGO**<br><small>Broadcom</small> | 346.28 USD | +53% | +3.9% | -1% | -6% | 42 | +0.26 | 5.1% → 5.1% | – | analyst α +0.31 · momentum -0.30 |
| ⚪ Hold | +0.10 | **LRCX**<br><small>Lam Research</small> | 286.72 USD | +31% | -2.2% | +95% | +2% | 37 | +0.02 | 0.0% → 0.0% | – | momentum +0.10 · trend -0.03 |
| ⚪ Hold | +0.08 | **MRVL**<br><small>Marvell Technology</small> | 245.24 USD | +20% | -5.3% | +167% | +40% | 44 | -0.12 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | -0.12 | **ASMI**<br><small>ASM.AS</small> | 756.60 EUR | +49% | +2.3% | +42% | -6% | 33 | -0.10 | 0.0% → 0.0% | – | analyst α +0.23 · momentum -0.12 |
| ⚪ Hold | -0.13 | **GFS**<br><small>GlobalFoundries</small> | 48.94 USD | +55% | +4.0% | +24% | -10% | 53 | -0.21 | 0.0% → 0.0% | – | analyst α +0.36 · momentum -0.14 |
| 🔴 Sell | -0.32 | **AMKR**<br><small>Amkor Technology</small> | 44.79 USD | +71% | +7.5% | +56% | -22% | 35 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 |
| 🔴 Sell | -0.36 | **TXN**<br><small>Texas Instruments</small> | 280.79 USD | +16% | -5.1% | +54% | +11% | 52 | +0.24 | 0.0% → 0.0% | – | analyst α -0.31 · trend +0.10 |
| 🔴 Sell | -0.38 | **Disco**<br><small>6146.T</small> | 53,270 JPY | +53% | +3.9% | +16% | -18% | 39 | +0.06 | 0.0% → 0.0% | – | analyst α +0.27 · momentum -0.26 |
| 🔴 Sell | -0.48 | **TER**<br><small>Teradyne</small> | 359.29 USD | +24% | -3.8% | +150% | +4% | 40 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.63 | **INTC**<br><small>Intel</small> | 98.11 USD | +19% | -5.6% | +184% | +16% | 38 | -0.62 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.75 | **Shin-Etsu**<br><small>4063.T</small> | 5,992 JPY | +30% | -1.7% | +20% | -4% | 49 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · quality -0.11 |
| 🔴🔴 Strong Sell | -0.88 | **QCOM**<br><small>Qualcomm</small> | 172.72 USD | +12% | -6.2% | +17% | +3% | 42 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.00 | **CDNS**<br><small>Cadence Design Systems</small> | 329.53 USD | +23% | -3.5% | -14% | +1% | 50 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -1.12 | **ENTG**<br><small>Entegris</small> | 153.07 USD | +13% | -6.2% | +44% | +13% | 50 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.12 |
| 🔴🔴 Strong Sell | -1.12 | **AMD**<br><small>Advanced Micro Devices</small> | 570.74 USD | +9% | -8.4% | +135% | +45% | 46 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.28 | **SMIC**<br><small>0981.HK</small> | 52.15 HKD | +84% | +12.4% | -33% | -24% | 24 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.34 | **SNPS**<br><small>Synopsys</small> | 480.00 USD | +19% | -4.7% | -15% | +8% | 60 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.27 |
| 🔴🔴 Strong Sell | -1.57 | **ARM**<br><small>Arm Holdings</small> | 238.09 USD | +21% | -6.4% | +45% | +7% | 36 | +0.04 | 0.0% → 0.0% | – | analyst α -0.66 · momentum -0.05 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.61"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 913.91 USD (+66%, 46 analysts); de-biased α +6.3% vs CAPM hurdle 14.0%. Uptrend +28% vs 200-day avg; 12-1 mom +396%; RSI 36. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.05"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 206,500 KRW (+131%, 36 analysts); de-biased α +23.3% vs CAPM hurdle 11.3%. Downtrend -11% vs 200-day avg; 12-1 mom +227%; RSI 27. Quality z -0.26 (ROE 11%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.88"
    Within rebalance band of target 10.0%: no trade. No reliable analyst target: α set to 0. Downtrend -14% vs 200-day avg; 12-1 mom +452%; RSI 25. Quality z +0.62 (ROE 44%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Infineon (IFX.DE) — 🟢🟢 Strong Buy, score +0.91"
    Within rebalance band of target 10.0%: no trade. Analyst target 86.74 EUR vs 51.23 EUR (+69%, 23 analysts); de-biased α +7.1% vs CAPM hurdle 14.1%. Downtrend -9% vs 200-day avg; 12-1 mom +67%; RSI 35. Quality z -0.04 (ROE 6%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.58"
    **TRIM 66 sh** → target 7.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 221.50 USD (+48%, 59 analysts); de-biased α +1.7% vs CAPM hurdle 13.9%. Uptrend +9% vs 200-day avg; 12-1 mom +19%; RSI 44. Quality z +0.47 (ROE 101%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.56"
    Within rebalance band of target 6.6%: no trade. Analyst target 233.77 USD vs 178.80 USD (+31%, 26 analysts); de-biased α -1.8% vs CAPM hurdle 11.1%. Downtrend -1% vs 200-day avg; 12-1 mom +64%; RSI 39. Quality z +0.51 (ROE 87%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.55"
    Within rebalance band of target 4.7%: no trade. Analyst target 42,686 JPY vs 34,350 JPY (+24%, 21 analysts); de-biased α -4.0% vs CAPM hurdle 13.4%. Uptrend +22% vs 200-day avg; 12-1 mom +132%; RSI 44. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.53"
    Within rebalance band of target 8.1%: no trade. Analyst target 552.26 USD vs 430.08 USD (+28%, 20 analysts); de-biased α -2.2% vs CAPM hurdle 10.8%. Uptrend +9% vs 200-day avg; 12-1 mom +43%; RSI 41. Quality z +0.58 (ROE 35%).

??? success "ASX (ASX) — 🟢 Buy, score +0.47"
    **ADD 259 sh** → target 5.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 44.32 USD (+15%, 1 analysts); de-biased α -2.9% vs CAPM hurdle 11.9%. Uptrend +39% vs 200-day avg; 12-1 mom +239%; RSI 52. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.45"
    **TRIM 56 sh** → target 4.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 446.48 USD (+43%, 36 analysts); de-biased α +1.2% vs CAPM hurdle 11.6%. Uptrend +2% vs 200-day avg; 12-1 mom +91%; RSI 36. Quality z +0.03 (ROE 36%).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.36"
    Within rebalance band of target 4.0%: no trade. Analyst target 15,275 JPY vs 10,340 JPY (+48%, 23 analysts); de-biased α +2.2% vs CAPM hurdle 12.8%. Uptrend +5% vs 200-day avg; 12-1 mom +102%; RSI 40. Quality z -0.28 (ROE 29%).

??? success "ASML (ASML) — 🟢 Buy, score +0.25"
    **TRIM 9 sh** → target 3.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 2,096.77 USD vs 1,649.85 USD (+27%, 16 analysts); de-biased α -3.0% vs CAPM hurdle 12.3%. Uptrend +5% vs 200-day avg; 12-1 mom +64%; RSI 38. Quality z +0.42 (ROE 50%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.11"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 346.28 USD (+53%, 47 analysts); de-biased α +3.9% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom -1%; RSI 42. Quality z +0.26 (ROE 31%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.10"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 286.72 USD (+31%, 31 analysts); de-biased α -2.2% vs CAPM hurdle 12.6%. Uptrend +2% vs 200-day avg; 12-1 mom +95%; RSI 37. Quality z +0.02 (ROE 65%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.08"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 245.24 USD (+20%, 43 analysts); de-biased α -5.3% vs CAPM hurdle 14.1%. Uptrend +40% vs 200-day avg; 12-1 mom +167%; RSI 44. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 756.60 EUR (+49%, 19 analysts); de-biased α +2.3% vs CAPM hurdle 13.2%. Downtrend -6% vs 200-day avg; 12-1 mom +42%; RSI 33. Quality z -0.10 (ROE 19%).

??? note "GFS (GFS) — ⚪ Hold, score -0.13"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.94 USD (+55%, 22 analysts); de-biased α +4.0% vs CAPM hurdle 12.4%. Downtrend -10% vs 200-day avg; 12-1 mom +24%; RSI 53. Quality z -0.21 (ROE 8%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 76.40 USD vs 44.79 USD (+71%, 10 analysts); de-biased α +7.5% vs CAPM hurdle 14.0%. Downtrend -22% vs 200-day avg; 12-1 mom +56%; RSI 35. Quality z -1.00 (ROE 9%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 324.71 USD vs 280.79 USD (+16%, 31 analysts); de-biased α -5.1% vs CAPM hurdle 10.8%. Uptrend +11% vs 200-day avg; 12-1 mom +54%; RSI 52. Quality z +0.24 (ROE 30%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 81,730 JPY vs 53,270 JPY (+53%, 20 analysts); de-biased α +3.9% vs CAPM hurdle 11.5%. Downtrend -18% vs 200-day avg; 12-1 mom +16%; RSI 39. Quality z +0.06 (ROE 25%).

??? failure "TER (TER) — 🔴 Sell, score -0.48"
    Avoid: not owned. Analyst target 446.47 USD vs 359.29 USD (+24%, 15 analysts); de-biased α -3.8% vs CAPM hurdle 12.3%. Uptrend +4% vs 200-day avg; 12-1 mom +150%; RSI 40. Quality z -0.31 (ROE 20%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.63"
    Avoid: not owned. Analyst target 116.37 USD vs 98.11 USD (+19%, 43 analysts); de-biased α -5.6% vs CAPM hurdle 14.0%. Uptrend +16% vs 200-day avg; 12-1 mom +184%; RSI 38. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.75"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,992 JPY (+30%, 17 analysts); de-biased α -1.7% vs CAPM hurdle 10.8%. Downtrend -4% vs 200-day avg; 12-1 mom +20%; RSI 49. Quality z -0.20 (ROE 10%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.88"
    Avoid: not owned. Analyst target 194.13 USD vs 172.72 USD (+12%, 30 analysts); de-biased α -6.2% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +17%; RSI 42. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.00"
    Avoid: not owned. Analyst target 405.47 USD vs 329.53 USD (+23%, 26 analysts); de-biased α -3.5% vs CAPM hurdle 10.0%. Uptrend +1% vs 200-day avg; 12-1 mom -14%; RSI 50. Quality z +0.31 (ROE 22%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.12"
    Avoid: not owned. Analyst target 173.36 USD vs 153.07 USD (+13%, 11 analysts); de-biased α -6.2% vs CAPM hurdle 11.0%. Uptrend +13% vs 200-day avg; 12-1 mom +44%; RSI 50. Quality z -0.02 (ROE 6%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.12"
    Avoid: not owned. Analyst target 619.51 USD vs 570.74 USD (+9%, 50 analysts); de-biased α -8.4% vs CAPM hurdle 14.9%. Uptrend +45% vs 200-day avg; 12-1 mom +135%; RSI 46. Quality z -0.15 (ROE 7%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.28"
    Avoid: not owned. Analyst target 95.99 HKD vs 52.15 HKD (+84%, 21 analysts); de-biased α +12.4% vs CAPM hurdle 7.3%. Downtrend -24% vs 200-day avg; 12-1 mom -33%; RSI 24. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.34"
    Avoid: not owned. Analyst target 569.78 USD vs 480.00 USD (+19%, 26 analysts); de-biased α -4.7% vs CAPM hurdle 10.3%. Uptrend +8% vs 200-day avg; 12-1 mom -15%; RSI 60. Quality z +0.14 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.57"
    Avoid: not owned. Analyst target 288.70 USD vs 238.09 USD (+21%, 40 analysts); de-biased α -6.4% vs CAPM hurdle 19.6%. Uptrend +7% vs 200-day avg; 12-1 mom +45%; RSI 36. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| IFX.DE | Infineon Technologies | 1,594 | 51.23 EUR | $91,651 | 10.0% | Strong Buy |
| 000660.KS | SK hynix | 98 | 1,251,000 KRW | $91,240 | 10.0% | Strong Buy |
| MU | Micron Technology | 92 | 913.91 USD | $84,080 | 9.2% | Strong Buy |
| NVDA | NVIDIA | 371 | 221.50 USD | $82,176 | 9.0% | Buy |
| TSM | TSMC | 187 | 430.08 USD | $80,425 | 8.8% | Buy |
| 005930.KS | Samsung Electronics | 485 | 206,500 KRW | $74,536 | 8.2% | Strong Buy |
| AMAT | Applied Materials | 156 | 446.48 USD | $69,651 | 7.6% | Buy |
| KLAC | KLA Corp | 372 | 178.80 USD | $66,514 | 7.3% | Buy |
| ASML | ASML Holding | 30 | 1,649.85 USD | $49,495 | 5.4% | Buy |
| AVGO | Broadcom | 134 | 346.28 USD | $46,402 | 5.1% | Hold |
| ASX | ASE Technology | 900 | 44.32 USD | $39,888 | 4.4% | Buy |
| 8035.T | Tokyo Electron | 600 | 10,340 JPY | $39,341 | 4.3% | Buy |
| 6857.T | Advantest | 100 | 34,350 JPY | $21,782 | 2.4% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 27.2%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
