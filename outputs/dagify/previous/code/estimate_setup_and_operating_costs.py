from ._estimate_setup_and_operating_costs.validate_input_data import validate_input_data
from ._estimate_setup_and_operating_costs.estimate_provider_costs import estimate_provider_costs
from ._estimate_setup_and_operating_costs.estimate_technology_costs import estimate_technology_costs
from ._estimate_setup_and_operating_costs.estimate_governance_costs import estimate_governance_costs
from ._estimate_setup_and_operating_costs.consolidate_service_names import consolidate_service_names
from ._estimate_setup_and_operating_costs.consolidate_monthly_costs import consolidate_monthly_costs
from ._estimate_setup_and_operating_costs.calculate_annual_costs import calculate_annual_costs
from ._estimate_setup_and_operating_costs.calculate_total_monthly import calculate_total_monthly
from ._estimate_setup_and_operating_costs.calculate_total_annual import calculate_total_annual
from ._estimate_setup_and_operating_costs.count_line_items import count_line_items
from ._estimate_setup_and_operating_costs.generate_budget_overview import generate_budget_overview

from pydantic import BaseModel, Field
from typing import List


class ListServiceProvidersOutput(BaseModel):
    """Pydantic model for list_service_providers node outputs."""
    provider_names: List[str] = (
        Field(..., description = (
            "List of mandatory external service provider names in the order: prime broker, custodian, fund administrator, legal counsel, compliance consultant.")
        )
    )
    provider_functions: List[str] = (
        Field(..., description = (
            "Core function description for each provider, matching the order of provider_names.")
        )
    )


class DefineTechnologyStackOutput(BaseModel):
    """Pydantic model for define_technology_stack node outputs."""
    workflow_stages: List[str] = (
        Field(..., description = (
            "Ordered list of workflow stages (e.g., Idea Generation, Signal Generation, Order Entry, Execution Management, Position Monitoring, Reconciliation, Settlement).")
        )
    )
    technology_solutions: List[str] = (
        Field(..., description = (
            "Corresponding technology solution for each stage (e.g., Data Analytics Platform, Portfolio Management System, OMS, FIX Gateway, Risk Engine, Reconciliation Tool).")
        )
    )
    vendor_in_house_flags: List[bool] = (
        Field(..., description = (
            "Boolean flag for each stage indicating whether the solution is implemented in-house (true) or outsourced to a vendor (false).")
        )
    )


class OutlinerGovernanceStructureOutput(BaseModel):
    """Pydantic model for outliner_governance_structure node outputs."""
    role_names: List[str] = Field(..., description="Names of the roles")
    role_responsibility_1: List[str] = (
        Field(..., description="First responsibility for each role")
    )
    role_responsibility_2: List[str] = (
        Field(..., description="Second responsibility for each role")
    )
    role_responsibility_3: List[str] = (
        Field(..., description="Third responsibility for each role")
    )
    role_authority_scope: List[str] = (
        Field(..., description="Authority scope for each role")
    )


class EstimateSetupAndOperatingCostsOutput(BaseModel):
    """Pydantic model for estimate_setup_and_operating_costs node outputs."""
    service_provider_name: List[str] = (
        Field(..., description = (
            "Names of the service providers or cost categories")
        )
    )
    monthly_cost: List[float] = (
        Field(..., description="Monthly cost in USD for each service provider")
    )
    annual_total: List[float] = (
        Field(..., description = (
            "Annual total cost in USD for each service provider (Monthly Cost \u00d7 12)")
        )
    )
    total_monthly_budget: float = (
        Field(..., description="Sum of all monthly costs across providers")
    )
    total_annual_budget: float = (
        Field(..., description="Sum of all annual totals across providers")
    )
    line_item_count: int = (
        Field(..., description = (
            "Number of line items included in the cost matrix (typically 10\u201115)")
        )
    )
    budget_overview: str = (
        Field(..., description = (
            "Short textual summary of the overall budget, highlighting major cost drivers")
        )
    )


