---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-10-19 21:04 UTC (Mon Oct 19, 05:04 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Mon 17:04) · Tokyo 🔴 closed (Tue 06:04) · Korea 🔴 closed (Tue 06:04) · Hong Kong 🔴 closed (Tue 05:04) · Xetra 🔴 closed (Mon 23:04) · Euronext Amsterdam 🔴 closed (Mon 23:04)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$903,113** | $128,835 (14%) | $774,277 (86%) | -9.69% | -11.22% | 🟢 Risk-on (+7.2%) | 90% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $903,113), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **LRCX**<br><small>Lam Research</small> | 103 | 272.05 USD | $28,021 | Queued · NYSE/Nasdaq closed | momentum +0.14 · trend -0.03 |
| TRIM | **Infineon**<br><small>IFX.DE</small> | 246 | 52.30 EUR | $14,428 | Queued · Xetra closed | analyst α +0.36 · trend -0.10 |
| TRIM | **ASML**<br><small>ASML Holding</small> | 6 | 1,647.42 USD | $9,885 | Queued · NYSE/Nasdaq closed | quality +0.18 · analyst α -0.15 |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.95 | **MU**<br><small>Micron Technology</small> | 905.35 USD | +68% | +5.8% | +402% | +26% | 38 | +0.12 | 9.2% → 10.0% | – | momentum +0.53 · analyst α +0.48 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.05 | **Samsung**<br><small>005930.KS</small> | 216,250 KRW | +121% | +19.8% | +191% | -7% | 32 | -0.26 | 8.7% → 10.0% | – | analyst α +0.85 · momentum +0.26 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.58 | **SK hynix**<br><small>000660.KS</small> | 1,256,000 KRW | – | +0.0% | +371% | -14% | 26 | +0.62 | 10.2% → 10.0% | – | momentum +0.41 · quality +0.33 · ⚠️ oversold, cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.78 | **NVDA**<br><small>NVIDIA</small> | 217.09 USD | +51% | +1.6% | +23% | +7% | 42 | +0.47 | 8.9% → 9.2% | – | quality +0.21 · analyst α +0.19 |
| 🟢🟢 Strong Buy | +0.77 | **AMAT**<br><small>Applied Materials</small> | 412.87 USD | +55% | +3.2% | +96% | -6% | 31 | +0.03 | 7.1% → 7.7% | – | analyst α +0.27 · momentum +0.12 |
| 🟢 Buy | +0.61 | **ASX**<br><small>ASE Technology</small> | 40.83 USD | +25% | -2.1% | +234% | +27% | 43 | -0.68 | 6.0% → 6.8% | – | momentum +0.35 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.59 | **Infineon**<br><small>IFX.DE</small> | 52.30 EUR | +66% | +5.4% | +65% | -8% | 36 | -0.04 | 8.4% → 6.9% | TRIM 246 | analyst α +0.36 · trend -0.10 |
| 🟢 Buy | +0.46 | **TSM**<br><small>TSMC</small> | 420.22 USD | +31% | -2.4% | +47% | +7% | 39 | +0.58 | 5.4% → 6.5% | – | quality +0.28 · momentum -0.12 |
| 🟢 Buy | +0.43 | **KLAC**<br><small>KLA Corp</small> | 166.41 USD | +40% | -0.3% | +62% | -8% | 32 | +0.51 | 5.1% → 4.6% | – | quality +0.24 · trend -0.12 |
| 🟢 Buy | +0.32 | **ASML**<br><small>ASML Holding</small> | 1,647.42 USD | +27% | -3.8% | +66% | +4% | 39 | +0.42 | 5.5% → 4.3% | TRIM 6 | quality +0.18 · analyst α -0.15 |
| 🟢 Buy | +0.28 | **LRCX**<br><small>Lam Research</small> | 272.05 USD | +38% | -1.3% | +103% | -4% | 35 | +0.02 | 0.0% → 3.1% | BUY 103 | momentum +0.14 · trend -0.03 |
| ⚪ Hold | +0.22 | **Advantest**<br><small>6857.T</small> | 34,440 JPY | +24% | -5.0% | +92% | +21% | 44 | +0.33 | 2.4% → 2.4% | – | analyst α -0.31 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | +0.22 | **Tokyo Electron**<br><small>8035.T</small> | 10,380 JPY | +47% | +1.2% | +79% | +4% | 41 | -0.28 | 3.6% → 3.6% | – | quality -0.18 · analyst α +0.15 |
| ⚪ Hold | +0.08 | **MRVL**<br><small>Marvell Technology</small> | 237.03 USD | +24% | -5.2% | +177% | +34% | 43 | -0.12 | 0.0% → 0.0% | – | analyst α -0.36 · trend +0.25 · ⚠️ rich valuation |
| ⚪ Hold | +0.08 | **AVGO**<br><small>Broadcom</small> | 334.64 USD | +59% | +4.4% | +2% | -9% | 39 | +0.26 | 5.0% → 5.0% | – | analyst α +0.31 · momentum -0.26 |
| ⚪ Hold | -0.10 | **GFS**<br><small>GlobalFoundries</small> | 46.13 USD | +65% | +5.5% | +39% | -16% | 44 | -0.21 | 0.0% → 0.0% | – | analyst α +0.41 · trend -0.18 |
| ⚪ Hold | -0.22 | **INTC**<br><small>Intel</small> | 91.97 USD | +27% | -4.6% | +195% | +8% | 35 | -0.62 | 0.0% → 0.0% | – | momentum +0.30 · analyst α -0.27 · ⚠️ rich valuation, high σ(e) |
| ⚪ Hold | -0.22 | **ASMI**<br><small>ASM.AS</small> | 762.20 EUR | +48% | +1.1% | +53% | -6% | 35 | -0.10 | 0.0% → 0.0% | – | analyst α +0.12 · momentum -0.10 |
| 🔴 Sell | -0.27 | **TER**<br><small>Teradyne</small> | 335.14 USD | +33% | -2.4% | +167% | -3% | 37 | -0.31 | 0.0% → 0.0% | – | quality -0.21 · momentum +0.20 |
| 🔴 Sell | -0.53 | **AMKR**<br><small>Amkor Technology</small> | 41.88 USD | +82% | +9.6% | +61% | -27% | 30 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 |
| 🔴 Sell | -0.55 | **Disco**<br><small>6146.T</small> | 53,900 JPY | +52% | +2.5% | +1% | -18% | 42 | +0.06 | 0.0% → 0.0% | – | momentum -0.30 · analyst α +0.23 |
| 🔴🔴 Strong Sell | -0.76 | **TXN**<br><small>Texas Instruments</small> | 276.12 USD | +18% | -5.5% | +56% | +9% | 47 | +0.24 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.14 |
| 🔴🔴 Strong Sell | -0.99 | **ENTG**<br><small>Entegris</small> | 144.52 USD | +20% | -5.4% | +58% | +6% | 44 | -0.02 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.07 |
| 🔴🔴 Strong Sell | -1.01 | **QCOM**<br><small>Qualcomm</small> | 173.51 USD | +12% | -7.2% | +11% | +3% | 45 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.04 | **SNPS**<br><small>Synopsys</small> | 454.37 USD | +25% | -3.9% | -13% | +2% | 50 | +0.14 | 0.0% → 0.0% | – | momentum -0.35 · analyst α -0.19 |
| 🔴🔴 Strong Sell | -1.06 | **SMIC**<br><small>0981.HK</small> | 52.40 HKD | +83% | +11.3% | -29% | -24% | 25 | -0.99 | 0.0% → 0.0% | – | analyst α +0.66 · momentum -0.53 · ⚠️ oversold |
| 🔴🔴 Strong Sell | -1.08 | **AMD**<br><small>Advanced Micro Devices</small> | 537.76 USD | +15% | -7.6% | +139% | +36% | 40 | -0.15 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -1.12 | **Shin-Etsu**<br><small>4063.T</small> | 5,973 JPY | +30% | -2.5% | +14% | -5% | 48 | -0.20 | 0.0% → 0.0% | – | momentum -0.20 · analyst α -0.12 |
| 🔴🔴 Strong Sell | -1.21 | **CDNS**<br><small>Cadence Design Systems</small> | 325.79 USD | +24% | -4.1% | -13% | -0% | 48 | +0.31 | 0.0% → 0.0% | – | momentum -0.41 · analyst α -0.23 |
| 🔴🔴 Strong Sell | -1.26 | **ARM**<br><small>Arm Holdings</small> | 227.74 USD | +27% | -5.9% | +61% | +2% | 34 | +0.04 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.03 · ⚠️ rich valuation, high σ(e) |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.95"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 905.35 USD (+68%, 46 analysts); de-biased α +5.8% vs CAPM hurdle 14.0%. Uptrend +26% vs 200-day avg; 12-1 mom +402%; RSI 38. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.05"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 216,250 KRW (+121%, 36 analysts); de-biased α +19.8% vs CAPM hurdle 11.3%. Downtrend -7% vs 200-day avg; 12-1 mom +191%; RSI 32. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.58"
    Within rebalance band of target 10.0%: no trade. No reliable analyst target: α set to 0. Downtrend -14% vs 200-day avg; 12-1 mom +371%; RSI 26. Quality z +0.62 (ROE 44%). ⚠️ oversold; cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +0.78"
    Within rebalance band of target 9.2%: no trade. Analyst target 327.70 USD vs 217.09 USD (+51%, 59 analysts); de-biased α +1.6% vs CAPM hurdle 13.9%. Uptrend +7% vs 200-day avg; 12-1 mom +23%; RSI 42. Quality z +0.47 (ROE 101%).

