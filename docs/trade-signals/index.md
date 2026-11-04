---
hide:
  - navigation
---

# Hourly Trade Signals — Silicon Supply Chain Model Portfolio

!!! danger "Model output, not investment advice"
    These are **rule-based signals for a paper (simulated) portfolio**, generated automatically from public, possibly delayed data. They do not account for your objectives, taxes, liquidity or risk tolerance, and they can be wrong. Nothing here is a recommendation to buy or sell securities. Consult a licensed adviser before investing.

**Last updated:** 2026-11-04 23:40 UTC (Wed Nov 04, 06:40 PM ET) · refreshes hourly · weekly model inputs as of 2026-10-02
**Markets:** NYSE/Nasdaq 🔴 closed (Wed 18:40) · Tokyo 🔴 closed (Thu 08:40) · Korea 🔴 closed (Thu 08:40) · Hong Kong 🔴 closed (Thu 07:40) · Xetra 🔴 closed (Thu 00:40) · Euronext Amsterdam 🔴 closed (Thu 00:40)

## Portfolio snapshot

| NAV | Cash | Invested | Return since inception | SOXX since inception | Regime (SOXX vs 200-day) | Equity budget |
|---|---|---|---|---|---|---|
| **$869,130** | $370,932 (43%) | $498,198 (57%) | -13.09% | -20.24% | 🔴 Risk-off (-5.6%) | 60% |

Inception 2026-09-24 08:59 UTC with $1,000,000 of paper cash. **Scaling quantities:** multiply by (your capital ÷ $869,130), then round to board lots (Tokyo 100 shares, Hong Kong/SMIC 500).

<canvas id="navChart" height="90"></canvas>

## This hour's orders

<div class="compact-table" markdown>

| Action | Name | Qty (shares) | Price (local) | Value (USD) | Status | Key drivers |
|---|---|--:|--:|--:|---|---|
| – | No trades this hour | | | | | All positions are within their rebalance bands. |

</div>

Orders execute in the paper portfolio only while the listing's home market is open, with 5 bp cost. Otherwise they are queued and re-evaluated next hour.

## Signals for all 30 names

