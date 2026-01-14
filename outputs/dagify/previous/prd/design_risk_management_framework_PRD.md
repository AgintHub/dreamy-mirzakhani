# design_risk_management_framework PRD

## Description
Create risk mitigation architecture


## Conceptual Info

This node translates performance targets and asset universe constraints into a concrete set of risk controls. It enumerates both numerical limits (e.g., position caps, VaR thresholds) and process-oriented safeguards (e.g., daily monitoring, weekly reporting). The output is structured for downstream use in pitch decks and operational workflows.

## Docstring

### Summary
Generate a risk mitigation framework that aligns with performance targets and the chosen asset universe.

### Parameters

- **metric_names** (List[str]): Names of performance and risk metrics from set_performance_and_risk_targets.
- **target_values** (List[float]): Numeric target values corresponding to each metric.
- **rationale_texts** (List[str]): Brief rationale for each target.
- **instrument_names** (List[str]): List of the 10 selected tradable instruments from define_asset_universe.
- **instrument_rationales** (List[str]): Rationales for each instrument.
- **asset_class_count** (int): Number of distinct asset classes represented among the 10 instruments.

### Returns

dict: Dictionary matching the node's output structure: {num_quant_controls, quant_controls_desc, num_qual_practices, qual_practices_desc}.

### Raises

- ValueError: If any required input list is empty or misaligned in length.
- TypeError: If input types do not match the expected PrimitiveTypes.

### Examples

```python
>>> design_risk_management_framework(

...     metric_names=['Gross Return', 'Volatility', 'Sharpe Ratio', 'Max Drawdown'],

...     target_values=[0.15, 0.10, 2.0, 0.20],

...     rationale_texts=['Targeting 15% return', 'Control volatility to 10%', 'Sharpe > 2', 'Drawdown < 20%'],

...     instrument_names=['SPX Futures', 'Emerging Debt', 'Gold Futures', 'USD Bonds', 'EU Equity ETF', 'Oil Futures', 'US Treasury', 'China Shares', 'Eurodollar Futures', 'US Equity ETF'],

...     instrument_rationales=['Liquidity', 'Diversification', 'Inflation hedge', 'Safe haven', 'European exposure', 'Energy cycle', 'Credit quality', 'Growth potential', 'Interest rate sensitivity', 'Broad market exposure'],

...     asset_class_count=4

>>> )
{
  "num_quant_controls": 5,
  "quant_controls_desc": [
    "Position limit: max 10% of portfolio per instrument",
    "Daily VaR: 2% of NAV at 99% confidence",
    "Liquidity threshold: min 20% of position must be marketable within 2 hours",
    "Concentration limit: no single asset class > 25% of total NAV",
    "Leverage cap: maximum 3x equity exposure"
  ],
  "num_qual_practices": 3,
  "qual_practices_desc": [
    "Daily risk dashboard emailed to Portfolio Manager and Head of Risk",
    "Weekly risk review meeting with investment team and compliance",
    "Monthly audit of risk controls against performance targets"
  ]
}
```

```python
>>> design_risk_management_framework(

...     metric_names=['Gross Return', 'Volatility'],

...     target_values=[0.12, 0.08],

...     rationale_texts=['12% return', '8% vol'],

...     instrument_names=['AAPL', 'SPX Futures', 'US Treasury', 'Gold'],

...     instrument_rationales=['Growth', 'Index', 'Safe haven', 'Inflation hedge'],

...     asset_class_count=3

>>> )
{
  "num_quant_controls": 4,
  "quant_controls_desc": [
    "Max position per security: 5% of NAV",
    "Daily VaR: 1.5% of NAV",
    "Liquidity: 15% of position must be liquid within 1 hour",
    "Leverage: capped at 2x equity"
  ],
  "num_qual_practices": 3,
  "qual_practices_desc": [
    "Daily risk metric report",
    "Bi‑weekly risk review",
    "Quarterly independent risk audit"
  ]
}
```
