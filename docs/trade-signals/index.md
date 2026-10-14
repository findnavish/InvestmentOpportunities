---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-14 00:21 UTC (Tue Oct 13, 08:21 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Tue 20:21) · Tokyo 🟢 open (Wed 09:21) · Korea 🟢 open (Wed 09:21) · Hong Kong 🔴 closed (Wed 08:21) · Xetra 🔴 closed (Wed 02:21) · Euronext Amsterdam 🔴 closed (Wed 02:21)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$970,007** | $121,442 (13%) | $848,566 (87%) | -3.00% | -3.83% | 🟢 Risk-on (+17.5%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $970,007), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| SELL (exit) | **Advantest**<br><small>6857.T</small> | 200 | 40,990 JPY | $51,779 | Executed (paper) | analyst α -0.66 · trend +0.18 · ⚠️ rich valuation |
| TRIM | **Infineon**<br><small>IFX.DE</small> | 541 | 55.72 EUR | $33,779 | Queued · Xetra closed | analyst α +0.31 · trend -0.12 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.49 | **SK hynix**<br><small>000660.KS</small> | 1,472,000 KRW | +113% | +19.3% | +422% | +2% | 34 | +0.62 | 8.4% → 10.0% | – | analyst α +0.85 · momentum +0.53 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.14 | **MU**<br><small>Micron Technology</small> | 953.19 USD | +59% | +5.8% | +409% | +35% | 40 | +0.12 | 9.0% → 10.0% | – | momentum +0.41 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.54 | **Samsung**<br><small>005930.KS</small> | 234,500 KRW | +104% | +17.7% | +217% | +2% | 36 | -0.26 | 8.8% → 10.0% | – | analyst α +0.66 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.55 | **NVDA**<br><small>NVIDIA</small> | 228.52 USD | +43% | +1.9% | +15% | +13% | 52 | +0.47 | 8.7% → 9.4% | – | analyst α +0.23 · momentum -0.23 |
| 🟢 Buy | +0.51 | **KLAC**<br><small>KLA Corp</small> | 183.98 USD | +27% | -1.5% | +73% | +2% | 43 | +0.51 | 7.1% → 8.0% | – | quality +0.24 · trend -0.07 |
| 🟢 Buy | +0.48 | **TSM**<br><small>TSMC</small> | 444.99 USD | +24% | -2.0% | +50% | +14% | 48 | +0.58 | 8.6% → 9.9% | – | quality +0.28 · momentum -0.10 |
| 🟢 Buy | +0.47 | **AMAT**<br><small>Applied Materials</small> | 464.18 USD | +38% | +1.1% | +103% | +6% | 41 | +0.03 | 7.5% → 6.9% | – | analyst α +0.15 · momentum +0.07 |
| 🟢 Buy | +0.40 | **Infineon**<br><small>IFX.DE</small> | 55.72 EUR | +56% | +5.0% | +70% | -1% | 43 | -0.04 | 10.3% → 6.8% | TRIM 541 | analyst α +0.31 · trend -0.12 |
| 🟢 Buy | +0.27 | **ASX**<br><small>ASE Technology</small> | 47.61 USD | +7% | -3.3% | +238% | +51% | 65 | -0.68 | 4.4% → 4.2% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.22 | **Tokyo Electron**<br><small>8035.T</small> | 11,560 JPY | +32% | -0.4% | +104% | +17% | 51 | -0.28 | 4.5% → 4.5% | – | quality -0.18 · trend +0.10 |
| ⚪ Hold | +0.17 | **ASML**<br><small>ASML Holding</small> | 1,717.08 USD | +22% | -3.0% | +69% | +10% | 45 | +0.42 | 5.3% → 5.3% | – | quality +0.18 · analyst α -0.12 |
| ⚪ Hold | +0.12 | **LRCX**<br><small>Lam Research</small> | 301.18 USD | +25% | -2.5% | +109% | +8% | 43 | +0.02 | 0.0% → 0.0% | – | momentum +0.12 · analyst α -0.05 |
| ⚪ Hold | -0.02 | **GFS**<br><small>GlobalFoundries</small> | 46.69 USD | +63% | +7.1% | +32% | -14% | 45 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.21 |
| ⚪ Hold | -0.15 | **AVGO**<br><small>Broadcom</small> | 357.41 USD | +49% | +4.0% | +7% | -3% | 48 | +0.26 | 4.9% → 4.9% | – | momentum -0.30 · analyst α +0.27 |
| ⚪ Hold | -0.18 | **MRVL**<br><small>Marvell Technology</small> | 268.84 USD | +9% | -6.7% | +156% | +55% | 57 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | -0.23 | **ASMI**<br><small>ASM.AS</small> | 826.40 EUR | +37% | +0.4% | +39% | +3% | 42 | -0.10 | 0.0% → 0.0% | – | momentum -0.12 · analyst α +0.12 |
| ⚪ Hold | -0.25 | **QCOM**<br><small>Qualcomm</small> | 176.93 USD | +10% | -5.6% | +20% | +5% | 47 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · analyst α -0.31 |
| 🔴 Sell | -0.29 | **TXN**<br><small>Texas Instruments</small> | 287.91 USD | +13% | -4.6% | +57% | +15% | 59 | +0.24 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.10 |
| 🔴 Sell | -0.37 | **TER**<br><small>Teradyne</small> | 380.52 USD | +17% | -4.2% | +150% | +11% | 46 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.39 | **Advantest**<br><small>6857.T</small> | 40,990 JPY | +4% | -7.8% | +117% | +46% | 67 | +0.33 | 0.0% → 0.0% | SELL 200 | analyst α -0.66 · trend +0.18 · ⚠️ rich valuation |
| 🔴 Sell | -0.44 | **INTC**<br><small>Intel</small> | 102.84 USD | +13% | -5.7% | +167% | +23% | 42 | -0.62 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.44 | **Disco**<br><small>6146.T</small> | 59,030 JPY | +38% | +1.4% | +15% | -10% | 52 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.19 |
| 🔴 Sell | -0.58 | **AMKR**<br><small>Amkor Technology</small> | 47.60 USD | +61% | +6.2% | +68% | -17% | 40 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.41 |
| 🔴🔴 Strong Sell | -0.80 | **Shin-Etsu**<br><small>4063.T</small> | 6,102 JPY | +27% | -1.0% | +21% | -2% | 55 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · trend -0.14 |
| 🔴🔴 Strong Sell | -0.86 | **ENTG**<br><small>Entegris</small> | 161.25 USD | +8% | -6.3% | +54% | +20% | 59 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.12 |
| 🔴🔴 Strong Sell | -0.91 | **CDNS**<br><small>Cadence Design Systems</small> | 334.20 USD | +21% | -2.7% | -15% | +2% | 53 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.13 |
| 🔴🔴 Strong Sell | -0.99 | **AMD**<br><small>Advanced Micro Devices</small> | 605.52 USD | +2% | -8.7% | +130% | +56% | 56 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.04 | **SNPS**<br><small>Synopsys</small> | 494.64 USD | +15% | -4.3% | -13% | +11% | 67 | +0.14 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.07 | **ARM**<br><small>Arm Holdings</small> | 255.45 USD | +13% | -7.2% | +54% | +15% | 41 | +0.04 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.09 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.36 | **SMIC**<br><small>0981.HK</small> | 55.55 HKD | +73% | +10.8% | -30% | -20% | 30 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 · ⚠️ oversold |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.49"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,472,000 KRW (+113%, 38 analysts); de-biased α +19.3% vs CAPM hurdle 14.3%. Uptrend +2% vs 200-day avg; 12-1 mom +422%; RSI 34. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.14"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 953.19 USD (+59%, 46 analysts); de-biased α +5.8% vs CAPM hurdle 14.0%. Uptrend +35% vs 200-day avg; 12-1 mom +409%; RSI 40. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.54"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 234,500 KRW (+104%, 36 analysts); de-biased α +17.7% vs CAPM hurdle 11.3%. Uptrend +2% vs 200-day avg; 12-1 mom +217%; RSI 36. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.55"
    Within rebalance band of target 9.4%: no trade. Analyst target 327.70 USD vs 228.52 USD (+43%, 59 analysts); de-biased α +1.9% vs CAPM hurdle 13.9%. Uptrend +13% vs 200-day avg; 12-1 mom +15%; RSI 52. Quality z +0.47 (ROE 101%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.51"
    Within rebalance band of target 8.0%: no trade. Analyst target 233.77 USD vs 183.98 USD (+27%, 26 analysts); de-biased α -1.5% vs CAPM hurdle 11.1%. Uptrend +2% vs 200-day avg; 12-1 mom +73%; RSI 43. Quality z +0.51 (ROE 87%).

??? success "TSM (TSM) — 🟢 Buy, score +0.48"
    Within rebalance band of target 9.9%: no trade. Analyst target 552.26 USD vs 444.99 USD (+24%, 20 analysts); de-biased α -2.0% vs CAPM hurdle 10.8%. Uptrend +14% vs 200-day avg; 12-1 mom +50%; RSI 48. Quality z +0.58 (ROE 35%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.47"
    Within rebalance band of target 6.9%: no trade. Analyst target 638.94 USD vs 464.18 USD (+38%, 36 analysts); de-biased α +1.1% vs CAPM hurdle 11.6%. Uptrend +6% vs 200-day avg; 12-1 mom +103%; RSI 41. Quality z +0.03 (ROE 36%).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.40"
    **TRIM 541 sh** → target 6.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 55.72 EUR (+56%, 23 analysts); de-biased α +5.0% vs CAPM hurdle 14.1%. Downtrend -1% vs 200-day avg; 12-1 mom +70%; RSI 43. Quality z -0.04 (ROE 6%).

??? success "ASX (ASX) — 🟢 Buy, score +0.27"
    Within rebalance band of target 4.2%: no trade. Analyst target 51.00 USD vs 47.61 USD (+7%, 1 analysts); de-biased α -3.3% vs CAPM hurdle 11.9%. Uptrend +51% vs 200-day avg; 12-1 mom +238%; RSI 65. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 11,560 JPY (+32%, 23 analysts); de-biased α -0.4% vs CAPM hurdle 12.8%. Uptrend +17% vs 200-day avg; 12-1 mom +104%; RSI 51. Quality z -0.28 (ROE 29%).

??? note "ASML (ASML) — ⚪ Hold, score +0.17"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,717.08 USD (+22%, 16 analysts); de-biased α -3.0% vs CAPM hurdle 12.3%. Uptrend +10% vs 200-day avg; 12-1 mom +69%; RSI 45. Quality z +0.42 (ROE 50%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.12"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 301.18 USD (+25%, 31 analysts); de-biased α -2.5% vs CAPM hurdle 12.6%. Uptrend +8% vs 200-day avg; 12-1 mom +109%; RSI 43. Quality z +0.02 (ROE 65%).

??? note "GFS (GFS) — ⚪ Hold, score -0.02"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 46.69 USD (+63%, 22 analysts); de-biased α +7.1% vs CAPM hurdle 12.4%. Downtrend -14% vs 200-day avg; 12-1 mom +32%; RSI 45. Quality z -0.21 (ROE 8%).

??? note "AVGO (AVGO) — ⚪ Hold, score -0.15"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 357.41 USD (+49%, 47 analysts); de-biased α +4.0% vs CAPM hurdle 11.2%. Downtrend -3% vs 200-day avg; 12-1 mom +7%; RSI 48. Quality z +0.26 (ROE 31%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 268.84 USD (+9%, 43 analysts); de-biased α -6.7% vs CAPM hurdle 14.1%. Uptrend +55% vs 200-day avg; 12-1 mom +156%; RSI 57. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 826.40 EUR (+37%, 19 analysts); de-biased α +0.4% vs CAPM hurdle 13.2%. Uptrend +3% vs 200-day avg; 12-1 mom +39%; RSI 42. Quality z -0.10 (ROE 19%).

??? note "QCOM (QCOM) — ⚪ Hold, score -0.25"
    Hold zone: not owned, no entry. Analyst target 194.13 USD vs 176.93 USD (+10%, 30 analysts); de-biased α -5.6% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +20%; RSI 47. Quality z +0.70 (ROE 23%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.29"
    Avoid: not owned. Analyst target 324.71 USD vs 287.91 USD (+13%, 31 analysts); de-biased α -4.6% vs CAPM hurdle 10.8%. Uptrend +15% vs 200-day avg; 12-1 mom +57%; RSI 59. Quality z +0.24 (ROE 30%).

??? failure "TER (TER) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 446.47 USD vs 380.52 USD (+17%, 15 analysts); de-biased α -4.2% vs CAPM hurdle 12.3%. Uptrend +11% vs 200-day avg; 12-1 mom +150%; RSI 46. Quality z -0.31 (ROE 20%).

??? failure "Advantest (6857.T) — 🔴 Sell, score -0.39"
    **SELL (exit) 200 sh** → target 0.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 42,686 JPY vs 40,990 JPY (+4%, 21 analysts); de-biased α -7.8% vs CAPM hurdle 13.4%. Uptrend +46% vs 200-day avg; 12-1 mom +117%; RSI 67. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? failure "INTC (INTC) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 116.37 USD vs 102.84 USD (+13%, 43 analysts); de-biased α -5.7% vs CAPM hurdle 14.0%. Uptrend +23% vs 200-day avg; 12-1 mom +167%; RSI 42. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 81,730 JPY vs 59,030 JPY (+38%, 20 analysts); de-biased α +1.4% vs CAPM hurdle 11.5%. Downtrend -10% vs 200-day avg; 12-1 mom +15%; RSI 52. Quality z +0.06 (ROE 25%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 76.40 USD vs 47.60 USD (+61%, 10 analysts); de-biased α +6.2% vs CAPM hurdle 14.0%. Downtrend -17% vs 200-day avg; 12-1 mom +68%; RSI 40. Quality z -1.00 (ROE 9%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.80"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,102 JPY (+27%, 17 analysts); de-biased α -1.0% vs CAPM hurdle 10.8%. Downtrend -2% vs 200-day avg; 12-1 mom +21%; RSI 55. Quality z -0.20 (ROE 10%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.86"
    Avoid: not owned. Analyst target 173.36 USD vs 161.25 USD (+8%, 11 analysts); de-biased α -6.3% vs CAPM hurdle 11.0%. Uptrend +20% vs 200-day avg; 12-1 mom +54%; RSI 59. Quality z -0.02 (ROE 6%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 405.47 USD vs 334.20 USD (+21%, 26 analysts); de-biased α -2.7% vs CAPM hurdle 10.0%. Uptrend +2% vs 200-day avg; 12-1 mom -15%; RSI 53. Quality z +0.31 (ROE 22%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 619.51 USD vs 605.52 USD (+2%, 50 analysts); de-biased α -8.7% vs CAPM hurdle 14.9%. Uptrend +56% vs 200-day avg; 12-1 mom +130%; RSI 56. Quality z -0.15 (ROE 7%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.04"
    Avoid: not owned. Analyst target 569.78 USD vs 494.64 USD (+15%, 26 analysts); de-biased α -4.3% vs CAPM hurdle 10.3%. Uptrend +11% vs 200-day avg; 12-1 mom -13%; RSI 67. Quality z +0.14 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.07"
    Avoid: not owned. Analyst target 288.70 USD vs 255.45 USD (+13%, 40 analysts); de-biased α -7.2% vs CAPM hurdle 19.6%. Uptrend +15% vs 200-day avg; 12-1 mom +54%; RSI 41. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.36"
    Avoid: not owned. Analyst target 95.99 HKD vs 55.55 HKD (+73%, 21 analysts); de-biased α +10.8% vs CAPM hurdle 7.3%. Downtrend -20% vs 200-day avg; 12-1 mom -30%; RSI 30. Quality z -0.99 (ROE 3%). ⚠️ oversold.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| IFX.DE | Infineon Technologies | 1,594 | 55.72 EUR | $99,527 | 10.3% | Buy |
| MU | Micron Technology | 92 | 953.19 USD | $87,693 | 9.0% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 234,500 KRW | $85,014 | 8.8% | Strong Buy |
| NVDA | NVIDIA | 371 | 228.52 USD | $84,781 | 8.7% | Buy |
| TSM | TSMC | 187 | 444.99 USD | $83,213 | 8.6% | Buy |
| 000660.KS | SK hynix | 74 | 1,472,000 KRW | $81,423 | 8.4% | Strong Buy |
| AMAT | Applied Materials | 156 | 464.18 USD | $72,412 | 7.5% | Buy |
| KLAC | KLA Corp | 372 | 183.98 USD | $68,441 | 7.1% | Buy |
| ASML | ASML Holding | 30 | 1,717.08 USD | $51,512 | 5.3% | Hold |
| AVGO | Broadcom | 134 | 357.41 USD | $47,893 | 4.9% | Hold |
| 8035.T | Tokyo Electron | 600 | 11,560 JPY | $43,808 | 4.5% | Hold |
| ASX | ASE Technology | 900 | 47.61 USD | $42,849 | 4.4% | Buy |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 22.1%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
