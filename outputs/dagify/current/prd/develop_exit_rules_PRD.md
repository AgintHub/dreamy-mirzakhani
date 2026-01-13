# develop_exit_rules PRD

## Description
Create logic for closing positions


## Conceptual Info

This node generates a set of quantitative exit rules that govern when a trading strategy should close open positions. It takes the chosen strategy framework and pre‑processed market data as inputs, formulates multiple exit conditions using pseudo‑code, assigns realistic parameters, and tags each condition with an order type. The output is a validated list of rules ready for use in backtesting and live execution.

## Docstring

### Summary
Generate a validated set of quantitative exit rules for a trading strategy.

### Parameters

- **methodology** (str): Strategy framework selected by `choose_strategy_approach` ('rule-based', 'machine-learning', or 'hybrid').
- **data_meta** (dict): Metadata dictionary from `preprocess_data` (contains asset list, volatility metrics, etc.).

### Returns

dict: Dictionary containing exit_conditions (List[str]), parameter_values (List[float]), exit_order_types (List[str]), and is_valid (bool).

### Raises

- ValueError: If the methodology string is not one of the supported types.
- KeyError: If required keys (e.g., 'ATR', 'volatility') are missing from the data_meta.

### Examples

```python
>>> # Assume a rule‑based strategy and pre‑processed data containing 14‑day ATR
>>> rules = develop_exit_rules(methodology='rule-based', data_meta={'ATR_14': 0.012, 'volatility': 0.18})
>>> print(rules['exit_conditions'])
['price <= entry_price * (1 - 0.02 * ATR_14)',
 'price >= entry_price * (1 + 0.03 * ATR_14)',
 'time_in_position >= 10']
```

```python
>>> # Machine‑learning strategy with volatility‑based exit
>>> rules = develop_exit_rules(methodology='machine-learning', data_meta={'volatility': 0.22})
>>> print(rules['exit_order_types'])
['market', 'market', 'limit']
```
