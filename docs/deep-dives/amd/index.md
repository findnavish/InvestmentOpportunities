# Advanced Micro Devices (AMD) — Deep Dive

*Prices as of the **Mon 05 Oct 2026** close · data pulled 2026-10-06 07:01:00+00:00 · refreshed weekly · [methodology](../../methodology.md)*

!!! warning "Not investment advice"
    Educational analysis built from public data (Yahoo Finance, Kenneth French Data Library) and explicit model assumptions. Numbers update automatically; the qualitative notes are dated.

!!! abstract "Verdict: Hold (great business, price already discounts it) — 5/8 checks pass"

    Advanced Micro Devices is a high-quality, net-cash franchise with accelerating revenue (consensus FY2026 revenue 50.9bn, FY2027 88.9bn), but at USD 631.75 the market already prices in **52% a year revenue growth after FY2027** (fading to 4%) at a 28% owner-FCF margin, or a **65% margin** on the base growth path. The base-case DCF is USD 280 (-56%).
    Our hourly signal model currently rates it **🔴 Sell** (score -0.36).

| Check | Pass | Evidence |
|---|:---:|---|
| Valuation: base-case DCF at or above price | ❌ | base DCF USD 280 vs price USD 632 |
| Relative value: forward P/E at most 1.2x the Top-30 median | ❌ | 40.2x FY2027E vs median 28.4x |
| Street: de-biased, shrunk analyst alpha > 0 (ch27) | ❌ | -7.0% |
| Momentum: 12-1 month return > 0 (ch11) | ✅ | +169% |
| Trend: price above 200-day MA (ch12) | ✅ | +68% vs 200DMA |
| Not overbought: RSI(14) below 70 | ✅ | RSI 69 |
| Fundamentals: revenue growing and FCF positive | ✅ | TTM FCF 8.4bn |
| Balance sheet: net cash | ✅ | net cash 8.8bn |

## Snapshot

| Metric | Value | Metric | Value |
|---|---|---|---|
| Price | USD 631.75 | Market cap | USD 1,031.3bn |
| Enterprise value | USD 1,022.5bn | Net cash | USD 8.8bn |
| 52-week range | 164.67 – 633.91 | From 52w high | -0.3% |
| Trailing P/E (GAAP) | 161.2x | Forward P/E FY2026 / FY2027 | 83.3x / 40.2x |
| PEG (FY+1 P/E ÷ EPS growth) | 0.37 | EV / TTM revenue | 24.8x |
| TTM revenue | USD 41.3bn | TTM FCF / after SBC | 8.4bn / 6.5bn |
| Beta vs SPY (raw / Blume) | 2.46 / 1.98 | Realized vol 20d / 1y | 53% / 72% |
| Analysts / mean target | 50 / USD 629 (-0.4%) | Next earnings | 2026-11-03 |
| Shares out (diluted proxy) | 1.632bn | Short interest (% float) | 2.5% |
| Institutions / insiders | 75% / 0.42% | Dividend | none |

## 1. Price over time

![Price history](charts/price_history.png)

| Ticker | 1M | 3M | 6M | YTD | 1Y | 3Y | 5Y | 10Y | 10Y CAGR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **AMD** | +32% | +14% | +187% | +195% | +284% | +489% | +521% | +9218% | 57.4% |
| SOXX | +13% | +1% | +72% | +96% | +111% | +275% | +316% | +1623% | 32.9% |
| SPY | +1% | +3% | +18% | +15% | +17% | +87% | +91% | +321% | 15.5% |
| NVDA | +4% | +22% | +35% | +28% | +28% | +424% | +1073% | +14172% | 64.2% |
| AVGO | +1% | -3% | +16% | +5% | +8% | +343% | +716% | +2623% | 39.2% |
| INTC | +21% | -5% | +129% | +215% | +215% | +226% | +134% | +277% | 14.2% |
| QCOM | +7% | -3% | +45% | +7% | +9% | +74% | +58% | +254% | 13.5% |
| ARM | +20% | -6% | +104% | +177% | +98% | +460% | n/a | n/a | n/a |
| MRVL | +21% | +9% | +148% | +220% | +215% | +402% | +365% | +2106% | 36.3% |

