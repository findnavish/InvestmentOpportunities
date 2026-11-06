---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-06 17:58 UTC (Fri Nov 06, 12:58 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🟢 open (Fri 12:58) · Tokyo 🔴 closed (Sat 02:58) · Korea 🔴 closed (Sat 02:58) · Hong Kong 🔴 closed (Sat 01:58) · Xetra 🔴 closed (Fri 18:58) · Euronext Amsterdam 🔴 closed (Fri 18:58)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$807,945** | $364,913 (45%) | $443,032 (55%) | -19.21% | -76.11% | 🔴 Risk-off (-15.3%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $807,945), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| SELL (exit) | **ASML**<br><small>ASML Holding</small> | 30 | 1,418.93 USD | $42,568 | Executed (paper) | analyst α -0.31 · quality +0.18 |
| ADD | **Infineon**<br><small>IFX.DE</small> | 228 | 45.92 EUR | $11,669 | Queued · Xetra closed | analyst α +0.19 · quality -0.04 |
| TRIM | **INTC**<br><small>Intel</small> | 184 | 55.91 USD | $10,287 | Executed (paper) | analyst α +0.36 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| ADD | **SK hynix**<br><small>000660.KS</small> | 12 | 1,144,000 KRW | $10,077 | Queued · Korea closed | momentum +0.41 · quality +0.33 · ⚠️ cycle-peak P/E, high σ(e) |
| ADD | **AMAT**<br><small>Applied Materials</small> | 20 | 333.00 USD | $6,660 | Executed (paper) | analyst α +0.23 · momentum +0.12 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.28 | **MU**<br><small>Micron Technology</small> | 686.28 USD | +121% | +11.6% | +337% | -9% | 31 | +0.12 | 9.9% → 10.0% | – | analyst α +0.66 · momentum +0.53 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.75 | **SK hynix**<br><small>000660.KS</small> | 1,144,000 KRW | – | +0.0% | +223% | -24% | 33 | +0.62 | 5.2% → 6.5% | ADD 12 | momentum +0.41 · quality +0.33 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +1.62 | **MRVL**<br><small>Marvell Technology</small> | 137.16 USD | +114% | +9.7% | +196% | -26% | 24 | -0.12 | 5.5% → 6.5% | – | analyst α +0.48 · momentum +0.35 · ⚠️ oversold, rich valuation |
| 🟢 Buy | +0.72 | **AMAT**<br><small>Applied Materials</small> | 333.00 USD | +92% | +4.8% | +113% | -25% | 31 | +0.03 | 3.8% → 3.8% | ADD 20 | analyst α +0.23 · momentum +0.12 |
| 🟢 Buy | +0.70 | **Advantest**<br><small>6857.T</small> | 28,200 JPY | +51% | -5.8% | +145% | -3% | 35 | +0.33 | 2.2% → 2.9% | – | analyst α -0.23 · momentum +0.20 · ⚠️ rich valuation |
| 🟢 Buy | +0.51 | **INTC**<br><small>Intel</small> | 55.91 USD | +108% | +8.2% | +179% | -36% | 25 | -0.62 | 1.8% → 1.8% | TRIM 184 | analyst α +0.36 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| 🟢 Buy | +0.47 | **Infineon**<br><small>IFX.DE</small> | 45.92 EUR | +89% | +3.5% | +81% | -20% | 33 | -0.04 | 1.4% → 2.9% | ADD 228 | analyst α +0.19 · quality -0.04 |
| 🟢 Buy | +0.26 | **TER**<br><small>Teradyne</small> | 214.73 USD | +108% | +8.6% | +113% | -39% | 23 | -0.31 | 0.9% → 1.4% | – | analyst α +0.41 · trend -0.25 · ⚠️ oversold |
| 🟢 Buy | +0.26 | **LRCX**<br><small>Lam Research</small> | 200.02 USD | +88% | +3.5% | +95% | -29% | 30 | +0.02 | 1.4% → 1.5% | – | analyst α +0.15 · trend -0.12 |
| ⚪ Hold | +0.23 | **TSM**<br><small>TSMC</small> | 371.45 USD | +49% | -5.7% | +58% | -7% | 35 | +0.58 | 5.8% → 5.8% | – | quality +0.28 · analyst α -0.19 |
| ⚪ Hold | +0.22 | **Samsung**<br><small>005930.KS</small> | 190,400 KRW | – | +0.0% | +170% | -19% | 32 | -0.26 | 9.7% → 9.7% | – | momentum +0.23 · quality -0.16 · ⚠️ cycle-peak P/E |
| ⚪ Hold | +0.18 | **NVDA**<br><small>NVIDIA</small> | 186.57 USD | +76% | +0.1% | +18% | -9% | 31 | +0.47 | 1.4% → 1.4% | – | momentum -0.26 · quality +0.21 |
| ⚪ Hold | +0.07 | **Tokyo Electron**<br><small>8035.T</small> | 8,290 JPY | +84% | +2.8% | +112% | -20% | 32 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.12 |
| ⚪ Hold | +0.06 | **KLAC**<br><small>KLA Corp</small> | 137.52 USD | +70% | -0.5% | +61% | -24% | 34 | +0.51 | 4.6% → 4.6% | – | quality +0.24 · analyst α -0.08 |
| ⚪ Hold | +0.05 | **ASX**<br><small>ASE Technology</small> | 31.29 USD | +63% | -1.2% | +189% | -7% | 33 | -0.68 | 1.2% → 1.2% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | -0.03 | **AMKR**<br><small>Amkor Technology</small> | 32.16 USD | +138% | +15.7% | +41% | -43% | 31 | -1.00 | 0.0% → 0.0% | – | analyst α +0.85 · quality -0.43 |
| ⚪ Hold | -0.10 | **AMD**<br><small>Advanced Micro Devices</small> | 437.74 USD | +42% | -8.7% | +142% | +5% | 36 | -0.15 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.25 |
| ⚪ Hold | -0.12 | **Disco**<br><small>6146.T</small> | 40,820 JPY | +100% | +7.1% | +25% | -38% | 27 | +0.06 | 0.0% → 0.0% | – | analyst α +0.31 · trend -0.21 · ⚠️ oversold |
| 🔴 Sell | -0.30 | **ASML**<br><small>ASML Holding</small> | 1,418.93 USD | +48% | -6.3% | +70% | -11% | 34 | +0.42 | 0.0% → 0.0% | SELL 30 | analyst α -0.31 · quality +0.18 |
| 🔴 Sell | -0.36 | **GFS**<br><small>GlobalFoundries</small> | 38.05 USD | +100% | +6.6% | +39% | -31% | 34 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · momentum -0.14 |
| 🔴 Sell | -0.42 | **AVGO**<br><small>Broadcom</small> | 292.93 USD | +81% | +2.4% | +1% | -20% | 32 | +0.26 | 0.0% → 0.0% | – | momentum -0.35 · quality +0.11 |
| 🔴 Sell | -0.49 | **ASMI**<br><small>ASM.AS</small> | 649.60 EUR | +74% | -0.1% | +69% | -20% | 33 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · momentum -0.05 |
| 🔴 Sell | -0.57 | **ARM**<br><small>Arm Holdings</small> | 171.65 USD | +68% | -3.2% | +72% | -26% | 30 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.09 · ⚠️ oversold, rich valuation, high σ(e) |
| 🔴 Sell | -0.58 | **TXN**<br><small>Texas Instruments</small> | 273.77 USD | +19% | -12.9% | +79% | +5% | 41 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴🔴 Strong Sell | -0.76 | **ENTG**<br><small>Entegris</small> | 127.90 USD | +36% | -9.1% | +84% | -8% | 38 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.09 |
| 🔴🔴 Strong Sell | -1.16 | **SMIC**<br><small>0981.HK</small> | 45.58 HKD | +111% | +10.5% | -24% | -32% | 37 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.24 | **SNPS**<br><small>Synopsys</small> | 442.14 USD | +29% | -10.7% | +22% | +0% | 45 | +0.14 | 0.0% → 0.0% | – | analyst α -0.55 · momentum -0.23 |
| 🔴🔴 Strong Sell | -1.27 | **CDNS**<br><small>Cadence Design Systems</small> | 312.58 USD | +30% | -10.4% | +6% | -5% | 43 | +0.31 | 0.0% → 0.0% | – | analyst α -0.48 · momentum -0.30 |
| 🔴🔴 Strong Sell | -1.31 | **Shin-Etsu**<br><small>4063.T</small> | 5,329 JPY | +46% | -6.2% | +30% | -16% | 27 | -0.20 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.17 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.65 | **QCOM**<br><small>Qualcomm</small> | 164.30 USD | +18% | -13.3% | -0% | -3% | 44 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.28"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 686.28 USD (+121%, 46 analysts); de-biased α +11.6% vs CAPM hurdle 14.0%. Downtrend -9% vs 200-day avg; 12-1 mom +337%; RSI 31. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.75"
    **ADD 12 sh** → target 6.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -24% vs 200-day avg; 12-1 mom +223%; RSI 33. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.62"
    Within rebalance band of target 6.5%: no trade. Analyst target 293.88 USD vs 137.16 USD (+114%, 43 analysts); de-biased α +9.7% vs CAPM hurdle 14.1%. Downtrend -26% vs 200-day avg; 12-1 mom +196%; RSI 24. Quality z -0.12 (ROE 19%). ⚠️ oversold; price implies 78% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.72"
    **ADD 20 sh** → target 3.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 333.00 USD (+92%, 36 analysts); de-biased α +4.8% vs CAPM hurdle 11.6%. Downtrend -25% vs 200-day avg; 12-1 mom +113%; RSI 31. Quality z +0.03 (ROE 36%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.70"
    Within rebalance band of target 2.9%: no trade. Analyst target 42,686 JPY vs 28,200 JPY (+51%, 21 analysts); de-biased α -5.8% vs CAPM hurdle 13.4%. Downtrend -3% vs 200-day avg; 12-1 mom +145%; RSI 35. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "INTC (INTC) — 🟢 Buy, score +0.51"
    **TRIM 184 sh** → target 1.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 55.91 USD (+108%, 43 analysts); de-biased α +8.2% vs CAPM hurdle 14.0%. Downtrend -36% vs 200-day avg; 12-1 mom +179%; RSI 25. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.47"
    **ADD 228 sh** → target 2.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 45.92 EUR (+89%, 23 analysts); de-biased α +3.5% vs CAPM hurdle 14.1%. Downtrend -20% vs 200-day avg; 12-1 mom +81%; RSI 33. Quality z -0.04 (ROE 6%).

??? success "TER (TER) — 🟢 Buy, score +0.26"
    Within rebalance band of target 1.4%: no trade. Analyst target 446.47 USD vs 214.73 USD (+108%, 15 analysts); de-biased α +8.6% vs CAPM hurdle 12.3%. Downtrend -39% vs 200-day avg; 12-1 mom +113%; RSI 23. Quality z -0.31 (ROE 20%). ⚠️ oversold.

??? success "LRCX (LRCX) — 🟢 Buy, score +0.26"
    Within rebalance band of target 1.5%: no trade. Analyst target 375.06 USD vs 200.02 USD (+88%, 31 analysts); de-biased α +3.5% vs CAPM hurdle 12.6%. Downtrend -29% vs 200-day avg; 12-1 mom +95%; RSI 30. Quality z +0.02 (ROE 65%).

??? note "TSM (TSM) — ⚪ Hold, score +0.23"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 371.45 USD (+49%, 20 analysts); de-biased α -5.7% vs CAPM hurdle 10.8%. Downtrend -7% vs 200-day avg; 12-1 mom +58%; RSI 35. Quality z +0.58 (ROE 35%).

??? note "Samsung (005930.KS) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. No reliable analyst target: α set to 0. Downtrend -19% vs 200-day avg; 12-1 mom +170%; RSI 32. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? note "NVDA (NVDA) — ⚪ Hold, score +0.18"
    Hold zone: keep any existing position, no new money. Analyst target 327.70 USD vs 186.57 USD (+76%, 59 analysts); de-biased α +0.1% vs CAPM hurdle 13.9%. Downtrend -9% vs 200-day avg; 12-1 mom +18%; RSI 31. Quality z +0.47 (ROE 101%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.07"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 8,290 JPY (+84%, 23 analysts); de-biased α +2.8% vs CAPM hurdle 12.8%. Downtrend -20% vs 200-day avg; 12-1 mom +112%; RSI 32. Quality z -0.28 (ROE 29%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 137.52 USD (+70%, 26 analysts); de-biased α -0.5% vs CAPM hurdle 11.1%. Downtrend -24% vs 200-day avg; 12-1 mom +61%; RSI 34. Quality z +0.51 (ROE 87%).

??? note "ASX (ASX) — ⚪ Hold, score +0.05"
    Hold zone: keep any existing position, no new money. Analyst target 51.00 USD vs 31.29 USD (+63%, 1 analysts); de-biased α -1.2% vs CAPM hurdle 11.9%. Downtrend -7% vs 200-day avg; 12-1 mom +189%; RSI 33. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "AMKR (AMKR) — ⚪ Hold, score -0.03"
    Hold zone: not owned, no entry. Analyst target 76.40 USD vs 32.16 USD (+138%, 10 analysts); de-biased α +15.7% vs CAPM hurdle 14.0%. Downtrend -43% vs 200-day avg; 12-1 mom +41%; RSI 31. Quality z -1.00 (ROE 9%).

??? note "AMD (AMD) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 437.74 USD (+42%, 50 analysts); de-biased α -8.7% vs CAPM hurdle 14.9%. Uptrend +5% vs 200-day avg; 12-1 mom +142%; RSI 36. Quality z -0.15 (ROE 7%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.12"
    Hold zone: not owned, no entry. Analyst target 81,730 JPY vs 40,820 JPY (+100%, 20 analysts); de-biased α +7.1% vs CAPM hurdle 11.5%. Downtrend -38% vs 200-day avg; 12-1 mom +25%; RSI 27. Quality z +0.06 (ROE 25%). ⚠️ oversold.

??? failure "ASML (ASML) — 🔴 Sell, score -0.30"
    **SELL (exit) 30 sh** → target 0.0% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 2,096.77 USD vs 1,418.93 USD (+48%, 16 analysts); de-biased α -6.3% vs CAPM hurdle 12.3%. Downtrend -11% vs 200-day avg; 12-1 mom +70%; RSI 34. Quality z +0.42 (ROE 50%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.36"
    Avoid: not owned. Analyst target 76.00 USD vs 38.05 USD (+100%, 22 analysts); de-biased α +6.6% vs CAPM hurdle 12.4%. Downtrend -31% vs 200-day avg; 12-1 mom +39%; RSI 34. Quality z -0.21 (ROE 8%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.42"
    Avoid: not owned. Analyst target 531.31 USD vs 292.93 USD (+81%, 47 analysts); de-biased α +2.4% vs CAPM hurdle 11.2%. Downtrend -20% vs 200-day avg; 12-1 mom +1%; RSI 32. Quality z +0.26 (ROE 31%).

??? failure "ASMI (ASM.AS) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 1,128.53 EUR vs 649.60 EUR (+74%, 19 analysts); de-biased α -0.1% vs CAPM hurdle 13.2%. Downtrend -20% vs 200-day avg; 12-1 mom +69%; RSI 33. Quality z -0.10 (ROE 19%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 288.70 USD vs 171.65 USD (+68%, 40 analysts); de-biased α -3.2% vs CAPM hurdle 19.6%. Downtrend -26% vs 200-day avg; 12-1 mom +72%; RSI 30. Quality z +0.04 (ROE 12%). ⚠️ oversold; price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "TXN (TXN) — 🔴 Sell, score -0.58"
    Avoid: not owned. Analyst target 324.71 USD vs 273.77 USD (+19%, 31 analysts); de-biased α -12.9% vs CAPM hurdle 10.8%. Uptrend +5% vs 200-day avg; 12-1 mom +79%; RSI 41. Quality z +0.24 (ROE 30%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.76"
    Avoid: not owned. Analyst target 173.36 USD vs 127.90 USD (+36%, 11 analysts); de-biased α -9.1% vs CAPM hurdle 11.0%. Downtrend -8% vs 200-day avg; 12-1 mom +84%; RSI 38. Quality z -0.02 (ROE 6%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.16"
    Avoid: not owned. Analyst target 95.99 HKD vs 45.58 HKD (+111%, 21 analysts); de-biased α +10.5% vs CAPM hurdle 7.3%. Downtrend -32% vs 200-day avg; 12-1 mom -24%; RSI 37. Quality z -0.99 (ROE 3%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.24"
    Avoid: not owned. Analyst target 569.78 USD vs 442.14 USD (+29%, 26 analysts); de-biased α -10.7% vs CAPM hurdle 10.3%. Uptrend +0% vs 200-day avg; 12-1 mom +22%; RSI 45. Quality z +0.14 (ROE 7%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.27"
    Avoid: not owned. Analyst target 405.47 USD vs 312.58 USD (+30%, 26 analysts); de-biased α -10.4% vs CAPM hurdle 10.0%. Downtrend -5% vs 200-day avg; 12-1 mom +6%; RSI 43. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.31"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,329 JPY (+46%, 17 analysts); de-biased α -6.2% vs CAPM hurdle 10.8%. Downtrend -16% vs 200-day avg; 12-1 mom +30%; RSI 27. Quality z -0.20 (ROE 10%). ⚠️ oversold.

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.65"
    Avoid: not owned. Analyst target 194.13 USD vs 164.30 USD (+18%, 30 analysts); de-biased α -13.3% vs CAPM hurdle 11.9%. Downtrend -3% vs 200-day avg; 12-1 mom -0%; RSI 44. Quality z +0.70 (ROE 23%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 686.28 USD | $79,608 | 9.9% | Strong Buy |
| 005930.KS | Samsung Electronics | 562 | 190,400 KRW | $78,550 | 9.7% | Hold |
| TSM | TSMC | 127 | 371.45 USD | $47,174 | 5.8% | Hold |
| MRVL | Marvell Technology | 324 | 137.16 USD | $44,440 | 5.5% | Strong Buy |
| 000660.KS | SK hynix | 50 | 1,144,000 KRW | $41,989 | 5.2% | Strong Buy |
| KLAC | KLA Corp | 268 | 137.52 USD | $36,857 | 4.6% | Hold |
| AMAT | Applied Materials | 91 | 333.00 USD | $30,303 | 3.8% | Buy |
| 6857.T | Advantest | 100 | 28,200 JPY | $17,817 | 2.2% | Buy |
| INTC | Intel | 263 | 55.91 USD | $14,704 | 1.8% | Buy |
| LRCX | Lam Research | 58 | 200.02 USD | $11,601 | 1.4% | Buy |
| IFX.DE | Infineon Technologies | 225 | 45.92 EUR | $11,516 | 1.4% | Buy |
| NVDA | NVIDIA | 60 | 186.57 USD | $11,194 | 1.4% | Hold |
| ASX | ASE Technology | 312 | 31.29 USD | $9,762 | 1.2% | Hold |
| TER | Teradyne | 35 | 214.73 USD | $7,516 | 0.9% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-11-03 15:09 UTC | TRIM | NVDA | -141 | 208.26 | $29,365 |
| 2026-11-02 15:55 UTC | BUY (new) | TER | 35 | 270.99 | $9,485 |
| 2026-11-02 15:55 UTC | ADD | MRVL | 35 | 184.11 | $6,444 |
| 2026-11-02 15:55 UTC | TRIM | IFX.DE | -1,076 | 52.66 | $63,473 |
| 2026-11-02 06:06 UTC | TRIM | 000660.KS | -18 | 1,490,500.00 | $20,008 |
| 2026-11-02 06:06 UTC | TRIM | 005930.KS | -163 | 231,750.00 | $28,171 |
| 2026-11-02 06:06 UTC | SELL (exit) | 8035.T | -500 | 10,115.00 | $32,062 |
| 2026-10-30 19:24 UTC | TRIM | MU | -28 | 866.70 | $24,267 |
| 2026-10-30 19:24 UTC | TRIM | AMAT | -65 | 385.15 | $25,035 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 61.3%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
