---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-21 23:21 UTC (Wed Oct 21, 07:21 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Wed 19:21) · Tokyo 🔴 closed (Thu 08:21) · Korea 🔴 closed (Thu 08:21) · Hong Kong 🔴 closed (Thu 07:21) · Xetra 🔴 closed (Thu 01:21) · Euronext Amsterdam 🔴 closed (Thu 01:21)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$914,119** | $124,394 (14%) | $789,725 (86%) | -8.59% | -9.78% | 🟢 Risk-on (+8.5%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $914,119), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

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
| 🟢🟢 Strong Buy | +3.12 | **SK hynix**<br><small>000660.KS</small> | 1,287,000 KRW | +144% | +24.2% | +309% | -12% | 31 | +0.62 | 10.4% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.58 | **MU**<br><small>Micron Technology</small> | 913.62 USD | +66% | +4.9% | +431% | +26% | 40 | +0.12 | 9.2% → 10.0% | – | momentum +0.53 · analyst α +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.45 | **Samsung**<br><small>005930.KS</small> | 221,000 KRW | +116% | +18.1% | +170% | -6% | 38 | -0.26 | 8.8% → 10.0% | – | analyst α +0.66 · momentum +0.20 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.70 | **Infineon**<br><small>IFX.DE</small> | 53.14 EUR | +63% | +4.2% | +77% | -6% | 40 | -0.04 | 8.5% → 10.0% | – | analyst α +0.36 · momentum +0.07 |
| 🟢 Buy | +0.59 | **AMAT**<br><small>Applied Materials</small> | 408.60 USD | +56% | +3.0% | +108% | -7% | 31 | +0.03 | 7.0% → 7.3% | – | analyst α +0.23 · momentum +0.12 |
| 🟢 Buy | +0.49 | **ASX**<br><small>ASE Technology</small> | 42.42 USD | +20% | -3.0% | +251% | +31% | 48 | -0.68 | 6.2% → 6.7% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.49 | **NVDA**<br><small>NVIDIA</small> | 221.87 USD | +48% | +0.2% | +26% | +9% | 48 | +0.47 | 7.1% → 7.1% | – | quality +0.21 · momentum -0.17 |
| 🟢 Buy | +0.41 | **TSM**<br><small>TSMC</small> | 431.82 USD | +28% | -3.8% | +53% | +9% | 46 | +0.58 | 7.3% → 7.3% | – | quality +0.28 · momentum -0.12 |
| 🟢 Buy | +0.27 | **KLAC**<br><small>KLA Corp</small> | 163.35 USD | +43% | -0.1% | +64% | -10% | 31 | +0.51 | 3.8% → 3.5% | – | quality +0.24 · trend -0.14 |
| ⚪ Hold | +0.13 | **Tokyo Electron**<br><small>8035.T</small> | 10,250 JPY | +49% | +1.1% | +71% | +3% | 41 | -0.28 | 3.5% → 3.5% | – | quality -0.18 · analyst α +0.15 |
| ⚪ Hold | +0.11 | **LRCX**<br><small>Lam Research</small> | 260.81 USD | +44% | -0.4% | +117% | -8% | 32 | +0.02 | 3.0% → 3.0% | – | momentum +0.14 · trend -0.10 |
| ⚪ Hold | +0.04 | **ASML**<br><small>ASML Holding</small> | 1,676.31 USD | +25% | -4.9% | +69% | +6% | 44 | +0.42 | 5.5% → 5.5% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | +0.02 | **AVGO**<br><small>Broadcom</small> | 337.68 USD | +57% | +3.5% | +5% | -8% | 41 | +0.26 | 3.7% → 3.7% | – | analyst α +0.27 · momentum -0.26 |
| ⚪ Hold | -0.03 | **Advantest**<br><small>6857.T</small> | 34,390 JPY | +24% | -5.5% | +68% | +20% | 45 | +0.33 | 2.4% → 2.4% | – | analyst α -0.31 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | -0.10 | **MRVL**<br><small>Marvell Technology</small> | 244.67 USD | +20% | -6.7% | +206% | +37% | 47 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · momentum +0.26 · ⚠️ rich valuation |
| ⚪ Hold | -0.13 | **ASMI**<br><small>ASM.AS</small> | 760.40 EUR | +48% | +0.6% | +55% | -6% | 37 | -0.10 | 0.0% → 0.0% | – | analyst α +0.12 · momentum -0.07 |
| ⚪ Hold | -0.23 | **TER**<br><small>Teradyne</small> | 345.51 USD | +29% | -4.0% | +187% | -0% | 41 | -0.31 | 0.0% → 0.0% | – | momentum +0.23 · quality -0.21 |
| 🔴 Sell | -0.27 | **INTC**<br><small>Intel</small> | 92.90 USD | +25% | -5.4% | +225% | +9% | 36 | -0.62 | 0.0% → 0.0% | – | momentum +0.30 · analyst α -0.27 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.31 | **GFS**<br><small>GlobalFoundries</small> | 47.69 USD | +59% | +3.6% | +35% | -13% | 50 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.18 |
| 🔴 Sell | -0.36 | **AMKR**<br><small>Amkor Technology</small> | 43.72 USD | +75% | +7.1% | +70% | -24% | 37 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.51 | **ARM**<br><small>Arm Holdings</small> | 226.57 USD | +27% | -6.3% | +94% | +1% | 36 | +0.04 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.59 | **Disco**<br><small>6146.T</small> | 53,910 JPY | +52% | +2.0% | -4% | -18% | 43 | +0.06 | 0.0% → 0.0% | – | momentum -0.30 · trend -0.21 |
| 🔴🔴 Strong Sell | -0.83 | **QCOM**<br><small>Qualcomm</small> | 177.83 USD | +9% | -8.4% | +21% | +6% | 50 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.90 | **Shin-Etsu**<br><small>4063.T</small> | 5,897 JPY | +32% | -2.6% | +12% | -6% | 45 | -0.20 | 0.0% → 0.0% | – | momentum -0.23 · quality -0.11 |
| 🔴🔴 Strong Sell | -0.91 | **TXN**<br><small>Texas Instruments</small> | 284.85 USD | +14% | -7.0% | +55% | +12% | 56 | +0.24 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.14 |
| 🔴🔴 Strong Sell | -0.91 | **CDNS**<br><small>Cadence Design Systems</small> | 326.10 USD | +24% | -4.6% | -8% | -0% | 49 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -0.92 | **ENTG**<br><small>Entegris</small> | 147.68 USD | +17% | -6.6% | +64% | +8% | 47 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.07 |
| 🔴🔴 Strong Sell | -1.00 | **AMD**<br><small>Advanced Micro Devices</small> | 552.70 USD | +12% | -8.9% | +159% | +38% | 45 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.02 | **SNPS**<br><small>Synopsys</small> | 451.11 USD | +26% | -4.2% | -10% | +1% | 49 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -1.36 | **SMIC**<br><small>0981.HK</small> | 49.96 HKD | +92% | +13.0% | -16% | -27% | 22 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 · ⚠️ oversold |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.12"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,287,000 KRW (+144%, 38 analysts); de-biased α +24.2% vs CAPM hurdle 14.3%. Downtrend -12% vs 200-day avg; 12-1 mom +309%; RSI 31. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.58"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 913.62 USD (+66%, 46 analysts); de-biased α +4.9% vs CAPM hurdle 14.0%. Uptrend +26% vs 200-day avg; 12-1 mom +431%; RSI 40. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.45"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 221,000 KRW (+116%, 36 analysts); de-biased α +18.1% vs CAPM hurdle 11.3%. Downtrend -6% vs 200-day avg; 12-1 mom +170%; RSI 38. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.70"
    Within rebalance band of target 10.0%: no trade. Analyst target 86.74 EUR vs 53.14 EUR (+63%, 23 analysts); de-biased α +4.2% vs CAPM hurdle 14.1%. Downtrend -6% vs 200-day avg; 12-1 mom +77%; RSI 40. Quality z -0.04 (ROE 6%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.59"
    Within rebalance band of target 7.3%: no trade. Analyst target 638.94 USD vs 408.60 USD (+56%, 36 analysts); de-biased α +3.0% vs CAPM hurdle 11.6%. Downtrend -7% vs 200-day avg; 12-1 mom +108%; RSI 31. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.49"
    Within rebalance band of target 6.7%: no trade. Analyst target 51.00 USD vs 42.42 USD (+20%, 1 analysts); de-biased α -3.0% vs CAPM hurdle 11.9%. Uptrend +31% vs 200-day avg; 12-1 mom +251%; RSI 48. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.49"
    Within rebalance band of target 7.1%: no trade. Analyst target 327.70 USD vs 221.87 USD (+48%, 59 analysts); de-biased α +0.2% vs CAPM hurdle 13.9%. Uptrend +9% vs 200-day avg; 12-1 mom +26%; RSI 48. Quality z +0.47 (ROE 101%).

??? success "TSM (TSM) — 🟢 Buy, score +0.41"
    Within rebalance band of target 7.3%: no trade. Analyst target 552.26 USD vs 431.82 USD (+28%, 20 analysts); de-biased α -3.8% vs CAPM hurdle 10.8%. Uptrend +9% vs 200-day avg; 12-1 mom +53%; RSI 46. Quality z +0.58 (ROE 35%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.27"
    Within rebalance band of target 3.5%: no trade. Analyst target 233.77 USD vs 163.35 USD (+43%, 26 analysts); de-biased α -0.1% vs CAPM hurdle 11.1%. Downtrend -10% vs 200-day avg; 12-1 mom +64%; RSI 31. Quality z +0.51 (ROE 87%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.13"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 10,250 JPY (+49%, 23 analysts); de-biased α +1.1% vs CAPM hurdle 12.8%. Uptrend +3% vs 200-day avg; 12-1 mom +71%; RSI 41. Quality z -0.28 (ROE 29%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.11"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 260.81 USD (+44%, 31 analysts); de-biased α -0.4% vs CAPM hurdle 12.6%. Downtrend -8% vs 200-day avg; 12-1 mom +117%; RSI 32. Quality z +0.02 (ROE 65%).

??? note "ASML (ASML) — ⚪ Hold, score +0.04"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,676.31 USD (+25%, 16 analysts); de-biased α -4.9% vs CAPM hurdle 12.3%. Uptrend +6% vs 200-day avg; 12-1 mom +69%; RSI 44. Quality z +0.42 (ROE 50%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.02"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 337.68 USD (+57%, 47 analysts); de-biased α +3.5% vs CAPM hurdle 11.2%. Downtrend -8% vs 200-day avg; 12-1 mom +5%; RSI 41. Quality z +0.26 (ROE 31%).

??? note "Advantest (6857.T) — ⚪ Hold, score -0.03"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 34,390 JPY (+24%, 21 analysts); de-biased α -5.5% vs CAPM hurdle 13.4%. Uptrend +20% vs 200-day avg; 12-1 mom +68%; RSI 45. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 244.67 USD (+20%, 43 analysts); de-biased α -6.7% vs CAPM hurdle 14.1%. Uptrend +37% vs 200-day avg; 12-1 mom +206%; RSI 47. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.13"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 760.40 EUR (+48%, 19 analysts); de-biased α +0.6% vs CAPM hurdle 13.2%. Downtrend -6% vs 200-day avg; 12-1 mom +55%; RSI 37. Quality z -0.10 (ROE 19%).

??? note "TER (TER) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 345.51 USD (+29%, 15 analysts); de-biased α -4.0% vs CAPM hurdle 12.3%. Downtrend -0% vs 200-day avg; 12-1 mom +187%; RSI 41. Quality z -0.31 (ROE 20%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 116.37 USD vs 92.90 USD (+25%, 43 analysts); de-biased α -5.4% vs CAPM hurdle 14.0%. Uptrend +9% vs 200-day avg; 12-1 mom +225%; RSI 36. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "GFS (GFS) — 🔴 Sell, score -0.31"
    Avoid: not owned. Analyst target 76.00 USD vs 47.69 USD (+59%, 22 analysts); de-biased α +3.6% vs CAPM hurdle 12.4%. Downtrend -13% vs 200-day avg; 12-1 mom +35%; RSI 50. Quality z -0.21 (ROE 8%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 76.40 USD vs 43.72 USD (+75%, 10 analysts); de-biased α +7.1% vs CAPM hurdle 14.0%. Downtrend -24% vs 200-day avg; 12-1 mom +70%; RSI 37. Quality z -1.00 (ROE 9%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.51"
    Avoid: not owned. Analyst target 288.70 USD vs 226.57 USD (+27%, 40 analysts); de-biased α -6.3% vs CAPM hurdle 19.6%. Uptrend +1% vs 200-day avg; 12-1 mom +94%; RSI 36. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 81,730 JPY vs 53,910 JPY (+52%, 20 analysts); de-biased α +2.0% vs CAPM hurdle 11.5%. Downtrend -18% vs 200-day avg; 12-1 mom -4%; RSI 43. Quality z +0.06 (ROE 25%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.83"
    Avoid: not owned. Analyst target 194.13 USD vs 177.83 USD (+9%, 30 analysts); de-biased α -8.4% vs CAPM hurdle 11.9%. Uptrend +6% vs 200-day avg; 12-1 mom +21%; RSI 50. Quality z +0.70 (ROE 23%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.90"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,897 JPY (+32%, 17 analysts); de-biased α -2.6% vs CAPM hurdle 10.8%. Downtrend -6% vs 200-day avg; 12-1 mom +12%; RSI 45. Quality z -0.20 (ROE 10%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 324.71 USD vs 284.85 USD (+14%, 31 analysts); de-biased α -7.0% vs CAPM hurdle 10.8%. Uptrend +12% vs 200-day avg; 12-1 mom +55%; RSI 56. Quality z +0.24 (ROE 30%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 405.47 USD vs 326.10 USD (+24%, 26 analysts); de-biased α -4.6% vs CAPM hurdle 10.0%. Downtrend -0% vs 200-day avg; 12-1 mom -8%; RSI 49. Quality z +0.31 (ROE 22%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 173.36 USD vs 147.68 USD (+17%, 11 analysts); de-biased α -6.6% vs CAPM hurdle 11.0%. Uptrend +8% vs 200-day avg; 12-1 mom +64%; RSI 47. Quality z -0.02 (ROE 6%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.00"
    Avoid: not owned. Analyst target 619.51 USD vs 552.70 USD (+12%, 50 analysts); de-biased α -8.9% vs CAPM hurdle 14.9%. Uptrend +38% vs 200-day avg; 12-1 mom +159%; RSI 45. Quality z -0.15 (ROE 7%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.02"
    Avoid: not owned. Analyst target 569.78 USD vs 451.11 USD (+26%, 26 analysts); de-biased α -4.2% vs CAPM hurdle 10.3%. Uptrend +1% vs 200-day avg; 12-1 mom -10%; RSI 49. Quality z +0.14 (ROE 7%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.36"
    Avoid: not owned. Analyst target 95.99 HKD vs 49.96 HKD (+92%, 21 analysts); de-biased α +13.0% vs CAPM hurdle 7.3%. Downtrend -27% vs 200-day avg; 12-1 mom -16%; RSI 22. Quality z -0.99 (ROE 3%). ⚠️ oversold.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,287,000 KRW | $95,129 | 10.4% | Strong Buy |
| MU | Micron Technology | 92 | 913.62 USD | $84,053 | 9.2% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 221,000 KRW | $80,843 | 8.8% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 53.14 EUR | $77,671 | 8.5% | Buy |
| TSM | TSMC | 154 | 431.82 USD | $66,500 | 7.3% | Buy |
| NVDA | NVIDIA | 294 | 221.87 USD | $65,230 | 7.1% | Buy |
| AMAT | Applied Materials | 156 | 408.60 USD | $63,742 | 7.0% | Buy |
| ASX | ASE Technology | 1,332 | 42.42 USD | $56,497 | 6.2% | Buy |
| ASML | ASML Holding | 30 | 1,676.31 USD | $50,289 | 5.5% | Hold |
| KLAC | KLA Corp | 211 | 163.35 USD | $34,467 | 3.8% | Buy |
| AVGO | Broadcom | 100 | 337.68 USD | $33,768 | 3.7% | Hold |
| 8035.T | Tokyo Electron | 500 | 10,250 JPY | $32,406 | 3.5% | Hold |
| LRCX | Lam Research | 105 | 260.81 USD | $27,385 | 3.0% | Hold |
| 6857.T | Advantest | 100 | 34,390 JPY | $21,745 | 2.4% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-10-13 07:43 UTC | ADD | IFX.DE | 620 | 54.55 | $37,861 |
| 2026-10-12 17:56 UTC | ADD | KLAC | 153 | 190.68 | $29,174 |
| 2026-10-12 17:56 UTC | ADD | AMAT | 41 | 497.22 | $20,386 |
| 2026-10-09 16:14 UTC | TRIM | KLAC | -47 | 196.81 | $9,250 |
| 2026-10-09 09:06 UTC | TRIM | IFX.DE | -437 | 59.90 | $29,382 |
| 2026-10-08 16:29 UTC | ADD | AMAT | 32 | 522.02 | $16,705 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 33.0%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
