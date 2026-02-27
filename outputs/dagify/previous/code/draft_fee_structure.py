from pydantic import BaseModel, Field
from typing import List


class SetPerformanceAndRiskTargetsOutput(BaseModel):
    """Pydantic model for set_performance_and_risk_targets node outputs."""
    annual_gross_return: float = (
        Field(..., description="Target annual gross return for the chosen strategy")
    )
    annual_volatility: float = (
        Field(..., description="Target annual volatility for the chosen strategy")
    )
    Sharpe_ratio: float = (
        Field(..., description="Target Sharpe ratio for the chosen strategy")
    )
    maximum_drawdown: float = (
        Field(..., description="Target maximum drawdown for the strategy")
    )
    performance_targets: float = (
        Field(..., description="A list of key performance metric targets for the strategy")
    )
    risk_targets: float = (
        Field(..., description="A list of risk metric targets for the strategy")
    )


class EstimateSetupAndOperatingCostsOutput(BaseModel):
    """Pydantic model for estimate_setup_and_operating_costs node outputs."""
    service_provider_costs: List[float] = (
        Field(..., description="Estimated annual costs in USD for each service provider category listed in 'list_service_providers'. The order corresponds to the list of provider categories.")
    )
    internal_overhead_costs: List[float] = (
        Field(..., description="Estimated annual costs in USD for internal overhead categories such as office, technology, staffing, etc., corresponding to internal cost components.")
    )


class DraftFeeStructureOutput(BaseModel):
    """Pydantic model for draft_fee_structure node outputs."""
    management_fees: str = (
        Field(..., description="Management fees percentage or structure")
    )
    performance_fees: str = (
        Field(..., description="Performance fees percentage or structure")
    )
    hurdle_rate: str = (
        Field(..., description="Hurdle rate or other performance targets")
    )
    fee_schedules: str = (
        Field(..., description="List of fee schedules or payment structures")
    )


def draft_fee_structure(set_performance_and_risk_targets_input: SetPerformanceAndRiskTargetsOutput, estimate_setup_and_operating_costs_input: EstimateSetupAndOperatingCostsOutput, **kwargs) -> DraftFeeStructureOutput:
    """
    Define the management and performance fee percentages, hurdle rate, and fee
    structures for the fund, considering market standards and internal cost
    recovery goals.

    Parameters
    ----------
    set_performance_and_risk_targets : dict
        Outputs from the parent node defining risk and performance targets,
        influencing fee structure decisions.
    estimate_setup_and_operating_costs : dict
        Outputs from the parent node estimating annual setup and operating
        costs that need to be covered by fund fees.

    Returns
    -------
    dict
        A dictionary containing the 'management_fees', 'performance_fees',
        'hurdle_rate', and 'fee_schedules' as string descriptions of the fee
        arrangements.

    Raises
    ------
    ValueError
        If fee components are missing or ill-formatted, indicating
        incomplete or inconsistent inputs.

    Examples
    --------
    >>> draft_fee_structure()
    >>> # Management fees: '2%', Performance fees: '20%', Hurdle rate: '5%',
    Payment structure: 'Standard tiered fees'
    {'management_fees': '2%', 'performance_fees': '20%', 'hurdle_rate': '5%',
    'fee_schedules': 'Standard tiered fees'}

    >>> draft_fee_structure()
    >>> # Management fees: '1.5%', Performance fees: '15%', Hurdle rate: 'None',
    Payment structure: 'High-water mark with clawback'
    {'management_fees': '1.5%', 'performance_fees': '15%', 'hurdle_rate':
    'None', 'fee_schedules': 'High-water mark with clawback'}

    """
    return DraftFeeStructureOutput(
        management_fees="",
        performance_fees="",
        hurdle_rate="",
        fee_schedules="",
    )