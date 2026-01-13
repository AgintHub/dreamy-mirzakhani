from pydantic import BaseModel, Field
from typing import List


class DevelopEntryRulesOutput(BaseModel):
    """Pydantic model for develop_entry_rules node outputs."""
    entry_conditions: List[str] = (
        Field(..., description="List of quantitative entry conditions as pseudo\u2011code equations")
    )
    parameter_values: List[float] = (
        Field(..., description="List of specific parameter values for the entry conditions")
    )
    condition_descriptions: List[str] = (
        Field(..., description="Brief description for each entry condition")
    )
    is_valid: bool = (
        Field(..., description="Whether the entry conditions are valid and can be used for initiating positions")
    )


class DevelopExitRulesOutput(BaseModel):
    """Pydantic model for develop_exit_rules node outputs."""
    exit_conditions: List[str] = (
        Field(..., description="List of quantitative exit conditions expressed as pseudo-code equations.")
    )
    parameter_values: List[float] = (
        Field(..., description="Parameter values associated with each exit condition.")
    )
    exit_order_types: List[str] = (
        Field(..., description="Order type for each exit condition (e.g., 'market', 'limit').")
    )
    is_valid: bool = (
        Field(..., description="Whether the generated exit rules satisfy all validation checks.")
    )


class CalculatePositionSizingOutput(BaseModel):
    """Pydantic model for calculate_position_sizing node outputs."""
    risk_per_trade: float = Field(..., description="Risk percentage per trade")
    volatility_scaling_multiple: float = (
        Field(..., description="Volatility scaling multiple")
    )
    maximum_position_size: float = (
        Field(..., description="Maximum position size")
    )
    account_equity_reference: float = (
        Field(..., description="Account equity reference value")
    )
    position_sizing_algorithm: str = (
        Field(..., description="Position sizing algorithm description")
    )


class BuildRiskRulesOutput(BaseModel):
    """Pydantic model for build_risk_rules node outputs."""
    portfolio_volatility_limit: float = (
        Field(..., description="The maximum allowed portfolio volatility")
    )
    sector_concentration_limit: float = (
        Field(..., description="The maximum allowed sector concentration")
    )
    drawdown_trigger_limit: float = (
        Field(..., description="The maximum allowed drawdown trigger")
    )
    position_correlation_limit: float = (
        Field(..., description="The maximum allowed position correlation")
    )
    risk_limit_rules: str = (
        Field(..., description="List of risk limit rules with their thresholds")
    )


class ValidateOutOfSampleOutput(BaseModel):
    """Pydantic model for validate_out_of_sample node outputs."""
    selected_param_set: str = (
        Field(..., description="Identifier of the parameter set used for the out-of-sample test")
    )
    in_sample_sharpe: float = (
        Field(..., description="Sharpe ratio calculated on the in-sample period")
    )
    out_of_sample_sharpe: float = (
        Field(..., description="Sharpe ratio calculated on the out-of-sample period")
    )
    in_sample_max_drawdown: float = (
        Field(..., description="Maximum drawdown percentage on the in-sample period")
    )
    out_of_sample_max_drawdown: float = (
        Field(..., description="Maximum drawdown percentage on the out-of-sample period")
    )
    overfitting_tests_passed: bool = (
        Field(..., description="Boolean results for each of the three statistical overfitting tests (true if passed)")
    )
    overfitting_test_names: str = (
        Field(..., description="Names of the statistical tests performed (e.g., t-test, Diebold-Mariano, etc.)")
    )


class CompileStrategyDocumentationOutput(BaseModel):
    """Pydantic model for compile_strategy_documentation node outputs."""
    manual_file: str = (
        Field(..., description="Path or identifier of the generated PDF strategy manual")
    )
    flowchart_file: str = (
        Field(..., description="Path or identifier of the flowchart image included in the manual")
    )
    parameter_table_file: str = (
        Field(..., description="Path or identifier of the parameter reference table image or embedded table")
    )
    risk_summary_file: str = (
        Field(..., description="Path or identifier of the risk limitation summary document or section")
    )
    compliance_checklist_file: str = (
        Field(..., description="Path or identifier of the regulatory compliance checklist section")
    )
    version: str = (
        Field(..., description="Version identifier of the generated documentation (e.g., 'v1.0')")
    )


def compile_strategy_documentation(develop_entry_rules_input: DevelopEntryRulesOutput, develop_exit_rules_input: DevelopExitRulesOutput, calculate_position_sizing_input: CalculatePositionSizingOutput, build_risk_rules_input: BuildRiskRulesOutput, validate_out_of_sample_input: ValidateOutOfSampleOutput, **kwargs) -> CompileStrategyDocumentationOutput:
    """Create operational and compliance documentation

    Args:
        develop_entry_rules_input: Input from the 'develop_entry_rules' node.
        develop_exit_rules_input: Input from the 'develop_exit_rules' node.
        calculate_position_sizing_input: Input from the 'calculate_position_sizing' node.
        build_risk_rules_input: Input from the 'build_risk_rules' node.
        validate_out_of_sample_input: Input from the 'validate_out_of_sample' node.
        **kwargs: Additional keyword arguments.

    Returns:
        CompileStrategyDocumentationOutput: Object containing outputs for this node.
    """
    # TODO: Implement this function

    # Return stub output with placeholder values
    return CompileStrategyDocumentationOutput(
        manual_file="",
        flowchart_file="",
        parameter_table_file="",
        risk_summary_file="",
        compliance_checklist_file="",
        version="",
    )