Largest one-day moves in the last 5 years: 09 Apr 2025 +23.8%, 06 Oct 2025 +23.7%, 04 Feb 2026 -17.3%, 06 May 2026 +18.6%, 07 Oct 2022 -13.9%.

## 2. Return and risk (ch.5)

Statistics use the 60 complete months to Sep 2026.

| Statistic | Value | What it means |
|---|---:|---|
| Arithmetic mean (annualized) | 56.9% | Expected one-period return if the past repeats |
| Geometric mean (CAGR) | 42.8% | What a buy-and-hold investor actually earned; the gap ≈ σ²/2 is volatility drag |
| Standard deviation (annualized) | 69.4% | 4.4× the S&P 500's 15.7% |
| Skewness / excess kurtosis | 1.11 / 1.65 | Right-skewed, fat tails vs normal |
| 5% monthly VaR: historical / normal | -20.7% / -28.2% | One month in 20 loses at least this much |
| 5% monthly expected shortfall | -24.0% | Average loss in that worst 5% of months |
| Sharpe ratio (S&P 500) | 0.77 (0.67) | Excess return per unit of total risk |
| Sortino ratio | 1.71 | Excess return per unit of downside risk |
| Max drawdown, 5y | -65.4% (trough Oct 2022) | Currently -0.3% from the peak |

![Risk](charts/risk.png)

## 3. Index model, CAPM and factors (ch.8–10)

| Regression (60m excess returns) | Alpha (ann.) | t(α) | Beta | t(β) | R² | Residual σ |
|---|---:|---:|---:|---:|---:|---:|
| vs SPY | +27.5% | 1.04 | 2.46 | 5.06 | 0.31 | 57.8% |
| vs SOXX | +4.8% | 0.29 | 1.56 | 12.25 | 0.72 | 36.6% |

- **Risk decomposition (ch.8):** systematic variance β²σ²(M) = 14.9% vs firm-specific σ²(e) = 33.4%, so **31% of the risk is market-driven** and 69% is diversifiable.
- **CAPM required return (ch.9):** k = r_f + β × MRP = 4.02% + 2.46 × 5.5% = **17.6%** (Blume-adjusted β 1.98 → **14.9%**, used as the DCF discount rate).
- **Historical alpha** of +27.5% a year has a t-stat of 1.04: not statistically distinguishable from zero (ch.11: past alpha is a weak guide).
- **Fama-French 5 factors + momentum (ch.10):** R² 0.44, alpha +27.3% (t 1.03). Loadings: Mkt-RF +2.17 (t 4.5), SMB -0.68 (t -0.8), HML -0.24 (t -0.3), RMW -1.19 (t -1.6), CMA -1.07 (t -1.0), Mom +0.45 (t 0.8). A negative RMW and CMA loading means returns co-move with low-profitability, aggressive-investment stocks, the classic growth profile.

![Rolling beta](charts/rolling_beta.png)

## 4. Portfolio fit: allocation and diversification (ch.6–7)

Correlation of monthly returns with AMD (60m): SOXX 0.85, SPY 0.55, NVDA 0.59, AVGO 0.46, INTC 0.62, QCOM 0.65, ARM 0.54, MRVL 0.65.

- A 50/50 mix with SPY would have had volatility of 39.6% vs 42.5% for the weighted average of the two, a diversification benefit because ρ = 0.55 < 1.
- **Optimal risky share y\* = [E(r) − r_f] / (A·σ²)**, holding AMD alone against T-bills (σ = 69.4%):

| Risk aversion A | y\* with CAPM E(r) | y\* with E(r) + Street α |
|---|---:|---:|
| 2 | 14% | 7% |
| 3 | 9% | 5% |
| 4 | 7% | 3% |
| 6 | 5% | 2% |

Even a risk-tolerant investor would put only a modest share in a single stock this volatile. Ch.7–8 say the efficient choice is the market portfolio plus a Treynor-Black tilt (section 9), not a concentrated position.

## 5. Financial statements: quality of earnings (ch.19)

