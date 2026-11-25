---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-25 23:37 UTC (Wed Nov 25, 06:37 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Wed 18:37) · Tokyo 🔴 closed (Thu 08:37) · Korea 🔴 closed (Thu 08:37) · Hong Kong 🔴 closed (Thu 07:37) · Xetra 🔴 closed (Thu 00:37) · Euronext Amsterdam 🔴 closed (Thu 00:37)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$766,034** | $311,602 (41%) | $454,432 (59%) | -23.40% | -77.37% | 🔴 Risk-off (-20.6%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $766,034), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| BUY (new) | **NVDA**<br><small>NVIDIA</small> | 452 | 149.29 USD | $67,479 | Queued · NYSE/Nasdaq closed | analyst α +0.55 · quality +0.21 |
| TRIM | **TSM**<br><small>TSMC</small> | 83 | 342.31 USD | $28,412 | Queued · NYSE/Nasdaq closed | quality +0.28 · analyst α -0.23 |
| TRIM | **AMAT**<br><small>Applied Materials</small> | 54 | 310.61 USD | $16,773 | Queued · NYSE/Nasdaq closed | analyst α +0.23 · momentum +0.10 |
| ADD | **Infineon**<br><small>IFX.DE</small> | 372 | 40.72 EUR | $16,630 | Queued · Xetra closed | analyst α +0.36 · momentum -0.05 |
| TRIM | **INTC**<br><small>Intel</small> | 304 | 54.44 USD | $16,550 | Queued · NYSE/Nasdaq closed | analyst α +0.41 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| TRIM | **ASX**<br><small>ASE Technology</small> | 559 | 29.48 USD | $16,477 | Queued · NYSE/Nasdaq closed | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +2.49 | **MRVL**<br><small>Marvell Technology</small> | 130.90 USD | +125% | +10.4% | +191% | -31% | 35 | -0.12 | 10.3% → 8.6% | – | analyst α +0.66 · momentum +0.35 · ⚠️ rich valuation |
| 🟢🟢 Strong Buy | +1.89 | **MU**<br><small>Micron Technology</small> | 604.16 USD | – | +0.0% | +315% | -22% | 36 | +0.12 | 5.0% → 6.3% | – | momentum +0.53 · quality +0.06 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.65 | **NVDA**<br><small>NVIDIA</small> | 149.29 USD | +120% | +9.2% | +20% | -26% | 37 | +0.47 | 0.0% → 8.8% | BUY 452 | analyst α +0.55 · quality +0.21 |
| 🟢🟢 Strong Buy | +1.56 | **SK hynix**<br><small>000660.KS</small> | 1,035,000 KRW | – | +0.0% | +166% | -32% | 36 | +0.62 | 4.1% → 5.0% | – | quality +0.33 · momentum +0.30 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +0.82 | **AMAT**<br><small>Applied Materials</small> | 310.61 USD | +106% | +6.3% | +72% | -30% | 37 | +0.03 | 5.9% → 3.7% | TRIM 54 | analyst α +0.23 · momentum +0.10 |
| 🟢 Buy | +0.67 | **INTC**<br><small>Intel</small> | 54.44 USD | +114% | +7.7% | +162% | -38% | 36 | -0.62 | 4.2% → 2.1% | TRIM 304 | analyst α +0.41 · momentum +0.26 · ⚠️ rich valuation, high σ(e) |
| 🟢 Buy | +0.66 | **Infineon**<br><small>IFX.DE</small> | 40.72 EUR | +113% | +7.6% | +52% | -29% | 32 | -0.04 | 1.3% → 3.5% | ADD 372 | analyst α +0.36 · momentum -0.05 |
| 🟢 Buy | +0.42 | **Advantest**<br><small>6857.T</small> | 23,715 JPY | +80% | -0.6% | +57% | -19% | 36 | +0.33 | 1.9% → 1.5% | – | quality +0.16 · analyst α -0.05 · ⚠️ rich valuation |
| 🟢 Buy | +0.35 | **ASX**<br><small>ASE Technology</small> | 29.48 USD | +73% | -0.9% | +200% | -14% | 40 | -0.68 | 3.9% → 1.7% | TRIM 559 | momentum +0.41 · quality -0.28 · ⚠️ rich valuation |
| 🟢 Buy | +0.30 | **TSM**<br><small>TSMC</small> | 342.31 USD | +61% | -4.4% | +55% | -15% | 39 | +0.58 | 5.7% → 1.9% | TRIM 83 | quality +0.28 · analyst α -0.23 |
| ⚪ Hold | +0.07 | **Samsung**<br><small>005930.KS</small> | 171,200 KRW | – | +0.0% | +155% | -28% | 34 | -0.26 | 7.6% → 7.6% | – | momentum +0.20 · quality -0.16 · ⚠️ cycle-peak P/E |
| ⚪ Hold | +0.07 | **AMD**<br><small>Advanced Micro Devices</small> | 406.83 USD | +52% | -7.9% | +161% | -6% | 38 | -0.15 | 0.0% → 0.0% | – | analyst α -0.31 · momentum +0.23 |
| ⚪ Hold | +0.06 | **LRCX**<br><small>Lam Research</small> | 184.93 USD | +103% | +5.4% | +61% | -35% | 36 | +0.02 | 3.3% → 3.3% | – | trend -0.16 · analyst α +0.15 |
| ⚪ Hold | +0.06 | **ASML**<br><small>ASML Holding</small> | 1,303.10 USD | +61% | -5.0% | +67% | -18% | 36 | +0.42 | 0.0% → 0.0% | – | analyst α -0.27 · quality +0.18 |
| ⚪ Hold | +0.05 | **ASMI**<br><small>ASM.AS</small> | 593.40 EUR | +90% | +2.1% | +57% | -27% | 36 | -0.10 | 0.0% → 0.0% | – | analyst α +0.08 · quality -0.06 |
| ⚪ Hold | +0.05 | **KLAC**<br><small>KLA Corp</small> | 134.08 USD | +74% | -1.4% | +36% | -26% | 41 | +0.51 | 2.6% → 2.6% | – | quality +0.24 · analyst α -0.15 |
| ⚪ Hold | +0.01 | **TER**<br><small>Teradyne</small> | 212.24 USD | +110% | +7.3% | +95% | -39% | 36 | -0.31 | 3.4% → 3.4% | – | analyst α +0.31 · trend -0.25 |
| ⚪ Hold | -0.18 | **AMKR**<br><small>Amkor Technology</small> | 32.00 USD | +139% | +14.1% | +21% | -43% | 40 | -1.00 | 0.0% → 0.0% | – | analyst α +0.85 · quality -0.43 |
| 🔴 Sell | -0.35 | **GFS**<br><small>GlobalFoundries</small> | 36.21 USD | +110% | +7.2% | +35% | -34% | 38 | -0.21 | 0.0% → 0.0% | – | analyst α +0.27 · trend -0.14 |
| 🔴 Sell | -0.37 | **TXN**<br><small>Texas Instruments</small> | 269.92 USD | +20% | -14.4% | +95% | +2% | 44 | +0.24 | 0.0% → 0.0% | – | analyst α -0.66 · trend +0.32 |
| 🔴 Sell | -0.41 | **Tokyo Electron**<br><small>8035.T</small> | 7,818 JPY | +95% | +3.7% | +35% | -25% | 36 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · analyst α +0.12 |
| 🔴 Sell | -0.57 | **ARM**<br><small>Arm Holdings</small> | 161.49 USD | +79% | -2.5% | +68% | -31% | 38 | +0.04 | 0.0% → 0.0% | – | analyst α -0.19 · trend -0.10 · ⚠️ rich valuation, high σ(e) |
| 🔴🔴 Strong Sell | -0.75 | **ENTG**<br><small>Entegris</small> | 128.08 USD | +35% | -11.1% | +103% | -9% | 43 | -0.02 | 0.0% → 0.0% | – | analyst α -0.55 · momentum +0.17 |
| 🔴🔴 Strong Sell | -0.86 | **Disco**<br><small>6146.T</small> | 40,590 JPY | +101% | +5.4% | -1% | -37% | 37 | +0.06 | 0.0% → 0.0% | – | momentum -0.35 · analyst α +0.19 |
| 🔴🔴 Strong Sell | -0.91 | **AVGO**<br><small>Broadcom</small> | 300.49 USD | +77% | -0.7% | -9% | -18% | 41 | +0.26 | 0.0% → 0.0% | – | momentum -0.41 · quality +0.11 |
| 🔴🔴 Strong Sell | -1.14 | **SNPS**<br><small>Synopsys</small> | 405.08 USD | +41% | -9.7% | +17% | -8% | 38 | +0.14 | 0.0% → 0.0% | – | analyst α -0.41 · momentum -0.23 |
| 🔴🔴 Strong Sell | -1.30 | **QCOM**<br><small>Qualcomm</small> | 168.61 USD | +15% | -16.0% | +14% | -1% | 50 | +0.70 | 0.0% → 0.0% | – | analyst α -0.85 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.35 | **SMIC**<br><small>0981.HK</small> | 45.30 HKD | +112% | +8.9% | -38% | -30% | 39 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.48 |
| 🔴🔴 Strong Sell | -1.48 | **Shin-Etsu**<br><small>4063.T</small> | 5,513 JPY | +41% | -9.3% | +28% | -13% | 44 | -0.20 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.14 |
| 🔴🔴 Strong Sell | -1.49 | **CDNS**<br><small>Cadence Design Systems</small> | 294.79 USD | +38% | -10.4% | +13% | -10% | 41 | +0.31 | 0.0% → 0.0% | – | analyst α -0.48 · momentum -0.30 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +2.49"
    Within rebalance band of target 8.6%: no trade. Analyst target 293.88 USD vs 130.90 USD (+125%, 43 analysts); de-biased α +10.4% vs CAPM hurdle 14.1%. Downtrend -31% vs 200-day avg; 12-1 mom +191%; RSI 35. Quality z -0.12 (ROE 19%). ⚠️ price implies 78% stage-1 growth (reverse DCF).

