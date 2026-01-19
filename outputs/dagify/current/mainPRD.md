# build_hedge_fund - Complete PRD Documentation

## Overview
PRDs for nodes in the 'build_hedge_fund' module.

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

- [produce_final_fund_plan_summary](#produce_final_fund_plan_summary)

- [select_jurisdiction](#select_jurisdiction)

- [set_performance_and_risk_targets](#set_performance_and_risk_targets)



---

## choose_investment_strategy

### Description
Chooses a high-level investment strategy

### Conceptual Info

Chooses a high-level investment strategy based on the objectives of the fund.

### Docstring

**Summary:** Selects a primary hedge-fund strategy category that best serves the objectives.

**Parameters:**

- fund_objectives (dict): Output from 'clarify_fund_objectives' node containing primary business objectives.
**Returns:** dict - A dictionary containing the 'chosen_investment_strategy' and 'justification' values.

**Examples:**

```python
>>> fund_objectives = {'investment_purpose': 'Capital appreciation', 'target_return_profile': 'Above market', 'competitive_advantage': 'Active management', 'long_term_vision': 'Long-term growth'}"
                "chosen_investment_strategy, justification = choose_investment_strategy(fund_objectives)
{'chosen_investment_strategy': 'Activemanagement', 'justification': 'To capture above-market returns through active management'}
```



---

## choose_legal_entity_type

### Description
Selects the legal entity form for the fund.

### Conceptual Info

This node selects the appropriate legal entity form (LP, LLC, SICAV, etc.) for the fund based on the selected jurisdiction.

### Docstring

**Summary:** Selects the legal entity form for the fund based on the selected jurisdiction.

**Parameters:**

- selected_jurisdiction (str): The legal jurisdiction selected by the fund.
**Returns:** dict[str, str] - A dictionary containing the selected legal vehicle structure and its brief explanation.

**Raises:**

- ValueError: If the input jurisdiction is invalid or unsupported.
**Examples:**

```python
>>> selected_jurisdiction = 'Cayman'
>>> chosen_entity = choose_legal_entity_type(selected_jurisdiction)
>>> print(chosen_entity)
{"selected_entity_type": 'LP', "entity_type_rationale": 'brief explanation'}
```



---

## clarify_fund_objectives

### Description
Produces a bullet-list of the fund's primary business objectives.

### Conceptual Info

Clarify the primary business objectives of a hedge fund, including investment purpose, target return profile, competitive advantage, and long-term vision.

### Docstring

**Summary:** clarify_fund_objectives

**Returns:** dict[str, str] - fund objectives

**Examples:**

```python
>>> result = clarify_fund_objectives()
>>> print(result)
{'investment_purpose': 'Generate absolute returns', 'target_return_profile': 'High returns with moderate risk', 'competitive_advantage': 'Active risk management', 'long_term_vision': 'Achieve long-term capital appreciation', 'other_objectives': 'Grow AUM and increase investor base'}
```

```python
>>> result = clarify_fund_objectives()
>>> print(result)
{'investment_purpose': 'Maximize return on investment', 'target_return_profile': 'High returns with high risk', 'competitive_advantage': 'Active risk management',
    'long_term_vision': 'Achieve long-term capital growth', 'other_objectives': 'Grow AUM and increase investor base'}
```



---

## compile_pitch_deck_outline

### Description
Provides the structure for fundraising presentation materials.

### Conceptual Info

This node creates a 10-slide outline for an investor pitch deck.

### Docstring

**Summary:** Creates a 10-slide outline for an investor pitch deck.

**Parameters:**

- investment_purpose (str): Investment purpose from clarify_fund_objectives
- strategy (str): Investment strategy from clarify_fund_objectives
- team (str): Team title from define_investor_profile
- edge (str): Edge title from clarify_fund_objectives
- risk_controls (str): Risk controls title from design_risk_management_framework
- fees (str): Fees title from draft_fee_structure
- target_returns (str): Target returns title from set_performance_and_risk_targets
- market_opportunity (str): Market opportunity title from clarify_fund_objectives
- service_providers (str): Service providers title from list_service_providers
- timeline (str): Timeline title from develop_timeline_and_milestones
**Returns:** -> dict[str, str] - A dictionary with 10 keys representing the slide titles

**Raises:**

- ValueError: If any input is missing
**Examples:**

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



---

## create_hiring_plan

### Description
Determines initial staffing requirements.

### Conceptual Info

Creates a list of essential roles required for launching the fund with detailed responsibilities.

### Docstring

**Summary:** Determine initial staffing requirements based on drafted operations workflow.

**Parameters:**

- tradelifecycle_steps (List[str]): List of daily trade lifecycle steps from drafted operations workflow.
**Returns:** dict - A dictionary containing 'roles_needed' and 'count_roles'.

**Raises:**

- ValueError: If 'tradelifecycle_steps' is empty.
**Examples:**

```python
>>> create_hiring_plan(tradelifecycle_steps=['Idea generation', 'Order creation', 'Execution', 'Confirmation', 'Settlement', 'Reconciliation'])

role_needed = roles_needed
count_roles = count_roles
print(role_needed)
print(count_roles)
```

```python
>>> create_hiring_plan(tradelifecycle_steps=['Idea generation', 'Order creation', 'Execution', 'Confirmation', 'Settlement', 'Reconciliation', 'Market Analysis'])

role_needed = roles_needed
count_roles = count_roles
print(role_needed)
print(count_roles)
```



---

## define_asset_universe

### Description
Enumerates the tradable assets and instruments.

### Conceptual Info

This node takes the chosen investment strategy as input and outputs the list of asset classes or instruments the strategy will trade.

### Docstring

**Summary:** Enumerate asset classes or instruments for the chosen investment strategy.

**Parameters:**

- chosen_investment_strategy (str): The chosen high-level investment strategy
**Returns:** LIST_STR - A list of specific asset classes or instruments that the strategy will trade, with a maximum of ten entries.

**Examples:**

```python
>>> chosen_investment_strategy = 'Long-Short Equity'
>>> asset_classes_instruments = define_asset_universe(chosen_investment_strategy)
['US large-cap equities', 'Euro-dollar futures', 'credit default swaps']
```



---

## define_investor_profile

### Description
Articulates the target investor segment.

### Conceptual Info

This node is responsible for defining the target investor segment, including their characteristics and preferences.

### Docstring

**Summary:** Define the target investor segment for the fund.

**Parameters:**

- fund_objectives (dict): Fund objectives as defined by the `clarify_fund_objectives` node.
**Returns:** dict - Defined investor profile as a dictionary with keys for investor type, ticket size, risk tolerance, liquidity preference, and geographic focus.

**Examples:**

```python
>>> define_investor_profile(fund_objectives={
...     'investment_purpose': 'capital appreciation',
...     'target_return_profile': 'high return',
...     'competitive_advantage': 'unique investment strategy',
...     'long_term_vision': 'long-term growth',
...     'other_objectives': 'diversification'"
                "})
{'investor_type': 'family offices', 'ticket_size': 1000000, 'risk_tolerance': 0.7, 'liquidity_preference': 'medium', 'geographic_focus': 'global'}
```



---

## define_technology_stack

### Description
Specifies the software and infrastructure needed to support operations.

### Conceptual Info

This node specifies the software and infrastructure needed to support operations.

### Docstring

**Summary:** This node takes a workflow with operation steps and specifies the technology components required for each step to create the final technology stack.

**Parameters:**

- workflow (List[str]): List of operation steps in the workflow
**Returns:** Tuple[List[str], List[str], str] - A tuple containing the list of operation steps, list of technology components, and the final technology stack

**Examples:**

```python
>>> ops_steps = ['Step 1', 'Step 2', 'Step 3']
>>> tech_components = []
>>> def define_technology_stack(workflow):
...     for op in workflow:
...         tech_components.append('Component 1')
...     return ops_steps, tech_components, ','.join(tech_components)
(['Step 1', 'Step 2', 'Step 3'], ['Component 1', 'Component 1', 'Component 1'], 'Component 1,Component 1,Component 1')
```

```python
>>> ops_steps = ['Step 4', 'Step 5', 'Step 6']
>>> tech_components = []
>>> def define_technology_stack(workflow):
...     for op in workflow:
...         tech_components.append('Component 2')
...     return ops_steps, tech_components, ','.join(tech_components)
(['Step 4', 'Step 5', 'Step 6'], ['Component 2', 'Component 2', 'Component 2'], 'Component 2,Component 2,Component 2')
```



---

## design_compliance_program

### Description
Creates the quantitative and qualitative risk control architecture.

### Conceptual Info

Generates the risk control architecture aligned with regulations and risk targets.

### Docstring

**Summary:** Creates the risk control architecture by implementing core risk controls and systems.

**Returns:** {risk_control_1: str, risk_control_2: str, risk_control_3: str, risk_control_4: str, risk_control_5: str, risk_control_6: str} - The implemented risk control architecture as a dictionary with keys: risk_control_1, risk_control_2, risk_control_3, risk_control_4, risk_control_5, risk_control_6, corresponding to the implemented risk controls.

**Raises:**

- RuntimeError: If any required risk control or system is not implemented.
**Examples:**

```python
>>> risk_controls = design_risk_management_framework(set_performance_and_risk_targets()).values
>>> print(risk_controls)
{'risk_control_1': 'position limits', 'risk_control_2': 'VaR caps', 'risk_control_3': 'stop-loss levels', 'risk_control_4': 'liquidity thresholds'}
```



---

## design_risk_management_framework

### Description
Creates the quantitative and qualitative risk control architecture.

### Conceptual Info

Designs a risk control architecture that aligns with the performance and risk targets, including position limits, VaR caps, stop-loss levels, and liquidity thresholds.

### Docstring

**Summary:** Designs a risk control architecture based on the performance and risk targets.

**Examples:**

```python
>>> risk_control_architecture = design_risk_management_framework(set_performance_and_risk_targets())
>>> print(risk_control_architecture['risk_control_1'])
position limits
```



---

## develop_timeline_and_milestones

### Description
Creates a phased schedule leading to fund launch.

### Conceptual Info

This node develops a phased schedule leading to fund launch, which is critical for the successful deployment of the hedge fund.

### Docstring

**Summary:** This function constructs a 12-month launch timeline with monthly milestones.

**Parameters:**

- inputs (dict): A dictionary containing 'draft_operations_workflow', 'define_technology_stack', 'create_hiring_plan', and 'compile_pitch_deck_outline' outputs.
**Returns:** dict - A dictionary containing 'timeline_months' and 'milestones', representing a phased schedule leading to fund launch.

**Raises:**

- ValueError: If inputs are missing required outputs.
**Examples:**

```python
>>> from datetime import datetime
>>> from tabulate import tabulate
>>> from typing import Dict, List, Union
>>> def develop_timeline_and_milestones(inputs: Dict) -> Dict:
...     timeline_months = inputs['draft_operations_workflow']['timeline_months'] + inputs['define_technology_stack']['timeline_months']
...     milestones = [f"Legal Formation" for _ in range(3)] + [f"Regulatory Filings" for _ in range(2)] + [f"Service Provider Contracts" for _ in range(2)] + [f"Tech Deployment" for _ in range(2)] + [f"Capital Raise" for _ in range(1)] + [f"First Trade" for _ in range(1)]
...     return {'timeline_months': timeline_months, 'milestones': milestones}
>>> result = develop_timeline_and_milestones({'draft_operations_workflow': {'timeline_months': [1, 2, 3]}, 'define_technology_stack': {'timeline_months': [4, 5, 6]}})
{'timeline_months': [1, 2, 3, 4, 5, 6], 'milestones': ['Legal Formation', 'Legal Formation', 'Legal Formation', 'Regulatory Filings', 'Regulatory Filings', 'Service Provider Contracts', 'Service Provider Contracts', 'Tech Deployment', 'Tech Deployment', 'Capital Raise', 'First Trade']}
```



---

## draft_fee_structure

### Description
Sets the fund's fee schedule by defining management fees, performance fees, hurdle rate, and fee payment structures to optimize revenue while remaining competitive.

### Conceptual Info

This node establishes the fund's fee schedule, balancing revenue needs with market competitiveness by setting management and performance fee percentages, incorporating hurdle rates if applicable, and detailing the payment structures.

### Docstring

**Summary:** Define the management and performance fee percentages, hurdle rate, and fee structures for the fund, considering market standards and internal cost recovery goals.

**Parameters:**

- set_performance_and_risk_targets (dict): Outputs from the parent node defining risk and performance targets, influencing fee structure decisions.
- estimate_setup_and_operating_costs (dict): Outputs from the parent node estimating annual setup and operating costs that need to be covered by fund fees.
**Returns:** dict - A dictionary containing the 'management_fees', 'performance_fees', 'hurdle_rate', and 'fee_schedules' as string descriptions of the fee arrangements.

**Raises:**

- ValueError: If fee components are missing or ill-formatted, indicating incomplete or inconsistent inputs.
**Examples:**

```python
>>> draft_fee_structure()
>>> # Management fees: '2%', Performance fees: '20%', Hurdle rate: '5%', Payment structure: 'Standard tiered fees'
{'management_fees': '2%', 'performance_fees': '20%', 'hurdle_rate': '5%', 'fee_schedules': 'Standard tiered fees'}
```

```python
>>> draft_fee_structure()
>>> # Management fees: '1.5%', Performance fees: '15%', Hurdle rate: 'None', Payment structure: 'High-water mark with clawback'
{'management_fees': '1.5%', 'performance_fees': '15%', 'hurdle_rate': 'None', 'fee_schedules': 'High-water mark with clawback'}
```



---

## draft_operations_workflow

### Description
Maps core trade and post-trade operational steps, outlining each stage in the trade lifecycle and assigning responsibility to internal teams or external service providers.

### Conceptual Info

This node details the sequence of core operational steps involved in executing a trade on a daily basis, including responsible parties at each stage.

### Docstring

**Summary:** Maps and outlines the end-to-end daily trading and post-trade workflow, specifying operational steps and responsible entities.

**Parameters:**

- define_asset_universe (list of str): Predefined list of tradable assets and instruments used to inform operational procedures.
- list_service_providers (list of str): Identifies external service providers involved in trade lifecycle steps.
- design_risk_management_framework (list of str): Framework outlining risk controls influencing operational workflows.
**Returns:** dict - Dictionary with 'tradelifecycle_steps' (list of trade steps) and 'responsible_parties' (respective responsible entities).

**Raises:**

- ValueError: If required dependencies are missing or contain invalid data.
**Examples:**

```python
>>> draft_operations_workflow()
{tradelifecycle_steps: [Idea Generation, Order Creation, Execution, Confirmation, Settlement, Reconciliation], responsible_parties: [Internal Research Team, Trading Desk, Broker Provider, Clearinghouse, Internal Operations, Compliance and Risk Team]}
```



---

## estimate_setup_and_operating_costs

### Description
Produces a high-level cost model for launch and ongoing operations.

### Conceptual Info

Estimate and summarize costs required for hedge fund operations.

### Docstring

**Summary:** Estimate and summarize costs required for hedge fund operations based on listed service providers and internal overhead categories.

**Parameters:**

- provider_categories_list (str): Output list from 'list_service_providers' node or other relevant data source.
- internal_overhead_categories (str): User-provided list of internal overhead categories.
**Returns:** Dict[str, Union[List[float], float]] - Cost estimates for each service provider category and internal overhead category.

**Raises:**

- ValueError: If 'provider_categories_list' or 'internal_overhead_categories' is invalid or empty.
**Examples:**

```python
>>> provider_categories_list = ['prime broker', 'fund administrator', 'auditor']
>>> internal_overhead_categories = ['office', 'technology', 'staffing']
>>> estimate_setup_and_operating_costs(provider_categories_list, internal_overhead_categories)
{"
              "  'service_provider_costs': [100000, 50000, 20000],"
              "  'internal_overhead_costs': [30000, 20000, 40000]"
              
```



---

## identify_regulatory_requirements

### Description
This node outputs the key regulatory filings and registrations necessary for the specified legal entity and jurisdiction, based on the entity type selected earlier. It helps ensure compliance with relevant regulatory frameworks by identifying mandatory submissions and overseeing authorities.

### Conceptual Info

This node determines the key regulatory obligations for a fund based on its legal structure and jurisdiction, facilitating compliance planning.

### Docstring

**Summary:** Returns the regulatory filings and authorities required for the specified legal entity type and jurisdiction.

**Parameters:**

- entity_type (str): The selected legal entity type for the fund, such as LP, LLC, SICAV.
- jurisdiction (str): The jurisdiction where the fund is established, e.g., Delaware, Cayman, Luxembourg.
**Returns:** Dict[str, List[str]] - A dictionary containing two lists: regulatory requirements and overseeing authorities.

**Raises:**

- ValueError: Raised if the entity type or jurisdiction is invalid or unsupported.
**Examples:**

```python
>>> identify_regulatory_requirements('LP', 'Delaware')
{regulatory_requirements: [Form D Filing, State Business License], regulatory_authorities: [SEC, Delaware Division of Corporations]}
```

```python
>>> identify_regulatory_requirements('SICAV', 'Luxembourg')
{regulatory_requirements: [LuxSE Authorization, COMEX Registration], regulatory_authorities: [Luxembourg Financial Supervisory Authority, Luxembourg Stock Exchange]}
```



---

## list_service_providers

### Description
Identifies required external service providers for establishing and operating a hedge fund, focusing on key categories necessary for compliance and functionality.

### Conceptual Info

This node generates a list of essential external service provider categories required to operate a hedge fund, based on jurisdictional and operational needs.

### Docstring

**Summary:** Creates a list of mandatory third-party service provider categories for hedge fund setup and operation.

**Parameters:**

- jurisdiction (str): The legal jurisdiction selected for the fund, influencing the service provider landscape.
**Returns:** dict - A dictionary containing provider categories and their counts.

**Raises:**

- ValueError: If jurisdiction input is invalid or not provided.
**Examples:**

```python
>>> list_service_providers('Cayman')
{
```



---

## produce_final_fund_plan_summary

### Description
Generates a comprehensive final plan document by integrating key outputs from core planning, compliance, marketing, and operational nodes into a structured executive summary and detailed sections.

### Conceptual Info

This node synthesizes various strategic, operational, compliance, marketing, and structural outputs into an all-encompassing final plan document, providing a comprehensive overview for stakeholders or regulatory review.

### Docstring

**Summary:** Synthesizes prior generated components into a detailed final plan document, including sections on strategy, structure, risk controls, operations, fees, cost model, compliance, staffing, technology, timeline, and fundraising materials.

**Parameters:**

- design_compliance_program_output (dict): Output dictionary from the design_compliance_program node containing compliance details.
- compile_pitch_deck_outline_output (dict): Output dictionary from the compile_pitch_deck_outline node with presentation structure.
- develop_timeline_and_milestones_output (dict): Output dictionary from the develop_timeline_and_milestones node with timeline details.
**Returns:** dict - A structured dictionary containing the final comprehensive plan document and summaries.

**Raises:**

- ValueError: If any of the dependent outputs are missing or malformed.
- RuntimeError: If synthesis process encounters internal errors.
**Examples:**

```python
>>> produce_final_fund_plan_summary()
{final_plan_document: This is a comprehensive final plan for the hedge fund..., executive_summary_bullet_points: [- Strategy focuses on long/short equity..., - Risk controls include VaR caps and position limits., - Technology stack features OMS and risk management systems., - Timeline includes legal formation and initial capital raise., - Fund structure is a Delaware LP with offshore components., - Fees are aligned with industry standards...], fund_structure_details: The fund is organized as a Delaware Limited Partnership..., risk_management_controls: Includes position limits, VaR caps, and stop-loss levels..., operational_steps: Daily operations include order management, execution, and reconciliation., fee_schedule: Management fee of 2%, performance fee of 20%, with a hurdle rate of 8%., cost_model: Annual operating costs estimated at $2 million, covering staff, technology, and compliance., compliance_framework: Aligned with SEC and CFTC requirements, including filings and internal policies., hiring_plan: Initial team includes PM, risk manager, compliance officer, and operations staff., technology_stack: Uses Bloomberg EMS, internal risk engine, and data warehouse., launch_timeline: Legal formation in Month 1, regulatory filings in Month 2, deployment tech in Month 3, capital raise in Month 4., fundraising_materials: A well-structured pitch deck targeting accredited investors and family offices...}
```



---

## select_jurisdiction

### Description
Determines the legal domicile and rationale for the fund based on its objectives and strategic considerations.

### Conceptual Info

This node evaluates and selects an optimal legal domicile for the hedge fund, justified by strategic analysis and jurisdictional pros and cons.

### Docstring

**Summary:** Selects a suitable jurisdiction for the hedge fund based on fund objectives and strategic considerations.

**Parameters:**

- clarify_fund_objectives (dict): The output dictionary from the clarify_fund_objectives node containing core fund objectives.
**Returns:** dict - A dictionary with the selected jurisdiction, its advantages, disadvantages, and accompanying rationale.

**Raises:**

- ValueError: Raised if fund objectives are insufficiently specified or missing necessary details for jurisdiction analysis.
**Examples:**

```python
>>> select_jurisdiction({'investment_purpose': 'Capital growth', 'target_return_profile': '8-12%', 'competitive_advantage': 'Tax efficiency', 'long_term_vision': 'Global expansion', 'other_objectives': 'Liquidity flexibility'})
{'chosen_jurisdiction': 'Cayman', 'advantages': ['Tax neutrality', 'Flexible fund structuring'], 'disadvantages': ['Less investor transparency', 'Perceived regulatory laxity'], 'rationale': 'Cayman aligns with objectives due to tax benefits and flexible legal frameworks suited for offshore structures.'}
```

```python
>>> select_jurisdiction({'investment_purpose': 'Stable income', 'target_return_profile': '6-10%', 'competitive_advantage': 'Robust regulation', 'long_term_vision': 'Regional focus', 'other_objectives': 'Liquidity retention'})
{'chosen_jurisdiction': 'Delaware', 'advantages': ['Solid legal precedent', 'Familiar regulatory environment'], 'disadvantages': ['Taxation on fund offshore', 'Less favorable for non-US investors'], 'rationale': 'Delaware is chosen for its well-established legal system and familiarity in US-based funds.'}
```



---

## set_performance_and_risk_targets

### Description
This node specifies the quantitative performance and risk targets for the hedge fund strategy, translating high-level objectives into numerical goals. It outputs key metrics like expected returns, volatility, Sharpe ratio, and maximum drawdown, based on the selected investment strategy.

### Conceptual Info

This node captures the specific numerical goals for the fund's performance, aligning strategy with measurable targets to guide risk management and performance assessment.

### Docstring

**Summary:** Defines numerical performance and risk targets for the hedge fund strategy, outputting key metrics such as expected return, volatility, Sharpe ratio, and max drawdown.

**Parameters:**

- annual_gross_return (float): The targeted annual gross return for the strategy, expressed as a percentage.
- annual_volatility (float): The targeted annual volatility (standard deviation) of returns, expressed as a percentage.
- Sharpe_ratio (float): The desired Sharpe ratio, representing risk-adjusted return.
- maximum_drawdown (float): The maximum allowable peak-to-trough loss during the investment period, expressed as a percentage.
**Returns:** dict - A dictionary containing all defined performance and risk metrics, including targets.

**Raises:**

- ValueError: If any of the inputs are out of realistic range or improperly specified.
**Examples:**

```python
>>> set_performance_and_risk_targets(
...     annual_gross_return=15.0,
...     annual_volatility=10.0,
...     Sharpe_ratio=1.5,
...     maximum_drawdown=20.0
>>> )
{'annual_gross_return': 15.0, 'annual_volatility': 10.0, 'Sharpe_ratio': 1.5, 'maximum_drawdown': 20.0, 'performance_targets': [15.0], 'risk_targets': [10.0, 1.5, 20.0]}
```

```python
>>> set_performance_and_risk_targets(
...     annual_gross_return=8.0,
...     annual_volatility=12.0,
...     Sharpe_ratio=0.8,
...     maximum_drawdown=30.0
>>> )
{'annual_gross_return': 8.0, 'annual_volatility': 12.0, 'Sharpe_ratio': 0.8, 'maximum_drawdown': 30.0, 'performance_targets': [8.0], 'risk_targets': [12.0, 0.8, 30.0]}
```

