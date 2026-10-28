---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-28 01:23 UTC (Tue Oct 27, 09:23 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Tue 21:23) · Tokyo 🟢 open (Wed 10:23) · Korea 🟢 open (Wed 10:23) · Hong Kong 🔴 closed (Wed 09:23) · Xetra 🔴 closed (Wed 02:23) · Euronext Amsterdam 🔴 closed (Wed 02:23)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$923,352** | $126,836 (14%) | $796,516 (86%) | -7.66% | -9.61% | 🟢 Risk-on (+8.2%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $923,352), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **AMAT**<br><small>Applied Materials</small> | 88 | 395.95 USD | $34,844 | Queued · NYSE/Nasdaq closed | analyst α +0.31 · momentum +0.14 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.38 | **SK hynix**<br><small>000660.KS</small> | 1,424,500 KRW | +121% | +18.2% | +313% | -4% | 45 | +0.62 | 11.3% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.25 | **MU**<br><small>Micron Technology</small> | 929.16 USD | +64% | +4.0% | +382% | +26% | 46 | +0.12 | 9.3% → 10.0% | – | momentum +0.53 · analyst α +0.27 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.36 | **Samsung**<br><small>005930.KS</small> | 237,500 KRW | +101% | +14.2% | +195% | +1% | 49 | -0.26 | 9.4% → 10.0% | – | analyst α +0.55 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +0.75 | **AMAT**<br><small>Applied Materials</small> | 395.95 USD | +61% | +4.1% | +114% | -10% | 34 | +0.03 | 6.2% → 10.0% | ADD 88 | analyst α +0.31 · momentum +0.14 |
| 🟢 Buy | +0.53 | **Infineon**<br><small>IFX.DE</small> | 52.85 EUR | +64% | +4.2% | +66% | -7% | 44 | -0.04 | 8.3% → 8.5% | – | analyst α +0.36 · trend -0.09 |
| 🟢 Buy | +0.49 | **ASX**<br><small>ASE Technology</small> | 42.09 USD | +21% | -2.9% | +241% | +28% | 50 | -0.68 | 6.0% → 7.5% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.31 | **TSM**<br><small>TSMC</small> | 436.88 USD | +26% | -4.3% | +55% | +10% | 51 | +0.58 | 6.0% → 6.1% | – | quality +0.28 · analyst α -0.15 |
| 🟢 Buy | +0.29 | **ASML**<br><small>ASML Holding</small> | 1,635.80 USD | +28% | -4.3% | +73% | +3% | 44 | +0.42 | 5.3% → 5.3% | – | quality +0.18 · analyst α -0.12 |
| 🟢 Buy | +0.25 | **Advantest**<br><small>6857.T</small> | 34,750 JPY | +23% | -6.0% | +99% | +21% | 49 | +0.33 | 4.8% → 2.8% | – | analyst α -0.27 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.24 | **NVDA**<br><small>NVIDIA</small> | 217.88 USD | +50% | +0.7% | +23% | +7% | 46 | +0.47 | 4.0% → 4.0% | – | quality +0.21 · momentum -0.17 |
| ⚪ Hold | +0.20 | **LRCX**<br><small>Lam Research</small> | 240.84 USD | +56% | +2.5% | +108% | -15% | 31 | +0.02 | 4.2% → 4.2% | – | trend -0.14 · momentum +0.12 |
| ⚪ Hold | +0.19 | **Tokyo Electron**<br><small>8035.T</small> | 9,743 JPY | +57% | +2.9% | +100% | -3% | 41 | -0.28 | 3.3% → 3.3% | – | analyst α +0.19 · quality -0.18 |
| ⚪ Hold | +0.15 | **KLAC**<br><small>KLA Corp</small> | 153.65 USD | +52% | +1.9% | +61% | -15% | 33 | +0.51 | 4.5% → 4.5% | – | quality +0.24 · trend -0.18 |
| ⚪ Hold | +0.03 | **MRVL**<br><small>Marvell Technology</small> | 243.62 USD | +21% | -6.8% | +200% | +35% | 49 | -0.12 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.26 · ⚠️ rich valuation |
| ⚪ Hold | -0.04 | **GFS**<br><small>GlobalFoundries</small> | 46.70 USD | +63% | +4.2% | +36% | -15% | 49 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.16 |
| ⚪ Hold | -0.13 | **INTC**<br><small>Intel</small> | 93.75 USD | +24% | -5.9% | +203% | +9% | 43 | -0.62 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| ⚪ Hold | -0.19 | **AVGO**<br><small>Broadcom</small> | 342.45 USD | +55% | +2.8% | -1% | -7% | 48 | +0.26 | 3.7% → 3.7% | – | momentum -0.30 · analyst α +0.15 |
| ⚪ Hold | -0.22 | **TER**<br><small>Teradyne</small> | 324.87 USD | +37% | -2.1% | +179% | -7% | 39 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.42 | **Disco**<br><small>6146.T</small> | 51,950 JPY | +57% | +3.3% | +6% | -21% | 43 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.23 |
| 🔴 Sell | -0.50 | **ASMI**<br><small>ASM.AS</small> | 743.20 EUR | +52% | +1.3% | +50% | -8% | 40 | -0.10 | 0.0% → 0.0% | – | momentum -0.12 · trend -0.10 |
| 🔴 Sell | -0.54 | **AMKR**<br><small>Amkor Technology</small> | 39.96 USD | +91% | +11.0% | +63% | -30% | 37 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.57 | **AMD**<br><small>Advanced Micro Devices</small> | 560.45 USD | +11% | -9.5% | +140% | +38% | 50 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.63 | **TXN**<br><small>Texas Instruments</small> | 309.02 USD | +5% | -9.4% | +69% | +20% | 70 | +0.24 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.14 |
| 🔴🔴 Strong Sell | -0.76 | **ARM**<br><small>Arm Holdings</small> | 226.55 USD | +27% | -6.4% | +66% | -0% | 40 | +0.04 | 0.0% → 0.0% | – | analyst α -0.36 · quality +0.03 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.87 | **SMIC**<br><small>0981.HK</small> | 45.34 HKD | +112% | +17.7% | -8% | -33% | 17 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.41 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -0.95 | **Shin-Etsu**<br><small>4063.T</small> | 6,013 JPY | +29% | -3.4% | +17% | -5% | 53 | -0.20 | 0.0% → 0.0% | – | momentum -0.20 · quality -0.11 |
| 🔴🔴 Strong Sell | -0.97 | **ENTG**<br><small>Entegris</small> | 150.18 USD | +15% | -7.2% | +65% | +9% | 52 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.09 |
| 🔴🔴 Strong Sell | -1.07 | **CDNS**<br><small>Cadence Design Systems</small> | 343.18 USD | +18% | -6.4% | -5% | +5% | 58 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.31 |
| 🔴🔴 Strong Sell | -1.19 | **QCOM**<br><small>Qualcomm</small> | 184.23 USD | +5% | -9.6% | +13% | +10% | 56 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.38 | **SNPS**<br><small>Synopsys</small> | 474.19 USD | +20% | -5.9% | -10% | +7% | 57 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · analyst α -0.23 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.38"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,424,500 KRW (+121%, 38 analysts); de-biased α +18.2% vs CAPM hurdle 14.3%. Downtrend -4% vs 200-day avg; 12-1 mom +313%; RSI 45. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.25"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 929.16 USD (+64%, 46 analysts); de-biased α +4.0% vs CAPM hurdle 14.0%. Uptrend +26% vs 200-day avg; 12-1 mom +382%; RSI 46. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.36"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 237,500 KRW (+101%, 36 analysts); de-biased α +14.2% vs CAPM hurdle 11.3%. Uptrend +1% vs 200-day avg; 12-1 mom +195%; RSI 49. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "AMAT (AMAT) — 🟢🟢 Strong Buy, score +0.75"
    **ADD 88 sh** → target 10.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 395.95 USD (+61%, 36 analysts); de-biased α +4.1% vs CAPM hurdle 11.6%. Downtrend -10% vs 200-day avg; 12-1 mom +114%; RSI 34. Quality z +0.03 (ROE 36%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.53"
    Within rebalance band of target 8.5%: no trade. Analyst target 86.74 EUR vs 52.85 EUR (+64%, 23 analysts); de-biased α +4.2% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +66%; RSI 44. Quality z -0.04 (ROE 6%).

??? success "ASX (ASX) — 🟢 Buy, score +0.49"
    Within rebalance band of target 7.5%: no trade. Analyst target 51.00 USD vs 42.09 USD (+21%, 1 analysts); de-biased α -2.9% vs CAPM hurdle 11.9%. Uptrend +28% vs 200-day avg; 12-1 mom +241%; RSI 50. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.31"
    Within rebalance band of target 6.1%: no trade. Analyst target 552.26 USD vs 436.88 USD (+26%, 20 analysts); de-biased α -4.3% vs CAPM hurdle 10.8%. Uptrend +10% vs 200-day avg; 12-1 mom +55%; RSI 51. Quality z +0.58 (ROE 35%).

??? success "ASML (ASML) — 🟢 Buy, score +0.29"
    Within rebalance band of target 5.3%: no trade. Analyst target 2,096.77 USD vs 1,635.80 USD (+28%, 16 analysts); de-biased α -4.3% vs CAPM hurdle 12.3%. Uptrend +3% vs 200-day avg; 12-1 mom +73%; RSI 44. Quality z +0.42 (ROE 50%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.25"
    Within rebalance band of target 2.8%: no trade. Analyst target 42,686 JPY vs 34,750 JPY (+23%, 21 analysts); de-biased α -6.0% vs CAPM hurdle 13.4%. Uptrend +21% vs 200-day avg; 12-1 mom +99%; RSI 49. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "NVDA (NVDA) — ⚪ Hold, score +0.24"
    Hold zone: keep any existing position, no new money. Analyst target 327.70 USD vs 217.88 USD (+50%, 59 analysts); de-biased α +0.7% vs CAPM hurdle 13.9%. Uptrend +7% vs 200-day avg; 12-1 mom +23%; RSI 46. Quality z +0.47 (ROE 101%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.20"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 240.84 USD (+56%, 31 analysts); de-biased α +2.5% vs CAPM hurdle 12.6%. Downtrend -15% vs 200-day avg; 12-1 mom +108%; RSI 31. Quality z +0.02 (ROE 65%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.19"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 9,743 JPY (+57%, 23 analysts); de-biased α +2.9% vs CAPM hurdle 12.8%. Downtrend -3% vs 200-day avg; 12-1 mom +100%; RSI 41. Quality z -0.28 (ROE 29%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 153.65 USD (+52%, 26 analysts); de-biased α +1.9% vs CAPM hurdle 11.1%. Downtrend -15% vs 200-day avg; 12-1 mom +61%; RSI 33. Quality z +0.51 (ROE 87%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.03"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 243.62 USD (+21%, 43 analysts); de-biased α -6.8% vs CAPM hurdle 14.1%. Uptrend +35% vs 200-day avg; 12-1 mom +200%; RSI 49. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "GFS (GFS) — ⚪ Hold, score -0.04"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 46.70 USD (+63%, 22 analysts); de-biased α +4.2% vs CAPM hurdle 12.4%. Downtrend -15% vs 200-day avg; 12-1 mom +36%; RSI 49. Quality z -0.21 (ROE 8%).

??? note "INTC (INTC) — ⚪ Hold, score -0.13"
    Hold zone: not owned, no entry. Analyst target 116.37 USD vs 93.75 USD (+24%, 43 analysts); de-biased α -5.9% vs CAPM hurdle 14.0%. Uptrend +9% vs 200-day avg; 12-1 mom +203%; RSI 43. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? note "AVGO (AVGO) — ⚪ Hold, score -0.19"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 342.45 USD (+55%, 47 analysts); de-biased α +2.8% vs CAPM hurdle 11.2%. Downtrend -7% vs 200-day avg; 12-1 mom -1%; RSI 48. Quality z +0.26 (ROE 31%).

??? note "TER (TER) — ⚪ Hold, score -0.22"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 324.87 USD (+37%, 15 analysts); de-biased α -2.1% vs CAPM hurdle 12.3%. Downtrend -7% vs 200-day avg; 12-1 mom +179%; RSI 39. Quality z -0.31 (ROE 20%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.42"
    Avoid: not owned. Analyst target 81,730 JPY vs 51,950 JPY (+57%, 20 analysts); de-biased α +3.3% vs CAPM hurdle 11.5%. Downtrend -21% vs 200-day avg; 12-1 mom +6%; RSI 43. Quality z +0.06 (ROE 25%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 743.20 EUR (+52%, 19 analysts); de-biased α +1.3% vs CAPM hurdle 13.2%. Downtrend -8% vs 200-day avg; 12-1 mom +50%; RSI 40. Quality z -0.10 (ROE 19%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 76.40 USD vs 39.96 USD (+91%, 10 analysts); de-biased α +11.0% vs CAPM hurdle 14.0%. Downtrend -30% vs 200-day avg; 12-1 mom +63%; RSI 37. Quality z -1.00 (ROE 9%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 619.51 USD vs 560.45 USD (+11%, 50 analysts); de-biased α -9.5% vs CAPM hurdle 14.9%. Uptrend +38% vs 200-day avg; 12-1 mom +140%; RSI 50. Quality z -0.15 (ROE 7%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.63"
    Avoid: not owned. Analyst target 324.71 USD vs 309.02 USD (+5%, 31 analysts); de-biased α -9.4% vs CAPM hurdle 10.8%. Uptrend +20% vs 200-day avg; 12-1 mom +69%; RSI 70. Quality z +0.24 (ROE 30%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.76"
    Avoid: not owned. Analyst target 288.70 USD vs 226.55 USD (+27%, 40 analysts); de-biased α -6.4% vs CAPM hurdle 19.6%. Downtrend -0% vs 200-day avg; 12-1 mom +66%; RSI 40. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.87"
    Avoid: not owned. Analyst target 95.99 HKD vs 45.34 HKD (+112%, 21 analysts); de-biased α +17.7% vs CAPM hurdle 7.3%. Downtrend -33% vs 200-day avg; 12-1 mom -8%; RSI 17. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.95"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,013 JPY (+29%, 17 analysts); de-biased α -3.4% vs CAPM hurdle 10.8%. Downtrend -5% vs 200-day avg; 12-1 mom +17%; RSI 53. Quality z -0.20 (ROE 10%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.97"
    Avoid: not owned. Analyst target 173.36 USD vs 150.18 USD (+15%, 11 analysts); de-biased α -7.2% vs CAPM hurdle 11.0%. Uptrend +9% vs 200-day avg; 12-1 mom +65%; RSI 52. Quality z -0.02 (ROE 6%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.07"
    Avoid: not owned. Analyst target 405.47 USD vs 343.18 USD (+18%, 26 analysts); de-biased α -6.4% vs CAPM hurdle 10.0%. Uptrend +5% vs 200-day avg; 12-1 mom -5%; RSI 58. Quality z +0.31 (ROE 22%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.19"
    Avoid: not owned. Analyst target 194.13 USD vs 184.23 USD (+5%, 30 analysts); de-biased α -9.6% vs CAPM hurdle 11.9%. Uptrend +10% vs 200-day avg; 12-1 mom +13%; RSI 56. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.38"
    Avoid: not owned. Analyst target 569.78 USD vs 474.19 USD (+20%, 26 analysts); de-biased α -5.9% vs CAPM hurdle 10.3%. Uptrend +7% vs 200-day avg; 12-1 mom -10%; RSI 57. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,424,500 KRW | $104,683 | 11.3% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 237,500 KRW | $86,376 | 9.4% | Strong Buy |
| MU | Micron Technology | 92 | 929.16 USD | $85,483 | 9.3% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 52.85 EUR | $76,517 | 8.3% | Buy |
| AMAT | Applied Materials | 145 | 395.95 USD | $57,413 | 6.2% | Strong Buy |
| ASX | ASE Technology | 1,320 | 42.09 USD | $55,559 | 6.0% | Buy |
| TSM | TSMC | 127 | 436.88 USD | $55,483 | 6.0% | Buy |
| ASML | ASML Holding | 30 | 1,635.80 USD | $49,074 | 5.3% | Buy |
| 6857.T | Advantest | 200 | 34,750 JPY | $44,026 | 4.8% | Buy |
| KLAC | KLA Corp | 268 | 153.65 USD | $41,178 | 4.5% | Hold |
| LRCX | Lam Research | 162 | 240.84 USD | $39,016 | 4.2% | Hold |
| NVDA | NVIDIA | 168 | 217.88 USD | $36,605 | 4.0% | Hold |
| AVGO | Broadcom | 100 | 342.45 USD | $34,245 | 3.7% | Hold |
| 8035.T | Tokyo Electron | 500 | 9,743 JPY | $30,859 | 3.3% | Hold |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 33.6%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