??? success "MU (MU) — 🟢🟢 Strong Buy, score +1.89"
    Within rebalance band of target 6.3%: no trade. No reliable analyst target: α set to 0. Downtrend -22% vs 200-day avg; 12-1 mom +315%; RSI 36. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "NVDA (NVDA) — 🟢🟢 Strong Buy, score +1.65"
    **BUY (new) 452 sh** → target 8.8% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 327.70 USD vs 149.29 USD (+120%, 59 analysts); de-biased α +9.2% vs CAPM hurdle 13.9%. Downtrend -26% vs 200-day avg; 12-1 mom +20%; RSI 37. Quality z +0.47 (ROE 101%).

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +1.56"
    Within rebalance band of target 5.0%: no trade. No reliable analyst target: α set to 0. Downtrend -32% vs 200-day avg; 12-1 mom +166%; RSI 36. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "AMAT (AMAT) — 🟢🟢 Strong Buy, score +0.82"
    **TRIM 54 sh** → target 3.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 638.94 USD vs 310.61 USD (+106%, 36 analysts); de-biased α +6.3% vs CAPM hurdle 11.6%. Downtrend -30% vs 200-day avg; 12-1 mom +72%; RSI 37. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.67"
    **TRIM 304 sh** → target 2.1% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 116.37 USD vs 54.44 USD (+114%, 43 analysts); de-biased α +7.7% vs CAPM hurdle 14.0%. Downtrend -38% vs 200-day avg; 12-1 mom +162%; RSI 36. Quality z -0.62 (ROE -0%). ⚠️ price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? success "Infineon (IFX.DE) — 🟢 Buy, score +0.66"
    **ADD 372 sh** → target 3.5% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 86.74 EUR vs 40.72 EUR (+113%, 23 analysts); de-biased α +7.6% vs CAPM hurdle 14.1%. Downtrend -29% vs 200-day avg; 12-1 mom +52%; RSI 32. Quality z -0.04 (ROE 6%).