| Quarter | Revenue | Q/Q | Gross m. | Op. m. (GAAP) | Net m. | R&D % | SBC % | Diluted EPS | FCF | FCF m. | DSO (days) | DIO (days) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025-06 | 7.7bn | n/a | 39.8% | -1.7% | 11.3% | 24.6% | 4.8% | 0.54 | 1.73bn | 22.5% | 61 | 131 |
| 2025-09 | 9.2bn | +20% | 51.7% | 13.7% | 13.4% | 23.1% | 4.5% | 0.75 | 1.90bn | 20.6% | 61 | 149 |
| 2025-12 | 10.3bn | +11% | 54.3% | 17.1% | 14.7% | 22.7% | 4.7% | 0.92 | 2.38bn | 23.2% | 56 | 154 |
| 2026-03 | 10.3bn | -0% | 52.8% | 14.4% | 13.5% | 23.4% | 4.7% | 0.84 | 2.57bn | 25.0% | 54 | 151 |
| 2026-06 | 11.5bn | +13% | 53.8% | 17.3% | 19.9% | 21.9% | 4.4% | 1.38 | 1.56bn | 13.5% | 57 | 144 |

![Fundamentals](charts/fundamentals.png)

- **DuPont, TTM:** ROE 10.2% = net margin 15.6% × asset turnover 0.53 × leverage 1.25. The low turnover reflects a large goodwill and intangibles base from acquisitions; leverage is minimal.
- **GAAP vs economic earnings:** TTM amortization of acquired intangibles was 1.2bn, a non-cash charge that depresses GAAP EPS. That is why the trailing P/E (161x) overstates the multiple; cash flow tells the clearer story.
- **Cash conversion:** TTM operating cash flow 10.1bn vs net income 6.4bn. The accruals ratio of -4.6% of assets is negative (cash earnings exceed accounting earnings), a sign of high-quality earnings.
- **Stock-based compensation** of 1.9bn TTM (4.6% of revenue) is a real cost to shareholders. The valuation below uses FCF *after* SBC (owner FCF margin 15.8%). Buybacks were 1.2bn; share count changed +0.6% over the year.
- **Operating leverage (ch.17):** degree of operating leverage 3.06 from the weekly pipeline: each 1% change in sales moves EBIT by about 3.1%.

## 6. Valuation (ch.18)

![Valuation](charts/valuation.png)

**Multiples vs peers** (weekly pipeline, latest fiscal year and TTM):

| Ticker | Fwd P/E | P/S TTM | EV/EBITDA | FCF yield | Rev. growth FY | Gross m. | EBIT m. | ROE TTM | Target upside |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **AMD** | 40.7x | 25.1x | 107.3x | 1% | 34% | 50% | 12% | 10% | -2% |
| NVDA | 14.9x | 18.6x | 28.0x | 1% | 65% | 71% | 66% | 117% | 40% |
| AVGO | 18.3x | 19.0x | 33.1x | 2% | 24% | 68% | 41% | 44% | 50% |
| INTC | 57.9x | 11.1x | 38.7x | 1% | -0% | 35% | 5% | -11% | -2% |
| QCOM | 18.1x | 4.5x | 17.0x | 5% | 14% | 55% | 30% | 34% | 5% |
| ARM | 100.7x | 63.7x | 305.5x | 0% | 23% | 98% | 18% | 13% | -6% |
| MRVL | 40.3x | 25.9x | 86.3x | 1% | 42% | 51% | 40% | 17% | 8% |
| *Top-30 median* | 28.4x | 13.8x | 32.2x | 1% | 13% | 51% | 28% | 29% | 17% |

**Growth embedded in the price (PVGO).** With FY2027E EPS of USD 15.72 and k = 14.9%, the no-growth value E₁/k is USD 106. **PVGO = USD 526, which is 83% of the price**, so most of the value depends on growth beyond FY2027. No-growth P/E = 1/k = 6.7x vs the actual 40.2x.

**Constant-growth check.** On TTM owner FCF, P = FCF₁/(k − g) implies a perpetual growth rate of **14.2%**, above the 4% long-run nominal-GDP ceiling the book recommends for g.

**Scenario DCF (owner FCF, k = 14.9%, terminal g = 4%).** The revenue path is consensus FY2026 (50.9bn), then the FY2027 low/avg/high estimate, then growth that fades linearly to 4% over 8 years. Owner-FCF margin ramps from today's 15.8% to the scenario margin over 3 years.

