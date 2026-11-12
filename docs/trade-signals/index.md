---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-12 11:12 UTC (Thu Nov 12, 06:12 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Thu 06:12) · Tokyo 🔴 closed (Thu 20:12) · Korea 🔴 closed (Thu 20:12) · Hong Kong 🔴 closed (Thu 19:12) · Xetra 🟢 open (Thu 12:12) · Euronext Amsterdam 🟢 open (Thu 12:12)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$872,720** | $326,313 (37%) | $546,407 (63%) | -12.73% | -72.52% | 🔴 Risk-off (-2.8%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $872,720), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **SK hynix**<br><small>000660.KS</small> | 49 | 1,255,000 KRW | $46,181 | Queued · Korea closed | quality +0.33 · momentum +0.26 · ⚠️ cycle-peak P/E, high σ(e) |
| ADD | **NVDA**<br><small>NVIDIA</small> | 108 | 173.85 USD | $18,776 | Queued · NYSE/Nasdaq closed | analyst α +0.48 · momentum -0.23 · ⚠️ oversold |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.00 | **MU**<br><small>Micron Technology</small> | 811.95 USD | +87% | +7.5% | +280% | +6% | 45 | +0.12 | 10.8% → 10.0% | – | momentum +0.53 · analyst α +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.08 | **Samsung**<br><small>005930.KS</small> | 208,000 KRW | +130% | +18.9% | +121% | -12% | 43 | -0.26 | 10.1% → 10.0% | – | analyst α +0.85 · momentum +0.17 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.33 | **MRVL**<br><small>Marvell Technology</small> | 168.75 USD | +74% | +4.2% | +175% | -10% | 38 | -0.12 | 4.8% → 5.1% | – | momentum +0.35 · analyst α +0.23 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.17 | **SK hynix**<br><small>000660.KS</small> | 1,255,000 KRW | – | +0.0% | +155% | -17% | 42 | +0.62 | 9.5% → 4.2% | TRIM 49 | quality +0.33 · momentum +0.26 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.96 | **NVDA**<br><small>NVIDIA</small> | 173.85 USD | +88% | +7.9% | +15% | -15% | 29 | +0.47 | 3.6% → 5.7% | ADD 108 | analyst α +0.48 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.73 | **Advantest**<br><small>6857.T</small> | 29,825 JPY | +43% | -3.3% | +124% | +2% | 41 | +0.33 | 2.1% → 2.9% | – | momentum +0.20 · quality +0.16 · ⚠️ rich valuation |
| 🟢 Buy | +0.58 | **ASX**<br><small>ASE Technology</small> | 37.79 USD | +35% | -2.4% | +199% | +11% | 47 | -0.68 | 3.7% → 3.2% | – | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.45 | **INTC**<br><small>Intel</small> | 62.51 USD | +86% | +7.2% | +159% | -28% | 34 | -0.62 | 1.1% → 1.5% | – | analyst α +0.36 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.43 | **AMAT**<br><small>Applied Materials</small> | 395.07 USD | +62% | +1.8% | +96% | -11% | 48 | +0.03 | 1.9% → 2.2% | – | momentum +0.12 · analyst α +0.08 |
| ⚪ Hold | +0.13 | **KLAC**<br><small>KLA Corp</small> | 161.00 USD | +45% | -2.2% | +51% | -11% | 50 | +0.51 | 4.9% → 4.9% | – | quality +0.24 · analyst α -0.08 |
| ⚪ Hold | +0.10 | **Infineon**<br><small>IFX.DE</small> | 51.59 EUR | +68% | +2.9% | +55% | -10% | 48 | -0.04 | 1.5% → 1.5% | – | analyst α +0.15 · momentum -0.05 |
| ⚪ Hold | +0.10 | **ASML**<br><small>ASML Holding</small> | 1,534.83 USD | +37% | -4.6% | +62% | -4% | 45 | +0.42 | 0.0% → 0.0% | – | analyst α -0.19 · quality +0.18 |
| ⚪ Hold | +0.07 | **Tokyo Electron**<br><small>8035.T</small> | 9,316 JPY | +64% | +2.3% | +87% | -10% | 44 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.12 |
| ⚪ Hold | +0.03 | **TSM**<br><small>TSMC</small> | 413.30 USD | +34% | -4.9% | +49% | +3% | 50 | +0.58 | 6.0% → 6.0% | – | quality +0.28 · analyst α -0.27 |
| ⚪ Hold | -0.02 | **LRCX**<br><small>Lam Research</small> | 235.79 USD | +59% | +0.9% | +81% | -17% | 45 | +0.02 | 1.6% → 1.6% | – | trend -0.10 · momentum +0.05 |
| ⚪ Hold | -0.07 | **TER**<br><small>Teradyne</small> | 265.79 USD | +68% | +3.2% | +103% | -24% | 41 | -0.31 | 1.1% → 1.1% | – | quality -0.21 · analyst α +0.19 |
| ⚪ Hold | -0.24 | **ASMI**<br><small>ASM.AS</small> | 730.40 EUR | +55% | -0.4% | +65% | -10% | 48 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · analyst α -0.05 |
| 🔴 Sell | -0.26 | **GFS**<br><small>GlobalFoundries</small> | 42.85 USD | +77% | +5.5% | +35% | -22% | 48 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · momentum -0.14 |
| 🔴 Sell | -0.40 | **Disco**<br><small>6146.T</small> | 47,480 JPY | +72% | +4.6% | +10% | -27% | 44 | +0.06 | 0.0% → 0.0% | – | analyst α +0.27 · momentum -0.26 |
| 🔴 Sell | -0.54 | **AMD**<br><small>Advanced Micro Devices</small> | 552.96 USD | +12% | -11.5% | +140% | +31% | 54 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.61 | **AVGO**<br><small>Broadcom</small> | 345.45 USD | +54% | +0.0% | -1% | -6% | 54 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴 Sell | -0.64 | **ENTG**<br><small>Entegris</small> | 154.33 USD | +12% | -10.4% | +83% | +11% | 55 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.18 |
| 🔴🔴 Strong Sell | -0.80 | **AMKR**<br><small>Amkor Technology</small> | 38.10 USD | +101% | +11.0% | +36% | -33% | 45 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.92 | **QCOM**<br><small>Qualcomm</small> | 176.55 USD | +10% | -10.8% | +1% | +4% | 52 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -0.99 | **SMIC**<br><small>0981.HK</small> | 48.74 HKD | +97% | +11.6% | -23% | -27% | 46 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.01 | **ARM**<br><small>Arm Holdings</small> | 203.38 USD | +42% | -5.2% | +59% | -12% | 44 | +0.04 | 0.0% → 0.0% | – | analyst α -0.31 · trend -0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.03 | **SNPS**<br><small>Synopsys</small> | 462.12 USD | +23% | -7.5% | +23% | +5% | 51 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.20 |
| 🔴🔴 Strong Sell | -1.17 | **CDNS**<br><small>Cadence Design Systems</small> | 329.26 USD | +23% | -7.5% | +2% | +0% | 51 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.23 | **TXN**<br><small>Texas Instruments</small> | 309.92 USD | +5% | -11.8% | +79% | +18% | 60 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.24 | **Shin-Etsu**<br><small>4063.T</small> | 5,819 JPY | +33% | -4.7% | +32% | -8% | 50 | -0.20 | 0.0% → 0.0% | – | analyst α -0.23 · momentum -0.17 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.00"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 811.95 USD (+87%, 46 analysts); de-biased α +7.5% vs CAPM hurdle 14.0%. Uptrend +6% vs 200-day avg; 12-1 mom +280%; RSI 45. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.08"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 208,000 KRW (+130%, 36 analysts); de-biased α +18.9% vs CAPM hurdle 11.3%. Downtrend -12% vs 200-day avg; 12-1 mom +121%; RSI 43. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.33"
    Within rebalance band of target 5.1%: no trade. Analyst target 293.88 USD vs 168.75 USD (+74%, 43 analysts); de-biased α +4.2% vs CAPM hurdle 14.1%. Downtrend -10% vs 200-day avg; 12-1 mom +175%; RSI 38. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.17"
    **TRIM 49 sh** → target 4.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -17% vs 200-day avg; 12-1 mom +155%; RSI 42. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +0.96"
    **ADD 108 sh** → target 5.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 173.85 USD (+88%, 59 analysts); de-biased α +7.9% vs CAPM hurdle 13.9%. Downtrend -15% vs 200-day avg; 12-1 mom +15%; RSI 29. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "Advantest (6857.T) — 🟢 Buy, score +0.73"
    Within rebalance band of target 2.9%: no trade. Analyst target 42,686 JPY vs 29,825 JPY (+43%, 21 analysts); de-biased α -3.3% vs CAPM hurdle 13.4%. Uptrend +2% vs 200-day avg; 12-1 mom +124%; RSI 41. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "ASX (ASX) — 🟢 Buy, score +0.58"
    Within rebalance band of target 3.2%: no trade. Analyst target 51.00 USD vs 37.79 USD (+35%, 1 analysts); de-biased α -2.4% vs CAPM hurdle 11.9%. Uptrend +11% vs 200-day avg; 12-1 mom +199%; RSI 47. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "INTC (INTC) — 🟢 Buy, score +0.45"
    Within rebalance band of target 1.5%: no trade. Analyst target 116.37 USD vs 62.51 USD (+86%, 43 analysts); de-biased α +7.2% vs CAPM hurdle 14.0%. Downtrend -28% vs 200-day avg; 12-1 mom +159%; RSI 34. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.43"
    Within rebalance band of target 2.2%: no trade. Analyst target 638.94 USD vs 395.07 USD (+62%, 36 analysts); de-biased α +1.8% vs CAPM hurdle 11.6%. Downtrend -11% vs 200-day avg; 12-1 mom +96%; RSI 48. Quality z +0.03 (ROE 36%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.13"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 161.00 USD (+45%, 26 analysts); de-biased α -2.2% vs CAPM hurdle 11.1%. Downtrend -11% vs 200-day avg; 12-1 mom +51%; RSI 50. Quality z +0.51 (ROE 87%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.10"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 51.59 EUR (+68%, 23 analysts); de-biased α +2.9% vs CAPM hurdle 14.1%. Downtrend -10% vs 200-day avg; 12-1 mom +55%; RSI 48. Quality z -0.04 (ROE 6%).

??? note "ASML (ASML) — ⚪ Hold, score +0.10"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,534.83 USD (+37%, 16 analysts); de-biased α -4.6% vs CAPM hurdle 12.3%. Downtrend -4% vs 200-day avg; 12-1 mom +62%; RSI 45. Quality z +0.42 (ROE 50%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.07"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 9,316 JPY (+64%, 23 analysts); de-biased α +2.3% vs CAPM hurdle 12.8%. Downtrend -10% vs 200-day avg; 12-1 mom +87%; RSI 44. Quality z -0.28 (ROE 29%).

??? note "TSM (TSM) — ⚪ Hold, score +0.03"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 413.30 USD (+34%, 20 analysts); de-biased α -4.9% vs CAPM hurdle 10.8%. Uptrend +3% vs 200-day avg; 12-1 mom +49%; RSI 50. Quality z +0.58 (ROE 35%).

??? note "LRCX (LRCX) — ⚪ Hold, score -0.02"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 235.79 USD (+59%, 31 analysts); de-biased α +0.9% vs CAPM hurdle 12.6%. Downtrend -17% vs 200-day avg; 12-1 mom +81%; RSI 45. Quality z +0.02 (ROE 65%).

??? note "TER (TER) — ⚪ Hold, score -0.07"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 265.79 USD (+68%, 15 analysts); de-biased α +3.2% vs CAPM hurdle 12.3%. Downtrend -24% vs 200-day avg; 12-1 mom +103%; RSI 41. Quality z -0.31 (ROE 20%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 730.40 EUR (+55%, 19 analysts); de-biased α -0.4% vs CAPM hurdle 13.2%. Downtrend -10% vs 200-day avg; 12-1 mom +65%; RSI 48. Quality z -0.10 (ROE 19%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.26"
    Avoid: not owned. Analyst target 76.00 USD vs 42.85 USD (+77%, 22 analysts); de-biased α +5.5% vs CAPM hurdle 12.4%. Downtrend -22% vs 200-day avg; 12-1 mom +35%; RSI 48. Quality z -0.21 (ROE 8%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.40"
    Avoid: not owned. Analyst target 81,730 JPY vs 47,480 JPY (+72%, 20 analysts); de-biased α +4.6% vs CAPM hurdle 11.5%. Downtrend -27% vs 200-day avg; 12-1 mom +10%; RSI 44. Quality z +0.06 (ROE 25%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.54"
    Avoid: not owned. Analyst target 619.51 USD vs 552.96 USD (+12%, 50 analysts); de-biased α -11.5% vs CAPM hurdle 14.9%. Uptrend +31% vs 200-day avg; 12-1 mom +140%; RSI 54. Quality z -0.15 (ROE 7%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.61"
    Avoid: not owned. Analyst target 531.31 USD vs 345.45 USD (+54%, 47 analysts); de-biased α +0.0% vs CAPM hurdle 11.2%. Downtrend -6% vs 200-day avg; 12-1 mom -1%; RSI 54. Quality z +0.26 (ROE 31%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.64"
    Avoid: not owned. Analyst target 173.36 USD vs 154.33 USD (+12%, 11 analysts); de-biased α -10.4% vs CAPM hurdle 11.0%. Uptrend +11% vs 200-day avg; 12-1 mom +83%; RSI 55. Quality z -0.02 (ROE 6%).

??? failure "AMKR (AMKR) — 🔴🔴 Strong Sell, score -0.80"
    Avoid: not owned. Analyst target 76.40 USD vs 38.10 USD (+101%, 10 analysts); de-biased α +11.0% vs CAPM hurdle 14.0%. Downtrend -33% vs 200-day avg; 12-1 mom +36%; RSI 45. Quality z -1.00 (ROE 9%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.92"
    Avoid: not owned. Analyst target 194.13 USD vs 176.55 USD (+10%, 30 analysts); de-biased α -10.8% vs CAPM hurdle 11.9%. Uptrend +4% vs 200-day avg; 12-1 mom +1%; RSI 52. Quality z +0.70 (ROE 23%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 95.99 HKD vs 48.74 HKD (+97%, 21 analysts); de-biased α +11.6% vs CAPM hurdle 7.3%. Downtrend -27% vs 200-day avg; 12-1 mom -23%; RSI 46. Quality z -0.99 (ROE 3%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 288.70 USD vs 203.38 USD (+42%, 40 analysts); de-biased α -5.2% vs CAPM hurdle 19.6%. Downtrend -12% vs 200-day avg; 12-1 mom +59%; RSI 44. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.03"
    Avoid: not owned. Analyst target 569.78 USD vs 462.12 USD (+23%, 26 analysts); de-biased α -7.5% vs CAPM hurdle 10.3%. Uptrend +5% vs 200-day avg; 12-1 mom +23%; RSI 51. Quality z +0.14 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.17"
    Avoid: not owned. Analyst target 405.47 USD vs 329.26 USD (+23%, 26 analysts); de-biased α -7.5% vs CAPM hurdle 10.0%. Uptrend +0% vs 200-day avg; 12-1 mom +2%; RSI 51. Quality z +0.31 (ROE 22%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.23"
    Avoid: not owned. Analyst target 324.71 USD vs 309.92 USD (+5%, 31 analysts); de-biased α -11.8% vs CAPM hurdle 10.8%. Uptrend +18% vs 200-day avg; 12-1 mom +79%; RSI 60. Quality z +0.24 (ROE 30%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.24"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,819 JPY (+33%, 17 analysts); de-biased α -4.7% vs CAPM hurdle 10.8%. Downtrend -8% vs 200-day avg; 12-1 mom +32%; RSI 50. Quality z -0.20 (ROE 10%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 811.95 USD | $94,186 | 10.8% | Strong Buy |
| 005930.KS | Samsung Electronics | 562 | 208,000 KRW | $87,785 | 10.1% | Strong Buy |
| 000660.KS | SK hynix | 88 | 1,255,000 KRW | $82,937 | 9.5% | Strong Buy |
| TSM | TSMC | 127 | 413.30 USD | $52,490 | 6.0% | Hold |
| KLAC | KLA Corp | 268 | 161.00 USD | $43,148 | 4.9% | Hold |
| MRVL | Marvell Technology | 248 | 168.75 USD | $41,850 | 4.8% | Strong Buy |
| ASX | ASE Technology | 864 | 37.79 USD | $32,651 | 3.7% | Buy |
| NVDA | NVIDIA | 179 | 173.85 USD | $31,119 | 3.6% | Strong Buy |
| 6857.T | Advantest | 100 | 29,825 JPY | $18,681 | 2.1% | Buy |
| AMAT | Applied Materials | 41 | 395.07 USD | $16,198 | 1.9% | Buy |
| LRCX | Lam Research | 58 | 235.79 USD | $13,676 | 1.6% | Hold |
| IFX.DE | Infineon Technologies | 225 | 51.59 EUR | $12,882 | 1.5% | Hold |
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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 43.2%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
