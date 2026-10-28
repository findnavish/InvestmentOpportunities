---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-28 08:34 UTC (Wed Oct 28, 04:34 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Wed 04:34) · Tokyo 🔴 closed (Wed 17:34) · Korea 🔴 closed (Wed 17:34) · Hong Kong 🔴 closed (Wed 16:34) · Xetra 🟢 open (Wed 09:34) · Euronext Amsterdam 🟢 open (Wed 09:34)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$927,921** | $126,836 (14%) | $801,086 (86%) | -7.21% | -9.61% | 🟢 Risk-on (+8.0%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $927,921), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **AMAT**<br><small>Applied Materials</small> | 73 | 395.95 USD | $28,904 | Queued · NYSE/Nasdaq closed | analyst α +0.31 · momentum +0.14 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.38 | **SK hynix**<br><small>000660.KS</small> | 1,481,000 KRW | +112% | +16.3% | +313% | -0% | 49 | +0.62 | 11.7% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.22 | **MU**<br><small>Micron Technology</small> | 929.16 USD | +64% | +4.2% | +384% | +25% | 46 | +0.12 | 9.2% → 10.0% | – | momentum +0.53 · analyst α +0.27 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.41 | **Samsung**<br><small>005930.KS</small> | 240,500 KRW | +99% | +13.8% | +195% | +2% | 51 | -0.26 | 9.4% → 10.0% | – | analyst α +0.55 · momentum +0.26 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.74 | **AMAT**<br><small>Applied Materials</small> | 395.95 USD | +61% | +4.4% | +123% | -11% | 34 | +0.03 | 6.2% → 9.3% | ADD 73 | analyst α +0.31 · momentum +0.14 |
| 🟢 Buy | +0.60 | **Infineon**<br><small>IFX.DE</small> | 52.55 EUR | +65% | +4.7% | +66% | -8% | 44 | -0.04 | 8.2% → 8.8% | – | analyst α +0.41 · trend -0.10 |
| 🟢 Buy | +0.48 | **ASX**<br><small>ASE Technology</small> | 42.09 USD | +21% | -2.8% | +246% | +28% | 50 | -0.68 | 6.0% → 6.7% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.31 | **NVDA**<br><small>NVIDIA</small> | 217.88 USD | +50% | +1.0% | +19% | +7% | 46 | +0.47 | 3.9% → 4.6% | – | quality +0.21 · momentum -0.17 |
| 🟢 Buy | +0.31 | **TSM**<br><small>TSMC</small> | 436.88 USD | +26% | -4.1% | +55% | +10% | 51 | +0.58 | 6.0% → 5.5% | – | quality +0.28 · analyst α -0.15 |
| 🟢 Buy | +0.28 | **ASML**<br><small>ASML Holding</small> | 1,635.80 USD | +28% | -4.1% | +74% | +3% | 44 | +0.42 | 5.3% → 4.7% | – | quality +0.18 · analyst α -0.12 |
| ⚪ Hold | +0.25 | **Advantest**<br><small>6857.T</small> | 35,020 JPY | +22% | -6.0% | +99% | +22% | 50 | +0.33 | 4.8% → 4.8% | – | analyst α -0.27 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.16 | **LRCX**<br><small>Lam Research</small> | 240.84 USD | +56% | +2.7% | +107% | -15% | 31 | +0.02 | 4.2% → 4.2% | – | trend -0.16 · momentum +0.12 |
| ⚪ Hold | +0.15 | **KLAC**<br><small>KLA Corp</small> | 153.65 USD | +52% | +2.2% | +63% | -15% | 33 | +0.51 | 4.4% → 4.4% | – | quality +0.24 · trend -0.18 |
| ⚪ Hold | +0.11 | **MRVL**<br><small>Marvell Technology</small> | 243.62 USD | +21% | -6.5% | +197% | +34% | 49 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.30 · ⚠️ rich valuation |
| ⚪ Hold | +0.08 | **Tokyo Electron**<br><small>8035.T</small> | 9,813 JPY | +56% | +2.8% | +100% | -2% | 41 | -0.28 | 3.4% → 3.4% | – | quality -0.18 · analyst α +0.15 |
| ⚪ Hold | -0.11 | **GFS**<br><small>GlobalFoundries</small> | 46.70 USD | +63% | +4.5% | +36% | -15% | 49 | -0.21 | 0.0% → 0.0% | – | analyst α +0.36 · momentum -0.14 |
| ⚪ Hold | -0.14 | **AVGO**<br><small>Broadcom</small> | 342.45 USD | +55% | +3.0% | -1% | -7% | 48 | +0.26 | 3.7% → 3.7% | – | momentum -0.30 · analyst α +0.19 |
| ⚪ Hold | -0.24 | **TER**<br><small>Teradyne</small> | 324.87 USD | +37% | -1.9% | +174% | -7% | 39 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.28 | **INTC**<br><small>Intel</small> | 93.73 USD | +24% | -5.6% | +193% | +8% | 43 | -0.62 | 0.0% → 0.0% | – | quality -0.24 · momentum +0.23 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.35 | **Disco**<br><small>6146.T</small> | 52,540 JPY | +56% | +3.0% | +6% | -20% | 45 | +0.06 | 0.0% → 0.0% | – | analyst α +0.23 · momentum -0.23 |
| 🔴 Sell | -0.47 | **ASMI**<br><small>ASM.AS</small> | 761.80 EUR | +48% | +0.6% | +50% | -6% | 43 | -0.10 | 0.0% → 0.0% | – | momentum -0.12 · quality -0.06 |
| 🔴 Sell | -0.57 | **AMD**<br><small>Advanced Micro Devices</small> | 560.45 USD | +11% | -9.3% | +134% | +38% | 50 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.62 | **TXN**<br><small>Texas Instruments</small> | 309.02 USD | +5% | -9.1% | +71% | +20% | 70 | +0.24 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.14 |
| 🔴 Sell | -0.68 | **AMKR**<br><small>Amkor Technology</small> | 39.96 USD | +91% | +11.3% | +64% | -30% | 37 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.70 | **SMIC**<br><small>0981.HK</small> | 47.80 HKD | +101% | +15.2% | -8% | -30% | 29 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.41 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -0.82 | **ARM**<br><small>Arm Holdings</small> | 226.55 USD | +27% | -6.2% | +64% | -1% | 40 | +0.04 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.03 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.91 | **ENTG**<br><small>Entegris</small> | 150.18 USD | +15% | -7.0% | +65% | +9% | 52 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.09 |
| 🔴🔴 Strong Sell | -0.94 | **Shin-Etsu**<br><small>4063.T</small> | 6,000 JPY | +29% | -3.1% | +17% | -5% | 53 | -0.20 | 0.0% → 0.0% | – | momentum -0.20 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.05 | **CDNS**<br><small>Cadence Design Systems</small> | 343.18 USD | +18% | -6.1% | -8% | +5% | 58 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.31 |
| 🔴🔴 Strong Sell | -1.25 | **QCOM**<br><small>Qualcomm</small> | 184.20 USD | +5% | -9.3% | +0% | +9% | 56 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.37 | **SNPS**<br><small>Synopsys</small> | 474.19 USD | +20% | -5.7% | -11% | +7% | 57 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · analyst α -0.23 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.38"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,481,000 KRW (+112%, 38 analysts); de-biased α +16.3% vs CAPM hurdle 14.3%. Downtrend -0% vs 200-day avg; 12-1 mom +313%; RSI 49. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.22"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 929.16 USD (+64%, 46 analysts); de-biased α +4.2% vs CAPM hurdle 14.0%. Uptrend +25% vs 200-day avg; 12-1 mom +384%; RSI 46. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.41"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 240,500 KRW (+99%, 36 analysts); de-biased α +13.8% vs CAPM hurdle 11.3%. Uptrend +2% vs 200-day avg; 12-1 mom +195%; RSI 51. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.74"
    **ADD 73 sh** → target 9.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 395.95 USD (+61%, 36 analysts); de-biased α +4.4% vs CAPM hurdle 11.6%. Downtrend -11% vs 200-day avg; 12-1 mom +123%; RSI 34. Quality z +0.03 (ROE 36%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.60"
    Within rebalance band of target 8.8%: no trade. Analyst target 86.74 EUR vs 52.55 EUR (+65%, 23 analysts); de-biased α +4.7% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +66%; RSI 44. Quality z -0.04 (ROE 6%).

??? success "ASX (ASX) — 🟢 Buy, score +0.48"
    Within rebalance band of target 6.7%: no trade. Analyst target 51.00 USD vs 42.09 USD (+21%, 1 analysts); de-biased α -2.8% vs CAPM hurdle 11.9%. Uptrend +28% vs 200-day avg; 12-1 mom +246%; RSI 50. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.31"
    Within rebalance band of target 4.6%: no trade. Analyst target 327.70 USD vs 217.88 USD (+50%, 59 analysts); de-biased α +1.0% vs CAPM hurdle 13.9%. Uptrend +7% vs 200-day avg; 12-1 mom +19%; RSI 46. Quality z +0.47 (ROE 101%).

??? success "TSM (TSM) — 🟢 Buy, score +0.31"
    Within rebalance band of target 5.5%: no trade. Analyst target 552.26 USD vs 436.88 USD (+26%, 20 analysts); de-biased α -4.1% vs CAPM hurdle 10.8%. Uptrend +10% vs 200-day avg; 12-1 mom +55%; RSI 51. Quality z +0.58 (ROE 35%).

??? success "ASML (ASML) — 🟢 Buy, score +0.28"
    Within rebalance band of target 4.7%: no trade. Analyst target 2,096.77 USD vs 1,635.80 USD (+28%, 16 analysts); de-biased α -4.1% vs CAPM hurdle 12.3%. Uptrend +3% vs 200-day avg; 12-1 mom +74%; RSI 44. Quality z +0.42 (ROE 50%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.25"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 35,020 JPY (+22%, 21 analysts); de-biased α -6.0% vs CAPM hurdle 13.4%. Uptrend +22% vs 200-day avg; 12-1 mom +99%; RSI 50. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.16"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 240.84 USD (+56%, 31 analysts); de-biased α +2.7% vs CAPM hurdle 12.6%. Downtrend -15% vs 200-day avg; 12-1 mom +107%; RSI 31. Quality z +0.02 (ROE 65%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 153.65 USD (+52%, 26 analysts); de-biased α +2.2% vs CAPM hurdle 11.1%. Downtrend -15% vs 200-day avg; 12-1 mom +63%; RSI 33. Quality z +0.51 (ROE 87%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.11"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 243.62 USD (+21%, 43 analysts); de-biased α -6.5% vs CAPM hurdle 14.1%. Uptrend +34% vs 200-day avg; 12-1 mom +197%; RSI 49. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 9,813 JPY (+56%, 23 analysts); de-biased α +2.8% vs CAPM hurdle 12.8%. Downtrend -2% vs 200-day avg; 12-1 mom +100%; RSI 41. Quality z -0.28 (ROE 29%).

??? note "GFS (GFS) — ⚪ Hold, score -0.11"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 46.70 USD (+63%, 22 analysts); de-biased α +4.5% vs CAPM hurdle 12.4%. Downtrend -15% vs 200-day avg; 12-1 mom +36%; RSI 49. Quality z -0.21 (ROE 8%).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.14"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 342.45 USD (+55%, 47 analysts); de-biased α +3.0% vs CAPM hurdle 11.2%. Downtrend -7% vs 200-day avg; 12-1 mom -1%; RSI 48. Quality z +0.26 (ROE 31%).

??? note "TER (TER) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 324.87 USD (+37%, 15 analysts); de-biased α -1.9% vs CAPM hurdle 12.3%. Downtrend -7% vs 200-day avg; 12-1 mom +174%; RSI 39. Quality z -0.31 (ROE 20%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.28"
    Avoid: not owned. Analyst target 116.37 USD vs 93.73 USD (+24%, 43 analysts); de-biased α -5.6% vs CAPM hurdle 14.0%. Uptrend +8% vs 200-day avg; 12-1 mom +193%; RSI 43. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 81,730 JPY vs 52,540 JPY (+56%, 20 analysts); de-biased α +3.0% vs CAPM hurdle 11.5%. Downtrend -20% vs 200-day avg; 12-1 mom +6%; RSI 45. Quality z +0.06 (ROE 25%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.47"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 761.80 EUR (+48%, 19 analysts); de-biased α +0.6% vs CAPM hurdle 13.2%. Downtrend -6% vs 200-day avg; 12-1 mom +50%; RSI 43. Quality z -0.10 (ROE 19%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 619.51 USD vs 560.45 USD (+11%, 50 analysts); de-biased α -9.3% vs CAPM hurdle 14.9%. Uptrend +38% vs 200-day avg; 12-1 mom +134%; RSI 50. Quality z -0.15 (ROE 7%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.62"
    Avoid: not owned. Analyst target 324.71 USD vs 309.02 USD (+5%, 31 analysts); de-biased α -9.1% vs CAPM hurdle 10.8%. Uptrend +20% vs 200-day avg; 12-1 mom +71%; RSI 70. Quality z +0.24 (ROE 30%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.68"
    Avoid: not owned. Analyst target 76.40 USD vs 39.96 USD (+91%, 10 analysts); de-biased α +11.3% vs CAPM hurdle 14.0%. Downtrend -30% vs 200-day avg; 12-1 mom +64%; RSI 37. Quality z -1.00 (ROE 9%).

??? failure "SMIC (0981.HK) — 🔴 Sell, score -0.70"
    Avoid: not owned. Analyst target 95.99 HKD vs 47.80 HKD (+101%, 21 analysts); de-biased α +15.2% vs CAPM hurdle 7.3%. Downtrend -30% vs 200-day avg; 12-1 mom -8%; RSI 29. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 288.70 USD vs 226.55 USD (+27%, 40 analysts); de-biased α -6.2% vs CAPM hurdle 19.6%. Downtrend -1% vs 200-day avg; 12-1 mom +64%; RSI 40. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 173.36 USD vs 150.18 USD (+15%, 11 analysts); de-biased α -7.0% vs CAPM hurdle 11.0%. Uptrend +9% vs 200-day avg; 12-1 mom +65%; RSI 52. Quality z -0.02 (ROE 6%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,000 JPY (+29%, 17 analysts); de-biased α -3.1% vs CAPM hurdle 10.8%. Downtrend -5% vs 200-day avg; 12-1 mom +17%; RSI 53. Quality z -0.20 (ROE 10%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.05"
    Avoid: not owned. Analyst target 405.47 USD vs 343.18 USD (+18%, 26 analysts); de-biased α -6.1% vs CAPM hurdle 10.0%. Uptrend +5% vs 200-day avg; 12-1 mom -8%; RSI 58. Quality z +0.31 (ROE 22%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.25"
    Avoid: not owned. Analyst target 194.13 USD vs 184.20 USD (+5%, 30 analysts); de-biased α -9.3% vs CAPM hurdle 11.9%. Uptrend +9% vs 200-day avg; 12-1 mom +0%; RSI 56. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.37"
    Avoid: not owned. Analyst target 569.78 USD vs 474.19 USD (+20%, 26 analysts); de-biased α -5.7% vs CAPM hurdle 10.3%. Uptrend +7% vs 200-day avg; 12-1 mom -11%; RSI 57. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,481,000 KRW | $108,346 | 11.7% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 240,500 KRW | $87,074 | 9.4% | Strong Buy |
| MU | Micron Technology | 92 | 929.16 USD | $85,483 | 9.2% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 52.55 EUR | $76,091 | 8.2% | Buy |
| AMAT | Applied Materials | 145 | 395.95 USD | $57,413 | 6.2% | Buy |
| ASX | ASE Technology | 1,320 | 42.09 USD | $55,559 | 6.0% | Buy |
| TSM | TSMC | 127 | 436.88 USD | $55,483 | 6.0% | Buy |
| ASML | ASML Holding | 30 | 1,635.80 USD | $49,074 | 5.3% | Buy |
| 6857.T | Advantest | 200 | 35,020 JPY | $44,409 | 4.8% | Hold |
| KLAC | KLA Corp | 268 | 153.65 USD | $41,178 | 4.4% | Hold |
| LRCX | Lam Research | 162 | 240.84 USD | $39,016 | 4.2% | Hold |
| NVDA | NVIDIA | 168 | 217.88 USD | $36,605 | 3.9% | Buy |
| AVGO | Broadcom | 100 | 342.45 USD | $34,245 | 3.7% | Hold |
| 8035.T | Tokyo Electron | 500 | 9,813 JPY | $31,110 | 3.4% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-10-15 04:41 UTC | ADD | 000660.KS | 24 | 1,270,000.00 | $22,625 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 32.7%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
