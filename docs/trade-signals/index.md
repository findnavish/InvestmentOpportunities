---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-11 21:59 UTC (Wed Nov 11, 04:59 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Wed 16:59) · Tokyo 🔴 closed (Thu 06:59) · Korea 🔴 closed (Thu 06:59) · Hong Kong 🔴 closed (Thu 05:59) · Xetra 🔴 closed (Wed 22:59) · Euronext Amsterdam 🔴 closed (Wed 22:59)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$873,394** | $326,313 (37%) | $547,081 (63%) | -12.66% | -72.52% | 🔴 Risk-off (-2.8%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $873,394), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **Samsung**<br><small>005930.KS</small> | 129 | 205,500 KRW | $19,804 | Queued · Korea closed | analyst α +0.66 · momentum +0.17 · ⚠️ cycle-peak P/E |
| ADD | **NVDA**<br><small>NVIDIA</small> | 45 | 173.85 USD | $7,823 | Queued · NYSE/Nasdaq closed | analyst α +0.41 · momentum -0.23 · ⚠️ oversold |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.07 | **SK hynix**<br><small>000660.KS</small> | 1,277,000 KRW | +146% | +21.5% | +155% | -16% | 43 | +0.62 | 9.6% → 10.0% | – | analyst α +0.85 · quality +0.33 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.49 | **MU**<br><small>Micron Technology</small> | 811.95 USD | +87% | +6.8% | +277% | +7% | 45 | +0.12 | 10.8% → 9.7% | – | momentum +0.53 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.37 | **Samsung**<br><small>005930.KS</small> | 205,500 KRW | +132% | +18.9% | +121% | -13% | 42 | -0.26 | 9.9% → 7.6% | TRIM 129 | analyst α +0.66 · momentum +0.17 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.10 | **MRVL**<br><small>Marvell Technology</small> | 168.75 USD | +74% | +3.5% | +189% | -9% | 38 | -0.12 | 4.8% → 4.5% | – | momentum +0.35 · analyst α +0.19 · ⚠️ rich valuation |
| 🟢 Buy | +0.71 | **NVDA**<br><small>NVIDIA</small> | 173.85 USD | +88% | +7.2% | +15% | -15% | 29 | +0.47 | 3.6% → 4.5% | ADD 45 | analyst α +0.41 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.59 | **ASX**<br><small>ASE Technology</small> | 37.79 USD | +35% | -2.7% | +213% | +12% | 47 | -0.68 | 3.7% → 3.5% | – | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.55 | **Advantest**<br><small>6857.T</small> | 31,440 JPY | +36% | -5.9% | +129% | +7% | 45 | +0.33 | 2.3% → 2.3% | – | analyst α -0.27 · momentum +0.20 · ⚠️ rich valuation |
| 🟢 Buy | +0.34 | **AMAT**<br><small>Applied Materials</small> | 395.07 USD | +62% | +1.1% | +99% | -11% | 48 | +0.03 | 1.9% → 1.8% | – | momentum +0.12 · analyst α +0.05 |
| 🟢 Buy | +0.29 | **INTC**<br><small>Intel</small> | 62.51 USD | +86% | +6.6% | +167% | -28% | 34 | -0.62 | 1.1% → 1.0% | – | analyst α +0.31 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| ⚪ Hold | +0.14 | **TSM**<br><small>TSMC</small> | 413.30 USD | +34% | -5.6% | +52% | +3% | 50 | +0.58 | 6.0% → 6.0% | – | quality +0.28 · analyst α -0.23 |
| ⚪ Hold | +0.13 | **ASML**<br><small>ASML Holding</small> | 1,534.83 USD | +37% | -5.3% | +66% | -4% | 45 | +0.42 | 0.0% → 0.0% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.13 | **Infineon**<br><small>IFX.DE</small> | 52.33 EUR | +66% | +1.6% | +56% | -9% | 50 | -0.04 | 1.5% → 1.5% | – | analyst α +0.12 · momentum -0.05 |
| ⚪ Hold | -0.05 | **KLAC**<br><small>KLA Corp</small> | 161.00 USD | +45% | -2.9% | +52% | -11% | 50 | +0.51 | 4.9% → 4.9% | – | quality +0.24 · analyst α -0.12 |
| ⚪ Hold | -0.07 | **Tokyo Electron**<br><small>8035.T</small> | 9,321 JPY | +64% | +1.6% | +87% | -10% | 44 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.08 |
| ⚪ Hold | -0.15 | **TER**<br><small>Teradyne</small> | 265.79 USD | +68% | +2.5% | +107% | -24% | 41 | -0.31 | 1.1% → 1.1% | – | quality -0.21 · trend -0.16 |
| ⚪ Hold | -0.18 | **LRCX**<br><small>Lam Research</small> | 235.79 USD | +59% | +0.2% | +82% | -17% | 45 | +0.02 | 1.6% → 1.6% | – | trend -0.12 · momentum +0.03 |
| 🔴 Sell | -0.33 | **GFS**<br><small>GlobalFoundries</small> | 42.85 USD | +77% | +4.8% | +35% | -22% | 48 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · momentum -0.14 |
| 🔴 Sell | -0.37 | **ASMI**<br><small>ASM.AS</small> | 725.20 EUR | +56% | -0.8% | +62% | -11% | 47 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · analyst α -0.05 |
| 🔴 Sell | -0.45 | **Disco**<br><small>6146.T</small> | 47,640 JPY | +72% | +3.7% | +10% | -27% | 44 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.23 |
| 🔴 Sell | -0.48 | **AMD**<br><small>Advanced Micro Devices</small> | 552.96 USD | +12% | -12.2% | +148% | +32% | 54 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.52 | **ENTG**<br><small>Entegris</small> | 154.33 USD | +12% | -11.1% | +88% | +11% | 55 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.18 |
| 🔴 Sell | -0.62 | **AVGO**<br><small>Broadcom</small> | 345.45 USD | +54% | -0.6% | +0% | -6% | 54 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴 Sell | -0.74 | **QCOM**<br><small>Qualcomm</small> | 176.55 USD | +10% | -11.5% | +5% | +5% | 52 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.82 | **ARM**<br><small>Arm Holdings</small> | 203.38 USD | +42% | -5.9% | +65% | -12% | 44 | +0.04 | 0.0% → 0.0% | – | analyst α -0.31 · trend -0.06 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.89 | **AMKR**<br><small>Amkor Technology</small> | 38.10 USD | +101% | +10.3% | +36% | -33% | 45 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.95 | **SNPS**<br><small>Synopsys</small> | 462.12 USD | +23% | -8.2% | +23% | +5% | 51 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.20 |
| 🔴🔴 Strong Sell | -0.99 | **Shin-Etsu**<br><small>4063.T</small> | 5,718 JPY | +36% | -4.8% | +32% | -10% | 46 | -0.20 | 0.0% → 0.0% | – | momentum -0.17 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -1.05 | **TXN**<br><small>Texas Instruments</small> | 309.92 USD | +5% | -12.5% | +82% | +19% | 60 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.11 | **SMIC**<br><small>0981.HK</small> | 49.00 HKD | +96% | +10.7% | -23% | -26% | 47 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.15 | **CDNS**<br><small>Cadence Design Systems</small> | 329.26 USD | +23% | -8.2% | +2% | +0% | 51 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.35 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.07"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,277,000 KRW (+146%, 38 analysts); de-biased α +21.5% vs CAPM hurdle 14.3%. Downtrend -16% vs 200-day avg; 12-1 mom +155%; RSI 43. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.49"
    Within rebalance band of target 9.7%: no trade. Analyst target 1,520.02 USD vs 811.95 USD (+87%, 46 analysts); de-biased α +6.8% vs CAPM hurdle 14.0%. Uptrend +7% vs 200-day avg; 12-1 mom +277%; RSI 45. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.37"
    **TRIM 129 sh** → target 7.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 477,517 KRW vs 205,500 KRW (+132%, 36 analysts); de-biased α +18.9% vs CAPM hurdle 11.3%. Downtrend -13% vs 200-day avg; 12-1 mom +121%; RSI 42. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.10"
    Within rebalance band of target 4.5%: no trade. Analyst target 293.88 USD vs 168.75 USD (+74%, 43 analysts); de-biased α +3.5% vs CAPM hurdle 14.1%. Downtrend -9% vs 200-day avg; 12-1 mom +189%; RSI 38. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.71"
    **ADD 45 sh** → target 4.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 173.85 USD (+88%, 59 analysts); de-biased α +7.2% vs CAPM hurdle 13.9%. Downtrend -15% vs 200-day avg; 12-1 mom +15%; RSI 29. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "ASX (ASX) — 🟢 Buy, score +0.59"
    Within rebalance band of target 3.5%: no trade. Analyst target 51.00 USD vs 37.79 USD (+35%, 1 analysts); de-biased α -2.7% vs CAPM hurdle 11.9%. Uptrend +12% vs 200-day avg; 12-1 mom +213%; RSI 47. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.55"
    Within rebalance band of target 2.3%: no trade. Analyst target 42,686 JPY vs 31,440 JPY (+36%, 21 analysts); de-biased α -5.9% vs CAPM hurdle 13.4%. Uptrend +7% vs 200-day avg; 12-1 mom +129%; RSI 45. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.34"
    Within rebalance band of target 1.8%: no trade. Analyst target 638.94 USD vs 395.07 USD (+62%, 36 analysts); de-biased α +1.1% vs CAPM hurdle 11.6%. Downtrend -11% vs 200-day avg; 12-1 mom +99%; RSI 48. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.29"
    Within rebalance band of target 1.0%: no trade. Analyst target 116.37 USD vs 62.51 USD (+86%, 43 analysts); de-biased α +6.6% vs CAPM hurdle 14.0%. Downtrend -28% vs 200-day avg; 12-1 mom +167%; RSI 34. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? note "TSM (TSM) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 413.30 USD (+34%, 20 analysts); de-biased α -5.6% vs CAPM hurdle 10.8%. Uptrend +3% vs 200-day avg; 12-1 mom +52%; RSI 50. Quality z +0.58 (ROE 35%).

