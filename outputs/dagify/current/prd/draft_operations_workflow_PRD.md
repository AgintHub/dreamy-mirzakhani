# draft_operations_workflow PRD

## Description
Map operational processes


## Conceptual Info

This node compiles a detailed, step‑by‑step operational workflow for a hedge fund, aligning each phase of the trade lifecycle with its primary owner, the asset universe, the risk controls that govern the process, and the essential external service providers needed for execution. The output is a concise, structured representation that can be consumed by downstream staffing, technology, and compliance modules.

## Docstring

### Summary
Generate a structured trade‑lifecycle workflow table for a hedge fund.

### Parameters

- **asset_classes** (List[str]): Asset classes/instruments that will constitute the investable universe, as returned by the `define_asset_universe` node.
- **service_provider_categories** (List[str]): Mandatory third‑party service provider categories required for the fund, as returned by the `list_service_providers` node.
- **risk_controls** (List[Tuple[str, float]]): Quantitative risk controls with their thresholds, as returned by the `design_risk_management_framework` node. Each tuple contains a control name and its numeric limit.

### Returns

Dict[str, List[str]]: A dictionary containing five keys: `step_sequence`, `responsible_party`, `asset_classes`, `risk_controls`, and `service_providers`. Each value is a list of strings ordered to match the trade lifecycle.

### Raises

- ValueError: If any of the input lists are empty or have mismatched lengths.
- TypeError: If an input is not of the expected type.

### Examples

```python
>>> asset_classes = ["US Equities", "Emerging Markets Bonds", "Commodities Futures"],
>>> service_provider_categories = ["Prime Broker", "Custodian", "Compliance Consultant"],
>>> risk_controls = [("VaR Limit", 2.5), ("Position Size Cap", 5.0), ("Liquidity Threshold", 3.0)]
>>> workflow = draft_operations_workflow(asset_classes, service_provider_categories, risk_controls)
>>> print(workflow["step_sequence"])
["Idea Generation", "Idea Screening", "Research", "Trade Decision", "Order Entry", "Execution", "Post‑Trade Processing", "Performance Reporting"]
```

```python
>>> print(workflow["responsible_party"])
["Research Analyst", "Senior Analyst", "Portfolio Manager", "Head of Trading", "Trading Desk", "Execution Team", "Post‑Trade Analyst", "Performance Analyst"]
```