| Scenario | FY2027 revenue | Growth after | Owner-FCF margin | FY2035 revenue | Terminal value share | Value / share | vs price |
|---|---:|---:|---:|---:|---:|---:|---:|
| Bear | 61.3bn | 12% | 20% | 117bn | 45% | **USD 96** | -85% |
| Base | 88.9bn | 25% | 28% | 285bn | 51% | **USD 280** | -56% |
| Bull | 118.1bn | 35% | 35% | 547bn | 54% | **USD 624** | -1% |

If the OpenAI warrant (up to 160M shares, vests on deployment and share-price milestones) fully vests, per-share values fall by about 8.9% (base case USD 255).


**Reverse DCF: what today's price assumes.** On the base revenue path the price requires a steady-state owner-FCF margin of **65%**. At the base 28% margin it requires **52% growth after FY2027**, or a discount rate of only **9.2%** (vs the CAPM 14.9%).

**Sensitivity:** base revenue path, value per share by discount rate (rows) and steady-state owner-FCF margin (columns).

| k \ margin | 20% | 25% | 30% | 35% | 40% |
|---|---:|---:|---:|---:|---:|
| 11.9% | 291 | 360 | 429 | 499 | 568 |
| 12.9% | 255 | 315 | 376 | 436 | 497 |
| 13.9% | 227 | 280 | 333 | 387 | 440 |
| 14.9% | 204 | 251 | 299 | 346 | 394 |
| 15.9% | 185 | 227 | 270 | 313 | 356 |

**Earnings-multiple cross-check:** FY2027E EPS USD 15.72 × 20x = 314, 25x = 393, 30x = 472, 35x = 550, 40x = 629, 45x = 707. The price implies 40x. The FY2027 EPS range across analysts is 9.60–20.25, so the estimate itself is very uncertain.

## 7. Market efficiency and earnings reactions (ch.11)

Market-model abnormal returns (vs SPY, estimated over the 250 days before each event) for the last 12 releases:

| Announced | Reaction day | EPS vs est. | Surprise | AR day 0 | CAR [−1,+1] | Drift CAR [+2,+20] |
|---|---|---|---:|---:|---:|---:|
| 2026-08-04 | 2026-08-05 | 1.66 vs 1.61 | 3.2% | -6.8% | -4.1% | -11.7% |
| 2026-05-05 | 2026-05-06 | 1.37 vs 1.29 | 5.8% | +15.3% | +14.6% | +13.8% |
| 2026-02-03 | 2026-02-04 | 1.53 vs 1.32 | 16.0% | -16.6% | -18.3% | -0.4% |
| 2025-11-04 | 2025-11-05 | 1.20 vs 1.17 | 2.5% | +1.7% | -5.1% | -14.1% |
| 2025-08-05 | 2025-08-06 | 0.48 vs 0.48 | -0.6% | -7.8% | -2.3% | -9.7% |
| 2025-05-06 | 2025-05-07 | 0.96 vs 0.93 | 2.8% | +1.2% | +1.3% | +8.2% |
| 2025-02-04 | 2025-02-05 | 1.09 vs 1.09 | 0.4% | -6.9% | -5.6% | +7.4% |
| 2024-10-29 | 2024-10-30 | 0.92 vs 0.92 | 0.5% | -9.8% | -4.6% | -15.9% |
| 2024-07-30 | 2024-07-31 | 0.69 vs 0.68 | 1.3% | +0.5% | -4.1% | +4.1% |
| 2024-04-30 | 2024-05-01 | 0.62 vs 0.61 | 2.0% | -8.3% | -6.8% | +4.2% |
| 2024-01-30 | 2024-01-31 | 0.77 vs 0.77 | -0.0% | +0.5% | -3.9% | +2.1% |
| 2023-10-31 | 2023-11-01 | 0.70 vs 0.68 | 3.6% | +7.4% | +4.3% | -2.1% |

- Average absolute day-0 abnormal move: **6.9%**. The sign of the EPS surprise matched the sign of the reaction 50% of the time, which is close to a coin flip: guidance and AI-GPU commentary matter more than the headline EPS beat.
- Post-announcement drift: the correlation between the initial reaction and the next-20-day drift is 0.35. A positive value hints at under-reaction (PEAD, ch.11–12), though with only 12 events the evidence is weak.

