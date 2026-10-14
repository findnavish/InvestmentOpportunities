---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-14 20:42 UTC (Wed Oct 14, 04:42 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Wed 16:42) · Tokyo 🔴 closed (Thu 05:42) · Korea 🔴 closed (Thu 05:42) · Hong Kong 🔴 closed (Thu 04:42) · Xetra 🔴 closed (Wed 22:42) · Euronext Amsterdam 🔴 closed (Wed 22:42)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$942,538** | $121,442 (13%) | $821,096 (87%) | -5.75% | -8.15% | 🟢 Risk-on (+11.6%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $942,538), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| – | No trades this hour | | | | | All positions are within their rebalance bands. |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.35 | **SK hynix**<br><small>000660.KS</small> | 1,415,000 KRW | +122% | +20.3% | +452% | -3% | 30 | +0.62 | 8.3% → 10.0% | – | analyst α +0.85 · momentum +0.53 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.21 | **MU**<br><small>Micron Technology</small> | 913.91 USD | +66% | +6.5% | +382% | +28% | 36 | +0.12 | 8.9% → 10.0% | – | analyst α +0.41 · momentum +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.65 | **Samsung**<br><small>005930.KS</small> | 231,250 KRW | +106% | +17.3% | +227% | -0% | 34 | -0.26 | 8.9% → 10.0% | – | analyst α +0.66 · momentum +0.35 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.54 | **Infineon**<br><small>IFX.DE</small> | 55.05 EUR | +58% | +4.4% | +68% | -3% | 41 | -0.04 | 10.4% → 9.0% | – | analyst α +0.36 · trend -0.12 |
| 🟢 Buy | +0.51 | **AMAT**<br><small>Applied Materials</small> | 446.48 USD | +43% | +1.4% | +93% | +2% | 36 | +0.03 | 7.4% → 7.3% | – | analyst α +0.19 · momentum +0.07 |
| 🟢 Buy | +0.50 | **NVDA**<br><small>NVIDIA</small> | 221.50 USD | +48% | +1.9% | +13% | +9% | 44 | +0.47 | 8.7% → 8.4% | – | momentum -0.26 · analyst α +0.23 |
| 🟢 Buy | +0.50 | **KLAC**<br><small>KLA Corp</small> | 178.80 USD | +31% | -1.6% | +65% | -1% | 39 | +0.51 | 7.1% → 7.7% | – | quality +0.24 · trend -0.09 |
| 🟢 Buy | +0.45 | **TSM**<br><small>TSMC</small> | 430.08 USD | +28% | -2.0% | +38% | +10% | 41 | +0.58 | 8.5% → 9.1% | – | quality +0.28 · momentum -0.12 |
| 🟢 Buy | +0.30 | **Tokyo Electron**<br><small>8035.T</small> | 11,320 JPY | +35% | -0.8% | +102% | +14% | 49 | -0.28 | 4.6% → 4.3% | – | quality -0.18 · momentum +0.12 |
| 🟢 Buy | +0.27 | **ASML**<br><small>ASML Holding</small> | 1,649.85 USD | +27% | -2.8% | +63% | +5% | 38 | +0.42 | 5.3% → 5.0% | – | quality +0.18 · analyst α -0.08 |
| ⚪ Hold | +0.17 | **ASX**<br><small>ASE Technology</small> | 44.32 USD | +15% | -2.8% | +220% | +40% | 52 | -0.68 | 4.2% → 4.2% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.13 | **LRCX**<br><small>Lam Research</small> | 286.72 USD | +31% | -2.0% | +97% | +2% | 37 | +0.02 | 0.0% → 0.0% | – | momentum +0.10 · trend -0.04 |
| ⚪ Hold | +0.09 | **MRVL**<br><small>Marvell Technology</small> | 245.24 USD | +20% | -5.1% | +148% | +41% | 44 | -0.12 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.23 · ⚠️ rich valuation |
| ⚪ Hold | -0.07 | **ASMI**<br><small>ASM.AS</small> | 825.00 EUR | +37% | -0.6% | +41% | +2% | 43 | -0.10 | 0.0% → 0.0% | – | analyst α +0.12 · momentum -0.07 |
| ⚪ Hold | -0.15 | **AVGO**<br><small>Broadcom</small> | 346.28 USD | +53% | +4.2% | -4% | -6% | 42 | +0.26 | 4.9% → 4.9% | – | momentum -0.30 · analyst α +0.27 |
| ⚪ Hold | -0.21 | **TXN**<br><small>Texas Instruments</small> | 280.79 USD | +16% | -4.9% | +54% | +12% | 52 | +0.24 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.10 |
| 🔴 Sell | -0.30 | **GFS**<br><small>GlobalFoundries</small> | 48.94 USD | +55% | +4.2% | +24% | -10% | 53 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.18 |
| 🔴 Sell | -0.42 | **TER**<br><small>Teradyne</small> | 359.29 USD | +24% | -3.6% | +140% | +5% | 40 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.44 | **INTC**<br><small>Intel</small> | 98.11 USD | +19% | -5.4% | +161% | +17% | 38 | -0.62 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.50 | **Disco**<br><small>6146.T</small> | 58,260 JPY | +40% | +0.8% | +16% | -11% | 50 | +0.06 | 0.0% → 0.0% | – | momentum -0.23 · trend -0.21 |
| 🔴 Sell | -0.54 | **QCOM**<br><small>Qualcomm</small> | 172.72 USD | +12% | -6.0% | +19% | +3% | 42 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴 Sell | -0.56 | **AMD**<br><small>Advanced Micro Devices</small> | 570.74 USD | +9% | -8.2% | +133% | +46% | 46 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.64 | **AMKR**<br><small>Amkor Technology</small> | 44.79 USD | +71% | +7.7% | +53% | -22% | 35 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.65 | **Advantest**<br><small>6857.T</small> | 40,700 JPY | +5% | -8.7% | +132% | +44% | 66 | +0.33 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 · ⚠️ rich valuation |
| 🔴🔴 Strong Sell | -0.83 | **ENTG**<br><small>Entegris</small> | 153.07 USD | +13% | -6.0% | +42% | +13% | 50 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.10 |
| 🔴🔴 Strong Sell | -0.90 | **CDNS**<br><small>Cadence Design Systems</small> | 329.53 USD | +23% | -3.3% | -18% | +1% | 50 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -0.92 | **Shin-Etsu**<br><small>4063.T</small> | 6,164 JPY | +26% | -2.4% | +20% | -1% | 57 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.10 | **SNPS**<br><small>Synopsys</small> | 480.00 USD | +19% | -4.5% | -18% | +8% | 60 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.18 | **SMIC**<br><small>0981.HK</small> | 54.30 HKD | +77% | +10.8% | -33% | -21% | 27 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.26 | **ARM**<br><small>Arm Holdings</small> | 238.09 USD | +21% | -6.2% | +41% | +7% | 36 | +0.04 | 0.0% → 0.0% | – | analyst α -0.55 · momentum -0.10 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.35"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,415,000 KRW (+122%, 38 analysts); de-biased α +20.3% vs CAPM hurdle 14.3%. Downtrend -3% vs 200-day avg; 12-1 mom +452%; RSI 30. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.21"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 913.91 USD (+66%, 46 analysts); de-biased α +6.5% vs CAPM hurdle 14.0%. Uptrend +28% vs 200-day avg; 12-1 mom +382%; RSI 36. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.65"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 231,250 KRW (+106%, 36 analysts); de-biased α +17.3% vs CAPM hurdle 11.3%. Downtrend -0% vs 200-day avg; 12-1 mom +227%; RSI 34. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.54"
    Within rebalance band of target 9.0%: no trade. Analyst target 86.74 EUR vs 55.05 EUR (+58%, 23 analysts); de-biased α +4.4% vs CAPM hurdle 14.1%. Downtrend -3% vs 200-day avg; 12-1 mom +68%; RSI 41. Quality z -0.04 (ROE 6%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.51"
    Within rebalance band of target 7.3%: no trade. Analyst target 638.94 USD vs 446.48 USD (+43%, 36 analysts); de-biased α +1.4% vs CAPM hurdle 11.6%. Uptrend +2% vs 200-day avg; 12-1 mom +93%; RSI 36. Quality z +0.03 (ROE 36%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.50"
    Within rebalance band of target 8.4%: no trade. Analyst target 327.70 USD vs 221.50 USD (+48%, 59 analysts); de-biased α +1.9% vs CAPM hurdle 13.9%. Uptrend +9% vs 200-day avg; 12-1 mom +13%; RSI 44. Quality z +0.47 (ROE 101%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.50"
    Within rebalance band of target 7.7%: no trade. Analyst target 233.77 USD vs 178.80 USD (+31%, 26 analysts); de-biased α -1.6% vs CAPM hurdle 11.1%. Downtrend -1% vs 200-day avg; 12-1 mom +65%; RSI 39. Quality z +0.51 (ROE 87%).

??? success "TSM (TSM) — 🟢 Buy, score +0.45"
    Within rebalance band of target 9.1%: no trade. Analyst target 552.26 USD vs 430.08 USD (+28%, 20 analysts); de-biased α -2.0% vs CAPM hurdle 10.8%. Uptrend +10% vs 200-day avg; 12-1 mom +38%; RSI 41. Quality z +0.58 (ROE 35%).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.30"
    Within rebalance band of target 4.3%: no trade. Analyst target 15,275 JPY vs 11,320 JPY (+35%, 23 analysts); de-biased α -0.8% vs CAPM hurdle 12.8%. Uptrend +14% vs 200-day avg; 12-1 mom +102%; RSI 49. Quality z -0.28 (ROE 29%).

??? success "ASML (ASML) — 🟢 Buy, score +0.27"
    Within rebalance band of target 5.0%: no trade. Analyst target 2,096.77 USD vs 1,649.85 USD (+27%, 16 analysts); de-biased α -2.8% vs CAPM hurdle 12.3%. Uptrend +5% vs 200-day avg; 12-1 mom +63%; RSI 38. Quality z +0.42 (ROE 50%).

??? note "ASX (ASX) — ⚪ Hold, score +0.17"
    Hold zone: keep any existing position, no new money. Analyst target 51.00 USD vs 44.32 USD (+15%, 1 analysts); de-biased α -2.8% vs CAPM hurdle 11.9%. Uptrend +40% vs 200-day avg; 12-1 mom +220%; RSI 52. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.13"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 286.72 USD (+31%, 31 analysts); de-biased α -2.0% vs CAPM hurdle 12.6%. Uptrend +2% vs 200-day avg; 12-1 mom +97%; RSI 37. Quality z +0.02 (ROE 65%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.09"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 245.24 USD (+20%, 43 analysts); de-biased α -5.1% vs CAPM hurdle 14.1%. Uptrend +41% vs 200-day avg; 12-1 mom +148%; RSI 44. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.07"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 825.00 EUR (+37%, 19 analysts); de-biased α -0.6% vs CAPM hurdle 13.2%. Uptrend +2% vs 200-day avg; 12-1 mom +41%; RSI 43. Quality z -0.10 (ROE 19%).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.15"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 346.28 USD (+53%, 47 analysts); de-biased α +4.2% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom -4%; RSI 42. Quality z +0.26 (ROE 31%).

??? note "TXN (TXN) — ⚪ Hold, score -0.21"
    Hold zone: not owned, no entry. Analyst target 324.71 USD vs 280.79 USD (+16%, 31 analysts); de-biased α -4.9% vs CAPM hurdle 10.8%. Uptrend +12% vs 200-day avg; 12-1 mom +54%; RSI 52. Quality z +0.24 (ROE 30%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.30"
    Avoid: not owned. Analyst target 76.00 USD vs 48.94 USD (+55%, 22 analysts); de-biased α +4.2% vs CAPM hurdle 12.4%. Downtrend -10% vs 200-day avg; 12-1 mom +24%; RSI 53. Quality z -0.21 (ROE 8%).

??? failure "TER (TER) — 🔴 Sell, score -0.42"
    Avoid: not owned. Analyst target 446.47 USD vs 359.29 USD (+24%, 15 analysts); de-biased α -3.6% vs CAPM hurdle 12.3%. Uptrend +5% vs 200-day avg; 12-1 mom +140%; RSI 40. Quality z -0.31 (ROE 20%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 116.37 USD vs 98.11 USD (+19%, 43 analysts); de-biased α -5.4% vs CAPM hurdle 14.0%. Uptrend +17% vs 200-day avg; 12-1 mom +161%; RSI 38. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 81,730 JPY vs 58,260 JPY (+40%, 20 analysts); de-biased α +0.8% vs CAPM hurdle 11.5%. Downtrend -11% vs 200-day avg; 12-1 mom +16%; RSI 50. Quality z +0.06 (ROE 25%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 194.13 USD vs 172.72 USD (+12%, 30 analysts); de-biased α -6.0% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +19%; RSI 42. Quality z +0.70 (ROE 23%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.56"
    Avoid: not owned. Analyst target 619.51 USD vs 570.74 USD (+9%, 50 analysts); de-biased α -8.2% vs CAPM hurdle 14.9%. Uptrend +46% vs 200-day avg; 12-1 mom +133%; RSI 46. Quality z -0.15 (ROE 7%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 76.40 USD vs 44.79 USD (+71%, 10 analysts); de-biased α +7.7% vs CAPM hurdle 14.0%. Downtrend -22% vs 200-day avg; 12-1 mom +53%; RSI 35. Quality z -1.00 (ROE 9%).

??? failure "Advantest (6857.T) — 🔴 Sell, score -0.65"
    Avoid: not owned. Analyst target 42,686 JPY vs 40,700 JPY (+5%, 21 analysts); de-biased α -8.7% vs CAPM hurdle 13.4%. Uptrend +44% vs 200-day avg; 12-1 mom +132%; RSI 66. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.83"
    Avoid: not owned. Analyst target 173.36 USD vs 153.07 USD (+13%, 11 analysts); de-biased α -6.0% vs CAPM hurdle 11.0%. Uptrend +13% vs 200-day avg; 12-1 mom +42%; RSI 50. Quality z -0.02 (ROE 6%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.90"
    Avoid: not owned. Analyst target 405.47 USD vs 329.53 USD (+23%, 26 analysts); de-biased α -3.3% vs CAPM hurdle 10.0%. Uptrend +1% vs 200-day avg; 12-1 mom -18%; RSI 50. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,164 JPY (+26%, 17 analysts); de-biased α -2.4% vs CAPM hurdle 10.8%. Downtrend -1% vs 200-day avg; 12-1 mom +20%; RSI 57. Quality z -0.20 (ROE 10%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.10"
    Avoid: not owned. Analyst target 569.78 USD vs 480.00 USD (+19%, 26 analysts); de-biased α -4.5% vs CAPM hurdle 10.3%. Uptrend +8% vs 200-day avg; 12-1 mom -18%; RSI 60. Quality z +0.14 (ROE 7%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.18"
    Avoid: not owned. Analyst target 95.99 HKD vs 54.30 HKD (+77%, 21 analysts); de-biased α +10.8% vs CAPM hurdle 7.3%. Downtrend -21% vs 200-day avg; 12-1 mom -33%; RSI 27. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.26"
    Avoid: not owned. Analyst target 288.70 USD vs 238.09 USD (+21%, 40 analysts); de-biased α -6.2% vs CAPM hurdle 19.6%. Uptrend +7% vs 200-day avg; 12-1 mom +41%; RSI 36. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| IFX.DE | Infineon Technologies | 1,594 | 55.05 EUR | $97,913 | 10.4% | Buy |
| MU | Micron Technology | 92 | 913.91 USD | $84,080 | 8.9% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 231,250 KRW | $83,601 | 8.9% | Strong Buy |
| NVDA | NVIDIA | 371 | 221.50 USD | $82,176 | 8.7% | Buy |
| TSM | TSMC | 187 | 430.08 USD | $80,425 | 8.5% | Buy |
| 000660.KS | SK hynix | 74 | 1,415,000 KRW | $78,051 | 8.3% | Strong Buy |
| AMAT | Applied Materials | 156 | 446.48 USD | $69,651 | 7.4% | Buy |
| KLAC | KLA Corp | 372 | 178.80 USD | $66,514 | 7.1% | Buy |
| ASML | ASML Holding | 30 | 1,649.85 USD | $49,495 | 5.3% | Buy |
| AVGO | Broadcom | 134 | 346.28 USD | $46,402 | 4.9% | Hold |
| 8035.T | Tokyo Electron | 600 | 11,320 JPY | $42,899 | 4.6% | Buy |
| ASX | ASE Technology | 900 | 44.32 USD | $39,888 | 4.2% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-09-30 13:45 UTC | TRIM | IFX.DE | -347 | 59.55 | $23,474 |
| 2026-09-30 00:28 UTC | BUY (new) | 8035.T | 700 | 11,900.00 | $52,952 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 26.4%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
