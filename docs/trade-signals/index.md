---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-04 01:22 UTC (Tue Nov 03, 08:22 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Tue 20:22) · Tokyo 🟢 open (Wed 10:22) · Korea 🟢 open (Wed 10:22) · Hong Kong 🔴 closed (Wed 09:22) · Xetra 🔴 closed (Wed 02:22) · Euronext Amsterdam 🔴 closed (Wed 02:22)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$887,049** | $360,906 (41%) | $526,143 (59%) | -11.30% | -17.77% | 🔴 Risk-off (-2.4%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $887,049), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

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
| 🟢🟢 Strong Buy | +3.22 | **SK hynix**<br><small>000660.KS</small> | 1,421,000 KRW | +121% | +15.4% | +286% | -5% | 46 | +0.62 | 9.6% → 9.3% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.39 | **MU**<br><small>Micron Technology</small> | 854.97 USD | +78% | +4.6% | +376% | +14% | 40 | +0.12 | 6.2% → 7.1% | – | momentum +0.53 · analyst α +0.31 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.61 | **Samsung**<br><small>005930.KS</small> | 221,000 KRW | +116% | +15.0% | +193% | -6% | 43 | -0.26 | 6.0% → 6.8% | – | analyst α +0.55 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +0.87 | **MRVL**<br><small>Marvell Technology</small> | 171.89 USD | +71% | +2.9% | +190% | -7% | 29 | -0.12 | 3.2% → 2.7% | – | analyst α +0.23 · momentum +0.23 · ⚠️ oversold, rich valuation |
| 🟢 Buy | +0.58 | **AMAT**<br><small>Applied Materials</small> | 382.16 USD | +67% | +2.7% | +134% | -14% | 36 | +0.03 | 2.7% → 2.4% | – | analyst α +0.19 · momentum +0.14 |
| 🟢 Buy | +0.51 | **INTC**<br><small>Intel</small> | 60.50 USD | +92% | +8.3% | +191% | -30% | 24 | -0.62 | 1.6% → 1.4% | – | analyst α +0.41 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.36 | **ASX**<br><small>ASE Technology</small> | 39.05 USD | +31% | -3.2% | +200% | +17% | 43 | -0.68 | 1.4% → 1.6% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.24 | **TSM**<br><small>TSMC</small> | 404.66 USD | +36% | -4.7% | +63% | +1% | 39 | +0.58 | 5.8% → 5.8% | – | quality +0.28 · analyst α -0.15 |
| ⚪ Hold | +0.22 | **Infineon**<br><small>IFX.DE</small> | 52.61 EUR | +65% | +1.5% | +87% | -8% | 46 | -0.04 | 1.5% → 1.5% | – | analyst α +0.12 · momentum +0.05 |
| ⚪ Hold | +0.18 | **NVDA**<br><small>NVIDIA</small> | 206.57 USD | +59% | -0.1% | +18% | +1% | 39 | +0.47 | 1.4% → 1.4% | – | quality +0.21 · momentum -0.20 |
| ⚪ Hold | +0.12 | **LRCX**<br><small>Lam Research</small> | 230.75 USD | +63% | +1.3% | +121% | -19% | 33 | +0.02 | 4.2% → 4.2% | – | trend -0.12 · momentum +0.10 |
| ⚪ Hold | -0.03 | **AMD**<br><small>Advanced Micro Devices</small> | 484.47 USD | +28% | -8.1% | +147% | +17% | 39 | -0.15 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.25 |
| ⚪ Hold | -0.05 | **KLAC**<br><small>KLA Corp</small> | 156.22 USD | +50% | -1.6% | +72% | -14% | 40 | +0.51 | 4.7% → 4.7% | – | quality +0.24 · trend -0.10 |
| ⚪ Hold | -0.05 | **Advantest**<br><small>6857.T</small> | 33,910 JPY | +26% | -8.1% | +121% | +17% | 47 | +0.33 | 4.8% → 4.8% | – | analyst α -0.48 · trend +0.18 · ⚠️ rich valuation |
| ⚪ Hold | -0.08 | **ASML**<br><small>ASML Holding</small> | 1,551.99 USD | +35% | -5.5% | +76% | -3% | 39 | +0.42 | 5.2% → 5.2% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | -0.09 | **TER**<br><small>Teradyne</small> | 269.31 USD | +66% | +2.1% | +145% | -23% | 30 | -0.31 | 1.1% → 1.1% | – | quality -0.21 · momentum +0.17 |
| ⚪ Hold | -0.12 | **GFS**<br><small>GlobalFoundries</small> | 42.95 USD | +77% | +4.9% | +37% | -22% | 41 | -0.21 | 0.0% → 0.0% | – | analyst α +0.36 · momentum -0.14 |
| ⚪ Hold | -0.21 | **Disco**<br><small>6146.T</small> | 47,020 JPY | +74% | +4.5% | +13% | -28% | 35 | +0.06 | 0.0% → 0.0% | – | analyst α +0.27 · momentum -0.23 |
| ⚪ Hold | -0.24 | **Tokyo Electron**<br><small>8035.T</small> | 9,548 JPY | +60% | +0.8% | +96% | -8% | 41 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.07 |
| 🔴 Sell | -0.50 | **ASMI**<br><small>ASM.AS</small> | 725.80 EUR | +55% | -0.7% | +75% | -11% | 40 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · trend -0.06 |
| 🔴 Sell | -0.66 | **AVGO**<br><small>Broadcom</small> | 332.09 USD | +60% | +1.1% | -1% | -9% | 45 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴 Sell | -0.66 | **AMKR**<br><small>Amkor Technology</small> | 37.62 USD | +103% | +11.1% | +70% | -34% | 36 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.74 | **ARM**<br><small>Arm Holdings</small> | 202.77 USD | +42% | -5.6% | +78% | -12% | 36 | +0.04 | 0.0% → 0.0% | – | analyst α -0.27 · trend -0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.74 | **SMIC**<br><small>0981.HK</small> | 42.62 HKD | +125% | +18.2% | -23% | -37% | 23 | -0.99 | 0.0% → 0.0% | – | analyst α +0.85 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -0.91 | **CDNS**<br><small>Cadence Design Systems</small> | 323.75 USD | +25% | -7.5% | +4% | -1% | 47 | +0.31 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.30 |
| 🔴🔴 Strong Sell | -0.91 | **TXN**<br><small>Texas Instruments</small> | 312.58 USD | +4% | -12.6% | +86% | +21% | 67 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -0.94 | **QCOM**<br><small>Qualcomm</small> | 164.50 USD | +18% | -9.3% | +2% | -2% | 40 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.08 | **SNPS**<br><small>Synopsys</small> | 463.01 USD | +23% | -8.1% | +8% | +5% | 51 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.26 |
| 🔴🔴 Strong Sell | -1.08 | **Shin-Etsu**<br><small>4063.T</small> | 5,854 JPY | +33% | -5.4% | +25% | -7% | 45 | -0.20 | 0.0% → 0.0% | – | analyst α -0.19 · momentum -0.17 |
| 🔴🔴 Strong Sell | -1.21 | **ENTG**<br><small>Entegris</small> | 152.79 USD | +13% | -10.6% | +83% | +10% | 52 | -0.02 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.14 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.22"
    Within rebalance band of target 9.3%: no trade. Analyst target 3,141,025 KRW vs 1,421,000 KRW (+121%, 38 analysts); de-biased α +15.4% vs CAPM hurdle 14.3%. Downtrend -5% vs 200-day avg; 12-1 mom +286%; RSI 46. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.39"
    Within rebalance band of target 7.1%: no trade. Analyst target 1,520.02 USD vs 854.97 USD (+78%, 46 analysts); de-biased α +4.6% vs CAPM hurdle 14.0%. Uptrend +14% vs 200-day avg; 12-1 mom +376%; RSI 40. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.61"
    Within rebalance band of target 6.8%: no trade. Analyst target 477,517 KRW vs 221,000 KRW (+116%, 36 analysts); de-biased α +15.0% vs CAPM hurdle 11.3%. Downtrend -6% vs 200-day avg; 12-1 mom +193%; RSI 43. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +0.87"
    Within rebalance band of target 2.7%: no trade. Analyst target 293.88 USD vs 171.89 USD (+71%, 43 analysts); de-biased α +2.9% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +190%; RSI 29. Quality z -0.12 (ROE 19%). ⚠️ oversold; price implies 78% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.58"
    Within rebalance band of target 2.4%: no trade. Analyst target 638.94 USD vs 382.16 USD (+67%, 36 analysts); de-biased α +2.7% vs CAPM hurdle 11.6%. Downtrend -14% vs 200-day avg; 12-1 mom +134%; RSI 36. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.51"
    Within rebalance band of target 1.4%: no trade. Analyst target 116.37 USD vs 60.50 USD (+92%, 43 analysts); de-biased α +8.3% vs CAPM hurdle 14.0%. Downtrend -30% vs 200-day avg; 12-1 mom +191%; RSI 24. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "ASX (ASX) — 🟢 Buy, score +0.36"
    Within rebalance band of target 1.6%: no trade. Analyst target 51.00 USD vs 39.05 USD (+31%, 1 analysts); de-biased α -3.2% vs CAPM hurdle 11.9%. Uptrend +17% vs 200-day avg; 12-1 mom +200%; RSI 43. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "TSM (TSM) — ⚪ Hold, score +0.24"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 404.66 USD (+36%, 20 analysts); de-biased α -4.7% vs CAPM hurdle 10.8%. Uptrend +1% vs 200-day avg; 12-1 mom +63%; RSI 39. Quality z +0.58 (ROE 35%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 52.61 EUR (+65%, 23 analysts); de-biased α +1.5% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +87%; RSI 46. Quality z -0.04 (ROE 6%).

??? note "NVDA (NVDA) — ⚪ Hold, score +0.18"
    Hold zone: keep any existing position, no new money. Analyst target 327.70 USD vs 206.57 USD (+59%, 59 analysts); de-biased α -0.1% vs CAPM hurdle 13.9%. Uptrend +1% vs 200-day avg; 12-1 mom +18%; RSI 39. Quality z +0.47 (ROE 101%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.12"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 230.75 USD (+63%, 31 analysts); de-biased α +1.3% vs CAPM hurdle 12.6%. Downtrend -19% vs 200-day avg; 12-1 mom +121%; RSI 33. Quality z +0.02 (ROE 65%).

??? note "AMD (AMD) — ⚪ Hold, score -0.03"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 484.47 USD (+28%, 50 analysts); de-biased α -8.1% vs CAPM hurdle 14.9%. Uptrend +17% vs 200-day avg; 12-1 mom +147%; RSI 39. Quality z -0.15 (ROE 7%).

??? note "KLAC (KLAC) — ⚪ Hold, score -0.05"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 156.22 USD (+50%, 26 analysts); de-biased α -1.6% vs CAPM hurdle 11.1%. Downtrend -14% vs 200-day avg; 12-1 mom +72%; RSI 40. Quality z +0.51 (ROE 87%).

??? note "Advantest (6857.T) — ⚪ Hold, score -0.05"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 33,910 JPY (+26%, 21 analysts); de-biased α -8.1% vs CAPM hurdle 13.4%. Uptrend +17% vs 200-day avg; 12-1 mom +121%; RSI 47. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "ASML (ASML) — ⚪ Hold, score -0.08"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,551.99 USD (+35%, 16 analysts); de-biased α -5.5% vs CAPM hurdle 12.3%. Downtrend -3% vs 200-day avg; 12-1 mom +76%; RSI 39. Quality z +0.42 (ROE 50%).

??? note "TER (TER) — ⚪ Hold, score -0.09"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 269.31 USD (+66%, 15 analysts); de-biased α +2.1% vs CAPM hurdle 12.3%. Downtrend -23% vs 200-day avg; 12-1 mom +145%; RSI 30. Quality z -0.31 (ROE 20%).

??? note "GFS (GFS) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 42.95 USD (+77%, 22 analysts); de-biased α +4.9% vs CAPM hurdle 12.4%. Downtrend -22% vs 200-day avg; 12-1 mom +37%; RSI 41. Quality z -0.21 (ROE 8%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.21"
    Hold zone: not owned, no entry. Analyst target 81,730 JPY vs 47,020 JPY (+74%, 20 analysts); de-biased α +4.5% vs CAPM hurdle 11.5%. Downtrend -28% vs 200-day avg; 12-1 mom +13%; RSI 35. Quality z +0.06 (ROE 25%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 9,548 JPY (+60%, 23 analysts); de-biased α +0.8% vs CAPM hurdle 12.8%. Downtrend -8% vs 200-day avg; 12-1 mom +96%; RSI 41. Quality z -0.28 (ROE 29%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 725.80 EUR (+55%, 19 analysts); de-biased α -0.7% vs CAPM hurdle 13.2%. Downtrend -11% vs 200-day avg; 12-1 mom +75%; RSI 40. Quality z -0.10 (ROE 19%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.66"
    Avoid: not owned. Analyst target 531.31 USD vs 332.09 USD (+60%, 47 analysts); de-biased α +1.1% vs CAPM hurdle 11.2%. Downtrend -9% vs 200-day avg; 12-1 mom -1%; RSI 45. Quality z +0.26 (ROE 31%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.66"
    Avoid: not owned. Analyst target 76.40 USD vs 37.62 USD (+103%, 10 analysts); de-biased α +11.1% vs CAPM hurdle 14.0%. Downtrend -34% vs 200-day avg; 12-1 mom +70%; RSI 36. Quality z -1.00 (ROE 9%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.74"
    Avoid: not owned. Analyst target 288.70 USD vs 202.77 USD (+42%, 40 analysts); de-biased α -5.6% vs CAPM hurdle 19.6%. Downtrend -12% vs 200-day avg; 12-1 mom +78%; RSI 36. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SMIC (0981.HK) — 🔴 Sell, score -0.74"
    Avoid: not owned. Analyst target 95.99 HKD vs 42.62 HKD (+125%, 21 analysts); de-biased α +18.2% vs CAPM hurdle 7.3%. Downtrend -37% vs 200-day avg; 12-1 mom -23%; RSI 23. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 405.47 USD vs 323.75 USD (+25%, 26 analysts); de-biased α -7.5% vs CAPM hurdle 10.0%. Downtrend -1% vs 200-day avg; 12-1 mom +4%; RSI 47. Quality z +0.31 (ROE 22%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 324.71 USD vs 312.58 USD (+4%, 31 analysts); de-biased α -12.6% vs CAPM hurdle 10.8%. Uptrend +21% vs 200-day avg; 12-1 mom +86%; RSI 67. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 194.13 USD vs 164.50 USD (+18%, 30 analysts); de-biased α -9.3% vs CAPM hurdle 11.9%. Downtrend -2% vs 200-day avg; 12-1 mom +2%; RSI 40. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.08"
    Avoid: not owned. Analyst target 569.78 USD vs 463.01 USD (+23%, 26 analysts); de-biased α -8.1% vs CAPM hurdle 10.3%. Uptrend +5% vs 200-day avg; 12-1 mom +8%; RSI 51. Quality z +0.14 (ROE 7%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.08"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,854 JPY (+33%, 17 analysts); de-biased α -5.4% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +25%; RSI 45. Quality z -0.20 (ROE 10%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.21"
    Avoid: not owned. Analyst target 173.36 USD vs 152.79 USD (+13%, 11 analysts); de-biased α -10.6% vs CAPM hurdle 11.0%. Uptrend +10% vs 200-day avg; 12-1 mom +83%; RSI 52. Quality z -0.02 (ROE 6%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 80 | 1,421,000 KRW | $84,793 | 9.6% | Strong Buy |
| MU | Micron Technology | 64 | 854.97 USD | $54,718 | 6.2% | Strong Buy |
| 005930.KS | Samsung Electronics | 322 | 221,000 KRW | $53,079 | 6.0% | Strong Buy |
| TSM | TSMC | 127 | 404.66 USD | $51,392 | 5.8% | Hold |
| ASML | ASML Holding | 30 | 1,551.99 USD | $46,560 | 5.2% | Hold |
| 6857.T | Advantest | 200 | 33,910 JPY | $42,877 | 4.8% | Hold |
| KLAC | KLA Corp | 268 | 156.22 USD | $41,867 | 4.7% | Hold |
| LRCX | Lam Research | 162 | 230.75 USD | $37,382 | 4.2% | Hold |
| MRVL | Marvell Technology | 164 | 171.89 USD | $28,190 | 3.2% | Strong Buy |
| AMAT | Applied Materials | 62 | 382.16 USD | $23,694 | 2.7% | Buy |
| INTC | Intel | 236 | 60.50 USD | $14,278 | 1.6% | Buy |
| IFX.DE | Infineon Technologies | 225 | 52.61 EUR | $13,311 | 1.5% | Hold |
| NVDA | NVIDIA | 60 | 206.57 USD | $12,394 | 1.4% | Hold |
| ASX | ASE Technology | 312 | 39.05 USD | $12,184 | 1.4% | Buy |
| TER | Teradyne | 35 | 269.31 USD | $9,426 | 1.1% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-03 15:09 UTC | ADD | INTC | 106 | 62.03 | $6,576 |
| 2026-11-03 15:09 UTC | ADD | MRVL | 50 | 172.03 | $8,602 |
| 2026-11-03 15:09 UTC | ADD | AMAT | 15 | 385.21 | $5,778 |
| 2026-11-03 15:09 UTC | TRIM | NVDA | -141 | 208.26 | $29,365 |
| 2026-11-02 15:55 UTC | BUY (new) | TER | 35 | 270.99 | $9,485 |
| 2026-11-02 15:55 UTC | ADD | MRVL | 35 | 184.11 | $6,444 |
| 2026-11-02 15:55 UTC | TRIM | IFX.DE | -1,076 | 52.66 | $63,473 |
| 2026-11-02 06:06 UTC | TRIM | 000660.KS | -18 | 1,490,500.00 | $20,008 |
| 2026-11-02 06:06 UTC | TRIM | 005930.KS | -163 | 231,750.00 | $28,171 |
| 2026-11-02 06:06 UTC | SELL (exit) | 8035.T | -500 | 10,115.00 | $32,062 |
| 2026-10-30 19:24 UTC | TRIM | MU | -28 | 866.70 | $24,267 |
| 2026-10-30 19:24 UTC | TRIM | AMAT | -65 | 385.15 | $25,035 |
| 2026-10-30 19:24 UTC | TRIM | MRVL | -139 | 193.20 | $26,855 |
| 2026-10-30 19:24 UTC | TRIM | INTC | -391 | 63.40 | $24,787 |
| 2026-10-30 19:24 UTC | TRIM | ASX | -1,008 | 38.89 | $39,201 |
| 2026-10-30 14:10 UTC | BUY (new) | INTC | 521 | 65.38 | $34,063 |
| 2026-10-30 14:10 UTC | TRIM | AMAT | -33 | 399.62 | $13,187 |
| 2026-10-29 14:21 UTC | BUY (new) | MRVL | 218 | 219.82 | $47,921 |
| 2026-10-29 14:21 UTC | TRIM | NVDA | -84 | 213.56 | $17,939 |
| 2026-10-29 14:21 UTC | SELL (exit) | AVGO | -100 | 342.58 | $34,258 |
| 2026-10-28 16:04 UTC | ADD | NVDA | 117 | 217.19 | $25,411 |
| 2026-10-26 19:22 UTC | TRIM | AMAT | -57 | 391.16 | $22,296 |
| 2026-10-26 19:22 UTC | TRIM | NVDA | -58 | 216.65 | $12,566 |
| 2026-10-26 19:22 UTC | TRIM | ASX | -395 | 40.15 | $15,859 |
| 2026-10-26 06:15 UTC | ADD | 6857.T | 100 | 31,220.00 | $19,871 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 45.2%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
