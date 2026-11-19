---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-19 03:29 UTC (Wed Nov 18, 10:29 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Wed 22:29) · Tokyo 🟢 open (Thu 12:29) · Korea 🟢 open (Thu 12:29) · Hong Kong 🟢 open (Thu 11:29) · Xetra 🔴 closed (Thu 04:29) · Euronext Amsterdam 🔴 closed (Thu 04:29)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$811,893** | $350,409 (43%) | $461,484 (57%) | -18.81% | -74.92% | 🔴 Risk-off (-11.7%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $811,893), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **NVDA**<br><small>NVIDIA</small> | 270 | 150.87 USD | $40,735 | Queued · NYSE/Nasdaq closed | analyst α +0.85 · quality +0.21 · ⚠️ oversold |
| TRIM | **TSM**<br><small>TSMC</small> | 79 | 362.62 USD | $28,647 | Queued · NYSE/Nasdaq closed | quality +0.28 · analyst α -0.15 |
| ADD | **MRVL**<br><small>Marvell Technology</small> | 145 | 145.55 USD | $21,105 | Queued · NYSE/Nasdaq closed | analyst α +0.41 · momentum +0.41 · ⚠️ rich valuation |
| TRIM | **ASX**<br><small>ASE Technology</small> | 341 | 32.54 USD | $11,096 | Queued · NYSE/Nasdaq closed | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| ADD | **LRCX**<br><small>Lam Research</small> | 24 | 211.71 USD | $5,081 | Queued · NYSE/Nasdaq closed | analyst α +0.15 · trend -0.10 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.12 | **MU**<br><small>Micron Technology</small> | 705.00 USD | +116% | +11.8% | +271% | -8% | 37 | +0.12 | 10.1% → 10.0% | – | analyst α +0.55 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.89 | **NVDA**<br><small>NVIDIA</small> | 150.87 USD | +117% | +12.3% | +16% | -26% | 21 | +0.47 | 5.0% → 10.0% | ADD 270 | analyst α +0.85 · quality +0.21 · ⚠️ oversold |
| 🟢🟢 Strong Buy | +1.68 | **MRVL**<br><small>Marvell Technology</small> | 145.55 USD | +102% | +8.4% | +189% | -23% | 33 | -0.12 | 4.4% → 7.1% | ADD 145 | analyst α +0.41 · momentum +0.41 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.06 | **SK hynix**<br><small>000660.KS</small> | 1,124,000 KRW | – | +0.0% | +124% | -26% | 37 | +0.62 | 4.3% → 4.1% | – | quality +0.33 · momentum +0.23 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢 Buy | +0.58 | **AMAT**<br><small>Applied Materials</small> | 352.53 USD | +81% | +3.9% | +78% | -21% | 40 | +0.03 | 3.6% → 3.2% | – | analyst α +0.19 · momentum +0.07 |
| 🟢 Buy | +0.55 | **INTC**<br><small>Intel</small> | 54.68 USD | +113% | +11.1% | +164% | -38% | 29 | -0.62 | 1.5% → 2.0% | – | analyst α +0.48 · trend -0.32 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.41 | **Advantest**<br><small>6857.T</small> | 26,860 JPY | +59% | -2.1% | +66% | -9% | 38 | +0.33 | 2.1% → 1.8% | – | quality +0.16 · analyst α -0.12 · ⚠️ rich valuation |
| 🟢 Buy | +0.36 | **LRCX**<br><small>Lam Research</small> | 211.71 USD | +77% | +2.7% | +79% | -25% | 38 | +0.02 | 1.5% → 2.2% | ADD 24 | analyst α +0.15 · trend -0.10 |
| 🟢 Buy | +0.31 | **ASX**<br><small>ASE Technology</small> | 32.54 USD | +57% | -1.1% | +188% | -5% | 39 | -0.68 | 3.2% → 1.9% | TRIM 341 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.27 | **TSM**<br><small>TSMC</small> | 362.62 USD | +52% | -3.0% | +52% | -10% | 37 | +0.58 | 5.7% → 2.1% | TRIM 79 | quality +0.28 · analyst α -0.15 |
| 🟢 Buy | +0.27 | **Infineon**<br><small>IFX.DE</small> | 49.22 EUR | +76% | +2.1% | +60% | -15% | 44 | -0.04 | 1.5% → 1.7% | – | analyst α +0.12 · quality -0.04 |
| ⚪ Hold | +0.21 | **Samsung**<br><small>005930.KS</small> | 190,800 KRW | – | +0.0% | +134% | -20% | 37 | -0.26 | 8.1% → 8.1% | – | momentum +0.26 · quality -0.16 · ⚠️ cycle-peak P/E |
| ⚪ Hold | +0.15 | **KLAC**<br><small>KLA Corp</small> | 145.19 USD | +61% | -1.0% | +43% | -20% | 42 | +0.51 | 4.8% → 4.8% | – | quality +0.24 · momentum -0.10 |
| ⚪ Hold | +0.07 | **ASML**<br><small>ASML Holding</small> | 1,395.27 USD | +50% | -4.0% | +61% | -13% | 36 | +0.42 | 0.0% → 0.0% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | +0.06 | **TER**<br><small>Teradyne</small> | 235.30 USD | +90% | +5.8% | +101% | -33% | 35 | -0.31 | 1.0% → 1.0% | – | analyst α +0.27 · trend -0.21 |
| ⚪ Hold | -0.12 | **ASMI**<br><small>ASM.AS</small> | 669.20 EUR | +69% | +0.4% | +56% | -18% | 41 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · analyst α +0.05 |
| ⚪ Hold | -0.24 | **GFS**<br><small>GlobalFoundries</small> | 39.81 USD | +91% | +6.1% | +43% | -27% | 41 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.16 |
| 🔴 Sell | -0.36 | **Tokyo Electron**<br><small>8035.T</small> | 8,796 JPY | +74% | +1.9% | +54% | -15% | 41 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.08 |
| 🔴 Sell | -0.40 | **AMKR**<br><small>Amkor Technology</small> | 35.30 USD | +116% | +12.2% | +36% | -37% | 42 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴 Sell | -0.42 | **Disco**<br><small>6146.T</small> | 44,750 JPY | +83% | +4.4% | +12% | -31% | 41 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.23 |
| 🔴 Sell | -0.50 | **TXN**<br><small>Texas Instruments</small> | 292.51 USD | +11% | -13.0% | +82% | +11% | 49 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.25 |
| 🔴 Sell | -0.58 | **ENTG**<br><small>Entegris</small> | 143.90 USD | +20% | -11.1% | +92% | +3% | 49 | -0.02 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.21 |
| 🔴 Sell | -0.59 | **QCOM**<br><small>Qualcomm</small> | 159.83 USD | +21% | -10.7% | +8% | -6% | 40 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.83 | **ARM**<br><small>Arm Holdings</small> | 182.69 USD | +58% | -4.0% | +58% | -22% | 40 | +0.04 | 0.0% → 0.0% | – | analyst α -0.27 · trend -0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.84 | **AVGO**<br><small>Broadcom</small> | 354.07 USD | +50% | -3.7% | -2% | -3% | 55 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -0.97 | **SNPS**<br><small>Synopsys</small> | 434.01 USD | +31% | -8.3% | +15% | -2% | 41 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.23 |
| 🔴🔴 Strong Sell | -1.09 | **AMD**<br><small>Advanced Micro Devices</small> | 530.81 USD | +17% | -13.1% | +122% | +24% | 50 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.19 | **CDNS**<br><small>Cadence Design Systems</small> | 305.82 USD | +33% | -7.9% | +3% | -7% | 40 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.41 | **SMIC**<br><small>0981.HK</small> | 51.45 HKD | +87% | +6.3% | -31% | -22% | 54 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.36 |
| 🔴🔴 Strong Sell | -1.43 | **Shin-Etsu**<br><small>4063.T</small> | 5,488 JPY | +41% | -5.5% | +30% | -13% | 39 | -0.20 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.17 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.12"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 705.00 USD (+116%, 46 analysts); de-biased α +11.8% vs CAPM hurdle 14.0%. Downtrend -8% vs 200-day avg; 12-1 mom +271%; RSI 37. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +1.89"
    **ADD 270 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 150.87 USD (+117%, 59 analysts); de-biased α +12.3% vs CAPM hurdle 13.9%. Downtrend -26% vs 200-day avg; 12-1 mom +16%; RSI 21. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.68"
    **ADD 145 sh** → target 7.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 145.55 USD (+102%, 43 analysts); de-biased α +8.4% vs CAPM hurdle 14.1%. Downtrend -23% vs 200-day avg; 12-1 mom +189%; RSI 33. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.06"
    Within rebalance band of target 4.1%: no trade. No reliable analyst target: α set to 0. Downtrend -26% vs 200-day avg; 12-1 mom +124%; RSI 37. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.58"
    Within rebalance band of target 3.2%: no trade. Analyst target 638.94 USD vs 352.53 USD (+81%, 36 analysts); de-biased α +3.9% vs CAPM hurdle 11.6%. Downtrend -21% vs 200-day avg; 12-1 mom +78%; RSI 40. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.55"
    Within rebalance band of target 2.0%: no trade. Analyst target 116.37 USD vs 54.68 USD (+113%, 43 analysts); de-biased α +11.1% vs CAPM hurdle 14.0%. Downtrend -38% vs 200-day avg; 12-1 mom +164%; RSI 29. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "Advantest (6857.T) — 🟢 Buy, score +0.41"
    Within rebalance band of target 1.8%: no trade. Analyst target 42,686 JPY vs 26,860 JPY (+59%, 21 analysts); de-biased α -2.1% vs CAPM hurdle 13.4%. Downtrend -9% vs 200-day avg; 12-1 mom +66%; RSI 38. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "LRCX (LRCX) — 🟢 Buy, score +0.36"
    **ADD 24 sh** → target 2.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 375.06 USD vs 211.71 USD (+77%, 31 analysts); de-biased α +2.7% vs CAPM hurdle 12.6%. Downtrend -25% vs 200-day avg; 12-1 mom +79%; RSI 38. Quality z +0.02 (ROE 65%).

