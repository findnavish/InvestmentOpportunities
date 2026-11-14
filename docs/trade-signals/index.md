---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-14 03:17 UTC (Fri Nov 13, 10:17 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Fri 22:17) · Tokyo 🔴 closed (Sat 12:17) · Korea 🔴 closed (Sat 12:17) · Hong Kong 🔴 closed (Sat 11:17) · Xetra 🔴 closed (Sat 04:17) · Euronext Amsterdam 🔴 closed (Sat 04:17)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$852,109** | $311,442 (37%) | $540,667 (63%) | -14.79% | -73.59% | 🔴 Risk-off (-6.8%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $852,109), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| TRIM | **SK hynix**<br><small>000660.KS</small> | 44 | 1,216,000 KRW | $40,075 | Queued · Korea closed | quality +0.33 · momentum +0.20 · ⚠️ cycle-peak P/E, high σ(e) |
| TRIM | **TSM**<br><small>TSMC</small> | 80 | 398.63 USD | $31,890 | Queued · NYSE/Nasdaq closed | quality +0.28 · analyst α -0.19 |
| ADD | **MRVL**<br><small>Marvell Technology</small> | 100 | 156.71 USD | $15,671 | Queued · NYSE/Nasdaq closed | momentum +0.35 · analyst α +0.31 · ⚠️ rich valuation |
| ADD | **ASX**<br><small>ASE Technology</small> | 233 | 35.54 USD | $8,282 | Queued · NYSE/Nasdaq closed | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| ADD | **INTC**<br><small>Intel</small> | 110 | 59.67 USD | $6,563 | Queued · NYSE/Nasdaq closed | analyst α +0.36 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.88 | **MU**<br><small>Micron Technology</small> | 778.40 USD | +95% | +8.2% | +281% | +2% | 42 | +0.12 | 10.6% → 10.0% | – | momentum +0.53 · analyst α +0.41 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +2.41 | **Samsung**<br><small>005930.KS</small> | 207,000 KRW | +131% | +17.8% | +111% | -13% | 43 | -0.26 | 8.3% → 10.0% | – | analyst α +0.85 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.40 | **MRVL**<br><small>Marvell Technology</small> | 156.71 USD | +88% | +6.2% | +171% | -16% | 35 | -0.12 | 4.6% → 6.4% | ADD 100 | momentum +0.35 · analyst α +0.31 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.10 | **SK hynix**<br><small>000660.KS</small> | 1,216,000 KRW | – | +0.0% | +104% | -20% | 40 | +0.62 | 9.4% → 4.7% | TRIM 44 | quality +0.33 · momentum +0.20 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.93 | **NVDA**<br><small>NVIDIA</small> | 162.82 USD | +101% | +9.7% | +12% | -20% | 25 | +0.47 | 6.4% → 6.6% | – | analyst α +0.48 · momentum -0.23 · ⚠️ oversold |
| 🟢 Buy | +0.65 | **AMAT**<br><small>Applied Materials</small> | 370.25 USD | +73% | +3.2% | +87% | -17% | 43 | +0.03 | 3.6% → 3.9% | – | analyst α +0.15 · momentum +0.14 |
| 🟢 Buy | +0.51 | **ASX**<br><small>ASE Technology</small> | 35.54 USD | +43% | -2.0% | +182% | +5% | 43 | -0.68 | 2.4% → 3.4% | ADD 233 | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.45 | **INTC**<br><small>Intel</small> | 59.67 USD | +95% | +8.1% | +152% | -32% | 32 | -0.62 | 1.1% → 1.8% | ADD 110 | analyst α +0.36 · momentum +0.30 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.25 | **TSM**<br><small>TSMC</small> | 398.63 USD | +39% | -5.0% | +47% | -1% | 45 | +0.58 | 5.9% → 2.2% | TRIM 80 | quality +0.28 · analyst α -0.19 |
| ⚪ Hold | +0.08 | **LRCX**<br><small>Lam Research</small> | 225.91 USD | +66% | +1.3% | +73% | -20% | 42 | +0.02 | 1.5% → 1.5% | – | trend -0.12 · analyst α +0.08 |
| ⚪ Hold | +0.07 | **ASML**<br><small>ASML Holding</small> | 1,494.80 USD | +40% | -5.0% | +61% | -6% | 42 | +0.42 | 0.0% → 0.0% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | +0.07 | **KLAC**<br><small>KLA Corp</small> | 152.33 USD | +53% | -1.4% | +46% | -16% | 45 | +0.51 | 4.8% → 4.8% | – | quality +0.24 · momentum -0.10 |
| ⚪ Hold | +0.05 | **Infineon**<br><small>IFX.DE</small> | 49.88 EUR | +74% | +3.0% | +50% | -13% | 45 | -0.04 | 1.5% → 1.5% | – | analyst α +0.12 · momentum -0.05 |
| ⚪ Hold | -0.04 | **TER**<br><small>Teradyne</small> | 249.49 USD | +79% | +4.6% | +92% | -29% | 37 | -0.31 | 1.0% → 1.0% | – | analyst α +0.23 · trend -0.21 |
| ⚪ Hold | -0.09 | **Advantest**<br><small>6857.T</small> | 30,730 JPY | +39% | -5.7% | +55% | +5% | 44 | +0.33 | 2.3% → 2.3% | – | analyst α -0.31 · quality +0.16 · ⚠️ rich valuation |
| ⚪ Hold | -0.19 | **ASMI**<br><small>ASM.AS</small> | 694.20 EUR | +63% | +0.3% | +57% | -14% | 43 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · trend -0.02 |
| ⚪ Hold | -0.23 | **Tokyo Electron**<br><small>8035.T</small> | 9,404 JPY | +62% | +0.5% | +60% | -9% | 45 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.05 |
| 🔴 Sell | -0.31 | **GFS**<br><small>GlobalFoundries</small> | 41.44 USD | +83% | +5.7% | +43% | -24% | 44 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.14 |
| 🔴 Sell | -0.39 | **ARM**<br><small>Arm Holdings</small> | 190.42 USD | +52% | -4.1% | +65% | -18% | 41 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.46 | **AMD**<br><small>Advanced Micro Devices</small> | 534.09 USD | +16% | -11.8% | +117% | +26% | 50 | -0.15 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.46 | **ENTG**<br><small>Entegris</small> | 147.36 USD | +18% | -10.4% | +75% | +6% | 51 | -0.02 | 0.0% → 0.0% | – | analyst α -0.48 · trend +0.21 |
| 🔴 Sell | -0.53 | **Disco**<br><small>6146.T</small> | 47,440 JPY | +72% | +3.3% | +4% | -27% | 44 | +0.06 | 0.0% → 0.0% | – | momentum -0.26 · analyst α +0.19 |
| 🔴 Sell | -0.67 | **AMKR**<br><small>Amkor Technology</small> | 36.10 USD | +112% | +12.4% | +29% | -36% | 42 | -1.00 | 0.0% → 0.0% | – | analyst α +0.66 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.75 | **AVGO**<br><small>Broadcom</small> | 346.62 USD | +53% | -1.4% | -2% | -5% | 53 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴🔴 Strong Sell | -0.80 | **QCOM**<br><small>Qualcomm</small> | 172.39 USD | +13% | -11.5% | +3% | +2% | 49 | +0.70 | 0.0% → 0.0% | – | analyst α -0.55 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.04 | **SNPS**<br><small>Synopsys</small> | 455.24 USD | +25% | -8.4% | +17% | +3% | 49 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.20 |
| 🔴🔴 Strong Sell | -1.08 | **TXN**<br><small>Texas Instruments</small> | 303.68 USD | +7% | -12.6% | +74% | +16% | 55 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.25 |
| 🔴🔴 Strong Sell | -1.21 | **SMIC**<br><small>0981.HK</small> | 48.52 HKD | +98% | +10.5% | -24% | -27% | 45 | -0.99 | 0.0% → 0.0% | – | analyst α +0.55 · momentum -0.53 |
| 🔴🔴 Strong Sell | -1.30 | **CDNS**<br><small>Cadence Design Systems</small> | 323.04 USD | +26% | -8.2% | +3% | -2% | 48 | +0.31 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.35 |
| 🔴🔴 Strong Sell | -1.33 | **Shin-Etsu**<br><small>4063.T</small> | 5,676 JPY | +37% | -5.2% | +31% | -10% | 45 | -0.20 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.14 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.88"
    Within rebalance band of target 10.0%: no trade. Analyst target 1,520.02 USD vs 778.40 USD (+95%, 46 analysts); de-biased α +8.2% vs CAPM hurdle 14.0%. Uptrend +2% vs 200-day avg; 12-1 mom +281%; RSI 42. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +2.41"
    Within rebalance band of target 10.0%: no trade. Analyst target 477,517 KRW vs 207,000 KRW (+131%, 36 analysts); de-biased α +17.8% vs CAPM hurdle 11.3%. Downtrend -13% vs 200-day avg; 12-1 mom +111%; RSI 43. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.40"
    **ADD 100 sh** → target 6.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 293.88 USD vs 156.71 USD (+88%, 43 analysts); de-biased α +6.2% vs CAPM hurdle 14.1%. Downtrend -16% vs 200-day avg; 12-1 mom +171%; RSI 35. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.10"
    **TRIM 44 sh** → target 4.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). No reliable analyst target: α set to 0. Downtrend -20% vs 200-day avg; 12-1 mom +104%; RSI 40. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +0.93"
    Within rebalance band of target 6.6%: no trade. Analyst target 327.70 USD vs 162.82 USD (+101%, 59 analysts); de-biased α +9.7% vs CAPM hurdle 13.9%. Downtrend -20% vs 200-day avg; 12-1 mom +12%; RSI 25. Quality z +0.47 (ROE 101%). ⚠️ oversold.

