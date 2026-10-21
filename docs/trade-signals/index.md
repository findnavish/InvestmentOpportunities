---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-21 10:10 UTC (Wed Oct 21, 06:10 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Wed 06:10) · Tokyo 🔴 closed (Wed 19:10) · Korea 🔴 closed (Wed 19:10) · Hong Kong 🔴 closed (Wed 18:10) · Xetra 🟢 open (Wed 12:10) · Euronext Amsterdam 🟢 open (Wed 12:10)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$905,999** | $129,183 (14%) | $776,816 (86%) | -9.40% | -11.54% | 🟢 Risk-on (+6.6%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $905,999), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **ASX**<br><small>ASE Technology</small> | 361 | 40.78 USD | $14,723 | Queued · NYSE/Nasdaq closed | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| TRIM | **KLAC**<br><small>KLA Corp</small> | 82 | 161.93 USD | $13,278 | Queued · NYSE/Nasdaq closed | quality +0.24 · trend -0.14 · ⚠️ oversold |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.12 | **SK hynix**<br><small>000660.KS</small> | 1,287,000 KRW | +144% | +23.7% | +346% | -12% | 31 | +0.62 | 10.5% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.57 | **MU**<br><small>Micron Technology</small> | 895.85 USD | +70% | +5.2% | +431% | +23% | 37 | +0.12 | 9.1% → 10.0% | – | momentum +0.53 · analyst α +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.45 | **Samsung**<br><small>005930.KS</small> | 221,000 KRW | +116% | +17.6% | +185% | -5% | 37 | -0.26 | 8.9% → 10.0% | – | analyst α +0.66 · momentum +0.20 · ⚠️ cycle-peak P/E |
| 🟢 Buy | +0.65 | **Infineon**<br><small>IFX.DE</small> | 53.32 EUR | +63% | +3.6% | +77% | -6% | 40 | -0.04 | 8.6% → 9.3% | – | analyst α +0.31 · momentum +0.07 |
| 🟢 Buy | +0.61 | **NVDA**<br><small>NVIDIA</small> | 216.48 USD | +51% | +0.7% | +26% | +7% | 41 | +0.47 | 7.0% → 8.7% | – | quality +0.21 · momentum -0.17 |
| 🟢 Buy | +0.56 | **ASX**<br><small>ASE Technology</small> | 40.78 USD | +25% | -2.6% | +251% | +26% | 43 | -0.68 | 6.0% → 7.6% | ADD 361 | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.56 | **AMAT**<br><small>Applied Materials</small> | 404.95 USD | +58% | +2.9% | +108% | -8% | 29 | +0.03 | 7.0% → 6.8% | – | analyst α +0.23 · momentum +0.12 · ⚠️ oversold |
| 🟢 Buy | +0.34 | **TSM**<br><small>TSMC</small> | 425.30 USD | +30% | -3.8% | +53% | +8% | 42 | +0.58 | 5.5% → 5.9% | – | quality +0.28 · momentum -0.12 |
| 🟢 Buy | +0.26 | **KLAC**<br><small>KLA Corp</small> | 161.93 USD | +44% | -0.3% | +64% | -11% | 30 | +0.51 | 5.0% → 3.5% | TRIM 82 | quality +0.24 · trend -0.14 · ⚠️ oversold |
| ⚪ Hold | +0.14 | **LRCX**<br><small>Lam Research</small> | 263.45 USD | +42% | -1.2% | +117% | -7% | 33 | +0.02 | 3.1% → 3.1% | – | momentum +0.14 · trend -0.09 |
| ⚪ Hold | +0.05 | **MRVL**<br><small>Marvell Technology</small> | 240.42 USD | +22% | -6.7% | +193% | +36% | 45 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.32 · ⚠️ rich valuation |
| ⚪ Hold | +0.02 | **AVGO**<br><small>Broadcom</small> | 334.51 USD | +59% | +3.4% | +5% | -9% | 39 | +0.26 | 3.7% → 3.7% | – | analyst α +0.27 · momentum -0.26 |
| ⚪ Hold | +0.01 | **Advantest**<br><small>6857.T</small> | 34,390 JPY | +24% | -6.0% | +72% | +21% | 45 | +0.33 | 2.4% → 2.4% | – | analyst α -0.36 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.00 | **Tokyo Electron**<br><small>8035.T</small> | 10,250 JPY | +49% | +0.6% | +71% | +3% | 41 | -0.28 | 3.6% → 3.6% | – | quality -0.18 · analyst α +0.12 |
| ⚪ Hold | -0.03 | **ASML**<br><small>ASML Holding</small> | 1,630.84 USD | +29% | -4.5% | +67% | +3% | 37 | +0.42 | 5.4% → 5.4% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | -0.18 | **TER**<br><small>Teradyne</small> | 336.17 USD | +33% | -3.5% | +187% | -3% | 37 | -0.31 | 0.0% → 0.0% | – | momentum +0.23 · quality -0.21 |
| ⚪ Hold | -0.21 | **GFS**<br><small>GlobalFoundries</small> | 47.03 USD | +62% | +3.7% | +35% | -14% | 47 | -0.21 | 0.0% → 0.0% | – | analyst α +0.36 · trend -0.18 |
| ⚪ Hold | -0.24 | **INTC**<br><small>Intel</small> | 91.61 USD | +27% | -5.5% | +225% | +7% | 34 | -0.62 | 0.0% → 0.0% | – | momentum +0.30 · analyst α -0.27 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.26 | **ASMI**<br><small>ASM.AS</small> | 756.40 EUR | +49% | +0.4% | +55% | -7% | 36 | -0.10 | 0.0% → 0.0% | – | analyst α +0.08 · momentum -0.07 |
| 🔴 Sell | -0.40 | **ARM**<br><small>Arm Holdings</small> | 220.92 USD | +31% | -5.9% | +94% | -2% | 33 | +0.04 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.56 | **AMKR**<br><small>Amkor Technology</small> | 41.69 USD | +83% | +8.7% | +70% | -28% | 30 | -1.00 | 0.0% → 0.0% | – | analyst α +0.48 · quality -0.43 · ⚠️ oversold |
| 🔴 Sell | -0.59 | **Disco**<br><small>6146.T</small> | 53,910 JPY | +52% | +1.5% | -5% | -18% | 42 | +0.06 | 0.0% → 0.0% | – | momentum -0.30 · trend -0.21 |
| 🔴 Sell | -0.73 | **AMD**<br><small>Advanced Micro Devices</small> | 534.60 USD | +16% | -8.5% | +159% | +34% | 40 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.25 |
| 🔴🔴 Strong Sell | -0.89 | **CDNS**<br><small>Cadence Design Systems</small> | 319.93 USD | +27% | -4.5% | -8% | -2% | 45 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -0.91 | **TXN**<br><small>Texas Instruments</small> | 277.92 USD | +17% | -6.7% | +55% | +9% | 49 | +0.24 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.14 |
| 🔴🔴 Strong Sell | -0.91 | **ENTG**<br><small>Entegris</small> | 142.76 USD | +21% | -6.0% | +64% | +5% | 42 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.07 |
| 🔴🔴 Strong Sell | -0.97 | **Shin-Etsu**<br><small>4063.T</small> | 5,897 JPY | +32% | -3.1% | +13% | -6% | 45 | -0.20 | 0.0% → 0.0% | – | momentum -0.23 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.02 | **SNPS**<br><small>Synopsys</small> | 447.60 USD | +27% | -4.5% | -10% | +0% | 47 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -1.20 | **SMIC**<br><small>0981.HK</small> | 49.96 HKD | +92% | +12.5% | -16% | -27% | 22 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.22 | **QCOM**<br><small>Qualcomm</small> | 175.60 USD | +11% | -8.6% | +21% | +4% | 47 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.12"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,287,000 KRW (+144%, 38 analysts); de-biased α +23.7% vs CAPM hurdle 14.3%. Downtrend -12% vs 200-day avg; 12-1 mom +346%; RSI 31. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.57"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 895.85 USD (+70%, 46 analysts); de-biased α +5.2% vs CAPM hurdle 14.0%. Uptrend +23% vs 200-day avg; 12-1 mom +431%; RSI 37. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.45"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 221,000 KRW (+116%, 36 analysts); de-biased α +17.6% vs CAPM hurdle 11.3%. Downtrend -5% vs 200-day avg; 12-1 mom +185%; RSI 37. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.65"
    Within rebalance band of target 9.3%: no trade. Analyst target 86.74 EUR vs 53.32 EUR (+63%, 23 analysts); de-biased α +3.6% vs CAPM hurdle 14.1%. Downtrend -6% vs 200-day avg; 12-1 mom +77%; RSI 40. Quality z -0.04 (ROE 6%).

