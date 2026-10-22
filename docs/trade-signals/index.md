---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-22 23:23 UTC (Thu Oct 22, 07:23 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Thu 19:23) · Tokyo 🔴 closed (Fri 08:23) · Korea 🔴 closed (Fri 08:23) · Hong Kong 🔴 closed (Fri 07:23) · Xetra 🔴 closed (Fri 01:23) · Euronext Amsterdam 🔴 closed (Fri 01:23)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$865,234** | $104,680 (12%) | $760,554 (88%) | -13.48% | -15.90% | 🟢 Risk-on (+1.0%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $865,234), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| ADD | **KLAC**<br><small>KLA Corp</small> | 89 | 147.83 USD | $13,157 | Queued · NYSE/Nasdaq closed | quality +0.24 · trend -0.14 · ⚠️ oversold |
| ADD | **LRCX**<br><small>Lam Research</small> | 52 | 230.16 USD | $11,968 | Queued · NYSE/Nasdaq closed | analyst α +0.23 · trend -0.16 · ⚠️ oversold |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.11 | **MU**<br><small>Micron Technology</small> | 857.01 USD | +77% | +5.8% | +430% | +18% | 35 | +0.12 | 9.1% → 10.0% | – | momentum +0.53 · analyst α +0.48 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.17 | **Samsung**<br><small>005930.KS</small> | 215,000 KRW | +122% | +17.8% | +182% | -8% | 36 | -0.26 | 9.1% → 10.0% | – | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.56 | **SK hynix**<br><small>000660.KS</small> | 1,223,000 KRW | – | +0.0% | +309% | -17% | 29 | +0.62 | 10.5% → 10.0% | – | momentum +0.41 · quality +0.33 · ⚠️ oversold, cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.83 | **AMAT**<br><small>Applied Materials</small> | 375.45 USD | +70% | +4.7% | +111% | -15% | 25 | +0.03 | 8.8% → 8.5% | – | analyst α +0.31 · momentum +0.12 · ⚠️ oversold |
| 🟢 Buy | +0.68 | **Infineon**<br><small>IFX.DE</small> | 49.94 EUR | +74% | +5.0% | +77% | -12% | 33 | -0.04 | 8.4% → 8.1% | – | analyst α +0.36 · trend -0.07 |
| 🟢 Buy | +0.51 | **LRCX**<br><small>Lam Research</small> | 230.16 USD | +63% | +2.6% | +113% | -19% | 25 | +0.02 | 4.3% → 5.7% | ADD 52 | analyst α +0.23 · trend -0.16 · ⚠️ oversold |
| 🟢 Buy | +0.50 | **NVDA**<br><small>NVIDIA</small> | 212.28 USD | +54% | +0.1% | +25% | +4% | 39 | +0.47 | 7.2% → 6.0% | – | quality +0.21 · momentum -0.17 |
| 🟢 Buy | +0.48 | **ASX**<br><small>ASE Technology</small> | 37.72 USD | +35% | -2.0% | +250% | +16% | 37 | -0.68 | 5.8% → 5.4% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.46 | **KLAC**<br><small>KLA Corp</small> | 147.83 USD | +58% | +1.8% | +65% | -18% | 24 | +0.51 | 3.6% → 5.1% | ADD 89 | quality +0.24 · trend -0.14 · ⚠️ oversold |
| ⚪ Hold | +0.22 | **Tokyo Electron**<br><small>8035.T</small> | 9,499 JPY | +61% | +2.2% | +83% | -5% | 35 | -0.28 | 3.5% → 3.5% | – | quality -0.18 · analyst α +0.15 |
| ⚪ Hold | +0.22 | **TSM**<br><small>TSMC</small> | 412.39 USD | +34% | -4.1% | +53% | +4% | 38 | +0.58 | 6.1% → 6.1% | – | quality +0.28 · analyst α -0.19 |
| ⚪ Hold | +0.16 | **AVGO**<br><small>Broadcom</small> | 323.33 USD | +64% | +3.4% | +4% | -12% | 35 | +0.26 | 3.7% → 3.7% | – | analyst α +0.27 · momentum -0.26 |
| ⚪ Hold | +0.05 | **ASML**<br><small>ASML Holding</small> | 1,561.35 USD | +34% | -4.4% | +71% | -1% | 34 | +0.42 | 5.4% → 5.4% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | -0.10 | **GFS**<br><small>GlobalFoundries</small> | 43.40 USD | +75% | +5.7% | +31% | -21% | 38 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.18 |
| ⚪ Hold | -0.12 | **MRVL**<br><small>Marvell Technology</small> | 223.55 USD | +31% | -5.7% | +210% | +25% | 38 | -0.12 | 0.0% → 0.0% | – | analyst α -0.48 · momentum +0.26 · ⚠️ rich valuation |
| ⚪ Hold | -0.12 | **Advantest**<br><small>6857.T</small> | 32,630 JPY | +31% | -5.6% | +79% | +14% | 40 | +0.33 | 2.4% → 2.4% | – | analyst α -0.41 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | -0.18 | **TER**<br><small>Teradyne</small> | 308.33 USD | +45% | -1.9% | +172% | -11% | 33 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.34 | **INTC**<br><small>Intel</small> | 85.49 USD | +36% | -4.5% | +222% | -0% | 30 | -0.62 | 0.0% → 0.0% | – | momentum +0.30 · analyst α -0.27 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.38 | **ENTG**<br><small>Entegris</small> | 128.06 USD | +35% | -3.9% | +63% | -6% | 35 | -0.02 | 0.0% → 0.0% | – | analyst α -0.08 · momentum -0.05 |
| 🔴 Sell | -0.44 | **ASMI**<br><small>ASM.AS</small> | 709.80 EUR | +59% | +1.5% | +52% | -12% | 31 | -0.10 | 0.0% → 0.0% | – | momentum -0.12 · trend -0.09 |
| 🔴 Sell | -0.49 | **AMKR**<br><small>Amkor Technology</small> | 39.06 USD | +96% | +10.5% | +67% | -32% | 30 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 · ⚠️ oversold |
| 🔴 Sell | -0.60 | **ARM**<br><small>Arm Holdings</small> | 210.09 USD | +37% | -5.6% | +96% | -7% | 31 | +0.04 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.65 | **AMD**<br><small>Advanced Micro Devices</small> | 507.76 USD | +22% | -8.2% | +158% | +27% | 36 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.66 | **Disco**<br><small>6146.T</small> | 50,910 JPY | +61% | +2.4% | +1% | -22% | 36 | +0.06 | 0.0% → 0.0% | – | momentum -0.30 · trend -0.21 |
| 🔴🔴 Strong Sell | -0.97 | **TXN**<br><small>Texas Instruments</small> | 279.56 USD | +16% | -8.2% | +55% | +10% | 50 | +0.24 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.14 |
| 🔴🔴 Strong Sell | -1.03 | **SNPS**<br><small>Synopsys</small> | 422.63 USD | +35% | -3.9% | -10% | -5% | 39 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.12 |
| 🔴🔴 Strong Sell | -1.10 | **SMIC**<br><small>0981.HK</small> | 46.84 HKD | +105% | +14.4% | -18% | -32% | 18 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.23 | **CDNS**<br><small>Cadence Design Systems</small> | 309.84 USD | +31% | -4.8% | -7% | -5% | 41 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.31 |
| 🔴🔴 Strong Sell | -1.25 | **Shin-Etsu**<br><small>4063.T</small> | 5,821 JPY | +33% | -4.0% | +16% | -7% | 42 | -0.20 | 0.0% → 0.0% | – | momentum -0.23 · analyst α -0.15 |
| 🔴🔴 Strong Sell | -1.31 | **QCOM**<br><small>Qualcomm</small> | 172.89 USD | +12% | -9.4% | +19% | +3% | 45 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.11"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 857.01 USD (+77%, 46 analysts); de-biased α +5.8% vs CAPM hurdle 14.0%. Uptrend +18% vs 200-day avg; 12-1 mom +430%; RSI 35. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.17"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 215,000 KRW (+122%, 36 analysts); de-biased α +17.8% vs CAPM hurdle 11.3%. Downtrend -8% vs 200-day avg; 12-1 mom +182%; RSI 36. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.56"
    Within rebalance band of target 10.0%: no trade. No reliable analyst target: α set to 0. Downtrend -17% vs 200-day avg; 12-1 mom +309%; RSI 29. Quality z +0.62 (ROE 44%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "AMAT (AMAT) — 🟢🟢 Strong Buy, score +0.83"
    Within rebalance band of target 8.5%: no trade. Analyst target 638.94 USD vs 375.45 USD (+70%, 36 analysts); de-biased α +4.7% vs CAPM hurdle 11.6%. Downtrend -15% vs 200-day avg; 12-1 mom +111%; RSI 25. Quality z +0.03 (ROE 36%). ⚠️ oversold.

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.68"
    Within rebalance band of target 8.1%: no trade. Analyst target 86.74 EUR vs 49.94 EUR (+74%, 23 analysts); de-biased α +5.0% vs CAPM hurdle 14.1%. Downtrend -12% vs 200-day avg; 12-1 mom +77%; RSI 33. Quality z -0.04 (ROE 6%).

??? success "LRCX (LRCX) — 🟢 Buy, score +0.51"
    **ADD 52 sh** → target 5.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 375.06 USD vs 230.16 USD (+63%, 31 analysts); de-biased α +2.6% vs CAPM hurdle 12.6%. Downtrend -19% vs 200-day avg; 12-1 mom +113%; RSI 25. Quality z +0.02 (ROE 65%). ⚠️ oversold.

??? success "NVDA (NVDA) — 🟢 Buy, score +0.50"
    Within rebalance band of target 6.0%: no trade. Analyst target 327.70 USD vs 212.28 USD (+54%, 59 analysts); de-biased α +0.1% vs CAPM hurdle 13.9%. Uptrend +4% vs 200-day avg; 12-1 mom +25%; RSI 39. Quality z +0.47 (ROE 101%).

??? success "ASX (ASX) — 🟢 Buy, score +0.48"
    Within rebalance band of target 5.4%: no trade. Analyst target 51.00 USD vs 37.72 USD (+35%, 1 analysts); de-biased α -2.0% vs CAPM hurdle 11.9%. Uptrend +16% vs 200-day avg; 12-1 mom +250%; RSI 37. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.46"
    **ADD 89 sh** → target 5.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 233.77 USD vs 147.83 USD (+58%, 26 analysts); de-biased α +1.8% vs CAPM hurdle 11.1%. Downtrend -18% vs 200-day avg; 12-1 mom +65%; RSI 24. Quality z +0.51 (ROE 87%). ⚠️ oversold.

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 9,499 JPY (+61%, 23 analysts); de-biased α +2.2% vs CAPM hurdle 12.8%. Downtrend -5% vs 200-day avg; 12-1 mom +83%; RSI 35. Quality z -0.28 (ROE 29%).

??? note "TSM (TSM) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 412.39 USD (+34%, 20 analysts); de-biased α -4.1% vs CAPM hurdle 10.8%. Uptrend +4% vs 200-day avg; 12-1 mom +53%; RSI 38. Quality z +0.58 (ROE 35%).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.16"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 323.33 USD (+64%, 47 analysts); de-biased α +3.4% vs CAPM hurdle 11.2%. Downtrend -12% vs 200-day avg; 12-1 mom +4%; RSI 35. Quality z +0.26 (ROE 31%).

??? note "ASML (ASML) — ⚪ Hold, score +0.05"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,561.35 USD (+34%, 16 analysts); de-biased α -4.4% vs CAPM hurdle 12.3%. Downtrend -1% vs 200-day avg; 12-1 mom +71%; RSI 34. Quality z +0.42 (ROE 50%).

??? note "GFS (GFS) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 43.40 USD (+75%, 22 analysts); de-biased α +5.7% vs CAPM hurdle 12.4%. Downtrend -21% vs 200-day avg; 12-1 mom +31%; RSI 38. Quality z -0.21 (ROE 8%).

??? note "MRVL (MRVL) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 223.55 USD (+31%, 43 analysts); de-biased α -5.7% vs CAPM hurdle 14.1%. Uptrend +25% vs 200-day avg; 12-1 mom +210%; RSI 38. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "Advantest (6857.T) — ⚪ Hold, score -0.12"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 32,630 JPY (+31%, 21 analysts); de-biased α -5.6% vs CAPM hurdle 13.4%. Uptrend +14% vs 200-day avg; 12-1 mom +79%; RSI 40. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "TER (TER) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 446.47 USD vs 308.33 USD (+45%, 15 analysts); de-biased α -1.9% vs CAPM hurdle 12.3%. Downtrend -11% vs 200-day avg; 12-1 mom +172%; RSI 33. Quality z -0.31 (ROE 20%).

??? failure "INTC (INTC) — 🔴 Sell, score -0.34"
    Avoid: not owned. Analyst target 116.37 USD vs 85.49 USD (+36%, 43 analysts); de-biased α -4.5% vs CAPM hurdle 14.0%. Downtrend -0% vs 200-day avg; 12-1 mom +222%; RSI 30. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.38"
    Avoid: not owned. Analyst target 173.36 USD vs 128.06 USD (+35%, 11 analysts); de-biased α -3.9% vs CAPM hurdle 11.0%. Downtrend -6% vs 200-day avg; 12-1 mom +63%; RSI 35. Quality z -0.02 (ROE 6%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.44"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 709.80 EUR (+59%, 19 analysts); de-biased α +1.5% vs CAPM hurdle 13.2%. Downtrend -12% vs 200-day avg; 12-1 mom +52%; RSI 31. Quality z -0.10 (ROE 19%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 76.40 USD vs 39.06 USD (+96%, 10 analysts); de-biased α +10.5% vs CAPM hurdle 14.0%. Downtrend -32% vs 200-day avg; 12-1 mom +67%; RSI 30. Quality z -1.00 (ROE 9%). ⚠️ oversold.

??? failure "ARM (ARM) — 🔴 Sell, score -0.60"
    Avoid: not owned. Analyst target 288.70 USD vs 210.09 USD (+37%, 40 analysts); de-biased α -5.6% vs CAPM hurdle 19.6%. Downtrend -7% vs 200-day avg; 12-1 mom +96%; RSI 31. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AMD (AMD) — 🔴 Sell, score -0.65"
    Avoid: not owned. Analyst target 619.51 USD vs 507.76 USD (+22%, 50 analysts); de-biased α -8.2% vs CAPM hurdle 14.9%. Uptrend +27% vs 200-day avg; 12-1 mom +158%; RSI 36. Quality z -0.15 (ROE 7%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.66"
    Avoid: not owned. Analyst target 81,730 JPY vs 50,910 JPY (+61%, 20 analysts); de-biased α +2.4% vs CAPM hurdle 11.5%. Downtrend -22% vs 200-day avg; 12-1 mom +1%; RSI 36. Quality z +0.06 (ROE 25%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.97"
    Avoid: not owned. Analyst target 324.71 USD vs 279.56 USD (+16%, 31 analysts); de-biased α -8.2% vs CAPM hurdle 10.8%. Uptrend +10% vs 200-day avg; 12-1 mom +55%; RSI 50. Quality z +0.24 (ROE 30%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.03"
    Avoid: not owned. Analyst target 569.78 USD vs 422.63 USD (+35%, 26 analysts); de-biased α -3.9% vs CAPM hurdle 10.3%. Downtrend -5% vs 200-day avg; 12-1 mom -10%; RSI 39. Quality z +0.14 (ROE 7%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.10"
    Avoid: not owned. Analyst target 95.99 HKD vs 46.84 HKD (+105%, 21 analysts); de-biased α +14.4% vs CAPM hurdle 7.3%. Downtrend -32% vs 200-day avg; 12-1 mom -18%; RSI 18. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.23"
    Avoid: not owned. Analyst target 405.47 USD vs 309.84 USD (+31%, 26 analysts); de-biased α -4.8% vs CAPM hurdle 10.0%. Downtrend -5% vs 200-day avg; 12-1 mom -7%; RSI 41. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.25"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,821 JPY (+33%, 17 analysts); de-biased α -4.0% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +16%; RSI 42. Quality z -0.20 (ROE 10%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.31"
    Avoid: not owned. Analyst target 194.13 USD vs 172.89 USD (+12%, 30 analysts); de-biased α -9.4% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +19%; RSI 45. Quality z +0.70 (ROE 23%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,223,000 KRW | $90,435 | 10.5% | Strong Buy |
| MU | Micron Technology | 92 | 857.01 USD | $78,845 | 9.1% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 215,000 KRW | $78,680 | 9.1% | Strong Buy |
| AMAT | Applied Materials | 202 | 375.45 USD | $75,841 | 8.8% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 49.94 EUR | $72,913 | 8.4% | Buy |
| NVDA | NVIDIA | 294 | 212.28 USD | $62,411 | 7.2% | Buy |
| TSM | TSMC | 127 | 412.39 USD | $52,374 | 6.1% | Hold |
| ASX | ASE Technology | 1,332 | 37.72 USD | $50,250 | 5.8% | Buy |
| ASML | ASML Holding | 30 | 1,561.35 USD | $46,840 | 5.4% | Hold |
| LRCX | Lam Research | 162 | 230.16 USD | $37,286 | 4.3% | Buy |
| AVGO | Broadcom | 100 | 323.33 USD | $32,333 | 3.7% | Hold |
| KLAC | KLA Corp | 211 | 147.83 USD | $31,192 | 3.6% | Buy |
| 8035.T | Tokyo Electron | 500 | 9,499 JPY | $30,322 | 3.5% | Hold |
| 6857.T | Advantest | 100 | 32,630 JPY | $20,831 | 2.4% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-10-22 15:18 UTC | ADD | LRCX | 57 | 234.49 | $13,366 |
| 2026-10-22 15:18 UTC | ADD | AMAT | 46 | 380.67 | $17,511 |
| 2026-10-22 15:18 UTC | TRIM | TSM | -27 | 414.23 | $11,184 |
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 40.1%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
