# _set_performance_and_risk_targets - Complete PRD Documentation

## Overview
PRDs for nodes in the '_set_performance_and_risk_targets' module.

## Table of Contents

- [validate_input_parameters](#validate_input_parameters)

- [get_strategy_template](#get_strategy_template)

- [adjust_targets_for_risk_profile](#adjust_targets_for_risk_profile)

- [generate_target_rationales](#generate_target_rationales)



---

## validate_input_parameters

### Description
Validates that the provided investment strategy parameters are non‑empty and of correct type before further processing.

### Conceptual Info

This shim ensures that the core parameters required to determine investment strategy—namely the strategy category, rationale, and risk profile—are present, non‑empty, and properly typed before any downstream calculations occur.

### Docstring

**Summary:** Validate that strategy_category, strategy_rationale, and risk_profile are non‑empty strings and raise appropriate errors otherwise.

**Parameters:**

- strategy_category (str): The chosen primary investment strategy category.
- strategy_rationale (str): A one‑paragraph explanation aligning the strategy with the fund's objectives.
- risk_profile (str): A concise description of the expected risk profile associated with the chosen strategy.
**Returns:** str - A confirmation message such as "Validation successful" when all inputs are valid.

**Raises:**

- ValueError: Raised when any of the input strings are empty or contain only whitespace.
- TypeError: Raised when any of the inputs is not of type str.
**Examples:**

```python
>>> validate_input_parameters(strategy_category='Growth',
...                       strategy_rationale='Focus on high growth stocks.',
...                       risk_profile='High')
'Validation successful'
```

```python
>>> try:
...     validate_input_parameters(strategy_category='',
...                               strategy_rationale='Growth',
...                               risk_profile='Medium')
>>> except ValueError as e:
...     print(e)
'strategy_category cannot be empty'
```



---

## get_strategy_template

### Description
Retrieves a strategy template based on the provided strategy category.

### Conceptual Info

The get_strategy_template shim function provides a strategy template based on the input strategy category, which is used to set performance and risk targets.

### Docstring

**Summary:** Retrieves a strategy template based on the provided strategy category.

**Parameters:**

- strategy_category (str): The primary investment strategy category.
**Returns:** dict - A dictionary containing the strategy template, including metric names and target values.

**Raises:**

- ValueError: When the input strategy category is invalid or not supported.
- TypeError: When the input strategy category is not a string.
**Examples:**

```python
>>> get_strategy_template(strategy_category='conservative')
{'metric_names': ['Gross Return', 'Volatility'], 'target_values': [0.05, 0.10]}
```

```python
>>> get_strategy_template(strategy_category='aggressive')
{'metric_names': ['Gross Return', 'Volatility'], 'target_values': [0.10, 0.20]}
```



---

## adjust_targets_for_risk_profile

### Description
Adjusts a dictionary of performance and risk targets according to the specified risk profile, returning the modified target set as a JSON string.

### Conceptual Info

This shim transforms generic strategy targets into risk‑adjusted targets, enabling downstream nodes to use realistic performance goals that align with the fund’s risk appetite.

### Docstring

**Summary:** Adjust performance and risk targets for a given risk profile.

**Parameters:**

- base_targets (str): A JSON string representing a dictionary with keys 'metric_names' (list of str) and 'target_values' (list of float) that defines the baseline targets for the chosen strategy.
- risk_profile (str): A short descriptor of the desired risk level (e.g., 'conservative', 'moderate', 'aggressive').
**Returns:** str - A JSON string of a dictionary with keys 'metric_names' and 'target_values', where each value has been adjusted to reflect the specified risk profile.

**Raises:**

- ValueError: If the base_targets JSON cannot be parsed or does not contain the required keys.
- TypeError: If either base_targets or risk_profile is not a string.
- KeyError: If the risk_profile is not recognized among supported profiles.
**Examples:**

```python
>>> base = '{"metric_names": ["Gross Return", "Volatility"], "target_values": [0.15, 0.10]}'
>>> result = adjust_targets_for_risk_profile(base_targets=base, risk_profile='aggressive')
>>> print(result)
"{\"metric_names\": [\"Gross Return\", \"Volatility\"], \"target_values\": [0.20, 0.12]}"
```

```python
>>> base = '{"metric_names": ["Sharpe Ratio", "Max Drawdown"], "target_values": [1.2, 0.05]}'
>>> result = adjust_targets_for_risk_profile(base_targets=base, risk_profile='conservative')
>>> print(result)
"{\"metric_names\": [\"Sharpe Ratio\", \"Max Drawdown\"], \"target_values\": [0.90, 0.08]}"
```



---

## generate_target_rationales

### Description
Generate brief rationales for performance and risk targets based on the investment strategy category and rationale.

### Conceptual Info

The generate_target_rationales shim function generates brief rationales for performance and risk targets based on the investment strategy category and rationale. These rationales explain how the targets align with the strategy and risk appetite.

### Docstring

**Summary:** Generate brief rationales for performance and risk targets based on the investment strategy category and rationale.

**Parameters:**

- targets (dict): Dictionary of performance and risk targets, including metric names and target values.
- strategy_rationale (str): One-paragraph explanation aligning the strategy with the fund's objectives.
- strategy_category (str): The chosen primary investment strategy category.
**Returns:** List[str] - List of brief rationales for performance and risk targets.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> generate_target_rationales(targets={'metric_names': ['Gross Return', 'Volatility'], 'target_values': [0.15, 0.10]}, strategy_rationale='This is a sample rationale.', strategy_category='Conservative')
['Rationale for Gross Return: 15% target is based on the fund\'s objective to achieve long-term growth.', 'Rationale for Volatility: 10% target is based on the fund\'s risk appetite to minimize losses.']
```

