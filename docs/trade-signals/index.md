---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-13 00:26 UTC (Thu Nov 12, 07:26 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Thu 19:26) · Tokyo 🟢 open (Fri 09:26) · Korea 🟢 open (Fri 09:26) · Hong Kong 🔴 closed (Fri 08:26) · Xetra 🔴 closed (Fri 01:26) · Euronext Amsterdam 🔴 closed (Fri 01:26)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$871,209** | $322,195 (37%) | $549,013 (63%) | -12.88% | -72.59% | 🔴 Risk-off (-3.2%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $871,209), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **Samsung**<br><small>005930.KS</small> | 104 | 214,000 KRW | $16,663 | Executed (paper) | analyst α +0.66 · quality -0.16 · ⚠️ cycle-peak P/E |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.09 | **SK hynix**<br><small>000660.KS</small> | 1,307,000 KRW | +140% | +19.9% | +104% | -14% | 46 | +0.62 | 9.9% → 10.0% | – | analyst α +0.85 · quality +0.33 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.41 | **MU**<br><small>Micron Technology</small> | 798.90 USD | +90% | +7.5% | +280% | +5% | 44 | +0.12 | 10.6% → 9.8% | – | momentum +0.53 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.46 | **Samsung**<br><small>005930.KS</small> | 214,000 KRW | +123% | +16.5% | +94% | -10% | 46 | -0.26 | 8.4% → 8.4% | TRIM 104 | analyst α +0.66 · quality -0.16 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.07 | **MRVL**<br><small>Marvell Technology</small> | 164.48 USD | +79% | +4.6% | +175% | -12% | 37 | -0.12 | 4.7% → 4.5% | – | momentum +0.35 · analyst α +0.23 · ⚠️ rich valuation |
| 🟢 Buy | +0.64 | **NVDA**<br><small>NVIDIA</small> | 166.04 USD | +97% | +9.3% | +15% | -19% | 26 | +0.47 | 4.9% → 4.2% | – | analyst α +0.41 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.55 | **ASX**<br><small>ASE Technology</small> | 36.29 USD | +41% | -2.1% | +199% | +7% | 45 | -0.68 | 3.6% → 3.4% | – | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.48 | **AMAT**<br><small>Applied Materials</small> | 381.28 USD | +68% | +2.5% | +96% | -14% | 45 | +0.03 | 2.7% → 2.7% | – | momentum +0.17 · analyst α +0.12 |
| 🟢 Buy | +0.29 | **INTC**<br><small>Intel</small> | 61.22 USD | +90% | +7.4% | +159% | -30% | 33 | -0.62 | 1.1% → 1.1% | – | analyst α +0.31 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.27 | **Advantest**<br><small>6857.T</small> | 31,690 JPY | +35% | -6.2% | +83% | +8% | 47 | +0.33 | 2.3% → 1.2% | – | analyst α -0.31 · trend +0.18 · ⚠️ rich valuation |
| ⚪ Hold | +0.14 | **TSM**<br><small>TSMC</small> | 405.65 USD | +36% | -5.1% | +49% | +1% | 47 | +0.58 | 5.9% → 5.9% | – | quality +0.28 · analyst α -0.19 |
| ⚪ Hold | +0.14 | **ASML**<br><small>ASML Holding</small> | 1,497.12 USD | +40% | -4.5% | +62% | -6% | 42 | +0.42 | 0.0% → 0.0% | – | quality +0.18 · analyst α -0.15 |
| ⚪ Hold | +0.08 | **KLAC**<br><small>KLA Corp</small> | 157.31 USD | +49% | -2.1% | +51% | -13% | 48 | +0.51 | 4.8% → 4.8% | – | quality +0.24 · analyst α -0.08 |
| ⚪ Hold | +0.05 | **TER**<br><small>Teradyne</small> | 263.74 USD | +69% | +2.7% | +103% | -25% | 40 | -0.31 | 1.1% → 1.1% | – | quality -0.21 · momentum +0.20 |
| ⚪ Hold | -0.01 | **Infineon**<br><small>IFX.DE</small> | 52.29 EUR | +66% | +1.5% | +55% | -9% | 50 | -0.04 | 1.5% → 1.5% | – | analyst α +0.08 · momentum -0.05 |
| ⚪ Hold | -0.04 | **LRCX**<br><small>Lam Research</small> | 233.79 USD | +60% | +0.5% | +81% | -18% | 44 | +0.02 | 1.6% → 1.6% | – | trend -0.10 · momentum +0.07 |
| ⚪ Hold | -0.15 | **Tokyo Electron**<br><small>8035.T</small> | 9,538 JPY | +60% | +0.5% | +76% | -8% | 47 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.05 |
| ⚪ Hold | -0.19 | **ASMI**<br><small>ASM.AS</small> | 726.80 EUR | +55% | -1.0% | +65% | -10% | 47 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · trend -0.02 |
| 🔴 Sell | -0.27 | **GFS**<br><small>GlobalFoundries</small> | 42.64 USD | +78% | +4.9% | +41% | -22% | 47 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.14 |
| 🔴 Sell | -0.40 | **ENTG**<br><small>Entegris</small> | 153.26 USD | +13% | -11.0% | +83% | +10% | 54 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.21 |
| 🔴 Sell | -0.55 | **Disco**<br><small>6146.T</small> | 48,930 JPY | +67% | +2.5% | +4% | -25% | 47 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · trend -0.18 |
| 🔴 Sell | -0.60 | **TXN**<br><small>Texas Instruments</small> | 312.50 USD | +4% | -12.8% | +79% | +19% | 61 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.25 |
| 🔴🔴 Strong Sell | -0.79 | **SNPS**<br><small>Synopsys</small> | 462.65 USD | +23% | -8.4% | +21% | +5% | 52 | +0.14 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.20 |
| 🔴🔴 Strong Sell | -0.80 | **ARM**<br><small>Arm Holdings</small> | 199.82 USD | +44% | -5.4% | +59% | -14% | 43 | +0.04 | 0.0% → 0.0% | – | analyst α -0.27 · trend -0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.82 | **QCOM**<br><small>Qualcomm</small> | 177.16 USD | +10% | -11.7% | +1% | +5% | 52 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.82 | **AVGO**<br><small>Broadcom</small> | 364.38 USD | +46% | -2.7% | -1% | -1% | 60 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.12 |
| 🔴🔴 Strong Sell | -0.83 | **AMKR**<br><small>Amkor Technology</small> | 37.11 USD | +106% | +11.5% | +32% | -34% | 44 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.84 | **AMD**<br><small>Advanced Micro Devices</small> | 585.58 USD | +6% | -13.8% | +140% | +39% | 58 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.07 | **Shin-Etsu**<br><small>4063.T</small> | 5,777 JPY | +34% | -5.3% | +35% | -9% | 48 | -0.20 | 0.0% → 0.0% | – | analyst α -0.23 · momentum -0.14 |
| 🔴🔴 Strong Sell | -1.13 | **CDNS**<br><small>Cadence Design Systems</small> | 333.23 USD | +22% | -8.7% | +3% | +2% | 53 | +0.31 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.36 | **SMIC**<br><small>0981.HK</small> | 48.74 HKD | +97% | +10.8% | -23% | -27% | 46 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.48 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.09"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,307,000 KRW (+140%, 38 analysts); de-biased α +19.9% vs CAPM hurdle 14.3%. Downtrend -14% vs 200-day avg; 12-1 mom +104%; RSI 46. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.41"
    Within rebalance band of target 9.8%: no trade. Analyst target 1,520.02 USD vs 798.90 USD (+90%, 46 analysts); de-biased α +7.5% vs CAPM hurdle 14.0%. Uptrend +5% vs 200-day avg; 12-1 mom +280%; RSI 44. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.46"
    **TRIM 104 sh** → target 8.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 477,517 KRW vs 214,000 KRW (+123%, 36 analysts); de-biased α +16.5% vs CAPM hurdle 11.3%. Downtrend -10% vs 200-day avg; 12-1 mom +94%; RSI 46. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.07"
    Within rebalance band of target 4.5%: no trade. Analyst target 293.88 USD vs 164.48 USD (+79%, 43 analysts); de-biased α +4.6% vs CAPM hurdle 14.1%. Downtrend -12% vs 200-day avg; 12-1 mom +175%; RSI 37. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.64"
    Within rebalance band of target 4.2%: no trade. Analyst target 327.70 USD vs 166.04 USD (+97%, 59 analysts); de-biased α +9.3% vs CAPM hurdle 13.9%. Downtrend -19% vs 200-day avg; 12-1 mom +15%; RSI 26. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "ASX (ASX) — 🟢 Buy, score +0.55"
    Within rebalance band of target 3.4%: no trade. Analyst target 51.00 USD vs 36.29 USD (+41%, 1 analysts); de-biased α -2.1% vs CAPM hurdle 11.9%. Uptrend +7% vs 200-day avg; 12-1 mom +199%; RSI 45. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.48"
    Within rebalance band of target 2.7%: no trade. Analyst target 638.94 USD vs 381.28 USD (+68%, 36 analysts); de-biased α +2.5% vs CAPM hurdle 11.6%. Downtrend -14% vs 200-day avg; 12-1 mom +96%; RSI 45. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.29"
    Within rebalance band of target 1.1%: no trade. Analyst target 116.37 USD vs 61.22 USD (+90%, 43 analysts); de-biased α +7.4% vs CAPM hurdle 14.0%. Downtrend -30% vs 200-day avg; 12-1 mom +159%; RSI 33. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "Advantest (6857.T) — 🟢 Buy, score +0.27"
    Within rebalance band of target 1.2%: no trade. Analyst target 42,686 JPY vs 31,690 JPY (+35%, 21 analysts); de-biased α -6.2% vs CAPM hurdle 13.4%. Uptrend +8% vs 200-day avg; 12-1 mom +83%; RSI 47. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "TSM (TSM) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 405.65 USD (+36%, 20 analysts); de-biased α -5.1% vs CAPM hurdle 10.8%. Uptrend +1% vs 200-day avg; 12-1 mom +49%; RSI 47. Quality z +0.58 (ROE 35%).