??? success "Advantest (6857.T) — 🟢 Buy, score +0.42"
    Within rebalance band of target 1.5%: no trade. Analyst target 42,686 JPY vs 23,715 JPY (+80%, 21 analysts); de-biased α -0.6% vs CAPM hurdle 13.4%. Downtrend -19% vs 200-day avg; 12-1 mom +57%; RSI 36. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? success "ASX (ASX) — 🟢 Buy, score +0.35"
    **TRIM 559 sh** → target 1.7% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 51.00 USD vs 29.48 USD (+73%, 1 analysts); de-biased α -0.9% vs CAPM hurdle 11.9%. Downtrend -14% vs 200-day avg; 12-1 mom +200%; RSI 40. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? success "TSM (TSM) — 🟢 Buy, score +0.30"
    **TRIM 83 sh** → target 1.9% of NAV (sized ∝ score ÷ σ(e), cap 10%). Analyst target 552.26 USD vs 342.31 USD (+61%, 20 analysts); de-biased α -4.4% vs CAPM hurdle 10.8%. Downtrend -15% vs 200-day avg; 12-1 mom +55%; RSI 39. Quality z +0.58 (ROE 35%).

??? note "Samsung (005930.KS) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. No reliable analyst target: α set to 0. Downtrend -28% vs 200-day avg; 12-1 mom +155%; RSI 34. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? note "AMD (AMD) — ⚪ Hold, score +0.07"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 406.83 USD (+52%, 50 analysts); de-biased α -7.9% vs CAPM hurdle 14.9%. Downtrend -6% vs 200-day avg; 12-1 mom +161%; RSI 38. Quality z -0.15 (ROE 7%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 184.93 USD (+103%, 31 analysts); de-biased α +5.4% vs CAPM hurdle 12.6%. Downtrend -35% vs 200-day avg; 12-1 mom +61%; RSI 36. Quality z +0.02 (ROE 65%).