![Event study](charts/event_study.png)

## 8. Technicals and behavioural signals (ch.12)

| Indicator | Value | Read |
|---|---:|---|
| Price vs 50-day / 200-day MA | +22% / +68% | Golden cross (50 > 200) |
| RSI(14) | 69 | Neutral |
| 12-1 month momentum | +169% | Strong (Jegadeesh-Titman) |
| 6-month relative strength vs SOXX | +67% | Leader |
| Insider sales / purchases, last 6m | USD 0.27bn / USD 0.00bn | Mostly planned (10b5-1) sales; insider *buying* would be the informative signal (ch.11) |
| Analyst actions, last 90 days | 35 actions, 21 target raises | Targets chasing the price is a sign of anchoring and herding (ch.12) |
| Recent targets below current price | 46% | Upside in the consensus has been used up |
| Ratings (strong buy / buy / hold / sell) | 5 / 39 / 11 / 0 | Near-unanimous bullishness is crowded positioning |
| FY2027 EPS estimate: now vs 90 days ago | 15.72 vs 13.20 | +19% revision; up/down revisions in the last 30 days: 3/1 |

## 9. Treynor-Black: should an active manager overweight it? (ch.27)

| Step | Value |
|---|---:|
| Analyst-implied 12m return (mean target / price − 1) | -0.4% |
| CAPM 1-year required return (raw β) | 17.6% |
| Raw alpha | -18.0% |
| Minus average analyst optimism bias (Top-30 cross-section) | -9.9% |
| Shrunk alpha (× 0.25, for forecast imprecision) | **-7.0%** |
| Residual variance σ²(e) | 33.4% |
| Initial active weight w₀ = [α/σ²(e)] / [E(R_M)/σ²_M] | -9.3% |
| Beta-adjusted weight w\* = w₀ / [1 + (1 − β)w₀] | **-8.2%** |

A negative weight means an active manager would **underweight** it relative to the index. The weekly Top-30 pipeline, which uses the same method, gives -7.5% in the combined 30-stock active portfolio.

## 10. Options market view (ch.20–21)

![IV term structure](charts/iv_term.png)

| Expiry | Days | ATM IV | Implied ±1σ move to expiry | 90% put − 110% call IV (skew) |
|---|---:|---:|---:|---:|
| 2026-10-12 | 7 | 40% | ±5.5% (±35) | +4.2% |
| 2026-10-14 | 9 | 43% | ±6.7% (±43) | +1.8% |
| 2026-10-16 | 11 | 44% | ±7.7% (±49) | +1.3% |
| 2026-10-23 | 18 | 45% | ±9.9% (±62) | -0.6% |
| 2026-10-30 | 25 | 47% | ±12.2% (±77) | -0.8% |
| 2026-11-06 | 32 | 54% | ±16.1% (±102) | -0.5% |
| 2026-11-13 | 39 | 53% | ±17.3% (±110) | +0.5% |
| 2026-11-20 | 46 | 53% | ±18.7% (±118) | -0.4% |
| 2026-12-18 | 74 | 51% | ±23.0% (±145) | -0.1% |
| 2027-01-15 | 102 | 50% | ±26.4% (±167) | -0.8% |
| 2027-02-19 | 137 | 52% | ±31.7% (±200) | -1.1% |
| 2027-03-19 | 165 | 51% | ±34.6% (±219) | -0.8% |
| 2027-04-16 | 193 | 52% | ±37.8% (±239) | -0.2% |
| 2027-06-17 | 255 | 52% | ±43.5% (±275) | -1.4% |
| 2027-09-17 | 347 | 54% | ±52.3% (±331) | -1.1% |

- **Earnings-implied move:** the jump in variance from the 2026-10-30 expiry (IV 47%) to 2026-11-06 (IV 54%) prices an earnings-day move of **±8.3% (1σ)**, or about ±6.6% in absolute terms (≈ ±42). Compare the historical average absolute reaction of 6.9% in section 7.
- **Implied vs realized:** the ~1-month ATM IV is 54% vs realized 53% (20d) / 64% (60d) / 72% (1y). Options are cheap relative to recent realized volatility, so buying protection is relatively inexpensive.
- **Put-call parity (ch.20):** at the ATM strike for 2026-11-06, C − P − (S − PV(K)) = -0.76 per share. Close to zero, as parity requires.
- *Quotes were unavailable when the data was pulled (outside market hours), so implied vols use each contract's last trade price. Treat them as approximate; illiquid strikes can be stale.*