def estimate_setup_and_operating_costs(list_service_providers_input: ListServiceProvidersOutput, define_technology_stack_input: DefineTechnologyStackOutput, outliner_governance_structure_input: OutlinerGovernanceStructureOutput, **kwargs) -> EstimateSetupAndOperatingCostsOutput:
    """
    Generate a cost matrix that aggregates monthly and annual expenditures for
    all service providers, technology implementations, and governance roles.

    Parameters
    ----------
    provider_names : List[str]
        List of mandatory external service provider names in the order:
        prime broker, custodian, fund administrator, legal counsel,
        compliance consultant.
    provider_functions : List[str]
        Core function description for each provider, matching the order of
        provider_names.
    workflow_stages : List[str]
        Ordered list of operational stages (e.g., Idea Generation, Signal
        Generation, Order Entry, Execution Management, Position Monitoring,
        Reconciliation, Settlement).
    technology_solutions : List[str]
        Corresponding technology solution for each workflow stage.
    vendor_in_house_flags : List[bool]
        Boolean flag for each stage indicating whether the solution is
        implemented in‑house (True) or outsourced to a vendor (False).
    role_names : List[str]
        Names of internal governance roles.
    role_responsibility_1 : List[str]
        First responsibility for each role.
    role_responsibility_2 : List[str]
        Second responsibility for each role.
    role_responsibility_3 : List[str]
        Third responsibility for each role.
    role_authority_scope : List[str]
        Authority scope for each role.

    Returns
    -------
    Dict[str, Union[List[str], List[float], float, int]]
        A dictionary containing the cost matrix, totals, line item count,
        and budget overview.

    Raises
    ------
    ValueError
        Raised if any of the input lists have mismatched lengths.
    TypeError
        Raised if inputs are not of the expected types.

    Examples
    --------
    >>> provider_names = ["Prime Broker", "Custodian", "Fund Admin", "Legal
    Counsel", "Compliance Consultant"],
    >>> provider_functions = ["Trade execution and clearing", "Asset
    safekeeping", "NAV calculation and reporting", "Legal advice", "AML & KYC
    oversight"],
    >>> workflow_stages = ["Idea Generation", "Signal Generation", "Order
    Entry", "Execution Management", "Position Monitoring", "Reconciliation",
    "Settlement"],
    >>> technology_solutions = ["Data Analytics", "Portfolio Mgmt", "OMS", "FIX
    Gateway", "Risk Engine", "Reconciliation Tool", "Settlement System"],
    >>> vendor_in_house_flags = [True, True, False, False, True, False, False],
    >>> role_names = ["GP", "Investment Manager", "Compliance Officer", "Chief
    Risk Officer", "Chief Operating Officer"],
    >>> role_responsibility_1 = ["Set investment mandate", "Develop strategies",
    "Ensure regulatory compliance", "Define risk limits", "Oversee operations"],
    >>> role_responsibility_2 = ["Allocate capital", "Monitor performance",
    "Review AML policies", "Approve risk models", "Manage budgets"],
    >>> role_responsibility_3 = ["Stakeholder communication", "Approve trades",
    "Report violations", "Maintain risk register", "Coordinate vendors"],
    >>> role_authority_scope = ["Full authority", "Decision authority on
    trades", "Legal & compliance decisions", "Risk approval", "Operational
    decisions"],
    >>> budget = estimate_setup_and_operating_costs(provider_names,
    provider_functions, workflow_stages, technology_solutions,
    vendor_in_house_flags, role_names, role_responsibility_1,
    role_responsibility_2, role_responsibility_3, role_authority_scope)
    {\n  "service_provider_name": ["Prime Broker", "Custodian", "Fund Admin",
    "Legal Counsel", "Compliance Consultant", "Data Analytics", "Portfolio
    Mgmt", "OMS", "FIX Gateway", "Risk Engine", "Reconciliation Tool",
    "Settlement System"],\n  "monthly_cost": [12000.0, 8000.0, 5000.0, 3000.0,
    2500.0, 4000.0, 3500.0, 6000.0, 2000.0, 4500.0, 3000.0, 2500.0],\n
    "annual_total": [144000.0, 96000.0, 60000.0, 36000.0, 30000.0, 48000.0,
    42000.0, 72000.0, 24000.0, 54000.0, 36000.0, 30000.0],\n
    "total_monthly_budget": 52000.0,\n  "total_annual_budget": 624000.0,\n
    "line_item_count": 12,\n  "budget_overview": "The annual budget totals
    $624k, driven primarily by prime broker ($144k), custodial services ($96k),
    and technology implementations such as OMS ($72k)."\n}

    """
    validate_input_data(providers=list_service_providers_input, tech_stack=define_technology_stack_input, governance=outliner_governance_structure_input)
    
    provider_costs: List[float] = estimate_provider_costs(provider_names=list_service_providers_input.provider_names, provider_functions=list_service_providers_input.provider_functions)
    
    technology_costs: List[float] = estimate_technology_costs(workflow_stages=define_technology_stack_input.workflow_stages, technology_solutions=define_technology_stack_input.technology_solutions, vendor_flags=define_technology_stack_input.vendor_in_house_flags)
    
    governance_costs: List[float] = estimate_governance_costs(role_names=outliner_governance_structure_input.role_names, responsibilities=[outliner_governance_structure_input.role_responsibility_1, outliner_governance_structure_input.role_responsibility_2, outliner_governance_structure_input.role_responsibility_3], authority_scopes=outliner_governance_structure_input.role_authority_scope)
    
    all_service_names: List[str] = consolidate_service_names(provider_names=list_service_providers_input.provider_names, technology_names=define_technology_stack_input.technology_solutions, governance_names=outliner_governance_structure_input.role_names)
    
    all_monthly_costs: List[float] = consolidate_monthly_costs(provider_costs=provider_costs, technology_costs=technology_costs, governance_costs=governance_costs)
    
    annual_costs: List[float] = calculate_annual_costs(monthly_costs=all_monthly_costs)
    
    total_monthly: float = calculate_total_monthly(monthly_costs=all_monthly_costs)
    total_annual: float = calculate_total_annual(annual_costs=annual_costs)
    
    line_count: int = count_line_items(service_names=all_service_names)
    
    budget_summary: str = generate_budget_overview(total_annual=total_annual, service_names=all_service_names, annual_costs=annual_costs)
    
    return EstimateSetupAndOperatingCostsOutput(
        service_provider_name=all_service_names,
        monthly_cost=all_monthly_costs,
        annual_total=annual_costs,
        total_monthly_budget=total_monthly,
        total_annual_budget=total_annual,
        line_item_count=line_count,
        budget_overview=budget_summary
    )