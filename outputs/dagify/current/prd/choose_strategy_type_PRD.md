# choose_strategy_type PRD

## Description
Select quant strategy category framework


## Conceptual Info

This node selects a primary quantitative trading strategy category based on predefined investment objectives. It maps the target risk-return profile, asset classes, and trading frequency to the most appropriate strategy framework, ensuring alignment with downstream risk management, parameter definition, and algorithmic logic components.

## Docstring

### Summary
Maps strategy objectives to framework category. Evaluates target return, risk tolerance, and asset classes to select a quant strategy type with a risk-aligned rationale.

### Parameters

- **annual_return_target_percentage** (float): Target annual return requirement in percent (e.g., 12.5 for 12.5%)
- **maximum_risk_tolerance_percentage** (float): Maximum acceptable drawdown or volatility threshold in percent (e.g., 10.0)
- **target_asset_classes** (List[str]): List of asset classes to be traded (e.g., ['equities', 'fixed income'])
- **trading_frequency_per_month** (int): Expected number of trades/signals per calendar month (e.g., 200)
- **additional_investment_goals** (List[str]): Supplemental constraints or objectives (e.g., ['liquidity preservation'])

### Returns

tuple[str, str]: Strategy type categorization and rationale. Returns (strategy_type, rationale) where strategy_type ∈ ['market neutral', 'statistical arbitrage', 'momentum', 'mean reversion', 'trend following']

### Raises

- ValueError: If no valid strategy type aligns with the provided objectives, or if required parameters are missing

### Examples

```python
>>> choose_strategy_type(annual_return_target_percentage=15.0," + 
                       "maximum_risk_tolerance_percentage=8.0," + 
                       "target_asset_classes=['equities'], " +
                       "trading_frequency_per_month=180, " +
                       "additional_investment_goals=['market beta neutrality'])
('market neutral', 'Diversified equity risk exposure aligns with beta neutrality goals')
```

```python
>>> choose_strategy_type(annual_return_target_percentage=25.0," +
                       "maximum_risk_tolerance_percentage=15.0," +
                       "target_asset_classes=['commodities'], " +
                       "trading_frequency_per_month=450, " +
                       "additional_investment_goals=['leveraged exposure'])
('trend following', 'High-return volatility profiles suit leveraged trend exploitation')
```
