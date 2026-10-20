---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-20 06:02 UTC (Tue Oct 20, 02:02 AM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Tue 02:02) · Tokyo 🟢 open (Tue 15:02) · Korea 🟢 open (Tue 15:02) · Hong Kong 🟢 open (Tue 14:02) · Xetra 🔴 closed (Tue 08:02) · Euronext Amsterdam 🔴 closed (Tue 08:02)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$898,065** | $128,835 (14%) | $769,230 (86%) | -10.19% | -11.22% | 🟢 Risk-on (+7.2%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $898,065), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **LRCX**<br><small>Lam Research</small> | 113 | 272.05 USD | $30,742 | Queued · NYSE/Nasdaq closed | momentum +0.14 · trend -0.03 |
| TRIM | **Infineon**<br><small>IFX.DE</small> | 362 | 52.30 EUR | $21,265 | Queued · Xetra closed | analyst α +0.36 · trend -0.09 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.10 | **MU**<br><small>Micron Technology</small> | 905.35 USD | +68% | +5.6% | +416% | +25% | 38 | +0.12 | 9.3% → 10.0% | – | momentum +0.53 · analyst α +0.48 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.95 | **Samsung**<br><small>005930.KS</small> | 210,500 KRW | +127% | +21.1% | +191% | -10% | 31 | -0.26 | 8.6% → 10.0% | – | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.61 | **SK hynix**<br><small>000660.KS</small> | 1,219,000 KRW | – | +0.0% | +371% | -17% | 25 | +0.62 | 10.0% → 10.0% | – | momentum +0.41 · quality +0.33 · ⚠️ oversold, cycle-peak P/E, high σ(e) |
| 🟢 Buy | +0.73 | **NVDA**<br><small>NVIDIA</small> | 217.09 USD | +51% | +1.4% | +23% | +7% | 42 | +0.47 | 9.0% → 9.0% | – | quality +0.21 · momentum -0.17 |
| 🟢 Buy | +0.71 | **AMAT**<br><small>Applied Materials</small> | 412.87 USD | +55% | +3.0% | +107% | -6% | 31 | +0.03 | 7.2% → 7.5% | – | analyst α +0.23 · momentum +0.12 |
| 🟢 Buy | +0.56 | **ASX**<br><small>ASE Technology</small> | 40.83 USD | +25% | -2.2% | +247% | +27% | 43 | -0.68 | 6.1% → 6.5% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.50 | **Infineon**<br><small>IFX.DE</small> | 52.30 EUR | +66% | +5.2% | +65% | -8% | 36 | -0.04 | 8.5% → 6.1% | TRIM 362 | analyst α +0.36 · trend -0.09 |
| 🟢 Buy | +0.44 | **KLAC**<br><small>KLA Corp</small> | 166.41 USD | +40% | -0.4% | +67% | -8% | 32 | +0.51 | 5.2% → 5.0% | – | quality +0.24 · trend -0.10 |
| 🟢 Buy | +0.40 | **TSM**<br><small>TSMC</small> | 420.22 USD | +31% | -2.5% | +47% | +7% | 39 | +0.58 | 5.5% → 5.9% | – | quality +0.28 · momentum -0.12 |
| 🟢 Buy | +0.30 | **LRCX**<br><small>Lam Research</small> | 272.05 USD | +38% | -1.5% | +114% | -4% | 35 | +0.02 | 0.0% → 3.4% | BUY 113 | momentum +0.14 · trend -0.03 |
| ⚪ Hold | +0.24 | **ASML**<br><small>ASML Holding</small> | 1,647.42 USD | +27% | -4.0% | +67% | +4% | 39 | +0.42 | 5.5% → 5.5% | – | quality +0.18 · analyst α -0.15 |
| ⚪ Hold | +0.20 | **Tokyo Electron**<br><small>8035.T</small> | 10,125 JPY | +51% | +1.9% | +79% | +2% | 39 | -0.28 | 3.6% → 3.6% | – | analyst α +0.19 · quality -0.18 |
| ⚪ Hold | +0.18 | **Advantest**<br><small>6857.T</small> | 34,010 JPY | +26% | -4.8% | +92% | +20% | 43 | +0.33 | 2.4% → 2.4% | – | analyst α -0.31 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.17 | **MRVL**<br><small>Marvell Technology</small> | 237.03 USD | +24% | -5.4% | +193% | +34% | 43 | -0.12 | 0.0% → 0.0% | – | analyst α -0.36 · momentum +0.26 · ⚠️ rich valuation |
| ⚪ Hold | +0.13 | **AVGO**<br><small>Broadcom</small> | 334.64 USD | +59% | +4.2% | +5% | -9% | 39 | +0.26 | 5.0% → 5.0% | – | analyst α +0.31 · momentum -0.26 |
| ⚪ Hold | -0.05 | **GFS**<br><small>GlobalFoundries</small> | 46.13 USD | +65% | +5.3% | +41% | -16% | 44 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.16 |
| ⚪ Hold | -0.20 | **ASMI**<br><small>ASM.AS</small> | 762.20 EUR | +48% | +0.9% | +53% | -6% | 35 | -0.10 | 0.0% → 0.0% | – | analyst α +0.12 · momentum -0.10 |
| ⚪ Hold | -0.23 | **INTC**<br><small>Intel</small> | 91.97 USD | +27% | -4.8% | +229% | +8% | 35 | -0.62 | 0.0% → 0.0% | – | momentum +0.30 · analyst α -0.27 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.37 | **TER**<br><small>Teradyne</small> | 335.14 USD | +33% | -2.6% | +177% | -3% | 37 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.40 | **AMKR**<br><small>Amkor Technology</small> | 41.88 USD | +82% | +9.4% | +68% | -27% | 30 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 |
| 🔴 Sell | -0.48 | **Disco**<br><small>6146.T</small> | 52,590 JPY | +55% | +3.3% | +1% | -20% | 39 | +0.06 | 0.0% → 0.0% | – | momentum -0.30 · analyst α +0.27 |
| 🔴🔴 Strong Sell | -0.80 | **TXN**<br><small>Texas Instruments</small> | 276.12 USD | +18% | -5.7% | +57% | +9% | 47 | +0.24 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.14 |
| 🔴🔴 Strong Sell | -0.95 | **QCOM**<br><small>Qualcomm</small> | 173.51 USD | +12% | -7.4% | +21% | +3% | 45 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.03 | **Shin-Etsu**<br><small>4063.T</small> | 5,889 JPY | +32% | -2.2% | +14% | -6% | 44 | -0.20 | 0.0% → 0.0% | – | momentum -0.23 · quality -0.11 |
| 🔴🔴 Strong Sell | -1.05 | **ENTG**<br><small>Entegris</small> | 144.52 USD | +20% | -5.6% | +58% | +6% | 44 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.07 |
| 🔴🔴 Strong Sell | -1.06 | **ARM**<br><small>Arm Holdings</small> | 227.74 USD | +27% | -6.1% | +95% | +1% | 35 | +0.04 | 0.0% → 0.0% | – | analyst α -0.55 · momentum +0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -1.11 | **CDNS**<br><small>Cadence Design Systems</small> | 325.79 USD | +24% | -4.3% | -10% | -0% | 48 | +0.31 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.12 | **SMIC**<br><small>0981.HK</small> | 51.00 HKD | +88% | +12.4% | -25% | -26% | 23 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.14 | **AMD**<br><small>Advanced Micro Devices</small> | 537.76 USD | +15% | -7.8% | +164% | +35% | 40 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.23 | **SNPS**<br><small>Synopsys</small> | 454.37 USD | +25% | -4.1% | -10% | +2% | 50 | +0.14 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.19 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +3.10"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 905.35 USD (+68%, 46 analysts); de-biased α +5.6% vs CAPM hurdle 14.0%. Uptrend +25% vs 200-day avg; 12-1 mom +416%; RSI 38. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.95"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 210,500 KRW (+127%, 36 analysts); de-biased α +21.1% vs CAPM hurdle 11.3%. Downtrend -10% vs 200-day avg; 12-1 mom +191%; RSI 31. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.61"
    Within rebalance band of target 10.0%: no trade. No reliable analyst target: α set to 0. Downtrend -17% vs 200-day avg; 12-1 mom +371%; RSI 25. Quality z +0.62 (ROE 44%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢 Buy, score +0.73"
    Within rebalance band of target 9.0%: no trade. Analyst target 327.70 USD vs 217.09 USD (+51%, 59 analysts); de-biased α +1.4% vs CAPM hurdle 13.9%. Uptrend +7% vs 200-day avg; 12-1 mom +23%; RSI 42. Quality z +0.47 (ROE 101%).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.71"
    Within rebalance band of target 7.5%: no trade. Analyst target 638.94 USD vs 412.87 USD (+55%, 36 analysts); de-biased α +3.0% vs CAPM hurdle 11.6%. Downtrend -6% vs 200-day avg; 12-1 mom +107%; RSI 31. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.56"
    Within rebalance band of target 6.5%: no trade. Analyst target 51.00 USD vs 40.83 USD (+25%, 1 analysts); de-biased α -2.2% vs CAPM hurdle 11.9%. Uptrend +27% vs 200-day avg; 12-1 mom +247%; RSI 43. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.50"
    **TRIM 362 sh** → target 6.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 52.30 EUR (+66%, 23 analysts); de-biased α +5.2% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +65%; RSI 36. Quality z -0.04 (ROE 6%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.44"
    Within rebalance band of target 5.0%: no trade. Analyst target 233.77 USD vs 166.41 USD (+40%, 26 analysts); de-biased α -0.4% vs CAPM hurdle 11.1%. Downtrend -8% vs 200-day avg; 12-1 mom +67%; RSI 32. Quality z +0.51 (ROE 87%).

??? success "TSM (TSM) — 🟢 Buy, score +0.40"
    Within rebalance band of target 5.9%: no trade. Analyst target 552.26 USD vs 420.22 USD (+31%, 20 analysts); de-biased α -2.5% vs CAPM hurdle 10.8%. Uptrend +7% vs 200-day avg; 12-1 mom +47%; RSI 39. Quality z +0.58 (ROE 35%).

??? success "LRCX (LRCX) — 🟢 Buy, score +0.30"
    **BUY (new) 113 sh** → target 3.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 375.06 USD vs 272.05 USD (+38%, 31 analysts); de-biased α -1.5% vs CAPM hurdle 12.6%. Downtrend -4% vs 200-day avg; 12-1 mom +114%; RSI 35. Quality z +0.02 (ROE 65%).

??? note "ASML (ASML) — ⚪ Hold, score +0.24"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,647.42 USD (+27%, 16 analysts); de-biased α -4.0% vs CAPM hurdle 12.3%. Uptrend +4% vs 200-day avg; 12-1 mom +67%; RSI 39. Quality z +0.42 (ROE 50%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.20"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 10,125 JPY (+51%, 23 analysts); de-biased α +1.9% vs CAPM hurdle 12.8%. Uptrend +2% vs 200-day avg; 12-1 mom +79%; RSI 39. Quality z -0.28 (ROE 29%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.18"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 34,010 JPY (+26%, 21 analysts); de-biased α -4.8% vs CAPM hurdle 13.4%. Uptrend +20% vs 200-day avg; 12-1 mom +92%; RSI 43. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.17"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 237.03 USD (+24%, 43 analysts); de-biased α -5.4% vs CAPM hurdle 14.1%. Uptrend +34% vs 200-day avg; 12-1 mom +193%; RSI 43. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.13"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 334.64 USD (+59%, 47 analysts); de-biased α +4.2% vs CAPM hurdle 11.2%. Downtrend -9% vs 200-day avg; 12-1 mom +5%; RSI 39. Quality z +0.26 (ROE 31%).

??? note "GFS (GFS) — ⚪ Hold, score -0.05"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 46.13 USD (+65%, 22 analysts); de-biased α +5.3% vs CAPM hurdle 12.4%. Downtrend -16% vs 200-day avg; 12-1 mom +41%; RSI 44. Quality z -0.21 (ROE 8%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.20"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 762.20 EUR (+48%, 19 analysts); de-biased α +0.9% vs CAPM hurdle 13.2%. Downtrend -6% vs 200-day avg; 12-1 mom +53%; RSI 35. Quality z -0.10 (ROE 19%).

??? note "INTC (INTC) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 116.37 USD vs 91.97 USD (+27%, 43 analysts); de-biased α -4.8% vs CAPM hurdle 14.0%. Uptrend +8% vs 200-day avg; 12-1 mom +229%; RSI 35. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? failure "TER (TER) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 446.47 USD vs 335.14 USD (+33%, 15 analysts); de-biased α -2.6% vs CAPM hurdle 12.3%. Downtrend -3% vs 200-day avg; 12-1 mom +177%; RSI 37. Quality z -0.31 (ROE 20%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.40"
    Avoid: not owned. Analyst target 76.40 USD vs 41.88 USD (+82%, 10 analysts); de-biased α +9.4% vs CAPM hurdle 14.0%. Downtrend -27% vs 200-day avg; 12-1 mom +68%; RSI 30. Quality z -1.00 (ROE 9%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.48"
    Avoid: not owned. Analyst target 81,730 JPY vs 52,590 JPY (+55%, 20 analysts); de-biased α +3.3% vs CAPM hurdle 11.5%. Downtrend -20% vs 200-day avg; 12-1 mom +1%; RSI 39. Quality z +0.06 (ROE 25%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.80"
    Avoid: not owned. Analyst target 324.71 USD vs 276.12 USD (+18%, 31 analysts); de-biased α -5.7% vs CAPM hurdle 10.8%. Uptrend +9% vs 200-day avg; 12-1 mom +57%; RSI 47. Quality z +0.24 (ROE 30%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.95"
    Avoid: not owned. Analyst target 194.13 USD vs 173.51 USD (+12%, 30 analysts); de-biased α -7.4% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +21%; RSI 45. Quality z +0.70 (ROE 23%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.03"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,889 JPY (+32%, 17 analysts); de-biased α -2.2% vs CAPM hurdle 10.8%. Downtrend -6% vs 200-day avg; 12-1 mom +14%; RSI 44. Quality z -0.20 (ROE 10%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -1.05"
    Avoid: not owned. Analyst target 173.36 USD vs 144.52 USD (+20%, 11 analysts); de-biased α -5.6% vs CAPM hurdle 11.0%. Uptrend +6% vs 200-day avg; 12-1 mom +58%; RSI 44. Quality z -0.02 (ROE 6%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.06"
    Avoid: not owned. Analyst target 288.70 USD vs 227.74 USD (+27%, 40 analysts); de-biased α -6.1% vs CAPM hurdle 19.6%. Uptrend +1% vs 200-day avg; 12-1 mom +95%; RSI 35. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.11"
    Avoid: not owned. Analyst target 405.47 USD vs 325.79 USD (+24%, 26 analysts); de-biased α -4.3% vs CAPM hurdle 10.0%. Downtrend -0% vs 200-day avg; 12-1 mom -10%; RSI 48. Quality z +0.31 (ROE 22%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.12"
    Avoid: not owned. Analyst target 95.99 HKD vs 51.00 HKD (+88%, 21 analysts); de-biased α +12.4% vs CAPM hurdle 7.3%. Downtrend -26% vs 200-day avg; 12-1 mom -25%; RSI 23. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.14"
    Avoid: not owned. Analyst target 619.51 USD vs 537.76 USD (+15%, 50 analysts); de-biased α -7.8% vs CAPM hurdle 14.9%. Uptrend +35% vs 200-day avg; 12-1 mom +164%; RSI 40. Quality z -0.15 (ROE 7%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.23"
    Avoid: not owned. Analyst target 569.78 USD vs 454.37 USD (+25%, 26 analysts); de-biased α -4.1% vs CAPM hurdle 10.3%. Uptrend +2% vs 200-day avg; 12-1 mom -10%; RSI 50. Quality z +0.14 (ROE 7%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,219,000 KRW | $89,937 | 10.0% | Strong Buy |
| MU | Micron Technology | 92 | 905.35 USD | $83,292 | 9.3% | Strong Buy |
| NVDA | NVIDIA | 371 | 217.09 USD | $80,540 | 9.0% | Buy |
| 005930.KS | Samsung Electronics | 485 | 210,500 KRW | $76,861 | 8.6% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 52.30 EUR | $76,426 | 8.5% | Buy |
| AMAT | Applied Materials | 156 | 412.87 USD | $64,408 | 7.2% | Buy |
| ASX | ASE Technology | 1,332 | 40.83 USD | $54,386 | 6.1% | Buy |
| ASML | ASML Holding | 30 | 1,647.42 USD | $49,423 | 5.5% | Hold |
| TSM | TSMC | 117 | 420.22 USD | $49,166 | 5.5% | Buy |
| KLAC | KLA Corp | 279 | 166.41 USD | $46,428 | 5.2% | Buy |
| AVGO | Broadcom | 134 | 334.64 USD | $44,842 | 5.0% | Hold |
| 8035.T | Tokyo Electron | 500 | 10,125 JPY | $32,014 | 3.6% | Hold |
| 6857.T | Advantest | 100 | 34,010 JPY | $21,507 | 2.4% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-10-06 17:12 UTC | ADD | KLAC | 189 | 198.10 | $37,441 |
| 2026-10-06 17:12 UTC | TRIM | AVGO | -36 | 377.64 | $13,595 |
| 2026-10-06 10:19 UTC | ADD | IFX.DE | 316 | 63.45 | $22,554 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 31.5%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