**Premium-selling menu for holders: the last expiry before earnings (2026-10-30), about 0.15/0.20/0.25/0.30 delta.**

| Type | Strike | Bid / Ask | Price | IV | Delta | P(expires OTM) | Distance | Yield | Annualized | OI |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Call | 680 | – | 14.55 | 48% | +0.31 | 74% | +7.6% | 2.30% | 34% | – |
| Call | 695 | – | 11.20 | 48% | +0.25 | 79% | +10.0% | 1.77% | 26% | – |
| Call | 710 | – | 8.60 | 49% | +0.20 | 83% | +12.4% | 1.36% | 20% | – |
| Call | 730 | – | 5.80 | 49% | +0.15 | 88% | +15.6% | 0.92% | 13% | – |
| Put | 560 | – | 6.46 | 48% | -0.15 | 82% | -11.4% | 1.15% | 17% | – |
| Put | 575 | – | 9.15 | 47% | -0.20 | 77% | -9.0% | 1.59% | 23% | – |
| Put | 585 | – | 11.55 | 47% | -0.24 | 72% | -7.4% | 1.97% | 29% | – |
| Put | 600 | – | 16.25 | 47% | -0.31 | 65% | -5.0% | 2.71% | 40% | – |

Calls = covered calls on shares you own (yield on the share price); puts = cash-secured puts (yield on the strike). Prices are last trades at the data pull and indicative only; check live quotes before trading.


## 11. Our hourly signal model

The [Hourly Trade Signals](../../trade-signals/index.md) engine rates AMD **🔴 Sell** with a composite score of **-0.36** (as of 2026-10-06 02:59 UTC). It combines the de-biased analyst alpha (40%), 12-1 momentum (25%), quality (20%) and trend (15%), with a penalty when RSI exceeds 75.

## 12. Qualitative analysis: business, PEST, catalysts and risks

!!! info "Qualitative notes reviewed 2026-10-06"
    These notes are written by hand, unlike the auto-refreshed numbers above. Events up to late 2025 come from company announcements. Later developments are *inferred from the data* (consensus estimates, price reactions) and should be checked against AMD's 10-Q/10-K filings and earnings calls.

### Business in one paragraph

AMD is a **fabless** designer of CPUs, GPUs and adaptive chips. TSMC manufactures its silicon (N3, moving to N2), with advanced packaging (CoWoS) and HBM memory from SK hynix, Samsung and Micron. It reports three segments:

- **Data Center:** EPYC server CPUs, Instinct AI GPUs, Pensando DPUs and NICs, and ZT Systems rack-scale design.
- **Client & Gaming:** Ryzen PC CPUs, Radeon GPUs, and semi-custom chips for Sony and Microsoft consoles.
- **Embedded:** the Xilinx FPGAs and adaptive SoCs.

The investment case today is almost entirely about **AI accelerators**. AMD is the only credible merchant alternative to NVIDIA at rack scale, while continuing to take server and PC CPU share from Intel.

### Key developments that shaped the numbers

| When | Event | Where it shows up above |
|---|---|---|
| Apr 2025 | US licence requirement on MI308 sales to China, with about USD 800M of inventory and related charges | Q2-2025 gross margin of 39.8% and a GAAP operating loss in the statements table |
| Jun 2025 | MI350/MI355X launch; Helios rack (MI400 series) and ROCm 7 roadmap | Data-center GPU ramp in 2026 revenue |
| 6 Oct 2025 | **OpenAI agreement for 6 GW of Instinct GPUs**, starting with 1 GW of MI450 in H2-2026. Includes a warrant for **up to 160M AMD shares** that vests on deployment and share-price milestones | +23.7% one-day move (largest in the table); dilution line under the DCF |
| Oct 2025 | Oracle plans to deploy MI450 at scale from 2026 | Consensus FY2027 revenue of about USD 89bn (+74%) |
| Nov 2025 | Financial analyst day: long-term targets of more than 35% revenue CAGR, more than 60% data-center CAGR and EPS above USD 20 within 3–5 years | Analyst targets up to USD 1,250 |
| Feb / May / Aug 2026 | Earnings reactions of −17%, +15% and −7% abnormal | Event-study table; the options market prices about ±8% for 3 Nov |

