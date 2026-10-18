---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-18 23:14 UTC (Sun Oct 18, 07:14 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Sun 19:14) · Tokyo 🔴 closed (Mon 08:14) · Korea 🔴 closed (Mon 08:14) · Hong Kong 🔴 closed (Mon 07:14) · Xetra 🔴 closed (Mon 01:14) · Euronext Amsterdam 🔴 closed (Mon 01:14)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$897,423** | $92,397 (10%) | $805,026 (90%) | -10.26% | -12.80% | 🟢 Risk-on (+5.5%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $897,423), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **MRVL**<br><small>Marvell Technology</small> | 98 | 227.76 USD | $22,320 | Queued · NYSE/Nasdaq closed | analyst α -0.27 · trend +0.25 · ⚠️ rich valuation |
| TRIM | **TSM**<br><small>TSMC</small> | 24 | 412.51 USD | $9,900 | Queued · NYSE/Nasdaq closed | quality +0.28 · momentum -0.12 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.02 | **SK hynix**<br><small>000660.KS</small> | 1,284,000 KRW | +145% | +23.7% | +390% | -12% | 27 | +0.62 | 10.5% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ oversold, cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.49 | **MU**<br><small>Micron Technology</small> | 878.67 USD | +73% | +5.9% | +402% | +22% | 34 | +0.12 | 9.0% → 10.0% | – | momentum +0.53 · analyst α +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.56 | **Samsung**<br><small>005930.KS</small> | 217,500 KRW | +120% | +18.3% | +199% | -6% | 33 | -0.26 | 8.8% → 10.0% | – | analyst α +0.66 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.59 | **NVDA**<br><small>NVIDIA</small> | 214.14 USD | +53% | +0.9% | +23% | +6% | 38 | +0.47 | 8.9% → 8.6% | – | quality +0.21 · momentum -0.17 |
| 🟢 Buy | +0.55 | **ASX**<br><small>ASE Technology</small> | 39.53 USD | +29% | -2.2% | +234% | +23% | 39 | -0.68 | 7.9% → 7.5% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.52 | **Infineon**<br><small>IFX.DE</small> | 52.35 EUR | +66% | +4.2% | +65% | -8% | 36 | -0.04 | 8.5% → 7.6% | – | analyst α +0.36 · trend -0.10 |
| 🟢 Buy | +0.48 | **AMAT**<br><small>Applied Materials</small> | 409.29 USD | +56% | +2.4% | +84% | -7% | 29 | +0.03 | 7.1% → 5.9% | – | analyst α +0.23 · trend -0.09 · ⚠️ oversold |
| 🟢 Buy | +0.38 | **KLAC**<br><small>KLA Corp</small> | 165.75 USD | +41% | -1.3% | +62% | -8% | 31 | +0.51 | 5.2% → 5.2% | – | quality +0.24 · trend -0.12 |
| 🟢 Buy | +0.30 | **TSM**<br><small>TSMC</small> | 412.51 USD | +34% | -2.9% | +47% | +5% | 34 | +0.58 | 6.5% → 5.4% | TRIM 24 | quality +0.28 · momentum -0.12 |
| 🟢 Buy | +0.26 | **MRVL**<br><small>Marvell Technology</small> | 227.76 USD | +29% | -5.1% | +177% | +29% | 38 | -0.12 | 0.0% → 2.5% | BUY 98 | analyst α -0.27 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | +0.25 | **Tokyo Electron**<br><small>8035.T</small> | 10,570 JPY | +45% | -0.7% | +85% | +6% | 43 | -0.28 | 4.5% → 4.5% | – | quality -0.18 · trend +0.12 |
| ⚪ Hold | +0.21 | **ASML**<br><small>ASML Holding</small> | 1,641.20 USD | +28% | -4.9% | +66% | +4% | 38 | +0.42 | 5.5% → 5.5% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.12 | **LRCX**<br><small>Lam Research</small> | 263.87 USD | +42% | -1.4% | +103% | -6% | 30 | +0.02 | 0.0% → 0.0% | – | momentum +0.12 · trend -0.07 |
| ⚪ Hold | +0.09 | **Advantest**<br><small>6857.T</small> | 34,480 JPY | +24% | -6.2% | +107% | +22% | 44 | +0.33 | 2.4% → 2.4% | – | analyst α -0.41 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.07 | **AVGO**<br><small>Broadcom</small> | 328.81 USD | +62% | +3.9% | +2% | -10% | 35 | +0.26 | 4.9% → 4.9% | – | analyst α +0.31 · momentum -0.26 |
| ⚪ Hold | -0.17 | **ASMI**<br><small>ASM.AS</small> | 758.60 EUR | +49% | +0.1% | +53% | -6% | 34 | -0.10 | 0.0% → 0.0% | – | analyst α +0.12 · momentum -0.10 |
| ⚪ Hold | -0.20 | **TER**<br><small>Teradyne</small> | 325.04 USD | +37% | -2.6% | +167% | -6% | 33 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| ⚪ Hold | -0.23 | **INTC**<br><small>Intel</small> | 89.76 USD | +30% | -5.0% | +195% | +6% | 31 | -0.62 | 0.0% → 0.0% | – | momentum +0.26 · quality -0.24 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.39 | **GFS**<br><small>GlobalFoundries</small> | 46.71 USD | +63% | +3.8% | +39% | -15% | 46 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.18 |
| 🔴 Sell | -0.57 | **Disco**<br><small>6146.T</small> | 53,760 JPY | +52% | +1.5% | +1% | -18% | 41 | +0.06 | 0.0% → 0.0% | – | momentum -0.30 · trend -0.21 |
| 🔴 Sell | -0.63 | **AMKR**<br><small>Amkor Technology</small> | 41.83 USD | +83% | +8.5% | +61% | -27% | 30 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.67 | **TXN**<br><small>Texas Instruments</small> | 276.55 USD | +17% | -6.7% | +56% | +9% | 48 | +0.24 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.14 |
| 🔴🔴 Strong Sell | -0.86 | **ENTG**<br><small>Entegris</small> | 138.68 USD | +25% | -5.3% | +58% | +2% | 38 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.05 |
| 🔴🔴 Strong Sell | -0.87 | **QCOM**<br><small>Qualcomm</small> | 172.04 USD | +13% | -8.1% | +11% | +2% | 43 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.92 | **CDNS**<br><small>Cadence Design Systems</small> | 319.62 USD | +27% | -4.6% | -13% | -2% | 44 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -0.94 | **Shin-Etsu**<br><small>4063.T</small> | 6,002 JPY | +29% | -3.8% | +19% | -4% | 49 | -0.20 | 0.0% → 0.0% | – | momentum -0.20 · analyst α -0.12 |
| 🔴🔴 Strong Sell | -0.97 | **AMD**<br><small>Advanced Micro Devices</small> | 528.75 USD | +17% | -8.3% | +128% | +34% | 38 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.12 | **ARM**<br><small>Arm Holdings</small> | 227.75 USD | +27% | -7.1% | +61% | +2% | 34 | +0.04 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.03 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.17 | **SMIC**<br><small>0981.HK</small> | 52.40 HKD | +83% | +10.1% | -29% | -24% | 25 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.19 | **SNPS**<br><small>Synopsys</small> | 454.79 USD | +25% | -5.1% | -13% | +2% | 50 | +0.14 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.31 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.02"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,284,000 KRW (+145%, 38 analysts); de-biased α +23.7% vs CAPM hurdle 14.3%. Downtrend -12% vs 200-day avg; 12-1 mom +390%; RSI 27. Quality z +0.62 (ROE 44%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.49"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 878.67 USD (+73%, 46 analysts); de-biased α +5.9% vs CAPM hurdle 14.0%. Uptrend +22% vs 200-day avg; 12-1 mom +402%; RSI 34. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.56"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 217,500 KRW (+120%, 36 analysts); de-biased α +18.3% vs CAPM hurdle 11.3%. Downtrend -6% vs 200-day avg; 12-1 mom +199%; RSI 33. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.59"
    Within rebalance band of target 8.6%: no trade. Analyst target 327.70 USD vs 214.14 USD (+53%, 59 analysts); de-biased α +0.9% vs CAPM hurdle 13.9%. Uptrend +6% vs 200-day avg; 12-1 mom +23%; RSI 38. Quality z +0.47 (ROE 101%).

