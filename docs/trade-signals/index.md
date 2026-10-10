---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-10 22:33 UTC (Sat Oct 10, 06:33 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Sat 18:33) · Tokyo 🔴 closed (Sun 07:33) · Korea 🔴 closed (Sun 07:33) · Hong Kong 🔴 closed (Sun 06:33) · Xetra 🔴 closed (Sun 00:33) · Euronext Amsterdam 🔴 closed (Sun 00:33)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$1,018,577** | $158,584 (16%) | $859,993 (84%) | +1.86% | -1.01% | 🟢 Risk-on (+21.2%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $1,018,577), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **NVDA**<br><small>NVIDIA</small> | 80 | 229.34 USD | $18,347 | Queued · NYSE/Nasdaq closed | analyst α +0.23 · momentum -0.23 |
| ADD | **KLAC**<br><small>KLA Corp</small> | 61 | 195.64 USD | $11,934 | Queued · NYSE/Nasdaq closed | quality +0.24 · trend -0.07 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.41 | **SK hynix**<br><small>000660.KS</small> | 1,699,000 KRW | +85% | +13.6% | +395% | +18% | 45 | +0.62 | 9.2% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.08 | **MU**<br><small>Micron Technology</small> | 1,028.14 USD | +48% | +4.4% | +408% | +46% | 50 | +0.12 | 9.3% → 10.0% | – | momentum +0.53 · analyst α +0.27 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.68 | **Samsung**<br><small>005930.KS</small> | 264,000 KRW | +81% | +13.4% | +223% | +15% | 49 | -0.26 | 9.4% → 10.0% | – | analyst α +0.66 · momentum +0.30 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.55 | **AMAT**<br><small>Applied Materials</small> | 506.85 USD | +26% | -0.4% | +108% | +17% | 54 | +0.03 | 8.0% → 8.3% | – | analyst α +0.12 · momentum +0.10 |
| 🟢 Buy | +0.49 | **TSM**<br><small>TSMC</small> | 453.26 USD | +22% | -1.2% | +46% | +16% | 53 | +0.58 | 8.3% → 10.0% | – | quality +0.28 · momentum -0.12 |
| 🟢 Buy | +0.46 | **ASX**<br><small>ASE Technology</small> | 46.43 USD | +10% | -2.2% | +239% | +48% | 62 | -0.68 | 6.9% → 7.7% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.42 | **Infineon**<br><small>IFX.DE</small> | 58.70 EUR | +48% | +4.4% | +81% | +4% | 49 | -0.04 | 6.3% → 7.5% | – | analyst α +0.31 · trend -0.12 |
| 🟢 Buy | +0.37 | **NVDA**<br><small>NVIDIA</small> | 229.34 USD | +43% | +3.2% | +14% | +14% | 53 | +0.47 | 8.4% → 6.5% | TRIM 80 | analyst α +0.23 · momentum -0.23 |
| 🟢 Buy | +0.33 | **KLAC**<br><small>KLA Corp</small> | 195.64 USD | +19% | -1.9% | +72% | +9% | 55 | +0.51 | 4.2% → 5.4% | ADD 61 | quality +0.24 · trend -0.07 |
| ⚪ Hold | +0.22 | **ASML**<br><small>ASML Holding</small> | 1,781.44 USD | +18% | -2.6% | +74% | +14% | 53 | +0.42 | 0.0% → 0.0% | – | quality +0.18 · analyst α -0.08 |
| ⚪ Hold | +0.09 | **Tokyo Electron**<br><small>8035.T</small> | 12,430 JPY | +23% | -1.3% | +107% | +26% | 62 | -0.28 | 4.6% → 4.6% | – | quality -0.18 · trend +0.14 |
| ⚪ Hold | +0.09 | **AVGO**<br><small>Broadcom</small> | 361.63 USD | +47% | +5.0% | +6% | -2% | 50 | +0.26 | 4.8% → 4.8% | – | analyst α +0.36 · momentum -0.30 |
| ⚪ Hold | -0.02 | **GFS**<br><small>GlobalFoundries</small> | 48.24 USD | +58% | +7.2% | +33% | -11% | 51 | -0.21 | 0.0% → 0.0% | – | analyst α +0.48 · trend -0.21 |
| ⚪ Hold | -0.08 | **MRVL**<br><small>Marvell Technology</small> | 275.33 USD | +7% | -5.9% | +161% | +59% | 62 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.32 · ⚠️ rich valuation |
| ⚪ Hold | -0.10 | **Advantest**<br><small>6857.T</small> | 41,560 JPY | +3% | -6.7% | +134% | +48% | 71 | +0.33 | 5.2% → 5.2% | – | analyst α -0.55 · trend +0.18 · ⚠️ rich valuation |
| ⚪ Hold | -0.10 | **LRCX**<br><small>Lam Research</small> | 318.83 USD | +18% | -2.8% | +112% | +14% | 51 | +0.02 | 0.0% → 0.0% | – | analyst α -0.15 · momentum +0.12 |
| ⚪ Hold | -0.18 | **ASMI**<br><small>ASM.AS</small> | 888.00 EUR | +27% | -0.6% | +52% | +11% | 54 | -0.10 | 0.0% → 0.0% | – | analyst α +0.08 · quality -0.06 |
| 🔴 Sell | -0.29 | **Disco**<br><small>6146.T</small> | 61,250 JPY | +33% | +1.6% | +16% | -6% | 58 | +0.06 | 0.0% → 0.0% | – | momentum -0.20 · analyst α +0.19 |
| 🔴 Sell | -0.34 | **TXN**<br><small>Texas Instruments</small> | 283.74 USD | +14% | -2.7% | +46% | +13% | 56 | +0.24 | 0.0% → 0.0% | – | analyst α -0.12 · momentum -0.10 |
| 🔴 Sell | -0.42 | **QCOM**<br><small>Qualcomm</small> | 175.56 USD | +11% | -4.0% | +12% | +4% | 45 | +0.70 | 0.0% → 0.0% | – | quality +0.43 · analyst α -0.27 |
| 🔴 Sell | -0.46 | **INTC**<br><small>Intel</small> | 104.70 USD | +11% | -4.8% | +168% | +26% | 43 | -0.62 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.49 | **TER**<br><small>Teradyne</small> | 402.64 USD | +11% | -4.4% | +162% | +18% | 53 | -0.31 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.23 |
| 🔴 Sell | -0.55 | **AMKR**<br><small>Amkor Technology</small> | 49.14 USD | +55% | +6.4% | +70% | -14% | 43 | -1.00 | 0.0% → 0.0% | – | quality -0.43 · analyst α +0.41 |
| 🔴 Sell | -0.58 | **Shin-Etsu**<br><small>4063.T</small> | 6,110 JPY | +27% | +0.4% | +21% | -2% | 55 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · trend -0.16 |
| 🔴🔴 Strong Sell | -0.85 | **ENTG**<br><small>Entegris</small> | 165.87 USD | +5% | -5.7% | +49% | +23% | 65 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.10 |
| 🔴🔴 Strong Sell | -0.90 | **SMIC**<br><small>0981.HK</small> | 57.65 HKD | +67% | +10.7% | -15% | -17% | 34 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.13 | **CDNS**<br><small>Cadence Design Systems</small> | 352.97 USD | +15% | -2.9% | -17% | +8% | 66 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -1.14 | **AMD**<br><small>Advanced Micro Devices</small> | 608.09 USD | +2% | -7.4% | +122% | +57% | 57 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.19 | **ARM**<br><small>Arm Holdings</small> | 266.55 USD | +8% | -6.9% | +55% | +21% | 44 | +0.04 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.09 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.39 | **SNPS**<br><small>Synopsys</small> | 509.95 USD | +12% | -3.7% | -18% | +14% | 75 | +0.14 | 0.0% → 0.0% | – | momentum -0.53 · analyst α -0.23 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.41"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,699,000 KRW (+85%, 38 analysts); de-biased α +13.6% vs CAPM hurdle 14.3%. Uptrend +18% vs 200-day avg; 12-1 mom +395%; RSI 45. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.08"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 1,028.14 USD (+48%, 46 analysts); de-biased α +4.4% vs CAPM hurdle 14.0%. Uptrend +46% vs 200-day avg; 12-1 mom +408%; RSI 50. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.68"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 264,000 KRW (+81%, 36 analysts); de-biased α +13.4% vs CAPM hurdle 11.3%. Uptrend +15% vs 200-day avg; 12-1 mom +223%; RSI 49. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.55"
    Within rebalance band of target 8.3%: no trade. Analyst target 638.94 USD vs 506.85 USD (+26%, 36 analysts); de-biased α -0.4% vs CAPM hurdle 11.6%. Uptrend +17% vs 200-day avg; 12-1 mom +108%; RSI 54. Quality z +0.03 (ROE 36%).

