# define_strategy_objective PRD

## Description
Establish the core goal of the quant strategy


## Conceptual Info

The `define_strategy_objective` node crystallises the high‑level ambition of the quant strategy into a single, unambiguous sentence and binds it to explicit quantitative performance and risk targets. This declaration serves as the foundation for downstream decisions on methodology, risk controls, position sizing, and backtesting parameters.

## Docstring

### Summary
Create a one‑sentence objective and associated quantitative benchmarks for a quantitative trading strategy.

### Parameters

- **objective_description** (str): Free‑text description of the intended trading goal (e.g., "Capture momentum in small‑cap stocks with <3% daily volatility").
- **cagr_target** (float): Desired Compound Annual Growth Rate expressed as a decimal (e.g., 0.15 for 15%).
- **annual_vol_target** (float): Maximum acceptable annual volatility expressed as a decimal (e.g., 0.20 for 20%).
- **max_drawdown** (float): Maximum acceptable drawdown expressed as a decimal (e.g., 0.25 for 25%).
- **sharpe_goal** (float): Target Sharpe ratio to be achieved by the strategy.

### Returns

dict: Dictionary containing the objective sentence and all benchmark values.

### Raises

- ValueError: Raised if any numeric benchmark is not within a realistic range (e.g., CAGR < 0 or > 1).
- TypeError: Raised if input types do not match the expected types.

### Examples

```python
>>> output = define_strategy_objective(

...     objective_description='Capture momentum in small‑cap stocks with <3%% daily volatility',

...     cagr_target=0.15,

...     annual_vol_target=0.20,

...     max_drawdown=0.25,

...     sharpe_goal=1.5

>>> )
{
  'strategy_sentence': 'Capture momentum in small‑cap stocks with <3% daily volatility',
  'cagr_target': 0.15,
  'annual_vol_target': 0.20,
  'max_drawdown': 0.25,
  'sharpe_goal': 1.5
}
```

```python
>>> # Invalid CAGR triggers ValueError

>>> try:

...     define_strategy_objective(

...         objective_description='Long‑term growth strategy',

...         cagr_target=-0.05,

...         annual_vol_target=0.15,

...         max_drawdown=0.2,

...         sharpe_goal=1.2

...     )

>>> except ValueError as e:

...     print(e)
"CAGR target must be between 0 and 1. Received: -0.05"
```
