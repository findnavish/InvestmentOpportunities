---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-27 16:40 UTC (Tue Oct 27, 12:40 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Tue 12:40) · Tokyo 🔴 closed (Wed 01:40) · Korea 🔴 closed (Wed 01:40) · Hong Kong 🔴 closed (Wed 00:40) · Xetra 🔴 closed (Tue 17:40) · Euronext Amsterdam 🔴 closed (Tue 17:40)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$910,649** | $126,836 (14%) | $783,813 (86%) | -8.94% | -9.99% | 🟢 Risk-on (+7.5%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $910,649), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **Infineon**<br><small>IFX.DE</small> | 434 | 52.85 EUR | $25,565 | Queued · Xetra closed | analyst α +0.27 · trend -0.07 |
| ADD | **Tokyo Electron**<br><small>8035.T</small> | 400 | 9,343 JPY | $23,673 | Queued · Tokyo closed | analyst α +0.36 · quality -0.18 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.33 | **SK hynix**<br><small>000660.KS</small> | 1,346,000 KRW | +133% | +20.9% | +337% | -9% | 39 | +0.62 | 10.9% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.15 | **MU**<br><small>Micron Technology</small> | 929.56 USD | +64% | +3.5% | +382% | +26% | 46 | +0.12 | 9.4% → 10.0% | – | momentum +0.53 · analyst α +0.19 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.38 | **Samsung**<br><small>005930.KS</small> | 222,500 KRW | +115% | +17.1% | +193% | -6% | 41 | -0.26 | 8.9% → 10.0% | – | analyst α +0.55 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.59 | **AMAT**<br><small>Applied Materials</small> | 396.66 USD | +61% | +3.6% | +114% | -10% | 34 | +0.03 | 6.3% → 7.6% | – | analyst α +0.23 · momentum +0.14 |
| 🟢 Buy | +0.51 | **ASX**<br><small>ASE Technology</small> | 41.71 USD | +22% | -3.0% | +241% | +27% | 49 | -0.68 | 6.0% → 7.2% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.49 | **Tokyo Electron**<br><small>8035.T</small> | 9,343 JPY | +63% | +4.1% | +95% | -7% | 35 | -0.28 | 3.2% → 6.4% | ADD 400 | analyst α +0.36 · quality -0.18 |
| 🟢 Buy | +0.40 | **TSM**<br><small>TSMC</small> | 436.63 USD | +26% | -4.8% | +55% | +10% | 51 | +0.58 | 6.1% → 7.3% | – | quality +0.28 · analyst α -0.12 |
| 🟢 Buy | +0.39 | **Advantest**<br><small>6857.T</small> | 34,040 JPY | +25% | -5.8% | +91% | +18% | 47 | +0.33 | 4.7% → 4.0% | – | analyst α -0.19 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.37 | **Infineon**<br><small>IFX.DE</small> | 52.85 EUR | +64% | +3.8% | +66% | -7% | 44 | -0.04 | 8.4% → 5.6% | TRIM 434 | analyst α +0.27 · trend -0.07 |
| 🟢 Buy | +0.25 | **NVDA**<br><small>NVIDIA</small> | 218.07 USD | +50% | +0.3% | +23% | +7% | 46 | +0.47 | 4.0% → 3.8% | – | quality +0.21 · momentum -0.17 |
| ⚪ Hold | +0.22 | **ASML**<br><small>ASML Holding</small> | 1,636.57 USD | +28% | -4.8% | +73% | +3% | 44 | +0.42 | 5.4% → 5.4% | – | quality +0.18 · analyst α -0.15 |
| ⚪ Hold | +0.21 | **LRCX**<br><small>Lam Research</small> | 240.56 USD | +56% | +2.0% | +108% | -15% | 31 | +0.02 | 4.3% → 4.3% | – | trend -0.14 · momentum +0.12 |
| ⚪ Hold | +0.16 | **KLAC**<br><small>KLA Corp</small> | 153.05 USD | +53% | +1.6% | +61% | -16% | 32 | +0.51 | 4.5% → 4.5% | – | quality +0.24 · trend -0.18 |
| ⚪ Hold | +0.15 | **MRVL**<br><small>Marvell Technology</small> | 242.40 USD | +21% | -7.1% | +200% | +34% | 48 | -0.12 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.26 · ⚠️ rich valuation |
| ⚪ Hold | -0.02 | **Disco**<br><small>6146.T</small> | 49,830 JPY | +64% | +4.5% | +2% | -24% | 37 | +0.06 | 0.0% → 0.0% | – | analyst α +0.41 · momentum -0.26 |
| ⚪ Hold | -0.11 | **AVGO**<br><small>Broadcom</small> | 343.48 USD | +55% | +2.2% | -1% | -6% | 48 | +0.26 | 3.8% → 3.8% | – | momentum -0.30 · analyst α +0.15 |
| ⚪ Hold | -0.13 | **TER**<br><small>Teradyne</small> | 325.84 USD | +37% | -2.6% | +179% | -6% | 40 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| ⚪ Hold | -0.15 | **INTC**<br><small>Intel</small> | 93.80 USD | +24% | -6.3% | +203% | +9% | 43 | -0.62 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.27 | **GFS**<br><small>GlobalFoundries</small> | 46.63 USD | +63% | +3.9% | +36% | -15% | 49 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.16 |
| 🔴 Sell | -0.48 | **ASMI**<br><small>ASM.AS</small> | 744.60 EUR | +52% | +0.8% | +50% | -8% | 40 | -0.10 | 0.0% → 0.0% | – | momentum -0.12 · trend -0.09 |
| 🔴 Sell | -0.55 | **AMKR**<br><small>Amkor Technology</small> | 38.74 USD | +97% | +12.1% | +63% | -32% | 33 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.63 | **QCOM**<br><small>Qualcomm</small> | 181.10 USD | +7% | -9.5% | +13% | +8% | 53 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴 Sell | -0.65 | **ARM**<br><small>Arm Holdings</small> | 226.70 USD | +27% | -6.9% | +66% | -0% | 40 | +0.04 | 0.0% → 0.0% | – | analyst α -0.31 · quality +0.03 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.84 | **TXN**<br><small>Texas Instruments</small> | 306.64 USD | +6% | -9.6% | +69% | +20% | 69 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.16 |
| 🔴🔴 Strong Sell | -0.98 | **Shin-Etsu**<br><small>4063.T</small> | 5,870 JPY | +32% | -3.1% | +18% | -7% | 46 | -0.20 | 0.0% → 0.0% | – | momentum -0.20 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.00 | **ENTG**<br><small>Entegris</small> | 149.18 USD | +16% | -7.5% | +65% | +9% | 51 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.09 |
| 🔴🔴 Strong Sell | -1.03 | **AMD**<br><small>Advanced Micro Devices</small> | 559.01 USD | +11% | -9.9% | +140% | +38% | 50 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.17 | **SMIC**<br><small>0981.HK</small> | 45.34 HKD | +112% | +17.3% | -14% | -34% | 17 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.25 | **SNPS**<br><small>Synopsys</small> | 474.92 USD | +20% | -6.4% | -10% | +7% | 57 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.27 |
| 🔴🔴 Strong Sell | -1.33 | **CDNS**<br><small>Cadence Design Systems</small> | 348.62 USD | +16% | -7.3% | -5% | +7% | 60 | +0.31 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.35 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.33"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,346,000 KRW (+133%, 38 analysts); de-biased α +20.9% vs CAPM hurdle 14.3%. Downtrend -9% vs 200-day avg; 12-1 mom +337%; RSI 39. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.15"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 929.56 USD (+64%, 46 analysts); de-biased α +3.5% vs CAPM hurdle 14.0%. Uptrend +26% vs 200-day avg; 12-1 mom +382%; RSI 46. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.38"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 222,500 KRW (+115%, 36 analysts); de-biased α +17.1% vs CAPM hurdle 11.3%. Downtrend -6% vs 200-day avg; 12-1 mom +193%; RSI 41. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.59"
    Within rebalance band of target 7.6%: no trade. Analyst target 638.94 USD vs 396.66 USD (+61%, 36 analysts); de-biased α +3.6% vs CAPM hurdle 11.6%. Downtrend -10% vs 200-day avg; 12-1 mom +114%; RSI 34. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.51"
    Within rebalance band of target 7.2%: no trade. Analyst target 51.00 USD vs 41.71 USD (+22%, 1 analysts); de-biased α -3.0% vs CAPM hurdle 11.9%. Uptrend +27% vs 200-day avg; 12-1 mom +241%; RSI 49. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Tokyo Electron (8035.T) — 🟢 Buy, score +0.49"
    **ADD 400 sh** → target 6.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 15,275 JPY vs 9,343 JPY (+63%, 23 analysts); de-biased α +4.1% vs CAPM hurdle 12.8%. Downtrend -7% vs 200-day avg; 12-1 mom +95%; RSI 35. Quality z -0.28 (ROE 29%).

