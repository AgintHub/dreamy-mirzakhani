# _define_asset_universe - Complete PRD Documentation

## Overview
PRDs for nodes in the '_define_asset_universe' module.

## Table of Contents

- [validate_strategy_inputs](#validate_strategy_inputs)

- [build_strategy_context](#build_strategy_context)

- [generate_candidate_instruments](#generate_candidate_instruments)

- [apply_regulatory_and_liquidity_filters](#apply_regulatory_and_liquidity_filters)

- [select_balanced_instrument_mix](#select_balanced_instrument_mix)

- [extract_instrument_names](#extract_instrument_names)

- [generate_instrument_rationales](#generate_instrument_rationales)

- [count_distinct_asset_classes](#count_distinct_asset_classes)



---

## validate_strategy_inputs

### Description
Validates the strategy inputs to ensure they meet the expected criteria.

### Conceptual Info

The validate_strategy_inputs shim function is responsible for verifying that the provided strategy category, rationale, and risk profile meet the required standards.

### Docstring

**Summary:** Validates strategy inputs to ensure they meet the expected criteria.

**Parameters:**

- strategy_category (str): The primary investment strategy category.
- strategy_rationale (str): A one-paragraph explanation aligning the strategy with the fund's objectives.
- risk_profile (str): A concise description of the expected risk profile associated with the chosen strategy.
**Returns:** str - Output message indicating the validation result.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> validate_strategy_inputs(strategy_category='example_category', strategy_rationale='example_rationale', risk_profile='example_risk_profile')
'Validation successful'
```

```python
>>> validate_strategy_inputs(strategy_category='', strategy_rationale='example_rationale', risk_profile='example_risk_profile')
'Validation failed: strategy_category is required'
```



---

## build_strategy_context

### Description
Creates a strategy context dictionary based on the provided investment strategy category, rationale, and risk profile.

### Conceptual Info

The build_strategy_context shim function generates a strategy context dictionary that captures key information about an investment strategy, including its category, rationale, and risk profile. This context is used to inform subsequent decisions in the investment process.

### Docstring

**Summary:** Creates a strategy context dictionary based on the provided investment strategy category, rationale, and risk profile.

**Parameters:**

- category (str): The primary investment strategy category.
- rationale (str): A one-paragraph explanation aligning the strategy with the fund's objectives.
- risk_profile (str): A concise description of the expected risk profile associated with the chosen strategy.
**Returns:** dict - A dictionary representing the strategy context, containing the provided category, rationale, and risk profile.

**Raises:**

- ValueError: When any of the input parameters are missing or empty.
- TypeError: When the input parameters are of incorrect types.
**Examples:**

```python
>>> build_strategy_context(category='Growth', rationale='This is a growth strategy.', risk_profile='Moderate')
{'category': 'Growth', 'rationale': 'This is a growth strategy.', 'risk_profile': 'Moderate'}
```

```python
>>> build_strategy_context(category='Income', rationale='This is an income strategy.', risk_profile='Low')
{'category': 'Income', 'rationale': 'This is an income strategy.', 'risk_profile': 'Low'}
```



---

## generate_candidate_instruments

### Description
Generates a list of candidate instruments based on the provided strategy context.

### Conceptual Info

The generate_candidate_instruments shim function generates a list of candidate instruments based on the provided strategy context. This function plays a crucial role in the investment strategy definition process.

### Docstring

**Summary:** Generates a list of candidate instruments based on the provided strategy context.

**Parameters:**

- strategy_context (str): A string representing the strategy context, including category, rationale, and risk profile.
**Returns:** List[dict] - A list of dictionaries representing candidate instruments, each containing relevant details such as instrument name, type, and characteristics.

**Raises:**

- ValueError: When the input strategy context is invalid or incomplete.
- TypeError: When the input strategy context is not a string.
**Examples:**

```python
>>> generate_candidate_instruments(strategy_context={'category': 'equities', 'rationale': 'long-term growth', 'risk_profile': 'moderate'})
[{'instrument_name': 'AAPL', 'type': 'stock', 'characteristics': {...}}, {'instrument_name': 'GOOGL', 'type': 'stock', 'characteristics': {...}}]
```



---

## apply_regulatory_and_liquidity_filters

### Description
Applies regulatory and liquidity filters to a list of candidate instruments based on a specified strategy category.

### Conceptual Info

This shim function filters candidate instruments based on regulatory and liquidity requirements for a given strategy category.

### Docstring

**Summary:** Applies regulatory and liquidity filters to candidate instruments.

**Parameters:**

- candidates (List[dict]): List of dictionaries representing candidate instruments.
- strategy_category (str): The primary investment strategy category.
**Returns:** List[dict] - List of dictionaries representing filtered instruments.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> apply_regulatory_and_liquidity_filters(candidates=[{'name': 'Instrument 1', 'type': 'stock'}, {'name': 'Instrument 2', 'type': 'bond'}], strategy_category='equities')
 [{'name': 'Instrument 1', 'type': 'stock'}]
```

```python
>>> apply_regulatory_and_liquidity_filters(candidates=[{'name': 'Instrument 3', 'type': 'derivative'}, {'name': 'Instrument 4', 'type': 'currency'}], strategy_category='fixed_income')
 [{'name': 'Instrument 3', 'type': 'derivative'}]
```



---

## select_balanced_instrument_mix

### Description
Selects a balanced mix of instruments from a filtered list based on a target count and strategy context.

### Conceptual Info

The select_balanced_instrument_mix shim function is used to select a balanced mix of instruments from a filtered list based on a target count and strategy context.

### Docstring

**Summary:** Selects a balanced mix of instruments from a filtered list based on a target count and strategy context.

**Parameters:**

- filtered_instruments (str): A string representation of the filtered instruments.
- target_count (str): A string representation of the target count.
- strategy_context (str): A string representation of the strategy context.
**Returns:** List[dict] - A list of dictionaries representing the selected instruments.

**Raises:**

- ValueError: When the target count is not achievable with the filtered instruments.
- TypeError: When the input types are incorrect.
**Examples:**

```python
>>> select_balanced_instrument_mix(filtered_instruments='[{"name": "instrument1"}, {"name": "instrument2"}]', target_count='2', strategy_context='{"category": "strategy_category"}')
[{"name": "instrument1"}, {"name": "instrument2"}]
```



---

## extract_instrument_names

### Description
Extracts the names of instruments from a list of instrument dictionaries.

### Conceptual Info

The shim encapsulates the logic to pull instrument identifiers from a collection of instrument data structures, enabling downstream processes to work with a clean list of names.

### Docstring

**Summary:** Return a list of instrument names extracted from the provided list of instrument dictionaries.

**Parameters:**

- instruments (list): A list of dictionaries, each representing an instrument. Each dictionary must contain a key `'symbol'` whose value is the instrument name.
**Returns:** list[str] - A list of strings containing the instrument names in the same order as the input list.

**Raises:**

- ValueError: If any dictionary in the input list does not contain the key `'symbol'`.
- TypeError: If the input is not a list or contains non-dictionary elements.
**Examples:**

```python
>>> instruments = [
...     {'symbol': 'AAPL', 'price': 150},
...     {'symbol': 'MSFT', 'price': 300},
>>> ]
>>> print(extract_instrument_names(instruments))
['AAPL', 'MSFT']
```

```python
>>> instruments = [
...     {'symbol': 'TSLA', 'price': 700},
...     {'price': 1000},
>>> ]
>>> extract_instrument_names(instruments)
ValueError: Missing 'symbol' key in one or more instrument dictionaries.
```



---

## generate_instrument_rationales

### Description
Generates brief rationales for a list of selected investment instruments based on a given strategy context.

### Conceptual Info

This shim function generates brief rationales for a list of selected investment instruments based on a given strategy context. It is used to provide a concise explanation for each instrument in the Define Asset Universe step.

### Docstring

**Summary:** Generate brief rationales for a list of selected investment instruments based on a given strategy context.

**Parameters:**

- instruments (str): A string representation of the list of selected investment instruments
- strategy_context (str): A string representation of the strategy context
**Returns:** List[str] - A list of brief rationales for each of the selected instruments

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> generate_instrument_rationales(instruments=['Instrument 1', 'Instrument 2'], strategy_context='Conservative')
['Rationale for Instrument 1', 'Rationale for Instrument 2']
```

```python
>>> generate_instrument_rationales(instruments=['Instrument 3', 'Instrument 4'], strategy_context='Aggressive')
['Rationale for Instrument 3', 'Rationale for Instrument 4']
```



---

## count_distinct_asset_classes

### Description
Counts the number of distinct asset classes represented in a list of instruments.

### Conceptual Info

This shim function takes a list of instruments as input and returns the number of distinct asset classes represented in the list.

### Docstring

**Summary:** Counts the number of distinct asset classes in a list of instruments.

**Parameters:**

- instruments (str): A string representation of a list of instruments, where each instrument is associated with an asset class.
**Returns:** int - The number of distinct asset classes in the input list of instruments.

**Raises:**

- ValueError: When the input string is not a valid representation of a list of instruments.
- TypeError: When the input is not a string.
**Examples:**

```python
>>> instruments = '[{"name": "Instrument 1", "asset_class": "Equity"}, {"name": "Instrument 2", "asset_class": "Fixed Income"}]'
>>> count_distinct_asset_classes(instruments)
2
```

```python
>>> instruments = '[{"name": "Instrument 1", "asset_class": "Equity"}, {"name": "Instrument 2", "asset_class": "Equity"}]'
>>> count_distinct_asset_classes(instruments)
1
```

