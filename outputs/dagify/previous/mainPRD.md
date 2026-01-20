# build_hedge_fund_detailed - Complete PRD Documentation

## Overview
PRDs for nodes in the 'build_hedge_fund_detailed' module.

## Table of Contents

- [choose_investment_strategy](#choose_investment_strategy)

- [choose_legal_entity_type](#choose_legal_entity_type)

- [clarify_fund_objectives](#clarify_fund_objectives)

- [compile_pitch_deck_outline](#compile_pitch_deck_outline)

- [create_hiring_plan](#create_hiring_plan)

- [define_asset_universe](#define_asset_universe)

- [define_investor_profile](#define_investor_profile)

- [define_technology_stack](#define_technology_stack)

- [design_compliance_program](#design_compliance_program)

- [design_risk_management_framework](#design_risk_management_framework)

- [develop_timeline_and_milestones](#develop_timeline_and_milestones)

- [draft_fee_structure](#draft_fee_structure)

- [draft_operations_workflow](#draft_operations_workflow)

- [estimate_setup_and_operating_costs](#estimate_setup_and_operating_costs)

- [identify_regulatory_requirements](#identify_regulatory_requirements)

- [list_service_providers](#list_service_providers)

- [outline_governance_structure](#outline_governance_structure)

- [produce_final_fund_plan_summary](#produce_final_fund_plan_summary)

- [select_jurisdiction](#select_jurisdiction)

- [set_performance_and_risk_targets](#set_performance_and_risk_targets)



---

## choose_investment_strategy

### Description
Select hedge fund strategy aligned with objectives

### Conceptual Info

This node translates the fund’s high‑level objectives into a concrete investment strategy choice, ensuring alignment between stated goals and the selected hedge fund approach.

### Docstring

**Summary:** Chooses a primary hedge fund strategy category that best aligns with the fund's objectives and returns a concise rationale.

**Parameters:**

- objectives (List[str]): Bullet list of the fund’s primary business objectives (investment purpose, competitive edge, long‑term vision).
- investment_purpose (str): Explicit description of the investment purpose extracted from the objectives.
- competitive_edge (str): Competitive advantage statement derived from the objectives.
- long_term_vision (str): Long‑term vision statement derived from the objectives.
**Returns:** Dict[str, str] - Dictionary containing the selected strategy category and a one‑sentence rationale.

**Raises:**

- ValueError: Raised if any of the input objective components are missing or empty.
- RuntimeError: Raised if no single strategy can be determined to satisfy all objectives.
**Examples:**

```python
>>> choose_investment_strategy(

...     objectives=["Generate alpha with low correlation to markets", "Maintain flexibility to trade multiple asset classes"],

...     investment_purpose="Create diversified alpha sources for institutional clients", 

...     competitive_edge="Access to proprietary data analytics", 

...     long_term_vision="Become a leading multi‑strategy fund in the next decade"

>>> )
{
  "strategy_category": "Multi‑Strategy (Long/Short Equity + Macro) ",
  "strategy_rationale": "Combines equity alpha generation with macro exposure to meet diversification and flexibility goals."
}
```

```python
>>> choose_investment_strategy(

...     objectives=["Achieve 15% annual gross return", "Limit volatility to 20%"],

...     investment_purpose="Deliver high risk‑adjusted returns to high‑net‑worth investors", 

...     competitive_edge="In‑house algorithmic models", 

...     long_term_vision="Establish a scalable, technology‑driven hedge fund"

>>> )
{
  "strategy_category": "Quantitative (Statistical Arbitrage) ",
  "strategy_rationale": "Algorithmic models enable consistent high returns while controlling volatility."
}
```



---

## choose_legal_entity_type

### Description
Define fund legal structure

### Conceptual Info

This node determines the most suitable legal entity for the hedge fund based on the previously selected jurisdiction, providing a concise justification.

### Docstring

**Summary:** Selects an appropriate legal entity type for the fund and returns a one‑sentence explanation.

**Parameters:**

- selected_jurisdiction (str): The fund domicile chosen in the preceding node (e.g., "Cayman", "Delaware", "Luxembourg").
**Returns:** dict - A dictionary with keys `legal_entity_type` (str) and `explanation` (str) describing the chosen entity.

**Raises:**

- ValueError: If `selected_jurisdiction` is not one of the supported jurisdictions.
**Examples:**

```python
>>> choose_legal_entity_type('Cayman')
{'legal_entity_type': 'LP', 'explanation': 'A Cayman Limited Partnership offers tax neutrality and flexibility for limited partners.'}
```

```python
>>> choose_legal_entity_type('Luxembourg')
{'legal_entity_type': 'SICAV', 'explanation': 'A Luxembourg SICAV provides an efficient structure for investment funds with a broad EU investor base.'}
```



---

## clarify_fund_objectives

### Description
State the primary business objectives for launching the hedge fund

### Conceptual Info

The node generates a succinct set of business objectives that guide the subsequent fund design process. These objectives serve as a reference for strategy selection, target investor profiling, and jurisdiction choice, ensuring all downstream decisions align with the fund’s core mission.

### Docstring

**Summary:** Generate a concise list of business objectives for a hedge fund launch.

**Parameters:**

- input_text (str): Prompt text instructing the objective generation. In practice this is the fixed prompt provided by the node.
**Returns:** dict - A dictionary containing four keys: 'objectives' (list of bullet strings), 'investment_purpose' (string), 'competitive_edge' (string), and 'long_term_vision' (string).

**Raises:**

- ValueError: If the input prompt is empty or not a string.
**Examples:**

```python
>>> def clarify_fund_objectives(input_text):
...     # implementation hidden
...     return {
...         'objectives': ['Maximize risk‑adjusted returns', 'Deliver consistent alpha', 'Build a resilient infrastructure'],
...         'investment_purpose': 'Generate excess returns beyond traditional indices',
...         'competitive_edge': 'Leverage proprietary analytics and a deep market network',
...         'long_term_vision': 'Become a leading global multi‑strategy fund with a 10‑year track record of outperforming benchmarks'}
{'objectives': ['Maximize risk‑adjusted returns', 'Deliver consistent alpha', 'Build a resilient infrastructure'], 'investment_purpose': 'Generate excess returns beyond traditional indices', 'competitive_edge': 'Leverage proprietary analytics and a deep market network', 'long_term_vision': 'Become a leading global multi‑strategy fund with a 10‑year track record of outperforming benchmarks'}
```

```python
>>> result = clarify_fund_objectives('')
>>> print(result['objectives'])
ValueError: Input prompt must be a non‑empty string.
```



---

## compile_pitch_deck_outline

### Description
Build fundraising presentation framework

### Conceptual Info

The node aggregates the outputs from several strategy, risk, and operational nodes to construct a coherent 10‑slide investor pitch deck outline. Each slide focuses on a key narrative element—objective, strategy, team, edge, risk, fees, technology, hiring, costs, governance, and compliance—providing concise, investor‑friendly summaries.

### Docstring

**Summary:** Generate a 10‑slide investor pitch deck outline from upstream fund planning outputs.

**Parameters:**

- clarify_fund_objectives_output (dict): Dictionary containing 'objectives', 'investment_purpose', 'competitive_edge', 'long_term_vision' from clarify_fund_objectives.
- define_investor_profile_output (dict): Dictionary with target investor characteristics.
- choose_investment_strategy_output (dict): Strategy category and rationale.
- set_performance_and_risk_targets_output (dict): Target financial and risk metrics.
- draft_fee_structure_output (dict): Fee percentages, hurdle and summary sentences.
- design_risk_management_framework_output (dict): List of risk control names, target metrics and limits.
- define_technology_stack_output (dict): Ops steps and corresponding tech components.
- create_hiring_plan_output (dict): Essential positions and responsibilities.
- estimate_setup_and_operating_costs_output (dict): Cost items and estimated USD.
- outline_governance_structure_output (dict): Governance roles and duties.
- design_compliance_program_output (dict): Compliance requirements and policy references.
**Returns:** dict - A dictionary matching the defined output_structure keys, each containing a string or list as specified.

**Raises:**

- ValueError: If any required upstream output is missing or contains invalid types.
- TypeError: If downstream data does not conform to expected primitive types.
**Examples:**

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



---

## create_hiring_plan

### Description
Define staffing requirements

### Conceptual Info

This node translates the operational workflow into a concrete hiring plan by identifying the most critical full‑time roles needed at launch and summarizing each role’s core responsibility.

### Docstring

**Summary:** Generate an essential staffing list for a hedge fund launch based on the daily trade lifecycle.

**Parameters:**

- trade_lifecycle_steps (List[str]): Ordered list of each operational step in the daily trade lifecycle.
- responsible_parties (List[str]): Ordered list of the party responsible for each corresponding step in trade_lifecycle_steps.
**Returns:** Dict[str, Any] - A dictionary containing three keys:
- `essential_positions`: List[str] of position titles.
- `position_responsibilities`: List[str] of one‑line responsibilities aligned with workflow gaps.
- `total_headcount`: int total number of positions.

**Raises:**

- ValueError: Raised if the input lists are empty or of mismatched length.
**Examples:**

```python
>>> steps = ["Idea Generation", "Order Entry", "Execution", "Confirmation", "Settlement", "Reconciliation"],
>>> parties = ["Research Analyst", "Trader", "Execution Trader", "Operations", "Operations", "Operations"],
>>> plan = create_hiring_plan(steps, parties)
>>> print(plan['essential_positions'])
>>> print(plan['position_responsibilities'])
>>> print(plan['total_headcount'])
[
  "Research Analyst",
  "Trader",
  "Execution Trader",
  "Operations Lead",
  "Settlement Specialist",
  "Reconciliation Analyst"
]
["Generate and screen investment ideas.",
 "Enter orders into the system.",
 "Execute trades on behalf of the fund.",
 "Oversee trade confirmation and post‑trade operations.",
 "Coordinate settlement with custodial and clearing partners.",
 "Validate daily P&L and reconcile accounts."]
6
```

```python
>>> steps = ["Idea Generation", "Order Entry", "Execution"],
>>> parties = ["Research", "Trader", "Execution"],
>>> plan = create_hiring_plan(steps, parties),
>>> print(plan['total_headcount'])
3
```



---

## define_asset_universe

### Description
Enumerate tradable assets/instruments for the selected hedge fund strategy.

### Conceptual Info

This node captures the market scope of the hedge fund by translating the chosen strategy into concrete asset classes and instruments, ensuring alignment with operational and risk frameworks downstream.

### Docstring

**Summary:** Generate a mapping of asset classes to specific instruments for a hedge fund strategy.

**Parameters:**

- strategy_category (str): The primary hedge fund strategy selected by `choose_investment_strategy` (e.g., "Long/Short Equity", "Global Macro").
**Returns:** Tuple[List[str], List[str]] - A tuple containing two lists: (asset_classes, instrument_types). Both lists contain at most eight string elements and are aligned by index.

**Raises:**

- ValueError: If `strategy_category` is not one of the supported strategy types.
- RuntimeError: If the derived lists exceed the maximum allowed length or are mismatched.
**Examples:**

```python
>>> asset_classes, instrument_types = define_asset_universe("Long/Short Equity")
(['Equities', 'Options', 'Fixed Income', 'Commodities'], ['S&P 500 ETF', 'Equity Options', 'US Treasury Bonds', 'Gold Futures'])
```

```python
>>> asset_classes, instrument_types = define_asset_universe("Global Macro")
(['Currencies', 'Futures', 'Equities', 'Fixed Income'], ['EUR/USD', 'Euro Stoxx 50 Futures', 'NASDAQ Composite', 'Euro Government Bonds'])
```



---

## define_investor_profile

### Description
Specify target investor characteristics

### Conceptual Info

The node translates the fund's business objectives into a concrete investor persona, outlining the financial size, risk appetite, liquidity needs, and geographic origin that align with the strategy.

### Docstring

**Summary:** Derives a target investor profile from clarified fund objectives.

**Parameters:**

- investment_purpose (str): The investment purpose defined in clarify_fund_objectives.
- competitive_edge (str): The competitive edge description from clarify_fund_objectives.
- long_term_vision (str): The long-term vision statement from clarify_fund_objectives.
**Returns:** dict - Dictionary containing typical_ticket_size (int), risk_tolerance (str), liquidity_preference (str), and geographic_focus (str).

**Raises:**

- ValueError: If any of the objective strings are empty or missing.
- TypeError: If the input types do not match the expected string types.
**Examples:**

```python
>>> profile = define_investor_profile(
...     investment_purpose='Generate alpha in emerging markets',
...     competitive_edge='Unique macro insights and rapid execution',
...     long_term_vision='Be the leading global macro fund by 2035'"
                ")
{
  'typical_ticket_size': 2000000,
  'risk_tolerance': 'high',
  'liquidity_preference': 'annual',
  'geographic_focus': 'North America & Europe'
}
```

```python
>>> profile = define_investor_profile(
...     investment_purpose='Diversify portfolio with low correlation assets',
...     competitive_edge='Access to niche commodity markets',
...     long_term_vision='Build a 5% IRR hedge fund portfolio by 2040'"
                ")
{
  'typical_ticket_size': 1000000,
  'risk_tolerance': 'medium',
  'liquidity_preference': 'quarterly',
  'geographic_focus': 'Global, with a focus on Asia-Pacific'
```



---

## define_technology_stack

### Description
Identify system requirements

### Conceptual Info

This node maps the daily trade lifecycle to the necessary software and infrastructure, ensuring each operational step has a clear technology owner.

### Docstring

**Summary:** Map each trade lifecycle step to its required technology component(s).

**Parameters:**

- trade_lifecycle_steps (List[str]): Ordered list of daily trade lifecycle steps as produced by draft_operations_workflow.
**Returns:** Dict[str, List[str]] - A dictionary containing two keys: 'ops_steps' and 'tech_components', each a list of strings aligned by index.

**Raises:**

- ValueError: If trade_lifecycle_steps is empty or contains non-string items.
**Examples:**

```python
>>> trade_lifecycle_steps = [
...     'Idea Generation',
...     'Order Entry',
...     'Execution',
...     'Confirmation',
...     'Settlement',
...     'Reconciliation']
>>> ops_steps, tech_components = define_technology_stack(trade_lifecycle_steps)
>>> print(ops_steps)
>>> print(tech_components)
[
    'Idea Generation',
    'Order Entry',
    'Execution',
    'Confirmation',
    'Settlement',
    'Reconciliation'
]
[
    'Ideation Platform (e.g., Slack, IdeaBoard)',
    'Order Management System (OMS)',
    'Execution Platform (e.g., FIX gateway, Algo engine)',
    'Confirmation System (e.g., Trade Capture)',
    'Clearing & Custody System',
    'Reconciliation Suite (e.g., Calypso, BlackLine)'
]
```

```python
>>> trade_lifecycle_steps = ['Order Entry', 'Execution', 'Settlement']
>>> ops_steps, tech_components = define_technology_stack(trade_lifecycle_steps)
>>> print(tech_components[-1])
'Clearing & Custody System'
```



---

## design_compliance_program

### Description
Create regulatory compliance framework

### Conceptual Info

The node assembles a compliance matrix that maps every regulatory requirement to a specific internal policy. It consumes the outputs from the risk‑management framework (to understand controls) and the regulatory‑requirements list (to know what must be met). The resulting matrices are used by the pitch deck and final summary.

### Docstring

**Summary:** Generate a compliance checklist that maps each regulatory requirement to its internal policy reference.

**Parameters:**

- control_name (List[str]): Names of the risk control measures from the risk‑management framework.
- target_metric (List[str]): Performance or risk metric each control is designed to limit.
- limit_value (List[float]): Numeric threshold for each control.
- requirements (List[str]): Primary regulatory filings or registrations required for the chosen legal entity.
- governing_bodies (List[str]): Governing bodies responsible for each regulatory requirement.
**Returns:** Tuple[List[str], List[str]] - A tuple containing two lists: the first list is the ordered regulatory requirements, the second list is the corresponding internal policy references that satisfy each requirement.

**Raises:**

- ValueError: If any input list is empty or if the lengths of the regulatory lists do not match.
**Examples:**

```python
>>> requirement_list, policy_reference_list = design_compliance_program(

...     control_name=["Position Limit", "VaR Limit"],

...     target_metric=["Daily Position Size", "Annual VaR"],

...     limit_value=[1.0, 0.02],

...     requirements=["Securities Act Registration", "AML Registration"],

...     governing_bodies=["SEC", "FINCEN"]

>>> )
{'requirement_list': ['Securities Act Registration', 'AML Registration'],
 'policy_reference_list': ['Policy_P100', 'Policy_P200']}
```

```python
>>> # Minimal example with one requirement

>>> design_compliance_program(

...     control_name=['Stop‑Loss Rule'],

...     target_metric=['Max Daily Loss'],

...     limit_value=[0.05],

...     requirements=['Regulation K'],

...     governing_bodies=['SEC']

>>> )
{'requirement_list': ['Regulation K'],
 'policy_reference_list': ['Policy_P300']}
```



---

## design_risk_management_framework

### Description
Outline core risk controls

### Conceptual Info

Generates a structured list of primary risk controls that tie directly to the fund’s quantitative performance and risk targets. Each control is mapped to a target metric and a numeric limit, forming the backbone of the fund’s risk‑management framework.

### Docstring

**Summary:** Creates core risk controls aligned with annual performance and risk targets.

**Parameters:**

- gross_return (float): Target annual gross return percentage (e.g., 0.15 for 15%).
- volatility (float): Target annual volatility percentage (e.g., 0.25 for 25%).
- sharpe_ratio (float): Target annual Sharpe ratio (e.g., 1.5).
- max_drawdown (float): Target maximum annual drawdown percentage (e.g., 0.30 for 30%).
**Returns:** dict - A dictionary containing three keys:
- 'control_name': List[str] of risk control names.
- 'target_metric': List[str] of metrics each control limits.
- 'limit_value': List[float] of numeric thresholds.

**Raises:**

- ValueError: If any target parameter is missing, None, or not a numeric type.
**Examples:**

```python
>>> controls = design_risk_management_framework(0.12, 0.20, 1.4, 0.25)
>>> print(controls['control_name'])
['Position Limit', 'VaR Limit', 'Stop‑Loss Rule']
```

```python
>>> controls = design_risk_management_framework(0.15, 0.22, 1.6, 0.28)
>>> print(controls['limit_value'])
[1.0, 0.02, 0.05]
```



---

## develop_timeline_and_milestones

### Description
Create launch schedule

### Conceptual Info

This node generates a month‑by‑month launch schedule for the hedge fund, integrating regulatory, operational, and fundraising milestones derived from prior design outputs.

### Docstring

**Summary:** Generate a 12‑month launch timeline with key milestones for regulatory filings, service‑provider onboarding, and capital raising.

**Parameters:**

- technology_stack (List[str]): List of technology components required for each operational step, produced by `define_technology_stack`.
- hiring_plan (List[str]): List of essential full‑time positions with one‑line responsibilities from `create_hiring_plan`.
- pitch_deck_outline (Dict[str, Any]): Dictionary containing slide titles, strategy, team, and other elements from `compile_pitch_deck_outline`; used to infer stakeholder needs.
**Returns:** Dict[str, Any] - A dictionary containing the six timeline fields described in `output_structure`.

**Raises:**

- ValueError: If any of the input lists are empty or missing required elements.
- KeyError: If mandatory keys are absent from the `pitch_deck_outline` dictionary.
**Examples:**

```python
>>> technology_stack = ["Trading platform", "Order management system", "Risk analytics suite"],
>>> hiring_plan = ["Head of Trading", "Senior Risk Analyst", "Operations Manager"],
>>> pitch_deck_outline = {"slide_1_title": "Alpha Fund", "investment_strategy": "Long/Short Equity", "team_members": ["John Doe, CIO", "Jane Smith, COO"]},
>>> timeline = develop_timeline_and_milestones(technology_stack, hiring_plan, pitch_deck_outline)
>>> print(timeline["milestone_descriptions"][0])
"Month 1: Finalize legal entity & file initial registration"
```

```python
>>> print(timeline["overall_completion_month"])
"12"
```



---

## draft_fee_structure

### Description
Define compensation model

### Conceptual Info

Creates a concise fee proposal that balances investor appeal with incentive alignment, integrating performance targets set by the risk‑management node.

### Docstring

**Summary:** Generate a structured fee schedule for a hedge fund based on performance and risk targets.

**Parameters:**

- gross_return (float): Target annual gross return (e.g., 0.15 for 15%) obtained from set_performance_and_risk_targets.
- volatility (float): Target annual volatility percentage from set_performance_and_risk_targets.
- sharpe_ratio (float): Target annual Sharpe ratio from set_performance_and_risk_targets.
- max_drawdown (float): Target maximum annual drawdown percentage from set_performance_and_risk_targets.
**Returns:** dict - A dictionary containing management_fee_percentage, performance_fee_percentage, hurdle_rate_percentage, and summary_sentences.

**Raises:**

- ValueError: If any input target is None or not a number.
- AssertionError: If performance_fee_percentage would exceed 50% or be negative.
**Examples:**

```python
>>> fee_structure = draft_fee_structure(gross_return=0.15, volatility=0.25, sharpe_ratio=1.5, max_drawdown=0.30)
{'management_fee_percentage': 0.025, 'performance_fee_percentage': 0.20, 'hurdle_rate_percentage': 0.08, 'summary_sentences': ['The fund charges a 2.5% annual management fee.', 'Performance fees of 20% apply to gains above an 8% hurdle.', 'This structure aligns manager incentives with investor returns.']}
```

```python
>>> fee_structure = draft_fee_structure(gross_return=0.10, volatility=0.20, sharpe_ratio=1.2, max_drawdown=0.25)
{'management_fee_percentage': 0.02, 'performance_fee_percentage': 0.15, 'hurdle_rate_percentage': 0.05, 'summary_sentences': ['The fund charges a 2% annual management fee.', 'Performance fees of 15% are charged on gains exceeding a 5% hurdle.', 'This fee schedule balances competitive pricing with strong incentive alignment.']}
```



---

## draft_operations_workflow

### Description
Generate an ordered list of daily trade lifecycle steps and the party responsible for each step.

### Conceptual Info

This node captures the day‑to‑day flow of a trade, mapping each activity to the entity or role that executes it. It provides a concise, step‑by‑step blueprint that feeds downstream staffing (create_hiring_plan) and technology requirements (define_technology_stack).

### Docstring

**Summary:** Creates an ordered list of daily trade lifecycle steps and the responsible party for each step.

**Parameters:**

- asset_classes (List[str]): List of asset classes the fund trades (from define_asset_universe). Used to infer any asset‑specific steps or responsibilities.
- instrument_types (List[str]): List of specific instruments traded (from define_asset_universe). Helps determine instrument‑specific responsibilities.
- prime_broker (str): Name of the selected prime broker (from list_service_providers). Often handles execution and confirmation.
- fund_administrator (str): Name of the fund administrator (from list_service_providers). Typically responsible for settlement and reconciliation.
- auditor (str): Name of the external auditor (from list_service_providers). May validate reconciliation.
- legal_counsel (str): Name of the legal counsel firm (from list_service_providers). Handles regulatory compliance of trade lifecycle.
- compliance_consultant (str): Name of the compliance consulting firm (from list_service_providers). Oversees policy adherence during each step.
- custodian (str): Name of the custodial service provider (from list_service_providers). Holds settled positions.
**Returns:** Tuple[List[str], List[str]] - A tuple containing an ordered list of trade lifecycle steps and a matching list of responsible parties.

**Raises:**

- ValueError: Raised if any required provider name is missing or empty.
- TypeError: Raised if input lists are not of type List[str] or provider arguments are not str.
**Examples:**

```python
>>> steps, parties = draft_operations_workflow(
...     asset_classes=['Equities', 'Futures'],
...     instrument_types=['S&P 500 ETF', 'Crude Oil Futures'],
...     prime_broker='PrimeCo',
...     fund_administrator='AdminInc',
...     auditor='AuditCo',
...     legal_counsel='LegalCo',
...     compliance_consultant='ComplianceCo',
...     custodian='CustodyCo' )
(
    ['Idea Generation', 'Order Entry', 'Execution', 'Confirmation', 'Settlement', 'Reconciliation'],
    ['In‑house Trading Desk', 'Compliance Team', 'PrimeCo', 'PrimeCo', 'AdminInc', 'AdminInc']
)
```

```python
>>> steps, parties = draft_operations_workflow(
...     asset_classes=['Equities'],
...     instrument_types=['SPY'],
...     prime_broker='PrimeCo',
...     fund_administrator='AdminInc',
...     auditor='AuditCo',
...     legal_counsel='LegalCo',
...     compliance_consultant='ComplianceCo',
...     custodian='CustodyCo' )
(
    ['Idea Generation', 'Order Entry', 'Execution', 'Confirmation', 'Settlement', 'Reconciliation'],
    ['In‑house Trading Desk', 'Compliance Team', 'PrimeCo', 'PrimeCo', 'AdminInc', 'AdminInc']
)
```



---

## estimate_setup_and_operating_costs

### Description
Produce an initial budget estimate for the hedge fund, aggregating annual fees from mandatory service providers and general operational overhead.

### Conceptual Info

This node generates a concise, annual cost estimate table that aggregates provider fees and overhead, enabling early budget planning and financial modeling for the hedge fund launch.

### Docstring

**Summary:** Estimates annual operating costs for each mandatory service provider and general overhead based on the selected providers.

**Parameters:**

- prime_broker (str): Name of the selected prime broker.
- fund_administrator (str): Name of the chosen fund administrator.
- auditor (str): Name of the external auditor.
- legal_counsel (str): Name of the legal counsel firm.
- compliance_consultant (str): Name of the compliance consulting firm.
- custodian (str): Name of the custodial service provider.
**Returns:** Tuple[List[str], List[float]] - A two‑tuple where the first element is a list of cost item names and the second is the corresponding annual USD amounts.

**Raises:**

- ValueError: Raised if any provider name is an empty string.
- TypeError: Raised if any input is not of type `str`.
**Examples:**

```python
>>> cost_items, costs = estimate_setup_and_operating_costs(
...     prime_broker='PrimeB',
...     fund_administrator='AdminCo',
...     auditor='AuditInc',
...     legal_counsel='LawFirm',
...     compliance_consultant='ComplianceGrp',
...     custodian='CustodianLLC')
[['Prime Broker Fees', 'Fund Administrator Fees', 'Auditor Fees', 'Legal Counsel Fees', 'Compliance Consultant Fees', 'Custodian Fees', 'General Overhead'],
 [120000.0, 85000.0, 40000.0, 30000.0, 25000.0, 50000.0, 75000.0]]
```

```python
>>> cost_items, costs = estimate_setup_and_operating_costs(
...     prime_broker='PrimeB',
...     fund_administrator='AdminCo',
...     auditor='AuditInc',
...     legal_counsel='LawFirm',
...     compliance_consultant='ComplianceGrp',
...     custodian='CustodianLLC')
>>> print(dict(zip(cost_items, costs)))
{'Prime Broker Fees': 120000.0, 'Fund Administrator Fees': 85000.0, 'Auditor Fees': 40000.0, 'Legal Counsel Fees': 30000.0, 'Compliance Consultant Fees': 25000.0, 'Custodian Fees': 50000.0, 'General Overhead': 75000.0}
```



---

## identify_regulatory_requirements

### Description
Generates a list of the key regulatory filings or registrations that the chosen legal entity must complete, along with the governing bodies responsible for each.

### Conceptual Info

This node takes the legal entity type chosen earlier in the workflow and returns a concise mapping of the most important regulatory filings along with the authorities that oversee those filings. The output feeds directly into the compliance checklist generation.

### Docstring

**Summary:** Determine the regulatory filings required for a selected legal entity and identify the corresponding governing bodies.

**Parameters:**

- legal_entity_type (str): The legal structure selected for the hedge fund (e.g., 'LP', 'LLC', 'SICAV').
**Returns:** Tuple[List[str], List[str]] - A tuple containing two lists:

1. `requirements`: the names of the primary filings or registrations.
2. `governing_bodies`: the names of the authorities that mandate each filing.

**Raises:**

- ValueError: If `legal_entity_type` is empty or not among the supported entity types.
- KeyError: If the internal mapping for the provided `legal_entity_type` cannot be found.
**Examples:**

```python
>>> requirements, governing_bodies = identify_regulatory_requirements('LLC')
(['DBS Filing', 'SEC Form D'], ['FINRA', 'SEC'])
```

```python
>>> requirements, governing_bodies = identify_regulatory_requirements('SICAV')
(['FCA Registration', 'Securities and Investment Fund Management Authority Filing'], ['FCA', 'SIFMA'])
```



---

## list_service_providers

### Description
Identify mandatory external providers required to launch a hedge fund based on the selected legal entity type.

### Conceptual Info

Creates a mandatory service‑provider checklist that feeds into operational planning and budgeting.

### Docstring

**Summary:** Generate a checklist of mandatory external service providers for a hedge fund, given the legal entity type selected earlier.

**Parameters:**

- legal_entity_type (str): The legal entity type chosen for the fund (e.g., LP, LLC, SICAV).  Used only to contextualize the provider selection but not directly influencing the output values.
**Returns:** dict - Dictionary with six string fields: prime_broker, fund_administrator, auditor, legal_counsel, compliance_consultant, custodian.

**Raises:**

- ValueError: If legal_entity_type is empty or not a recognized string.
- RuntimeError: If provider selection logic fails due to missing internal data.
**Examples:**

```python
>>> # Example 1: Simple LP structure
{
    "prime_broker": "Goldman Sachs",
    "fund_administrator": "KPMG",
    "auditor": "Deloitte",
    "legal_counsel": "Latham & Watkins",
    "compliance_consultant": "FATCA Compliance Partners",
    "custodian": "J.P. Morgan"
}
```



---

## outline_governance_structure

### Description
Define internal governance framework

### Conceptual Info

The node generates a concise governance chart that outlines the key internal roles and their primary responsibilities for a hedge fund. It supports the pitch deck and overall fund structure by providing a clear, easily digestible representation of governance.

### Docstring

**Summary:** Generate a five-role governance chart with one-line duties for each role.

**Parameters:**

- legal_entity_type (str): The chosen legal entity type (e.g., LP, LLC, SICAV). This value is used to contextualize role titles but not directly in the output.
**Returns:** dict - Dictionary containing the role names and their corresponding duties.

**Raises:**

- ValueError: Raised if any input parameter is missing or empty.
**Examples:**

```python
>>> output = outline_governance_structure(legal_entity_type='LP')
>>> print(output['role1_name'])
>>> print(output['role1_duty'])
"General Partner\nResponsible for investment decisions and fund oversight"
```

```python
>>> output = outline_governance_structure(legal_entity_type='LLC')
>>> print(output['role5_name'])
>>> print(output['role5_duty'])
"Compliance Officer\nEnsures regulatory adherence and internal policy enforcement"
```



---

## produce_final_fund_plan_summary

### Description
Aggregates outputs from the compliance, pitch deck, and timeline nodes to create a single executive summary that encapsulates the fund’s strategy, legal structure, governance, risk framework, operations, fee model, and launch schedule.

### Conceptual Info

The node stitches together compliance, presentation, and scheduling data into a concise 400‑word executive summary that can be used by stakeholders to quickly understand the fund’s launch plan.

### Docstring

**Summary:** Generates a concise executive summary of the hedge fund launch plan by synthesizing compliance, pitch deck, and timeline outputs.

**Parameters:**

- compliance_output (dict): Output from the design_compliance_program node, containing 'requirement_list' and 'policy_reference_list'.
- pitch_deck_output (dict): Output from the compile_pitch_deck_outline node, containing fields such as 'investment_strategy', 'legal_structure', and 'governance_structure'.
- timeline_output (dict): Output from the develop_timeline_and_milestones node, containing monthly milestones and key dates.
**Returns:** dict - Dictionary matching the output_structure of the node, including summary_title, strategy_highlight, etc.

**Raises:**

- ValueError: If any required input field is missing or of incorrect type.
- KeyError: If expected keys are not present in the input dictionaries.
**Examples:**

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



---

## select_jurisdiction

### Description
Choose optimal fund domicile

### Conceptual Info

This node evaluates the fund’s strategic objectives to recommend a domicile jurisdiction that best aligns with legal, tax, and operational considerations. It returns the selected jurisdiction name along with a balanced pros‑and‑cons list to inform downstream decisions such as legal entity selection.

### Docstring

**Summary:** Selects the most suitable fund domicile based on the fund’s objectives, returning the jurisdiction name and a concise pros/cons list.

**Parameters:**

- objectives (List[str]): Concise bullet list of the fund’s primary business objectives, including investment purpose, competitive edge, and long‑term vision.
- investment_purpose (str): Description of the investment purpose derived from the objectives.
- competitive_edge (str): Description of the competitive edge identified from the objectives.
- long_term_vision (str): Description of the long‑term vision derived from the objectives.
**Returns:** Dict[str, Any] - Dictionary with keys 'selected_jurisdiction' (str), 'pros' (List[str]), and 'cons' (List[str]).

**Raises:**

- ValueError: Raised if any of the objective inputs are missing or empty.
**Examples:**

```python
>>> select_jurisdiction(

...     objectives=[

...         "Generate alpha via multi‑strategy equity", 

...         "Leverage low regulatory friction", 

...         "Maintain investor confidentiality"

...     ],
...     investment_purpose="Long‑term capital appreciation via diversified equity strategies",
...     competitive_edge="Low tax burden and flexible legal framework",
...     long_term_vision="Become a leading independent multi‑strategy fund in the Americas"

>>> )
{
  "selected_jurisdiction": "Cayman Islands",
  "pros": ["Low corporate tax and no capital gains tax", "Strong confidentiality protections and established fund industry"],
  "cons": ["Perception of regulatory laxity may deter certain investors", "Limited local banking infrastructure requires offshore arrangements"]
}
```

```python
>>> select_jurisdiction(

...     objectives=["Global macro trading with high leverage"],

...     investment_purpose="Capture macro opportunities worldwide",
...     competitive_edge="Ability to deploy large leverage efficiently",
...     long_term_vision="Scale to $10B AUM within 5 years"

>>> )
{
  "selected_jurisdiction": "Delaware, USA",
  "pros": ["Well‑established legal framework for LLCs", "Access to U.S. capital markets and regulatory clarity"],
  "cons": ["Higher U.S. tax obligations for foreign investors", "More stringent reporting and disclosure requirements"]
}
```



---

## set_performance_and_risk_targets

### Description
Quantify financial and risk goals

### Conceptual Info

Sets quantitative performance and risk benchmarks that guide strategy design, risk controls, and fee structuring.

### Docstring

**Summary:** Generate annual financial and risk targets for a hedge fund based on the chosen investment strategy.

**Parameters:**

- strategy_category (str): Primary hedge fund strategy category selected by the `choose_investment_strategy` node.
- strategy_rationale (str): One‑sentence justification for the chosen strategy, provided by the parent node.
**Returns:** dict - Dictionary containing the four numeric target fields: `gross_return`, `volatility`, `sharpe_ratio`, and `max_drawdown`.

**Raises:**

- ValueError: If any input is missing or empty.
- TypeError: If inputs are not of type `str`.
**Examples:**

```python
>>> targets = set_performance_and_risk_targets('Long/Short Equity', 'A blend of alpha generation and risk mitigation through directional bets.')
{'gross_return': 0.18, 'volatility': 0.22, 'sharpe_ratio': 1.64, 'max_drawdown': 0.28}
```

```python
>>> targets = set_performance_and_risk_targets('Global Macro', 'Leveraging macroeconomic trends across multiple markets.')
{'gross_return': 0.15, 'volatility': 0.30, 'sharpe_ratio': 1.25, 'max_drawdown': 0.35}
```

