# define_asset_universe PRD

## Description
Specify eligible investment instruments for the hedge fund, ensuring alignment with the chosen investment strategy and compliance requirements.


## Conceptual Info

This node defines the concrete set of tradable instruments that the hedge fund will target. The selection must reflect the strategy chosen in the parent node, cover a balanced mix of asset classes, and satisfy regulatory and liquidity constraints.

## Docstring

### Summary
Generate a list of 10 tradable financial instruments along with short rationales and compute the distinct asset class count.

### Parameters

- **strategy_category** (str): Primary investment strategy category determined by the parent node (e.g., 'Long/Short Equity', 'Global Macro', 'Event‑Driven'). This informs the asset selection.
- **strategy_rationale** (str): One‑paragraph justification of the chosen strategy, used for contextual filtering of instruments.
- **risk_profile** (str): Concise description of the expected risk profile (e.g., 'High volatility, leverage‑enabled'). Helps prioritize high‑yield or high‑liquidity assets.

### Returns

dict: Dictionary with keys `instrument_names` (List[str]), `instrument_rationales` (List[str]), and `asset_class_count` (int) as defined in the node’s output structure.

### Raises

- ValueError: If any of the input parameters are missing or empty.
- RuntimeError: If the algorithm fails to assemble 10 distinct instruments after exhaustive search.

### Examples

```python
>>> # Example 1: Long/Short Equity strategy with moderate risk
>>> result = define_asset_universe(

...     strategy_category='Long/Short Equity',

...     strategy_rationale='Capitalize on market inefficiencies while providing downside protection.',

...     risk_profile='Moderate volatility with limited leverage.'

>>> )
{
  'instrument_names': [
    'S&P 500 Equity Index',
    'Nasdaq 100 Equity Index',
    'US Treasury 10‑Year Bond',
    'US Treasury 30‑Year Bond',
    'Gold Futures',
    'Oil Futures',
    'EUR/USD Spot',
    'US 10‑Year Treasury Futures',
    'Emerging Market Corporate Bond Index',
    'Credit Default Swap on S&P 500'
  ],
  'instrument_rationales': [
    'Large‑cap equity exposure for core long bets.',
    'High‑growth tech exposure to balance risk.',
    'Cash‑like instrument for portfolio liquidity.',
    'Long‑term yield curve play for duration control.',
    'Inflation hedge and commodity diversification.',
    'Oil price volatility capture.',
    'Currency overlay for hedge and speculation.',
    'Leverage and duration adjustment via futures.',
    'Diversification into high‑yield debt markets.',
    'Credit risk exposure and spread trading.'
  ],
  'asset_class_count': 5
}
```

```python
>>> # Example 2: Global Macro strategy with high risk tolerance
>>> result = define_asset_universe(

...     strategy_category='Global Macro',

...     strategy_rationale='Exploit macroeconomic trends across asset classes worldwide.',

...     risk_profile='High volatility, aggressive leverage allowed.'
                )
{
  'instrument_names': [
    'S&P 500 Futures',
    'Euro Stoxx 50 Futures',
    'US Treasury 10‑Year Futures',
    'US Treasury 30‑Year Futures',
    'Gold Spot',
    'Crude Oil Spot',
    'EUR/USD Forward',
    'Emerging Market Debt Futures',
    'Credit Default Swap Index on Emerging Markets',
    'Volatility Index (VIX) Futures'
  ],
  'instrument_rationales': [
    'Leverage on major equity markets.',
    'Exposure to European equity trends.',
    'Yield curve trade for duration control.',
    'Long‑term interest rate play.',
    'Inflation hedge.',
    'Energy market speculation.',
    'Currency overlay for macro bets.',
    'Emerging market debt trend exploitation.',
    'Credit spread trading across emerging markets.',
    'Volatility capture and risk management.'
  ],
  'asset_class_count': 5
}
```