??? note "ASML (ASML) — ⚪ Hold, score +0.14"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,497.12 USD (+40%, 16 analysts); de-biased α -4.5% vs CAPM hurdle 12.3%. Downtrend -6% vs 200-day avg; 12-1 mom +62%; RSI 42. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 157.31 USD (+49%, 26 analysts); de-biased α -2.1% vs CAPM hurdle 11.1%. Downtrend -13% vs 200-day avg; 12-1 mom +51%; RSI 48. Quality z +0.51 (ROE 87%).

??? note "TER (TER) — ⚪ Hold, score +0.05"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 263.74 USD (+69%, 15 analysts); de-biased α +2.7% vs CAPM hurdle 12.3%. Downtrend -25% vs 200-day avg; 12-1 mom +103%; RSI 40. Quality z -0.31 (ROE 20%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score -0.01"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 52.29 EUR (+66%, 23 analysts); de-biased α +1.5% vs CAPM hurdle 14.1%. Downtrend -9% vs 200-day avg; 12-1 mom +55%; RSI 50. Quality z -0.04 (ROE 6%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.04"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 233.79 USD (+60%, 31 analysts); de-biased α +0.5% vs CAPM hurdle 12.6%. Downtrend -18% vs 200-day avg; 12-1 mom +81%; RSI 44. Quality z +0.02 (ROE 65%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score -0.15"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 9,538 JPY (+60%, 23 analysts); de-biased α +0.5% vs CAPM hurdle 12.8%. Downtrend -8% vs 200-day avg; 12-1 mom +76%; RSI 47. Quality z -0.28 (ROE 29%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.19"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 726.80 EUR (+55%, 19 analysts); de-biased α -1.0% vs CAPM hurdle 13.2%. Downtrend -10% vs 200-day avg; 12-1 mom +65%; RSI 47. Quality z -0.10 (ROE 19%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 76.00 USD vs 42.64 USD (+78%, 22 analysts); de-biased α +4.9% vs CAPM hurdle 12.4%. Downtrend -22% vs 200-day avg; 12-1 mom +41%; RSI 47. Quality z -0.21 (ROE 8%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.40"
    Avoid: not owned. Analyst target 173.36 USD vs 153.26 USD (+13%, 11 analysts); de-biased α -11.0% vs CAPM hurdle 11.0%. Uptrend +10% vs 200-day avg; 12-1 mom +83%; RSI 54. Quality z -0.02 (ROE 6%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 81,730 JPY vs 48,930 JPY (+67%, 20 analysts); de-biased α +2.5% vs CAPM hurdle 11.5%. Downtrend -25% vs 200-day avg; 12-1 mom +4%; RSI 47. Quality z +0.06 (ROE 25%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.60"
    Avoid: not owned. Analyst target 324.71 USD vs 312.50 USD (+4%, 31 analysts); de-biased α -12.8% vs CAPM hurdle 10.8%. Uptrend +19% vs 200-day avg; 12-1 mom +79%; RSI 61. Quality z +0.24 (ROE 30%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.79"
    Avoid: not owned. Analyst target 569.78 USD vs 462.65 USD (+23%, 26 analysts); de-biased α -8.4% vs CAPM hurdle 10.3%. Uptrend +5% vs 200-day avg; 12-1 mom +21%; RSI 52. Quality z +0.14 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.80"
    Avoid: not owned. Analyst target 288.70 USD vs 199.82 USD (+44%, 40 analysts); de-biased α -5.4% vs CAPM hurdle 19.6%. Downtrend -14% vs 200-day avg; 12-1 mom +59%; RSI 43. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 194.13 USD vs 177.16 USD (+10%, 30 analysts); de-biased α -11.7% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +1%; RSI 52. Quality z +0.70 (ROE 23%).

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 531.31 USD vs 364.38 USD (+46%, 47 analysts); de-biased α -2.7% vs CAPM hurdle 11.2%. Downtrend -1% vs 200-day avg; 12-1 mom -1%; RSI 60. Quality z +0.26 (ROE 31%).

??? failure "AMKR (AMKR) — 🔴🔴 Strong Sell, score -0.83"
    Avoid: not owned. Analyst target 76.40 USD vs 37.11 USD (+106%, 10 analysts); de-biased α +11.5% vs CAPM hurdle 14.0%. Downtrend -34% vs 200-day avg; 12-1 mom +32%; RSI 44. Quality z -1.00 (ROE 9%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -0.84"
    Avoid: not owned. Analyst target 619.51 USD vs 585.58 USD (+6%, 50 analysts); de-biased α -13.8% vs CAPM hurdle 14.9%. Uptrend +39% vs 200-day avg; 12-1 mom +140%; RSI 58. Quality z -0.15 (ROE 7%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.07"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,777 JPY (+34%, 17 analysts); de-biased α -5.3% vs CAPM hurdle 10.8%. Downtrend -9% vs 200-day avg; 12-1 mom +35%; RSI 48. Quality z -0.20 (ROE 10%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.13"
    Avoid: not owned. Analyst target 405.47 USD vs 333.23 USD (+22%, 26 analysts); de-biased α -8.7% vs CAPM hurdle 10.0%. Uptrend +2% vs 200-day avg; 12-1 mom +3%; RSI 53. Quality z +0.31 (ROE 22%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.36"
    Avoid: not owned. Analyst target 95.99 HKD vs 48.74 HKD (+97%, 21 analysts); de-biased α +10.8% vs CAPM hurdle 7.3%. Downtrend -27% vs 200-day avg; 12-1 mom -23%; RSI 46. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 798.90 USD | $92,672 | 10.6% | Strong Buy |
| 000660.KS | SK hynix | 88 | 1,307,000 KRW | $86,110 | 9.9% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 214,000 KRW | $73,380 | 8.4% | Strong Buy |
| TSM | TSMC | 127 | 405.65 USD | $51,518 | 5.9% | Hold |
| NVDA | NVIDIA | 258 | 166.04 USD | $42,838 | 4.9% | Buy |
| KLAC | KLA Corp | 268 | 157.31 USD | $42,159 | 4.8% | Hold |
| MRVL | Marvell Technology | 248 | 164.48 USD | $40,791 | 4.7% | Strong Buy |
| ASX | ASE Technology | 864 | 36.29 USD | $31,355 | 3.6% | Buy |
| AMAT | Applied Materials | 61 | 381.28 USD | $23,258 | 2.7% | Buy |
| 6857.T | Advantest | 100 | 31,690 JPY | $19,828 | 2.3% | Buy |
| LRCX | Lam Research | 58 | 233.79 USD | $13,560 | 1.6% | Hold |
| IFX.DE | Infineon Technologies | 225 | 52.29 EUR | $13,007 | 1.5% | Hold |
| INTC | Intel | 152 | 61.22 USD | $9,305 | 1.1% | Buy |
| TER | Teradyne | 35 | 263.74 USD | $9,231 | 1.1% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-11-05 15:28 UTC | ADD | INTC | 309 | 52.94 | $16,359 |
| 2026-11-05 15:28 UTC | ADD | MRVL | 160 | 140.70 | $22,512 |
| 2026-11-05 15:28 UTC | ADD | MU | 52 | 693.52 | $36,063 |
| 2026-11-05 15:28 UTC | ADD | AMAT | 21 | 332.95 | $6,992 |
| 2026-11-05 15:28 UTC | TRIM | LRCX | -104 | 195.72 | $20,355 |
| 2026-11-04 17:18 UTC | TRIM | AMAT | -12 | 366.64 | $4,400 |
| 2026-11-04 17:18 UTC | TRIM | INTC | -98 | 57.47 | $5,632 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 46.3%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
