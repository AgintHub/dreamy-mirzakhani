# compile_pitch_deck_outline PRD

## Description
Provides the structure for fundraising presentation materials.


## Conceptual Info

This node creates a 10-slide outline for an investor pitch deck.

## Docstring

### Summary
Creates a 10-slide outline for an investor pitch deck.

### Parameters

- **investment_purpose** (str): Investment purpose from clarify_fund_objectives
- **strategy** (str): Investment strategy from clarify_fund_objectives
- **team** (str): Team title from define_investor_profile
- **edge** (str): Edge title from clarify_fund_objectives
- **risk_controls** (str): Risk controls title from design_risk_management_framework
- **fees** (str): Fees title from draft_fee_structure
- **target_returns** (str): Target returns title from set_performance_and_risk_targets
- **market_opportunity** (str): Market opportunity title from clarify_fund_objectives
- **service_providers** (str): Service providers title from list_service_providers
- **timeline** (str): Timeline title from develop_timeline_and_milestones

### Returns

-> dict[str, str]: A dictionary with 10 keys representing the slide titles

### Raises

- ValueError: If any input is missing

### Examples

```python
>>> investment_purpose = 'Invest in stocks and bonds'
>>> strategy = 'Grow and diversify assets'
>>> team = 'Our Investment Team'
>>> edge = 'Our edge in the market'
>>> risk_controls = 'Risk controls in place'
>>> fees = 'Management and performance fees'
>>> target_returns = 'Target return on investment'
>>> market_opportunity = 'Market opportunity'
>>> service_providers = 'Service providers'
>>> timeline = 'Launch timeline'
{'objectives': 'Objectives slide title', 'strategy': 'Strategy slide title', 'team': 'Team slide title', 'edge': 'Edge slide title', 'risk_controls': 'Risk controls slide title', 'fees': 'Fees slide title', 'target_returns': 'Target returns slide title', 'market_opportunity': 'Market opportunity slide title', 'service_providers': 'Service providers slide title', 'timeline': 'Timeline slide title'}
```
