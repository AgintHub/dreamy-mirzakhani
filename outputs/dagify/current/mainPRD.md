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

- [outline_governance_structure](#outline_governance_structure)

- [produce_final_fund_plan_summary](#produce_final_fund_plan_summary)

- [select_jurisdiction](#select_jurisdiction)

- [set_performance_and_risk_targets](#set_performance_and_risk_targets)



---

## choose_investment_strategy

### Description
Select primary investment approach and strategy classification

### Conceptual Info

This node selects a primary investment strategy and explains its alignment with the fund's objectives.

### Docstring

**Summary:** Selects a hedge fund strategy and explains its alignment with fund objectives.

**Parameters:**

- investment_objectives (List[str]): List of fund objectives defined in the clarify_fund_objectives node
**Returns:** {chosen_strategy: str, alignment_explanation: str} - A dictionary containing the chosen strategy and its alignment explanation

**Raises:**

- ValueError: If the chosen strategy is not one of the predefined categories
**Examples:**

```python
>>> investment_objectives = ['generate alpha', 'manage risk']
>>> chosen_strategy = 'long/short equity'
>>> alignment_explanation = 'The long/short equity strategy aligns with the objectives by generating alpha through stock selection and managing risk through hedging'
{'chosen_strategy': 'long/short equity', 'alignment_explanation': 'The long/short equity strategy aligns with the objectives by generating alpha through stock selection and managing risk through hedging'}
```



---

## choose_legal_entity_type

### Description
Specify fund structure and legal form

### Conceptual Info

This node determines the appropriate legal structure for a hedge fund based on the previously selected jurisdiction.

### Docstring

**Summary:** Executes the selection of a legal entity type based on the chosen jurisdiction and provides a rationale for the choice.

**Parameters:**

- jurisdiction_name (str): The name of the jurisdiction selected in the previous node.
- rationale_for_jurisdiction (str): The rationale provided for choosing the jurisdiction.
**Returns:** dict - A dictionary containing the chosen legal entity type and the rationale for the selection.

**Raises:**

- ValueError: If the jurisdiction name or rationale is empty.
**Examples:**

```python
>>> choose_legal_entity_type(jurisdiction_name='Cayman Islands', rationale_for_jurisdiction='Tax efficiency and minimal regulatory oversight.')
{'legal_entity_type': 'LP', 'rationale': 'LP structure is suitable for the Cayman Islands due to its flexibility and tax benefits.'}
```



---

## clarify_fund_objectives

### Description
Define the core business and investment objectives for the hedge fund

### Conceptual Info

Generates a concise, bullet‑point list of the hedge fund’s core business and investment objectives, providing a clear foundation for strategy selection, legal structuring, investor targeting, and jurisdiction choice.

### Docstring

**Summary:** Generate a list of up to eight bullet points that capture the hedge fund’s investment purpose, risk/reward expectations, and target market differentiation.

**Parameters:**

- prompt (str): Instruction string that specifies the maximum number of bullets and the focus areas (investment purpose, risk/reward, target market).
**Returns:** List[str] - A list of bullet‑point strings, each describing a distinct business or investment objective.

**Raises:**

- ValueError: Raised if the input prompt is empty or does not contain a clear instruction.
**Examples:**

```python
>>> output = clarify_fund_objectives(prompt)
>>> print(output)
["Generate alpha through a diversified long/short equity strategy.", "Maintain portfolio volatility below 15% annualized.", "Deliver 20% gross annual returns to institutional investors.", "Differentiate by leveraging proprietary quantitative models."]
```

```python
>>> output = clarify_fund_objectives(prompt)
>>> print(len(output))
4
```



---

## compile_pitch_deck_outline

### Description
Generates a concise list of 10 slide titles for an investor pitch deck, pulling key themes from related fund design nodes.

### Conceptual Info

The node consolidates critical fund attributes into a structured slide‑title list, enabling a clear, investor‑focused narrative.

### Docstring

**Summary:** Generate a 10‑slide title list for an investor pitch deck.

**Parameters:**

- investment_objectives (List[str]): Bullet points from clarify_fund_objectives outlining the fund’s purpose, risk/reward, and market differentiation.
- investor_profile_characteristics (List[str]): Four key traits defining the target investor demographic, sourced from define_investor_profile.
- chosen_strategy (str): Primary hedge‑fund strategy selected in choose_investment_strategy.
- alignment_explanation (str): One‑sentence rationale linking the chosen strategy to the fund’s objectives.
- annual_gross_return_target (float): Target gross return (decimal) from set_performance_and_risk_targets.
- volatility_limit_pct (float): Maximum acceptable volatility (percentage) from set_performance_and_risk_targets.
- sharpe_ratio_goal (float): Desired Sharpe ratio from set_performance_and_risk_targets.
- max_drawdown_pct (float): Maximum acceptable drawdown (percentage) from set_performance_and_risk_targets.
- management_fee_percent (float): Management fee percentage (AUM) from draft_fee_structure.
- performance_fee_percent (float): Performance fee percentage (returns) from draft_fee_structure.
- hurdle_rate_percent (float): Hurdle rate percentage from draft_fee_structure.
- control_name (List[str]): Names of quantitative risk controls from design_risk_management_framework.
- control_limit (List[float]): Numerical limits for each risk control.
- roles (List[str]): Five leadership roles from outline_governance_structure.
- duties (List[str]): One‑sentence duty for each leadership role.
**Returns:** List[str] - An ordered list of 10 slide titles.

**Raises:**

- ValueError: If any required input list is empty or contains fewer items than expected.
**Examples:**

```python
>>> slide_titles = compile_pitch_deck_outline(
...     investment_objectives=['Generate alpha through market‑neutral strategies', 'Cap volatility at 12%'],
...     investor_profile_characteristics=['Institutional', 'North America', 'Minimum $10M', 'Medium liquidity'],
...     chosen_strategy='market neutral',
...     alignment_explanation='Aligns with low volatility goal',
...     annual_gross_return_target=0.15,
...     volatility_limit_pct=12.0,
...     sharpe_ratio_goal=1.5,
...     max_drawdown_pct=18.0,
...     management_fee_percent=1.5,
...     performance_fee_percent=20.0,
...     hurdle_rate_percent=5.0,
...     control_name=['VaR limit', 'Position size cap'],
...     control_limit=[1.5, 5.0],
...     roles=['GP', 'CIO', 'CFO', 'Head of Ops', 'Chief Compliance'],
...     duties=['Oversight', 'Strategy', 'Finance', 'Operations', 'Compliance']"
                ")
["1. Fund Objectives & Investment Thesis", "2. Target Investor Profile", "3. Core Investment Strategy", "4. Performance & Risk Targets", "5. Fee & Incentive Structure", "6. Quantitative Risk Controls", "7. Governance & Leadership", "8. Operations & Execution Model", "9. Timeline & Milestones", "10. Closing & Q&A"]
```

```python
>>> slide_titles = compile_pitch_deck_outline(
...     investment_objectives=['Alpha generation', 'Risk‑adjusted returns'],
...     investor_profile_characteristics=['Institutional', 'Europe', 'Minimum $5M', 'High liquidity'],
...     chosen_strategy='global macro',
...     alignment_explanation='Supports alpha generation via macro exposure',
...     annual_gross_return_target=0.18,
...     volatility_limit_pct=15.0,
...     sharpe_ratio_goal=1.8,
...     max_drawdown_pct=20.0,
...     management_fee_percent=2.0,
...     performance_fee_percent=25.0,
...     hurdle_rate_percent=7.0,
...     control_name=['Liquidity threshold'],
...     control_limit=[10.0],
...     roles=['GP', 'CIO', 'CFO', 'Head of Ops', 'Compliance Officer'],
...     duties=['Oversight', 'Strategy', 'Finance', 'Operations', 'Compliance']
>>> )
["1. Fund Objectives & Investment Thesis", "2. Target Investor Profile", "3. Core Investment Strategy", "4. Performance & Risk Targets", "5. Fee & Incentive Structure", "6. Quantitative Risk Controls", "7. Governance & Leadership", "8. Operations & Execution Model", "9. Timeline & Milestones", "10. Closing & Q&A"]
```



---

## create_hiring_plan

### Description
Determine staffing requirements

### Conceptual Info

This node is responsible for determining the staffing requirements for a hedge fund by identifying essential FTE roles and their core responsibilities.

### Docstring

**Summary:** Creates a hiring plan by identifying essential FTE roles and their core responsibilities based on the operations workflow gaps.

**Parameters:**

- operations_workflow (dict): Output from the draft_operations_workflow node
- governance_structure (dict): Output from the outline_governance_structure node
**Returns:** dict - A dictionary containing the essential roles, core responsibilities, and the total number of roles

**Raises:**

- ValueError: If the input operations workflow or governance structure is invalid
**Examples:**

```python
>>> operations_workflow = {'step_sequence': ['idea generation', 'order entry', 'execution'],
...                       'responsible_party': ['investment team', 'trader', 'execution team']}
>>> governance_structure = {'roles': ['GP', 'CIO', 'CFO'], 'duties': ['overall strategy', 'investment decisions', 'financial management']}
>>> hiring_plan = create_hiring_plan(operations_workflow, governance_structure)
>>> print(hiring_plan)
{'essential_roles': ['investment analyst', 'trader', 'execution specialist', 'compliance officer', 'risk manager', 'financial controller', 'operations manager', 'technology specialist'], 'core_responsibilities': ['research and analysis', 'trade execution', 'trade settlement', 'regulatory compliance', 'risk monitoring', 'financial reporting', 'operations management', 'technology support'], 'role_count': 8}
```



---

## define_asset_universe

### Description
Specify tradable asset categories

### Conceptual Info

The node generates a concise list of tradable asset classes that form the hedge fund’s investable universe, aligning with the selected investment strategy.

### Docstring

**Summary:** Generate a list of tradable asset classes for the hedge fund’s investable universe.

**Parameters:**

- chosen_strategy (str): The specific hedge fund strategy selected from the predefined categories (e.g., long/short equity, market neutral, global macro, event-driven, arbitrage).
**Returns:** Dict[str, Union[List[str], int]] - A dictionary containing two keys:

- ``asset_classes``: a list of specific asset classes/instruments that will constitute the investable universe.
- ``number_of_assets``: an integer representing the count of asset classes listed.

**Raises:**

- ValueError: If ``chosen_strategy`` is empty or not one of the supported strategy categories.
**Examples:**

```python
>>> define_asset_universe(chosen_strategy='long/short equity')
{'asset_classes': ['US Equities', 'EU Equities', 'Emerging Market Equities', 'US Equity Options', 'EU Equity Options'], 'number_of_assets': 5}
```

```python
>>> define_asset_universe(chosen_strategy='global macro')
{'asset_classes': ['US Treasuries', 'Eurodollar Futures', 'Gold Futures', 'USD/JPY FX', 'Commodities Futures'], 'number_of_assets': 5}
```



---

## define_investor_profile

### Description
Characterize target investor demographic

### Conceptual Info

The node captures the demographic and financial profile of the intended investor base, ensuring alignment with the fund’s strategic objectives and regulatory constraints.

### Docstring

**Summary:** Generates a concise list of four key traits defining the target investor demographic.

**Parameters:**

- investment_objectives (List[str]): Bullet list of the hedge fund’s primary business objectives, as produced by the `clarify_fund_objectives` node.
**Returns:** Dict[str, List[str]] - Dictionary containing the key‑characteristics list under the key `investor_profile_characteristics`.

**Raises:**

- ValueError: Raised if `investment_objectives` is empty or not a list of strings.
**Examples:**

```python
>>> investment_objectives = [
...     "Generate >12% annual gross return",
...     "Maintain volatility below 12%",
...     "Target institutional investors in North America",
...     "Offer 30‑day liquidity window"
>>> ]
>>> result = define_investor_profile(investment_objectives)
>>> print(result['investor_profile_characteristics'])
["Institutional investors", "North America", "Minimum investment $5M", "30‑day liquidity window"]
```

```python
>>> investment_objectives = ["Focus on macro opportunities", "Target high net worth retail"]
>>> result = define_investor_profile(investment_objectives)
>>> print(result['investor_profile_characteristics'])
["High net worth retail", "Global reach", "Minimum investment $500k", "Monthly liquidity"]
```



---

## define_technology_stack

### Description
Specify required software systems for each operational step identified in the draft_operations_workflow.

### Conceptual Info

The node maps each trade lifecycle step to the specific technology solution that enables its execution, ensuring a coherent and technology‑aligned operational workflow.

### Docstring

**Summary:** Map each operational step to the required technology component.

**Parameters:**

- step_sequence (List[str]): Ordered list of trade lifecycle steps from the draft_operations_workflow node.
- responsible_party (List[str]): Primary responsible party for each step (not used directly but required for context).
- asset_classes (List[str]): List of asset classes/instruments in the investable universe (contextual).
- risk_controls (List[str]): Quantitative risk controls applied to the workflow (contextual).
- service_providers (List[str]): Mandatory third‑party service provider categories required for execution (contextual).
**Returns:** Tuple[List[str], List[str]] - A tuple containing two lists: the first is the ordered step_names, the second is the aligned tech_components.

**Raises:**

- ValueError: Raised if step_sequence is empty or any element is not a string.
- ValueError: Raised if the length of step_sequence does not match the expected number of technology components.
**Examples:**

```python
>>> step_sequence = [
...     'Idea Generation',
...     'Trade Planning',
...     'Order Entry',
...     'Execution',
...     'Trade Confirmation',
...     'Settlement',
...     'Post‑Trade Analytics'
>>> ]
>>> responsible_party = [
...     'Quant Team',
...     'Portfolio Manager',
...     'Trader',
...     'Trader',
...     'Trader',
...     'Operations',
...     'Risk Team'
>>> ]
>>> asset_classes = ['Equities', 'Fixed Income', 'Derivatives']
>>> risk_controls = ['Position Size Cap', 'Daily VaR', 'Liquidity Threshold']
>>> service_providers = ['Prime Broker', 'Custodian', 'Clearer']
>>> step_names, tech_components = define_technology_stack(
...     step_sequence, responsible_party, asset_classes, risk_controls, service_providers)
>>> print(step_names)
>>> print(tech_components)
[['Idea Generation', 'Trade Planning', 'Order Entry', 'Execution', 'Trade Confirmation', 'Settlement', 'Post‑Trade Analytics'], ['Research Portal', 'Portfolio Management System', 'Order Management System', 'Execution Platform', 'Trade Capture System', 'Clearing Service', 'Analytics Dashboard']]
```

```python
>>> # Minimal example with only two steps
>>> step_names, tech_components = define_technology_stack(
...     ['Idea Generation', 'Order Entry'], [], [], [], [])
>>> print(step_names)
>>> print(tech_components)
[['Idea Generation', 'Order Entry'], ['Research Portal', 'Order Management System']]
```



---

## design_compliance_program

### Description
Create regulatory compliance framework

### Conceptual Info

This node creates a regulatory compliance framework by mapping regulatory requirements to internal policies and controls.

### Docstring

**Summary:** Designs a compliance program by mapping regulatory requirements to internal policies and controls.

**Parameters:**

- regulatory_requirements (List[str]): List of regulatory requirements identified for the fund (output from identify_regulatory_requirements node)
- risk_controls (List[str]): List of quantitative risk controls implemented (output from design_risk_management_framework node)
**Returns:** dict - {regulations: List of regulatory requirements, policies_controls: List of corresponding internal policies or controls, entry_count: Total number of regulatory-policy/control entries}

**Raises:**

- ValueError: If the number of regulatory-policy/control entries is not between 7 and 10
**Examples:**

```python
>>> regulatory_requirements = ['SEC Form CFA', 'EFIS', 'AIFM']
>>> risk_controls = ['VaR limits', 'position size caps']
>>> design_compliance_program(regulatory_requirements, risk_controls)
{'regulations': ['SEC Form CFA', 'EFIS', 'AIFM'], 'policies_controls': ['Internal Policy 1', 'Internal Policy 2'], 'entry_count': 7}
```



---

## design_risk_management_framework

### Description
Create risk mitigation mechanism

### Conceptual Info

This node specifies the quantitative risk controls that will govern the hedge fund’s trading activities.  It takes the investment strategy and the performance‑and‑risk targets defined upstream to produce a concise list of control names and their numeric thresholds, enabling downstream nodes to incorporate these limits into the pitch deck, compliance program, and operations workflow.

### Docstring

**Summary:** Generate a list of quantitative risk controls and their numeric limits based on the chosen investment strategy and performance targets.

**Parameters:**

- chosen_strategy (str): The hedge fund strategy selected in the `choose_investment_strategy` node (e.g., "long/short equity", "market neutral", etc.).
- annual_gross_return_target (float): Target annual gross return expressed as a decimal (e.g., 0.12 for 12%).
- volatility_limit_pct (float): Maximum acceptable annual volatility expressed as a percentage (e.g., 15 for 15%).
- sharpe_ratio_goal (float): Desired Sharpe ratio target for the fund.
- max_drawdown_pct (float): Maximum acceptable peak‑to‑trough drawdown expressed as a percentage (e.g., 20 for 20%).
**Returns:** Tuple[List[str], List[float]] - Two lists: control_name and control_limit, each element corresponding by index.

**Raises:**

- ValueError: If any numeric target is negative or out of a realistic range (e.g., VaR > 100%).
- KeyError: If a required input key is missing from the arguments.
**Examples:**

```python
>>> control_name, control_limit = design_risk_management_framework(
...     chosen_strategy="long/short equity",
...     annual_gross_return_target=0.15,
...     volatility_limit_pct=12.0,
...     sharpe_ratio_goal=1.5,
...     max_drawdown_pct=18.0)
>>> ]
"control_name": ["VaR limit", "Position size cap", "Liquidity threshold", "Stop‑loss level"],\n"control_limit": [2.5, 10.0, 5.0, 3.0]
```

```python
>>> control_name, control_limit = design_risk_management_framework(
...     chosen_strategy="market neutral",
...     annual_gross_return_target=0.10,
...     volatility_limit_pct=8.0,
...     sharpe_ratio_goal=1.2,
...     max_drawdown_pct=12.0)
>>> ]
"control_name": ["VaR limit", "Position size cap", "Liquidity threshold"],\n"control_limit": [1.8, 8.0, 4.0]
```



---

## develop_timeline_and_milestones

### Description
Create implementation schedule

### Conceptual Info

This node orchestrates a 12‑month operational timeline, mapping key milestones—regulatory filing, provider onboarding, capital raise, technology rollout, and launch—onto sequential calendar months. It synthesizes information from the pitch‑deck outline, fee structure, cost estimates, and hiring plan to produce a coherent schedule that aligns with the fund’s launch cadence.

### Docstring

**Summary:** Generate a 12‑month implementation roadmap based on prerequisite inputs.

**Parameters:**

- slide_titles (List[str]): Ordered list of slide titles from the pitch deck outline.
- management_fee_percent (float): Management fee percentage from the fee structure.
- performance_fee_percent (float): Performance fee percentage from the fee structure.
- service_provider_cost_usd (float): Annual cost of service providers.
- technology_systems_cost_usd (float): Annual cost of technology systems.
- office_human_infrastructure_cost_usd (float): Annual cost of office and human infrastructure.
- essential_roles (List[str]): List of essential FTE roles from the hiring plan.
- core_responsibilities (List[str]): Core responsibilities for each essential role.
- role_count (int): Total number of essential FTE roles.
**Returns:** Dict[str, List[Union[int, str]]] - A dictionary with keys 'month_numbers', 'milestone_names', and 'milestone_descriptions', each mapping to a list of 12 items.

**Raises:**

- ValueError: If any input list is empty or has mismatched lengths.
- TypeError: If inputs are not of the expected types.
**Examples:**

```python
>>> timeline = develop_timeline_and_milestones(

...     slide_titles=["Objective", "Strategy", "Investor Profile", "Risk Controls", "Fee Model", "Operations", "Governance", "Capital Raise", "Tech Deployment", "Launch"],

...     management_fee_percent=1.5,

...     performance_fee_percent=20.0,

...     service_provider_cost_usd=300000.0,

...     technology_systems_cost_usd=250000.0,

...     office_human_infrastructure_cost_usd=400000.0,

...     essential_roles=["Portfolio Manager", "Compliance Officer", "Operations Lead"],

...     core_responsibilities=["Lead strategy", "Ensure regulatory compliance", "Oversee day‑to‑day ops"],

...     role_count=3

>>> )
{\n  "month_numbers": [1,2,3,4,5,6,7,8,9,10,11,12],\n  "milestone_names": ["Regulatory Filing","Provider Onboarding","Capital Raise","Tech Deployment","Launch","", "", "", "", "", "", ""],\n  "milestone_descriptions": ["File SEC Form 13D with advisors", "Engage prime broker and custodian", "Secure $10M AUM", "Deploy OMS and risk engine", "Go live", "", "", "", "", "", "", ""]}
```



---

## draft_fee_structure

### Description
Define fee model parameters

### Conceptual Info

The draft_fee_structure node calculates the fee schedule for a hedge fund, translating strategic targets and cost assumptions into concrete percentage figures for management and performance fees, optionally incorporating a hurdle rate.

### Docstring

**Summary:** Generate a fee model based on target returns, risk limits, and operating cost estimates.

**Parameters:**

- annual_gross_return_target (float): Target annual gross return expressed as a decimal (e.g., 0.12 for 12%).
- volatility_limit_pct (float): Maximum acceptable annual volatility in percent.
- sharpe_ratio_goal (float): Desired Sharpe ratio target for the fund.
- max_drawdown_pct (float): Maximum acceptable peak‑to‑trough drawdown in percent.
- service_provider_cost_usd (float): Estimated annual cost for all service providers.
- technology_systems_cost_usd (float): Estimated annual cost for all required technology systems.
- office_human_infrastructure_cost_usd (float): Estimated annual cost for office space, hardware, and human infrastructure.
**Returns:** dict - A dictionary containing fee percentages and a brief commentary.

**Raises:**

- ValueError: If any numeric input is negative or missing.
- TypeError: If inputs are not of expected numeric types.
**Examples:**

```python
>>> draft_fee_structure(
...     annual_gross_return_target=0.15,
...     volatility_limit_pct=10,
...     sharpe_ratio_goal=1.5,
...     max_drawdown_pct=15,
...     service_provider_cost_usd=400000,
...     technology_systems_cost_usd=200000,
...     office_human_infrastructure_cost_usd=300000)
>>> )
{
  "management_fee_percent": 1.5,
  "performance_fee_percent": 20.0,
  "hurdle_rate_percent": 5.0,
  "fee_commentary": "A 1.5% AUM management fee and 20% performance fee above a 5% hurdle aligns with the 15% return target and cost structure."
}
```

```python
>>> draft_fee_structure(
...     annual_gross_return_target=0.10,
...     volatility_limit_pct=12,
...     sharpe_ratio_goal=1.0,
...     max_drawdown_pct=20,
...     service_provider_cost_usd=250000,
...     technology_systems_cost_usd=150000,
...     office_human_infrastructure_cost_usd=200000)
>>> )
{
  "management_fee_percent": 1.25,
  "performance_fee_percent": 15.0,
  "hurdle_rate_percent": 0.0,
  "fee_commentary": "A 1.25% AUM fee and 15% performance fee with no hurdle accommodate the 10% return target and operating costs."
}
```



---

## draft_operations_workflow

### Description
Map operational processes

### Conceptual Info

This node compiles a detailed, step‑by‑step operational workflow for a hedge fund, aligning each phase of the trade lifecycle with its primary owner, the asset universe, the risk controls that govern the process, and the essential external service providers needed for execution. The output is a concise, structured representation that can be consumed by downstream staffing, technology, and compliance modules.

### Docstring

**Summary:** Generate a structured trade‑lifecycle workflow table for a hedge fund.

**Parameters:**

- asset_classes (List[str]): Asset classes/instruments that will constitute the investable universe, as returned by the `define_asset_universe` node.
- service_provider_categories (List[str]): Mandatory third‑party service provider categories required for the fund, as returned by the `list_service_providers` node.
- risk_controls (List[Tuple[str, float]]): Quantitative risk controls with their thresholds, as returned by the `design_risk_management_framework` node. Each tuple contains a control name and its numeric limit.
**Returns:** Dict[str, List[str]] - A dictionary containing five keys: `step_sequence`, `responsible_party`, `asset_classes`, `risk_controls`, and `service_providers`. Each value is a list of strings ordered to match the trade lifecycle.

**Raises:**

- ValueError: If any of the input lists are empty or have mismatched lengths.
- TypeError: If an input is not of the expected type.
**Examples:**

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



---

## estimate_setup_and_operating_costs

### Description
Quantify financial resources needed for the hedge fund set‑up by aggregating estimated annual costs for service providers, technology systems, and office/human infrastructure.

### Conceptual Info

This node calculates the annual capital and operating expenditure required to launch the hedge fund, based on the service providers and technology stack identified in prior steps.

### Docstring

**Summary:** Estimate annual costs for service providers, technology systems, and office/human infrastructure.

**Parameters:**

- service_provider_categories (List[str]): List of mandatory service provider categories (e.g., prime broker, custodian, compliance consultant) supplied by the `list_service_providers` node.
- step_names (List[str]): Ordered list of operational steps produced by the `define_technology_stack` node.
- tech_components (List[str]): Ordered list of technology components corresponding to each operational step.
**Returns:** Tuple[float, float, float] - A tuple containing the annual cost estimates for service providers, technology systems, and office/human infrastructure, respectively.

**Raises:**

- ValueError: If any input list is empty or if the lengths of `step_names` and `tech_components` differ.
- TypeError: If any input is not of the expected type.
**Examples:**

```python
>>> service_provider_categories = ["Prime Broker", "Custodian", "Compliance Consultant", "Legal Advisor", "Fund Administrator", "Auditor"]
>>> step_names = ["Idea Generation", "Order Entry", "Execution", "Post‑Trade Processing", "Reporting"]
>>> tech_components = ["Research Platform", "OMS", "Execution System", "Post‑Trade System", "Reporting Suite"]
>>> costs = estimate_setup_and_operating_costs(service_provider_categories, step_names, tech_components)
>>> print(costs)
(225000.0, 180000.0, 125000.0)
```

```python
>>> service_provider_categories = []
>>> step_names = []
>>> tech_components = []
>>> try:
...     estimate_setup_and_operating_costs(service_provider_categories, step_names, tech_components)
>>> except ValueError as e:
...     print(str(e))
Input lists must not be empty.
```



---

## identify_regulatory_requirements

### Description
Lists mandatory compliance obligations for a hedge fund based on the chosen legal entity and jurisdiction.

### Conceptual Info

This node gathers the regulatory filing requirements that must be met by the hedge fund once its legal structure is chosen. The output is a concise, jurisdiction‑specific checklist that downstream compliance and governance modules can map to internal controls.

### Docstring

**Summary:** Generate a list of mandatory regulatory filings for the selected legal entity and jurisdiction.

**Parameters:**

- legal_entity_type (str): The legal entity type chosen for the hedge fund (e.g., LP, LLC, SICAV).
**Returns:** Dict[str, Any] - A dictionary containing the legal entity type and a list of required regulatory filings.

**Raises:**

- ValueError: Raised if the input legal_entity_type is not one of the supported types (LP, LLC, SICAV).
- LookupError: Raised when the jurisdiction‑specific filing data for the given entity type cannot be retrieved.
**Examples:**

```python
>>> output = identify_regulatory_requirements('LLC')
>>> print(output['legal_entity_type'])
>>> print(output['regulatory_filings'])
"LLC\n[\n  'SEC Form 13D',\n  'SEC Form 13G',\n  'EFIS Filing',\n  'AIFM Registration',\n  'FCA FCA 21',\n  'HMRC Fund Registration',\n  'EU UCITS Directive',\n  'FINRA 24-13'\n]"
```

```python
>>> output = identify_regulatory_requirements('SICAV')
>>> print(output['regulatory_filings'])
"[\n  'Luxembourg AIFMD Registration',\n  'Luxembourg Fund Law Filing',\n  'EU UCITS Directive',\n  'FCA FCA 21',\n  'SEC Form N-1A',\n  'SEC Form 13D',\n  'EFIS Filing',\n  'HMRC Fund Registration'\n]"
```



---

## list_service_providers

### Description
Identify required third‑party vendors

### Conceptual Info

Collects a concise list of external vendor categories indispensable for a hedge fund’s operation, ensuring subsequent nodes receive a standardized taxonomy for cost estimation and workflow mapping.

### Docstring

**Summary:** Generate a fixed list of service provider categories needed to launch a hedge fund.

**Parameters:**

- legal_entity_type (str): The legal entity type chosen for the fund (e.g., LP, LLC, SICAV).
**Returns:** dict - Dictionary containing a single key `service_provider_categories` mapped to a list of strings.

**Raises:**

- ValueError: If `legal_entity_type` is empty or not one of the supported types (LP, LLC, SICAV).
**Examples:**

```python
>>> list_service_providers('LP')
{'service_provider_categories': ['Prime Broker', 'Custodian', 'Compliance Consultant', 'Transfer Agent', 'Fund Administrator', 'Legal Counsel', 'Audit Firm', 'IT Service Provider']}
```

```python
>>> list_service_providers('LLC')
{'service_provider_categories': ['Prime Broker', 'Custodian', 'Compliance Consultant', 'Transfer Agent', 'Fund Administrator', 'Legal Counsel', 'Audit Firm', 'IT Service Provider']}
```



---

## outline_governance_structure

### Description
Define the core management and oversight framework for the hedge fund by enumerating five key leadership positions and summarizing each role’s primary duty in a concise statement.

### Conceptual Info

This node establishes the governance skeleton of the hedge fund, mapping the legal entity type to a clear set of leadership roles and their responsibilities. The output feeds into both the pitch deck (to demonstrate institutional credibility) and the hiring plan (to identify staffing requirements).

### Docstring

**Summary:** Generate a list of five leadership roles and a one‑sentence description of each duty for a hedge fund, based on the chosen legal entity type.

**Parameters:**

- legal_entity_type (str): The legal entity type selected in the choose_legal_entity_type node (e.g., LP, LLC, SICAV).
**Returns:** Dict[str, List[str]] - A dictionary with two keys: 'roles', a list of role names, and 'duties', a list of one‑sentence duty statements in the same order.

**Raises:**

- ValueError: Raised if legal_entity_type is not one of the supported types (LP, LLC, SICAV).
- KeyError: Raised if the internal role mapping for the provided entity type is missing.
**Examples:**

```python
>>> output = outline_governance_structure('LP')
{
  "roles": ["General Partner (GP)", "Chief Investment Officer (CIO)", "Chief Financial Officer (CFO)", "Chief Operating Officer (COO)", "Chief Compliance Officer (CCO)"],
  "duties": ["Oversee overall fund strategy and execution.", "Set investment mandates and monitor performance.", "Manage capital structure, budgeting, and reporting.", "Coordinate day‑to‑day operations and technology.", "Ensure regulatory compliance and risk oversight."]
}
```

```python
>>> output = outline_governance_structure('SICAV')
{
  "roles": ["President", "Chief Investment Officer (CIO)", "Chief Financial Officer (CFO)", "Chief Operating Officer (COO)", "Chief Risk Officer (CRO)"],
  "duties": ["Represent the SICAV to regulators and investors.", "Define and monitor investment strategies.", "Oversee financial reporting and capital management.", "Lead operational efficiency and IT governance.", "Develop and enforce risk policies across the fund."]
}
```



---

## produce_final_fund_plan_summary

### Description
Generate consolidated launch document

### Conceptual Info

The produce_final_fund_plan_summary node generates a comprehensive executive summary for a hedge fund launch, synthesizing key information from various parent nodes into a concise document.

### Docstring

**Summary:** Produces a consolidated launch document summarizing fund strategy, structure, risk framework, operational plan, fee model, and timeline.

**Parameters:**

- timeline_milestones (dict): A dictionary containing the 12-month implementation timeline milestones from the develop_timeline_and_milestones node.
- pitch_deck_outline (dict): A dictionary containing the investor pitch deck outline from the compile_pitch_deck_outline node.
- compliance_program (dict): A dictionary containing the regulatory compliance framework from the design_compliance_program node.
**Returns:** dict - A dictionary containing the executive summary bullet points and word count.

**Raises:**

- ValueError: If any of the input dictionaries are missing required keys or have incorrect data types.
**Examples:**

```python
>>> inputs = {
...   'timeline_milestones': ['Milestone 1', 'Milestone 2'],
...   'pitch_deck_outline': ['Slide 1', 'Slide 2'],
...   'compliance_program': ['Regulation 1', 'Regulation 2']
>>> }
>>> output = produce_final_fund_plan_summary(inputs)
{'strategy_bullet_points': [...], 'structure_bullet_points': [...], ...}
```



---

## select_jurisdiction

### Description
Determine optimal fund registration location

### Conceptual Info

Selects the most suitable domicile for the hedge fund based on its business objectives, providing concise justification and a balanced view of benefits and drawbacks.

### Docstring

**Summary:** Chooses a fund domicile and returns a rationale, pros, and cons based on investment objectives.

**Parameters:**

- investment_objectives (List[str]): A list of up to eight bullet points outlining the hedge fund's primary business objectives, covering investment purpose, risk/reward expectations, and target market differentiation.
**Returns:** Dict[str, Any] - A dictionary containing the chosen jurisdiction name, a one‑sentence rationale, two pros, and two cons.

**Raises:**

- ValueError: If `investment_objectives` is empty or None.
**Examples:**

```python
>>> investment_objectives = [
...     "Generate high risk‑adjusted returns via long/short equity",
...     "Maintain volatility below 12%",
...     "Target institutional investors in North America"
>>> ]
>>> result = select_jurisdiction(investment_objectives)
{
  "jurisdiction_name": "Cayman Islands",
  "rationale": "The Cayman Islands provide a flexible regulatory environment and tax neutrality that align with the fund's high‑return, low‑volatility strategy.",
  "pros": ["Tax‑free jurisdiction", "Well‑established legal framework for funds"],
  "cons": ["Limited investor protection compared to EU jurisdictions", "Higher compliance costs for certain regulatory filings"]
}
```

```python
>>> investment_objectives = [
...     "Focus on global macro opportunities",
...     "Cap volatility at 15%",
...     "Target both institutional and accredited retail investors"
>>> ]
>>> result = select_jurisdiction(investment_objectives)
{
  "jurisdiction_name": "Delaware, USA",
  "rationale": "Delaware offers a mature legal system and favorable corporate law for global macro funds seeking a U.S. presence.",
  "pros": ["Strong legal precedent", "Ease of accessing U.S. capital markets"],
  "cons": ["U.S. corporate tax implications", "Mandatory SEC reporting requirements"]
}
```



---

## set_performance_and_risk_targets

### Description
Quantify financial and risk metrics for the hedge fund based on the selected investment strategy.

### Conceptual Info

This node translates the chosen investment strategy into concrete performance and risk benchmarks that guide the fund’s fee structure, risk management, and investor communications.

### Docstring

**Summary:** Generate quantitative performance and risk targets for a hedge fund based on its investment strategy.

**Parameters:**

- chosen_strategy (str): The hedge fund strategy selected in the `choose_investment_strategy` node.
**Returns:** dict - A dictionary containing four float fields: `annual_gross_return_target`, `volatility_limit_pct`, `sharpe_ratio_goal`, and `max_drawdown_pct`.

**Raises:**

- ValueError: If `chosen_strategy` is not one of the supported strategy categories.
**Examples:**

```python
>>> targets = set_performance_and_risk_targets('long/short equity')
>>> print(targets['annual_gross_return_target'])
0.12
```

```python
>>> targets = set_performance_and_risk_targets('global macro')
>>> print(targets['volatility_limit_pct'])
20.0
```