??? note "ASML (ASML) — ⚪ Hold, score +0.13"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,534.83 USD (+37%, 16 analysts); de-biased α -5.3% vs CAPM hurdle 12.3%. Downtrend -4% vs 200-day avg; 12-1 mom +66%; RSI 45. Quality z +0.42 (ROE 50%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.13"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 52.33 EUR (+66%, 23 analysts); de-biased α +1.6% vs CAPM hurdle 14.1%. Downtrend -9% vs 200-day avg; 12-1 mom +56%; RSI 50. Quality z -0.04 (ROE 6%).

??? note "KLAC (KLAC) — ⚪ Hold, score -0.05"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 161.00 USD (+45%, 26 analysts); de-biased α -2.9% vs CAPM hurdle 11.1%. Downtrend -11% vs 200-day avg; 12-1 mom +52%; RSI 50. Quality z +0.51 (ROE 87%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score -0.07"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 9,321 JPY (+64%, 23 analysts); de-biased α +1.6% vs CAPM hurdle 12.8%. Downtrend -10% vs 200-day avg; 12-1 mom +87%; RSI 44. Quality z -0.28 (ROE 29%).

??? note "TER (TER) — ⚪ Hold, score -0.15"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 265.79 USD (+68%, 15 analysts); de-biased α +2.5% vs CAPM hurdle 12.3%. Downtrend -24% vs 200-day avg; 12-1 mom +107%; RSI 41. Quality z -0.31 (ROE 20%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.18"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 235.79 USD (+59%, 31 analysts); de-biased α +0.2% vs CAPM hurdle 12.6%. Downtrend -17% vs 200-day avg; 12-1 mom +82%; RSI 45. Quality z +0.02 (ROE 65%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.33"
    Avoid: not owned. Analyst target 76.00 USD vs 42.85 USD (+77%, 22 analysts); de-biased α +4.8% vs CAPM hurdle 12.4%. Downtrend -22% vs 200-day avg; 12-1 mom +35%; RSI 48. Quality z -0.21 (ROE 8%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 725.20 EUR (+56%, 19 analysts); de-biased α -0.8% vs CAPM hurdle 13.2%. Downtrend -11% vs 200-day avg; 12-1 mom +62%; RSI 47. Quality z -0.10 (ROE 19%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.45"
    Avoid: not owned. Analyst target 81,730 JPY vs 47,640 JPY (+72%, 20 analysts); de-biased α +3.7% vs CAPM hurdle 11.5%. Downtrend -27% vs 200-day avg; 12-1 mom +10%; RSI 44. Quality z +0.06 (ROE 25%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.48"
    Avoid: not owned. Analyst target 619.51 USD vs 552.96 USD (+12%, 50 analysts); de-biased α -12.2% vs CAPM hurdle 14.9%. Uptrend +32% vs 200-day avg; 12-1 mom +148%; RSI 54. Quality z -0.15 (ROE 7%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.52"
    Avoid: not owned. Analyst target 173.36 USD vs 154.33 USD (+12%, 11 analysts); de-biased α -11.1% vs CAPM hurdle 11.0%. Uptrend +11% vs 200-day avg; 12-1 mom +88%; RSI 55. Quality z -0.02 (ROE 6%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.62"
    Avoid: not owned. Analyst target 531.31 USD vs 345.45 USD (+54%, 47 analysts); de-biased α -0.6% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom +0%; RSI 54. Quality z +0.26 (ROE 31%).

??? failure "QCOM (QCOM) — 🔴 Sell, score -0.74"
    Avoid: not owned. Analyst target 194.13 USD vs 176.55 USD (+10%, 30 analysts); de-biased α -11.5% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +5%; RSI 52. Quality z +0.70 (ROE 23%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 288.70 USD vs 203.38 USD (+42%, 40 analysts); de-biased α -5.9% vs CAPM hurdle 19.6%. Downtrend -12% vs 200-day avg; 12-1 mom +65%; RSI 44. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AMKR (AMKR) — 🔴🔴 Strong Sell, score -0.89"
    Avoid: not owned. Analyst target 76.40 USD vs 38.10 USD (+101%, 10 analysts); de-biased α +10.3% vs CAPM hurdle 14.0%. Downtrend -33% vs 200-day avg; 12-1 mom +36%; RSI 45. Quality z -1.00 (ROE 9%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.95"
    Avoid: not owned. Analyst target 569.78 USD vs 462.12 USD (+23%, 26 analysts); de-biased α -8.2% vs CAPM hurdle 10.3%. Uptrend +5% vs 200-day avg; 12-1 mom +23%; RSI 51. Quality z +0.14 (ROE 7%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,718 JPY (+36%, 17 analysts); de-biased α -4.8% vs CAPM hurdle 10.8%. Downtrend -10% vs 200-day avg; 12-1 mom +32%; RSI 46. Quality z -0.20 (ROE 10%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.05"
    Avoid: not owned. Analyst target 324.71 USD vs 309.92 USD (+5%, 31 analysts); de-biased α -12.5% vs CAPM hurdle 10.8%. Uptrend +19% vs 200-day avg; 12-1 mom +82%; RSI 60. Quality z +0.24 (ROE 30%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.11"
    Avoid: not owned. Analyst target 95.99 HKD vs 49.00 HKD (+96%, 21 analysts); de-biased α +10.7% vs CAPM hurdle 7.3%. Downtrend -26% vs 200-day avg; 12-1 mom -23%; RSI 47. Quality z -0.99 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.15"
    Avoid: not owned. Analyst target 405.47 USD vs 329.26 USD (+23%, 26 analysts); de-biased α -8.2% vs CAPM hurdle 10.0%. Uptrend +0% vs 200-day avg; 12-1 mom +2%; RSI 51. Quality z +0.31 (ROE 22%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 811.95 USD | $94,186 | 10.8% | Strong Buy |
| 005930.KS | Samsung Electronics | 562 | 205,500 KRW | $86,276 | 9.9% | Strong Buy |
| 000660.KS | SK hynix | 88 | 1,277,000 KRW | $83,949 | 9.6% | Strong Buy |
| TSM | TSMC | 127 | 413.30 USD | $52,490 | 6.0% | Hold |
| KLAC | KLA Corp | 268 | 161.00 USD | $43,148 | 4.9% | Hold |
| MRVL | Marvell Technology | 248 | 168.75 USD | $41,850 | 4.8% | Strong Buy |
| ASX | ASE Technology | 864 | 37.79 USD | $32,651 | 3.7% | Buy |
| NVDA | NVIDIA | 179 | 173.85 USD | $31,119 | 3.6% | Buy |
| 6857.T | Advantest | 100 | 31,440 JPY | $19,673 | 2.3% | Buy |
| AMAT | Applied Materials | 41 | 395.07 USD | $16,198 | 1.9% | Buy |
| LRCX | Lam Research | 58 | 235.79 USD | $13,676 | 1.6% | Hold |
| IFX.DE | Infineon Technologies | 225 | 52.33 EUR | $13,061 | 1.5% | Hold |
| INTC | Intel | 152 | 62.51 USD | $9,502 | 1.1% | Buy |
| TER | Teradyne | 35 | 265.79 USD | $9,303 | 1.1% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-11 15:13 UTC | TRIM | AMAT | -32 | 387.02 | $12,385 |
| 2026-11-11 15:13 UTC | TRIM | MRVL | -76 | 165.15 | $12,551 |
| 2026-11-11 15:13 UTC | TRIM | INTC | -83 | 61.66 | $5,118 |
| 2026-11-11 06:23 UTC | ADD | 000660.KS | 38 | 1,277,000.00 | $36,371 |
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 45.9%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
