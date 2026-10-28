---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-28 16:04 UTC (Wed Oct 28, 12:04 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Wed 12:04) · Tokyo 🔴 closed (Thu 01:04) · Korea 🔴 closed (Thu 01:04) · Hong Kong 🔴 closed (Thu 00:04) · Xetra 🟢 open (Wed 17:04) · Euronext Amsterdam 🟢 open (Wed 17:04)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$941,169** | $101,412 (11%) | $839,757 (89%) | -5.88% | -8.62% | 🟢 Risk-on (+8.9%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $941,169), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **NVDA**<br><small>NVIDIA</small> | 117 | 217.19 USD | $25,411 | Executed (paper) | quality +0.21 · momentum -0.17 |
| ADD | **Tokyo Electron**<br><small>8035.T</small> | 100 | 9,813 JPY | $6,202 | Queued · Tokyo closed | analyst α +0.27 · quality -0.18 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.46 | **SK hynix**<br><small>000660.KS</small> | 1,481,000 KRW | +112% | +16.7% | +313% | -0% | 49 | +0.62 | 11.5% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.03 | **MU**<br><small>Micron Technology</small> | 972.42 USD | +56% | +2.8% | +384% | +31% | 52 | +0.12 | 9.5% → 10.0% | – | momentum +0.53 · trend +0.18 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.43 | **Samsung**<br><small>005930.KS</small> | 240,500 KRW | +99% | +14.1% | +195% | +2% | 51 | -0.26 | 9.2% → 10.0% | – | analyst α +0.55 · momentum +0.26 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.61 | **AMAT**<br><small>Applied Materials</small> | 412.88 USD | +55% | +3.1% | +123% | -7% | 41 | +0.03 | 6.4% → 7.8% | – | analyst α +0.23 · momentum +0.14 |
| 🟢 Buy | +0.58 | **Infineon**<br><small>IFX.DE</small> | 53.33 EUR | +63% | +4.5% | +74% | -6% | 46 | -0.04 | 8.2% → 8.6% | – | analyst α +0.36 · trend -0.09 |
| 🟢 Buy | +0.44 | **NVDA**<br><small>NVIDIA</small> | 217.19 USD | +51% | +1.5% | +19% | +7% | 46 | +0.47 | 6.6% → 6.6% | ADD 117 | quality +0.21 · momentum -0.17 |
| 🟢 Buy | +0.42 | **ASX**<br><small>ASE Technology</small> | 43.40 USD | +17% | -3.1% | +246% | +32% | 53 | -0.68 | 6.1% → 5.9% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.35 | **Advantest**<br><small>6857.T</small> | 35,020 JPY | +22% | -5.6% | +99% | +22% | 50 | +0.33 | 4.7% → 3.4% | – | analyst α -0.23 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.34 | **Tokyo Electron**<br><small>8035.T</small> | 9,813 JPY | +56% | +3.2% | +100% | -2% | 41 | -0.28 | 3.3% → 4.3% | ADD 100 | analyst α +0.27 · quality -0.18 |
| 🟢 Buy | +0.31 | **TSM**<br><small>TSMC</small> | 439.01 USD | +26% | -3.9% | +55% | +10% | 52 | +0.58 | 5.9% → 5.5% | – | quality +0.28 · momentum -0.12 |
| ⚪ Hold | +0.22 | **ASML**<br><small>ASML Holding</small> | 1,661.92 USD | +26% | -4.2% | +74% | +5% | 47 | +0.42 | 5.3% → 5.3% | – | quality +0.18 · analyst α -0.15 |
| ⚪ Hold | +0.20 | **KLAC**<br><small>KLA Corp</small> | 158.93 USD | +47% | +1.3% | +63% | -12% | 38 | +0.51 | 4.5% → 4.5% | – | quality +0.24 · trend -0.16 |
| ⚪ Hold | +0.12 | **MRVL**<br><small>Marvell Technology</small> | 250.25 USD | +17% | -7.0% | +197% | +38% | 52 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.30 · ⚠️ rich valuation |
| ⚪ Hold | +0.10 | **LRCX**<br><small>Lam Research</small> | 253.50 USD | +48% | +1.1% | +107% | -11% | 38 | +0.02 | 4.4% → 4.4% | – | momentum +0.12 · trend -0.12 |
| ⚪ Hold | -0.09 | **GFS**<br><small>GlobalFoundries</small> | 45.69 USD | +66% | +5.7% | +36% | -17% | 46 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.18 |
| ⚪ Hold | -0.14 | **AVGO**<br><small>Broadcom</small> | 346.36 USD | +53% | +2.9% | -1% | -6% | 50 | +0.26 | 3.7% → 3.7% | – | momentum -0.30 · analyst α +0.19 |
| ⚪ Hold | -0.17 | **Disco**<br><small>6146.T</small> | 52,540 JPY | +56% | +3.4% | +6% | -20% | 45 | +0.06 | 0.0% → 0.0% | – | analyst α +0.31 · momentum -0.23 |
| 🔴 Sell | -0.26 | **INTC**<br><small>Intel</small> | 93.88 USD | +24% | -5.3% | +193% | +8% | 43 | -0.62 | 0.0% → 0.0% | – | quality -0.24 · momentum +0.23 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.36 | **TER**<br><small>Teradyne</small> | 308.83 USD | +45% | +0.3% | +174% | -11% | 35 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.40 | **ASMI**<br><small>ASM.AS</small> | 773.40 EUR | +46% | +0.4% | +58% | -5% | 46 | -0.10 | 0.0% → 0.0% | – | momentum -0.10 · quality -0.06 |
| 🔴 Sell | -0.55 | **AMKR**<br><small>Amkor Technology</small> | 40.98 USD | +86% | +10.5% | +64% | -28% | 39 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.69 | **TXN**<br><small>Texas Instruments</small> | 306.83 USD | +6% | -8.6% | +71% | +19% | 68 | +0.24 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.14 |
| 🔴🔴 Strong Sell | -0.79 | **ARM**<br><small>Arm Holdings</small> | 232.79 USD | +24% | -6.7% | +64% | +2% | 43 | +0.04 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.03 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.87 | **ENTG**<br><small>Entegris</small> | 154.62 USD | +12% | -7.5% | +65% | +12% | 54 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.12 |
| 🔴🔴 Strong Sell | -0.88 | **SMIC**<br><small>0981.HK</small> | 47.80 HKD | +101% | +15.6% | -8% | -30% | 29 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.41 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -0.92 | **Shin-Etsu**<br><small>4063.T</small> | 6,000 JPY | +29% | -2.7% | +17% | -5% | 53 | -0.20 | 0.0% → 0.0% | – | momentum -0.20 · quality -0.11 |
| 🔴🔴 Strong Sell | -0.92 | **QCOM**<br><small>Qualcomm</small> | 181.74 USD | +7% | -8.6% | +0% | +8% | 53 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.01 | **AMD**<br><small>Advanced Micro Devices</small> | 567.61 USD | +9% | -9.2% | +134% | +39% | 51 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.08 | **CDNS**<br><small>Cadence Design Systems</small> | 342.68 USD | +18% | -5.7% | -8% | +5% | 58 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.31 |
| 🔴🔴 Strong Sell | -1.47 | **SNPS**<br><small>Synopsys</small> | 479.10 USD | +19% | -5.7% | -11% | +8% | 58 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · analyst α -0.27 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.46"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,481,000 KRW (+112%, 38 analysts); de-biased α +16.7% vs CAPM hurdle 14.3%. Downtrend -0% vs 200-day avg; 12-1 mom +313%; RSI 49. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.03"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 972.42 USD (+56%, 46 analysts); de-biased α +2.8% vs CAPM hurdle 14.0%. Uptrend +31% vs 200-day avg; 12-1 mom +384%; RSI 52. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.43"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 240,500 KRW (+99%, 36 analysts); de-biased α +14.1% vs CAPM hurdle 11.3%. Uptrend +2% vs 200-day avg; 12-1 mom +195%; RSI 51. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.61"
    Within rebalance band of target 7.8%: no trade. Analyst target 638.94 USD vs 412.88 USD (+55%, 36 analysts); de-biased α +3.1% vs CAPM hurdle 11.6%. Downtrend -7% vs 200-day avg; 12-1 mom +123%; RSI 41. Quality z +0.03 (ROE 36%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.58"
    Within rebalance band of target 8.6%: no trade. Analyst target 86.74 EUR vs 53.33 EUR (+63%, 23 analysts); de-biased α +4.5% vs CAPM hurdle 14.1%. Downtrend -6% vs 200-day avg; 12-1 mom +74%; RSI 46. Quality z -0.04 (ROE 6%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.44"
    **ADD 117 sh** → target 6.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 217.19 USD (+51%, 59 analysts); de-biased α +1.5% vs CAPM hurdle 13.9%. Uptrend +7% vs 200-day avg; 12-1 mom +19%; RSI 46. Quality z +0.47 (ROE 101%).

??? success "ASX (ASX) — 🟢 Buy, score +0.42"
    Within rebalance band of target 5.9%: no trade. Analyst target 51.00 USD vs 43.40 USD (+17%, 1 analysts); de-biased α -3.1% vs CAPM hurdle 11.9%. Uptrend +32% vs 200-day avg; 12-1 mom +246%; RSI 53. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.35"
    Within rebalance band of target 3.4%: no trade. Analyst target 42,686 JPY vs 35,020 JPY (+22%, 21 analysts); de-biased α -5.6% vs CAPM hurdle 13.4%. Uptrend +22% vs 200-day avg; 12-1 mom +99%; RSI 50. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.34"
    **ADD 100 sh** → target 4.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 15,275 JPY vs 9,813 JPY (+56%, 23 analysts); de-biased α +3.2% vs CAPM hurdle 12.8%. Downtrend -2% vs 200-day avg; 12-1 mom +100%; RSI 41. Quality z -0.28 (ROE 29%).

??? success "TSM (TSM) — 🟢 Buy, score +0.31"
    Within rebalance band of target 5.5%: no trade. Analyst target 552.26 USD vs 439.01 USD (+26%, 20 analysts); de-biased α -3.9% vs CAPM hurdle 10.8%. Uptrend +10% vs 200-day avg; 12-1 mom +55%; RSI 52. Quality z +0.58 (ROE 35%).

??? note "ASML (ASML) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,661.92 USD (+26%, 16 analysts); de-biased α -4.2% vs CAPM hurdle 12.3%. Uptrend +5% vs 200-day avg; 12-1 mom +74%; RSI 47. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.20"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 158.93 USD (+47%, 26 analysts); de-biased α +1.3% vs CAPM hurdle 11.1%. Downtrend -12% vs 200-day avg; 12-1 mom +63%; RSI 38. Quality z +0.51 (ROE 87%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.12"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 250.25 USD (+17%, 43 analysts); de-biased α -7.0% vs CAPM hurdle 14.1%. Uptrend +38% vs 200-day avg; 12-1 mom +197%; RSI 52. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.10"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 253.50 USD (+48%, 31 analysts); de-biased α +1.1% vs CAPM hurdle 12.6%. Downtrend -11% vs 200-day avg; 12-1 mom +107%; RSI 38. Quality z +0.02 (ROE 65%).

??? note "GFS (GFS) — ⚪ Hold, score -0.09"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 45.69 USD (+66%, 22 analysts); de-biased α +5.7% vs CAPM hurdle 12.4%. Downtrend -17% vs 200-day avg; 12-1 mom +36%; RSI 46. Quality z -0.21 (ROE 8%).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.14"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 346.36 USD (+53%, 47 analysts); de-biased α +2.9% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom -1%; RSI 50. Quality z +0.26 (ROE 31%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.17"
    Hold zone: not owned, no entry. Analyst target 81,730 JPY vs 52,540 JPY (+56%, 20 analysts); de-biased α +3.4% vs CAPM hurdle 11.5%. Downtrend -20% vs 200-day avg; 12-1 mom +6%; RSI 45. Quality z +0.06 (ROE 25%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.26"
    Avoid: not owned. Analyst target 116.37 USD vs 93.88 USD (+24%, 43 analysts); de-biased α -5.3% vs CAPM hurdle 14.0%. Uptrend +8% vs 200-day avg; 12-1 mom +193%; RSI 43. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "TER (TER) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 446.47 USD vs 308.83 USD (+45%, 15 analysts); de-biased α +0.3% vs CAPM hurdle 12.3%. Downtrend -11% vs 200-day avg; 12-1 mom +174%; RSI 35. Quality z -0.31 (ROE 20%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.40"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 773.40 EUR (+46%, 19 analysts); de-biased α +0.4% vs CAPM hurdle 13.2%. Downtrend -5% vs 200-day avg; 12-1 mom +58%; RSI 46. Quality z -0.10 (ROE 19%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 76.40 USD vs 40.98 USD (+86%, 10 analysts); de-biased α +10.5% vs CAPM hurdle 14.0%. Downtrend -28% vs 200-day avg; 12-1 mom +64%; RSI 39. Quality z -1.00 (ROE 9%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.69"
    Avoid: not owned. Analyst target 324.71 USD vs 306.83 USD (+6%, 31 analysts); de-biased α -8.6% vs CAPM hurdle 10.8%. Uptrend +19% vs 200-day avg; 12-1 mom +71%; RSI 68. Quality z +0.24 (ROE 30%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.79"
    Avoid: not owned. Analyst target 288.70 USD vs 232.79 USD (+24%, 40 analysts); de-biased α -6.7% vs CAPM hurdle 19.6%. Uptrend +2% vs 200-day avg; 12-1 mom +64%; RSI 43. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.87"
    Avoid: not owned. Analyst target 173.36 USD vs 154.62 USD (+12%, 11 analysts); de-biased α -7.5% vs CAPM hurdle 11.0%. Uptrend +12% vs 200-day avg; 12-1 mom +65%; RSI 54. Quality z -0.02 (ROE 6%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.88"
    Avoid: not owned. Analyst target 95.99 HKD vs 47.80 HKD (+101%, 21 analysts); de-biased α +15.6% vs CAPM hurdle 7.3%. Downtrend -30% vs 200-day avg; 12-1 mom -8%; RSI 29. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,000 JPY (+29%, 17 analysts); de-biased α -2.7% vs CAPM hurdle 10.8%. Downtrend -5% vs 200-day avg; 12-1 mom +17%; RSI 53. Quality z -0.20 (ROE 10%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 194.13 USD vs 181.74 USD (+7%, 30 analysts); de-biased α -8.6% vs CAPM hurdle 11.9%. Uptrend +8% vs 200-day avg; 12-1 mom +0%; RSI 53. Quality z +0.70 (ROE 23%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 619.51 USD vs 567.61 USD (+9%, 50 analysts); de-biased α -9.2% vs CAPM hurdle 14.9%. Uptrend +39% vs 200-day avg; 12-1 mom +134%; RSI 51. Quality z -0.15 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.08"
    Avoid: not owned. Analyst target 405.47 USD vs 342.68 USD (+18%, 26 analysts); de-biased α -5.7% vs CAPM hurdle 10.0%. Uptrend +5% vs 200-day avg; 12-1 mom -8%; RSI 58. Quality z +0.31 (ROE 22%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.47"
    Avoid: not owned. Analyst target 569.78 USD vs 479.10 USD (+19%, 26 analysts); de-biased α -5.7% vs CAPM hurdle 10.3%. Uptrend +8% vs 200-day avg; 12-1 mom -11%; RSI 58. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,481,000 KRW | $107,967 | 11.5% | Strong Buy |
| MU | Micron Technology | 92 | 972.42 USD | $89,463 | 9.5% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 240,500 KRW | $86,769 | 9.2% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 53.33 EUR | $77,315 | 8.2% | Buy |
| NVDA | NVIDIA | 285 | 217.19 USD | $61,899 | 6.6% | Buy |
| AMAT | Applied Materials | 145 | 412.88 USD | $59,867 | 6.4% | Buy |
| ASX | ASE Technology | 1,320 | 43.40 USD | $57,295 | 6.1% | Buy |
| TSM | TSMC | 127 | 439.01 USD | $55,754 | 5.9% | Buy |
| ASML | ASML Holding | 30 | 1,661.92 USD | $49,858 | 5.3% | Hold |
| 6857.T | Advantest | 200 | 35,020 JPY | $44,265 | 4.7% | Buy |
| KLAC | KLA Corp | 268 | 158.93 USD | $42,593 | 4.5% | Hold |
| LRCX | Lam Research | 162 | 253.50 USD | $41,067 | 4.4% | Hold |
| AVGO | Broadcom | 100 | 346.36 USD | $34,636 | 3.7% | Hold |
| 8035.T | Tokyo Electron | 500 | 9,813 JPY | $31,009 | 3.3% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-28 16:04 UTC | ADD | NVDA | 117 | 217.19 | $25,411 |
| 2026-10-26 19:22 UTC | TRIM | AMAT | -57 | 391.16 | $22,296 |
| 2026-10-26 19:22 UTC | TRIM | NVDA | -58 | 216.65 | $12,566 |
| 2026-10-26 19:22 UTC | TRIM | ASX | -395 | 40.15 | $15,859 |
| 2026-10-26 06:15 UTC | ADD | 6857.T | 100 | 31,220.00 | $19,871 |
| 2026-10-23 19:14 UTC | ADD | KLAC | 57 | 145.31 | $8,282 |
| 2026-10-23 15:05 UTC | ADD | ASX | 383 | 38.70 | $14,822 |
| 2026-10-23 15:05 UTC | TRIM | NVDA | -68 | 212.70 | $14,464 |
| 2026-10-22 15:18 UTC | ADD | LRCX | 57 | 234.49 | $13,366 |
| 2026-10-22 15:18 UTC | ADD | AMAT | 46 | 380.67 | $17,511 |
| 2026-10-22 15:18 UTC | TRIM | TSM | -27 | 414.23 | $11,184 |
| 2026-10-21 19:21 UTC | ADD | TSM | 37 | 430.88 | $15,943 |
| 2026-10-21 15:16 UTC | TRIM | KLAC | -68 | 164.22 | $11,167 |
| 2026-10-20 17:08 UTC | BUY (new) | LRCX | 105 | 263.68 | $27,686 |
| 2026-10-20 17:08 UTC | TRIM | AVGO | -34 | 334.29 | $11,366 |
| 2026-10-20 17:08 UTC | TRIM | NVDA | -77 | 216.83 | $16,696 |
| 2026-10-19 15:37 UTC | TRIM | TSM | -25 | 426.75 | $10,669 |
| 2026-10-19 15:37 UTC | TRIM | ASX | -465 | 41.40 | $19,251 |
| 2026-10-19 01:19 UTC | TRIM | 8035.T | -100 | 10,325.00 | $6,537 |
| 2026-10-16 17:25 UTC | ADD | ASX | 558 | 39.86 | $22,242 |
| 2026-10-16 17:25 UTC | TRIM | TSM | -45 | 412.93 | $18,582 |
| 2026-10-16 12:26 UTC | TRIM | IFX.DE | -293 | 52.84 | $17,423 |
| 2026-10-15 15:02 UTC | ADD | ASX | 339 | 41.52 | $14,077 |
| 2026-10-15 15:02 UTC | TRIM | KLAC | -93 | 172.43 | $16,036 |
| 2026-10-15 04:41 UTC | BUY (new) | 6857.T | 100 | 34,860.00 | $22,075 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 31.2%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
