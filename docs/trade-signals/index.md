---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-18 13:59 UTC (Wed Nov 18, 08:59 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Wed 08:59) · Tokyo 🔴 closed (Wed 22:59) · Korea 🔴 closed (Wed 22:59) · Hong Kong 🔴 closed (Wed 21:59) · Xetra 🟢 open (Wed 14:59) · Euronext Amsterdam 🟢 open (Wed 14:59)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$815,447** | $350,409 (43%) | $465,038 (57%) | -18.46% | -74.99% | 🔴 Risk-off (-11.9%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $815,447), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **TSM**<br><small>TSMC</small> | 73 | 359.69 USD | $26,257 | Queued · NYSE/Nasdaq closed | quality +0.28 · analyst α -0.15 |
| ADD | **MRVL**<br><small>Marvell Technology</small> | 144 | 148.81 USD | $21,429 | Queued · NYSE/Nasdaq closed | momentum +0.41 · analyst α +0.31 · ⚠️ rich valuation |
| ADD | **NVDA**<br><small>NVIDIA</small> | 91 | 155.46 USD | $14,146 | Queued · NYSE/Nasdaq closed | analyst α +0.48 · momentum -0.23 · ⚠️ oversold |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 23 | 349.22 USD | $8,032 | Queued · NYSE/Nasdaq closed | analyst α +0.15 · momentum +0.07 |
| ADD | **INTC**<br><small>Intel</small> | 124 | 55.17 USD | $6,842 | Queued · NYSE/Nasdaq closed | analyst α +0.41 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.99 | **MU**<br><small>Micron Technology</small> | 712.42 USD | +113% | +10.5% | +267% | -7% | 38 | +0.12 | 10.1% → 10.0% | – | analyst α +0.55 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.22 | **Samsung**<br><small>005930.KS</small> | 193,600 KRW | +147% | +19.6% | +119% | -19% | 38 | -0.26 | 8.2% → 10.0% | – | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.48 | **MRVL**<br><small>Marvell Technology</small> | 148.81 USD | +97% | +6.5% | +189% | -21% | 34 | -0.12 | 4.5% → 7.2% | ADD 144 | momentum +0.41 · analyst α +0.31 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.08 | **SK hynix**<br><small>000660.KS</small> | 1,148,000 KRW | – | +0.0% | +107% | -25% | 39 | +0.62 | 4.3% → 4.9% | – | quality +0.33 · momentum +0.20 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.92 | **NVDA**<br><small>NVIDIA</small> | 155.46 USD | +111% | +9.9% | +16% | -24% | 23 | +0.47 | 5.1% → 6.8% | ADD 91 | analyst α +0.48 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.56 | **INTC**<br><small>Intel</small> | 55.17 USD | +111% | +9.9% | +164% | -37% | 30 | -0.62 | 1.6% → 2.4% | ADD 124 | analyst α +0.41 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.42 | **ASX**<br><small>ASE Technology</small> | 31.83 USD | +60% | -1.0% | +182% | -7% | 37 | -0.68 | 3.1% → 2.9% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.41 | **AMAT**<br><small>Applied Materials</small> | 349.22 USD | +83% | +3.6% | +78% | -22% | 39 | +0.03 | 3.6% → 2.6% | TRIM 23 | analyst α +0.15 · momentum +0.07 |
| 🟢 Buy | +0.26 | **TSM**<br><small>TSMC</small> | 359.69 USD | +54% | -3.5% | +49% | -11% | 36 | +0.58 | 5.6% → 2.4% | TRIM 73 | quality +0.28 · analyst α -0.15 |
| ⚪ Hold | +0.18 | **LRCX**<br><small>Lam Research</small> | 210.68 USD | +78% | +2.1% | +79% | -26% | 38 | +0.02 | 1.5% → 1.5% | – | trend -0.14 · analyst α +0.12 |
| ⚪ Hold | +0.18 | **Infineon**<br><small>IFX.DE</small> | 49.96 EUR | +74% | +0.6% | +60% | -13% | 46 | -0.04 | 1.5% → 1.5% | – | analyst α +0.05 · quality -0.04 |
| ⚪ Hold | +0.15 | **Advantest**<br><small>6857.T</small> | 27,315 JPY | +56% | -3.6% | +59% | -7% | 39 | +0.33 | 2.1% → 2.1% | – | analyst α -0.19 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.06 | **KLAC**<br><small>KLA Corp</small> | 144.41 USD | +62% | -1.6% | +43% | -20% | 41 | +0.51 | 4.7% → 4.7% | – | quality +0.24 · momentum -0.10 |
| ⚪ Hold | +0.06 | **ASML**<br><small>ASML Holding</small> | 1,383.91 USD | +52% | -4.5% | +61% | -13% | 35 | +0.42 | 0.0% → 0.0% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | -0.04 | **TER**<br><small>Teradyne</small> | 234.80 USD | +90% | +5.1% | +101% | -33% | 35 | -0.31 | 1.0% → 1.0% | – | analyst α +0.23 · trend -0.21 |
| ⚪ Hold | -0.17 | **AMD**<br><small>Advanced Micro Devices</small> | 503.69 USD | +23% | -12.3% | +122% | +18% | 47 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.33 | **ASMI**<br><small>ASM.AS</small> | 680.00 EUR | +66% | -1.1% | +56% | -16% | 43 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · analyst α -0.05 |
| 🔴 Sell | -0.34 | **GFS**<br><small>GlobalFoundries</small> | 39.60 USD | +92% | +5.6% | +40% | -28% | 40 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.16 |
| 🔴 Sell | -0.37 | **ENTG**<br><small>Entegris</small> | 140.73 USD | +23% | -11.3% | +92% | +1% | 47 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.21 |
| 🔴 Sell | -0.38 | **Tokyo Electron**<br><small>8035.T</small> | 8,690 JPY | +76% | +1.6% | +51% | -16% | 39 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.08 |
| 🔴 Sell | -0.57 | **AMKR**<br><small>Amkor Technology</small> | 34.05 USD | +124% | +13.4% | +33% | -39% | 39 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴 Sell | -0.60 | **Disco**<br><small>6146.T</small> | 44,530 JPY | +84% | +3.8% | +4% | -31% | 40 | +0.06 | 0.0% → 0.0% | – | momentum -0.30 · analyst α +0.19 |
| 🔴🔴 Strong Sell | -0.77 | **ARM**<br><small>Arm Holdings</small> | 183.33 USD | +57% | -4.9% | +58% | -22% | 40 | +0.04 | 0.0% → 0.0% | – | analyst α -0.27 · trend -0.06 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.77 | **AVGO**<br><small>Broadcom</small> | 341.69 USD | +55% | -3.1% | -2% | -7% | 51 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.12 |
| 🔴🔴 Strong Sell | -0.83 | **QCOM**<br><small>Qualcomm</small> | 166.71 USD | +16% | -12.7% | +8% | -2% | 45 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.87 | **SNPS**<br><small>Synopsys</small> | 435.51 USD | +31% | -9.2% | +17% | -1% | 42 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.20 |
| 🔴🔴 Strong Sell | -0.96 | **TXN**<br><small>Texas Instruments</small> | 295.81 USD | +10% | -14.2% | +82% | +12% | 51 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.07 | **CDNS**<br><small>Cadence Design Systems</small> | 306.87 USD | +32% | -8.8% | +3% | -7% | 41 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.36 | **Shin-Etsu**<br><small>4063.T</small> | 5,571 JPY | +39% | -6.8% | +30% | -12% | 41 | -0.20 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.17 |
| 🔴🔴 Strong Sell | -1.52 | **SMIC**<br><small>0981.HK</small> | 49.20 HKD | +95% | +7.6% | -31% | -25% | 49 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.36 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.99"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 712.42 USD (+113%, 46 analysts); de-biased α +10.5% vs CAPM hurdle 14.0%. Downtrend -7% vs 200-day avg; 12-1 mom +267%; RSI 38. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.22"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 193,600 KRW (+147%, 36 analysts); de-biased α +19.6% vs CAPM hurdle 11.3%. Downtrend -19% vs 200-day avg; 12-1 mom +119%; RSI 38. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.48"
    **ADD 144 sh** → target 7.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 148.81 USD (+97%, 43 analysts); de-biased α +6.5% vs CAPM hurdle 14.1%. Downtrend -21% vs 200-day avg; 12-1 mom +189%; RSI 34. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.08"
    Within rebalance band of target 4.9%: no trade. No reliable analyst target: α set to 0. Downtrend -25% vs 200-day avg; 12-1 mom +107%; RSI 39. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +0.92"
    **ADD 91 sh** → target 6.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 155.46 USD (+111%, 59 analysts); de-biased α +9.9% vs CAPM hurdle 13.9%. Downtrend -24% vs 200-day avg; 12-1 mom +16%; RSI 23. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "INTC (INTC) — 🟢 Buy, score +0.56"
    **ADD 124 sh** → target 2.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 55.17 USD (+111%, 43 analysts); de-biased α +9.9% vs CAPM hurdle 14.0%. Downtrend -37% vs 200-day avg; 12-1 mom +164%; RSI 30. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "ASX (ASX) — 🟢 Buy, score +0.42"
    Within rebalance band of target 2.9%: no trade. Analyst target 51.00 USD vs 31.83 USD (+60%, 1 analysts); de-biased α -1.0% vs CAPM hurdle 11.9%. Downtrend -7% vs 200-day avg; 12-1 mom +182%; RSI 37. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.41"
    **TRIM 23 sh** → target 2.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 349.22 USD (+83%, 36 analysts); de-biased α +3.6% vs CAPM hurdle 11.6%. Downtrend -22% vs 200-day avg; 12-1 mom +78%; RSI 39. Quality z +0.03 (ROE 36%).

