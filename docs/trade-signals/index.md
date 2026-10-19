---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-19 15:37 UTC (Mon Oct 19, 11:37 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Mon 11:37) · Tokyo 🔴 closed (Tue 00:37) · Korea 🔴 closed (Tue 00:37) · Hong Kong 🔴 closed (Mon 23:37) · Xetra 🔴 closed (Mon 17:37) · Euronext Amsterdam 🔴 closed (Mon 17:37)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$912,845** | $128,835 (14%) | $784,010 (86%) | -8.72% | -9.29% | 🟢 Risk-on (+9.5%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $912,845), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **ASX**<br><small>ASE Technology</small> | 465 | 41.40 USD | $19,251 | Executed (paper) | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| TRIM | **TSM**<br><small>TSMC</small> | 25 | 426.75 USD | $10,669 | Executed (paper) | quality +0.28 · momentum -0.12 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.80 | **MU**<br><small>Micron Technology</small> | 925.63 USD | +64% | +5.4% | +402% | +28% | 41 | +0.12 | 9.3% → 10.0% | – | momentum +0.53 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.21 | **Samsung**<br><small>005930.KS</small> | 216,250 KRW | +121% | +20.3% | +199% | -7% | 32 | -0.26 | 8.6% → 10.0% | – | analyst α +0.85 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.66 | **SK hynix**<br><small>000660.KS</small> | 1,256,000 KRW | – | +0.0% | +390% | -14% | 25 | +0.62 | 10.1% → 10.0% | – | momentum +0.41 · quality +0.33 · ⚠️ oversold, cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.82 | **Infineon**<br><small>IFX.DE</small> | 52.17 EUR | +66% | +6.0% | +65% | -8% | 36 | -0.04 | 8.3% → 9.3% | – | analyst α +0.48 · trend -0.14 |
| 🟢 Buy | +0.75 | **NVDA**<br><small>NVIDIA</small> | 219.25 USD | +49% | +1.8% | +23% | +8% | 44 | +0.47 | 8.9% → 8.6% | – | quality +0.21 · analyst α +0.19 |
| 🟢 Buy | +0.72 | **AMAT**<br><small>Applied Materials</small> | 426.87 USD | +50% | +2.4% | +96% | -3% | 36 | +0.03 | 7.3% → 7.0% | – | analyst α +0.23 · momentum +0.10 |
| 🟢 Buy | +0.56 | **KLAC**<br><small>KLA Corp</small> | 172.11 USD | +36% | -0.9% | +62% | -5% | 38 | +0.51 | 5.3% → 6.0% | – | quality +0.24 · trend -0.07 |
| 🟢 Buy | +0.56 | **ASX**<br><small>ASE Technology</small> | 41.40 USD | +23% | -2.1% | +234% | +29% | 45 | -0.68 | 6.0% → 6.0% | TRIM 465 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.46 | **Advantest**<br><small>6857.T</small> | 34,440 JPY | +24% | -4.5% | +107% | +22% | 44 | +0.33 | 2.4% → 3.5% | – | analyst α -0.27 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.39 | **TSM**<br><small>TSMC</small> | 426.75 USD | +29% | -2.3% | +47% | +8% | 43 | +0.58 | 5.5% → 5.5% | TRIM 25 | quality +0.28 · momentum -0.12 |
| ⚪ Hold | +0.24 | **LRCX**<br><small>Lam Research</small> | 279.70 USD | +34% | -1.7% | +103% | -1% | 39 | +0.02 | 0.0% → 0.0% | – | momentum +0.12 · trend -0.03 |
| ⚪ Hold | +0.15 | **ASML**<br><small>ASML Holding</small> | 1,681.14 USD | +25% | -3.9% | +66% | +7% | 44 | +0.42 | 5.5% → 5.5% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | +0.13 | **AVGO**<br><small>Broadcom</small> | 339.83 USD | +56% | +4.3% | +2% | -7% | 42 | +0.26 | 5.0% → 5.0% | – | analyst α +0.31 · momentum -0.26 |
| ⚪ Hold | +0.11 | **Tokyo Electron**<br><small>8035.T</small> | 10,380 JPY | +47% | +1.7% | +85% | +5% | 41 | -0.28 | 3.6% → 3.6% | – | quality -0.18 · analyst α +0.12 |
| ⚪ Hold | -0.10 | **GFS**<br><small>GlobalFoundries</small> | 46.75 USD | +63% | +5.4% | +39% | -15% | 46 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.18 |
| ⚪ Hold | -0.20 | **MRVL**<br><small>Marvell Technology</small> | 245.81 USD | +20% | -5.8% | +177% | +39% | 47 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | -0.22 | **ASMI**<br><small>ASM.AS</small> | 760.20 EUR | +48% | +1.7% | +53% | -6% | 34 | -0.10 | 0.0% → 0.0% | – | analyst α +0.15 · momentum -0.10 |
| 🔴 Sell | -0.37 | **TER**<br><small>Teradyne</small> | 346.32 USD | +29% | -3.0% | +167% | +0% | 41 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.47 | **TXN**<br><small>Texas Instruments</small> | 274.43 USD | +18% | -4.8% | +56% | +8% | 46 | +0.24 | 0.0% → 0.0% | – | analyst α -0.31 · trend +0.10 |
| 🔴 Sell | -0.48 | **Disco**<br><small>6146.T</small> | 53,900 JPY | +52% | +3.1% | +1% | -18% | 41 | +0.06 | 0.0% → 0.0% | – | momentum -0.30 · analyst α +0.27 |
| 🔴 Sell | -0.51 | **INTC**<br><small>Intel</small> | 95.28 USD | +22% | -5.1% | +195% | +12% | 39 | -0.62 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.55 | **AMKR**<br><small>Amkor Technology</small> | 42.95 USD | +78% | +9.0% | +61% | -25% | 34 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.93 | **ENTG**<br><small>Entegris</small> | 148.70 USD | +17% | -5.7% | +58% | +9% | 47 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.12 |
| 🔴🔴 Strong Sell | -0.95 | **Shin-Etsu**<br><small>4063.T</small> | 5,973 JPY | +30% | -1.9% | +19% | -5% | 48 | -0.20 | 0.0% → 0.0% | – | momentum -0.20 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.02 | **QCOM**<br><small>Qualcomm</small> | 177.54 USD | +9% | -7.3% | +11% | +6% | 49 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.08 | **CDNS**<br><small>Cadence Design Systems</small> | 329.15 USD | +23% | -3.9% | -13% | +1% | 50 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -1.11 | **SMIC**<br><small>0981.HK</small> | 52.40 HKD | +83% | +11.8% | -29% | -24% | 25 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.12 | **SNPS**<br><small>Synopsys</small> | 461.68 USD | +23% | -3.9% | -13% | +4% | 52 | +0.14 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -1.14 | **AMD**<br><small>Advanced Micro Devices</small> | 553.57 USD | +12% | -7.9% | +139% | +40% | 44 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.29 | **ARM**<br><small>Arm Holdings</small> | 234.09 USD | +23% | -6.2% | +61% | +4% | 37 | +0.04 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.03 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.80"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 925.63 USD (+64%, 46 analysts); de-biased α +5.4% vs CAPM hurdle 14.0%. Uptrend +28% vs 200-day avg; 12-1 mom +402%; RSI 41. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.21"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 216,250 KRW (+121%, 36 analysts); de-biased α +20.3% vs CAPM hurdle 11.3%. Downtrend -7% vs 200-day avg; 12-1 mom +199%; RSI 32. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.66"
    Within rebalance band of target 10.0%: no trade. No reliable analyst target: α set to 0. Downtrend -14% vs 200-day avg; 12-1 mom +390%; RSI 25. Quality z +0.62 (ROE 44%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "Infineon (IFX.DE) — 🟢🟢 Strong Buy, score +0.82"
    Within rebalance band of target 9.3%: no trade. Analyst target 86.74 EUR vs 52.17 EUR (+66%, 23 analysts); de-biased α +6.0% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +65%; RSI 36. Quality z -0.04 (ROE 6%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.75"
    Within rebalance band of target 8.6%: no trade. Analyst target 327.70 USD vs 219.25 USD (+49%, 59 analysts); de-biased α +1.8% vs CAPM hurdle 13.9%. Uptrend +8% vs 200-day avg; 12-1 mom +23%; RSI 44. Quality z +0.47 (ROE 101%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.72"
    Within rebalance band of target 7.0%: no trade. Analyst target 638.94 USD vs 426.87 USD (+50%, 36 analysts); de-biased α +2.4% vs CAPM hurdle 11.6%. Downtrend -3% vs 200-day avg; 12-1 mom +96%; RSI 36. Quality z +0.03 (ROE 36%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.56"
    Within rebalance band of target 6.0%: no trade. Analyst target 233.77 USD vs 172.11 USD (+36%, 26 analysts); de-biased α -0.9% vs CAPM hurdle 11.1%. Downtrend -5% vs 200-day avg; 12-1 mom +62%; RSI 38. Quality z +0.51 (ROE 87%).

??? success "ASX (ASX) — 🟢 Buy, score +0.56"
    **TRIM 465 sh** → target 6.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 41.40 USD (+23%, 1 analysts); de-biased α -2.1% vs CAPM hurdle 11.9%. Uptrend +29% vs 200-day avg; 12-1 mom +234%; RSI 45. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.46"
    Within rebalance band of target 3.5%: no trade. Analyst target 42,686 JPY vs 34,440 JPY (+24%, 21 analysts); de-biased α -4.5% vs CAPM hurdle 13.4%. Uptrend +22% vs 200-day avg; 12-1 mom +107%; RSI 44. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.39"
    **TRIM 25 sh** → target 5.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 426.75 USD (+29%, 20 analysts); de-biased α -2.3% vs CAPM hurdle 10.8%. Uptrend +8% vs 200-day avg; 12-1 mom +47%; RSI 43. Quality z +0.58 (ROE 35%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.24"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 279.70 USD (+34%, 31 analysts); de-biased α -1.7% vs CAPM hurdle 12.6%. Downtrend -1% vs 200-day avg; 12-1 mom +103%; RSI 39. Quality z +0.02 (ROE 65%).

??? note "ASML (ASML) — ⚪ Hold, score +0.15"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,681.14 USD (+25%, 16 analysts); de-biased α -3.9% vs CAPM hurdle 12.3%. Uptrend +7% vs 200-day avg; 12-1 mom +66%; RSI 44. Quality z +0.42 (ROE 50%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.13"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 339.83 USD (+56%, 47 analysts); de-biased α +4.3% vs CAPM hurdle 11.2%. Downtrend -7% vs 200-day avg; 12-1 mom +2%; RSI 42. Quality z +0.26 (ROE 31%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.11"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 10,380 JPY (+47%, 23 analysts); de-biased α +1.7% vs CAPM hurdle 12.8%. Uptrend +5% vs 200-day avg; 12-1 mom +85%; RSI 41. Quality z -0.28 (ROE 29%).

??? note "GFS (GFS) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 46.75 USD (+63%, 22 analysts); de-biased α +5.4% vs CAPM hurdle 12.4%. Downtrend -15% vs 200-day avg; 12-1 mom +39%; RSI 46. Quality z -0.21 (ROE 8%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.20"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 245.81 USD (+20%, 43 analysts); de-biased α -5.8% vs CAPM hurdle 14.1%. Uptrend +39% vs 200-day avg; 12-1 mom +177%; RSI 47. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.22"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 760.20 EUR (+48%, 19 analysts); de-biased α +1.7% vs CAPM hurdle 13.2%. Downtrend -6% vs 200-day avg; 12-1 mom +53%; RSI 34. Quality z -0.10 (ROE 19%).

??? failure "TER (TER) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 446.47 USD vs 346.32 USD (+29%, 15 analysts); de-biased α -3.0% vs CAPM hurdle 12.3%. Uptrend +0% vs 200-day avg; 12-1 mom +167%; RSI 41. Quality z -0.31 (ROE 20%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.47"
    Avoid: not owned. Analyst target 324.71 USD vs 274.43 USD (+18%, 31 analysts); de-biased α -4.8% vs CAPM hurdle 10.8%. Uptrend +8% vs 200-day avg; 12-1 mom +56%; RSI 46. Quality z +0.24 (ROE 30%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.48"
    Avoid: not owned. Analyst target 81,730 JPY vs 53,900 JPY (+52%, 20 analysts); de-biased α +3.1% vs CAPM hurdle 11.5%. Downtrend -18% vs 200-day avg; 12-1 mom +1%; RSI 41. Quality z +0.06 (ROE 25%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.51"
    Avoid: not owned. Analyst target 116.37 USD vs 95.28 USD (+22%, 43 analysts); de-biased α -5.1% vs CAPM hurdle 14.0%. Uptrend +12% vs 200-day avg; 12-1 mom +195%; RSI 39. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 76.40 USD vs 42.95 USD (+78%, 10 analysts); de-biased α +9.0% vs CAPM hurdle 14.0%. Downtrend -25% vs 200-day avg; 12-1 mom +61%; RSI 34. Quality z -1.00 (ROE 9%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.93"
    Avoid: not owned. Analyst target 173.36 USD vs 148.70 USD (+17%, 11 analysts); de-biased α -5.7% vs CAPM hurdle 11.0%. Uptrend +9% vs 200-day avg; 12-1 mom +58%; RSI 47. Quality z -0.02 (ROE 6%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.95"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,973 JPY (+30%, 17 analysts); de-biased α -1.9% vs CAPM hurdle 10.8%. Downtrend -5% vs 200-day avg; 12-1 mom +19%; RSI 48. Quality z -0.20 (ROE 10%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.02"
    Avoid: not owned. Analyst target 194.13 USD vs 177.54 USD (+9%, 30 analysts); de-biased α -7.3% vs CAPM hurdle 11.9%. Uptrend +6% vs 200-day avg; 12-1 mom +11%; RSI 49. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.08"
    Avoid: not owned. Analyst target 405.47 USD vs 329.15 USD (+23%, 26 analysts); de-biased α -3.9% vs CAPM hurdle 10.0%. Uptrend +1% vs 200-day avg; 12-1 mom -13%; RSI 50. Quality z +0.31 (ROE 22%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.11"
    Avoid: not owned. Analyst target 95.99 HKD vs 52.40 HKD (+83%, 21 analysts); de-biased α +11.8% vs CAPM hurdle 7.3%. Downtrend -24% vs 200-day avg; 12-1 mom -29%; RSI 25. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.12"
    Avoid: not owned. Analyst target 569.78 USD vs 461.68 USD (+23%, 26 analysts); de-biased α -3.9% vs CAPM hurdle 10.3%. Uptrend +4% vs 200-day avg; 12-1 mom -13%; RSI 52. Quality z +0.14 (ROE 7%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.14"
    Avoid: not owned. Analyst target 619.51 USD vs 553.57 USD (+12%, 50 analysts); de-biased α -7.9% vs CAPM hurdle 14.9%. Uptrend +40% vs 200-day avg; 12-1 mom +139%; RSI 44. Quality z -0.15 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.29"
    Avoid: not owned. Analyst target 288.70 USD vs 234.09 USD (+23%, 40 analysts); de-biased α -6.2% vs CAPM hurdle 19.6%. Uptrend +4% vs 200-day avg; 12-1 mom +61%; RSI 37. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,256,000 KRW | $92,442 | 10.1% | Strong Buy |
| MU | Micron Technology | 92 | 925.63 USD | $85,158 | 9.3% | Strong Buy |
| NVDA | NVIDIA | 371 | 219.25 USD | $81,342 | 8.9% | Buy |
| 005930.KS | Samsung Electronics | 485 | 216,250 KRW | $78,768 | 8.6% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 52.17 EUR | $76,151 | 8.3% | Strong Buy |
| AMAT | Applied Materials | 156 | 426.87 USD | $66,592 | 7.3% | Buy |
| ASX | ASE Technology | 1,332 | 41.40 USD | $55,145 | 6.0% | Buy |
| ASML | ASML Holding | 30 | 1,681.14 USD | $50,434 | 5.5% | Hold |
| TSM | TSMC | 117 | 426.75 USD | $49,930 | 5.5% | Buy |
| KLAC | KLA Corp | 279 | 172.11 USD | $48,019 | 5.3% | Buy |
| AVGO | Broadcom | 134 | 339.83 USD | $45,537 | 5.0% | Hold |
| 8035.T | Tokyo Electron | 500 | 10,380 JPY | $32,757 | 3.6% | Hold |
| 6857.T | Advantest | 100 | 34,440 JPY | $21,737 | 2.4% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 28.7%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
