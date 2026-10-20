---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-20 20:36 UTC (Tue Oct 20, 04:36 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Tue 16:36) · Tokyo 🔴 closed (Wed 05:36) · Korea 🔴 closed (Wed 05:36) · Hong Kong 🔴 closed (Wed 04:36) · Xetra 🔴 closed (Tue 22:36) · Euronext Amsterdam 🔴 closed (Tue 22:36)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$894,422** | $129,183 (14%) | $765,239 (86%) | -10.56% | -11.54% | 🟢 Risk-on (+6.6%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $894,422), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

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
| 🟢🟢 Strong Buy | +3.10 | **MU**<br><small>Micron Technology</small> | 895.85 USD | +70% | +5.9% | +416% | +24% | 37 | +0.12 | 9.2% → 10.0% | – | momentum +0.53 · analyst α +0.48 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.00 | **Samsung**<br><small>005930.KS</small> | 210,500 KRW | +127% | +21.0% | +185% | -10% | 31 | -0.26 | 8.6% → 10.0% | – | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.52 | **SK hynix**<br><small>000660.KS</small> | 1,217,000 KRW | – | +0.0% | +346% | -17% | 24 | +0.62 | 10.1% → 10.0% | – | momentum +0.41 · quality +0.33 · ⚠️ oversold, cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.84 | **AMAT**<br><small>Applied Materials</small> | 404.95 USD | +58% | +3.6% | +107% | -8% | 29 | +0.03 | 7.1% → 8.5% | – | analyst α +0.27 · momentum +0.12 · ⚠️ oversold |
| 🟢 Buy | +0.67 | **Infineon**<br><small>IFX.DE</small> | 52.18 EUR | +66% | +5.1% | +67% | -8% | 36 | -0.04 | 8.5% → 7.9% | – | analyst α +0.41 · trend -0.07 |
| 🟢 Buy | +0.65 | **ASX**<br><small>ASE Technology</small> | 40.78 USD | +25% | -2.3% | +247% | +27% | 43 | -0.68 | 6.1% → 7.2% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.60 | **NVDA**<br><small>NVIDIA</small> | 216.48 USD | +51% | +1.3% | +24% | +7% | 41 | +0.47 | 7.1% → 7.2% | – | quality +0.21 · momentum -0.17 |
| 🟢 Buy | +0.45 | **TSM**<br><small>TSMC</small> | 425.30 USD | +30% | -3.1% | +52% | +8% | 42 | +0.58 | 5.6% → 6.4% | – | quality +0.28 · analyst α -0.12 |
| 🟢 Buy | +0.44 | **KLAC**<br><small>KLA Corp</small> | 161.93 USD | +44% | +0.3% | +67% | -11% | 29 | +0.51 | 5.1% → 4.8% | – | quality +0.24 · trend -0.14 · ⚠️ oversold |
| 🟢 Buy | +0.27 | **LRCX**<br><small>Lam Research</small> | 263.45 USD | +42% | -0.5% | +114% | -7% | 33 | +0.02 | 3.1% → 2.9% | – | momentum +0.14 · trend -0.04 |
| ⚪ Hold | +0.23 | **Tokyo Electron**<br><small>8035.T</small> | 10,115 JPY | +51% | +1.8% | +71% | +1% | 39 | -0.28 | 3.6% → 3.6% | – | analyst α +0.19 · quality -0.18 |
| ⚪ Hold | +0.18 | **Advantest**<br><small>6857.T</small> | 33,880 JPY | +26% | -4.9% | +72% | +19% | 43 | +0.33 | 2.4% → 2.4% | – | analyst α -0.31 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.17 | **AVGO**<br><small>Broadcom</small> | 334.51 USD | +59% | +4.0% | +5% | -9% | 39 | +0.26 | 3.7% → 3.7% | – | analyst α +0.31 · momentum -0.26 |
| ⚪ Hold | +0.06 | **MRVL**<br><small>Marvell Technology</small> | 240.42 USD | +22% | -6.0% | +193% | +36% | 45 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.32 · ⚠️ rich valuation |
| ⚪ Hold | +0.02 | **ASML**<br><small>ASML Holding</small> | 1,630.84 USD | +29% | -3.9% | +67% | +3% | 37 | +0.42 | 5.5% → 5.5% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | -0.18 | **GFS**<br><small>GlobalFoundries</small> | 47.03 USD | +62% | +4.3% | +41% | -14% | 47 | -0.21 | 0.0% → 0.0% | – | analyst α +0.36 · trend -0.16 |
| 🔴 Sell | -0.27 | **INTC**<br><small>Intel</small> | 91.66 USD | +27% | -4.8% | +229% | +8% | 34 | -0.62 | 0.0% → 0.0% | – | momentum +0.30 · analyst α -0.27 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.27 | **ASMI**<br><small>ASM.AS</small> | 743.80 EUR | +52% | +1.6% | +52% | -8% | 32 | -0.10 | 0.0% → 0.0% | – | analyst α +0.15 · momentum -0.12 |
| 🔴 Sell | -0.28 | **TER**<br><small>Teradyne</small> | 336.17 USD | +33% | -2.9% | +177% | -3% | 37 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.40 | **AMKR**<br><small>Amkor Technology</small> | 41.69 USD | +83% | +9.4% | +68% | -28% | 30 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 · ⚠️ oversold |
| 🔴 Sell | -0.58 | **ARM**<br><small>Arm Holdings</small> | 220.92 USD | +31% | -5.3% | +95% | -2% | 33 | +0.04 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.58 | **Disco**<br><small>6146.T</small> | 52,720 JPY | +55% | +3.0% | -5% | -20% | 39 | +0.06 | 0.0% → 0.0% | – | momentum -0.30 · analyst α +0.23 |
| 🔴🔴 Strong Sell | -0.84 | **AMD**<br><small>Advanced Micro Devices</small> | 534.60 USD | +16% | -7.8% | +164% | +35% | 40 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.25 |
| 🔴🔴 Strong Sell | -0.99 | **TXN**<br><small>Texas Instruments</small> | 277.92 USD | +17% | -6.1% | +57% | +9% | 49 | +0.24 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.14 |
| 🔴🔴 Strong Sell | -1.01 | **CDNS**<br><small>Cadence Design Systems</small> | 319.93 USD | +27% | -3.9% | -10% | -2% | 45 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -1.05 | **ENTG**<br><small>Entegris</small> | 142.76 USD | +21% | -5.4% | +58% | +5% | 42 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.07 |
| 🔴🔴 Strong Sell | -1.05 | **Shin-Etsu**<br><small>4063.T</small> | 5,893 JPY | +32% | -2.4% | +13% | -6% | 45 | -0.20 | 0.0% → 0.0% | – | momentum -0.23 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.12 | **SMIC**<br><small>0981.HK</small> | 51.20 HKD | +87% | +12.0% | -25% | -26% | 24 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.17 | **SNPS**<br><small>Synopsys</small> | 447.60 USD | +27% | -3.8% | -10% | +0% | 47 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -1.40 | **QCOM**<br><small>Qualcomm</small> | 175.60 USD | +11% | -7.9% | +21% | +4% | 47 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.10"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 895.85 USD (+70%, 46 analysts); de-biased α +5.9% vs CAPM hurdle 14.0%. Uptrend +24% vs 200-day avg; 12-1 mom +416%; RSI 37. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.00"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 210,500 KRW (+127%, 36 analysts); de-biased α +21.0% vs CAPM hurdle 11.3%. Downtrend -10% vs 200-day avg; 12-1 mom +185%; RSI 31. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.52"
    Within rebalance band of target 10.0%: no trade. No reliable analyst target: α set to 0. Downtrend -17% vs 200-day avg; 12-1 mom +346%; RSI 24. Quality z +0.62 (ROE 44%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "AMAT (AMAT) — 🟢🟢 Strong Buy, score +0.84"
    Within rebalance band of target 8.5%: no trade. Analyst target 638.94 USD vs 404.95 USD (+58%, 36 analysts); de-biased α +3.6% vs CAPM hurdle 11.6%. Downtrend -8% vs 200-day avg; 12-1 mom +107%; RSI 29. Quality z +0.03 (ROE 36%). ⚠️ oversold.

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.67"
    Within rebalance band of target 7.9%: no trade. Analyst target 86.74 EUR vs 52.18 EUR (+66%, 23 analysts); de-biased α +5.1% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +67%; RSI 36. Quality z -0.04 (ROE 6%).

??? success "ASX (ASX) — 🟢 Buy, score +0.65"
    Within rebalance band of target 7.2%: no trade. Analyst target 51.00 USD vs 40.78 USD (+25%, 1 analysts); de-biased α -2.3% vs CAPM hurdle 11.9%. Uptrend +27% vs 200-day avg; 12-1 mom +247%; RSI 43. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.60"
    Within rebalance band of target 7.2%: no trade. Analyst target 327.70 USD vs 216.48 USD (+51%, 59 analysts); de-biased α +1.3% vs CAPM hurdle 13.9%. Uptrend +7% vs 200-day avg; 12-1 mom +24%; RSI 41. Quality z +0.47 (ROE 101%).

??? success "TSM (TSM) — 🟢 Buy, score +0.45"
    Within rebalance band of target 6.4%: no trade. Analyst target 552.26 USD vs 425.30 USD (+30%, 20 analysts); de-biased α -3.1% vs CAPM hurdle 10.8%. Uptrend +8% vs 200-day avg; 12-1 mom +52%; RSI 42. Quality z +0.58 (ROE 35%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.44"
    Within rebalance band of target 4.8%: no trade. Analyst target 233.77 USD vs 161.93 USD (+44%, 26 analysts); de-biased α +0.3% vs CAPM hurdle 11.1%. Downtrend -11% vs 200-day avg; 12-1 mom +67%; RSI 29. Quality z +0.51 (ROE 87%). ⚠️ oversold.

??? success "LRCX (LRCX) — 🟢 Buy, score +0.27"
    Within rebalance band of target 2.9%: no trade. Analyst target 375.06 USD vs 263.45 USD (+42%, 31 analysts); de-biased α -0.5% vs CAPM hurdle 12.6%. Downtrend -7% vs 200-day avg; 12-1 mom +114%; RSI 33. Quality z +0.02 (ROE 65%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.23"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 10,115 JPY (+51%, 23 analysts); de-biased α +1.8% vs CAPM hurdle 12.8%. Uptrend +1% vs 200-day avg; 12-1 mom +71%; RSI 39. Quality z -0.28 (ROE 29%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.18"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 33,880 JPY (+26%, 21 analysts); de-biased α -4.9% vs CAPM hurdle 13.4%. Uptrend +19% vs 200-day avg; 12-1 mom +72%; RSI 43. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.17"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 334.51 USD (+59%, 47 analysts); de-biased α +4.0% vs CAPM hurdle 11.2%. Downtrend -9% vs 200-day avg; 12-1 mom +5%; RSI 39. Quality z +0.26 (ROE 31%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.06"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 240.42 USD (+22%, 43 analysts); de-biased α -6.0% vs CAPM hurdle 14.1%. Uptrend +36% vs 200-day avg; 12-1 mom +193%; RSI 45. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score +0.02"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,630.84 USD (+29%, 16 analysts); de-biased α -3.9% vs CAPM hurdle 12.3%. Uptrend +3% vs 200-day avg; 12-1 mom +67%; RSI 37. Quality z +0.42 (ROE 50%).

??? note "GFS (GFS) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 47.03 USD (+62%, 22 analysts); de-biased α +4.3% vs CAPM hurdle 12.4%. Downtrend -14% vs 200-day avg; 12-1 mom +41%; RSI 47. Quality z -0.21 (ROE 8%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 116.37 USD vs 91.66 USD (+27%, 43 analysts); de-biased α -4.8% vs CAPM hurdle 14.0%. Uptrend +8% vs 200-day avg; 12-1 mom +229%; RSI 34. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 743.80 EUR (+52%, 19 analysts); de-biased α +1.6% vs CAPM hurdle 13.2%. Downtrend -8% vs 200-day avg; 12-1 mom +52%; RSI 32. Quality z -0.10 (ROE 19%).

??? failure "TER (TER) — 🔴 Sell, score -0.28"
    Avoid: not owned. Analyst target 446.47 USD vs 336.17 USD (+33%, 15 analysts); de-biased α -2.9% vs CAPM hurdle 12.3%. Downtrend -3% vs 200-day avg; 12-1 mom +177%; RSI 37. Quality z -0.31 (ROE 20%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.40"
    Avoid: not owned. Analyst target 76.40 USD vs 41.69 USD (+83%, 10 analysts); de-biased α +9.4% vs CAPM hurdle 14.0%. Downtrend -28% vs 200-day avg; 12-1 mom +68%; RSI 30. Quality z -1.00 (ROE 9%). ⚠️ oversold.

??? failure "ARM (ARM) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 288.70 USD vs 220.92 USD (+31%, 40 analysts); de-biased α -5.3% vs CAPM hurdle 19.6%. Downtrend -2% vs 200-day avg; 12-1 mom +95%; RSI 33. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 81,730 JPY vs 52,720 JPY (+55%, 20 analysts); de-biased α +3.0% vs CAPM hurdle 11.5%. Downtrend -20% vs 200-day avg; 12-1 mom -5%; RSI 39. Quality z +0.06 (ROE 25%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -0.84"
    Avoid: not owned. Analyst target 619.51 USD vs 534.60 USD (+16%, 50 analysts); de-biased α -7.8% vs CAPM hurdle 14.9%. Uptrend +35% vs 200-day avg; 12-1 mom +164%; RSI 40. Quality z -0.15 (ROE 7%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 324.71 USD vs 277.92 USD (+17%, 31 analysts); de-biased α -6.1% vs CAPM hurdle 10.8%. Uptrend +9% vs 200-day avg; 12-1 mom +57%; RSI 49. Quality z +0.24 (ROE 30%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 405.47 USD vs 319.93 USD (+27%, 26 analysts); de-biased α -3.9% vs CAPM hurdle 10.0%. Downtrend -2% vs 200-day avg; 12-1 mom -10%; RSI 45. Quality z +0.31 (ROE 22%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.05"
    Avoid: not owned. Analyst target 173.36 USD vs 142.76 USD (+21%, 11 analysts); de-biased α -5.4% vs CAPM hurdle 11.0%. Uptrend +5% vs 200-day avg; 12-1 mom +58%; RSI 42. Quality z -0.02 (ROE 6%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.05"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,893 JPY (+32%, 17 analysts); de-biased α -2.4% vs CAPM hurdle 10.8%. Downtrend -6% vs 200-day avg; 12-1 mom +13%; RSI 45. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.12"
    Avoid: not owned. Analyst target 95.99 HKD vs 51.20 HKD (+87%, 21 analysts); de-biased α +12.0% vs CAPM hurdle 7.3%. Downtrend -26% vs 200-day avg; 12-1 mom -25%; RSI 24. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.17"
    Avoid: not owned. Analyst target 569.78 USD vs 447.60 USD (+27%, 26 analysts); de-biased α -3.8% vs CAPM hurdle 10.3%. Uptrend +0% vs 200-day avg; 12-1 mom -10%; RSI 47. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.40"
    Avoid: not owned. Analyst target 194.13 USD vs 175.60 USD (+11%, 30 analysts); de-biased α -7.9% vs CAPM hurdle 11.9%. Uptrend +4% vs 200-day avg; 12-1 mom +21%; RSI 47. Quality z +0.70 (ROE 23%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,217,000 KRW | $89,984 | 10.1% | Strong Buy |
| MU | Micron Technology | 92 | 895.85 USD | $82,418 | 9.2% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 210,500 KRW | $77,027 | 8.6% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 52.18 EUR | $76,302 | 8.5% | Buy |
| NVDA | NVIDIA | 294 | 216.48 USD | $63,645 | 7.1% | Buy |
| AMAT | Applied Materials | 156 | 404.95 USD | $63,172 | 7.1% | Strong Buy |
| ASX | ASE Technology | 1,332 | 40.78 USD | $54,326 | 6.1% | Buy |
| TSM | TSMC | 117 | 425.30 USD | $49,760 | 5.6% | Buy |
| ASML | ASML Holding | 30 | 1,630.84 USD | $48,925 | 5.5% | Hold |
| KLAC | KLA Corp | 279 | 161.93 USD | $45,177 | 5.1% | Buy |
| AVGO | Broadcom | 100 | 334.51 USD | $33,451 | 3.7% | Hold |
| 8035.T | Tokyo Electron | 500 | 10,115 JPY | $31,972 | 3.6% | Hold |
| LRCX | Lam Research | 105 | 263.45 USD | $27,662 | 3.1% | Buy |
| 6857.T | Advantest | 100 | 33,880 JPY | $21,418 | 2.4% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-10-08 08:59 UTC | ADD | IFX.DE | 479 | 59.28 | $31,780 |
| 2026-10-07 16:29 UTC | TRIM | KLAC | -184 | 195.46 | $35,964 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 32.3%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