??? success "AMAT (AMAT) — 🟢 Buy, score +0.65"
    Within rebalance band of target 3.9%: no trade. Analyst target 638.94 USD vs 370.25 USD (+73%, 36 analysts); de-biased α +3.2% vs CAPM hurdle 11.6%. Downtrend -17% vs 200-day avg; 12-1 mom +87%; RSI 43. Quality z +0.03 (ROE 36%).

??? success "ASX (ASX) — 🟢 Buy, score +0.51"
    **ADD 233 sh** → target 3.4% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 35.54 USD (+43%, 1 analysts); de-biased α -2.0% vs CAPM hurdle 11.9%. Uptrend +5% vs 200-day avg; 12-1 mom +182%; RSI 43. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "INTC (INTC) — 🟢 Buy, score +0.45"
    **ADD 110 sh** → target 1.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 59.67 USD (+95%, 43 analysts); de-biased α +8.1% vs CAPM hurdle 14.0%. Downtrend -32% vs 200-day avg; 12-1 mom +152%; RSI 32. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "TSM (TSM) — 🟢 Buy, score +0.25"
    **TRIM 80 sh** → target 2.2% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 398.63 USD (+39%, 20 analysts); de-biased α -5.0% vs CAPM hurdle 10.8%. Downtrend -1% vs 200-day avg; 12-1 mom +47%; RSI 45. Quality z +0.58 (ROE 35%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.08"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 225.91 USD (+66%, 31 analysts); de-biased α +1.3% vs CAPM hurdle 12.6%. Downtrend -20% vs 200-day avg; 12-1 mom +73%; RSI 42. Quality z +0.02 (ROE 65%).

??? note "ASML (ASML) — ⚪ Hold, score +0.07"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,494.80 USD (+40%, 16 analysts); de-biased α -5.0% vs CAPM hurdle 12.3%. Downtrend -6% vs 200-day avg; 12-1 mom +61%; RSI 42. Quality z +0.42 (ROE 50%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 152.33 USD (+53%, 26 analysts); de-biased α -1.4% vs CAPM hurdle 11.1%. Downtrend -16% vs 200-day avg; 12-1 mom +46%; RSI 45. Quality z +0.51 (ROE 87%).

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.05"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 49.88 EUR (+74%, 23 analysts); de-biased α +3.0% vs CAPM hurdle 14.1%. Downtrend -13% vs 200-day avg; 12-1 mom +50%; RSI 45. Quality z -0.04 (ROE 6%).

??? note "TER (TER) — ⚪ Hold, score -0.04"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 249.49 USD (+79%, 15 analysts); de-biased α +4.6% vs CAPM hurdle 12.3%. Downtrend -29% vs 200-day avg; 12-1 mom +92%; RSI 37. Quality z -0.31 (ROE 20%).

??? note "Advantest (6857.T) — ⚪ Hold, score -0.09"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 30,730 JPY (+39%, 21 analysts); de-biased α -5.7% vs CAPM hurdle 13.4%. Uptrend +5% vs 200-day avg; 12-1 mom +55%; RSI 44. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.19"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 694.20 EUR (+63%, 19 analysts); de-biased α +0.3% vs CAPM hurdle 13.2%. Downtrend -14% vs 200-day avg; 12-1 mom +57%; RSI 43. Quality z -0.10 (ROE 19%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 9,404 JPY (+62%, 23 analysts); de-biased α +0.5% vs CAPM hurdle 12.8%. Downtrend -9% vs 200-day avg; 12-1 mom +60%; RSI 45. Quality z -0.28 (ROE 29%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.31"
    Avoid: not owned. Analyst target 76.00 USD vs 41.44 USD (+83%, 22 analysts); de-biased α +5.7% vs CAPM hurdle 12.4%. Downtrend -24% vs 200-day avg; 12-1 mom +43%; RSI 44. Quality z -0.21 (ROE 8%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.39"
    Avoid: not owned. Analyst target 288.70 USD vs 190.42 USD (+52%, 40 analysts); de-biased α -4.1% vs CAPM hurdle 19.6%. Downtrend -18% vs 200-day avg; 12-1 mom +65%; RSI 41. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AMD (AMD) — 🔴 Sell, score -0.46"
    Avoid: not owned. Analyst target 619.51 USD vs 534.09 USD (+16%, 50 analysts); de-biased α -11.8% vs CAPM hurdle 14.9%. Uptrend +26% vs 200-day avg; 12-1 mom +117%; RSI 50. Quality z -0.15 (ROE 7%).

??? failure "ENTG (ENTG) — 🔴 Sell, score -0.46"
    Avoid: not owned. Analyst target 173.36 USD vs 147.36 USD (+18%, 11 analysts); de-biased α -10.4% vs CAPM hurdle 11.0%. Uptrend +6% vs 200-day avg; 12-1 mom +75%; RSI 51. Quality z -0.02 (ROE 6%).

??? failure "Disco (6146.T) — 🔴 Sell, score -0.53"
    Avoid: not owned. Analyst target 81,730 JPY vs 47,440 JPY (+72%, 20 analysts); de-biased α +3.3% vs CAPM hurdle 11.5%. Downtrend -27% vs 200-day avg; 12-1 mom +4%; RSI 44. Quality z +0.06 (ROE 25%).

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.67"
    Avoid: not owned. Analyst target 76.40 USD vs 36.10 USD (+112%, 10 analysts); de-biased α +12.4% vs CAPM hurdle 14.0%. Downtrend -36% vs 200-day avg; 12-1 mom +29%; RSI 42. Quality z -1.00 (ROE 9%).

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.75"
    Avoid: not owned. Analyst target 531.31 USD vs 346.62 USD (+53%, 47 analysts); de-biased α -1.4% vs CAPM hurdle 11.2%. Downtrend -5% vs 200-day avg; 12-1 mom -2%; RSI 53. Quality z +0.26 (ROE 31%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -0.80"
    Avoid: not owned. Analyst target 194.13 USD vs 172.39 USD (+13%, 30 analysts); de-biased α -11.5% vs CAPM hurdle 11.9%. Uptrend +2% vs 200-day avg; 12-1 mom +3%; RSI 49. Quality z +0.70 (ROE 23%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.04"
    Avoid: not owned. Analyst target 569.78 USD vs 455.24 USD (+25%, 26 analysts); de-biased α -8.4% vs CAPM hurdle 10.3%. Uptrend +3% vs 200-day avg; 12-1 mom +17%; RSI 49. Quality z +0.14 (ROE 7%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -1.08"
    Avoid: not owned. Analyst target 324.71 USD vs 303.68 USD (+7%, 31 analysts); de-biased α -12.6% vs CAPM hurdle 10.8%. Uptrend +16% vs 200-day avg; 12-1 mom +74%; RSI 55. Quality z +0.24 (ROE 30%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.21"
    Avoid: not owned. Analyst target 95.99 HKD vs 48.52 HKD (+98%, 21 analysts); de-biased α +10.5% vs CAPM hurdle 7.3%. Downtrend -27% vs 200-day avg; 12-1 mom -24%; RSI 45. Quality z -0.99 (ROE 3%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.30"
    Avoid: not owned. Analyst target 405.47 USD vs 323.04 USD (+26%, 26 analysts); de-biased α -8.2% vs CAPM hurdle 10.0%. Downtrend -2% vs 200-day avg; 12-1 mom +3%; RSI 48. Quality z +0.31 (ROE 22%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.33"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,676 JPY (+37%, 17 analysts); de-biased α -5.2% vs CAPM hurdle 10.8%. Downtrend -10% vs 200-day avg; 12-1 mom +31%; RSI 45. Quality z -0.20 (ROE 10%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MU | Micron Technology | 116 | 778.40 USD | $90,294 | 10.6% | Strong Buy |
| 000660.KS | SK hynix | 88 | 1,216,000 KRW | $80,149 | 9.4% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 207,000 KRW | $71,010 | 8.3% | Strong Buy |
| NVDA | NVIDIA | 337 | 162.82 USD | $54,870 | 6.4% | Strong Buy |
| TSM | TSMC | 127 | 398.63 USD | $50,626 | 5.9% | Buy |
| KLAC | KLA Corp | 268 | 152.33 USD | $40,824 | 4.8% | Hold |
| MRVL | Marvell Technology | 248 | 156.71 USD | $38,864 | 4.6% | Strong Buy |
| AMAT | Applied Materials | 84 | 370.25 USD | $31,101 | 3.6% | Buy |
| ASX | ASE Technology | 574 | 35.54 USD | $20,403 | 2.4% | Buy |
| 6857.T | Advantest | 100 | 30,730 JPY | $19,244 | 2.3% | Hold |
| LRCX | Lam Research | 58 | 225.91 USD | $13,103 | 1.5% | Hold |
| IFX.DE | Infineon Technologies | 225 | 49.88 EUR | $12,376 | 1.5% | Hold |
| INTC | Intel | 152 | 59.67 USD | $9,069 | 1.1% | Buy |
| TER | Teradyne | 35 | 249.49 USD | $8,732 | 1.0% | Hold |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-13 16:26 UTC | ADD | NVDA | 79 | 159.94 | $12,635 |
| 2026-11-13 16:26 UTC | ADD | AMAT | 23 | 357.03 | $8,212 |
| 2026-11-13 16:26 UTC | TRIM | ASX | -290 | 34.86 | $10,109 |
| 2026-11-13 00:26 UTC | TRIM | 005930.KS | -104 | 214,000.00 | $16,663 |
| 2026-11-12 18:57 UTC | ADD | NVDA | 79 | 164.84 | $13,022 |
| 2026-11-12 18:57 UTC | ADD | AMAT | 20 | 386.98 | $7,740 |
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 48.5%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