??? note "ASML (ASML) — ⚪ Hold, score +0.06"
    Hold zone: not owned, no entry. Analyst target 2,096.77 USD vs 1,303.10 USD (+61%, 16 analysts); de-biased α -5.0% vs CAPM hurdle 12.3%. Downtrend -18% vs 200-day avg; 12-1 mom +67%; RSI 36. Quality z +0.42 (ROE 50%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score +0.05"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 593.40 EUR (+90%, 19 analysts); de-biased α +2.1% vs CAPM hurdle 13.2%. Downtrend -27% vs 200-day avg; 12-1 mom +57%; RSI 36. Quality z -0.10 (ROE 19%).

??? note "KLAC (KLAC) — ⚪ Hold, score +0.05"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 134.08 USD (+74%, 26 analysts); de-biased α -1.4% vs CAPM hurdle 11.1%. Downtrend -26% vs 200-day avg; 12-1 mom +36%; RSI 41. Quality z +0.51 (ROE 87%).

??? note "TER (TER) — ⚪ Hold, score +0.01"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 212.24 USD (+110%, 15 analysts); de-biased α +7.3% vs CAPM hurdle 12.3%. Downtrend -39% vs 200-day avg; 12-1 mom +95%; RSI 36. Quality z -0.31 (ROE 20%).

??? note "AMKR (AMKR) — ⚪ Hold, score -0.18"
    Hold zone: not owned, no entry. Analyst target 76.40 USD vs 32.00 USD (+139%, 10 analysts); de-biased α +14.1% vs CAPM hurdle 14.0%. Downtrend -43% vs 200-day avg; 12-1 mom +21%; RSI 40. Quality z -1.00 (ROE 9%).

??? failure "GFS (GFS) — 🔴 Sell, score -0.35"
    Avoid: not owned. Analyst target 76.00 USD vs 36.21 USD (+110%, 22 analysts); de-biased α +7.2% vs CAPM hurdle 12.4%. Downtrend -34% vs 200-day avg; 12-1 mom +35%; RSI 38. Quality z -0.21 (ROE 8%).

??? failure "TXN (TXN) — 🔴 Sell, score -0.37"
    Avoid: not owned. Analyst target 324.71 USD vs 269.92 USD (+20%, 31 analysts); de-biased α -14.4% vs CAPM hurdle 10.8%. Uptrend +2% vs 200-day avg; 12-1 mom +95%; RSI 44. Quality z +0.24 (ROE 30%).

??? failure "Tokyo Electron (8035.T) — 🔴 Sell, score -0.41"
    Avoid: not owned. Analyst target 15,275 JPY vs 7,818 JPY (+95%, 23 analysts); de-biased α +3.7% vs CAPM hurdle 12.8%. Downtrend -25% vs 200-day avg; 12-1 mom +35%; RSI 36. Quality z -0.28 (ROE 29%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.57"
    Avoid: not owned. Analyst target 288.70 USD vs 161.49 USD (+79%, 40 analysts); de-biased α -2.5% vs CAPM hurdle 19.6%. Downtrend -31% vs 200-day avg; 12-1 mom +68%; RSI 38. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.75"
    Avoid: not owned. Analyst target 173.36 USD vs 128.08 USD (+35%, 11 analysts); de-biased α -11.1% vs CAPM hurdle 11.0%. Downtrend -9% vs 200-day avg; 12-1 mom +103%; RSI 43. Quality z -0.02 (ROE 6%).

??? failure "Disco (6146.T) — 🔴🔴 Strong Sell, score -0.86"
    Avoid: not owned. Analyst target 81,730 JPY vs 40,590 JPY (+101%, 20 analysts); de-biased α +5.4% vs CAPM hurdle 11.5%. Downtrend -37% vs 200-day avg; 12-1 mom -1%; RSI 37. Quality z +0.06 (ROE 25%).

??? failure "AVGO (AVGO) — 🔴🔴 Strong Sell, score -0.91"
    Avoid: not owned. Analyst target 531.31 USD vs 300.49 USD (+77%, 47 analysts); de-biased α -0.7% vs CAPM hurdle 11.2%. Downtrend -18% vs 200-day avg; 12-1 mom -9%; RSI 41. Quality z +0.26 (ROE 31%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -1.14"
    Avoid: not owned. Analyst target 569.78 USD vs 405.08 USD (+41%, 26 analysts); de-biased α -9.7% vs CAPM hurdle 10.3%. Downtrend -8% vs 200-day avg; 12-1 mom +17%; RSI 38. Quality z +0.14 (ROE 7%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.30"
    Avoid: not owned. Analyst target 194.13 USD vs 168.61 USD (+15%, 30 analysts); de-biased α -16.0% vs CAPM hurdle 11.9%. Downtrend -1% vs 200-day avg; 12-1 mom +14%; RSI 50. Quality z +0.70 (ROE 23%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.35"
    Avoid: not owned. Analyst target 95.99 HKD vs 45.30 HKD (+112%, 21 analysts); de-biased α +8.9% vs CAPM hurdle 7.3%. Downtrend -30% vs 200-day avg; 12-1 mom -38%; RSI 39. Quality z -0.99 (ROE 3%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.48"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,513 JPY (+41%, 17 analysts); de-biased α -9.3% vs CAPM hurdle 10.8%. Downtrend -13% vs 200-day avg; 12-1 mom +28%; RSI 44. Quality z -0.20 (ROE 10%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -1.49"
    Avoid: not owned. Analyst target 405.47 USD vs 294.79 USD (+38%, 26 analysts); de-biased α -10.4% vs CAPM hurdle 10.0%. Downtrend -10% vs 200-day avg; 12-1 mom +13%; RSI 41. Quality z +0.31 (ROE 22%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| MRVL | Marvell Technology | 601 | 130.90 USD | $78,671 | 10.3% | Strong Buy |
| 005930.KS | Samsung Electronics | 458 | 171,200 KRW | $58,344 | 7.6% | Hold |
| AMAT | Applied Materials | 146 | 310.61 USD | $45,349 | 5.9% | Strong Buy |
| TSM | TSMC | 127 | 342.31 USD | $43,473 | 5.7% | Buy |
| MU | Micron Technology | 64 | 604.16 USD | $38,666 | 5.0% | Strong Buy |
| INTC | Intel | 595 | 54.44 USD | $32,392 | 4.2% | Buy |
| 000660.KS | SK hynix | 41 | 1,035,000 KRW | $31,576 | 4.1% | Strong Buy |
| ASX | ASE Technology | 1,010 | 29.48 USD | $29,770 | 3.9% | Buy |
| TER | Teradyne | 123 | 212.24 USD | $26,106 | 3.4% | Hold |
| LRCX | Lam Research | 136 | 184.93 USD | $25,150 | 3.3% | Hold |
| KLAC | KLA Corp | 150 | 134.08 USD | $20,112 | 2.6% | Hold |
| 6857.T | Advantest | 100 | 23,715 JPY | $14,897 | 1.9% | Buy |
| IFX.DE | Infineon Technologies | 222 | 40.72 EUR | $9,924 | 1.3% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
| 2026-11-23 12:44 UTC | TRIM | IFX.DE | -147 | 47.12 | $7,589 |
| 2026-11-20 20:22 UTC | ADD | INTC | 365 | 52.70 | $19,236 |
| 2026-11-20 20:22 UTC | ADD | MRVL | 353 | 123.14 | $43,470 |
| 2026-11-20 20:22 UTC | ADD | ASX | 205 | 26.54 | $5,441 |
| 2026-11-20 20:22 UTC | ADD | TER | 88 | 204.82 | $18,024 |
| 2026-11-20 20:22 UTC | ADD | LRCX | 78 | 183.03 | $14,277 |
| 2026-11-20 20:22 UTC | ADD | AMAT | 62 | 303.82 | $18,837 |
| 2026-11-20 20:22 UTC | TRIM | MU | -52 | 596.09 | $30,997 |
| 2026-11-20 20:22 UTC | TRIM | KLAC | -118 | 126.94 | $14,979 |
| 2026-11-20 20:22 UTC | SELL (exit) | NVDA | -268 | 128.30 | $34,384 |
| 2026-11-20 11:54 UTC | ADD | IFX.DE | 144 | 46.65 | $7,364 |
| 2026-11-17 03:55 UTC | TRIM | 000660.KS | -47 | 1,144,000.00 | $40,195 |
| 2026-11-16 20:30 UTC | ADD | ASX | 231 | 32.86 | $7,591 |
| 2026-11-16 20:30 UTC | ADD | INTC | 78 | 55.61 | $4,338 |
| 2026-11-16 20:30 UTC | TRIM | NVDA | -69 | 155.52 | $10,731 |
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

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 69.1%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
