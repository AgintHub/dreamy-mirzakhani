# identify_regulatory_requirements PRD

## Description
This node outputs the key regulatory filings and registrations necessary for the specified legal entity and jurisdiction, based on the entity type selected earlier. It helps ensure compliance with relevant regulatory frameworks by identifying mandatory submissions and overseeing authorities.


## Conceptual Info

This node determines the key regulatory obligations for a fund based on its legal structure and jurisdiction, facilitating compliance planning.

## Docstring

### Summary
Returns the regulatory filings and authorities required for the specified legal entity type and jurisdiction.

### Parameters

- **entity_type** (str): The selected legal entity type for the fund, such as LP, LLC, SICAV.
- **jurisdiction** (str): The jurisdiction where the fund is established, e.g., Delaware, Cayman, Luxembourg.

### Returns

Dict[str, List[str]]: A dictionary containing two lists: regulatory requirements and overseeing authorities.

### Raises

- ValueError: Raised if the entity type or jurisdiction is invalid or unsupported.

### Examples

```python
>>> identify_regulatory_requirements('LP', 'Delaware')
{regulatory_requirements: [Form D Filing, State Business License], regulatory_authorities: [SEC, Delaware Division of Corporations]}
```

```python
>>> identify_regulatory_requirements('SICAV', 'Luxembourg')
{regulatory_requirements: [LuxSE Authorization, COMEX Registration], regulatory_authorities: [Luxembourg Financial Supervisory Authority, Luxembourg Stock Exchange]}
```