### PEST analysis

| Factor | Tailwinds | Headwinds | Net |
|---|---|---|:---:|
| **Political** | CHIPS-Act onshoring: TSMC Arizona builds EPYC, reducing Taiwan single-point risk. US policy favours domestic AI champions. | **Export controls**: China data-center GPUs need licences and revenue-sharing terms. Possible Section 232 semiconductor tariffs. Taiwan concentration of leading-edge supply (TSMC). Government equity support for a rival (Intel). | ⚠️ |
| **Economic** | Hyperscaler and AI-lab capex supercycle, with multi-GW commitments. Net-cash balance sheet. Operating leverage (DOL about 3) lifts margins as revenue scales. | **Customer concentration** and circular-financing optics (the OpenAI warrant). A long-duration equity (PVGO more than 80% of price) is very sensitive to the discount rate. HBM, DRAM and CoWoS cost inflation. PC and console cyclicality. | ⚖️ |
| **Social** | Mass adoption of AI by enterprises and consumers. Strong engineering brand under CEO Lisa Su. | Power, water and community pushback against GW-scale data centers. Talent costs (SBC about 4–5% of revenue). Crowded, retail-heavy positioning in AI stocks. | ⚖️ |
| **Technological** | Annual Instinct cadence (MI350 → MI450/Helios → MI500). Chiplet and 3D-stacking leadership. EPYC on TSMC 2 nm. ROCm improving. Rack-scale capability through ZT Systems. Open interconnects (UALink, Ultra Ethernet). | **The CUDA software moat** and NVIDIA's NVLink rack scale. Custom ASICs (Google TPU, AWS Trainium, Meta MTIA, OpenAI–Broadcom). Arm server CPUs (Graviton, Axion, Cobalt, Grace/Vera). Arm PCs (Snapdragon X). | ✅ |

### Bull case vs bear case

- **Bull:** MI450/Helios ships on time, and OpenAI and Oracle become reference customers that pull in more hyperscalers. Data-center GPU revenue compounds faster than consensus. Owner-FCF margin rises toward 35–40% (NVIDIA-like economics). The sensitivity table shows that at a 35–40% margin with an 11–12% discount rate, value reaches about USD 500–570, and the bull scenario is roughly today's price.
- **Bear:** delays or yield problems on the new rack, or customers favouring NVIDIA Rubin or their own ASICs, would hit FY2027 estimates. The low FY2027 estimate is 31% below the average, and the EPS range is 9.6–20.3. Margins would stay in the 20s, and the multiple would de-rate toward the peer median of about 28× forward earnings. That implies roughly USD 300–450.

### Catalysts to watch (next 6–12 months)

1. **Q3 FY2026 earnings, 3 Nov 2026 (after close).** Data-center GPU revenue and FY2027 guidance matter more than the EPS beat (section 7). The options market implies about ±8%.
2. **MI450 / Helios volume shipments** and the first OpenAI GW milestone, which also triggers warrant tranches (dilution).
3. **Hyperscaler capex guidance** in late-October results (Microsoft, Alphabet, Amazon, Meta, Oracle).
4. **Export-licence and tariff decisions** affecting China data-center sales.
5. **NVIDIA Rubin ramp** and custom-ASIC wins, the competitive read-through.

### What would change the verdict

- **More constructive:**
  - a pull-back toward the 50-day moving average or below about USD 470 (30× FY2027 EPS of 15.72, about 25% under today), where the bull and sensitivity cases offer upside;
  - FY2027 revenue consensus moving toward the high estimate (about USD 118bn) with margins holding;
  - evidence that owner-FCF margins can exceed 35%.
- **More cautious:**
  - GPU slippage;
  - gross margin falling below 50%;
  - FY2027 EPS revisions turning negative;
  - RSI above 75 combined with targets lagging the price.


---
*Generated by `analyses/deep-dives/deep_dive.py`. Quantitative sections refresh weekly; the qualitative notes carry their own review date.*
