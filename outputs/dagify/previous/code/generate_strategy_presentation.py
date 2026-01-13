from pydantic import BaseModel, Field
from typing import List


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


class GenerateStrategyPresentationOutput(BaseModel):
    """Pydantic model for generate_strategy_presentation node outputs."""
    slide_titles: List[str] = (
        Field(..., description="List of titles for each of the 12 slides in presentation order")
    )
    slide_contents: List[str] = (
        Field(..., description="Brief text content or bullet points for each slide corresponding to slide_titles")
    )
    equity_curve_image_path: str = (
        Field(..., description="File path or URL to the equity curve visualization image")
    )
    risk_heatmap_image_path: str = (
        Field(..., description="File path or URL to the risk heatmap visualization image")
    )
    presentation_version: str = (
        Field(..., description="Version identifier for the generated presentation")
    )


def generate_strategy_presentation(compile_strategy_documentation_input: CompileStrategyDocumentationOutput, validate_out_of_sample_input: ValidateOutOfSampleOutput, **kwargs) -> GenerateStrategyPresentationOutput:
    """
    Creates a 12-slide presentation summarizing strategy details, performance
    metrics, risk analysis, and implementation roadmap.

    Parameters
    ----------
    strategy_summary : str
        Summary of the strategy, including its objectives and methodology.
    performance_overview : str
        Overview of the strategy's performance, including key metrics such
        as Sharpe ratio, CAGR, and maximum drawdown.
    risk_analysis : str
        Analysis of the strategy's risk profile, including risk heatmaps and
        equity curves.
    implementation_roadmap : str
        Roadmap for implementing the strategy, including key milestones and
        capital requirements.

    Returns
    -------
    {slide_titles: List[str], slide_contents: List[str], equity_curve_image_path: str, risk_heatmap_image_path: str, presentation_version: str}
        A dictionary containing the presentation's slide titles, contents,
        equity curve image path, risk heatmap image path, and presentation
        version.

    Raises
    ------
    ValueError
        If any required input (strategy_summary, performance_overview,
        risk_analysis, implementation_roadmap) is missing or empty.

    Examples
    --------
    >>> generate_strategy_presentation(strategy_summary='Strategy to capture
    momentum in small-cap stocks', performance_overview='Sharpe ratio: 1.2,
    CAGR: 15%', risk_analysis='Risk heatmap and equity curve visualizations',
    implementation_roadmap='Implementation within 6 months with $1M capital')
    {'slide_titles': ['Slide 1', 'Slide 2', ...], 'slide_contents': ['Content
    1', 'Content 2', ...], 'equity_curve_image_path':
    '/path/to/equity_curve.png', 'risk_heatmap_image_path':
    '/path/to/risk_heatmap.png', 'presentation_version': 'v1.0'}

    """
    return GenerateStrategyPresentationOutput(
        slide_titles=[],
        slide_contents=[],
        equity_curve_image_path="",
        risk_heatmap_image_path="",
        presentation_version="",
    )