Sorted by score. **Weight** = current → target share of NAV. **Key drivers** = the two largest contributions to the score. Full reasoning for each name is in [Rationale by name](#rationale-by-name).

<div class="compact-table" markdown>

| Rating | Score | Name | Price | Analyst upside | De-biased α | 12-1 mom | vs 200DMA | RSI | Quality z | Weight | Order | Key drivers |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| 🟢🟢 Strong Buy | +3.38 | **SK hynix**<br><small>000660.KS</small> | 1,386,000 KRW | +127% | +15.8% | +249% | -8% | 44 | +0.62 | 9.5% → 10.0% | – | analyst α +0.85 · momentum +0.41 · ⚠️ cycle-peak P/E, high σ(e) |
| 🟢🟢 Strong Buy | +2.32 | **MU**<br><small>Micron Technology</small> | 795.45 USD | +91% | +7.0% | +346% | +6% | 35 | +0.12 | 5.9% → 7.2% | – | momentum +0.53 · analyst α +0.36 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.54 | **Samsung**<br><small>005930.KS</small> | 216,250 KRW | +121% | +15.2% | +182% | -8% | 41 | -0.26 | 6.0% → 6.7% | – | analyst α +0.66 · momentum +0.23 · ⚠️ cycle-peak P/E |
| 🟢🟢 Strong Buy | +1.04 | **MRVL**<br><small>Marvell Technology</small> | 159.91 USD | +84% | +5.1% | +218% | -13% | 27 | -0.12 | 3.0% → 3.3% | – | momentum +0.35 · analyst α +0.27 · ⚠️ oversold, rich valuation |
| 🟢 Buy | +0.41 | **AMAT**<br><small>Applied Materials</small> | 369.36 USD | +73% | +3.1% | +124% | -17% | 34 | +0.03 | 2.1% → 1.7% | – | analyst α +0.15 · momentum +0.12 |
| 🟢 Buy | +0.40 | **INTC**<br><small>Intel</small> | 58.28 USD | +100% | +9.1% | +185% | -33% | 23 | -0.62 | 0.9% → 1.1% | – | analyst α +0.41 · momentum +0.26 · ⚠️ oversold, rich valuation, high σ(e) |
| ⚪ Hold | +0.20 | **Infineon**<br><small>IFX.DE</small> | 50.65 EUR | +71% | +2.1% | +90% | -12% | 41 | -0.04 | 1.5% → 1.5% | – | analyst α +0.12 · momentum +0.05 |
| ⚪ Hold | +0.17 | **ASX**<br><small>ASE Technology</small> | 37.49 USD | +36% | -3.0% | +192% | +12% | 40 | -0.68 | 1.3% → 1.3% | – | momentum +0.30 · quality -0.28 · ⚠️ rich valuation |
| ⚪ Hold | +0.13 | **TSM**<br><small>TSMC</small> | 395.62 USD | +40% | -4.9% | +60% | -1% | 36 | +0.58 | 5.8% → 5.8% | – | quality +0.28 · analyst α -0.19 |
| ⚪ Hold | +0.07 | **LRCX**<br><small>Lam Research</small> | 221.55 USD | +69% | +1.9% | +108% | -22% | 30 | +0.02 | 4.1% → 4.1% | – | trend -0.12 · analyst α +0.08 |
| ⚪ Hold | +0.06 | **Advantest**<br><small>6857.T</small> | 34,390 JPY | +24% | -9.6% | +132% | +18% | 48 | +0.33 | 5.0% → 5.0% | – | analyst α -0.48 · trend +0.21 · ⚠️ rich valuation |
| ⚪ Hold | +0.05 | **NVDA**<br><small>NVIDIA</small> | 200.29 USD | +64% | +0.1% | +16% | -2% | 35 | +0.47 | 1.4% → 1.4% | – | momentum -0.23 · quality +0.21 |
| ⚪ Hold | +0.02 | **TER**<br><small>Teradyne</small> | 251.03 USD | +78% | +4.1% | +136% | -28% | 27 | -0.31 | 1.0% → 1.0% | – | analyst α +0.23 · quality -0.21 · ⚠️ oversold |
| ⚪ Hold | -0.04 | **KLAC**<br><small>KLA Corp</small> | 149.78 USD | +56% | -1.0% | +63% | -18% | 36 | +0.51 | 4.6% → 4.6% | – | quality +0.24 · trend -0.10 |
| ⚪ Hold | -0.12 | **ASML**<br><small>ASML Holding</small> | 1,496.50 USD | +40% | -5.2% | +73% | -6% | 35 | +0.42 | 5.2% → 5.2% | – | analyst α -0.23 · quality +0.18 |
| ⚪ Hold | -0.14 | **AMD**<br><small>Advanced Micro Devices</small> | 488.85 USD | +27% | -9.4% | +150% | +18% | 40 | -0.15 | 0.0% → 0.0% | – | analyst α -0.41 · trend +0.25 |
| ⚪ Hold | -0.21 | **GFS**<br><small>GlobalFoundries</small> | 40.39 USD | +88% | +6.7% | +37% | -27% | 35 | -0.21 | 0.0% → 0.0% | – | analyst α +0.31 · momentum -0.14 |
| ⚪ Hold | -0.22 | **Tokyo Electron**<br><small>8035.T</small> | 9,584 JPY | +59% | -0.4% | +111% | -7% | 41 | -0.28 | 0.0% → 0.0% | – | quality -0.18 · momentum +0.10 |
| ⚪ Hold | -0.23 | **ASMI**<br><small>ASM.AS</small> | 683.00 EUR | +65% | +0.8% | +81% | -16% | 35 | -0.10 | 0.0% → 0.0% | – | quality -0.06 · trend -0.06 |
| ⚪ Hold | -0.25 | **Disco**<br><small>6146.T</small> | 47,110 JPY | +73% | +3.4% | +22% | -28% | 35 | +0.06 | 0.0% → 0.0% | – | momentum -0.20 · analyst α +0.19 |
| 🔴 Sell | -0.42 | **AVGO**<br><small>Broadcom</small> | 325.70 USD | +63% | +0.8% | +4% | -11% | 42 | +0.26 | 0.0% → 0.0% | – | momentum -0.35 · quality +0.11 |
| 🔴 Sell | -0.49 | **ARM**<br><small>Arm Holdings</small> | 192.34 USD | +50% | -4.7% | +79% | -16% | 33 | +0.04 | 0.0% → 0.0% | – | analyst α -0.15 · trend -0.07 · ⚠️ rich valuation, high σ(e) |
| 🔴 Sell | -0.65 | **AMKR**<br><small>Amkor Technology</small> | 35.65 USD | +114% | +12.9% | +42% | -37% | 33 | -1.00 | 0.0% → 0.0% | – | analyst α +0.55 · quality -0.43 |
| 🔴🔴 Strong Sell | -0.82 | **CDNS**<br><small>Cadence Design Systems</small> | 329.51 USD | +23% | -9.1% | +7% | +1% | 50 | +0.31 | 0.0% → 0.0% | – | analyst α -0.31 · momentum -0.30 |
| 🔴🔴 Strong Sell | -0.85 | **TXN**<br><small>Texas Instruments</small> | 311.54 USD | +4% | -13.5% | +87% | +20% | 66 | +0.24 | 0.0% → 0.0% | – | analyst α -0.85 · trend +0.32 |
| 🔴🔴 Strong Sell | -0.86 | **SNPS**<br><small>Synopsys</small> | 462.99 USD | +23% | -9.1% | +13% | +5% | 51 | +0.14 | 0.0% → 0.0% | – | analyst α -0.36 · momentum -0.26 |
| 🔴🔴 Strong Sell | -0.94 | **ENTG**<br><small>Entegris</small> | 142.87 USD | +21% | -9.7% | +83% | +3% | 45 | -0.02 | 0.0% → 0.0% | – | analyst α -0.55 · trend +0.12 |
| 🔴🔴 Strong Sell | -1.14 | **QCOM**<br><small>Qualcomm</small> | 173.73 USD | +12% | -11.9% | +2% | +3% | 48 | +0.70 | 0.0% → 0.0% | – | analyst α -0.66 · quality +0.43 |
| 🔴🔴 Strong Sell | -1.17 | **Shin-Etsu**<br><small>4063.T</small> | 5,801 JPY | +34% | -6.1% | +28% | -8% | 42 | -0.20 | 0.0% → 0.0% | – | analyst α -0.27 · momentum -0.17 |
| 🔴🔴 Strong Sell | -1.24 | **SMIC**<br><small>0981.HK</small> | 46.44 HKD | +107% | +12.5% | -23% | -31% | 37 | -0.99 | 0.0% → 0.0% | – | momentum -0.53 · analyst α +0.48 |

</div>

## Rationale by name

Click a name to expand the full reasoning behind its rating and quantity.

??? success "SK hynix (000660.KS) — 🟢🟢 Strong Buy, score +3.38"
    Within rebalance band of target 10.0%: no trade. Analyst target 3,141,025 KRW vs 1,386,000 KRW (+127%, 38 analysts); de-biased α +15.8% vs CAPM hurdle 14.3%. Downtrend -8% vs 200-day avg; 12-1 mom +249%; RSI 44. Quality z +0.62 (ROE 44%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18); high firm-specific risk σ(e) 60% → smaller size.

??? success "MU (MU) — 🟢🟢 Strong Buy, score +2.32"
    Within rebalance band of target 7.2%: no trade. Analyst target 1,520.02 USD vs 795.45 USD (+91%, 46 analysts); de-biased α +7.0% vs CAPM hurdle 14.0%. Uptrend +6% vs 200-day avg; 12-1 mom +346%; RSI 35. Quality z +0.12 (ROE 17%). ⚠️ cyclical-peak risk: fwd P/E 5.2 (ch.17-18).

??? success "Samsung (005930.KS) — 🟢🟢 Strong Buy, score +1.54"
    Within rebalance band of target 6.7%: no trade. Analyst target 477,517 KRW vs 216,250 KRW (+121%, 36 analysts); de-biased α +15.2% vs CAPM hurdle 11.3%. Downtrend -8% vs 200-day avg; 12-1 mom +182%; RSI 41. Quality z -0.26 (ROE 11%). ⚠️ cyclical-peak risk: fwd P/E 3.9 (ch.17-18).

??? success "MRVL (MRVL) — 🟢🟢 Strong Buy, score +1.04"
    Within rebalance band of target 3.3%: no trade. Analyst target 293.88 USD vs 159.91 USD (+84%, 43 analysts); de-biased α +5.1% vs CAPM hurdle 14.1%. Downtrend -13% vs 200-day avg; 12-1 mom +218%; RSI 27. Quality z -0.12 (ROE 19%). ⚠️ oversold; price implies 78% stage-1 growth (reverse DCF).

??? success "AMAT (AMAT) — 🟢 Buy, score +0.41"
    Within rebalance band of target 1.7%: no trade. Analyst target 638.94 USD vs 369.36 USD (+73%, 36 analysts); de-biased α +3.1% vs CAPM hurdle 11.6%. Downtrend -17% vs 200-day avg; 12-1 mom +124%; RSI 34. Quality z +0.03 (ROE 36%).

??? success "INTC (INTC) — 🟢 Buy, score +0.40"
    Within rebalance band of target 1.1%: no trade. Analyst target 116.37 USD vs 58.28 USD (+100%, 43 analysts); de-biased α +9.1% vs CAPM hurdle 14.0%. Downtrend -33% vs 200-day avg; 12-1 mom +185%; RSI 23. Quality z -0.62 (ROE -0%). ⚠️ oversold; price implies 86% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 63% → smaller size.

??? note "Infineon (IFX.DE) — ⚪ Hold, score +0.20"
    Hold zone: keep any existing position, no new money. Analyst target 86.74 EUR vs 50.65 EUR (+71%, 23 analysts); de-biased α +2.1% vs CAPM hurdle 14.1%. Downtrend -12% vs 200-day avg; 12-1 mom +90%; RSI 41. Quality z -0.04 (ROE 6%).

??? note "ASX (ASX) — ⚪ Hold, score +0.17"
    Hold zone: keep any existing position, no new money. Analyst target 51.00 USD vs 37.49 USD (+36%, 1 analysts); de-biased α -3.0% vs CAPM hurdle 11.9%. Uptrend +12% vs 200-day avg; 12-1 mom +192%; RSI 40. Quality z -0.68 (ROE 12%). ⚠️ price implies 69% stage-1 growth (reverse DCF).

??? note "TSM (TSM) — ⚪ Hold, score +0.13"
    Hold zone: keep any existing position, no new money. Analyst target 552.26 USD vs 395.62 USD (+40%, 20 analysts); de-biased α -4.9% vs CAPM hurdle 10.8%. Downtrend -1% vs 200-day avg; 12-1 mom +60%; RSI 36. Quality z +0.58 (ROE 35%).

??? note "LRCX (LRCX) — ⚪ Hold, score +0.07"
    Hold zone: keep any existing position, no new money. Analyst target 375.06 USD vs 221.55 USD (+69%, 31 analysts); de-biased α +1.9% vs CAPM hurdle 12.6%. Downtrend -22% vs 200-day avg; 12-1 mom +108%; RSI 30. Quality z +0.02 (ROE 65%).

??? note "Advantest (6857.T) — ⚪ Hold, score +0.06"
    Hold zone: keep any existing position, no new money. Analyst target 42,686 JPY vs 34,390 JPY (+24%, 21 analysts); de-biased α -9.6% vs CAPM hurdle 13.4%. Uptrend +18% vs 200-day avg; 12-1 mom +132%; RSI 48. Quality z +0.33 (ROE 58%). ⚠️ price implies 82% stage-1 growth (reverse DCF).

??? note "NVDA (NVDA) — ⚪ Hold, score +0.05"
    Hold zone: keep any existing position, no new money. Analyst target 327.70 USD vs 200.29 USD (+64%, 59 analysts); de-biased α +0.1% vs CAPM hurdle 13.9%. Downtrend -2% vs 200-day avg; 12-1 mom +16%; RSI 35. Quality z +0.47 (ROE 101%).

??? note "TER (TER) — ⚪ Hold, score +0.02"
    Hold zone: keep any existing position, no new money. Analyst target 446.47 USD vs 251.03 USD (+78%, 15 analysts); de-biased α +4.1% vs CAPM hurdle 12.3%. Downtrend -28% vs 200-day avg; 12-1 mom +136%; RSI 27. Quality z -0.31 (ROE 20%). ⚠️ oversold.

??? note "KLAC (KLAC) — ⚪ Hold, score -0.04"
    Hold zone: keep any existing position, no new money. Analyst target 233.77 USD vs 149.78 USD (+56%, 26 analysts); de-biased α -1.0% vs CAPM hurdle 11.1%. Downtrend -18% vs 200-day avg; 12-1 mom +63%; RSI 36. Quality z +0.51 (ROE 87%).

??? note "ASML (ASML) — ⚪ Hold, score -0.12"
    Hold zone: keep any existing position, no new money. Analyst target 2,096.77 USD vs 1,496.50 USD (+40%, 16 analysts); de-biased α -5.2% vs CAPM hurdle 12.3%. Downtrend -6% vs 200-day avg; 12-1 mom +73%; RSI 35. Quality z +0.42 (ROE 50%).

??? note "AMD (AMD) — ⚪ Hold, score -0.14"
    Hold zone: not owned, no entry. Analyst target 619.51 USD vs 488.85 USD (+27%, 50 analysts); de-biased α -9.4% vs CAPM hurdle 14.9%. Uptrend +18% vs 200-day avg; 12-1 mom +150%; RSI 40. Quality z -0.15 (ROE 7%).

??? note "GFS (GFS) — ⚪ Hold, score -0.21"
    Hold zone: not owned, no entry. Analyst target 76.00 USD vs 40.39 USD (+88%, 22 analysts); de-biased α +6.7% vs CAPM hurdle 12.4%. Downtrend -27% vs 200-day avg; 12-1 mom +37%; RSI 35. Quality z -0.21 (ROE 8%).

??? note "Tokyo Electron (8035.T) — ⚪ Hold, score -0.22"
    Hold zone: not owned, no entry. Analyst target 15,275 JPY vs 9,584 JPY (+59%, 23 analysts); de-biased α -0.4% vs CAPM hurdle 12.8%. Downtrend -7% vs 200-day avg; 12-1 mom +111%; RSI 41. Quality z -0.28 (ROE 29%).

??? note "ASMI (ASM.AS) — ⚪ Hold, score -0.23"
    Hold zone: not owned, no entry. Analyst target 1,128.53 EUR vs 683.00 EUR (+65%, 19 analysts); de-biased α +0.8% vs CAPM hurdle 13.2%. Downtrend -16% vs 200-day avg; 12-1 mom +81%; RSI 35. Quality z -0.10 (ROE 19%).

??? note "Disco (6146.T) — ⚪ Hold, score -0.25"
    Hold zone: not owned, no entry. Analyst target 81,730 JPY vs 47,110 JPY (+73%, 20 analysts); de-biased α +3.4% vs CAPM hurdle 11.5%. Downtrend -28% vs 200-day avg; 12-1 mom +22%; RSI 35. Quality z +0.06 (ROE 25%).

??? failure "AVGO (AVGO) — 🔴 Sell, score -0.42"
    Avoid: not owned. Analyst target 531.31 USD vs 325.70 USD (+63%, 47 analysts); de-biased α +0.8% vs CAPM hurdle 11.2%. Downtrend -11% vs 200-day avg; 12-1 mom +4%; RSI 42. Quality z +0.26 (ROE 31%).

??? failure "ARM (ARM) — 🔴 Sell, score -0.49"
    Avoid: not owned. Analyst target 288.70 USD vs 192.34 USD (+50%, 40 analysts); de-biased α -4.7% vs CAPM hurdle 19.6%. Downtrend -16% vs 200-day avg; 12-1 mom +79%; RSI 33. Quality z +0.04 (ROE 12%). ⚠️ price implies 113% stage-1 growth (reverse DCF); high firm-specific risk σ(e) 78% → smaller size.

??? failure "AMKR (AMKR) — 🔴 Sell, score -0.65"
    Avoid: not owned. Analyst target 76.40 USD vs 35.65 USD (+114%, 10 analysts); de-biased α +12.9% vs CAPM hurdle 14.0%. Downtrend -37% vs 200-day avg; 12-1 mom +42%; RSI 33. Quality z -1.00 (ROE 9%).

??? failure "CDNS (CDNS) — 🔴🔴 Strong Sell, score -0.82"
    Avoid: not owned. Analyst target 405.47 USD vs 329.51 USD (+23%, 26 analysts); de-biased α -9.1% vs CAPM hurdle 10.0%. Uptrend +1% vs 200-day avg; 12-1 mom +7%; RSI 50. Quality z +0.31 (ROE 22%).

??? failure "TXN (TXN) — 🔴🔴 Strong Sell, score -0.85"
    Avoid: not owned. Analyst target 324.71 USD vs 311.54 USD (+4%, 31 analysts); de-biased α -13.5% vs CAPM hurdle 10.8%. Uptrend +20% vs 200-day avg; 12-1 mom +87%; RSI 66. Quality z +0.24 (ROE 30%).

??? failure "SNPS (SNPS) — 🔴🔴 Strong Sell, score -0.86"
    Avoid: not owned. Analyst target 569.78 USD vs 462.99 USD (+23%, 26 analysts); de-biased α -9.1% vs CAPM hurdle 10.3%. Uptrend +5% vs 200-day avg; 12-1 mom +13%; RSI 51. Quality z +0.14 (ROE 7%).

??? failure "ENTG (ENTG) — 🔴🔴 Strong Sell, score -0.94"
    Avoid: not owned. Analyst target 173.36 USD vs 142.87 USD (+21%, 11 analysts); de-biased α -9.7% vs CAPM hurdle 11.0%. Uptrend +3% vs 200-day avg; 12-1 mom +83%; RSI 45. Quality z -0.02 (ROE 6%).

??? failure "QCOM (QCOM) — 🔴🔴 Strong Sell, score -1.14"
    Avoid: not owned. Analyst target 194.13 USD vs 173.73 USD (+12%, 30 analysts); de-biased α -11.9% vs CAPM hurdle 11.9%. Uptrend +3% vs 200-day avg; 12-1 mom +2%; RSI 48. Quality z +0.70 (ROE 23%).

??? failure "Shin-Etsu (4063.T) — 🔴🔴 Strong Sell, score -1.17"
    Avoid: not owned. Analyst target 7,763 JPY vs 5,801 JPY (+34%, 17 analysts); de-biased α -6.1% vs CAPM hurdle 10.8%. Downtrend -8% vs 200-day avg; 12-1 mom +28%; RSI 42. Quality z -0.20 (ROE 10%).

??? failure "SMIC (0981.HK) — 🔴🔴 Strong Sell, score -1.24"
    Avoid: not owned. Analyst target 95.99 HKD vs 46.44 HKD (+107%, 21 analysts); de-biased α +12.5% vs CAPM hurdle 7.3%. Downtrend -31% vs 200-day avg; 12-1 mom -23%; RSI 37. Quality z -0.99 (ROE 3%).

## Current holdings

| Ticker | Company | Shares | Price | Value (USD) | Weight | Rating |
|---|---|---|---|---|---|---|
| 000660.KS | SK hynix | 80 | 1,386,000 KRW | $82,714 | 9.5% | Strong Buy |
| 005930.KS | Samsung Electronics | 322 | 216,250 KRW | $51,944 | 6.0% | Strong Buy |
| MU | Micron Technology | 64 | 795.45 USD | $50,909 | 5.9% | Strong Buy |
| TSM | TSMC | 127 | 395.62 USD | $50,244 | 5.8% | Hold |
| ASML | ASML Holding | 30 | 1,496.50 USD | $44,895 | 5.2% | Hold |
| 6857.T | Advantest | 200 | 34,390 JPY | $43,420 | 5.0% | Hold |
| KLAC | KLA Corp | 268 | 149.78 USD | $40,141 | 4.6% | Hold |
| LRCX | Lam Research | 162 | 221.55 USD | $35,891 | 4.1% | Hold |
| MRVL | Marvell Technology | 164 | 159.91 USD | $26,225 | 3.0% | Strong Buy |
| AMAT | Applied Materials | 50 | 369.36 USD | $18,468 | 2.1% | Buy |
| IFX.DE | Infineon Technologies | 225 | 50.65 EUR | $12,805 | 1.5% | Hold |
| NVDA | NVIDIA | 60 | 200.29 USD | $12,017 | 1.4% | Hold |
| ASX | ASE Technology | 312 | 37.49 USD | $11,697 | 1.3% | Hold |
| TER | Teradyne | 35 | 251.03 USD | $8,786 | 1.0% | Hold |
| INTC | Intel | 138 | 58.28 USD | $8,043 | 0.9% | Buy |

## Recent paper trades

| Time | Action | Ticker | Qty | Price (local) | Value (USD) |
|---|---|---|---|---|---|
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
| 2026-10-30 19:24 UTC | TRIM | MRVL | -139 | 193.20 | $26,855 |
| 2026-10-30 19:24 UTC | TRIM | INTC | -391 | 63.40 | $24,787 |
| 2026-10-30 19:24 UTC | TRIM | ASX | -1,008 | 38.89 | $39,201 |
| 2026-10-30 14:10 UTC | BUY (new) | INTC | 521 | 65.38 | $34,063 |
| 2026-10-30 14:10 UTC | TRIM | AMAT | -33 | 399.62 | $13,187 |
| 2026-10-29 14:21 UTC | BUY (new) | MRVL | 218 | 219.82 | $47,921 |
| 2026-10-29 14:21 UTC | TRIM | NVDA | -84 | 213.56 | $17,939 |
| 2026-10-29 14:21 UTC | SELL (exit) | AVGO | -100 | 342.58 | $34,258 |
| 2026-10-28 16:04 UTC | ADD | NVDA | 117 | 217.19 | $25,411 |
| 2026-10-26 19:22 UTC | TRIM | AMAT | -57 | 391.16 | $22,296 |
| 2026-10-26 19:22 UTC | TRIM | NVDA | -58 | 216.65 | $12,566 |

## How the signals are built

1. **Expected return vs hurdle (ch.9, 27).** Analyst-implied return $E(r) = \text{target}/P - 1 + \text{dividend yield}$ at the live price. The CAPM hurdle is $k = r_f + \beta_{adj} \times MRP$ ($r_f$ = 3.99%, MRP = 5.5%, Blume-adjusted β). The raw α is $E(r) - k$. The cross-sectional mean (the Street's average optimism, currently 49.3%) is subtracted, and the remainder is shrunk ×0.25 (×half again if fewer than 5 analysts).
2. **Momentum & trend (ch.11–12).** 12-1-month momentum and price vs the 200-day average (z-scored), plus a −0.25 penalty when RSI(14) > 75.
3. **Quality (ch.19).** Weekly quality z-score: EBIT margin, ROE, FCF conversion and low accruals.
4. **Score** = cross-sectionally standardized $(0.4\,z_\alpha + 0.25\,z_{mom} + 0.2\,z_{quality} + 0.15\,z_{trend})$, where each $z$ is a rank-based normal score (robust to outliers). The score is therefore relative to the other 29 names. Ratings: Strong Buy ≥ 0.75, Buy ≥ 0.25, Hold, Sell ≤ -0.25, Strong Sell ≤ -0.75.
5. **Sizing (ch.8, 27).** Buy-rated names get $w_i \propto \text{score}_i / \sigma(e_i)$. This is Treynor-Black $\alpha/\sigma^2(e)$ with Grinold's $\alpha = IC \cdot \sigma \cdot z$. Caps: 10% per name and 35% per segment. Hold-rated positions are kept (capped). Sell-rated positions are exited.
6. **Capital allocation (ch.6).** Total equity is 90% of NAV when SOXX is above its 200-day average and 60% when below. The rest is held in cash (T-bills).
7. **Trading discipline.** Positions trade only when they drift more than max(0.5% of NAV, 20% of target), which limits hourly churn and costs.

**Limitations:** data may be delayed 15+ minutes; analyst targets and fundamentals refresh weekly; exchange holidays outside the US are inferred from data; no slippage model beyond the flat cost; backtest-free, rule-based model. See the [full analysis](../silicon-supply-chain/index.md) for the underlying research.
