# calculate_performance_metrics PRD

## Description
Quantify strategy effectiveness


## Conceptual Info

Analyzes strategy performance using metrics like CAGR, Sharpe ratio, and max drawdown. Compares results against defined benchmarks to assess relative effectiveness.

## Docstring

### Summary
Quantify strategy effectiveness through performance metrics and benchmark comparisons

### Parameters

- **strategy_daily_returns** (List[float]): Daily returns of the strategy (from execute_backtesting)
- **strategy_cumulative_returns** (List[float]): Cumulative returns of the strategy (from execute_backtesting)
- **strategy_max_drawdown** (float): Maximum drawdown value from backtest results
- **strategy_number_of_trades** (int): Total executed trades from backtest results
- **benchmark_daily_returns** (List[float]): Daily returns of the benchmark (typically major index)
- **benchmark_cumulative_returns** (List[float]): Cumulative returns of the benchmark
- **benchmark_max_drawdown** (float): Maximum drawdown of the benchmark

### Returns

Dict[str, Union[float, bool]]: Dictionary containing performance metrics and benchmark comparisons

### Raises

- ValueError: If input lists are empty or input types are invalid
- ZeroDivisionError: If benchmark or strategy has zero trades when calculating win rate

### Examples

```python
>>> calculate_performance_metrics(strat_returns=[0.02, -0.01, 0.03], strat_cumulative=[1.02, 1.01, 1.04], strat_max DD=0.05, trades=150, bench_returns=[0.01, 0.005, 0.02], bench_cumulative=[1.01, 1.015, 1.04], bench_max DD=0.08)
{'cagr': 1.183, 'sharpe_ratio': 0.76, ... 'cagr_benchmark': 1.03, 'cagr_outperforms_benchmark': True}
```

```python
>>> calculate_performance_metrics(strat_returns=[], trades=0)
ValueError: Daily returns list cannot be empty
```
