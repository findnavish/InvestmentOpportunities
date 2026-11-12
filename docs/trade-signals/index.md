---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-12 18:57 UTC (Thu Nov 12, 01:57 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Thu 13:57) · Tokyo 🔴 closed (Fri 03:57) · Korea 🔴 closed (Fri 03:57) · Hong Kong 🔴 closed (Fri 02:57) · Xetra 🔴 closed (Thu 19:57) · Euronext Amsterdam 🔴 closed (Thu 19:57)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$864,676** | $305,541 (35%) | $559,135 (65%) | -13.53% | -72.59% | 🔴 Risk-off (-3.2%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $864,676), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **SK hynix**<br><small>000660.KS</small> | 46 | 1,255,000 KRW | $43,227 | Queued · Korea closed | quality +0.33 · momentum +0.26 · ⚠️ cycle-peak P/E, high σ(e) |
| ADD | **NVDA**<br><small>NVIDIA</small> | 79 | 164.84 USD | $13,022 | Executed (paper) | analyst α +0.48 · momentum -0.23 · ⚠️ oversold |
| ADD | **AMAT**<br><small>Applied Materials</small> | 20 | 386.98 USD | $7,740 | Executed (paper) | analyst α +0.15 · momentum +0.12 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.84 | **MU**<br><small>Micron Technology</small> | 792.95 USD | +92% | +8.4% | +280% | +4% | 44 | +0.12 | 10.6% → 10.0% | – | momentum +0.53 · analyst α +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.10 | **Samsung**<br><small>005930.KS</small> | 208,000 KRW | +130% | +18.7% | +121% | -12% | 43 | -0.26 | 10.1% → 10.0% | – | analyst α +0.85 · momentum +0.17 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.32 | **MRVL**<br><small>Marvell Technology</small> | 165.89 USD | +77% | +4.8% | +175% | -11% | 38 | -0.12 | 4.8% → 4.9% | – | momentum +0.35 · analyst α +0.27 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.31 | **SK hynix**<br><small>000660.KS</small> | 1,255,000 KRW | – | +0.0% | +155% | -17% | 42 | +0.62 | 9.6% → 4.5% | TRIM 46 | quality +0.33 · momentum +0.26 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.86 | **NVDA**<br><small>NVIDIA</small> | 164.84 USD | +99% | +10.2% | +15% | -19% | 26 | +0.47 | 4.9% → 4.9% | ADD 79 | analyst α +0.48 · momentum -0.23 · ⚠️ oversold |
| 🟢🟢 Strong Buy | +0.76 | **Advantest**<br><small>6857.T</small> | 29,825 JPY | +43% | -3.6% | +124% | +2% | 41 | +0.33 | 2.2% → 2.9% | – | momentum +0.20 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.67 | **ASX**<br><small>ASE Technology</small> | 36.44 USD | +40% | -1.9% | +199% | +7% | 45 | -0.68 | 3.6% → 3.6% | – | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.57 | **AMAT**<br><small>Applied Materials</small> | 386.98 USD | +65% | +2.4% | +96% | -13% | 46 | +0.03 | 2.7% → 2.8% | ADD 20 | analyst α +0.15 · momentum +0.12 |
| 🟢 Buy | +0.44 | **INTC**<br><small>Intel</small> | 61.79 USD | +88% | +7.6% | +159% | -29% | 34 | -0.62 | 1.1% → 1.4% | – | analyst α +0.36 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| ⚪ Hold | +0.11 | **Infineon**<br><small>IFX.DE</small> | 52.29 EUR | +66% | +2.1% | +55% | -9% | 50 | -0.04 | 1.5% → 1.5% | – | analyst α +0.12 · momentum -0.05 |
| ⚪ Hold | +0.09 | **TSM**<br><small>TSMC</small> | 407.35 USD | +36% | -4.6% | +49% | +1% | 48 | +0.58 | 6.0% → 6.0% | – | quality +0.28 · analyst α -0.23 |
| ⚪ Hold | +0.09 | **KLAC**<br><small>KLA Corp</small> | 158.85 USD | +47% | -1.9% | +51% | -13% | 48 | +0.51 | 4.9% → 4.9% | – | quality +0.24 · analyst α -0.08 |
| ⚪ Hold | +0.06 | **ASML**<br><small>ASML Holding</small> | 1,509.98 USD | +39% | -4.3% | +62% | -6% | 43 | +0.42 | 0.0% → 0.0% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.02 | **Tokyo Electron**<br><small>8035.T</small> | 9,316 JPY | +64% | +2.0% | +87% | -10% | 44 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.10 |
| ⚪ Hold | -0.02 | **LRCX**<br><small>Lam Research</small> | 233.31 USD | +61% | +1.1% | +81% | -18% | 44 | +0.02 | 1.6% → 1.6% | – | trend -0.10 · momentum +0.05 |
| ⚪ Hold | -0.07 | **TER**<br><small>Teradyne</small> | 265.12 USD | +68% | +3.0% | +103% | -24% | 41 | -0.31 | 1.1% → 1.1% | – | quality -0.21 · analyst α +0.19 |
| ⚪ Hold | -0.18 | **ASMI**<br><small>ASM.AS</small> | 726.80 EUR | +55% | -0.4% | +65% | -10% | 47 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · analyst α -0.02 |
| ⚪ Hold | -0.19 | **GFS**<br><small>GlobalFoundries</small> | 42.93 USD | +77% | +5.2% | +41% | -22% | 48 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.14 |
| 🔴 Sell | -0.49 | **Disco**<br><small>6146.T</small> | 47,480 JPY | +72% | +4.3% | +10% | -27% | 44 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.23 |
| 🔴 Sell | -0.56 | **ENTG**<br><small>Entegris</small> | 152.95 USD | +13% | -10.4% | +83% | +10% | 54 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.21 |
| 🔴 Sell | -0.58 | **AMKR**<br><small>Amkor Technology</small> | 37.21 USD | +105% | +12.0% | +32% | -34% | 44 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴 Sell | -0.72 | **TXN**<br><small>Texas Instruments</small> | 312.40 USD | +4% | -12.3% | +79% | +19% | 61 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.25 |
| 🔴🔴 Strong Sell | -0.80 | **QCOM**<br><small>Qualcomm</small> | 177.65 USD | +9% | -11.2% | +1% | +5% | 53 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.87 | **SNPS**<br><small>Synopsys</small> | 461.75 USD | +23% | -7.7% | +21% | +5% | 51 | +0.14 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.20 |
| 🔴🔴 Strong Sell | -0.88 | **ARM**<br><small>Arm Holdings</small> | 200.60 USD | +44% | -4.9% | +59% | -14% | 44 | +0.04 | 0.0% → 0.0% | – | analyst α -0.27 · trend -0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.90 | **AVGO**<br><small>Broadcom</small> | 364.93 USD | +46% | -2.2% | -1% | -0% | 60 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.12 |
| 🔴🔴 Strong Sell | -1.02 | **AMD**<br><small>Advanced Micro Devices</small> | 579.24 USD | +7% | -13.0% | +140% | +37% | 57 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.23 | **SMIC**<br><small>0981.HK</small> | 48.74 HKD | +97% | +11.4% | -23% | -27% | 46 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.28 | **CDNS**<br><small>Cadence Design Systems</small> | 330.85 USD | +23% | -7.9% | +3% | +1% | 51 | +0.31 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.43 | **Shin-Etsu**<br><small>4063.T</small> | 5,819 JPY | +33% | -4.9% | +32% | -8% | 50 | -0.20 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.17 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.84"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 792.95 USD (+92%, 46 analysts); de-biased α +8.4% vs CAPM hurdle 14.0%. Uptrend +4% vs 200-day avg; 12-1 mom +280%; RSI 44. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.10"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 208,000 KRW (+130%, 36 analysts); de-biased α +18.7% vs CAPM hurdle 11.3%. Downtrend -12% vs 200-day avg; 12-1 mom +121%; RSI 43. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.32"
    Within rebalance band of target 4.9%: no trade. Analyst target 293.88 USD vs 165.89 USD (+77%, 43 analysts); de-biased α +4.8% vs CAPM hurdle 14.1%. Downtrend -11% vs 200-day avg; 12-1 mom +175%; RSI 38. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.31"
    **TRIM 46 sh** → target 4.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -17% vs 200-day avg; 12-1 mom +155%; RSI 42. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +0.86"
    **ADD 79 sh** → target 4.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 164.84 USD (+99%, 59 analysts); de-biased α +10.2% vs CAPM hurdle 13.9%. Downtrend -19% vs 200-day avg; 12-1 mom +15%; RSI 26. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "Advantest (6857.T) — 🟢🟢 Strong Buy, score +0.76"
    Within rebalance band of target 2.9%: no trade. Analyst target 42,686 JPY vs 29,825 JPY (+43%, 21 analysts); de-biased α -3.6% vs CAPM hurdle 13.4%. Uptrend +2% vs 200-day avg; 12-1 mom +124%; RSI 41. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "ASX (ASX) — 🟢 Buy, score +0.67"
    Within rebalance band of target 3.6%: no trade. Analyst target 51.00 USD vs 36.44 USD (+40%, 1 analysts); de-biased α -1.9% vs CAPM hurdle 11.9%. Uptrend +7% vs 200-day avg; 12-1 mom +199%; RSI 45. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.57"
    **ADD 20 sh** → target 2.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 386.98 USD (+65%, 36 analysts); de-biased α +2.4% vs CAPM hurdle 11.6%. Downtrend -13% vs 200-day avg; 12-1 mom +96%; RSI 46. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.44"
    Within rebalance band of target 1.4%: no trade. Analyst target 116.37 USD vs 61.79 USD (+88%, 43 analysts); de-biased α +7.6% vs CAPM hurdle 14.0%. Downtrend -29% vs 200-day avg; 12-1 mom +159%; RSI 34. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.11"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 52.29 EUR (+66%, 23 analysts); de-biased α +2.1% vs CAPM hurdle 14.1%. Downtrend -9% vs 200-day avg; 12-1 mom +55%; RSI 50. Quality z -0.04 (ROE 6%).

