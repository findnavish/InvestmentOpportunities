---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-23 19:14 UTC (Fri Oct 23, 03:14 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Fri 15:14) · Tokyo 🔴 closed (Sat 04:14) · Korea 🔴 closed (Sat 04:14) · Hong Kong 🔴 closed (Sat 03:14) · Xetra 🔴 closed (Fri 21:14) · Euronext Amsterdam 🔴 closed (Fri 21:14)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$870,264** | $96,021 (11%) | $774,244 (89%) | -12.97% | -15.27% | 🟢 Risk-on (+1.6%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $870,264), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **KLAC**<br><small>KLA Corp</small> | 57 | 145.30 USD | $8,282 | Executed (paper) | quality +0.24 · trend -0.18 · ⚠️ oversold |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.23 | **SK hynix**<br><small>000660.KS</small> | 1,269,000 KRW | +148% | +22.7% | +355% | -14% | 33 | +0.62 | 10.8% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.47 | **MU**<br><small>Micron Technology</small> | 878.05 USD | +73% | +4.2% | +445% | +20% | 38 | +0.12 | 9.3% → 10.0% | – | momentum +0.53 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.48 | **Samsung**<br><small>005930.KS</small> | 214,000 KRW | +123% | +17.5% | +202% | -9% | 35 | -0.26 | 9.0% → 10.0% | – | analyst α +0.66 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.66 | **AMAT**<br><small>Applied Materials</small> | 378.67 USD | +69% | +3.8% | +116% | -14% | 27 | +0.03 | 8.8% → 8.8% | – | analyst α +0.27 · momentum +0.12 · ⚠️ oversold |
| 🟢 Buy | +0.52 | **Infineon**<br><small>IFX.DE</small> | 48.52 EUR | +79% | +5.7% | +69% | -15% | 31 | -0.04 | 8.1% → 8.0% | – | analyst α +0.41 · trend -0.12 |
| 🟢 Buy | +0.49 | **ASX**<br><small>ASE Technology</small> | 38.69 USD | +32% | -2.7% | +253% | +19% | 40 | -0.68 | 7.6% → 7.2% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.38 | **TSM**<br><small>TSMC</small> | 418.09 USD | +32% | -5.1% | +58% | +6% | 41 | +0.58 | 6.1% → 7.2% | – | quality +0.28 · analyst α -0.12 |
| 🟢 Buy | +0.33 | **LRCX**<br><small>Lam Research</small> | 229.85 USD | +63% | +2.1% | +118% | -19% | 25 | +0.02 | 4.3% → 4.7% | – | analyst α +0.15 · momentum +0.14 · ⚠️ oversold |
| 🟢 Buy | +0.31 | **KLAC**<br><small>KLA Corp</small> | 145.30 USD | +61% | +1.9% | +69% | -20% | 23 | +0.51 | 4.5% → 4.5% | ADD 57 | quality +0.24 · trend -0.18 · ⚠️ oversold |
| 🟢 Buy | +0.30 | **NVDA**<br><small>NVIDIA</small> | 211.96 USD | +55% | -0.4% | +25% | +4% | 39 | +0.47 | 5.5% → 4.7% | – | quality +0.21 · momentum -0.17 |
| ⚪ Hold | +0.16 | **Advantest**<br><small>6857.T</small> | 32,360 JPY | +32% | -5.9% | +84% | +13% | 39 | +0.33 | 2.4% → 2.4% | – | analyst α -0.31 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.12 | **ASML**<br><small>ASML Holding</small> | 1,571.76 USD | +33% | -5.2% | +71% | -1% | 35 | +0.42 | 5.4% → 5.4% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | -0.02 | **AVGO**<br><small>Broadcom</small> | 323.67 USD | +64% | +2.8% | +4% | -12% | 35 | +0.26 | 3.7% → 3.7% | – | momentum -0.26 · analyst α +0.19 |
| ⚪ Hold | -0.10 | **MRVL**<br><small>Marvell Technology</small> | 228.57 USD | +29% | -7.0% | +220% | +27% | 41 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · momentum +0.26 · ⚠️ rich valuation |
| ⚪ Hold | -0.15 | **Tokyo Electron**<br><small>8035.T</small> | 9,519 JPY | +60% | +1.6% | +83% | -5% | 35 | -0.28 | 3.5% → 3.5% | – | quality -0.18 · momentum +0.05 |
| ⚪ Hold | -0.21 | **INTC**<br><small>Intel</small> | 86.67 USD | +34% | -5.5% | +245% | +1% | 32 | -0.62 | 0.0% → 0.0% | – | momentum +0.30 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| ⚪ Hold | -0.23 | **TER**<br><small>Teradyne</small> | 311.73 USD | +43% | -2.8% | +180% | -10% | 34 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.26 | **GFS**<br><small>GlobalFoundries</small> | 44.38 USD | +71% | +4.2% | +37% | -19% | 41 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.16 |
| 🔴 Sell | -0.35 | **AMKR**<br><small>Amkor Technology</small> | 39.52 USD | +93% | +9.4% | +72% | -31% | 31 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.42 | **ASMI**<br><small>ASM.AS</small> | 692.60 EUR | +63% | +1.9% | +50% | -15% | 29 | -0.10 | 0.0% → 0.0% | – | momentum -0.12 · trend -0.10 · ⚠️ oversold |
| 🔴 Sell | -0.50 | **Disco**<br><small>6146.T</small> | 49,290 JPY | +66% | +3.2% | +1% | -25% | 34 | +0.06 | 0.0% → 0.0% | – | momentum -0.30 · analyst α +0.23 |
| 🔴 Sell | -0.57 | **AMD**<br><small>Advanced Micro Devices</small> | 517.30 USD | +20% | -9.4% | +173% | +29% | 39 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.64 | **ARM**<br><small>Arm Holdings</small> | 211.09 USD | +37% | -6.3% | +85% | -7% | 32 | +0.04 | 0.0% → 0.0% | – | analyst α -0.41 · momentum +0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.64 | **ENTG**<br><small>Entegris</small> | 133.52 USD | +30% | -5.8% | +68% | -2% | 39 | -0.02 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.05 |
| 🔴🔴 Strong Sell | -0.84 | **TXN**<br><small>Texas Instruments</small> | 284.87 USD | +14% | -9.3% | +63% | +12% | 55 | +0.24 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.14 |
| 🔴🔴 Strong Sell | -0.94 | **Shin-Etsu**<br><small>4063.T</small> | 5,826 JPY | +33% | -4.6% | +16% | -7% | 42 | -0.20 | 0.0% → 0.0% | – | momentum -0.23 · quality -0.11 |
| 🔴🔴 Strong Sell | -0.97 | **SNPS**<br><small>Synopsys</small> | 430.67 USD | +32% | -5.1% | -6% | -3% | 43 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -1.11 | **QCOM**<br><small>Qualcomm</small> | 175.71 USD | +10% | -10.5% | +17% | +5% | 48 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.18 | **CDNS**<br><small>Cadence Design Systems</small> | 316.53 USD | +28% | -6.1% | -3% | -3% | 45 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.33 | **SMIC**<br><small>0981.HK</small> | 47.06 HKD | +104% | +13.6% | -12% | -31% | 19 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 · ⚠️ oversold |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.23"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,269,000 KRW (+148%, 38 analysts); de-biased α +22.7% vs CAPM hurdle 14.3%. Downtrend -14% vs 200-day avg; 12-1 mom +355%; RSI 33. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.47"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 878.05 USD (+73%, 46 analysts); de-biased α +4.2% vs CAPM hurdle 14.0%. Uptrend +20% vs 200-day avg; 12-1 mom +445%; RSI 38. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.48"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 214,000 KRW (+123%, 36 analysts); de-biased α +17.5% vs CAPM hurdle 11.3%. Downtrend -9% vs 200-day avg; 12-1 mom +202%; RSI 35. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.66"
    Within rebalance band of target 8.8%: no trade. Analyst target 638.94 USD vs 378.67 USD (+69%, 36 analysts); de-biased α +3.8% vs CAPM hurdle 11.6%. Downtrend -14% vs 200-day avg; 12-1 mom +116%; RSI 27. Quality z +0.03 (ROE 36%). ⚠️ oversold.

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.52"
    Within rebalance band of target 8.0%: no trade. Analyst target 86.74 EUR vs 48.52 EUR (+79%, 23 analysts); de-biased α +5.7% vs CAPM hurdle 14.1%. Downtrend -15% vs 200-day avg; 12-1 mom +69%; RSI 31. Quality z -0.04 (ROE 6%).

