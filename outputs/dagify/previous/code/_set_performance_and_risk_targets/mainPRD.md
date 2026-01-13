# _set_performance_and_risk_targets - Complete PRD Documentation

## Overview
PRDs for nodes in the '_set_performance_and_risk_targets' module.

## Table of Contents

- [validate_input_parameters](#validate_input_parameters)

- [get_strategy_target_template](#get_strategy_target_template)

- [adjust_targets_for_risk_profile](#adjust_targets_for_risk_profile)

- [extract_metric_names](#extract_metric_names)

- [extract_target_values](#extract_target_values)

- [generate_target_rationales](#generate_target_rationales)



---

## validate_input_parameters

### Description
Validates the input parameters for the investment strategy.

### Conceptual Info

The validate_input_parameters shim function is used to validate the input parameters for the investment strategy, ensuring they meet the required criteria.

### Docstring

**Summary:** Validates the input parameters for the investment strategy.

**Parameters:**

- strategy_category (str): The primary investment strategy category.
- strategy_rationale (str): A one-paragraph explanation aligning the strategy with the fund's objectives.
- risk_profile (str): A concise description of the expected risk profile associated with the chosen strategy.
**Returns:** str - The output of the validation process.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> validate_input_parameters(strategy_category='conservative', strategy_rationale='This is a conservative strategy.', risk_profile='low risk')
'Validation successful'
```

```python
>>> validate_input_parameters(strategy_category='', strategy_rationale='This is a conservative strategy.', risk_profile='low risk')
'Validation failed: strategy_category is required'
```



---

## get_strategy_target_template

### Description
This shim function generates a base target template for performance and risk metrics based on the chosen investment strategy category.

### Conceptual Info

The get_strategy_target_template shim is responsible for providing initial target values for key performance and risk metrics based on the selected investment strategy, serving as a foundation for further adjustments and refinements.

### Docstring

**Summary:** Generates a base target template for performance and risk metrics based on the chosen investment strategy category, returning a dictionary with metric names as keys and target values as values.

**Parameters:**

- strategy_category (str): The category of the investment strategy (e.g., conservative, moderate, aggressive).
**Returns:** dict - A dictionary containing the base target metrics and their values for the specified strategy category.

**Raises:**

- ValueError: Raised when the strategy category is not recognized or supported.
- TypeError: Raised when the input strategy category is not a string.
**Examples:**

```python
>>> base_targets = get_strategy_target_template(strategy_category='conservative')
>>> print(base_targets)
{'Gross Return': 0.08, 'Volatility': 0.05, 'Sharpe Ratio': 1.2}
```

```python
>>> base_targets = get_strategy_target_template(strategy_category='aggressive')
>>> print(base_targets)
{'Gross Return': 0.15, 'Volatility': 0.12, 'Sharpe Ratio': 1.5}
```



---

## adjust_targets_for_risk_profile

### Description
Adjusts base targets according to the specified risk profile.

### Conceptual Info

The adjust_targets_for_risk_profile shim function adjusts base investment targets according to a specified risk profile, ensuring alignment between risk appetite and investment strategy.

### Docstring

**Summary:** Adjusts base investment targets according to a specified risk profile.

**Parameters:**

- base_targets (str): Base targets in dictionary format.
- risk_profile (str): Risk profile to adjust targets for.
**Returns:** str - The adjusted targets in dictionary format.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> adjust_targets_for_risk_profile(base_targets='{"metric1": 0.1, "metric2": 0.2}', risk_profile='conservative')
{"metric1": 0.05, "metric2": 0.1}
```

```python
>>> adjust_targets_for_risk_profile(base_targets='{"metric1": 0.1, "metric2": 0.2}', risk_profile='aggressive')
{"metric1": 0.2, "metric2": 0.4}
```



---

## extract_metric_names

### Description
Extracts metric names from a given set of targets.

### Conceptual Info

The extract_metric_names shim function takes in a set of targets and returns a list of corresponding metric names.

### Docstring

**Summary:** Extracts metric names from a given set of targets.

**Parameters:**

- targets (str): A string representation of the targets, expected to be a dictionary or a JSON string representing a dictionary.
**Returns:** List[str] - A list of extracted metric names.

**Raises:**

- ValueError: When the input targets are invalid or cannot be parsed.
- TypeError: When the input type is incorrect.
**Examples:**

```python
>>> import json
>>> targets = json.dumps({'Gross Return': 0.15, 'Volatility': 0.10})
>>> extract_metric_names(targets=targets)
['Gross Return', 'Volatility']
```

```python
>>> targets = '{'Gross Return': 0.15, 'Volatility': 0.10}'
>>> extract_metric_names(targets=targets)
['Gross Return', 'Volatility']
```



---

## extract_target_values

### Description
Extracts target values from a dictionary of targets.

### Conceptual Info

The extract_target_values shim function is used to extract target values from a dictionary of targets. It plays a crucial role in the set_performance_and_risk_targets function by providing the target values for performance and risk metrics.

### Docstring

**Summary:** Extracts target values from a dictionary of targets.

**Parameters:**

- targets (dict): A dictionary containing target values
**Returns:** List[float] - A list of target values

**Raises:**

- ValueError: When the input dictionary is empty or does not contain the expected keys.
- TypeError: When the input is not a dictionary.
**Examples:**

```python
>>> targets = {'metric1': 0.1, 'metric2': 0.2}
>>> extract_target_values(targets=targets)
[0.1, 0.2]
```

```python
>>> targets = {}
>>> extract_target_values(targets=targets)
[]
```



---

## generate_target_rationales

### Description
Generates brief rationales for each target, explaining how it aligns with strategy and risk appetite.

### Conceptual Info

The generate_target_rationales shim function generates brief rationales for each target, explaining how it aligns with strategy and risk appetite.

### Docstring

**Summary:** Generates brief rationales for each target, explaining how it aligns with strategy and risk appetite.

**Parameters:**

- metric_names (str): Names of the performance and risk metrics (e.g., Gross Return, Volatility, Sharpe Ratio, Max Drawdown).
- target_values (str): Numerical target values corresponding to each metric (e.g., 0.15 for 15% gross return, 0.10 for 10% volatility).
- strategy_rationale (str): A one-paragraph explanation aligning the strategy with the fund's objectives.
- risk_profile (str): A concise description of the expected risk profile associated with the chosen strategy.
**Returns:** LIST_STR - List of brief rationales for each target

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> generate_target_rationales(metric_names='Gross Return, Volatility', target_values='0.15, 0.10', strategy_rationale='This is a strategy rationale.', risk_profile='This is a risk profile.')
['Rationale for Gross Return: ...', 'Rationale for Volatility: ...']
```