??? success "TSM (TSM) — 🟢 Buy, score +0.26"
    **TRIM 73 sh** → target 2.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 359.69 USD (+54%, 20 analysts); de-biased α -3.5% vs CAPM hurdle 10.8%. Downtrend -11% vs 200-day avg; 12-1 mom +49%; RSI 36. Quality z +0.58 (ROE 35%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.18"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 210.68 USD (+78%, 31 analysts); de-biased α +2.1% vs CAPM hurdle 12.6%. Downtrend -26% vs 200-day avg; 12-1 mom +79%; RSI 38. Quality z +0.02 (ROE 65%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.18"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 49.96 EUR (+74%, 23 analysts); de-biased α +0.6% vs CAPM hurdle 14.1%. Downtrend -13% vs 200-day avg; 12-1 mom +60%; RSI 46. Quality z -0.04 (ROE 6%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 27,315 JPY (+56%, 21 analysts); de-biased α -3.6% vs CAPM hurdle 13.4%. Downtrend -7% vs 200-day avg; 12-1 mom +59%; RSI 39. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 144.41 USD (+62%, 26 analysts); de-biased α -1.6% vs CAPM hurdle 11.1%. Downtrend -20% vs 200-day avg; 12-1 mom +43%; RSI 41. Quality z +0.51 (ROE 87%).

??? note "ASML (ASML) — ⚪ Hold, score +0.06"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,383.91 USD (+52%, 16 analysts); de-biased α -4.5% vs CAPM hurdle 12.3%. Downtrend -13% vs 200-day avg; 12-1 mom +61%; RSI 35. Quality z +0.42 (ROE 50%).

??? note "TER (TER) — ⚪ Hold, score -0.04"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 234.80 USD (+90%, 15 analysts); de-biased α +5.1% vs CAPM hurdle 12.3%. Downtrend -33% vs 200-day avg; 12-1 mom +101%; RSI 35. Quality z -0.31 (ROE 20%).

??? note "AMD (AMD) — ⚪ Hold, score -0.17"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 503.69 USD (+23%, 50 analysts); de-biased α -12.3% vs CAPM hurdle 14.9%. Uptrend +18% vs 200-day avg; 12-1 mom +122%; RSI 47. Quality z -0.15 (ROE 7%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.33"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 680.00 EUR (+66%, 19 analysts); de-biased α -1.1% vs CAPM hurdle 13.2%. Downtrend -16% vs 200-day avg; 12-1 mom +56%; RSI 43. Quality z -0.10 (ROE 19%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.34"
    Avoid: not owned. Analyst target 76.00 USD vs 39.60 USD (+92%, 22 analysts); de-biased α +5.6% vs CAPM hurdle 12.4%. Downtrend -28% vs 200-day avg; 12-1 mom +40%; RSI 40. Quality z -0.21 (ROE 8%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 173.36 USD vs 140.73 USD (+23%, 11 analysts); de-biased α -11.3% vs CAPM hurdle 11.0%. Uptrend +1% vs 200-day avg; 12-1 mom +92%; RSI 47. Quality z -0.02 (ROE 6%).

??? failure "Tokyo Electron (8035.T) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 15,275 JPY vs 8,690 JPY (+76%, 23 analysts); de-biased α +1.6% vs CAPM hurdle 12.8%. Downtrend -16% vs 200-day avg; 12-1 mom +51%; RSI 39. Quality z -0.28 (ROE 29%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 76.40 USD vs 34.05 USD (+124%, 10 analysts); de-biased α +13.4% vs CAPM hurdle 14.0%. Downtrend -39% vs 200-day avg; 12-1 mom +33%; RSI 39. Quality z -1.00 (ROE 9%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.60"
    Avoid: not owned. Analyst target 81,730 JPY vs 44,530 JPY (+84%, 20 analysts); de-biased α +3.8% vs CAPM hurdle 11.5%. Downtrend -31% vs 200-day avg; 12-1 mom +4%; RSI 40. Quality z +0.06 (ROE 25%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.77"
    Avoid: not owned. Analyst target 288.70 USD vs 183.33 USD (+57%, 40 analysts); de-biased α -4.9% vs CAPM hurdle 19.6%. Downtrend -22% vs 200-day avg; 12-1 mom +58%; RSI 40. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.77"
    Avoid: not owned. Analyst target 531.31 USD vs 341.69 USD (+55%, 47 analysts); de-biased α -3.1% vs CAPM hurdle 11.2%. Downtrend -7% vs 200-day avg; 12-1 mom -2%; RSI 51. Quality z +0.26 (ROE 31%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.83"
    Avoid: not owned. Analyst target 194.13 USD vs 166.71 USD (+16%, 30 analysts); de-biased α -12.7% vs CAPM hurdle 11.9%. Downtrend -2% vs 200-day avg; 12-1 mom +8%; RSI 45. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.87"
    Avoid: not owned. Analyst target 569.78 USD vs 435.51 USD (+31%, 26 analysts); de-biased α -9.2% vs CAPM hurdle 10.3%. Downtrend -1% vs 200-day avg; 12-1 mom +17%; RSI 42. Quality z +0.14 (ROE 7%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.96"
    Avoid: not owned. Analyst target 324.71 USD vs 295.81 USD (+10%, 31 analysts); de-biased α -14.2% vs CAPM hurdle 10.8%. Uptrend +12% vs 200-day avg; 12-1 mom +82%; RSI 51. Quality z +0.24 (ROE 30%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.07"
    Avoid: not owned. Analyst target 405.47 USD vs 306.87 USD (+32%, 26 analysts); de-biased α -8.8% vs CAPM hurdle 10.0%. Downtrend -7% vs 200-day avg; 12-1 mom +3%; RSI 41. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.36"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,571 JPY (+39%, 17 analysts); de-biased α -6.8% vs CAPM hurdle 10.8%. Downtrend -12% vs 200-day avg; 12-1 mom +30%; RSI 41. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.52"
    Avoid: not owned. Analyst target 95.99 HKD vs 49.20 HKD (+95%, 21 analysts); de-biased α +7.6% vs CAPM hurdle 7.3%. Downtrend -25% vs 200-day avg; 12-1 mom -31%; RSI 49. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 712.42 USD | $82,641 | 10.1% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 193,600 KRW | $66,559 | 8.2% | Strong Buy |
| TSM | TSMC | 127 | 359.69 USD | $45,681 | 5.6% | Buy |
| NVDA | NVIDIA | 268 | 155.46 USD | $41,662 | 5.1% | Strong Buy |
| KLAC | KLA Corp | 268 | 144.41 USD | $38,702 | 4.7% | Hold |
| MRVL | Marvell Technology | 248 | 148.81 USD | $36,905 | 4.5% | Strong Buy |
| 000660.KS | SK hynix | 41 | 1,148,000 KRW | $35,331 | 4.3% | Strong Buy |
| AMAT | Applied Materials | 84 | 349.22 USD | $29,334 | 3.6% | Buy |
| ASX | ASE Technology | 805 | 31.83 USD | $25,623 | 3.1% | Buy |
| 6857.T | Advantest | 100 | 27,315 JPY | $17,139 | 2.1% | Hold |
| INTC | Intel | 230 | 55.17 USD | $12,690 | 1.6% | Buy |
| IFX.DE | Infineon Technologies | 225 | 49.96 EUR | $12,334 | 1.5% | Hold |
| LRCX | Lam Research | 58 | 210.68 USD | $12,219 | 1.5% | Hold |
| TER | Teradyne | 35 | 234.80 USD | $8,218 | 1.0% | Hold |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 57.5%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