??? success "ASX (ASX) — 🟢 Buy, score +0.49"
    Within rebalance band of target 7.2%: no trade. Analyst target 51.00 USD vs 38.69 USD (+32%, 1 analysts); de-biased α -2.7% vs CAPM hurdle 11.9%. Uptrend +19% vs 200-day avg; 12-1 mom +253%; RSI 40. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.38"
    Within rebalance band of target 7.2%: no trade. Analyst target 552.26 USD vs 418.09 USD (+32%, 20 analysts); de-biased α -5.1% vs CAPM hurdle 10.8%. Uptrend +6% vs 200-day avg; 12-1 mom +58%; RSI 41. Quality z +0.58 (ROE 35%).

??? success "LRCX (LRCX) — 🟢 Buy, score +0.33"
    Within rebalance band of target 4.7%: no trade. Analyst target 375.06 USD vs 229.85 USD (+63%, 31 analysts); de-biased α +2.1% vs CAPM hurdle 12.6%. Downtrend -19% vs 200-day avg; 12-1 mom +118%; RSI 25. Quality z +0.02 (ROE 65%). ⚠️ oversold.

??? success "KLAC (KLAC) — 🟢 Buy, score +0.31"
    **ADD 57 sh** → target 4.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 233.77 USD vs 145.30 USD (+61%, 26 analysts); de-biased α +1.9% vs CAPM hurdle 11.1%. Downtrend -20% vs 200-day avg; 12-1 mom +69%; RSI 23. Quality z +0.51 (ROE 87%). ⚠️ oversold.

