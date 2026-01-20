# produce_final_fund_plan_summary PRD

## Description
Aggregates outputs from the compliance, pitch deck, and timeline nodes to create a single executive summary that encapsulates the fund’s strategy, legal structure, governance, risk framework, operations, fee model, and launch schedule.


## Conceptual Info

The node stitches together compliance, presentation, and scheduling data into a concise 400‑word executive summary that can be used by stakeholders to quickly understand the fund’s launch plan.

## Docstring

### Summary
Generates a concise executive summary of the hedge fund launch plan by synthesizing compliance, pitch deck, and timeline outputs.

### Parameters

- **compliance_output** (dict): Output from the design_compliance_program node, containing 'requirement_list' and 'policy_reference_list'.
- **pitch_deck_output** (dict): Output from the compile_pitch_deck_outline node, containing fields such as 'investment_strategy', 'legal_structure', and 'governance_structure'.
- **timeline_output** (dict): Output from the develop_timeline_and_milestones node, containing monthly milestones and key dates.

### Returns

dict: Dictionary matching the output_structure of the node, including summary_title, strategy_highlight, etc.

### Raises

- ValueError: If any required input field is missing or of incorrect type.
- KeyError: If expected keys are not present in the input dictionaries.

### Examples

```python
>>> compliance_output = {
...     'requirement_list': ['KYC', 'AML', 'Securities Act Compliance'],
...     'policy_reference_list': ['Policy_KYC', 'Policy_AML', 'Policy_Securities']
>>> }
>>> pitch_deck_output = {
...     'investment_strategy': 'Global Macro – focus on macroeconomic trends and commodity exposures.',
...     'legal_structure': 'Limited Partnership',
...     'governance_structure': 'GP oversees investment decisions; LP holds capital; Board provides oversight; Audit Committee ensures compliance; Compensation Committee sets fees.',
...     'risk_controls': ['Position Limits: 10% of AUM', 'Daily VaR: 2%', 'Stop‑Loss: 5%'],
...     'fee_structure': '1% Management Fee; 20% Performance Fee above 8% hurdle; 8% hurdle rate.',
...     'operations': 'Trade lifecycle: idea generation → order entry → execution → confirmation → settlement → reconciliation; Prime Broker: XYZ, Administrator: ABC.'
>>> }
>>> timeline_output = {
...     'month_numbers': list(range(1,13)),
...     'milestone_descriptions': [
...         'Month 1: Finalize legal documentation',
...         'Month 2: Onboard Prime Broker',
...         'Month 3: Launch marketing campaign',
...         'Month 4: First capital raise round',
...         'Month 5: Begin trading operations',
...         'Month 6: Regulatory filing complete',
...         'Month 7: First performance review',
...         'Month 8: Expand investment universe',
...         'Month 9: Second capital raise',
...         'Month 10: Full operational launch',
...         'Month 11: Audit commencement',
...         'Month 12: Investor reporting finalized'
...     ],
...     'regulatory_filing_months': [6],
...     'service_provider_onboarding_months': [2],
...     'capital_raise_months': [4, 9],
...     'overall_completion_month': 12
>>> }
>>> summary = produce_final_fund_plan_summary(compliance_output, pitch_deck_output, timeline_output)
>>> print(summary['summary_title'])
'Executive Summary: Global Macro Hedge Fund Launch'
```

```python
>>> print(summary['compliance_checklist_count'])
3
```
