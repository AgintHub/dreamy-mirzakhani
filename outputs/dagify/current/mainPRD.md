# build_quant_strategy - Complete PRD Documentation

## Overview
PRDs for nodes in the 'build_quant_strategy' module.

## Table of Contents

- [analyze_backtest_results](#analyze_backtest_results)

- [build_risk_rules](#build_risk_rules)

- [calculate_position_sizing](#calculate_position_sizing)

- [choose_strategy_approach](#choose_strategy_approach)

- [define_strategy_objective](#define_strategy_objective)

- [deploy_automated_backtest](#deploy_automated_backtest)

- [develop_entry_rules](#develop_entry_rules)

- [develop_exit_rules](#develop_exit_rules)

- [execute_in_sample_backtest](#execute_in_sample_backtest)

- [generate_strategy_presentation](#generate_strategy_presentation)

- [implement_slippage_model](#implement_slippage_model)

- [optimize_parameters](#optimize_parameters)

- [preprocess_data](#preprocess_data)

- [select_data_sources](#select_data_sources)

- [set_backtest_parameters](#set_backtest_parameters)

- [set_performance_benchmarks](#set_performance_benchmarks)

- [validate_out_of_sample](#validate_out_of_sample)



---

## analyze_backtest_results

### Description
Evaluate in‑sample backtest performance against predefined benchmarks, distill key drivers and infractions, and recommend actionable parameter tweaks.

### Conceptual Info

The node aggregates quantitative backtest outcomes and benchmark definitions to surface actionable insights. It transforms raw equity curves, trade‑level PnL, and risk metrics into concise, human‑readable summaries that highlight performance levers and compliance breaches.

### Docstring

**Summary:** Analyze in‑sample backtest results against performance benchmarks and return top drivers, constraint violations, and parameter adjustment recommendations.

**Parameters:**

- equity_curve_dates (List[str]): Sequential dates of the equity curve in YYYY‑MM‑DD format.
- equity_curve_values (List[float]): Equity value for each date in the equity curve.
- drawdown_series (List[float]): Cumulative drawdown percentage at each date.
- trade_ids (List[str]): Unique identifiers for each executed trade.
- trade_pnl (List[float]): Profit or loss for each trade.
- sharpe_ratio (float): Annualized Sharpe ratio of the backtest.
- max_drawdown (float): Maximum drawdown percentage observed during the backtest.
- total_return (float): Total return percentage over the backtest period.
- cagr_target (float): Target CAGR in decimal form (e.g., 0.15 for 15%).
- annual_volatility_constraint (float): Maximum acceptable annual volatility in decimal form.
- drawdown_limit (float): Maximum allowable drawdown expressed as a decimal.
- sharpe_ratio_goal (float): Target Sharpe ratio to be achieved by the strategy.
**Returns:** Dict[str, str] - Dictionary containing the nine output fields specified in the node's output structure.

**Raises:**

- ValueError: Raised if any required input list is empty or contains mismatched lengths.
- RuntimeError: Raised if benchmark comparison fails due to inconsistent data types.
**Examples:**

```python
>>> result = analyze_backtest_results(
...     equity_curve_dates=['2020-01-01', '2020-01-02', '2020-01-03'],
...     equity_curve_values=[100000, 102000, 101500],
...     drawdown_series=[0.0, 0.0, -0.0025],
...     trade_ids=['T1', 'T2'],
...     trade_pnl=[2000, -500],
...     sharpe_ratio=1.5,
...     max_drawdown=0.025,
...     total_return=0.015,
...     cagr_target=0.12,
...     annual_volatility_constraint=0.18,
...     drawdown_limit=0.20,
...     sharpe_ratio_goal=1.4)
>>> print(result['performance_driver_1'])
"Positive correlation with S&P 500"
```

```python
>>> result = analyze_backtest_results(
...     equity_curve_dates=['2020-01-01', '2020-01-02'],
...     equity_curve_values=[100000, 99000],
...     drawdown_series=[0.0, -0.01],
...     trade_ids=['T1'],
...     trade_pnl=[-1000],
...     sharpe_ratio=0.8,
...     max_drawdown=0.01,
...     total_return=-0.01,
...     cagr_target=0.10,
...     annual_volatility_constraint=0.15,
...     drawdown_limit=0.10,
...     sharpe_ratio_goal=1.0)
>>> print(result['constraint_violation_1'])
"Sharpe ratio below target"
```



---

## build_risk_rules

### Description
Create portfolio-level risk controls

### Conceptual Info

This node creates a set of risk limit rules to control portfolio-level risks.

### Docstring

**Summary:** Builds portfolio-level risk controls based on given risk limit rules and thresholds.

**Parameters:**

- performance_benchmarks (dict): Performance benchmarks output from 'set_performance_benchmarks' node
- risk_limit_rules_input (dict): Input dictionary containing risk limit rules and their thresholds
**Returns:** dict - A dictionary containing the portfolio volatility limit, sector concentration limit, drawdown trigger limit, position correlation limit, and a list of risk limit rules with their thresholds

**Raises:**

- ValueError: If the input dictionary is empty or missing required keys
- TypeError: If the input dictionary values are not of the correct type
**Examples:**

```python
>>> performance_benchmarks = {'cagr_target': 0.15, 'annual_volatility_constraint': 0.20, 'drawdown_limit': 0.25, 'sharpe_ratio_goal': 1.5}
>>> risk_limit_rules_input = {'portfolio_volatility': 0.10, 'sector_concentration': 0.30, 'drawdown_trigger': 0.20, 'position_correlation': 0.50}
>>> risk_limits = build_risk_rules(performance_benchmarks, risk_limit_rules_input)
{'portfolio_volatility_limit': 0.10, 'sector_concentration_limit': 0.30, 'drawdown_trigger_limit': 0.20, 'position_correlation_limit': 0.50, 'risk_limit_rules': ['portfolio_volatility: 0.10', 'sector_concentration: 0.30', 'drawdown_trigger: 0.20', 'position_correlation: 0.50']}
```



---

## calculate_position_sizing

### Description
Determine capital allocation logic

### Conceptual Info

This node determines the capital allocation logic for a quant strategy by designing a position sizing algorithm with three rules: risk per trade, volatility scaling, and maximum position size. It also references the account equity in its calculations.

### Docstring

**Summary:** This function calculates the position sizing parameters based on the provided risk per trade, volatility scaling multiple, and maximum position size, while considering the account equity.

**Parameters:**

- cagr_target (float): Target compound annual growth rate
- annual_volatility_constraint (float): Maximum acceptable annual volatility
- drawdown_limit (float): Maximum allowable drawdown
- sharpe_ratio_goal (float): Target Sharpe ratio
**Returns:** dict - A dictionary containing the calculated position sizing parameters: risk per trade, volatility scaling multiple, maximum position size, account equity reference, and position sizing algorithm description.

**Raises:**

- ValueError: If any of the input parameters are invalid or inconsistent.
**Examples:**

```python
>>> calculate_position_sizing(cagr_target=0.15, annual_volatility_constraint=0.20, drawdown_limit=0.25, sharpe_ratio_goal=1.5)
{'risk_per_trade': 0.02, 'volatility_scaling_multiple': 1.5, 'maximum_position_size': 10000.0, 'account_equity_reference': 100000.0, 'position_sizing_algorithm': 'Risk-based position sizing'}
```



---

## choose_strategy_approach

### Description
Select trading methodology framework

### Conceptual Info

This node maps a high‑level strategy objective to a concrete methodological framework, providing justification and technical rationale that guides downstream rule and model design.

### Docstring

**Summary:** Selects the trading methodology (rule‑based, machine‑learning, or hybrid) that best fits the strategy objective.

**Parameters:**

- strategy_sentence (str): One‑sentence statement of the strategy’s objective, e.g., 'Capture momentum in small‑cap stocks with <3% daily volatility'.
- cagr_target (float): Target Compound Annual Growth Rate expressed as a decimal (e.g., 0.15).
- annual_vol_target (float): Maximum acceptable annual volatility expressed as a decimal (e.g., 0.20).
- max_drawdown (float): Maximum drawdown limit expressed as a decimal (e.g., 0.25).
- sharpe_goal (float): Target Sharpe ratio to be achieved.
**Returns:** dict - Dictionary containing `methodology`, `justifications`, and `technical_reasons` as described in the output structure.

**Raises:**

- ValueError: Raised if any required input is missing or of incorrect type.
**Examples:**

```python
>>> result = choose_strategy_approach(
...     strategy_sentence='Capture momentum in small-cap stocks with <3% daily volatility',
...     cagr_target=0.15,
...     annual_vol_target=0.20,
...     max_drawdown=0.25,
...     sharpe_goal=1.5)
>>> print(result['methodology'])
>>> print(result['justifications'])
>>> print(result['technical_reasons'])
```
methodology: 'rule-based'
justifications: ['Momentum signals are well captured by trend-following rules.', 'Requires minimal computational overhead for high-frequency execution.']
technical_reasons: ['Historical data is abundant and clean.', 'Model interpretability is critical for regulatory compliance.', 'Low latency execution is achievable with rule-based logic.']
```
```

```python
>>> result = choose_strategy_approach(
...     strategy_sentence='Generate alpha from mean-reversion patterns in high-volatility futures',
...     cagr_target=0.20,
...     annual_vol_target=0.35,
...     max_drawdown=0.30,
...     sharpe_goal=2.0)
>>> print(result['methodology'])
```
methodology: 'machine-learning'
```
```



---

## define_strategy_objective

### Description
Establish the core goal of the quant strategy

### Conceptual Info

The `define_strategy_objective` node crystallises the high‑level ambition of the quant strategy into a single, unambiguous sentence and binds it to explicit quantitative performance and risk targets. This declaration serves as the foundation for downstream decisions on methodology, risk controls, position sizing, and backtesting parameters.

### Docstring

**Summary:** Create a one‑sentence objective and associated quantitative benchmarks for a quantitative trading strategy.

**Parameters:**

- objective_description (str): Free‑text description of the intended trading goal (e.g., "Capture momentum in small‑cap stocks with <3% daily volatility").
- cagr_target (float): Desired Compound Annual Growth Rate expressed as a decimal (e.g., 0.15 for 15%).
- annual_vol_target (float): Maximum acceptable annual volatility expressed as a decimal (e.g., 0.20 for 20%).
- max_drawdown (float): Maximum acceptable drawdown expressed as a decimal (e.g., 0.25 for 25%).
- sharpe_goal (float): Target Sharpe ratio to be achieved by the strategy.
**Returns:** dict - Dictionary containing the objective sentence and all benchmark values.

**Raises:**

- ValueError: Raised if any numeric benchmark is not within a realistic range (e.g., CAGR < 0 or > 1).
- TypeError: Raised if input types do not match the expected types.
**Examples:**

```python
>>> output = define_strategy_objective(

...     objective_description='Capture momentum in small‑cap stocks with <3%% daily volatility',

...     cagr_target=0.15,

...     annual_vol_target=0.20,

...     max_drawdown=0.25,

...     sharpe_goal=1.5

>>> )
{
  'strategy_sentence': 'Capture momentum in small‑cap stocks with <3% daily volatility',
  'cagr_target': 0.15,
  'annual_vol_target': 0.20,
  'max_drawdown': 0.25,
  'sharpe_goal': 1.5
}
```

```python
>>> # Invalid CAGR triggers ValueError

>>> try:

...     define_strategy_objective(

...         objective_description='Long‑term growth strategy',

...         cagr_target=-0.05,

...         annual_vol_target=0.15,

...         max_drawdown=0.2,

...         sharpe_goal=1.2

...     )

>>> except ValueError as e:

...     print(e)
"CAGR target must be between 0 and 1. Received: -0.05"
```



---

## deploy_automated_backtest

### Description
Implement continuous evaluation framework

### Conceptual Info

This node sets up a continuous evaluation framework by creating a Docker container that automates the backtesting pipeline, including data monitoring, backtest execution, parameter optimization updates, and compliance report generation.

### Docstring

**Summary:** Creates a Docker container for automated backtesting pipeline.

**Parameters:**

- backtest_parameters (dict): Backtest parameters including in-sample and out-of-sample periods, Monte Carlo simulations, and walk-forward analysis schedule
- optimized_parameters (list): Top 3 parameter sets with their metrics from the optimization process
- slippage_model (dict): Slippage model parameters including bid-ask spread, price impact coefficient, and time slippage decay factor
**Returns:** dict - Dictionary containing the Docker image name, CI/CD YAML generation status, backtest run log path, parameter optimization status, and compliance report path

**Raises:**

- ValueError: If backtest parameters are invalid or missing
- RuntimeError: If Docker image build or CI/CD YAML generation fails
**Examples:**

```python
>>> deploy_automated_backtest(backtest_parameters={'in_sample_start': '2020-01-01', 'out_sample_start': '2021-01-01'},
...                           optimized_parameters=[{'param1': 0.1, 'param2': 0.2}, {'param1': 0.3, 'param2': 0.4}],
...                           slippage_model={'bid_ask_spread_percent': 0.05, 'price_impact_coefficient': 0.01})
{'docker_image_name': 'automated-backtest-image:latest', 'ci_cd_yaml_generated': True, 'backtest_run_log': '/path/to/log.txt', 'parameter_optimization_status': True, 'compliance_report_path': '/path/to/report.pdf'}
```



---

## develop_entry_rules

### Description
Create logic for initiating positions

### Conceptual Info

The `develop_entry_rules` node generates a set of quantitative conditions that trigger the opening of a trade.  It takes the selected strategy framework and the pre‑processed market data as inputs, then outputs a concise list of pseudo‑code expressions, their numeric parameters, human‑readable descriptions, and a validity flag that indicates whether the rules satisfy all internal consistency checks (e.g., no circular dependencies, all required indicators computed).

### Docstring

**Summary:** Generate a list of entry conditions, parameters, descriptions, and a validity flag for a rule‑based trading strategy.

**Parameters:**

- strategy_methodology (str): Chosen strategy framework from `choose_strategy_approach`; one of 'rule-based', 'machine-learning', or 'hybrid'.  Only 'rule-based' and 'hybrid' are supported for explicit pseudo‑code generation.
- preprocessed_data_meta (dict): Metadata dictionary returned by `preprocess_data` indicating available indicators, asset count, and time steps.  The function uses this to validate that required inputs (e.g., EMA, ATR) exist.
**Returns:** dict - Dictionary with keys:
- `entry_conditions`: List[str]
- `parameter_values`: List[float]
- `condition_descriptions`: List[str]
- `is_valid`: bool

**Raises:**

- ValueError: If `strategy_methodology` is not supported or required indicators are missing from `preprocessed_data_meta`.
- TypeError: If input types do not match the expected signatures.
**Examples:**

```python
>>> entry_rules = develop_entry_rules(
...     strategy_methodology='rule-based',
...     preprocessed_data_meta={'indicators': ['EMA20', 'EMA50', 'ATR', 'StdDev2']})
{
  'entry_conditions': [
    'EMA20 > EMA50',
    'Close > EMA20 + 2 * ATR',
    'StdDev2 > 1.5'
  ],
  'parameter_values': [20.0, 50.0, 2.0, 1.5],
  'condition_descriptions': [
    'Short‑term EMA crossing above long‑term EMA',
    'Price breaks above two‑ATR volatility breakout',
    'Standard deviation exceeds 1.5 standard deviations'
  ],
  'is_valid': True
}
```

```python
>>> entry_rules = develop_entry_rules(
...     strategy_methodology='machine-learning',
...     preprocessed_data_meta={'indicators': ['EMA20']})
ValueError: Unsupported strategy_methodology 'machine-learning' for entry rule generation.
```



---

## develop_exit_rules

### Description
Create logic for closing positions

### Conceptual Info

This node generates a set of quantitative exit rules that govern when a trading strategy should close open positions. It takes the chosen strategy framework and pre‑processed market data as inputs, formulates multiple exit conditions using pseudo‑code, assigns realistic parameters, and tags each condition with an order type. The output is a validated list of rules ready for use in backtesting and live execution.

### Docstring

**Summary:** Generate a validated set of quantitative exit rules for a trading strategy.

**Parameters:**

- methodology (str): Strategy framework selected by `choose_strategy_approach` ('rule-based', 'machine-learning', or 'hybrid').
- data_meta (dict): Metadata dictionary from `preprocess_data` (contains asset list, volatility metrics, etc.).
**Returns:** dict - Dictionary containing exit_conditions (List[str]), parameter_values (List[float]), exit_order_types (List[str]), and is_valid (bool).

**Raises:**

- ValueError: If the methodology string is not one of the supported types.
- KeyError: If required keys (e.g., 'ATR', 'volatility') are missing from the data_meta.
**Examples:**

```python
>>> # Assume a rule‑based strategy and pre‑processed data containing 14‑day ATR
>>> rules = develop_exit_rules(methodology='rule-based', data_meta={'ATR_14': 0.012, 'volatility': 0.18})
>>> print(rules['exit_conditions'])
['price <= entry_price * (1 - 0.02 * ATR_14)',
 'price >= entry_price * (1 + 0.03 * ATR_14)',
 'time_in_position >= 10']
```

```python
>>> # Machine‑learning strategy with volatility‑based exit
>>> rules = develop_exit_rules(methodology='machine-learning', data_meta={'volatility': 0.22})
>>> print(rules['exit_order_types'])
['market', 'market', 'limit']
```



---

## execute_in_sample_backtest

### Description
Run strategy against historical data

### Conceptual Info

Executes an in‑sample backtest of a quant strategy by simulating trades on historical data using the previously defined entry/exit rules, position sizing, slippage model, and risk constraints. It produces a daily equity curve, drawdown series, and trade‑level PnL, along with key performance statistics.

### Docstring

**Summary:** Run an in‑sample backtest of the strategy and return performance metrics.

**Parameters:**

- entry_conditions (List[str]): Pseudo‑code expressions defining when to open positions.
- exit_conditions (List[str]): Pseudo‑code expressions defining when to close positions.
- parameter_values (List[float]): Numerical values associated with the entry/exit conditions.
- position_sizing_algo (str): Description or identifier of the position sizing algorithm.
- slippage_params (dict): Dictionary with keys 'bid_ask_spread_percent', 'price_impact_coefficient', 'time_slippage_decay_factor'.
- risk_limits (dict): Risk limits including portfolio volatility, sector concentration, drawdown trigger, and position correlation thresholds.
- backtest_params (dict): Backtest configuration containing in‑sample start/end dates, walk‑forward windows, etc.
- historical_data (numpy.ndarray): 4‑D array of pre‑processed market data (assets × features × time × channels).
**Returns:** dict - Dictionary containing equity curve, drawdown series, trade details, and performance statistics.

**Raises:**

- ValueError: If any required input (e.g., entry_conditions) is missing or empty.
- RuntimeError: If the backtest simulation fails due to insufficient data or internal errors.
**Examples:**

```python
>>> # Example 1: Simple moving‑average crossover strategy
>>> result = execute_in_sample_backtest(
...     entry_conditions=["price > sma_50"],
...     exit_conditions=["price < sma_20"],
...     parameter_values=[50, 20],
...     position_sizing_algo="risk_per_trade_1percent",
...     slippage_params={
...         "bid_ask_spread_percent": 0.1,
...         "price_impact_coefficient": 0.0005,
...         "time_slippage_decay_factor": 0.99
...     },
...     risk_limits={
...         "portfolio_volatility_limit": 0.15,
...         "sector_concentration_limit": 0.4,
...         "drawdown_trigger_limit": 0.2,
...         "position_correlation_limit": 0.7
...     },
...     backtest_params={
...         "in_sample_start": "2020-01-01",
...         "in_sample_end": "2022-12-31"
...     },
...     historical_data=market_array)
>>> # Expected output (excerpt)
>>> result["sharpe_ratio"]  # -> 1.25
>>> result["max_drawdown"]   # -> 0.18
>>> len(result["trade_ids"]) # -> 350
"... (dictionary containing the full backtest report) ..."
```

```python
>>> # Example 2: Strategy with stop‑loss and profit‑target
>>> result = execute_in_sample_backtest(
...     entry_conditions=["rsi < 30"],
...     exit_conditions=["rsi > 70", "price < stop_loss", "price > profit_target"],
...     parameter_values=[30, 70, 0.02, 0.05],
...     position_sizing_algo="volatility_scaling",
...     slippage_params={
...         "bid_ask_spread_percent": 0.2,
...         "price_impact_coefficient": 0.001,
...         "time_slippage_decay_factor": 0.95
...     },
...     risk_limits={
...         "portfolio_volatility_limit": 0.12,
...         "sector_concentration_limit": 0.3,
...         "drawdown_trigger_limit": 0.15,
...         "position_correlation_limit": 0.6
...     },
...     backtest_params={
...         "in_sample_start": "2018-01-01",
...         "in_sample_end": "2020-12-31"
...     },
...     historical_data=market_array)
>>> # Expected output (excerpt)
>>> result["total_return"]   # -> 0.48
>>> result["drawdown_series"][:5] # -> [0.0, -0.02, -0.015, -0.025, -0.02]
"... (dictionary containing the full backtest report) ..."
```



---

## generate_strategy_presentation

### Description
Create executive summary for stakeholders

### Conceptual Info

Generate a comprehensive presentation summarizing the strategy, its performance, risk analysis, and implementation details for stakeholders.

### Docstring

**Summary:** Creates a 12-slide presentation summarizing strategy details, performance metrics, risk analysis, and implementation roadmap.

**Parameters:**

- strategy_summary (str): Summary of the strategy, including its objectives and methodology.
- performance_overview (str): Overview of the strategy's performance, including key metrics such as Sharpe ratio, CAGR, and maximum drawdown.
- risk_analysis (str): Analysis of the strategy's risk profile, including risk heatmaps and equity curves.
- implementation_roadmap (str): Roadmap for implementing the strategy, including key milestones and capital requirements.
**Returns:** {slide_titles: List[str], slide_contents: List[str], equity_curve_image_path: str, risk_heatmap_image_path: str, presentation_version: str} - A dictionary containing the presentation's slide titles, contents, equity curve image path, risk heatmap image path, and presentation version.

**Raises:**

- ValueError: If any required input (strategy_summary, performance_overview, risk_analysis, implementation_roadmap) is missing or empty.
**Examples:**

```python
>>> generate_strategy_presentation(strategy_summary='Strategy to capture momentum in small-cap stocks', performance_overview='Sharpe ratio: 1.2, CAGR: 15%', risk_analysis='Risk heatmap and equity curve visualizations', implementation_roadmap='Implementation within 6 months with $1M capital')
{'slide_titles': ['Slide 1', 'Slide 2', ...], 'slide_contents': ['Content 1', 'Content 2', ...], 'equity_curve_image_path': '/path/to/equity_curve.png', 'risk_heatmap_image_path': '/path/to/risk_heatmap.png', 'presentation_version': 'v1.0'}
```



---

## implement_slippage_model

### Description
Create realistic execution cost framework

### Conceptual Info

Transforms cleaned market data into a quantitative slippage model that estimates execution costs for each trade. The model aggregates liquidity‑aware statistics such as average spread, depth‑adjusted impact, and time‑decay of slippage to provide three key parameters usable by downstream backtesting and live execution modules.

### Docstring

**Summary:** Generate a three‑parameter slippage model from a pre‑processed market data set.

**Parameters:**

- preprocessed_metadata (dict): Dictionary returned by `preprocess_data` containing `array_shape`, `num_assets`, `num_time_steps`, `price_normalized`, `volatility_calculated`, and `data_integrity` flags.
- market_liquidity_stats (dict): Optional dictionary with pre‑computed liquidity statistics (e.g., average spread, average depth, trade size distribution). If omitted, the function will compute these statistics directly from the pre‑processed array.
**Returns:** dict - Dictionary with keys `bid_ask_spread_percent`, `price_impact_coefficient`, and `time_slippage_decay_factor`, each mapped to a float value.

**Raises:**

- ValueError: Raised if `preprocessed_metadata` is missing required keys or if `data_integrity` is False.
- TypeError: Raised if `market_liquidity_stats` contains non‑numeric values.
**Examples:**

```python
>>> # Example 1: Using only pre‑processed metadata
>>> model = implement_slippage_model(preprocessed_metadata={
...     'array_shape': [10, 5, 252, 1],
...     'num_assets': 10,
...     'num_time_steps': 252,
...     'price_normalized': True,
...     'volatility_calculated': True,
...     'data_integrity': True
>>> })
>>> print(model['bid_ask_spread_percent'])
0.0012
```

```python
>>> # Example 2: Providing explicit liquidity statistics
>>> model = implement_slippage_model(preprocessed_metadata={
...     'array_shape': [5, 4, 500, 1],
...     'num_assets': 5,
...     'num_time_steps': 500,
...     'price_normalized': True,
...     'volatility_calculated': True,
...     'data_integrity': True
>>> }, market_liquidity_stats={
...     'avg_spread': 0.0015,
...     'avg_depth': 2000,
...     'avg_trade_size': 1000
>>> })
>>> print(model['price_impact_coefficient'])
0.000003
```



---

## optimize_parameters

### Description
Refine strategy inputs through testing

### Conceptual Info

The optimize_parameters node conducts a Bayesian optimization over a 5‑dimensional space of entry and exit rule parameters. It leverages back‑test results from the analyze_backtest_results node to guide the search and respects risk controls defined elsewhere. The output lists the three best parameter sets along with their Sharpe ratio, maximum drawdown, and total return, enabling downstream nodes to pick a robust configuration.

### Docstring

**Summary:** Execute Bayesian optimization over 5‑dimensional entry/exit rule parameters and return the top 3 configurations with performance metrics.

**Parameters:**

- analysis_results (Dict[str, Any]): Dictionary containing back‑test performance metrics from analyze_backtest_results, typically including 'sharpe_ratio', 'max_drawdown', and 'total_return'.
- risk_limits (Dict[str, float]): Risk control thresholds such as maximum allowed drawdown and volatility constraints. Keys correspond to metric names used in the optimization objective.
- parameter_space (Dict[str, Tuple[float, float]]): Search domain for each of the five parameters. Each key maps to a tuple (min, max) defining the continuous bounds.
- n_iter (int): Number of Bayesian optimization iterations to perform.
**Returns:** Tuple[List[str], List[float], List[float], List[float]] - A tuple containing (top3_parameters, top3_sharpe, top3_drawdown, top3_return). Each list has length three.

**Raises:**

- ValueError: If any required key is missing from analysis_results or parameter_space.
- RuntimeError: If the Bayesian optimizer fails to converge or encounters numerical instability.
**Examples:**

```python
>>> analysis_results = {
...     'sharpe_ratio': 1.2,
...     'max_drawdown': 0.15,
...     'total_return': 0.35
>>> }
>>> risk_limits = {'max_drawdown': 0.2, 'volatility': 0.25}
>>> parameter_space = {
...     'entry_threshold': (0.1, 0.5),
...     'exit_threshold': (0.05, 0.3),
...     'stop_loss': (0.01, 0.05),
...     'take_profit': (0.02, 0.1),
...     'lookback': (10, 60)
>>> }
>>> top3_params, top3_sharpe, top3_dd, top3_ret = optimize_parameters(
...     analysis_results, risk_limits, parameter_space, n_iter=50)
>>> print(top3_params)
>>> print(top3_sharpe)
['entry_threshold=0.34, exit_threshold=0.18, stop_loss=0.025, take_profit=0.06, lookback=30',
 'entry_threshold=0.31, exit_threshold=0.20, stop_loss=0.030, take_profit=0.07, lookback=45',
 'entry_threshold=0.36, exit_threshold=0.16, stop_loss=0.020, take_profit=0.05, lookback=25']
[1.45, 1.42, 1.38]
```



---

## preprocess_data

### Description
Clean and align market data for analysis

### Conceptual Info

Transforms raw market feeds into a structured, feature‑rich 4‑D NumPy array suitable for quantitative modeling.

### Docstring

**Summary:** Preprocesses raw market data by normalizing prices, computing volatility, and aligning OHLCV into a 4‑D NumPy array.

**Parameters:**

- raw_data (dict): Dictionary mapping asset tickers to raw OHLCV time series. Each series is a list of dictionaries with keys ['timestamp', 'open', 'high', 'low', 'close', 'volume'].
- config (dict): Configuration dict containing preprocessing options: 
- `normalization_method` (str): 'minmax' or 'zscore';
- `volatility_window` (int): Number of periods for rolling volatility;
- `alignment_frequency` (str): Desired resampling frequency (e.g., '1h', '1d');
- `features` (List[str]): Features to compute (e.g., ['price', 'volatility', 'returns']);
- `channels` (List[str]): Optional channels such as ['price', 'volume'].
**Returns:** dict - Dictionary containing the processed data and metadata:
- `data`: 4‑D NumPy array of shape [assets, features, time_steps, channels];
- `metadata`: Dict with keys 'array_shape', 'num_assets', 'num_time_steps', 'price_normalized', 'volatility_calculated', 'data_integrity'.

**Raises:**

- ValueError: If any asset has fewer than 2 valid time steps after alignment.
- KeyError: If required OHLCV keys are missing in raw data.
- RuntimeError: If data integrity checks fail (e.g., NaNs remain after imputation).
**Examples:**

```python
>>> raw_data = {
...     'AAPL': [
...         {'timestamp': '2023-01-01T09:30:00', 'open': 150.0, 'high': 152.0, 'low': 149.5, 'close': 151.0, 'volume': 1000000},
...         {'timestamp': '2023-01-01T10:30:00', 'open': 151.0, 'high': 153.0, 'low': 150.0, 'close': 152.5, 'volume': 1200000}
...     ],
...     'MSFT': [
...         {'timestamp': '2023-01-01T09:30:00', 'open': 250.0, 'high': 251.0, 'low': 249.0, 'close': 250.5, 'volume': 800000},
...         {'timestamp': '2023-01-01T10:30:00', 'open': 250.5, 'high': 252.0, 'low': 250.0, 'close': 251.0, 'volume': 900000}
...     ]
>>> }
{
  'data': <4‑D array shape [2, 3, 2, 1]>,
  'metadata': {
    'array_shape': [2, 3, 2, 1],
    'num_assets': 2,
    'num_time_steps': 2,
    'price_normalized': true,
    'volatility_calculated': true,
    'data_integrity': true
  }
}
```

```python
>>> config = {
...   'normalization_method': 'minmax',
...   'volatility_window': 10,
...   'alignment_frequency': '1h',
...   'features': ['price', 'volatility'],
...   'channels': ['price']
>>> }
{
  'data': <4‑D array shape [5, 2, 240, 1]>,
  'metadata': {
    'array_shape': [5, 2, 240, 1],
    'num_assets': 5,
    'num_time_steps': 240,
    'price_normalized': true,
    'volatility_calculated': true,
    'data_integrity': true
  }
}
```



---

## select_data_sources

### Description
Identify high‑quality market data feeds

### Conceptual Info

The node selects and documents the market data feeds that will be ingested into the pipeline. It ensures that each feed meets the time‑range, frequency and data‑type requirements of the strategy, and produces a structured list that downstream nodes (e.g., preprocess_data) can consume.

### Docstring

**Summary:** Selects and validates high‑quality market data sources for a quantitative strategy.

**Parameters:**

- strategy_objective (str): A concise one‑sentence description of the strategy’s goal (e.g., "Capture momentum in small‑cap stocks with <3% daily volatility").
- performance_benchmarks (dict): Benchmark metrics dict with keys 'cagr_target', 'annual_vol_target', 'max_drawdown', 'sharpe_goal' produced by set_performance_benchmarks.
- risk_limits (dict): Risk limits dict with keys 'portfolio_volatility_limit', 'sector_concentration_limit', 'drawdown_trigger_limit', 'position_correlation_limit' produced by build_risk_rules.
- entry_exit_requirements (dict): Entry/exit rule descriptors (e.g., required features such as SMA, ATR, volatility) produced by develop_entry_rules and develop_exit_rules.
**Returns:** tuple - Four lists: source_names (List[str]), time_ranges (List[str]), frequencies (List[str]), source_types (List[str])

**Raises:**

- ValueError: Raised if the strategy objective is empty or missing required fields.
- LookupError: Raised if a requested data source is unavailable or does not satisfy the required frequency/time‑range constraints.
**Examples:**

```python
>>> source_names, time_ranges, frequencies, source_types = select_data_sources(
...     strategy_objective='Capture momentum in small‑cap stocks with <3% daily volatility',
...     performance_benchmarks={
...         'cagr_target': 0.15,
...         'annual_vol_target': 0.20,
...         'max_drawdown': 0.25,
...         'sharpe_goal': 1.2
...     },
...     risk_limits={
...         'portfolio_volatility_limit': 0.15,
...         'sector_concentration_limit': 0.30,
...         'drawdown_trigger_limit': 0.20,
...         'position_correlation_limit': 0.70
...     },
...     entry_exit_requirements={
...         'required_features': ['SMA_50', 'ATR_14', 'volatility'],
...         'data_type': 'OHLCV'
...     }
>>> )
[
  ['Bloomberg', 'YahooFinance', 'AlphaVantage'],
  ['2018-01-01 to 2023-12-31', '2018-01-01 to 2023-12-31', '2018-01-01 to 2023-12-31'],
  ['tick', '1d', '1d'],
  ['tick', 'OHLCV', 'fundamental']
]
```

```python
>>> source_names, time_ranges, frequencies, source_types = select_data_sources(
...     strategy_objective='Mean‑reversion on FX pairs',
...     performance_benchmarks={},
...     risk_limits={},
...     entry_exit_requirements={}
>>> )
[
  ['Reuters', 'Oanda'],
  ['2015-01-01 to 2023-12-31', '2015-01-01 to 2023-12-31'],
  ['1h', 'tick'],
  ['OHLCV', 'tick']
]
```



---

## set_backtest_parameters

### Description
Configure strategy evaluation framework

### Conceptual Info

This node establishes the temporal and stochastic bounds for backtesting a quantitative strategy. It defines the in‑sample and out‑of‑sample windows, the range of Monte Carlo simulation counts, and the schedule for walk‑forward validation. The configuration produced here is consumed by downstream nodes that execute the backtests, optimize parameters, and validate out‑of‑sample performance.

### Docstring

**Summary:** Configure the backtesting framework for a quantitative strategy.

**Parameters:**

- in_sample_start (str): Start date of the in-sample period in 'YYYY-MM-DD' format.
- in_sample_end (str): End date of the in-sample period in 'YYYY-MM-DD' format.
- out_sample_start (str): Start date of the out-of-sample period in 'YYYY-MM-DD' format.
- out_sample_end (str): End date of the out-of-sample period in 'YYYY-MM-DD' format.
- montecarlo_min (int): Minimum number of Monte Carlo simulations to run.
- montecarlo_max (int): Maximum number of Monte Carlo simulations to run.
- walkforward_window_days (List[int]): Sequence of window sizes (in days) for walk‑forward analysis. Each element defines the length of a training window before a test window is applied.
**Returns:** Dict[str, Any] - Dictionary containing the seven configuration fields specified in `output_structure`.

**Raises:**

- ValueError: If any date string is not in ISO format or if `in_sample_end` precedes `in_sample_start`.
- ValueError: If `montecarlo_min` is greater than `montecarlo_max` or if any window size in `walkforward_window_days` is non‑positive.
**Examples:**

```python
>>> config = set_backtest_parameters(
...     in_sample_start='2020-01-01',
...     in_sample_end='2021-12-31',
...     out_sample_start='2022-01-01',
...     out_sample_end='2022-12-31',
...     montecarlo_min=1000,
...     montecarlo_max=5000,
...     walkforward_window_days=[90, 180, 360])
{'in_sample_start': '2020-01-01', 'in_sample_end': '2021-12-31', 'out_sample_start': '2022-01-01', 'out_sample_end': '2022-12-31', 'montecarlo_min': 1000, 'montecarlo_max': 5000, 'walkforward_window_days': [90, 180, 360]}
```

```python
>>> # Invalid example: in_sample_end before start
>>> set_backtest_parameters(
...     in_sample_start='2021-01-01',
...     in_sample_end='2020-12-31',
...     out_sample_start='2021-01-01',
...     out_sample_end='2021-12-31',
...     montecarlo_min=500,
...     montecarlo_max=2000,
...     walkforward_window_days=[30, 60])
ValueError: in_sample_end must be after in_sample_start
```



---

## set_performance_benchmarks

### Description
Define quantifiable success metrics

### Conceptual Info

The node translates a textual specification of performance goals into a structured dictionary of numerical benchmarks. These benchmarks serve as inputs for downstream risk, sizing, and validation modules.

### Docstring

**Summary:** Parse performance benchmark parameters from user input and return a dictionary of numerical metrics.

**Parameters:**

- input_text (str): Raw prompt response containing numeric values for CAGR, volatility, drawdown, and Sharpe ratio. Example: "0.12, 0.18, 0.25, 1.5".
**Returns:** Dict[str, float] - Dictionary with keys 'cagr_target', 'annual_volatility_constraint', 'drawdown_limit', and 'sharpe_ratio_goal', each mapped to a float value.

**Raises:**

- ValueError: If the input cannot be parsed into exactly four numeric values or if any value is out of a reasonable range (e.g., negative CAGR).
- TypeError: If the input is not a string.
**Examples:**

```python
>>> benchmarks = set_performance_benchmarks('0.15, 0.20, 0.25, 1.8')
{'cagr_target': 0.15, 'annual_volatility_constraint': 0.20, 'drawdown_limit': 0.25, 'sharpe_ratio_goal': 1.8}
```

```python
>>> benchmarks = set_performance_benchmarks('12%, 20%, 25%, 1.8')
{'cagr_target': 0.12, 'annual_volatility_constraint': 0.20, 'drawdown_limit': 0.25, 'sharpe_ratio_goal': 1.8}
```



---

## validate_out_of_sample

### Description
Test the top‑ranked parameter combination on fresh market data outside the training window, quantify its performance relative to the in‑sample period, and apply statistical tests to flag potential over‑fitting.

### Conceptual Info

Runs the best parameter combination identified by Bayesian optimisation on a held‑out data window, compares key risk‑return metrics to the in‑sample period, and applies three statistical tests to detect over‑fitting.

### Docstring

**Summary:** Validate a strategy on out‑of‑sample data and detect over‑fitting.

**Parameters:**

- top3_parameters (list[str]): List of the top three parameter‑set strings produced by ``optimize_parameters``.
- top3_sharpe (list[float]): Sharpe ratios corresponding to each of the top three parameter sets.
- in_sample_equity (dict): Dictionary containing in‑sample equity curve data with keys ``dates`` and ``values``.
- out_sample_start (str): ISO format start date of the out‑sample window (YYYY‑MM‑DD).
- out_sample_end (str): ISO format end date of the out‑sample window (YYYY‑MM‑DD).
- backtest_function (Callable): Callable that accepts a parameter set string and returns a dict with ``sharpe`` and ``max_drawdown`` for a given date range.
**Returns:** dict - A dictionary containing the selected parameter set identifier, in‑sample and out‑of‑sample Sharpe ratios, max drawdowns, and over‑fitting test results.

**Raises:**

- ValueError: If the ``top3_parameters`` list is empty or does not contain the selected set.
- RuntimeError: If the backtest function fails to return a valid performance metric.
**Examples:**

```python
>>> top3_parameters = ['alpha=0.1,beta=0.2,gamma=0.3',
...                 'alpha=0.15,beta=0.25,gamma=0.35',
...                 'alpha=0.2,beta=0.3,gamma=0.4']
>>> top3_sharpe = [1.25, 1.10, 0.95]
>>> in_sample_equity = {
...     'dates': ['2020-01-01', '2020-01-02'],
...     'values': [100000, 102500]}
>>> def dummy_backtest(param_set):
...     return {'sharpe': 1.05 if 'alpha=0.1' in param_set else 0.9,
...             'max_drawdown': 0.12}
>>> result = validate_out_of_sample(
...     top3_parameters=top3_parameters,
...     top3_sharpe=top3_sharpe,
...     in_sample_equity=in_sample_equity,
...     out_sample_start='2020-02-01',
...     out_sample_end='2020-04-01',
...     backtest_function=dummy_backtest)
{
  'selected_param_set': 'alpha=0.1,beta=0.2,gamma=0.3',
  'in_sample_sharpe': 1.25,
  'out_of_sample_sharpe': 1.05,
  'in_sample_max_drawdown': 0.12,
  'out_of_sample_max_drawdown': 0.12,
  'overfitting_tests_passed': [True, False, True],
  'overfitting_test_names': ['t-test', 'Diebold-Mariano', 'ADF']
}
```

```python
>>> # Using the second best parameter set
result2 = validate_out_of_sample(
...     top3_parameters=top3_parameters,
...     top3_sharpe=top3_sharpe,
...     in_sample_equity=in_sample_equity,
...     out_sample_start='2020-02-01',
...     out_sample_end='2020-04-01',
...     backtest_function=dummy_backtest)
{
  'selected_param_set': 'alpha=0.15,beta=0.25,gamma=0.35',
  'in_sample_sharpe': 1.10,
  'out_of_sample_sharpe': 0.90,
  'in_sample_max_drawdown': 0.12,
  'out_of_sample_max_drawdown': 0.12,
  'overfitting_tests_passed': [False, False, True],
  'overfitting_test_names': ['t-test', 'Diebold-Mariano', 'ADF']
}
```