??? success "NVDA (NVDA) — 🟢 Buy, score +0.30"
    Within rebalance band of target 4.7%: no trade. Analyst target 327.70 USD vs 211.96 USD (+55%, 59 analysts); de-biased α -0.4% vs CAPM hurdle 13.9%. Uptrend +4% vs 200-day avg; 12-1 mom +25%; RSI 39. Quality z +0.47 (ROE 101%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.16"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 32,360 JPY (+32%, 21 analysts); de-biased α -5.9% vs CAPM hurdle 13.4%. Uptrend +13% vs 200-day avg; 12-1 mom +84%; RSI 39. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score +0.12"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,571.76 USD (+33%, 16 analysts); de-biased α -5.2% vs CAPM hurdle 12.3%. Downtrend -1% vs 200-day avg; 12-1 mom +71%; RSI 35. Quality z +0.42 (ROE 50%).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.02"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 323.67 USD (+64%, 47 analysts); de-biased α +2.8% vs CAPM hurdle 11.2%. Downtrend -12% vs 200-day avg; 12-1 mom +4%; RSI 35. Quality z +0.26 (ROE 31%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 228.57 USD (+29%, 43 analysts); de-biased α -7.0% vs CAPM hurdle 14.1%. Uptrend +27% vs 200-day avg; 12-1 mom +220%; RSI 41. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score -0.15"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 9,519 JPY (+60%, 23 analysts); de-biased α +1.6% vs CAPM hurdle 12.8%. Downtrend -5% vs 200-day avg; 12-1 mom +83%; RSI 35. Quality z -0.28 (ROE 29%).

??? note "INTC (INTC) — ⚪ Hold, score -0.21"
    Hold zone: not owned, no entry. Analyst target 116.37 USD vs 86.67 USD (+34%, 43 analysts); de-biased α -5.5% vs CAPM hurdle 14.0%. Uptrend +1% vs 200-day avg; 12-1 mom +245%; RSI 32. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? note "TER (TER) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 311.73 USD (+43%, 15 analysts); de-biased α -2.8% vs CAPM hurdle 12.3%. Downtrend -10% vs 200-day avg; 12-1 mom +180%; RSI 34. Quality z -0.31 (ROE 20%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.26"
    Avoid: not owned. Analyst target 76.00 USD vs 44.38 USD (+71%, 22 analysts); de-biased α +4.2% vs CAPM hurdle 12.4%. Downtrend -19% vs 200-day avg; 12-1 mom +37%; RSI 41. Quality z -0.21 (ROE 8%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 76.40 USD vs 39.52 USD (+93%, 10 analysts); de-biased α +9.4% vs CAPM hurdle 14.0%. Downtrend -31% vs 200-day avg; 12-1 mom +72%; RSI 31. Quality z -1.00 (ROE 9%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.42"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 692.60 EUR (+63%, 19 analysts); de-biased α +1.9% vs CAPM hurdle 13.2%. Downtrend -15% vs 200-day avg; 12-1 mom +50%; RSI 29. Quality z -0.10 (ROE 19%). ⚠️ oversold.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 81,730 JPY vs 49,290 JPY (+66%, 20 analysts); de-biased α +3.2% vs CAPM hurdle 11.5%. Downtrend -25% vs 200-day avg; 12-1 mom +1%; RSI 34. Quality z +0.06 (ROE 25%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 619.51 USD vs 517.30 USD (+20%, 50 analysts); de-biased α -9.4% vs CAPM hurdle 14.9%. Uptrend +29% vs 200-day avg; 12-1 mom +173%; RSI 39. Quality z -0.15 (ROE 7%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 288.70 USD vs 211.09 USD (+37%, 40 analysts); de-biased α -6.3% vs CAPM hurdle 19.6%. Downtrend -7% vs 200-day avg; 12-1 mom +85%; RSI 32. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 173.36 USD vs 133.52 USD (+30%, 11 analysts); de-biased α -5.8% vs CAPM hurdle 11.0%. Downtrend -2% vs 200-day avg; 12-1 mom +68%; RSI 39. Quality z -0.02 (ROE 6%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.84"
    Avoid: not owned. Analyst target 324.71 USD vs 284.87 USD (+14%, 31 analysts); de-biased α -9.3% vs CAPM hurdle 10.8%. Uptrend +12% vs 200-day avg; 12-1 mom +63%; RSI 55. Quality z +0.24 (ROE 30%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,826 JPY (+33%, 17 analysts); de-biased α -4.6% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +16%; RSI 42. Quality z -0.20 (ROE 10%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.97"
    Avoid: not owned. Analyst target 569.78 USD vs 430.67 USD (+32%, 26 analysts); de-biased α -5.1% vs CAPM hurdle 10.3%. Downtrend -3% vs 200-day avg; 12-1 mom -6%; RSI 43. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.11"
    Avoid: not owned. Analyst target 194.13 USD vs 175.71 USD (+10%, 30 analysts); de-biased α -10.5% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +17%; RSI 48. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.18"
    Avoid: not owned. Analyst target 405.47 USD vs 316.53 USD (+28%, 26 analysts); de-biased α -6.1% vs CAPM hurdle 10.0%. Downtrend -3% vs 200-day avg; 12-1 mom -3%; RSI 45. Quality z +0.31 (ROE 22%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.33"
    Avoid: not owned. Analyst target 95.99 HKD vs 47.06 HKD (+104%, 21 analysts); de-biased α +13.6% vs CAPM hurdle 7.3%. Downtrend -31% vs 200-day avg; 12-1 mom -12%; RSI 19. Quality z -0.99 (ROE 3%). ⚠️ oversold.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,269,000 KRW | $93,890 | 10.8% | Strong Buy |
| MU | Micron Technology | 92 | 878.05 USD | $80,781 | 9.3% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 214,000 KRW | $78,359 | 9.0% | Strong Buy |
| AMAT | Applied Materials | 202 | 378.67 USD | $76,491 | 8.8% | Buy |
| IFX.DE | Infineon Technologies | 1,301 | 48.52 EUR | $70,688 | 8.1% | Buy |
| ASX | ASE Technology | 1,715 | 38.69 USD | $66,362 | 7.6% | Buy |
| TSM | TSMC | 127 | 418.09 USD | $53,098 | 6.1% | Buy |
| NVDA | NVIDIA | 226 | 211.96 USD | $47,903 | 5.5% | Buy |
| ASML | ASML Holding | 30 | 1,571.76 USD | $47,153 | 5.4% | Hold |
| KLAC | KLA Corp | 268 | 145.30 USD | $38,942 | 4.5% | Buy |
| LRCX | Lam Research | 162 | 229.85 USD | $37,236 | 4.3% | Buy |
| AVGO | Broadcom | 100 | 323.67 USD | $32,367 | 3.7% | Hold |
| 8035.T | Tokyo Electron | 500 | 9,519 JPY | $30,344 | 3.5% | Hold |
| 6857.T | Advantest | 100 | 32,360 JPY | $20,631 | 2.4% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-10-14 00:21 UTC | SELL (exit) | 6857.T | -200 | 40,990.00 | $51,779 |
| 2026-10-13 16:00 UTC | BUY (new) | ASML | 30 | 1,699.05 | $50,972 |
| 2026-10-13 16:00 UTC | TRIM | AMAT | -45 | 464.47 | $20,901 |
| 2026-10-13 16:00 UTC | TRIM | ASX | -609 | 47.11 | $28,690 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 42.4%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
