# Methodology

Each analysis maps textbook methods from Bodie, Kane & Marcus, *Investments* (13th ed.) to market data. The table below lists the standard toolkit. Each analysis page states its own assumptions at the top and in its appendix.

| Area | Method | Book chapters |
|---|---|---|
| Return & risk | Holding-period and annualized (arithmetic vs geometric) returns, σ, Sharpe, Sortino, skew/kurtosis, VaR/Expected Shortfall, drawdowns | 5 |
| Capital allocation | Optimal risky share \(y^* = [E(r_P)-r_f]/(A\sigma_P^2)\) across risk-aversion levels | 6 |
| Diversification | Correlation, equal-weight diversification curve, long-only efficient frontier (min-variance, tangency) | 7 |
| Index models | Single-index regression (α, β, R², residual σ), Blume-adjusted β | 8 |
| Equilibrium | CAPM cost of equity, Security Market Line, Jensen's α and its t-statistic | 9 |
| Multifactor | Fama-French 5 factors + momentum regressions | 10, 13 |
| Market efficiency | Momentum, moving averages, RSI, and behavioral caveats. Deep dives add a market-model **earnings event study** (abnormal returns, CAR, post-announcement drift) | 11–12 |
| Macro & industry | PEST analysis, business-cycle sensitivity, operating leverage (DOL), industry life cycle | 17 |
| Equity valuation | Forward P/E, sustainable growth \(g = ROE \times b\), PVGO, constant-growth and two-stage FCF models, reverse-DCF implied growth, sensitivity | 18 |
| Financial statements | Five-factor DuPont, capital/R&D intensity, cash conversion, accruals-based earnings quality | 19 |
| Options | Implied vs realized volatility, implied move. Deep dives add the IV term structure, earnings-implied move, skew, a put-call parity check and Black-Scholes deltas for covered calls and cash-secured puts | 20–21 |
| Performance evaluation | Sharpe, Treynor, Jensen, information ratio, M² | 24 |
| International | Local vs USD return decomposition, currency contribution | 25 |
| Active management | Treynor-Black optimal active portfolio with de-biased, shrunk analyst alphas | 27 |
| Policy | Core-satellite framing, investment-policy guidance | 28 |

## Stock deep dives

`analyses/deep-dives/deep_dive.py TICKER` applies the toolkit above to one stock. It adds a **scenario DCF on owner FCF (FCF after stock-based compensation)**:

- Revenue follows consensus for the current and next fiscal year (low/avg/high), then growth fades linearly to 4% over 8 years.
- Margins ramp to the scenario level over 3 years.
- Cash flows are discounted at the Blume-adjusted CAPM rate.
- A reverse DCF solves for the margin, growth or discount rate that the price implies.

**Default scenarios** apply unless `config.json` overrides them:

| Inputs | Bear | Base | Bull |
|---|---|---|---|
| Next-year revenue | consensus low | consensus average | consensus high |
| Growth after next year (g = 0.6 × consensus growth + 2%, capped at 2–30%) | g / 2 | g | 1.4 × g + 1% (max 40%) |
| Owner-FCF margin, profitable companies (m = today's margin, 3–45%) | 0.75 × m | m | 1.25 × m |
| Margin, profitable but capex-heavy (m = 0.6 × operating margin) | 0.75 × m | m | 1.25 × m |
| Margin, loss-makers (m = 0.3 × gross margin, 5–12%; ramps over 5 years) | 3% | m | 1.6 × m |

Other rules:

- When no consensus estimates exist, the revenue path starts from TTM revenue and grows at the latest reported rate (±15% for low/high).
- The discount rate is never below r_f + 2% or g + 2%. A ticker can add an explicit risk premium, for example for country or legal-structure risk.
- Foreign filers' statements are converted to the quote currency.
- Peer multiples come from live Yahoo data for hand-picked peers; the relative-value check compares against the peer median.
- A speculative name (loss-making with net debt) cannot score above "Hold".

The verdict comes from a transparent 8-point checklist covering valuation, Street alpha, momentum, trend, RSI, fundamentals and balance sheet. Hand-written PEST and catalyst notes live in `analyses/deep-dives/notes/`.

## Data & reproducibility

- **Sources:** Yahoo Finance via `yfinance` (prices, fundamentals, option chains) and the Kenneth French Data Library (factors).
- **Currency:** foreign listings are converted to USD at daily spot FX. Fundamentals are converted when the reporting currency differs from the listing currency.
- **Refresh:** a scheduled GitHub Action re-fetches data, re-runs every model, rebuilds charts and tables, and republishes the site each week. The history of commits in `docs/` is a weekly snapshot archive.
- **Known limitations:** short estimation windows produce noisy αs and βs, vendor fundamentals contain errors (flagged where detected), and the universe choice introduces survivorship bias. DCF outputs are illustrative, not price targets.
