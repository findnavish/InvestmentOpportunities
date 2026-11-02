---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-02 23:31 UTC (Mon Nov 02, 06:31 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Mon 18:31) · Tokyo 🔴 closed (Tue 08:31) · Korea 🔴 closed (Tue 08:31) · Hong Kong 🔴 closed (Tue 07:31) · Xetra 🔴 closed (Tue 00:31) · Euronext Amsterdam 🔴 closed (Tue 00:31)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$889,429** | $352,521 (40%) | $536,908 (60%) | -11.06% | -19.78% | 🔴 Risk-off (-4.8%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $889,429), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **AMAT**<br><small>Applied Materials</small> | 17 | 374.62 USD | $6,369 | Queued · NYSE/Nasdaq closed | analyst α +0.27 · momentum +0.14 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.25 | **SK hynix**<br><small>000660.KS</small> | 1,488,000 KRW | +111% | +12.9% | +282% | -1% | 50 | +0.62 | 10.0% → 8.4% | – | analyst α +0.66 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.35 | **MU**<br><small>Micron Technology</small> | 833.06 USD | +82% | +5.8% | +380% | +11% | 37 | +0.12 | 6.0% → 6.3% | – | momentum +0.53 · analyst α +0.31 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.45 | **Samsung**<br><small>005930.KS</small> | 230,750 KRW | +107% | +12.7% | +182% | -3% | 47 | -0.26 | 6.2% → 5.5% | – | analyst α +0.55 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +0.87 | **MRVL**<br><small>Marvell Technology</small> | 171.35 USD | +72% | +3.0% | +208% | -7% | 29 | -0.12 | 2.2% → 2.4% | – | momentum +0.30 · analyst α +0.19 · ⚠️ oversold, rich valuation |
| 🟢 Buy | +0.74 | **AMAT**<br><small>Applied Materials</small> | 374.62 USD | +71% | +3.5% | +134% | -16% | 33 | +0.03 | 2.0% → 2.7% | ADD 17 | analyst α +0.27 · momentum +0.14 |
| 🟢 Buy | +0.50 | **INTC**<br><small>Intel</small> | 59.95 USD | +94% | +8.7% | +197% | -31% | 23 | -0.62 | 0.9% → 1.2% | – | analyst α +0.41 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.44 | **ASX**<br><small>ASE Technology</small> | 39.17 USD | +30% | -3.3% | +219% | +18% | 43 | -0.68 | 1.4% → 1.8% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.20 | **TSM**<br><small>TSMC</small> | 398.44 USD | +39% | -4.2% | +58% | -0% | 36 | +0.58 | 5.7% → 5.7% | – | quality +0.28 · analyst α -0.15 |
| ⚪ Hold | +0.19 | **NVDA**<br><small>NVIDIA</small> | 202.20 USD | +62% | +0.7% | +16% | -1% | 33 | +0.47 | 4.6% → 4.6% | – | quality +0.21 · momentum -0.20 |
| ⚪ Hold | +0.17 | **Infineon**<br><small>IFX.DE</small> | 52.07 EUR | +67% | +1.9% | +88% | -9% | 44 | -0.04 | 1.5% → 1.5% | – | analyst α +0.12 · quality -0.04 |
| ⚪ Hold | +0.12 | **LRCX**<br><small>Lam Research</small> | 227.66 USD | +65% | +1.8% | +117% | -20% | 31 | +0.02 | 4.1% → 4.1% | – | trend -0.12 · momentum +0.10 |
| ⚪ Hold | +0.09 | **Advantest**<br><small>6857.T</small> | 35,860 JPY | +19% | -9.9% | +121% | +23% | 52 | +0.33 | 5.1% → 5.1% | – | analyst α -0.55 · trend +0.32 · ⚠️ rich valuation |
| ⚪ Hold | +0.09 | **TER**<br><small>Teradyne</small> | 261.02 USD | +71% | +3.4% | +154% | -25% | 27 | -0.31 | 1.0% → 1.0% | – | analyst α +0.23 · quality -0.21 · ⚠️ oversold |
| ⚪ Hold | -0.02 | **KLAC**<br><small>KLA Corp</small> | 153.16 USD | +53% | -0.9% | +71% | -16% | 37 | +0.51 | 4.6% → 4.6% | – | quality +0.24 · trend -0.10 |
| ⚪ Hold | -0.14 | **AMD**<br><small>Advanced Micro Devices</small> | 466.70 USD | +33% | -6.9% | +149% | +13% | 35 | -0.15 | 0.0% → 0.0% | – | analyst α -0.31 · trend +0.18 |
| ⚪ Hold | -0.16 | **GFS**<br><small>GlobalFoundries</small> | 41.87 USD | +82% | +6.0% | +40% | -24% | 37 | -0.21 | 0.0% → 0.0% | – | analyst α +0.36 · trend -0.16 |
| ⚪ Hold | -0.21 | **ASML**<br><small>ASML Holding</small> | 1,526.36 USD | +37% | -5.0% | +74% | -4% | 36 | +0.42 | 5.1% → 5.1% | – | analyst α -0.23 · quality +0.18 |
| 🔴 Sell | -0.32 | **Tokyo Electron**<br><small>8035.T</small> | 10,105 JPY | +51% | -1.5% | +96% | -2% | 46 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α -0.08 |
| 🔴 Sell | -0.43 | **ASMI**<br><small>ASM.AS</small> | 718.20 EUR | +57% | -0.3% | +72% | -12% | 39 | -0.10 | 0.0% → 0.0% | – | momentum -0.07 · quality -0.06 |
| 🔴 Sell | -0.44 | **AVGO**<br><small>Broadcom</small> | 322.41 USD | +65% | +2.2% | -5% | -12% | 39 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · analyst α +0.15 |
| 🔴 Sell | -0.50 | **AMKR**<br><small>Amkor Technology</small> | 36.95 USD | +107% | +12.0% | +77% | -35% | 34 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴 Sell | -0.55 | **ARM**<br><small>Arm Holdings</small> | 196.64 USD | +47% | -4.5% | +86% | -14% | 33 | +0.04 | 0.0% → 0.0% | – | analyst α -0.19 · trend -0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.60 | **Disco**<br><small>6146.T</small> | 50,380 JPY | +62% | +1.5% | +13% | -23% | 41 | +0.06 | 0.0% → 0.0% | – | momentum -0.23 · trend -0.14 |
| 🔴 Sell | -0.73 | **SMIC**<br><small>0981.HK</small> | 43.62 HKD | +120% | +16.9% | -19% | -35% | 25 | -0.99 | 0.0% → 0.0% | – | analyst α +0.85 · momentum -0.53 · ⚠️ oversold |
| 🔴 Sell | -0.73 | **QCOM**<br><small>Qualcomm</small> | 162.07 USD | +20% | -8.9% | +6% | -4% | 37 | +0.70 | 0.0% → 0.0% | – | analyst α -0.48 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.04 | **CDNS**<br><small>Cadence Design Systems</small> | 329.64 USD | +23% | -8.1% | +5% | +1% | 50 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.06 | **SNPS**<br><small>Synopsys</small> | 466.23 USD | +22% | -8.4% | +11% | +5% | 53 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.26 |
| 🔴🔴 Strong Sell | -1.10 | **ENTG**<br><small>Entegris</small> | 151.53 USD | +14% | -10.4% | +91% | +10% | 51 | -0.02 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.14 |
| 🔴🔴 Strong Sell | -1.19 | **TXN**<br><small>Texas Instruments</small> | 302.19 USD | +7% | -11.7% | +88% | +17% | 62 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.21 |
| 🔴🔴 Strong Sell | -1.24 | **Shin-Etsu**<br><small>4063.T</small> | 5,906 JPY | +31% | -5.8% | +25% | -7% | 47 | -0.20 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.17 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.25"
    Within rebalance band of target 8.4%: no trade. Analyst target 3,141,025 KRW vs 1,488,000 KRW (+111%, 38 analysts); de-biased α +12.9% vs CAPM hurdle 14.3%. Downtrend -1% vs 200-day avg; 12-1 mom +282%; RSI 50. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.35"
    Within rebalance band of target 6.3%: no trade. Analyst target 1,520.02 USD vs 833.06 USD (+82%, 46 analysts); de-biased α +5.8% vs CAPM hurdle 14.0%. Uptrend +11% vs 200-day avg; 12-1 mom +380%; RSI 37. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.45"
    Within rebalance band of target 5.5%: no trade. Analyst target 477,517 KRW vs 230,750 KRW (+107%, 36 analysts); de-biased α +12.7% vs CAPM hurdle 11.3%. Downtrend -3% vs 200-day avg; 12-1 mom +182%; RSI 47. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +0.87"
    Within rebalance band of target 2.4%: no trade. Analyst target 293.88 USD vs 171.35 USD (+72%, 43 analysts); de-biased α +3.0% vs CAPM hurdle 14.1%. Downtrend -7% vs 200-day avg; 12-1 mom +208%; RSI 29. Quality z -0.12 (ROE 19%). ⚠️ oversold; price implies 78% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.74"
    **ADD 17 sh** → target 2.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 374.62 USD (+71%, 36 analysts); de-biased α +3.5% vs CAPM hurdle 11.6%. Downtrend -16% vs 200-day avg; 12-1 mom +134%; RSI 33. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.50"
    Within rebalance band of target 1.2%: no trade. Analyst target 116.37 USD vs 59.95 USD (+94%, 43 analysts); de-biased α +8.7% vs CAPM hurdle 14.0%. Downtrend -31% vs 200-day avg; 12-1 mom +197%; RSI 23. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "ASX (ASX) — 🟢 Buy, score +0.44"
    Within rebalance band of target 1.8%: no trade. Analyst target 51.00 USD vs 39.17 USD (+30%, 1 analysts); de-biased α -3.3% vs CAPM hurdle 11.9%. Uptrend +18% vs 200-day avg; 12-1 mom +219%; RSI 43. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "TSM (TSM) — ⚪ Hold, score +0.20"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 398.44 USD (+39%, 20 analysts); de-biased α -4.2% vs CAPM hurdle 10.8%. Downtrend -0% vs 200-day avg; 12-1 mom +58%; RSI 36. Quality z +0.58 (ROE 35%).