??? success "AMAT (AMAT) — 🟢🟢 Strong Buy, score +0.77"
    Within rebalance band of target 7.7%: no trade. Analyst target 638.94 USD vs 412.87 USD (+55%, 36 analysts); de-biased α +3.2% vs CAPM hurdle 11.6%. Downtrend -6% vs 200-day avg; 12-1 mom +96%; RSI 31. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.61"
    Within rebalance band of target 6.8%: no trade. Analyst target 51.00 USD vs 40.83 USD (+25%, 1 analysts); de-biased α -2.1% vs CAPM hurdle 11.9%. Uptrend +27% vs 200-day avg; 12-1 mom +234%; RSI 43. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.59"
    **TRIM 246 sh** → target 6.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 52.30 EUR (+66%, 23 analysts); de-biased α +5.4% vs CAPM hurdle 14.1%. Downtrend -8% vs 200-day avg; 12-1 mom +65%; RSI 36. Quality z -0.04 (ROE 6%).

??? success "TSM (TSM) — 🟢 Buy, score +0.46"
    Within rebalance band of target 6.5%: no trade. Analyst target 552.26 USD vs 420.22 USD (+31%, 20 analysts); de-biased α -2.4% vs CAPM hurdle 10.8%. Uptrend +7% vs 200-day avg; 12-1 mom +47%; RSI 39. Quality z +0.58 (ROE 35%).