??? success "ASX (ASX) — 🟢 Buy, score +0.55"
    Within rebalance band of target 7.5%: no trade. Analyst target 51.00 USD vs 39.53 USD (+29%, 1 analysts); de-biased α -2.2% vs CAPM hurdle 11.9%. Uptrend +23% vs 200-day avg; 12-1 mom +234%; RSI 39. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.52"
    Within rebalance band of target 7.6%: no trade. Analyst target 86.74 EUR vs 52.35 EUR (+66%, 23 analysts); de-biased α +4.2% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +65%; RSI 36. Quality z -0.04 (ROE 6%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.48"
    Within rebalance band of target 5.9%: no trade. Analyst target 638.94 USD vs 409.29 USD (+56%, 36 analysts); de-biased α +2.4% vs CAPM hurdle 11.6%. Downtrend -7% vs 200-day avg; 12-1 mom +84%; RSI 29. Quality z +0.03 (ROE 36%). ⚠️ oversold.

??? success "KLAC (KLAC) — 🟢 Buy, score +0.38"
    Within rebalance band of target 5.2%: no trade. Analyst target 233.77 USD vs 165.75 USD (+41%, 26 analysts); de-biased α -1.3% vs CAPM hurdle 11.1%. Downtrend -8% vs 200-day avg; 12-1 mom +62%; RSI 31. Quality z +0.51 (ROE 87%).

??? success "TSM (TSM) — 🟢 Buy, score +0.30"
    **TRIM 24 sh** → target 5.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 412.51 USD (+34%, 20 analysts); de-biased α -2.9% vs CAPM hurdle 10.8%. Uptrend +5% vs 200-day avg; 12-1 mom +47%; RSI 34. Quality z +0.58 (ROE 35%).

??? success "MRVL (MRVL) — 🟢 Buy, score +0.26"
    **BUY (new) 98 sh** → target 2.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 227.76 USD (+29%, 43 analysts); de-biased α -5.1% vs CAPM hurdle 14.1%. Uptrend +29% vs 200-day avg; 12-1 mom +177%; RSI 38. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.25"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 10,570 JPY (+45%, 23 analysts); de-biased α -0.7% vs CAPM hurdle 12.8%. Uptrend +6% vs 200-day avg; 12-1 mom +85%; RSI 43. Quality z -0.28 (ROE 29%).

??? note "ASML (ASML) — ⚪ Hold, score +0.21"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,641.20 USD (+28%, 16 analysts); de-biased α -4.9% vs CAPM hurdle 12.3%. Uptrend +4% vs 200-day avg; 12-1 mom +66%; RSI 38. Quality z +0.42 (ROE 50%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.12"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 263.87 USD (+42%, 31 analysts); de-biased α -1.4% vs CAPM hurdle 12.6%. Downtrend -6% vs 200-day avg; 12-1 mom +103%; RSI 30. Quality z +0.02 (ROE 65%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.09"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 34,480 JPY (+24%, 21 analysts); de-biased α -6.2% vs CAPM hurdle 13.4%. Uptrend +22% vs 200-day avg; 12-1 mom +107%; RSI 44. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 328.81 USD (+62%, 47 analysts); de-biased α +3.9% vs CAPM hurdle 11.2%. Downtrend -10% vs 200-day avg; 12-1 mom +2%; RSI 35. Quality z +0.26 (ROE 31%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.17"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 758.60 EUR (+49%, 19 analysts); de-biased α +0.1% vs CAPM hurdle 13.2%. Downtrend -6% vs 200-day avg; 12-1 mom +53%; RSI 34. Quality z -0.10 (ROE 19%).

??? note "TER (TER) — ⚪ Hold, score -0.20"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 325.04 USD (+37%, 15 analysts); de-biased α -2.6% vs CAPM hurdle 12.3%. Downtrend -6% vs 200-day avg; 12-1 mom +167%; RSI 33. Quality z -0.31 (ROE 20%).

??? note "INTC (INTC) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 116.37 USD vs 89.76 USD (+30%, 43 analysts); de-biased α -5.0% vs CAPM hurdle 14.0%. Uptrend +6% vs 200-day avg; 12-1 mom +195%; RSI 31. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "GFS (GFS) — 🔴 Sell, score -0.39"
    Avoid: not owned. Analyst target 76.00 USD vs 46.71 USD (+63%, 22 analysts); de-biased α +3.8% vs CAPM hurdle 12.4%. Downtrend -15% vs 200-day avg; 12-1 mom +39%; RSI 46. Quality z -0.21 (ROE 8%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 81,730 JPY vs 53,760 JPY (+52%, 20 analysts); de-biased α +1.5% vs CAPM hurdle 11.5%. Downtrend -18% vs 200-day avg; 12-1 mom +1%; RSI 41. Quality z +0.06 (ROE 25%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.63"
    Avoid: not owned. Analyst target 76.40 USD vs 41.83 USD (+83%, 10 analysts); de-biased α +8.5% vs CAPM hurdle 14.0%. Downtrend -27% vs 200-day avg; 12-1 mom +61%; RSI 30. Quality z -1.00 (ROE 9%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.67"
    Avoid: not owned. Analyst target 324.71 USD vs 276.55 USD (+17%, 31 analysts); de-biased α -6.7% vs CAPM hurdle 10.8%. Uptrend +9% vs 200-day avg; 12-1 mom +56%; RSI 48. Quality z +0.24 (ROE 30%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.86"
    Avoid: not owned. Analyst target 173.36 USD vs 138.68 USD (+25%, 11 analysts); de-biased α -5.3% vs CAPM hurdle 11.0%. Uptrend +2% vs 200-day avg; 12-1 mom +58%; RSI 38. Quality z -0.02 (ROE 6%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.87"
    Avoid: not owned. Analyst target 194.13 USD vs 172.04 USD (+13%, 30 analysts); de-biased α -8.1% vs CAPM hurdle 11.9%. Uptrend +2% vs 200-day avg; 12-1 mom +11%; RSI 43. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 405.47 USD vs 319.62 USD (+27%, 26 analysts); de-biased α -4.6% vs CAPM hurdle 10.0%. Downtrend -2% vs 200-day avg; 12-1 mom -13%; RSI 44. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,002 JPY (+29%, 17 analysts); de-biased α -3.8% vs CAPM hurdle 10.8%. Downtrend -4% vs 200-day avg; 12-1 mom +19%; RSI 49. Quality z -0.20 (ROE 10%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -0.97"
    Avoid: not owned. Analyst target 619.51 USD vs 528.75 USD (+17%, 50 analysts); de-biased α -8.3% vs CAPM hurdle 14.9%. Uptrend +34% vs 200-day avg; 12-1 mom +128%; RSI 38. Quality z -0.15 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.12"
    Avoid: not owned. Analyst target 288.70 USD vs 227.75 USD (+27%, 40 analysts); de-biased α -7.1% vs CAPM hurdle 19.6%. Uptrend +2% vs 200-day avg; 12-1 mom +61%; RSI 34. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.17"
    Avoid: not owned. Analyst target 95.99 HKD vs 52.40 HKD (+83%, 21 analysts); de-biased α +10.1% vs CAPM hurdle 7.3%. Downtrend -24% vs 200-day avg; 12-1 mom -29%; RSI 25. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.19"
    Avoid: not owned. Analyst target 569.78 USD vs 454.79 USD (+25%, 26 analysts); de-biased α -5.1% vs CAPM hurdle 10.3%. Uptrend +2% vs 200-day avg; 12-1 mom -13%; RSI 50. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,284,000 KRW | $94,303 | 10.5% | Strong Buy |
| MU | Micron Technology | 92 | 878.67 USD | $80,838 | 9.0% | Strong Buy |
| NVDA | NVIDIA | 371 | 214.14 USD | $79,446 | 8.9% | Buy |
| 005930.KS | Samsung Electronics | 485 | 217,500 KRW | $79,056 | 8.8% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 52.35 EUR | $76,388 | 8.5% | Buy |
| ASX | ASE Technology | 1,797 | 39.53 USD | $71,026 | 7.9% | Buy |
| AMAT | Applied Materials | 156 | 409.29 USD | $63,849 | 7.1% | Buy |
| TSM | TSMC | 142 | 412.51 USD | $58,576 | 6.5% | Buy |
| ASML | ASML Holding | 30 | 1,641.20 USD | $49,236 | 5.5% | Hold |
| KLAC | KLA Corp | 279 | 165.75 USD | $46,244 | 5.2% | Buy |
| AVGO | Broadcom | 134 | 328.81 USD | $44,061 | 4.9% | Hold |
| 8035.T | Tokyo Electron | 600 | 10,570 JPY | $40,166 | 4.5% | Hold |
| 6857.T | Advantest | 100 | 34,480 JPY | $21,837 | 2.4% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 35.4%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
