# produce_final_fund_plan_summary PRD

## Description
Create comprehensive launch blueprint


## Conceptual Info

Synthesizes information from prior nodes to generate a comprehensive executive summary for the hedge fund launch plan.

## Docstring

### Summary
Produces a 200-word executive summary covering strategy, target returns, risk controls, regulatory structure, personnel, technology, and launch timeline.

### Parameters

- **pitch_deck_outline** (dict): Output from compile_pitch_deck_outline node
- **costs_estimation** (dict): Output from estimate_setup_and_operating_costs node
- **compliance_program** (dict): Output from design_compliance_program node

### Returns

dict: Dictionary containing the executive summary and its components

### Raises

- ValueError: If any of the input nodes are missing required fields

### Examples

```python
>>> pitch_deck_outline = {'strategy_overview': 'Long/short equity', 'risk_return_analysis': 'Target 15% annual return'}
>>> costs_estimation = {'total_annual_budget': 1000000.0, 'budget_overview': 'Detailed breakdown of costs'}
>>> compliance_program = {'accreditation_items': ['Item 1', 'Item 2'], 'aml_items': ['AML Item 1']}
>>> produce_final_fund_plan_summary(pitch_deck_outline, costs_estimation, compliance_program)
{'summary': '* Strategy: Long/short equity\n* Target Returns: 15% annual return\n* Risk Controls: Detailed risk management framework\n* Regulatory Structure: Registered with regulatory bodies\n* Personnel: Experienced team in place\n* Technology: State-of-the-art trading platform\n* Launch Timeline: Q1 2025'}
```
