---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-10 09:52 UTC (Tue Nov 10, 04:52 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Tue 04:52) · Tokyo 🔴 closed (Tue 18:52) · Korea 🔴 closed (Tue 18:52) · Hong Kong 🔴 closed (Tue 17:52) · Xetra 🟢 open (Tue 10:52) · Euronext Amsterdam 🟢 open (Tue 10:52)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$843,713** | $343,857 (41%) | $499,856 (59%) | -15.63% | -74.05% | 🔴 Risk-off (-8.0%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $843,713), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **ASX**<br><small>ASE Technology</small> | 436 | 34.38 USD | $14,988 | Queued · NYSE/Nasdaq closed | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| TRIM | **INTC**<br><small>Intel</small> | 132 | 59.38 USD | $7,838 | Queued · NYSE/Nasdaq closed | analyst α +0.41 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.88 | **MU**<br><small>Micron Technology</small> | 733.50 USD | +107% | +10.6% | +316% | -3% | 36 | +0.12 | 10.1% → 10.0% | – | momentum +0.53 · analyst α +0.48 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.25 | **Samsung**<br><small>005930.KS</small> | 199,600 KRW | +139% | +19.4% | +156% | -15% | 38 | -0.26 | 9.9% → 10.0% | – | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.45 | **MRVL**<br><small>Marvell Technology</small> | 154.59 USD | +90% | +6.3% | +193% | -17% | 32 | -0.12 | 5.9% → 5.8% | – | analyst α +0.36 · momentum +0.35 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.33 | **SK hynix**<br><small>000660.KS</small> | 1,220,000 KRW | – | +0.0% | +188% | -19% | 39 | +0.62 | 5.4% → 5.0% | – | quality +0.33 · momentum +0.30 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢 Buy | +0.68 | **NVDA**<br><small>NVIDIA</small> | 178.60 USD | +83% | +4.7% | +21% | -13% | 27 | +0.47 | 3.8% → 4.3% | – | analyst α +0.27 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.59 | **AMAT**<br><small>Applied Materials</small> | 370.57 USD | +72% | +2.5% | +117% | -17% | 41 | +0.03 | 3.2% → 3.1% | – | analyst α +0.15 · momentum +0.14 |
| 🟢 Buy | +0.54 | **Advantest**<br><small>6857.T</small> | 29,505 JPY | +45% | -4.9% | +140% | +1% | 39 | +0.33 | 2.2% → 2.3% | – | analyst α -0.23 · momentum +0.17 · ⚠️ rich valuation |
| 🟢 Buy | +0.52 | **ASX**<br><small>ASE Technology</small> | 34.38 USD | +48% | -1.7% | +215% | +2% | 40 | -0.68 | 1.3% → 3.0% | ADD 436 | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.48 | **INTC**<br><small>Intel</small> | 59.38 USD | +96% | +7.7% | +166% | -32% | 29 | -0.62 | 2.6% → 1.7% | TRIM 132 | analyst α +0.41 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| ⚪ Hold | +0.19 | **TSM**<br><small>TSMC</small> | 388.62 USD | +42% | -4.8% | +58% | -3% | 41 | +0.58 | 5.8% → 5.8% | – | quality +0.28 · analyst α -0.19 |
| ⚪ Hold | +0.08 | **LRCX**<br><small>Lam Research</small> | 221.53 USD | +69% | +1.5% | +95% | -22% | 39 | +0.02 | 1.5% → 1.5% | – | trend -0.12 · analyst α +0.08 |
| ⚪ Hold | +0.07 | **Tokyo Electron**<br><small>8035.T</small> | 8,978 JPY | +70% | +1.8% | +105% | -13% | 40 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.12 |
| ⚪ Hold | +0.00 | **KLAC**<br><small>KLA Corp</small> | 151.43 USD | +54% | -1.9% | +60% | -17% | 44 | +0.51 | 4.8% → 4.8% | – | quality +0.24 · analyst α -0.12 |
| ⚪ Hold | -0.03 | **Infineon**<br><small>IFX.DE</small> | 51.84 EUR | +67% | +0.7% | +70% | -10% | 49 | -0.04 | 1.6% → 1.6% | – | trend +0.04 · quality -0.04 |
| ⚪ Hold | -0.10 | **TER**<br><small>Teradyne</small> | 246.01 USD | +81% | +4.6% | +111% | -30% | 34 | -0.31 | 1.0% → 1.0% | – | analyst α +0.23 · quality -0.21 |
| ⚪ Hold | -0.16 | **ASML**<br><small>ASML Holding</small> | 1,513.40 USD | +39% | -6.1% | +73% | -5% | 43 | +0.42 | 0.0% → 0.0% | – | analyst α -0.31 · quality +0.18 |
| ⚪ Hold | -0.19 | **GFS**<br><small>GlobalFoundries</small> | 40.49 USD | +88% | +6.1% | +42% | -26% | 41 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.14 |
| 🔴 Sell | -0.34 | **AMD**<br><small>Advanced Micro Devices</small> | 509.01 USD | +22% | -11.1% | +154% | +22% | 48 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.35 | **ASMI**<br><small>ASM.AS</small> | 693.40 EUR | +63% | -0.3% | +72% | -15% | 41 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · analyst α -0.05 |
| 🔴 Sell | -0.58 | **AMKR**<br><small>Amkor Technology</small> | 35.03 USD | +118% | +13.4% | +39% | -38% | 38 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴 Sell | -0.59 | **ENTG**<br><small>Entegris</small> | 140.14 USD | +24% | -9.5% | +85% | +1% | 47 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.10 |
| 🔴 Sell | -0.59 | **Disco**<br><small>6146.T</small> | 45,540 JPY | +79% | +4.4% | +15% | -30% | 39 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · trend -0.21 |
| 🔴 Sell | -0.61 | **AVGO**<br><small>Broadcom</small> | 319.53 USD | +66% | +1.2% | +2% | -13% | 45 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴 Sell | -0.71 | **ARM**<br><small>Arm Holdings</small> | 186.33 USD | +55% | -3.9% | +68% | -20% | 36 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.75 | **SNPS**<br><small>Synopsys</small> | 466.88 USD | +22% | -9.8% | +28% | +6% | 53 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.21 |
| 🔴🔴 Strong Sell | -1.12 | **QCOM**<br><small>Qualcomm</small> | 171.56 USD | +13% | -12.0% | +4% | +2% | 49 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.17 | **CDNS**<br><small>Cadence Design Systems</small> | 336.47 USD | +21% | -10.1% | +7% | +3% | 54 | +0.31 | 0.0% → 0.0% | – | analyst α -0.48 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.17 | **SMIC**<br><small>0981.HK</small> | 47.24 HKD | +103% | +11.2% | -23% | -29% | 42 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.21 | **TXN**<br><small>Texas Instruments</small> | 295.83 USD | +10% | -12.5% | +78% | +13% | 53 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.39 | **Shin-Etsu**<br><small>4063.T</small> | 5,666 JPY | +37% | -5.8% | +26% | -10% | 44 | -0.20 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.20 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.88"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 733.50 USD (+107%, 46 analysts); de-biased α +10.6% vs CAPM hurdle 14.0%. Downtrend -3% vs 200-day avg; 12-1 mom +316%; RSI 36. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.25"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 199,600 KRW (+139%, 36 analysts); de-biased α +19.4% vs CAPM hurdle 11.3%. Downtrend -15% vs 200-day avg; 12-1 mom +156%; RSI 38. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.45"
    Within rebalance band of target 5.8%: no trade. Analyst target 293.88 USD vs 154.59 USD (+90%, 43 analysts); de-biased α +6.3% vs CAPM hurdle 14.1%. Downtrend -17% vs 200-day avg; 12-1 mom +193%; RSI 32. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.33"
    Within rebalance band of target 5.0%: no trade. No reliable analyst target: α set to 0. Downtrend -19% vs 200-day avg; 12-1 mom +188%; RSI 39. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢 Buy, score +0.68"
    Within rebalance band of target 4.3%: no trade. Analyst target 327.70 USD vs 178.60 USD (+83%, 59 analysts); de-biased α +4.7% vs CAPM hurdle 13.9%. Downtrend -13% vs 200-day avg; 12-1 mom +21%; RSI 27. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.59"
    Within rebalance band of target 3.1%: no trade. Analyst target 638.94 USD vs 370.57 USD (+72%, 36 analysts); de-biased α +2.5% vs CAPM hurdle 11.6%. Downtrend -17% vs 200-day avg; 12-1 mom +117%; RSI 41. Quality z +0.03 (ROE 36%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.54"
    Within rebalance band of target 2.3%: no trade. Analyst target 42,686 JPY vs 29,505 JPY (+45%, 21 analysts); de-biased α -4.9% vs CAPM hurdle 13.4%. Uptrend +1% vs 200-day avg; 12-1 mom +140%; RSI 39. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "ASX (ASX) — 🟢 Buy, score +0.52"
    **ADD 436 sh** → target 3.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 34.38 USD (+48%, 1 analysts); de-biased α -1.7% vs CAPM hurdle 11.9%. Uptrend +2% vs 200-day avg; 12-1 mom +215%; RSI 40. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "INTC (INTC) — 🟢 Buy, score +0.48"
    **TRIM 132 sh** → target 1.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 59.38 USD (+96%, 43 analysts); de-biased α +7.7% vs CAPM hurdle 14.0%. Downtrend -32% vs 200-day avg; 12-1 mom +166%; RSI 29. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? note "TSM (TSM) — ⚪ Hold, score +0.19"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 388.62 USD (+42%, 20 analysts); de-biased α -4.8% vs CAPM hurdle 10.8%. Downtrend -3% vs 200-day avg; 12-1 mom +58%; RSI 41. Quality z +0.58 (ROE 35%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 221.53 USD (+69%, 31 analysts); de-biased α +1.5% vs CAPM hurdle 12.6%. Downtrend -22% vs 200-day avg; 12-1 mom +95%; RSI 39. Quality z +0.02 (ROE 65%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.07"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 8,978 JPY (+70%, 23 analysts); de-biased α +1.8% vs CAPM hurdle 12.8%. Downtrend -13% vs 200-day avg; 12-1 mom +105%; RSI 40. Quality z -0.28 (ROE 29%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.00"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 151.43 USD (+54%, 26 analysts); de-biased α -1.9% vs CAPM hurdle 11.1%. Downtrend -17% vs 200-day avg; 12-1 mom +60%; RSI 44. Quality z +0.51 (ROE 87%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score -0.03"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 51.84 EUR (+67%, 23 analysts); de-biased α +0.7% vs CAPM hurdle 14.1%. Downtrend -10% vs 200-day avg; 12-1 mom +70%; RSI 49. Quality z -0.04 (ROE 6%).

??? note "TER (TER) — ⚪ Hold, score -0.10"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 246.01 USD (+81%, 15 analysts); de-biased α +4.6% vs CAPM hurdle 12.3%. Downtrend -30% vs 200-day avg; 12-1 mom +111%; RSI 34. Quality z -0.31 (ROE 20%).

??? note "ASML (ASML) — ⚪ Hold, score -0.16"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,513.40 USD (+39%, 16 analysts); de-biased α -6.1% vs CAPM hurdle 12.3%. Downtrend -5% vs 200-day avg; 12-1 mom +73%; RSI 43. Quality z +0.42 (ROE 50%).

??? note "GFS (GFS) — ⚪ Hold, score -0.19"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 40.49 USD (+88%, 22 analysts); de-biased α +6.1% vs CAPM hurdle 12.4%. Downtrend -26% vs 200-day avg; 12-1 mom +42%; RSI 41. Quality z -0.21 (ROE 8%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.34"
    Avoid: not owned. Analyst target 619.51 USD vs 509.01 USD (+22%, 50 analysts); de-biased α -11.1% vs CAPM hurdle 14.9%. Uptrend +22% vs 200-day avg; 12-1 mom +154%; RSI 48. Quality z -0.15 (ROE 7%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 693.40 EUR (+63%, 19 analysts); de-biased α -0.3% vs CAPM hurdle 13.2%. Downtrend -15% vs 200-day avg; 12-1 mom +72%; RSI 41. Quality z -0.10 (ROE 19%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 76.40 USD vs 35.03 USD (+118%, 10 analysts); de-biased α +13.4% vs CAPM hurdle 14.0%. Downtrend -38% vs 200-day avg; 12-1 mom +39%; RSI 38. Quality z -1.00 (ROE 9%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 173.36 USD vs 140.14 USD (+24%, 11 analysts); de-biased α -9.5% vs CAPM hurdle 11.0%. Uptrend +1% vs 200-day avg; 12-1 mom +85%; RSI 47. Quality z -0.02 (ROE 6%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 81,730 JPY vs 45,540 JPY (+79%, 20 analysts); de-biased α +4.4% vs CAPM hurdle 11.5%. Downtrend -30% vs 200-day avg; 12-1 mom +15%; RSI 39. Quality z +0.06 (ROE 25%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.61"
    Avoid: not owned. Analyst target 531.31 USD vs 319.53 USD (+66%, 47 analysts); de-biased α +1.2% vs CAPM hurdle 11.2%. Downtrend -13% vs 200-day avg; 12-1 mom +2%; RSI 45. Quality z +0.26 (ROE 31%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.71"
    Avoid: not owned. Analyst target 288.70 USD vs 186.33 USD (+55%, 40 analysts); de-biased α -3.9% vs CAPM hurdle 19.6%. Downtrend -20% vs 200-day avg; 12-1 mom +68%; RSI 36. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.75"
    Avoid: not owned. Analyst target 569.78 USD vs 466.88 USD (+22%, 26 analysts); de-biased α -9.8% vs CAPM hurdle 10.3%. Uptrend +6% vs 200-day avg; 12-1 mom +28%; RSI 53. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.12"
    Avoid: not owned. Analyst target 194.13 USD vs 171.56 USD (+13%, 30 analysts); de-biased α -12.0% vs CAPM hurdle 11.9%. Uptrend +2% vs 200-day avg; 12-1 mom +4%; RSI 49. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.17"
    Avoid: not owned. Analyst target 405.47 USD vs 336.47 USD (+21%, 26 analysts); de-biased α -10.1% vs CAPM hurdle 10.0%. Uptrend +3% vs 200-day avg; 12-1 mom +7%; RSI 54. Quality z +0.31 (ROE 22%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.17"
    Avoid: not owned. Analyst target 95.99 HKD vs 47.24 HKD (+103%, 21 analysts); de-biased α +11.2% vs CAPM hurdle 7.3%. Downtrend -29% vs 200-day avg; 12-1 mom -23%; RSI 42. Quality z -0.99 (ROE 3%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.21"
    Avoid: not owned. Analyst target 324.71 USD vs 295.83 USD (+10%, 31 analysts); de-biased α -12.5% vs CAPM hurdle 10.8%. Uptrend +13% vs 200-day avg; 12-1 mom +78%; RSI 53. Quality z +0.24 (ROE 30%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.39"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,666 JPY (+37%, 17 analysts); de-biased α -5.8% vs CAPM hurdle 10.8%. Downtrend -10% vs 200-day avg; 12-1 mom +26%; RSI 44. Quality z -0.20 (ROE 10%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 733.50 USD | $85,086 | 10.1% | Strong Buy |
| 005930.KS | Samsung Electronics | 562 | 199,600 KRW | $83,891 | 9.9% | Strong Buy |
| MRVL | Marvell Technology | 324 | 154.59 USD | $50,087 | 5.9% | Strong Buy |
| TSM | TSMC | 127 | 388.62 USD | $49,355 | 5.8% | Hold |
| 000660.KS | SK hynix | 50 | 1,220,000 KRW | $45,619 | 5.4% | Strong Buy |
| KLAC | KLA Corp | 268 | 151.43 USD | $40,585 | 4.8% | Hold |
| NVDA | NVIDIA | 179 | 178.60 USD | $31,969 | 3.8% | Buy |
| AMAT | Applied Materials | 73 | 370.57 USD | $27,052 | 3.2% | Buy |
| INTC | Intel | 375 | 59.38 USD | $22,268 | 2.6% | Buy |
| 6857.T | Advantest | 100 | 29,505 JPY | $18,662 | 2.2% | Buy |
| IFX.DE | Infineon Technologies | 225 | 51.84 EUR | $13,098 | 1.6% | Hold |
| LRCX | Lam Research | 58 | 221.53 USD | $12,849 | 1.5% | Hold |
| ASX | ASE Technology | 312 | 34.38 USD | $10,725 | 1.3% | Buy |
| TER | Teradyne | 35 | 246.01 USD | $8,610 | 1.0% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-11-03 15:09 UTC | ADD | MRVL | 50 | 172.03 | $8,602 |
| 2026-11-03 15:09 UTC | ADD | AMAT | 15 | 385.21 | $5,778 |
| 2026-11-03 15:09 UTC | TRIM | NVDA | -141 | 208.26 | $29,365 |
| 2026-11-02 15:55 UTC | BUY (new) | TER | 35 | 270.99 | $9,485 |
| 2026-11-02 15:55 UTC | ADD | MRVL | 35 | 184.11 | $6,444 |
| 2026-11-02 15:55 UTC | TRIM | IFX.DE | -1,076 | 52.66 | $63,473 |
| 2026-11-02 06:06 UTC | TRIM | 000660.KS | -18 | 1,490,500.00 | $20,008 |
| 2026-11-02 06:06 UTC | TRIM | 005930.KS | -163 | 231,750.00 | $28,171 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 51.1%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