??? success "TSM (TSM) — 🟢 Buy, score +0.49"
    Within rebalance band of target 10.0%: no trade. Analyst target 552.26 USD vs 453.26 USD (+22%, 20 analysts); de-biased α -1.2% vs CAPM hurdle 10.8%. Uptrend +16% vs 200-day avg; 12-1 mom +46%; RSI 53. Quality z +0.58 (ROE 35%).

??? success "ASX (ASX) — 🟢 Buy, score +0.46"
    Within rebalance band of target 7.7%: no trade. Analyst target 51.00 USD vs 46.43 USD (+10%, 1 analysts); de-biased α -2.2% vs CAPM hurdle 11.9%. Uptrend +48% vs 200-day avg; 12-1 mom +239%; RSI 62. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.42"
    Within rebalance band of target 7.5%: no trade. Analyst target 86.74 EUR vs 58.70 EUR (+48%, 23 analysts); de-biased α +4.4% vs CAPM hurdle 14.1%. Uptrend +4% vs 200-day avg; 12-1 mom +81%; RSI 49. Quality z -0.04 (ROE 6%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.37"
    **TRIM 80 sh** → target 6.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 229.34 USD (+43%, 59 analysts); de-biased α +3.2% vs CAPM hurdle 13.9%. Uptrend +14% vs 200-day avg; 12-1 mom +14%; RSI 53. Quality z +0.47 (ROE 101%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.33"
    **ADD 61 sh** → target 5.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 233.77 USD vs 195.64 USD (+19%, 26 analysts); de-biased α -1.9% vs CAPM hurdle 11.1%. Uptrend +9% vs 200-day avg; 12-1 mom +72%; RSI 55. Quality z +0.51 (ROE 87%).

??? note "ASML (ASML) — ⚪ Hold, score +0.22"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,781.44 USD (+18%, 16 analysts); de-biased α -2.6% vs CAPM hurdle 12.3%. Uptrend +14% vs 200-day avg; 12-1 mom +74%; RSI 53. Quality z +0.42 (ROE 50%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.09"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 12,430 JPY (+23%, 23 analysts); de-biased α -1.3% vs CAPM hurdle 12.8%. Uptrend +26% vs 200-day avg; 12-1 mom +107%; RSI 62. Quality z -0.28 (ROE 29%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.09"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 361.63 USD (+47%, 47 analysts); de-biased α +5.0% vs CAPM hurdle 11.2%. Downtrend -2% vs 200-day avg; 12-1 mom +6%; RSI 50. Quality z +0.26 (ROE 31%).

??? note "GFS (GFS) — ⚪ Hold, score -0.02"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 48.24 USD (+58%, 22 analysts); de-biased α +7.2% vs CAPM hurdle 12.4%. Downtrend -11% vs 200-day avg; 12-1 mom +33%; RSI 51. Quality z -0.21 (ROE 8%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.08"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 275.33 USD (+7%, 43 analysts); de-biased α -5.9% vs CAPM hurdle 14.1%. Uptrend +59% vs 200-day avg; 12-1 mom +161%; RSI 62. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "Advantest (6857.T) — ⚪ Hold, score -0.10"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 41,560 JPY (+3%, 21 analysts); de-biased α -6.7% vs CAPM hurdle 13.4%. Uptrend +48% vs 200-day avg; 12-1 mom +134%; RSI 71. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 375.06 USD vs 318.83 USD (+18%, 31 analysts); de-biased α -2.8% vs CAPM hurdle 12.6%. Uptrend +14% vs 200-day avg; 12-1 mom +112%; RSI 51. Quality z +0.02 (ROE 65%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 888.00 EUR (+27%, 19 analysts); de-biased α -0.6% vs CAPM hurdle 13.2%. Uptrend +11% vs 200-day avg; 12-1 mom +52%; RSI 54. Quality z -0.10 (ROE 19%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.29"
    Avoid: not owned. Analyst target 81,730 JPY vs 61,250 JPY (+33%, 20 analysts); de-biased α +1.6% vs CAPM hurdle 11.5%. Downtrend -6% vs 200-day avg; 12-1 mom +16%; RSI 58. Quality z +0.06 (ROE 25%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.34"
    Avoid: not owned. Analyst target 324.71 USD vs 283.74 USD (+14%, 31 analysts); de-biased α -2.7% vs CAPM hurdle 10.8%. Uptrend +13% vs 200-day avg; 12-1 mom +46%; RSI 56. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.42"
    Avoid: not owned. Analyst target 194.13 USD vs 175.56 USD (+11%, 30 analysts); de-biased α -4.0% vs CAPM hurdle 11.9%. Uptrend +4% vs 200-day avg; 12-1 mom +12%; RSI 45. Quality z +0.70 (ROE 23%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.46"
    Avoid: not owned. Analyst target 116.37 USD vs 104.70 USD (+11%, 43 analysts); de-biased α -4.8% vs CAPM hurdle 14.0%. Uptrend +26% vs 200-day avg; 12-1 mom +168%; RSI 43. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "TER (TER) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 446.47 USD vs 402.64 USD (+11%, 15 analysts); de-biased α -4.4% vs CAPM hurdle 12.3%. Uptrend +18% vs 200-day avg; 12-1 mom +162%; RSI 53. Quality z -0.31 (ROE 20%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 76.40 USD vs 49.14 USD (+55%, 10 analysts); de-biased α +6.4% vs CAPM hurdle 14.0%. Downtrend -14% vs 200-day avg; 12-1 mom +70%; RSI 43. Quality z -1.00 (ROE 9%).

??? failure "Shin-Etsu (4063.T) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 7,763 JPY vs 6,110 JPY (+27%, 17 analysts); de-biased α +0.4% vs CAPM hurdle 10.8%. Downtrend -2% vs 200-day avg; 12-1 mom +21%; RSI 55. Quality z -0.20 (ROE 10%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.85"
    Avoid: not owned. Analyst target 173.36 USD vs 165.87 USD (+5%, 11 analysts); de-biased α -5.7% vs CAPM hurdle 11.0%. Uptrend +23% vs 200-day avg; 12-1 mom +49%; RSI 65. Quality z -0.02 (ROE 6%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.90"
    Avoid: not owned. Analyst target 95.99 HKD vs 57.65 HKD (+67%, 21 analysts); de-biased α +10.7% vs CAPM hurdle 7.3%. Downtrend -17% vs 200-day avg; 12-1 mom -15%; RSI 34. Quality z -0.99 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.13"
    Avoid: not owned. Analyst target 405.47 USD vs 352.97 USD (+15%, 26 analysts); de-biased α -2.9% vs CAPM hurdle 10.0%. Uptrend +8% vs 200-day avg; 12-1 mom -17%; RSI 66. Quality z +0.31 (ROE 22%).

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.14"
    Avoid: not owned. Analyst target 619.51 USD vs 608.09 USD (+2%, 50 analysts); de-biased α -7.4% vs CAPM hurdle 14.9%. Uptrend +57% vs 200-day avg; 12-1 mom +122%; RSI 57. Quality z -0.15 (ROE 7%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.19"
    Avoid: not owned. Analyst target 288.70 USD vs 266.55 USD (+8%, 40 analysts); de-biased α -6.9% vs CAPM hurdle 19.6%. Uptrend +21% vs 200-day avg; 12-1 mom +55%; RSI 44. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.39"
    Avoid: not owned. Analyst target 569.78 USD vs 509.95 USD (+12%, 26 analysts); de-biased α -3.7% vs CAPM hurdle 10.3%. Uptrend +14% vs 200-day avg; 12-1 mom -18%; RSI 75. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 005930.KS | Samsung Electronics | 485 | 264,000 KRW | $95,551 | 9.4% | Strong Buy |
| MU | Micron Technology | 92 | 1,028.14 USD | $94,588 | 9.3% | Strong Buy |
| 000660.KS | SK hynix | 74 | 1,699,000 KRW | $93,824 | 9.2% | Strong Buy |
| NVDA | NVIDIA | 371 | 229.34 USD | $85,085 | 8.4% | Buy |
| TSM | TSMC | 187 | 453.26 USD | $84,760 | 8.3% | Buy |
| AMAT | Applied Materials | 160 | 506.85 USD | $81,096 | 8.0% | Buy |
| ASX | ASE Technology | 1,509 | 46.43 USD | $70,063 | 6.9% | Buy |
| IFX.DE | Infineon Technologies | 974 | 58.70 EUR | $64,067 | 6.3% | Buy |
| 6857.T | Advantest | 200 | 41,560 JPY | $52,526 | 5.2% | Hold |
| AVGO | Broadcom | 134 | 361.63 USD | $48,458 | 4.8% | Hold |
| 8035.T | Tokyo Electron | 600 | 12,430 JPY | $47,129 | 4.6% | Hold |
| KLAC | KLA Corp | 219 | 195.64 USD | $42,845 | 4.2% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-09-29 15:53 UTC | BUY (new) | TSM | 187 | 457.37 | $85,528 |
| 2026-09-29 15:53 UTC | TRIM | AMAT | -87 | 501.81 | $43,657 |
| 2026-09-29 15:53 UTC | TRIM | AVGO | -112 | 357.74 | $40,067 |
| 2026-09-28 15:29 UTC | BUY (new) | AVGO | 282 | 349.88 | $98,666 |
| 2026-09-28 00:48 UTC | BUY (new) | 005930.KS | 485 | 280,750.00 | $100,255 |
| 2026-09-28 00:48 UTC | BUY (new) | 6857.T | 400 | 34,870.00 | $88,422 |
| 2026-09-28 00:48 UTC | BUY (new) | 000660.KS | 74 | 1,818,500.00 | $99,080 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 16.4%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
