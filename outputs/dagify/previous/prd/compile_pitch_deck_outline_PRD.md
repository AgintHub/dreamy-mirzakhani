# compile_pitch_deck_outline PRD

## Description
Build fundraising presentation framework


## Conceptual Info

The node aggregates the outputs from several strategy, risk, and operational nodes to construct a coherent 10‑slide investor pitch deck outline. Each slide focuses on a key narrative element—objective, strategy, team, edge, risk, fees, technology, hiring, costs, governance, and compliance—providing concise, investor‑friendly summaries.

## Docstring

### Summary
Generate a 10‑slide investor pitch deck outline from upstream fund planning outputs.

### Parameters

- **clarify_fund_objectives_output** (dict): Dictionary containing 'objectives', 'investment_purpose', 'competitive_edge', 'long_term_vision' from clarify_fund_objectives.
- **define_investor_profile_output** (dict): Dictionary with target investor characteristics.
- **choose_investment_strategy_output** (dict): Strategy category and rationale.
- **set_performance_and_risk_targets_output** (dict): Target financial and risk metrics.
- **draft_fee_structure_output** (dict): Fee percentages, hurdle and summary sentences.
- **design_risk_management_framework_output** (dict): List of risk control names, target metrics and limits.
- **define_technology_stack_output** (dict): Ops steps and corresponding tech components.
- **create_hiring_plan_output** (dict): Essential positions and responsibilities.
- **estimate_setup_and_operating_costs_output** (dict): Cost items and estimated USD.
- **outline_governance_structure_output** (dict): Governance roles and duties.
- **design_compliance_program_output** (dict): Compliance requirements and policy references.

### Returns

dict: A dictionary matching the defined output_structure keys, each containing a string or list as specified.

### Raises

- ValueError: If any required upstream output is missing or contains invalid types.
- TypeError: If downstream data does not conform to expected primitive types.

### Examples

```python
>>> result = compile_pitch_deck_outline(
...     clarify_fund_objectives_output={'objectives': ['High alpha'], 'investment_purpose': 'Alpha generation', 'competitive_edge': 'Quant model', 'long_term_vision': 'Global expansion'},
...     define_investor_profile_output={'typical_ticket_size': 5000000, 'risk_tolerance': 'high', 'liquidity_preference': 'annual', 'geographic_focus': 'North America'},
...     choose_investment_strategy_output={'strategy_category': 'Quantitative', 'strategy_rationale': 'Data‑driven alpha'},
...     set_performance_and_risk_targets_output={'gross_return': 0.20, 'volatility': 0.30, 'sharpe_ratio': 1.5, 'max_drawdown': 0.25},
...     draft_fee_structure_output={'management_fee_percentage': 0.02, 'performance_fee_percentage': 0.20, 'hurdle_rate_percentage': 0.05, 'summary_sentences': ['2% mgmt fee', '20% perf fee above 5% hurdle']},
...     design_risk_management_framework_output={'control_name': ['Position Limit', 'VaR Limit'], 'target_metric': ['Daily', 'Annual'], 'limit_value': [1.0, 0.02]},
...     define_technology_stack_output={'ops_steps': ['Data Collection', 'Model Development', 'Execution'], 'tech_components': ['Python', 'TensorFlow', 'FIX']},
...     create_hiring_plan_output={'essential_positions': ['Quant', 'Trader'], 'position_responsibilities': ['Build models', 'Execute trades'], 'total_headcount': 2},
...     estimate_setup_and_operating_costs_output={'cost_item': ['Prime Broker', 'Admin'], 'estimated_usd': [500000, 200000]},
...     outline_governance_structure_output={'role1_name': 'GP', 'role1_duty': 'Lead investment', 'role2_name': 'Manager', 'role2_duty': 'Day‑to‑day operations', 'role3_name': 'Board', 'role3_duty': 'Oversight', 'role4_name': 'Compliance Officer', 'role4_duty': 'Regulatory adherence', 'role5_name': 'Risk Officer', 'role5_duty': 'Risk monitoring'},
...     design_compliance_program_output={'requirement_list': ['KYC', 'AML'], 'policy_reference_list': ['Policy 1', 'Policy 2']}"
                ")
{
  "slide_1_title": "Introduction to QuantumAlpha Fund",
  "investment_objectives": "Generate 20% annual gross return while maintaining volatility below 30%.",
  "investment_strategy": "Quantitative multi‑factor strategy based on machine learning models.",
  "team_members": ["John Doe – Chief Quantitative Analyst", "Jane Smith – Lead Trader"],
  "competitive_edge": "Proprietary data‑driven models and real‑time execution platform.",
  "risk_controls": ["Position Limit: 100% of capital", "Annual VaR Limit: 2%"],
  "fee_structure": "2% management fee and 20% performance fee above a 5% hurdle.",
  "technology_stack": ["Python for data science", "TensorFlow for model training", "FIX protocol for execution"],
  "hiring_plan": ["Quant – Build models", "Trader – Execute trades"],
  "operating_costs": [500000.0, 200000.0],
  "governance_structure": "GP leads investment, Manager handles daily ops, Board provides oversight, Compliance Officer ensures regulatory compliance, Risk Officer monitors risk limits.",
  "compliance_program": "KYC and AML policies mapped to internal procedures."
}
```
