---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-10 23:23 UTC (Tue Nov 10, 06:23 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Tue 18:23) · Tokyo 🔴 closed (Wed 08:23) · Korea 🔴 closed (Wed 08:23) · Hong Kong 🔴 closed (Wed 07:23) · Xetra 🔴 closed (Wed 00:23) · Euronext Amsterdam 🔴 closed (Wed 00:23)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$841,217** | $332,664 (40%) | $508,553 (60%) | -15.88% | -74.10% | 🔴 Risk-off (-8.3%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $841,217), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

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
| 🟢🟢 Strong Buy | +2.89 | **MU**<br><small>Micron Technology</small> | 724.85 USD | +110% | +11.0% | +316% | -5% | 36 | +0.12 | 10.0% → 10.0% | – | momentum +0.53 · analyst α +0.48 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.17 | **Samsung**<br><small>005930.KS</small> | 199,600 KRW | +139% | +19.2% | +129% | -16% | 39 | -0.26 | 9.9% → 10.0% | – | analyst α +0.85 · momentum +0.17 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.33 | **MRVL**<br><small>Marvell Technology</small> | 154.31 USD | +90% | +6.2% | +193% | -17% | 32 | -0.12 | 5.9% → 5.3% | – | momentum +0.35 · analyst α +0.31 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.23 | **SK hynix**<br><small>000660.KS</small> | 1,220,000 KRW | – | +0.0% | +155% | -19% | 39 | +0.62 | 5.4% → 4.5% | – | quality +0.33 · momentum +0.26 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢 Buy | +0.71 | **Advantest**<br><small>6857.T</small> | 29,505 JPY | +45% | -5.1% | +129% | +1% | 39 | +0.33 | 2.2% → 2.9% | – | momentum +0.20 · analyst α -0.19 · ⚠️ rich valuation |
| 🟢 Buy | +0.69 | **NVDA**<br><small>NVIDIA</small> | 168.79 USD | +94% | +7.1% | +21% | -17% | 24 | +0.47 | 3.6% → 4.2% | – | analyst α +0.36 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.58 | **INTC**<br><small>Intel</small> | 58.11 USD | +100% | +8.6% | +166% | -33% | 29 | -0.62 | 1.6% → 2.0% | – | analyst α +0.41 · momentum +0.30 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.57 | **AMAT**<br><small>Applied Materials</small> | 372.63 USD | +71% | +2.1% | +117% | -16% | 42 | +0.03 | 3.2% → 3.0% | – | momentum +0.14 · analyst α +0.12 |
| 🟢 Buy | +0.57 | **ASX**<br><small>ASE Technology</small> | 35.49 USD | +44% | -2.4% | +215% | +5% | 42 | -0.68 | 3.6% → 3.2% | – | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.22 | **Infineon**<br><small>IFX.DE</small> | 49.30 EUR | +76% | +2.6% | +70% | -14% | 43 | -0.04 | 1.5% → 1.5% | – | analyst α +0.15 · quality -0.04 |
| ⚪ Hold | +0.16 | **KLAC**<br><small>KLA Corp</small> | 152.66 USD | +53% | -2.4% | +60% | -16% | 45 | +0.51 | 4.9% → 4.9% | – | quality +0.24 · analyst α -0.08 |
| ⚪ Hold | +0.09 | **TSM**<br><small>TSMC</small> | 396.51 USD | +39% | -5.6% | +57% | -1% | 44 | +0.58 | 6.0% → 6.0% | – | quality +0.28 · analyst α -0.23 |
| ⚪ Hold | +0.05 | **Tokyo Electron**<br><small>8035.T</small> | 8,978 JPY | +70% | +1.7% | +107% | -13% | 41 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.10 |
| ⚪ Hold | -0.00 | **LRCX**<br><small>Lam Research</small> | 222.24 USD | +69% | +1.2% | +95% | -22% | 40 | +0.02 | 1.5% → 1.5% | – | trend -0.12 · momentum +0.07 |
| ⚪ Hold | -0.10 | **TER**<br><small>Teradyne</small> | 245.27 USD | +82% | +4.5% | +111% | -30% | 34 | -0.31 | 1.0% → 1.0% | – | analyst α +0.23 · quality -0.21 |
| ⚪ Hold | -0.16 | **ASML**<br><small>ASML Holding</small> | 1,507.04 USD | +39% | -6.1% | +73% | -6% | 43 | +0.42 | 0.0% → 0.0% | – | analyst α -0.31 · quality +0.18 |
| ⚪ Hold | -0.21 | **ASMI**<br><small>ASM.AS</small> | 679.80 EUR | +66% | +0.3% | +72% | -16% | 39 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · trend -0.03 |
| 🔴 Sell | -0.26 | **AMD**<br><small>Advanced Micro Devices</small> | 515.49 USD | +20% | -11.6% | +154% | +23% | 49 | -0.15 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.32 |
| 🔴 Sell | -0.30 | **GFS**<br><small>GlobalFoundries</small> | 40.62 USD | +87% | +5.8% | +42% | -26% | 41 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.14 |
| 🔴 Sell | -0.58 | **AMKR**<br><small>Amkor Technology</small> | 34.47 USD | +122% | +14.1% | +39% | -39% | 37 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴 Sell | -0.59 | **ENTG**<br><small>Entegris</small> | 138.50 USD | +25% | -9.3% | +85% | -0% | 46 | -0.02 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.10 |
| 🔴 Sell | -0.59 | **Disco**<br><small>6146.T</small> | 45,540 JPY | +79% | +4.2% | +14% | -30% | 39 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · trend -0.21 |
| 🔴 Sell | -0.72 | **ARM**<br><small>Arm Holdings</small> | 181.42 USD | +59% | -3.1% | +68% | -22% | 35 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.77 | **AVGO**<br><small>Broadcom</small> | 331.98 USD | +60% | -0.6% | +2% | -9% | 49 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴🔴 Strong Sell | -0.90 | **SNPS**<br><small>Synopsys</small> | 459.92 USD | +24% | -9.6% | +28% | +4% | 51 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.20 |
| 🔴🔴 Strong Sell | -1.07 | **QCOM**<br><small>Qualcomm</small> | 173.52 USD | +12% | -12.5% | +4% | +3% | 50 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.18 | **SMIC**<br><small>0981.HK</small> | 47.24 HKD | +103% | +11.0% | -23% | -29% | 42 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.21 | **TXN**<br><small>Texas Instruments</small> | 300.50 USD | +8% | -13.2% | +78% | +15% | 55 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.28 | **CDNS**<br><small>Cadence Design Systems</small> | 331.70 USD | +22% | -9.9% | +7% | +1% | 52 | +0.31 | 0.0% → 0.0% | – | analyst α -0.48 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.32 | **Shin-Etsu**<br><small>4063.T</small> | 5,666 JPY | +37% | -6.0% | +30% | -10% | 44 | -0.20 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.17 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.89"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 724.85 USD (+110%, 46 analysts); de-biased α +11.0% vs CAPM hurdle 14.0%. Downtrend -5% vs 200-day avg; 12-1 mom +316%; RSI 36. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.17"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 199,600 KRW (+139%, 36 analysts); de-biased α +19.2% vs CAPM hurdle 11.3%. Downtrend -16% vs 200-day avg; 12-1 mom +129%; RSI 39. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.33"
    Within rebalance band of target 5.3%: no trade. Analyst target 293.88 USD vs 154.31 USD (+90%, 43 analysts); de-biased α +6.2% vs CAPM hurdle 14.1%. Downtrend -17% vs 200-day avg; 12-1 mom +193%; RSI 32. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.23"
    Within rebalance band of target 4.5%: no trade. No reliable analyst target: α set to 0. Downtrend -19% vs 200-day avg; 12-1 mom +155%; RSI 39. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Advantest (6857.T) — 🟢 Buy, score +0.71"
    Within rebalance band of target 2.9%: no trade. Analyst target 42,686 JPY vs 29,505 JPY (+45%, 21 analysts); de-biased α -5.1% vs CAPM hurdle 13.4%. Uptrend +1% vs 200-day avg; 12-1 mom +129%; RSI 39. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.69"
    Within rebalance band of target 4.2%: no trade. Analyst target 327.70 USD vs 168.79 USD (+94%, 59 analysts); de-biased α +7.1% vs CAPM hurdle 13.9%. Downtrend -17% vs 200-day avg; 12-1 mom +21%; RSI 24. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "INTC (INTC) — 🟢 Buy, score +0.58"
    Within rebalance band of target 2.0%: no trade. Analyst target 116.37 USD vs 58.11 USD (+100%, 43 analysts); de-biased α +8.6% vs CAPM hurdle 14.0%. Downtrend -33% vs 200-day avg; 12-1 mom +166%; RSI 29. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.57"
    Within rebalance band of target 3.0%: no trade. Analyst target 638.94 USD vs 372.63 USD (+71%, 36 analysts); de-biased α +2.1% vs CAPM hurdle 11.6%. Downtrend -16% vs 200-day avg; 12-1 mom +117%; RSI 42. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.57"
    Within rebalance band of target 3.2%: no trade. Analyst target 51.00 USD vs 35.49 USD (+44%, 1 analysts); de-biased α -2.4% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +215%; RSI 42. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 49.30 EUR (+76%, 23 analysts); de-biased α +2.6% vs CAPM hurdle 14.1%. Downtrend -14% vs 200-day avg; 12-1 mom +70%; RSI 43. Quality z -0.04 (ROE 6%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.16"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 152.66 USD (+53%, 26 analysts); de-biased α -2.4% vs CAPM hurdle 11.1%. Downtrend -16% vs 200-day avg; 12-1 mom +60%; RSI 45. Quality z +0.51 (ROE 87%).

??? note "TSM (TSM) — ⚪ Hold, score +0.09"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 396.51 USD (+39%, 20 analysts); de-biased α -5.6% vs CAPM hurdle 10.8%. Downtrend -1% vs 200-day avg; 12-1 mom +57%; RSI 44. Quality z +0.58 (ROE 35%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.05"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 8,978 JPY (+70%, 23 analysts); de-biased α +1.7% vs CAPM hurdle 12.8%. Downtrend -13% vs 200-day avg; 12-1 mom +107%; RSI 41. Quality z -0.28 (ROE 29%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.00"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 222.24 USD (+69%, 31 analysts); de-biased α +1.2% vs CAPM hurdle 12.6%. Downtrend -22% vs 200-day avg; 12-1 mom +95%; RSI 40. Quality z +0.02 (ROE 65%).

??? note "TER (TER) — ⚪ Hold, score -0.10"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 245.27 USD (+82%, 15 analysts); de-biased α +4.5% vs CAPM hurdle 12.3%. Downtrend -30% vs 200-day avg; 12-1 mom +111%; RSI 34. Quality z -0.31 (ROE 20%).

??? note "ASML (ASML) — ⚪ Hold, score -0.16"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,507.04 USD (+39%, 16 analysts); de-biased α -6.1% vs CAPM hurdle 12.3%. Downtrend -6% vs 200-day avg; 12-1 mom +73%; RSI 43. Quality z +0.42 (ROE 50%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.21"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 679.80 EUR (+66%, 19 analysts); de-biased α +0.3% vs CAPM hurdle 13.2%. Downtrend -16% vs 200-day avg; 12-1 mom +72%; RSI 39. Quality z -0.10 (ROE 19%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.26"
    Avoid: not owned. Analyst target 619.51 USD vs 515.49 USD (+20%, 50 analysts); de-biased α -11.6% vs CAPM hurdle 14.9%. Uptrend +23% vs 200-day avg; 12-1 mom +154%; RSI 49. Quality z -0.15 (ROE 7%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.30"
    Avoid: not owned. Analyst target 76.00 USD vs 40.62 USD (+87%, 22 analysts); de-biased α +5.8% vs CAPM hurdle 12.4%. Downtrend -26% vs 200-day avg; 12-1 mom +42%; RSI 41. Quality z -0.21 (ROE 8%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 76.40 USD vs 34.47 USD (+122%, 10 analysts); de-biased α +14.1% vs CAPM hurdle 14.0%. Downtrend -39% vs 200-day avg; 12-1 mom +39%; RSI 37. Quality z -1.00 (ROE 9%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 173.36 USD vs 138.50 USD (+25%, 11 analysts); de-biased α -9.3% vs CAPM hurdle 11.0%. Downtrend -0% vs 200-day avg; 12-1 mom +85%; RSI 46. Quality z -0.02 (ROE 6%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 81,730 JPY vs 45,540 JPY (+79%, 20 analysts); de-biased α +4.2% vs CAPM hurdle 11.5%. Downtrend -30% vs 200-day avg; 12-1 mom +14%; RSI 39. Quality z +0.06 (ROE 25%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.72"
    Avoid: not owned. Analyst target 288.70 USD vs 181.42 USD (+59%, 40 analysts); de-biased α -3.1% vs CAPM hurdle 19.6%. Downtrend -22% vs 200-day avg; 12-1 mom +68%; RSI 35. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.77"
    Avoid: not owned. Analyst target 531.31 USD vs 331.98 USD (+60%, 47 analysts); de-biased α -0.6% vs CAPM hurdle 11.2%. Downtrend -9% vs 200-day avg; 12-1 mom +2%; RSI 49. Quality z +0.26 (ROE 31%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.90"
    Avoid: not owned. Analyst target 569.78 USD vs 459.92 USD (+24%, 26 analysts); de-biased α -9.6% vs CAPM hurdle 10.3%. Uptrend +4% vs 200-day avg; 12-1 mom +28%; RSI 51. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.07"
    Avoid: not owned. Analyst target 194.13 USD vs 173.52 USD (+12%, 30 analysts); de-biased α -12.5% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +4%; RSI 50. Quality z +0.70 (ROE 23%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.18"
    Avoid: not owned. Analyst target 95.99 HKD vs 47.24 HKD (+103%, 21 analysts); de-biased α +11.0% vs CAPM hurdle 7.3%. Downtrend -29% vs 200-day avg; 12-1 mom -23%; RSI 42. Quality z -0.99 (ROE 3%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.21"
    Avoid: not owned. Analyst target 324.71 USD vs 300.50 USD (+8%, 31 analysts); de-biased α -13.2% vs CAPM hurdle 10.8%. Uptrend +15% vs 200-day avg; 12-1 mom +78%; RSI 55. Quality z +0.24 (ROE 30%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.28"
    Avoid: not owned. Analyst target 405.47 USD vs 331.70 USD (+22%, 26 analysts); de-biased α -9.9% vs CAPM hurdle 10.0%. Uptrend +1% vs 200-day avg; 12-1 mom +7%; RSI 52. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.32"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,666 JPY (+37%, 17 analysts); de-biased α -6.0% vs CAPM hurdle 10.8%. Downtrend -10% vs 200-day avg; 12-1 mom +30%; RSI 44. Quality z -0.20 (ROE 10%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 724.85 USD | $84,083 | 10.0% | Strong Buy |
| 005930.KS | Samsung Electronics | 562 | 199,600 KRW | $83,566 | 9.9% | Strong Buy |
| TSM | TSMC | 127 | 396.51 USD | $50,357 | 6.0% | Hold |
| MRVL | Marvell Technology | 324 | 154.31 USD | $49,996 | 5.9% | Strong Buy |
| 000660.KS | SK hynix | 50 | 1,220,000 KRW | $45,443 | 5.4% | Strong Buy |
| KLAC | KLA Corp | 268 | 152.66 USD | $40,913 | 4.9% | Hold |
| ASX | ASE Technology | 864 | 35.49 USD | $30,663 | 3.6% | Buy |
| NVDA | NVIDIA | 179 | 168.79 USD | $30,213 | 3.6% | Buy |
| AMAT | Applied Materials | 73 | 372.63 USD | $27,202 | 3.2% | Buy |
| 6857.T | Advantest | 100 | 29,505 JPY | $18,593 | 2.2% | Buy |
| INTC | Intel | 235 | 58.11 USD | $13,656 | 1.6% | Buy |
| LRCX | Lam Research | 58 | 222.24 USD | $12,890 | 1.5% | Hold |
| IFX.DE | Infineon Technologies | 225 | 49.30 EUR | $12,392 | 1.5% | Hold |
| TER | Teradyne | 35 | 245.27 USD | $8,584 | 1.0% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-11-03 15:09 UTC | ADD | MRVL | 50 | 172.03 | $8,602 |
| 2026-11-03 15:09 UTC | ADD | AMAT | 15 | 385.21 | $5,778 |
| 2026-11-03 15:09 UTC | TRIM | NVDA | -141 | 208.26 | $29,365 |
| 2026-11-02 15:55 UTC | BUY (new) | TER | 35 | 270.99 | $9,485 |
| 2026-11-02 15:55 UTC | ADD | MRVL | 35 | 184.11 | $6,444 |
| 2026-11-02 15:55 UTC | TRIM | IFX.DE | -1,076 | 52.66 | $63,473 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 51.8%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