??? success "NVDA (NVDA) — 🟢 Buy, score +0.61"
    Within rebalance band of target 8.7%: no trade. Analyst target 327.70 USD vs 216.48 USD (+51%, 59 analysts); de-biased α +0.7% vs CAPM hurdle 13.9%. Uptrend +7% vs 200-day avg; 12-1 mom +26%; RSI 41. Quality z +0.47 (ROE 101%).

??? success "ASX (ASX) — 🟢 Buy, score +0.56"
    **ADD 361 sh** → target 7.6% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 40.78 USD (+25%, 1 analysts); de-biased α -2.6% vs CAPM hurdle 11.9%. Uptrend +26% vs 200-day avg; 12-1 mom +251%; RSI 43. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.56"
    Within rebalance band of target 6.8%: no trade. Analyst target 638.94 USD vs 404.95 USD (+58%, 36 analysts); de-biased α +2.9% vs CAPM hurdle 11.6%. Downtrend -8% vs 200-day avg; 12-1 mom +108%; RSI 29. Quality z +0.03 (ROE 36%). ⚠️ oversold.

??? success "TSM (TSM) — 🟢 Buy, score +0.34"
    Within rebalance band of target 5.9%: no trade. Analyst target 552.26 USD vs 425.30 USD (+30%, 20 analysts); de-biased α -3.8% vs CAPM hurdle 10.8%. Uptrend +8% vs 200-day avg; 12-1 mom +53%; RSI 42. Quality z +0.58 (ROE 35%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.26"
    **TRIM 82 sh** → target 3.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 233.77 USD vs 161.93 USD (+44%, 26 analysts); de-biased α -0.3% vs CAPM hurdle 11.1%. Downtrend -11% vs 200-day avg; 12-1 mom +64%; RSI 30. Quality z +0.51 (ROE 87%). ⚠️ oversold.

??? note "LRCX (LRCX) — ⚪ Hold, score +0.14"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 263.45 USD (+42%, 31 analysts); de-biased α -1.2% vs CAPM hurdle 12.6%. Downtrend -7% vs 200-day avg; 12-1 mom +117%; RSI 33. Quality z +0.02 (ROE 65%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.05"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 240.42 USD (+22%, 43 analysts); de-biased α -6.7% vs CAPM hurdle 14.1%. Uptrend +36% vs 200-day avg; 12-1 mom +193%; RSI 45. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.02"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 334.51 USD (+59%, 47 analysts); de-biased α +3.4% vs CAPM hurdle 11.2%. Downtrend -9% vs 200-day avg; 12-1 mom +5%; RSI 39. Quality z +0.26 (ROE 31%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.01"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 34,390 JPY (+24%, 21 analysts); de-biased α -6.0% vs CAPM hurdle 13.4%. Uptrend +21% vs 200-day avg; 12-1 mom +72%; RSI 45. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.00"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 10,250 JPY (+49%, 23 analysts); de-biased α +0.6% vs CAPM hurdle 12.8%. Uptrend +3% vs 200-day avg; 12-1 mom +71%; RSI 41. Quality z -0.28 (ROE 29%).

??? note "ASML (ASML) — ⚪ Hold, score -0.03"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,630.84 USD (+29%, 16 analysts); de-biased α -4.5% vs CAPM hurdle 12.3%. Uptrend +3% vs 200-day avg; 12-1 mom +67%; RSI 37. Quality z +0.42 (ROE 50%).

??? note "TER (TER) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 336.17 USD (+33%, 15 analysts); de-biased α -3.5% vs CAPM hurdle 12.3%. Downtrend -3% vs 200-day avg; 12-1 mom +187%; RSI 37. Quality z -0.31 (ROE 20%).

??? note "GFS (GFS) — ⚪ Hold, score -0.21"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 47.03 USD (+62%, 22 analysts); de-biased α +3.7% vs CAPM hurdle 12.4%. Downtrend -14% vs 200-day avg; 12-1 mom +35%; RSI 47. Quality z -0.21 (ROE 8%).

??? note "INTC (INTC) — ⚪ Hold, score -0.24"
    Hold zone: not owned, no entry. Analyst target 116.37 USD vs 91.61 USD (+27%, 43 analysts); de-biased α -5.5% vs CAPM hurdle 14.0%. Uptrend +7% vs 200-day avg; 12-1 mom +225%; RSI 34. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.26"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 756.40 EUR (+49%, 19 analysts); de-biased α +0.4% vs CAPM hurdle 13.2%. Downtrend -7% vs 200-day avg; 12-1 mom +55%; RSI 36. Quality z -0.10 (ROE 19%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.40"
    Avoid: not owned. Analyst target 288.70 USD vs 220.92 USD (+31%, 40 analysts); de-biased α -5.9% vs CAPM hurdle 19.6%. Downtrend -2% vs 200-day avg; 12-1 mom +94%; RSI 33. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.56"
    Avoid: not owned. Analyst target 76.40 USD vs 41.69 USD (+83%, 10 analysts); de-biased α +8.7% vs CAPM hurdle 14.0%. Downtrend -28% vs 200-day avg; 12-1 mom +70%; RSI 30. Quality z -1.00 (ROE 9%). ⚠️ oversold.

??? failure "Disco (6146.T) — 🔴 Sell, score -0.59"
    Avoid: not owned. Analyst target 81,730 JPY vs 53,910 JPY (+52%, 20 analysts); de-biased α +1.5% vs CAPM hurdle 11.5%. Downtrend -18% vs 200-day avg; 12-1 mom -5%; RSI 42. Quality z +0.06 (ROE 25%).

??? failure "AMD (AMD) — 🔴 Sell, score -0.73"
    Avoid: not owned. Analyst target 619.51 USD vs 534.60 USD (+16%, 50 analysts); de-biased α -8.5% vs CAPM hurdle 14.9%. Uptrend +34% vs 200-day avg; 12-1 mom +159%; RSI 40. Quality z -0.15 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.89"
    Avoid: not owned. Analyst target 405.47 USD vs 319.93 USD (+27%, 26 analysts); de-biased α -4.5% vs CAPM hurdle 10.0%. Downtrend -2% vs 200-day avg; 12-1 mom -8%; RSI 45. Quality z +0.31 (ROE 22%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 324.71 USD vs 277.92 USD (+17%, 31 analysts); de-biased α -6.7% vs CAPM hurdle 10.8%. Uptrend +9% vs 200-day avg; 12-1 mom +55%; RSI 49. Quality z +0.24 (ROE 30%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 173.36 USD vs 142.76 USD (+21%, 11 analysts); de-biased α -6.0% vs CAPM hurdle 11.0%. Uptrend +5% vs 200-day avg; 12-1 mom +64%; RSI 42. Quality z -0.02 (ROE 6%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -0.97"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,897 JPY (+32%, 17 analysts); de-biased α -3.1% vs CAPM hurdle 10.8%. Downtrend -6% vs 200-day avg; 12-1 mom +13%; RSI 45. Quality z -0.20 (ROE 10%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.02"
    Avoid: not owned. Analyst target 569.78 USD vs 447.60 USD (+27%, 26 analysts); de-biased α -4.5% vs CAPM hurdle 10.3%. Uptrend +0% vs 200-day avg; 12-1 mom -10%; RSI 47. Quality z +0.14 (ROE 7%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.20"
    Avoid: not owned. Analyst target 95.99 HKD vs 49.96 HKD (+92%, 21 analysts); de-biased α +12.5% vs CAPM hurdle 7.3%. Downtrend -27% vs 200-day avg; 12-1 mom -16%; RSI 22. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.22"
    Avoid: not owned. Analyst target 194.13 USD vs 175.60 USD (+11%, 30 analysts); de-biased α -8.6% vs CAPM hurdle 11.9%. Uptrend +4% vs 200-day avg; 12-1 mom +21%; RSI 47. Quality z +0.70 (ROE 23%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,287,000 KRW | $95,281 | 10.5% | Strong Buy |
| MU | Micron Technology | 92 | 895.85 USD | $82,418 | 9.1% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 221,000 KRW | $80,972 | 8.9% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 53.32 EUR | $77,856 | 8.6% | Buy |
| NVDA | NVIDIA | 294 | 216.48 USD | $63,645 | 7.0% | Buy |
| AMAT | Applied Materials | 156 | 404.95 USD | $63,172 | 7.0% | Buy |
| ASX | ASE Technology | 1,332 | 40.78 USD | $54,326 | 6.0% | Buy |
| TSM | TSMC | 117 | 425.30 USD | $49,760 | 5.5% | Buy |
| ASML | ASML Holding | 30 | 1,630.84 USD | $48,925 | 5.4% | Hold |
| KLAC | KLA Corp | 279 | 161.93 USD | $45,177 | 5.0% | Buy |
| AVGO | Broadcom | 100 | 334.51 USD | $33,451 | 3.7% | Hold |
| 8035.T | Tokyo Electron | 500 | 10,250 JPY | $32,418 | 3.6% | Hold |
| LRCX | Lam Research | 105 | 263.45 USD | $27,662 | 3.1% | Hold |
| 6857.T | Advantest | 100 | 34,390 JPY | $21,753 | 2.4% | Hold |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 34.9%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
