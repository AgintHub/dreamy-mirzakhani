from pydantic import BaseModel, Field
from typing import List


class OptimizeParametersOutput(BaseModel):
    """Pydantic model for optimize_parameters node outputs."""
    top3_parameters: List[str] = (
        Field(..., description="String representations of the top 3 parameter combinations, formatted as key=value pairs separated by commas")
    )
    top3_sharpe: List[float] = (
        Field(..., description="Sharpe ratio values corresponding to each of the top 3 parameter sets")
    )
    top3_drawdown: List[float] = (
        Field(..., description="Maximum drawdown percentages corresponding to each of the top 3 parameter sets")
    )
    top3_return: List[float] = (
        Field(..., description="Total return percentages corresponding to each of the top 3 parameter sets")
    )


class ImplementSlippageModelOutput(BaseModel):
    """Pydantic model for implement_slippage_model node outputs."""
    bid_ask_spread_percent: float = (
        Field(..., description="Estimated average bid\u2011ask spread as a percentage of price")
    )
    price_impact_coefficient: float = (
        Field(..., description="Coefficient representing price impact per unit of trade size")
    )
    time_slippage_decay_factor: float = (
        Field(..., description="Decay factor for slippage over time during execution")
    )


class SetBacktestParametersOutput(BaseModel):
    """Pydantic model for set_backtest_parameters node outputs."""
    in_sample_start: str = (
        Field(..., description="Start date of the in-sample period (YYYY-MM-DD)")
    )
    in_sample_end: str = (
        Field(..., description="End date of the in-sample period (YYYY-MM-DD)")
    )
    out_sample_start: str = (
        Field(..., description="Start date of the out-of-sample period (YYYY-MM-DD)")
    )
    out_sample_end: str = (
        Field(..., description="End date of the out-of-sample period (YYYY-MM-DD)")
    )
    montecarlo_min: int = (
        Field(..., description="Minimum number of Monte Carlo simulations to run")
    )
    montecarlo_max: int = (
        Field(..., description="Maximum number of Monte Carlo simulations to run")
    )
    walkforward_window_days: List[int] = (
        Field(..., description="List of window sizes (in days) for walk-forward analysis")
    )


class DeployAutomatedBacktestOutput(BaseModel):
    """Pydantic model for deploy_automated_backtest node outputs."""
    docker_image_name: str = (
        Field(..., description="Name of the built Docker image for the automated backtesting pipeline")
    )
    ci_cd_yaml_generated: bool = (
        Field(..., description="Whether the CI/CD deployment YAML file was successfully generated")
    )
    backtest_run_log: str = (
        Field(..., description="Path or content reference to the most recent backtest run log file")
    )
    parameter_optimization_status: bool = (
        Field(..., description="Indicates if the latest parameter optimization cycle completed without errors")
    )
    compliance_report_path: str = (
        Field(..., description="File path to the generated compliance-ready report for the latest run")
    )


def deploy_automated_backtest(optimize_parameters_input: OptimizeParametersOutput, implement_slippage_model_input: ImplementSlippageModelOutput, set_backtest_parameters_input: SetBacktestParametersOutput, **kwargs) -> DeployAutomatedBacktestOutput:
    """
    Creates a Docker container for automated backtesting pipeline.

    Parameters
    ----------
    backtest_parameters : dict
        Backtest parameters including in-sample and out-of-sample periods,
        Monte Carlo simulations, and walk-forward analysis schedule
    optimized_parameters : list
        Top 3 parameter sets with their metrics from the optimization
        process
    slippage_model : dict
        Slippage model parameters including bid-ask spread, price impact
        coefficient, and time slippage decay factor

    Returns
    -------
    dict
        Dictionary containing the Docker image name, CI/CD YAML generation
        status, backtest run log path, parameter optimization status, and
        compliance report path

    Raises
    ------
    ValueError
        If backtest parameters are invalid or missing
    RuntimeError
        If Docker image build or CI/CD YAML generation fails

    Examples
    --------
    >>> deploy_automated_backtest(backtest_parameters={'in_sample_start':
    '2020-01-01', 'out_sample_start': '2021-01-01'},
    ...                           optimized_parameters=[{'param1': 0.1,
    'param2': 0.2}, {'param1': 0.3, 'param2': 0.4}],
    ...                           slippage_model={'bid_ask_spread_percent':
    0.05, 'price_impact_coefficient': 0.01})
    {'docker_image_name': 'automated-backtest-image:latest',
    'ci_cd_yaml_generated': True, 'backtest_run_log': '/path/to/log.txt',
    'parameter_optimization_status': True, 'compliance_report_path':
    '/path/to/report.pdf'}

    """
    return DeployAutomatedBacktestOutput(
        docker_image_name="",
        ci_cd_yaml_generated=False,
        backtest_run_log="",
        parameter_optimization_status=False,
        compliance_report_path="",
    )