??? note "NVDA (NVDA) — ⚪ Hold, score +0.19"
    Hold zone: keep any existing position, no new money. Analyst target 327.70 USD vs 202.20 USD (+62%, 59 analysts); de-biased α +0.7% vs CAPM hurdle 13.9%. Downtrend -1% vs 200-day avg; 12-1 mom +16%; RSI 33. Quality z +0.47 (ROE 101%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.17"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 52.07 EUR (+67%, 23 analysts); de-biased α +1.9% vs CAPM hurdle 14.1%. Downtrend -9% vs 200-day avg; 12-1 mom +88%; RSI 44. Quality z -0.04 (ROE 6%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.12"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 227.66 USD (+65%, 31 analysts); de-biased α +1.8% vs CAPM hurdle 12.6%. Downtrend -20% vs 200-day avg; 12-1 mom +117%; RSI 31. Quality z +0.02 (ROE 65%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.09"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 35,860 JPY (+19%, 21 analysts); de-biased α -9.9% vs CAPM hurdle 13.4%. Uptrend +23% vs 200-day avg; 12-1 mom +121%; RSI 52. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "TER (TER) — ⚪ Hold, score +0.09"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 261.02 USD (+71%, 15 analysts); de-biased α +3.4% vs CAPM hurdle 12.3%. Downtrend -25% vs 200-day avg; 12-1 mom +154%; RSI 27. Quality z -0.31 (ROE 20%). ⚠️ oversold.

??? note "KLAC (KLAC) — ⚪ Hold, score -0.02"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 153.16 USD (+53%, 26 analysts); de-biased α -0.9% vs CAPM hurdle 11.1%. Downtrend -16% vs 200-day avg; 12-1 mom +71%; RSI 37. Quality z +0.51 (ROE 87%).

??? note "AMD (AMD) — ⚪ Hold, score -0.14"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 466.70 USD (+33%, 50 analysts); de-biased α -6.9% vs CAPM hurdle 14.9%. Uptrend +13% vs 200-day avg; 12-1 mom +149%; RSI 35. Quality z -0.15 (ROE 7%).

??? note "GFS (GFS) — ⚪ Hold, score -0.16"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 41.87 USD (+82%, 22 analysts); de-biased α +6.0% vs CAPM hurdle 12.4%. Downtrend -24% vs 200-day avg; 12-1 mom +40%; RSI 37. Quality z -0.21 (ROE 8%).

??? note "ASML (ASML) — ⚪ Hold, score -0.21"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,526.36 USD (+37%, 16 analysts); de-biased α -5.0% vs CAPM hurdle 12.3%. Downtrend -4% vs 200-day avg; 12-1 mom +74%; RSI 36. Quality z +0.42 (ROE 50%).

??? failure "Tokyo Electron (8035.T) — 🔴 Sell, score -0.32"
    Avoid: not owned. Analyst target 15,275 JPY vs 10,105 JPY (+51%, 23 analysts); de-biased α -1.5% vs CAPM hurdle 12.8%. Downtrend -2% vs 200-day avg; 12-1 mom +96%; RSI 46. Quality z -0.28 (ROE 29%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.43"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 718.20 EUR (+57%, 19 analysts); de-biased α -0.3% vs CAPM hurdle 13.2%. Downtrend -12% vs 200-day avg; 12-1 mom +72%; RSI 39. Quality z -0.10 (ROE 19%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 531.31 USD vs 322.41 USD (+65%, 47 analysts); de-biased α +2.2% vs CAPM hurdle 11.2%. Downtrend -12% vs 200-day avg; 12-1 mom -5%; RSI 39. Quality z +0.26 (ROE 31%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.50"
    Avoid: not owned. Analyst target 76.40 USD vs 36.95 USD (+107%, 10 analysts); de-biased α +12.0% vs CAPM hurdle 14.0%. Downtrend -35% vs 200-day avg; 12-1 mom +77%; RSI 34. Quality z -1.00 (ROE 9%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 288.70 USD vs 196.64 USD (+47%, 40 analysts); de-biased α -4.5% vs CAPM hurdle 19.6%. Downtrend -14% vs 200-day avg; 12-1 mom +86%; RSI 33. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.60"
    Avoid: not owned. Analyst target 81,730 JPY vs 50,380 JPY (+62%, 20 analysts); de-biased α +1.5% vs CAPM hurdle 11.5%. Downtrend -23% vs 200-day avg; 12-1 mom +13%; RSI 41. Quality z +0.06 (ROE 25%).

??? failure "SMIC (0981.HK) — 🔴 Sell, score -0.73"
    Avoid: not owned. Analyst target 95.99 HKD vs 43.62 HKD (+120%, 21 analysts); de-biased α +16.9% vs CAPM hurdle 7.3%. Downtrend -35% vs 200-day avg; 12-1 mom -19%; RSI 25. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.73"
    Avoid: not owned. Analyst target 194.13 USD vs 162.07 USD (+20%, 30 analysts); de-biased α -8.9% vs CAPM hurdle 11.9%. Downtrend -4% vs 200-day avg; 12-1 mom +6%; RSI 37. Quality z +0.70 (ROE 23%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.04"
    Avoid: not owned. Analyst target 405.47 USD vs 329.64 USD (+23%, 26 analysts); de-biased α -8.1% vs CAPM hurdle 10.0%. Uptrend +1% vs 200-day avg; 12-1 mom +5%; RSI 50. Quality z +0.31 (ROE 22%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.06"
    Avoid: not owned. Analyst target 569.78 USD vs 466.23 USD (+22%, 26 analysts); de-biased α -8.4% vs CAPM hurdle 10.3%. Uptrend +5% vs 200-day avg; 12-1 mom +11%; RSI 53. Quality z +0.14 (ROE 7%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.10"
    Avoid: not owned. Analyst target 173.36 USD vs 151.53 USD (+14%, 11 analysts); de-biased α -10.4% vs CAPM hurdle 11.0%. Uptrend +10% vs 200-day avg; 12-1 mom +91%; RSI 51. Quality z -0.02 (ROE 6%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.19"
    Avoid: not owned. Analyst target 324.71 USD vs 302.19 USD (+7%, 31 analysts); de-biased α -11.7% vs CAPM hurdle 10.8%. Uptrend +17% vs 200-day avg; 12-1 mom +88%; RSI 62. Quality z +0.24 (ROE 30%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.24"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,906 JPY (+31%, 17 analysts); de-biased α -5.8% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +25%; RSI 47. Quality z -0.20 (ROE 10%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 80 | 1,488,000 KRW | $88,541 | 10.0% | Strong Buy |
| 005930.KS | Samsung Electronics | 322 | 230,750 KRW | $55,265 | 6.2% | Strong Buy |
| MU | Micron Technology | 64 | 833.06 USD | $53,316 | 6.0% | Strong Buy |
| TSM | TSMC | 127 | 398.44 USD | $50,602 | 5.7% | Hold |
| ASML | ASML Holding | 30 | 1,526.36 USD | $45,791 | 5.1% | Hold |
| 6857.T | Advantest | 200 | 35,860 JPY | $45,420 | 5.1% | Hold |
| KLAC | KLA Corp | 268 | 153.16 USD | $41,047 | 4.6% | Hold |
| NVDA | NVIDIA | 201 | 202.20 USD | $40,642 | 4.6% | Hold |
| LRCX | Lam Research | 162 | 227.66 USD | $36,881 | 4.1% | Hold |
| MRVL | Marvell Technology | 114 | 171.35 USD | $19,534 | 2.2% | Strong Buy |
| AMAT | Applied Materials | 47 | 374.62 USD | $17,607 | 2.0% | Buy |
| IFX.DE | Infineon Technologies | 225 | 52.07 EUR | $13,111 | 1.5% | Hold |
| ASX | ASE Technology | 312 | 39.17 USD | $12,223 | 1.4% | Buy |
| TER | Teradyne | 35 | 261.02 USD | $9,136 | 1.0% | Hold |
| INTC | Intel | 130 | 59.95 USD | $7,794 | 0.9% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-10-23 19:14 UTC | ADD | KLAC | 57 | 145.31 | $8,282 |
| 2026-10-23 15:05 UTC | ADD | ASX | 383 | 38.70 | $14,822 |
| 2026-10-23 15:05 UTC | TRIM | NVDA | -68 | 212.70 | $14,464 |
| 2026-10-22 15:18 UTC | ADD | LRCX | 57 | 234.49 | $13,366 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 45.4%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