??? note "TSM (TSM) — ⚪ Hold, score +0.09"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 407.35 USD (+36%, 20 analysts); de-biased α -4.6% vs CAPM hurdle 10.8%. Uptrend +1% vs 200-day avg; 12-1 mom +49%; RSI 48. Quality z +0.58 (ROE 35%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.09"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 158.85 USD (+47%, 26 analysts); de-biased α -1.9% vs CAPM hurdle 11.1%. Downtrend -13% vs 200-day avg; 12-1 mom +51%; RSI 48. Quality z +0.51 (ROE 87%).

??? note "ASML (ASML) — ⚪ Hold, score +0.06"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,509.98 USD (+39%, 16 analysts); de-biased α -4.3% vs CAPM hurdle 12.3%. Downtrend -6% vs 200-day avg; 12-1 mom +62%; RSI 43. Quality z +0.42 (ROE 50%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.02"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 9,316 JPY (+64%, 23 analysts); de-biased α +2.0% vs CAPM hurdle 12.8%. Downtrend -10% vs 200-day avg; 12-1 mom +87%; RSI 44. Quality z -0.28 (ROE 29%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.02"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 233.31 USD (+61%, 31 analysts); de-biased α +1.1% vs CAPM hurdle 12.6%. Downtrend -18% vs 200-day avg; 12-1 mom +81%; RSI 44. Quality z +0.02 (ROE 65%).

??? note "TER (TER) — ⚪ Hold, score -0.07"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 265.12 USD (+68%, 15 analysts); de-biased α +3.0% vs CAPM hurdle 12.3%. Downtrend -24% vs 200-day avg; 12-1 mom +103%; RSI 41. Quality z -0.31 (ROE 20%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 726.80 EUR (+55%, 19 analysts); de-biased α -0.4% vs CAPM hurdle 13.2%. Downtrend -10% vs 200-day avg; 12-1 mom +65%; RSI 47. Quality z -0.10 (ROE 19%).

??? note "GFS (GFS) — ⚪ Hold, score -0.19"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 42.93 USD (+77%, 22 analysts); de-biased α +5.2% vs CAPM hurdle 12.4%. Downtrend -22% vs 200-day avg; 12-1 mom +41%; RSI 48. Quality z -0.21 (ROE 8%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 81,730 JPY vs 47,480 JPY (+72%, 20 analysts); de-biased α +4.3% vs CAPM hurdle 11.5%. Downtrend -27% vs 200-day avg; 12-1 mom +10%; RSI 44. Quality z +0.06 (ROE 25%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.56"
    Avoid: not owned. Analyst target 173.36 USD vs 152.95 USD (+13%, 11 analysts); de-biased α -10.4% vs CAPM hurdle 11.0%. Uptrend +10% vs 200-day avg; 12-1 mom +83%; RSI 54. Quality z -0.02 (ROE 6%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 76.40 USD vs 37.21 USD (+105%, 10 analysts); de-biased α +12.0% vs CAPM hurdle 14.0%. Downtrend -34% vs 200-day avg; 12-1 mom +32%; RSI 44. Quality z -1.00 (ROE 9%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.72"
    Avoid: not owned. Analyst target 324.71 USD vs 312.40 USD (+4%, 31 analysts); de-biased α -12.3% vs CAPM hurdle 10.8%. Uptrend +19% vs 200-day avg; 12-1 mom +79%; RSI 61. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.80"
    Avoid: not owned. Analyst target 194.13 USD vs 177.65 USD (+9%, 30 analysts); de-biased α -11.2% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +1%; RSI 53. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.87"
    Avoid: not owned. Analyst target 569.78 USD vs 461.75 USD (+23%, 26 analysts); de-biased α -7.7% vs CAPM hurdle 10.3%. Uptrend +5% vs 200-day avg; 12-1 mom +21%; RSI 51. Quality z +0.14 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.88"
    Avoid: not owned. Analyst target 288.70 USD vs 200.60 USD (+44%, 40 analysts); de-biased α -4.9% vs CAPM hurdle 19.6%. Downtrend -14% vs 200-day avg; 12-1 mom +59%; RSI 44. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.90"
    Avoid: not owned. Analyst target 531.31 USD vs 364.93 USD (+46%, 47 analysts); de-biased α -2.2% vs CAPM hurdle 11.2%. Downtrend -0% vs 200-day avg; 12-1 mom -1%; RSI 60. Quality z +0.26 (ROE 31%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.02"
    Avoid: not owned. Analyst target 619.51 USD vs 579.24 USD (+7%, 50 analysts); de-biased α -13.0% vs CAPM hurdle 14.9%. Uptrend +37% vs 200-day avg; 12-1 mom +140%; RSI 57. Quality z -0.15 (ROE 7%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.23"
    Avoid: not owned. Analyst target 95.99 HKD vs 48.74 HKD (+97%, 21 analysts); de-biased α +11.4% vs CAPM hurdle 7.3%. Downtrend -27% vs 200-day avg; 12-1 mom -23%; RSI 46. Quality z -0.99 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.28"
    Avoid: not owned. Analyst target 405.47 USD vs 330.85 USD (+23%, 26 analysts); de-biased α -7.9% vs CAPM hurdle 10.0%. Uptrend +1% vs 200-day avg; 12-1 mom +3%; RSI 51. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.43"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,819 JPY (+33%, 17 analysts); de-biased α -4.9% vs CAPM hurdle 10.8%. Downtrend -8% vs 200-day avg; 12-1 mom +32%; RSI 50. Quality z -0.20 (ROE 10%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 792.95 USD | $91,982 | 10.6% | Strong Buy |
| 005930.KS | Samsung Electronics | 562 | 208,000 KRW | $87,528 | 10.1% | Strong Buy |
| 000660.KS | SK hynix | 88 | 1,255,000 KRW | $82,694 | 9.6% | Strong Buy |
| TSM | TSMC | 127 | 407.35 USD | $51,733 | 6.0% | Hold |
| KLAC | KLA Corp | 268 | 158.85 USD | $42,572 | 4.9% | Hold |
| NVDA | NVIDIA | 258 | 164.84 USD | $42,528 | 4.9% | Strong Buy |
| MRVL | Marvell Technology | 248 | 165.89 USD | $41,141 | 4.8% | Strong Buy |
| ASX | ASE Technology | 864 | 36.44 USD | $31,484 | 3.6% | Buy |
| AMAT | Applied Materials | 61 | 386.98 USD | $23,606 | 2.7% | Buy |
| 6857.T | Advantest | 100 | 29,825 JPY | $18,660 | 2.2% | Strong Buy |
| LRCX | Lam Research | 58 | 233.31 USD | $13,532 | 1.6% | Hold |
| IFX.DE | Infineon Technologies | 225 | 52.29 EUR | $13,003 | 1.5% | Hold |
| INTC | Intel | 152 | 61.79 USD | $9,393 | 1.1% | Buy |
| TER | Teradyne | 35 | 265.12 USD | $9,279 | 1.1% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-11-03 15:09 UTC | ADD | INTC | 106 | 62.03 | $6,576 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 44.1%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