??? success "TSM (TSM) — 🟢 Buy, score +0.40"
    Within rebalance band of target 7.3%: no trade. Analyst target 552.26 USD vs 436.63 USD (+26%, 20 analysts); de-biased α -4.8% vs CAPM hurdle 10.8%. Uptrend +10% vs 200-day avg; 12-1 mom +55%; RSI 51. Quality z +0.58 (ROE 35%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.39"
    Within rebalance band of target 4.0%: no trade. Analyst target 42,686 JPY vs 34,040 JPY (+25%, 21 analysts); de-biased α -5.8% vs CAPM hurdle 13.4%. Uptrend +18% vs 200-day avg; 12-1 mom +91%; RSI 47. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.37"
    **TRIM 434 sh** → target 5.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 52.85 EUR (+64%, 23 analysts); de-biased α +3.8% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +66%; RSI 44. Quality z -0.04 (ROE 6%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.25"
    Within rebalance band of target 3.8%: no trade. Analyst target 327.70 USD vs 218.07 USD (+50%, 59 analysts); de-biased α +0.3% vs CAPM hurdle 13.9%. Uptrend +7% vs 200-day avg; 12-1 mom +23%; RSI 46. Quality z +0.47 (ROE 101%).

??? note "ASML (ASML) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,636.57 USD (+28%, 16 analysts); de-biased α -4.8% vs CAPM hurdle 12.3%. Uptrend +3% vs 200-day avg; 12-1 mom +73%; RSI 44. Quality z +0.42 (ROE 50%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.21"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 240.56 USD (+56%, 31 analysts); de-biased α +2.0% vs CAPM hurdle 12.6%. Downtrend -15% vs 200-day avg; 12-1 mom +108%; RSI 31. Quality z +0.02 (ROE 65%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.16"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 153.05 USD (+53%, 26 analysts); de-biased α +1.6% vs CAPM hurdle 11.1%. Downtrend -16% vs 200-day avg; 12-1 mom +61%; RSI 32. Quality z +0.51 (ROE 87%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.15"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 242.40 USD (+21%, 43 analysts); de-biased α -7.1% vs CAPM hurdle 14.1%. Uptrend +34% vs 200-day avg; 12-1 mom +200%; RSI 48. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "Disco (6146.T) — ⚪ Hold, score -0.02"
    Hold zone: not owned, no entry. Analyst target 81,730 JPY vs 49,830 JPY (+64%, 20 analysts); de-biased α +4.5% vs CAPM hurdle 11.5%. Downtrend -24% vs 200-day avg; 12-1 mom +2%; RSI 37. Quality z +0.06 (ROE 25%).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.11"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 343.48 USD (+55%, 47 analysts); de-biased α +2.2% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom -1%; RSI 48. Quality z +0.26 (ROE 31%).

??? note "TER (TER) — ⚪ Hold, score -0.13"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 325.84 USD (+37%, 15 analysts); de-biased α -2.6% vs CAPM hurdle 12.3%. Downtrend -6% vs 200-day avg; 12-1 mom +179%; RSI 40. Quality z -0.31 (ROE 20%).

??? note "INTC (INTC) — ⚪ Hold, score -0.15"
    Hold zone: not owned, no entry. Analyst target 116.37 USD vs 93.80 USD (+24%, 43 analysts); de-biased α -6.3% vs CAPM hurdle 14.0%. Uptrend +9% vs 200-day avg; 12-1 mom +203%; RSI 43. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "GFS (GFS) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 76.00 USD vs 46.63 USD (+63%, 22 analysts); de-biased α +3.9% vs CAPM hurdle 12.4%. Downtrend -15% vs 200-day avg; 12-1 mom +36%; RSI 49. Quality z -0.21 (ROE 8%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.48"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 744.60 EUR (+52%, 19 analysts); de-biased α +0.8% vs CAPM hurdle 13.2%. Downtrend -8% vs 200-day avg; 12-1 mom +50%; RSI 40. Quality z -0.10 (ROE 19%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 76.40 USD vs 38.74 USD (+97%, 10 analysts); de-biased α +12.1% vs CAPM hurdle 14.0%. Downtrend -32% vs 200-day avg; 12-1 mom +63%; RSI 33. Quality z -1.00 (ROE 9%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.63"
    Avoid: not owned. Analyst target 194.13 USD vs 181.10 USD (+7%, 30 analysts); de-biased α -9.5% vs CAPM hurdle 11.9%. Uptrend +8% vs 200-day avg; 12-1 mom +13%; RSI 53. Quality z +0.70 (ROE 23%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.65"
    Avoid: not owned. Analyst target 288.70 USD vs 226.70 USD (+27%, 40 analysts); de-biased α -6.9% vs CAPM hurdle 19.6%. Downtrend -0% vs 200-day avg; 12-1 mom +66%; RSI 40. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.84"
    Avoid: not owned. Analyst target 324.71 USD vs 306.64 USD (+6%, 31 analysts); de-biased α -9.6% vs CAPM hurdle 10.8%. Uptrend +20% vs 200-day avg; 12-1 mom +69%; RSI 69. Quality z +0.24 (ROE 30%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.98"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,870 JPY (+32%, 17 analysts); de-biased α -3.1% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +18%; RSI 46. Quality z -0.20 (ROE 10%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.00"
    Avoid: not owned. Analyst target 173.36 USD vs 149.18 USD (+16%, 11 analysts); de-biased α -7.5% vs CAPM hurdle 11.0%. Uptrend +9% vs 200-day avg; 12-1 mom +65%; RSI 51. Quality z -0.02 (ROE 6%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.03"
    Avoid: not owned. Analyst target 619.51 USD vs 559.01 USD (+11%, 50 analysts); de-biased α -9.9% vs CAPM hurdle 14.9%. Uptrend +38% vs 200-day avg; 12-1 mom +140%; RSI 50. Quality z -0.15 (ROE 7%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.17"
    Avoid: not owned. Analyst target 95.99 HKD vs 45.34 HKD (+112%, 21 analysts); de-biased α +17.3% vs CAPM hurdle 7.3%. Downtrend -34% vs 200-day avg; 12-1 mom -14%; RSI 17. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.25"
    Avoid: not owned. Analyst target 569.78 USD vs 474.92 USD (+20%, 26 analysts); de-biased α -6.4% vs CAPM hurdle 10.3%. Uptrend +7% vs 200-day avg; 12-1 mom -10%; RSI 57. Quality z +0.14 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.33"
    Avoid: not owned. Analyst target 405.47 USD vs 348.62 USD (+16%, 26 analysts); de-biased α -7.3% vs CAPM hurdle 10.0%. Uptrend +7% vs 200-day avg; 12-1 mom -5%; RSI 60. Quality z +0.31 (ROE 22%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,346,000 KRW | $99,471 | 10.9% | Strong Buy |
| MU | Micron Technology | 92 | 929.56 USD | $85,520 | 9.4% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 222,500 KRW | $81,376 | 8.9% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 52.85 EUR | $76,636 | 8.4% | Buy |
| AMAT | Applied Materials | 145 | 396.66 USD | $57,516 | 6.3% | Buy |
| TSM | TSMC | 127 | 436.63 USD | $55,452 | 6.1% | Buy |
| ASX | ASE Technology | 1,320 | 41.71 USD | $55,057 | 6.0% | Buy |
| ASML | ASML Holding | 30 | 1,636.57 USD | $49,097 | 5.4% | Hold |
| 6857.T | Advantest | 200 | 34,040 JPY | $43,125 | 4.7% | Buy |
| KLAC | KLA Corp | 268 | 153.05 USD | $41,017 | 4.5% | Hold |
| LRCX | Lam Research | 162 | 240.56 USD | $38,971 | 4.3% | Hold |
| NVDA | NVIDIA | 168 | 218.07 USD | $36,636 | 4.0% | Buy |
| AVGO | Broadcom | 100 | 343.48 USD | $34,348 | 3.8% | Hold |
| 8035.T | Tokyo Electron | 500 | 9,343 JPY | $29,592 | 3.2% | Buy |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 35.4%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