??? success "KLAC (KLAC) — 🟢 Buy, score +0.43"
    Within rebalance band of target 4.6%: no trade. Analyst target 233.77 USD vs 166.41 USD (+40%, 26 analysts); de-biased α -0.3% vs CAPM hurdle 11.1%. Downtrend -8% vs 200-day avg; 12-1 mom +62%; RSI 32. Quality z +0.51 (ROE 87%).

??? success "ASML (ASML) — 🟢 Buy, score +0.32"
    **TRIM 6 sh** → target 4.3% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 2,096.77 USD vs 1,647.42 USD (+27%, 16 analysts); de-biased α -3.8% vs CAPM hurdle 12.3%. Uptrend +4% vs 200-day avg; 12-1 mom +66%; RSI 39. Quality z +0.42 (ROE 50%).

??? success "LRCX (LRCX) — 🟢 Buy, score +0.28"
    **BUY (new) 103 sh** → target 3.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 375.06 USD vs 272.05 USD (+38%, 31 analysts); de-biased α -1.3% vs CAPM hurdle 12.6%. Downtrend -4% vs 200-day avg; 12-1 mom +103%; RSI 35. Quality z +0.02 (ROE 65%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 34,440 JPY (+24%, 21 analysts); de-biased α -5.0% vs CAPM hurdle 13.4%. Uptrend +21% vs 200-day avg; 12-1 mom +92%; RSI 44. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score +0.22"
    Hold zone: keep any existing position, no new money. Analyst target 15,275 JPY vs 10,380 JPY (+47%, 23 analysts); de-biased α +1.2% vs CAPM hurdle 12.8%. Uptrend +4% vs 200-day avg; 12-1 mom +79%; RSI 41. Quality z -0.28 (ROE 29%).

??? note "MRVL (MRVL) — ⚪ Hold, score +0.08"
    Hold zone: not owned, no entry. Analyst target 293.88 USD vs 237.03 USD (+24%, 43 analysts); de-biased α -5.2% vs CAPM hurdle 14.1%. Uptrend +34% vs 200-day avg; 12-1 mom +177%; RSI 43. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? note "AVGO (AVGO) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 531.31 USD vs 334.64 USD (+59%, 47 analysts); de-biased α +4.4% vs CAPM hurdle 11.2%. Downtrend -9% vs 200-day avg; 12-1 mom +2%; RSI 39. Quality z +0.26 (ROE 31%).

??? note "GFS (GFS) — ⚪ Hold, score -0.10"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 46.13 USD (+65%, 22 analysts); de-biased α +5.5% vs CAPM hurdle 12.4%. Downtrend -16% vs 200-day avg; 12-1 mom +39%; RSI 44. Quality z -0.21 (ROE 8%).

??? note "INTC (INTC) — ⚪ Hold, score -0.22"
    Hold zone: not owned, no entry. Analyst target 116.37 USD vs 91.97 USD (+27%, 43 analysts); de-biased α -4.6% vs CAPM hurdle 14.0%. Uptrend +8% vs 200-day avg; 12-1 mom +195%; RSI 35. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.22"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 762.20 EUR (+48%, 19 analysts); de-biased α +1.1% vs CAPM hurdle 13.2%. Downtrend -6% vs 200-day avg; 12-1 mom +53%; RSI 35. Quality z -0.10 (ROE 19%).

??? failure "TER (TER) — 🔴 Sell, score -0.27"
    Avoid: not owned. Analyst target 446.47 USD vs 335.14 USD (+33%, 15 analysts); de-biased α -2.4% vs CAPM hurdle 12.3%. Downtrend -3% vs 200-day avg; 12-1 mom +167%; RSI 37. Quality z -0.31 (ROE 20%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.53"
    Avoid: not owned. Analyst target 76.40 USD vs 41.88 USD (+82%, 10 analysts); de-biased α +9.6% vs CAPM hurdle 14.0%. Downtrend -27% vs 200-day avg; 12-1 mom +61%; RSI 30. Quality z -1.00 (ROE 9%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.55"
    Avoid: not owned. Analyst target 81,730 JPY vs 53,900 JPY (+52%, 20 analysts); de-biased α +2.5% vs CAPM hurdle 11.5%. Downtrend -18% vs 200-day avg; 12-1 mom +1%; RSI 42. Quality z +0.06 (ROE 25%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.76"
    Avoid: not owned. Analyst target 324.71 USD vs 276.12 USD (+18%, 31 analysts); de-biased α -5.5% vs CAPM hurdle 10.8%. Uptrend +9% vs 200-day avg; 12-1 mom +56%; RSI 47. Quality z +0.24 (ROE 30%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.99"
    Avoid: not owned. Analyst target 173.36 USD vs 144.52 USD (+20%, 11 analysts); de-biased α -5.4% vs CAPM hurdle 11.0%. Uptrend +6% vs 200-day avg; 12-1 mom +58%; RSI 44. Quality z -0.02 (ROE 6%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.01"
    Avoid: not owned. Analyst target 194.13 USD vs 173.51 USD (+12%, 30 analysts); de-biased α -7.2% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +11%; RSI 45. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.04"
    Avoid: not owned. Analyst target 569.78 USD vs 454.37 USD (+25%, 26 analysts); de-biased α -3.9% vs CAPM hurdle 10.3%. Uptrend +2% vs 200-day avg; 12-1 mom -13%; RSI 50. Quality z +0.14 (ROE 7%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.06"
    Avoid: not owned. Analyst target 95.99 HKD vs 52.40 HKD (+83%, 21 analysts); de-biased α +11.3% vs CAPM hurdle 7.3%. Downtrend -24% vs 200-day avg; 12-1 mom -29%; RSI 25. Quality z -0.99 (ROE 3%). ⚠️ oversold.

??? failure "AMD (AMD) — 🔴🔴 Strong Sell, score -1.08"
    Avoid: not owned. Analyst target 619.51 USD vs 537.76 USD (+15%, 50 analysts); de-biased α -7.6% vs CAPM hurdle 14.9%. Uptrend +36% vs 200-day avg; 12-1 mom +139%; RSI 40. Quality z -0.15 (ROE 7%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.12"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,973 JPY (+30%, 17 analysts); de-biased α -2.5% vs CAPM hurdle 10.8%. Downtrend -5% vs 200-day avg; 12-1 mom +14%; RSI 48. Quality z -0.20 (ROE 10%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.21"
    Avoid: not owned. Analyst target 405.47 USD vs 325.79 USD (+24%, 26 analysts); de-biased α -4.1% vs CAPM hurdle 10.0%. Downtrend -0% vs 200-day avg; 12-1 mom -13%; RSI 48. Quality z +0.31 (ROE 22%).

??? failure "ARM (ARM) — 🔴🔴 Strong Sell, score -1.26"
    Avoid: not owned. Analyst target 288.70 USD vs 227.74 USD (+27%, 40 analysts); de-biased α -5.9% vs CAPM hurdle 19.6%. Uptrend +2% vs 200-day avg; 12-1 mom +61%; RSI 34. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 98 | 1,256,000 KRW | $92,324 | 10.2% | Strong Buy |
| MU | Micron Technology | 92 | 905.35 USD | $83,292 | 9.2% | Strong Buy |
| NVDA | NVIDIA | 371 | 217.09 USD | $80,540 | 8.9% | Strong Buy |
| 005930.KS | Samsung Electronics | 485 | 216,250 KRW | $78,668 | 8.7% | Strong Buy |
| IFX.DE | Infineon Technologies | 1,301 | 52.30 EUR | $76,306 | 8.4% | Buy |
| AMAT | Applied Materials | 156 | 412.87 USD | $64,408 | 7.1% | Strong Buy |
| ASX | ASE Technology | 1,332 | 40.83 USD | $54,386 | 6.0% | Buy |
| ASML | ASML Holding | 30 | 1,647.42 USD | $49,423 | 5.5% | Buy |
| TSM | TSMC | 117 | 420.22 USD | $49,166 | 5.4% | Buy |
| KLAC | KLA Corp | 279 | 166.41 USD | $46,428 | 5.1% | Buy |
| AVGO | Broadcom | 134 | 334.64 USD | $44,842 | 5.0% | Hold |
| 8035.T | Tokyo Electron | 500 | 10,380 JPY | $32,758 | 3.6% | Hold |
| 6857.T | Advantest | 100 | 34,440 JPY | $21,737 | 2.4% | Hold |

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

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 30.8%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
