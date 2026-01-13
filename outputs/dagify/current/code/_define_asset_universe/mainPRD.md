# _define_asset_universe - Complete PRD Documentation

## Overview
PRDs for nodes in the '_define_asset_universe' module.

## Table of Contents

- [validate_input_parameters](#validate_input_parameters)

- [get_available_instruments_database](#get_available_instruments_database)

- [filter_instruments_by_strategy](#filter_instruments_by_strategy)

- [prioritize_by_risk_profile](#prioritize_by_risk_profile)

- [select_balanced_instruments](#select_balanced_instruments)

- [extract_instrument_names](#extract_instrument_names)

- [generate_instrument_rationales](#generate_instrument_rationales)

- [count_distinct_asset_classes](#count_distinct_asset_classes)



---

## validate_input_parameters

### Description
Validate that investment strategy inputs are non‑empty strings and conform to predefined categories before proceeding with asset universe construction

### Conceptual Info

This shim ensures that the investment strategy inputs received from the `choose_investment_strategy` node are syntactically and semantically valid before any downstream processing occurs.

### Docstring

**Summary:** Validate strategy inputs to ensure they are non-empty strings and match allowed categories, raising errors otherwise.

**Parameters:**

- strategy_category (str): The primary investment strategy category selected by the user.
- strategy_rationale (str): A one‑paragraph explanation supporting the chosen strategy.
- risk_profile (str): The expected risk profile associated with the chosen strategy.
**Returns:** str - A message confirming that all inputs passed validation (e.g., "Validation succeeded").

**Raises:**

- ValueError: Raised when any input is an empty string or does not match an allowed category/risk profile.
- TypeError: Raised when any input is not of type `str`.
**Examples:**

```python
>>> validate_input_parameters(strategy_category='Growth',
...                        strategy_rationale='We aim for capital appreciation.',
...                        risk_profile='High')
"Validation succeeded"
```

```python
>>> validate_input_parameters(strategy_category='',
                                     strategy_rationale='Missing category.',
                                     risk_profile='Low')
"ValueError: strategy_category must be a non‑empty string"
```



---

## get_available_instruments_database

### Description
Retrieves a complete list of tradable instruments available for portfolio construction

### Conceptual Info

This shim abstracts the data retrieval layer for tradable instruments, enabling higher‑level strategy nodes to filter and rank assets without hard‑coding the source or schema.

### Docstring

**Summary:** Return the full instruments database as a list of dictionaries for downstream processing.

**Returns:** list of dict - Each dict contains keys such as 'name', 'ticker', 'asset_class', 'risk_factor', and any other metadata required by the strategy engine.

**Raises:**

- RuntimeError: If the data source is unreachable or returns an unexpected format.
- ValueError: If the retrieved data cannot be validated against the expected schema.
**Examples:**

```python
>>> instruments = get_available_instruments_database()
>>> len(instruments)
>>> instruments[0]['name']
100
'Apple Inc.'
```

```python
>>> try:
...     get_available_instruments_database()
>>> except RuntimeError as e:
...     print(str(e))
Data source unavailable.
```



---

## filter_instruments_by_strategy

### Description
Filters a list of available instruments based on a specified investment strategy category and rationale.

### Conceptual Info

This shim function filters a list of available instruments based on a specified investment strategy category and rationale, and returns a list of dictionaries representing the filtered instruments.

### Docstring

**Summary:** Filters a list of available instruments based on a specified investment strategy category and rationale.

**Parameters:**

- instruments (List[dict]): A list of dictionaries representing the available instruments.
- strategy_category (str): The primary investment strategy category.
- strategy_rationale (str): A one-paragraph explanation aligning the strategy with the fund's objectives.
**Returns:** List[dict] - A list of dictionaries representing the filtered instruments.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> available_instruments = [{'name': 'Instrument 1', 'asset_class': 'Stock'}, {'name': 'Instrument 2', 'asset_class': 'Bond'}]
>>> filtered_instruments = filter_instruments_by_strategy(instruments=available_instruments, strategy_category='Conservative', strategy_rationale='Low risk tolerance')
>>> print(filtered_instruments)
[{'name': 'Instrument 2', 'asset_class': 'Bond'}]
```

```python
>>> available_instruments = [{'name': 'Instrument 1', 'asset_class': 'Stock'}, {'name': 'Instrument 2', 'asset_class': 'Bond'}]
>>> filtered_instruments = filter_instruments_by_strategy(instruments=available_instruments, strategy_category='Aggressive', strategy_rationale='High risk tolerance')
>>> print(filtered_instruments)
[{'name': 'Instrument 1', 'asset_class': 'Stock'}]
```



---

## prioritize_by_risk_profile

### Description
Sorts a list of instrument dictionaries by their compatibility with a specified risk profile, returning the reordered list.

### Conceptual Info

The prioritize_by_risk_profile shim is responsible for ordering a collection of investment instruments so that those best aligned with a given risk appetite appear first. This ordering is used downstream to select a balanced set of assets.

### Docstring

**Summary:** Return an instrument list sorted by how well each instrument matches the requested risk profile.

**Parameters:**

- instruments (str): A JSON string representing a list of instrument dictionaries, each containing at least a 'risk_score' key and an 'identifier'.
- risk_profile (str): Desired risk level ('low', 'medium', 'high') that will guide the sorting heuristic.
**Returns:** str - A JSON string of the input instruments sorted in descending order of suitability for the specified risk profile.

**Raises:**

- ValueError: Raised if 'risk_profile' is not one of the supported values or if any instrument dictionary lacks required keys.
- TypeError: Raised if 'instruments' is not a valid JSON string or if parsed content is not a list of dictionaries.
**Examples:**

```python
>>> instruments = '[{"identifier": "ABC", "risk_score": 0.2}, {"identifier": "XYZ", "risk_score": 0.8}]'
>>> risk_profile = "high"
>>> result = prioritize_by_risk_profile(instruments, risk_profile)
>>> print(result)
"[{'identifier': 'XYZ', 'risk_score': 0.8}, {'identifier': 'ABC', 'risk_score': 0.2}]"
```

```python
>>> instruments = '[{"identifier": "DEF", "risk_score": 0.5}]'
>>> risk_profile = "low"
>>> print(prioritize_by_risk_profile(instruments, risk_profile))
"[{'identifier': 'DEF', 'risk_score': 0.5}]"
```



---

## select_balanced_instruments

### Description
Selects a balanced set of instruments from an input list to meet a target count while preserving diversity and risk preferences.

### Conceptual Info

The shim chooses a subset of instruments that balances asset class representation and risk considerations, ensuring the portfolio reaches the desired number of distinct tradable securities.

### Docstring

**Summary:** Selects a balanced subset of instruments from a given list, ensuring the returned set meets the target count and preserves diversity across asset classes while respecting the specified risk profile.

**Parameters:**

- instruments (List[dict]): A list of instrument dictionaries, each containing at least the keys 'name', 'asset_class', and 'risk'.
- target_count (int): The desired number of instruments to return.
**Returns:** List[dict] - A list of dictionaries representing the selected instruments, matching the structure of the input instruments.

**Raises:**

- ValueError: Raised if the target_count is less than 1 or greater than the number of unique asset classes available.
- TypeError: Raised if instruments is not a list or if target_count is not an integer.
**Examples:**

```python
>>> instruments = [
...     {'name': 'StockA', 'asset_class': 'Equity', 'risk': 0.3},
...     {'name': 'BondB', 'asset_class': 'Fixed Income', 'risk': 0.1},
...     {'name': 'CommodityC', 'asset_class': 'Commodity', 'risk': 0.5},
...     {'name': 'StockD', 'asset_class': 'Equity', 'risk': 0.4},
...     {'name': 'BondE', 'asset_class': 'Fixed Income', 'risk': 0.2},
>>> ]
>>> result = select_balanced_instruments(instruments, target_count=3)
>>> print(result)
[{'name': 'StockA', 'asset_class': 'Equity', 'risk': 0.3}, {'name': 'BondB', 'asset_class': 'Fixed Income', 'risk': 0.1}, {'name': 'CommodityC', 'asset_class': 'Commodity', 'risk': 0.5}]
```

```python
>>> select_balanced_instruments([], target_count=5)
ValueError: target_count must be at least 1 and at most the number of unique asset classes available.
```



---

## extract_instrument_names

### Description
Extracts the instrument names from a list of instrument dictionaries.

### Conceptual Info

In the asset universe definition workflow, this shim retrieves the names of the selected instruments to populate the output model.

### Docstring

**Summary:** Return a list of instrument names extracted from a list of instrument dictionaries.

**Parameters:**

- instruments (list[dict]): A list of dictionaries, each representing an instrument with at least a 'name' key.
**Returns:** list[str] - A list containing the value of the 'name' key from each instrument dictionary, preserving order.

**Raises:**

- TypeError: If `instruments` is not a list or if any element is not a dict.
- KeyError: If any instrument dictionary does not contain a 'name' key.
**Examples:**

```python
>>> instruments = [
...     {'name': 'AAPL', 'price': 150},
...     {'name': 'MSFT', 'price': 300},
...     {'name': 'GOOG', 'price': 2800}
>>> ]
>>> names = extract_instrument_names(instruments)
>>> print(names)
['AAPL', 'MSFT', 'GOOG']
```

```python
>>> instruments = [
...     {'id': 1, 'symbol': 'BTC'},
...     {'id': 2, 'symbol': 'ETH'}
>>> ]
>>> try:
...     extract_instrument_names(instruments)
>>> except KeyError as e:
...     print('KeyError:', e)
KeyError: 'name'
```



---

## generate_instrument_rationales

### Description
Generate brief rationales for a list of selected investment instruments based on a given strategy category.

### Conceptual Info

The generate_instrument_rationales shim function generates brief rationales for a list of selected investment instruments based on a given strategy category. This function plays a crucial role in providing explanations for the chosen instruments.

### Docstring

**Summary:** Generate brief rationales for a list of selected investment instruments based on a given strategy category.

**Parameters:**

- instruments (str): A string representation of the selected instruments.
- strategy_category (str): A string representing the strategy category.
**Returns:** List[str] - A list of brief rationales for each of the selected instruments.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> generate_instrument_rationales(instruments=['Instrument1', 'Instrument2'], strategy_category='Conservative')
>>> => ['Rationale for Instrument1', 'Rationale for Instrument2']
['Rationale for Instrument1', 'Rationale for Instrument2']
```

```python
>>> generate_instrument_rationales(instruments=['Instrument3', 'Instrument4'], strategy_category='Aggressive')
>>> => ['Rationale for Instrument3', 'Rationale for Instrument4']
['Rationale for Instrument3', 'Rationale for Instrument4']
```



---

## count_distinct_asset_classes

### Description
Counts the number of unique asset classes among a list of instrument dictionaries.

### Conceptual Info

This shim function aggregates the asset class field from each instrument in the input list and returns the count of unique asset classes, enabling downstream components to assess portfolio diversification.

### Docstring

**Summary:** Return the count of unique asset classes in a list of instrument dictionaries.

**Parameters:**

- instruments (List[dict]): A list of dictionaries, each representing an instrument with an 'asset_class' key.
**Returns:** int - The number of distinct asset classes present in the input list.

**Raises:**

- ValueError: Raised when the input list is empty or contains no valid 'asset_class' entries.
- TypeError: Raised when the input is not a list or when any element is not a dictionary.
**Examples:**

```python
>>> instruments = [
...     {'symbol': 'AAPL', 'asset_class': 'Equity'},
...     {'symbol': 'MSFT', 'asset_class': 'Equity'},
...     {'symbol': 'TLT', 'asset_class': 'Bond'}
>>> ]
>>> count_distinct_asset_classes(instruments)
2
```

```python
>>> instruments = [
...     {'symbol': 'GLD', 'asset_class': 'Commodity'},
...     {'symbol': 'SLV', 'asset_class': 'Commodity'},
...     {'symbol': 'VNQ', 'asset_class': 'Real Estate'}
>>> ]
>>> count_distinct_asset_classes(instruments)
3
```

