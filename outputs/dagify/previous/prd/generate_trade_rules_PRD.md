# generate_trade_rules PRD

## Description
Create trade rule specifications.


## Conceptual Info

The goal of this node is to take the selected models and generate trade rules for each one. These trade rules are created by defining signal thresholds and position sizing rules that translate the models' predictions into buy/sell signals. The rules are then listed in a table for reference.

## Docstring

### Summary
Generate trade rules from selected models.

### Parameters

- **selected_models** (list[str]): A list of models to generate trade rules for.

### Returns

dict: A dictionary of trade rules with model names as keys.

### Raises

- ValueError: If the input models are empty.

### Examples

```python
>>> models = ['model1', 'model2', 'model3']
>>> trade_rules = generate_trade_rules(models)
{
    'model1': {'signal_threshold': 0.5, 'position_sizing_rule': 'fixed', 'buy_signal': 'price > signal_threshold', 'sell_signal': 'price < signal_threshold'},
    'model2': {'signal_threshold': 0.3, 'position_sizing_rule': 'dynamic', 'buy_signal': 'price > signal_threshold', 'sell_signal': 'price < signal_threshold'},
    'model3': {'signal_threshold': 0.2, 'position_sizing_rule': 'fixed', 'buy_signal': 'price > signal_threshold', 'sell_signal': 'price < signal_threshold'}
}
```
