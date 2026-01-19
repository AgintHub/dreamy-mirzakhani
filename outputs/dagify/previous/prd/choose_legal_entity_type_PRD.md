# choose_legal_entity_type PRD

## Description
Selects the legal entity form for the fund.


## Conceptual Info

This node selects the appropriate legal entity form (LP, LLC, SICAV, etc.) for the fund based on the selected jurisdiction.

## Docstring

### Summary
Selects the legal entity form for the fund based on the selected jurisdiction.

### Parameters

- **selected_jurisdiction** (str): The legal jurisdiction selected by the fund.

### Returns

dict[str, str]: A dictionary containing the selected legal vehicle structure and its brief explanation.

### Raises

- ValueError: If the input jurisdiction is invalid or unsupported.

### Examples

```python
>>> selected_jurisdiction = 'Cayman'
>>> chosen_entity = choose_legal_entity_type(selected_jurisdiction)
>>> print(chosen_entity)
{"selected_entity_type": 'LP', "entity_type_rationale": 'brief explanation'}
```