??? success "ASX (ASX) — 🟢 Buy, score +0.31"
    **TRIM 341 sh** → target 1.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 32.54 USD (+57%, 1 analysts); de-biased α -1.1% vs CAPM hurdle 11.9%. Downtrend -5% vs 200-day avg; 12-1 mom +188%; RSI 39. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.27"
    **TRIM 79 sh** → target 2.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 362.62 USD (+52%, 20 analysts); de-biased α -3.0% vs CAPM hurdle 10.8%. Downtrend -10% vs 200-day avg; 12-1 mom +52%; RSI 37. Quality z +0.58 (ROE 35%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.27"
    Within rebalance band of target 1.7%: no trade. Analyst target 86.74 EUR vs 49.22 EUR (+76%, 23 analysts); de-biased α +2.1% vs CAPM hurdle 14.1%. Downtrend -15% vs 200-day avg; 12-1 mom +60%; RSI 44. Quality z -0.04 (ROE 6%).

??? note "Samsung (005930.KS) — ⚪ Hold, score +0.21"
    Hold zone: keep any existing position, no new money. No reliable analyst target: α set to 0. Downtrend -20% vs 200-day avg; 12-1 mom +134%; RSI 37. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 145.19 USD (+61%, 26 analysts); de-biased α -1.0% vs CAPM hurdle 11.1%. Downtrend -20% vs 200-day avg; 12-1 mom +43%; RSI 42. Quality z +0.51 (ROE 87%).

??? note "ASML (ASML) — ⚪ Hold, score +0.07"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,395.27 USD (+50%, 16 analysts); de-biased α -4.0% vs CAPM hurdle 12.3%. Downtrend -13% vs 200-day avg; 12-1 mom +61%; RSI 36. Quality z +0.42 (ROE 50%).

??? note "TER (TER) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 235.30 USD (+90%, 15 analysts); de-biased α +5.8% vs CAPM hurdle 12.3%. Downtrend -33% vs 200-day avg; 12-1 mom +101%; RSI 35. Quality z -0.31 (ROE 20%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 669.20 EUR (+69%, 19 analysts); de-biased α +0.4% vs CAPM hurdle 13.2%. Downtrend -18% vs 200-day avg; 12-1 mom +56%; RSI 41. Quality z -0.10 (ROE 19%).

??? note "GFS (GFS) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 39.81 USD (+91%, 22 analysts); de-biased α +6.1% vs CAPM hurdle 12.4%. Downtrend -27% vs 200-day avg; 12-1 mom +43%; RSI 41. Quality z -0.21 (ROE 8%).

??? failure "Tokyo Electron (8035.T) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 15,275 JPY vs 8,796 JPY (+74%, 23 analysts); de-biased α +1.9% vs CAPM hurdle 12.8%. Downtrend -15% vs 200-day avg; 12-1 mom +54%; RSI 41. Quality z -0.28 (ROE 29%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.40"
    Avoid: not owned. Analyst target 76.40 USD vs 35.30 USD (+116%, 10 analysts); de-biased α +12.2% vs CAPM hurdle 14.0%. Downtrend -37% vs 200-day avg; 12-1 mom +36%; RSI 42. Quality z -1.00 (ROE 9%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.42"
    Avoid: not owned. Analyst target 81,730 JPY vs 44,750 JPY (+83%, 20 analysts); de-biased α +4.4% vs CAPM hurdle 11.5%. Downtrend -31% vs 200-day avg; 12-1 mom +12%; RSI 41. Quality z +0.06 (ROE 25%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 324.71 USD vs 292.51 USD (+11%, 31 analysts); de-biased α -13.0% vs CAPM hurdle 10.8%. Uptrend +11% vs 200-day avg; 12-1 mom +82%; RSI 49. Quality z +0.24 (ROE 30%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 173.36 USD vs 143.90 USD (+20%, 11 analysts); de-biased α -11.1% vs CAPM hurdle 11.0%. Uptrend +3% vs 200-day avg; 12-1 mom +92%; RSI 49. Quality z -0.02 (ROE 6%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 194.13 USD vs 159.83 USD (+21%, 30 analysts); de-biased α -10.7% vs CAPM hurdle 11.9%. Downtrend -6% vs 200-day avg; 12-1 mom +8%; RSI 40. Quality z +0.70 (ROE 23%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.83"
    Avoid: not owned. Analyst target 288.70 USD vs 182.69 USD (+58%, 40 analysts); de-biased α -4.0% vs CAPM hurdle 19.6%. Downtrend -22% vs 200-day avg; 12-1 mom +58%; RSI 40. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.84"
    Avoid: not owned. Analyst target 531.31 USD vs 354.07 USD (+50%, 47 analysts); de-biased α -3.7% vs CAPM hurdle 11.2%. Downtrend -3% vs 200-day avg; 12-1 mom -2%; RSI 55. Quality z +0.26 (ROE 31%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.97"
    Avoid: not owned. Analyst target 569.78 USD vs 434.01 USD (+31%, 26 analysts); de-biased α -8.3% vs CAPM hurdle 10.3%. Downtrend -2% vs 200-day avg; 12-1 mom +15%; RSI 41. Quality z +0.14 (ROE 7%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.09"
    Avoid: not owned. Analyst target 619.51 USD vs 530.81 USD (+17%, 50 analysts); de-biased α -13.1% vs CAPM hurdle 14.9%. Uptrend +24% vs 200-day avg; 12-1 mom +122%; RSI 50. Quality z -0.15 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.19"
    Avoid: not owned. Analyst target 405.47 USD vs 305.82 USD (+33%, 26 analysts); de-biased α -7.9% vs CAPM hurdle 10.0%. Downtrend -7% vs 200-day avg; 12-1 mom +3%; RSI 40. Quality z +0.31 (ROE 22%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.41"
    Avoid: not owned. Analyst target 95.99 HKD vs 51.45 HKD (+87%, 21 analysts); de-biased α +6.3% vs CAPM hurdle 7.3%. Downtrend -22% vs 200-day avg; 12-1 mom -31%; RSI 54. Quality z -0.99 (ROE 3%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.43"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,488 JPY (+41%, 17 analysts); de-biased α -5.5% vs CAPM hurdle 10.8%. Downtrend -13% vs 200-day avg; 12-1 mom +30%; RSI 39. Quality z -0.20 (ROE 10%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 705.00 USD | $81,780 | 10.1% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 190,800 KRW | $65,690 | 8.1% | Hold |
| TSM | TSMC | 127 | 362.62 USD | $46,053 | 5.7% | Buy |
| NVDA | NVIDIA | 268 | 150.87 USD | $40,433 | 5.0% | Strong Buy |
| KLAC | KLA Corp | 268 | 145.19 USD | $38,911 | 4.8% | Hold |
| MRVL | Marvell Technology | 248 | 145.55 USD | $36,096 | 4.4% | Strong Buy |
| 000660.KS | SK hynix | 41 | 1,124,000 KRW | $34,642 | 4.3% | Strong Buy |
| AMAT | Applied Materials | 84 | 352.53 USD | $29,613 | 3.6% | Buy |
| ASX | ASE Technology | 805 | 32.54 USD | $26,195 | 3.2% | Buy |
| 6857.T | Advantest | 100 | 26,860 JPY | $16,839 | 2.1% | Buy |
| INTC | Intel | 230 | 54.68 USD | $12,576 | 1.5% | Buy |
| LRCX | Lam Research | 58 | 211.71 USD | $12,279 | 1.5% | Buy |
| IFX.DE | Infineon Technologies | 225 | 49.22 EUR | $12,142 | 1.5% | Buy |
| TER | Teradyne | 35 | 235.30 USD | $8,236 | 1.0% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-17 03:55 UTC | TRIM | 000660.KS | -47 | 1,144,000.00 | $40,195 |
| 2026-11-16 20:30 UTC | ADD | ASX | 231 | 32.86 | $7,591 |
| 2026-11-16 20:30 UTC | ADD | INTC | 78 | 55.61 | $4,338 |
| 2026-11-16 20:30 UTC | TRIM | NVDA | -69 | 155.52 | $10,731 |
| 2026-11-13 16:26 UTC | ADD | NVDA | 79 | 159.94 | $12,635 |
| 2026-11-13 16:26 UTC | ADD | AMAT | 23 | 357.03 | $8,212 |
| 2026-11-13 16:26 UTC | TRIM | ASX | -290 | 34.86 | $10,109 |
| 2026-11-13 00:26 UTC | TRIM | 005930.KS | -104 | 214,000.00 | $16,663 |
| 2026-11-12 18:57 UTC | ADD | NVDA | 79 | 164.84 | $13,022 |
| 2026-11-12 18:57 UTC | ADD | AMAT | 20 | 386.98 | $7,740 |
| 2026-11-11 15:13 UTC | TRIM | AMAT | -32 | 387.02 | $12,385 |
| 2026-11-11 15:13 UTC | TRIM | MRVL | -76 | 165.15 | $12,551 |
| 2026-11-11 15:13 UTC | TRIM | INTC | -83 | 61.66 | $5,118 |
| 2026-11-11 06:23 UTC | ADD | 000660.KS | 38 | 1,277,000.00 | $36,371 |
| 2026-11-10 17:51 UTC | ADD | ASX | 552 | 34.76 | $19,188 |
| 2026-11-10 17:51 UTC | TRIM | INTC | -140 | 57.20 | $8,008 |
| 2026-11-09 17:30 UTC | ADD | NVDA | 119 | 177.94 | $21,175 |
| 2026-11-09 17:30 UTC | ADD | INTC | 112 | 58.31 | $6,531 |
| 2026-11-09 17:30 UTC | TRIM | AMAT | -18 | 370.39 | $6,667 |
| 2026-11-06 17:58 UTC | ADD | AMAT | 20 | 333.00 | $6,660 |
| 2026-11-06 17:58 UTC | SELL (exit) | ASML | -30 | 1,418.92 | $42,568 |
| 2026-11-06 17:58 UTC | TRIM | INTC | -184 | 55.91 | $10,287 |
| 2026-11-06 02:27 UTC | ADD | 005930.KS | 240 | 191,400.00 | $33,864 |
| 2026-11-06 02:27 UTC | TRIM | 000660.KS | -30 | 1,169,000.00 | $25,854 |
| 2026-11-06 02:27 UTC | TRIM | 6857.T | -100 | 27,610.00 | $17,487 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 54.3%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
