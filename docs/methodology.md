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
| Market efficiency | Momentum, moving averages, RSI, and behavioral caveats | 11–12 |
| Macro & industry | PEST analysis, business-cycle sensitivity, operating leverage (DOL), industry life cycle | 17 |
| Equity valuation | Forward P/E, sustainable growth \(g = ROE \times b\), PVGO, constant-growth and two-stage FCF models, reverse-DCF implied growth, sensitivity | 18 |
| Financial statements | Five-factor DuPont, capital/R&D intensity, cash conversion, accruals-based earnings quality | 19 |
| Options | Implied vs realized volatility, implied move | 20–21 |
| Performance evaluation | Sharpe, Treynor, Jensen, information ratio, M² | 24 |
| International | Local vs USD return decomposition, currency contribution | 25 |
| Active management | Treynor-Black optimal active portfolio with de-biased, shrunk analyst alphas | 27 |
| Policy | Core-satellite framing, investment-policy guidance | 28 |

## Data & reproducibility

- **Sources:** Yahoo Finance via `yfinance` (prices, fundamentals, option chains) and the Kenneth French Data Library (factors).
- **Currency:** foreign listings are converted to USD at daily spot FX. Fundamentals are converted when the reporting currency differs from the listing currency.
- **Refresh:** a scheduled GitHub Action re-fetches data, re-runs every model, rebuilds charts and tables, and republishes the site each week. The history of commits in `docs/` is a weekly snapshot archive.
- **Known limitations:** short estimation windows produce noisy αs and βs, vendor fundamentals contain errors (flagged where detected), and the universe choice introduces survivorship bias. DCF outputs are illustrative, not price targets.
