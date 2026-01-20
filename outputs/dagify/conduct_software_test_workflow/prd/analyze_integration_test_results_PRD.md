# analyze_integration_test_results PRD

## Description
Identify interface-level issues.


## Conceptual Info

This node analyzes the results of integration tests executed by `run_integration_tests`, extracting interface-level failures such as component mismatches, data format problems, and protocol contract violations.

## Docstring

### Summary
Analyzes integration test logs to extract interface failures.

### Parameters

- **communication_logs** (List[str]): Logs of communication during each test scenario, as produced by `run_integration_tests`.
- **interface_validation_results** (List[str]): Validation outcomes for each interface per test step, as produced by `run_integration_tests`.
- **test_scenario_ids** (List[str]): Identifiers for each executed test scenario, as produced by `run_integration_tests`.

### Returns

Dict[str, List[str]]: Dictionary containing four keys: `interface_failures`, `component_pairs`, `data_exchange_issues`, and `contract_violations`. Each key maps to a list of strings describing the corresponding failure information.

### Raises

- ValueError: If any of the input lists are empty or None.
- IndexError: If the lengths of `communication_logs`, `interface_validation_results`, and `test_scenario_ids` are mismatched.

### Examples

```python
>>> analysis = analyze_integration_test_results(

...     communication_logs=["Scenario A: OK", "Scenario B: Timeout"],

...     interface_validation_results=["OK", "FAIL: timeout"],

...     test_scenario_ids=["A", "B"]

>>> )
{
  "interface_failures": ["ComponentA-ComponentB: Timeout"],
  "component_pairs": ["ComponentA-ComponentB"],
  "data_exchange_issues": ["Timeout during data transfer"],
  "contract_violations": []
}
```

```python
>>> analysis = analyze_integration_test_results(

...     communication_logs=["Scenario X: Data corruption"],

...     interface_validation_results=["FAIL: schema mismatch"],

...     test_scenario_ids=["X"]

>>> )
{
  "interface_failures": ["ComponentX-ComponentY: Schema mismatch"],
  "component_pairs": ["ComponentX-ComponentY"],
  "data_exchange_issues": ["Schema mismatch during data exchange"],
  "contract_violations": ["Expected JSON schema v1.2 not met"]
}
```
