# analyze_integration_test_results PRD

## Description
Identify interface-level issues.


## Conceptual Info

Extract and summarize interface-level issues from integration test results, producing structured lists that identify failing component interactions, data exchange problems, and any contract violations.

## Docstring

### Summary
Analyze integration test results to produce a structured report of interface-level issues.

### Parameters

- **integration_test_results** (Dict[str, List[str]]): Structured results from run_integration_tests, containing fields such as interface_validation_results, data_exchange_issues, component_pairs, and contract_violations.

### Returns

Dict[str, List[str]]: Dictionary with four lists: interface_failures, component_pairs, data_exchange_issues, and contract_violations.

### Raises

- ValueError: If required keys are missing in the input dictionary.

### Examples

```python
>>> integration_results = {'interface_validation_results': ['A-B contract violation: payload size mismatch'], 'data_exchange_issues': ['payload type mismatch'], 'component_pairs': ['A-B'], 'contract_violations': ['payload size mismatch']}
>>> analyze_integration_test_results(integration_results)
{'interface_failures': ['Interface failure: A-B - contract violation: payload size mismatch'], 'component_pairs': ['A-B'], 'data_exchange_issues': ['payload type mismatch'], 'contract_violations': ['payload size mismatch']}
```

```python
>>> integration_results = {'interface_validation_results': [], 'data_exchange_issues': [], 'component_pairs': [], 'contract_violations': []}
>>> analyze_integration_test_results(integration_results)
{'interface_failures': [], 'component_pairs': [], 'data_exchange_issues': [], 'contract_violations': []}
```
