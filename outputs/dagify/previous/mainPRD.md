# build_quant_trading_strategy - Complete PRD Documentation

## Overview
PRDs for nodes in the 'build_quant_trading_strategy' module.

## Table of Contents

- [calculate_performance_metrics](#calculate_performance_metrics)

- [choose_strategy_type](#choose_strategy_type)

- [clean_fundamental_data](#clean_fundamental_data)

- [clean_price_data](#clean_price_data)

- [create_risk_framework](#create_risk_framework)

- [define_strategy_objectives](#define_strategy_objectives)

- [define_strategy_parameters](#define_strategy_parameters)

- [develop_algorithmic_logic](#develop_algorithmic_logic)

- [document_live_trading_plan](#document_live_trading_plan)

- [execute_backtesting](#execute_backtesting)

- [execute_out_of_sample](#execute_out_of_sample)

- [generate_deployment_blueprint](#generate_deployment_blueprint)

- [implement_signal_processing](#implement_signal_processing)

- [list_required_data_assets](#list_required_data_assets)

- [optimize_parameters](#optimize_parameters)

- [retrieve_fundamental_data](#retrieve_fundamental_data)

- [retrieve_historical_price_data](#retrieve_historical_price_data)

- [test_overfitting](#test_overfitting)

- [verify_backtest_integrity](#verify_backtest_integrity)



---

## calculate_performance_metrics

### Description
Quantify strategy effectiveness

### Conceptual Info

Analyzes strategy performance using metrics like CAGR, Sharpe ratio, and max drawdown. Compares results against defined benchmarks to assess relative effectiveness.

### Docstring

**Summary:** Quantify strategy effectiveness through performance metrics and benchmark comparisons

**Parameters:**

- strategy_daily_returns (List[float]): Daily returns of the strategy (from execute_backtesting)
- strategy_cumulative_returns (List[float]): Cumulative returns of the strategy (from execute_backtesting)
- strategy_max_drawdown (float): Maximum drawdown value from backtest results
- strategy_number_of_trades (int): Total executed trades from backtest results
- benchmark_daily_returns (List[float]): Daily returns of the benchmark (typically major index)
- benchmark_cumulative_returns (List[float]): Cumulative returns of the benchmark
- benchmark_max_drawdown (float): Maximum drawdown of the benchmark
**Returns:** Dict[str, Union[float, bool]] - Dictionary containing performance metrics and benchmark comparisons

**Raises:**

- ValueError: If input lists are empty or input types are invalid
- ZeroDivisionError: If benchmark or strategy has zero trades when calculating win rate
**Examples:**

```python
>>> calculate_performance_metrics(strat_returns=[0.02, -0.01, 0.03], strat_cumulative=[1.02, 1.01, 1.04], strat_max DD=0.05, trades=150, bench_returns=[0.01, 0.005, 0.02], bench_cumulative=[1.01, 1.015, 1.04], bench_max DD=0.08)
{'cagr': 1.183, 'sharpe_ratio': 0.76, ... 'cagr_benchmark': 1.03, 'cagr_outperforms_benchmark': True}
```

```python
>>> calculate_performance_metrics(strat_returns=[], trades=0)
ValueError: Daily returns list cannot be empty
```



---

## choose_strategy_type

### Description
Select quant strategy category framework

### Conceptual Info

This node selects a primary quantitative trading strategy category based on predefined investment objectives. It maps the target risk-return profile, asset classes, and trading frequency to the most appropriate strategy framework, ensuring alignment with downstream risk management, parameter definition, and algorithmic logic components.

### Docstring

**Summary:** Maps strategy objectives to framework category. Evaluates target return, risk tolerance, and asset classes to select a quant strategy type with a risk-aligned rationale.

**Parameters:**

- annual_return_target_percentage (float): Target annual return requirement in percent (e.g., 12.5 for 12.5%)
- maximum_risk_tolerance_percentage (float): Maximum acceptable drawdown or volatility threshold in percent (e.g., 10.0)
- target_asset_classes (List[str]): List of asset classes to be traded (e.g., ['equities', 'fixed income'])
- trading_frequency_per_month (int): Expected number of trades/signals per calendar month (e.g., 200)
- additional_investment_goals (List[str]): Supplemental constraints or objectives (e.g., ['liquidity preservation'])
**Returns:** tuple[str, str] - Strategy type categorization and rationale. Returns (strategy_type, rationale) where strategy_type ∈ ['market neutral', 'statistical arbitrage', 'momentum', 'mean reversion', 'trend following']

**Raises:**

- ValueError: If no valid strategy type aligns with the provided objectives, or if required parameters are missing
**Examples:**

```python
>>> choose_strategy_type(annual_return_target_percentage=15.0," + 
                       "maximum_risk_tolerance_percentage=8.0," + 
                       "target_asset_classes=['equities'], " +
                       "trading_frequency_per_month=180, " +
                       "additional_investment_goals=['market beta neutrality'])
('market neutral', 'Diversified equity risk exposure aligns with beta neutrality goals')
```

```python
>>> choose_strategy_type(annual_return_target_percentage=25.0," +
                       "maximum_risk_tolerance_percentage=15.0," +
                       "target_asset_classes=['commodities'], " +
                       "trading_frequency_per_month=450, " +
                       "additional_investment_goals=['leveraged exposure'])
('trend following', 'High-return volatility profiles suit leveraged trend exploitation')
```



---

## clean_fundamental_data

### Description
Standardize fundamental metrics

### Conceptual Info

This node harmonizes financial data from Bloomberg and Yahoo Finance by converting dissimilar metrics (earnings, revenues, EPS) into standardized units and aligns reporting periods (Q1-2018 → Q1-2023). It ensures consistent time intervals for 50 companies while maintaining audit trails of source data.

### Docstring

**Summary:** Standardize raw fundamental financial metrics from multiple sources into consistent units and reporting periods

**Parameters:**

- raw_data_path (str): Path/URI to raw data file generated by retrieve_fundamental_data
- file_format (str): Format of source file (CSV/Parquet/etc)
- company_tickers (List[str]): List of tickers with successfully retrieved data
- source_platforms (List[str]): List of source platforms (Bloomberg/Yahoo Finance) used
**Returns:** Dict[str, Any] - Dictionary containing standardized metrics, source platforms, periodic alignment status, and company count with success flag

**Raises:**

- FileNotFoundError: If source data file cannot be located at specified path
- ValueError: If required metrics (earnings, revenues) are missing from source data
- ConversionError: If unit conversion between currencies or units fails
**Examples:**

```python
>>> clean_fundamental_data(raw_data_path='/data/fundamentals.parquet', file_format='Parquet', company_tickers=['AAPL', 'MSFT'], source_platforms=['Bloomberg'])
{'success': True, 'standardized_metrics': ['earnings', 'revenues', 'EPS'], 'data_sources': ['Bloomberg'], 'adjusted_reporting_periods': ['Q1-2022', 'Q2-2022'], 'company_count': 2}
```

```python
>>> clean_fundamental_data(raw_data_path='/data/missing_data.csv', file_format='CSV', company_tickers=['GOOGL'], source_platforms=['Yahoo Finance'])
{'success': False, 'error': 'ValueError: Revenues missing for 25% of GOOGL records'}
```



---

## clean_price_data

### Description
Standardize pricing dataset.

### Conceptual Info

This node cleans and standardizes raw price data retrieved from multiple exchanges, ensuring that missing values, duplicate records, and abrupt price jumps are resolved, resulting in a continuous, ready‑to‑use time series for each of the 50 target instruments.

### Docstring

**Summary:** clean_price_data cleans raw pricing data by handling missing entries, duplicates, and price jumps, returning a standardized dataset with continuous time intervals.

**Parameters:**

- data_file_path (str): File path to the raw pricing data (CSV, Parquet, or other supported format) retrieved by the `retrieve_historical_price_data` node.
**Returns:** dict - A dictionary containing the cleaned pricing information:
- `instruments`: List of 50 instrument symbols/IDs processed.
- `timestamp_intervals`: Continuous time intervals in ISO format.
- `missing_values_handled`: List of counts of missing values resolved per instrument.
- `duplicates_removed`: List of counts of duplicate entries removed per instrument.
- `price_jumps_adjusted`: List of counts of price jumps corrected per instrument.
- `is_time_continuous`: Boolean indicating whether the time series is uniformly continuous.

**Raises:**

- FileNotFoundError: If `data_file_path` does not point to an existing file.
- ValueError: If the input file cannot be parsed into the expected tabular format.
- RuntimeError: If an unexpected error occurs during the cleaning process (e.g., inconsistent data shapes).
**Examples:**

```python
>>> cleaned = clean_price_data('data/raw_prices.parquet')
>>> print(cleaned['instruments'][:5])
['AAPL', 'GOOG', 'MSFT', 'AMZN', 'FB']
```

```python
>>> try:
...     clean_price_data('nonexistent.csv')
>>> except FileNotFoundError as e:
...     print(e)
FileNotFoundError: No such file or directory: 'nonexistent.csv'
```



---

## create_risk_framework

### Description
Define capital protection rules

### Conceptual Info

Creates a comprehensive risk framework that protects capital by defining how large each position can be, the exposure limits per instrument, the drawdown threshold that will trigger a trading halt, the daily profit/loss ceiling, and a final rule such as volatility‑based sizing or a stop‑loss mechanism. The framework adapts to the chosen strategy type and the optimized parameter set to ensure the strategy operates within acceptable risk limits.

### Docstring

**Summary:** Creates a risk framework specifying position sizing, exposure limits, drawdown halts, daily P&L thresholds, and an additional control rule based on the chosen strategy type and optimized parameters.

**Parameters:**

- strategy_type (str): Primary strategy category (e.g., 'market neutral', 'trend following', etc.).
- optimized_parameters (List[float]): List of optimized values for each core strategy parameter returned by the genetic algorithm.
- parameter_names (List[str]): Names of the core strategy parameters corresponding to the optimized_parameters list.
**Returns:** dict - Dictionary containing the risk framework fields: position_sizing_rule, max_exposure_per_instrument, drawdown_threshold, daily_pnl_limit, and additional_control_rule.

**Raises:**

- ValueError: Raised if strategy_type is not one of the supported categories.
- ValueError: Raised if lengths of optimized_parameters and parameter_names do not match.
**Examples:**

```python
>>> framework = create_risk_framework(strategy_type='market neutral', optimized_parameters=[0.3, 0.2, 0.5], parameter_names=['beta', 'volatility', 'alpha'])
>>> print(framework)
{'position_sizing_rule': 'Equal weight long and short with 1% equity per trade', 'max_exposure_per_instrument': 0.02, 'drawdown_threshold': 0.15, 'daily_pnl_limit': 5000.0, 'additional_control_rule': 'Volatility-based sizing: size ∝ 1/(σ * √lookback)'}
```

```python
>>> framework = create_risk_framework(strategy_type='trend following', optimized_parameters=[0.25, 0.35, 0.4], parameter_names=['alpha', 'beta', 'gamma'])
>>> print(framework)
{'position_sizing_rule': 'Kelly criterion based on win/loss ratio', 'max_exposure_per_instrument': 0.05, 'drawdown_threshold': 0.20, 'daily_pnl_limit': 10000.0, 'additional_control_rule': 'Trailing stop of 1.5× ATR'}
```



---

## define_strategy_objectives

### Description
Specify the primary goals of the trading strategy

### Conceptual Info

The define_strategy_objectives node captures the high‑level investment objectives that guide the design, optimization, and risk management of the quantitative trading strategy. It translates a user‑written textual description of return targets, risk limits, asset‑class focus, and trading cadence into a structured dictionary that downstream nodes can consume.

### Docstring

**Summary:** Parse a textual description of investment objectives and return a structured dictionary containing target return, risk tolerance, asset classes, trading frequency, and any additional constraints.

**Parameters:**

- prompt (str): A string containing the user’s investment objective specification. The prompt should mention the annual return target, maximum risk tolerance, asset classes, trading frequency, and optionally any extra goals.
**Returns:** dict - A dictionary with keys:

- annual_return_target_percentage (float)
- maximum_risk_tolerance_percentage (float)
- target_asset_classes (list of str)
- trading_frequency_per_month (int)
- additional_investment_goals (list of str)

Each key maps to the corresponding value extracted from the prompt.

**Raises:**

- ValueError: If any of the required fields (return target, risk tolerance, asset classes, or trading frequency) cannot be found or parsed from the prompt.
- TypeError: If the prompt argument is not a string.
**Examples:**

```python
>>> print(define_strategy_objectives('Annual return target: 20%; Max drawdown: 15%; Asset classes: equities, bonds; Trading frequency: 12; Additional goals: ESG compliance.'))
{'annual_return_target_percentage': 20.0, 'maximum_risk_tolerance_percentage': 15.0, 'target_asset_classes': ['equities', 'bonds'], 'trading_frequency_per_month': 12, 'additional_investment_goals': ['ESG compliance']}
```

```python
>>> print(define_strategy_objectives('Annual return target: 15%; Max risk tolerance: 10%; Asset classes: equities; Trading frequency: 8; Additional investment goals: low volatility.'))
{'annual_return_target_percentage': 15.0, 'maximum_risk_tolerance_percentage': 10.0, 'target_asset_classes': ['equities'], 'trading_frequency_per_month': 8, 'additional_investment_goals': ['low volatility']}
```



---

## define_strategy_parameters

### Description
Establish model rules in mathematical terms

### Conceptual Info

Defines the quantitative hyper‑parameters that govern signal generation and risk management for a selected strategy type. The node produces a set of parameter names, their mathematical definitions, and feasible search ranges for subsequent optimisation.

### Docstring

**Summary:** Generate core strategy parameters from a strategy type. The function receives the chosen strategy category and returns four parallel lists containing parameter names, their mathematical expressions, and min/max bounds for hyper‑parameter tuning.

**Parameters:**

- strategy_type (str): Primary strategy category returned by `choose_strategy_type`. Expected values are 'market neutral', 'statistical arbitrage', 'momentum', 'mean reversion', or 'trend following'.
**Returns:** dict - A dictionary with keys 'parameter_names', 'parameter_expressions', 'parameter_min_values', and 'parameter_max_values', each mapping to a list of strings or floats. The lists are aligned by index so that the i‑th element of each list corresponds to the same parameter.

**Raises:**

- ValueError: If `strategy_type` is not one of the recognised strategy categories.
**Examples:**

```python
>>> params = define_strategy_parameters('momentum')
>>> print(params)
{'parameter_names': ['fast_period', 'slow_period', 'volatility_window', 'factor_weight', 'signal_threshold'], 'parameter_expressions': ['EMA(price, fast_period)', 'EMA(price, slow_period)', 'sqrt(Var(price, volatility_window))', 'weight * factor', 'threshold'], 'parameter_min_values': [5.0, 20.0, 10.0, 0.1, 0.01], 'parameter_max_values': [20.0, 50.0, 60.0, 1.0, 0.1]}
```

```python
>>> params = define_strategy_parameters('mean reversion')
>>> print(params['parameter_min_values'])
>>> print(params['parameter_max_values'])
[5.0, 10.0, 15.0, 0.2, 0.05]
[30.0, 60.0, 45.0, 1.0, 0.15]
```



---

## develop_algorithmic_logic

### Description
Create signal generation equations

### Conceptual Info

The develop_algorithmic_logic node synthesizes a set of weighted, normalized mathematical expressions that transform raw market and factor inputs into binary signals (0 or 1). These equations are tailored to the chosen strategy type and its core parameter definitions, ensuring that the resulting signals are aligned with the strategy’s objectives and risk profile.

### Docstring

**Summary:** Generates a collection of signal equations based on the selected strategy type and its core parameters, returning equations, weights, lookback windows, and normalization methods.

**Parameters:**

- strategy_type (str): Primary strategy category selected by the choose_strategy_type node.
- parameter_names (List[str]): List of the 5 core parameter names defined by define_strategy_parameters.
- parameter_expressions (List[str]): Mathematical expressions for each core parameter.
- parameter_min_values (List[float]): Minimum exploration bounds for each core parameter.
- parameter_max_values (List[float]): Maximum exploration bounds for each core parameter.
**Returns:** dict - Dictionary containing signal generation equations and associated metadata:
- equation_count (int): Number of equations.
- equations (List[str]): Equations in standard notation.
- weight_factors (List[float]): Weight for each equation.
- lookback_windows (List[int]): Lookback days for each equation.
- normalization_methods (List[str]): Normalization method used per equation.
- output_signal_range (str): Expected signal range, always '0-1'.

**Raises:**

- ValueError: If the lengths of parameter lists do not match or if strategy_type is unsupported.
- TypeError: If any input parameter is of an incorrect type.
**Examples:**

```python
>>> output = develop_algorithmic_logic(
...     strategy_type='momentum',
...     parameter_names=['short_window', 'long_window', 'vol_window'],
...     parameter_expressions=['5', '20', '10'],
...     parameter_min_values=[2.0, 10.0, 5.0],
...     parameter_max_values=[10.0, 40.0, 20.0])
{'equation_count': 3, 'equations': ['sig1 = ((price_t - price_{t-5}) / price_{t-5}) * w1', 'sig2 = ((price_t - price_{t-20}) / price_{t-20}) * w2', 'sig3 = vol_t * w3'], 'weight_factors': [0.5, 0.3, 0.2], 'lookback_windows': [5, 20, 10], 'normalization_methods': ['z-score', 'min-max', 'log'], 'output_signal_range': '0-1'}
```

```python
>>> output = develop_algorithmic_logic(
...     strategy_type='mean_reversion',
...     parameter_names=['lookback', 'threshold', 'vol_scale', 'alpha'],
...     parameter_expressions=['10', '1.5', '0.5', '0.8'],
...     parameter_min_values=[5.0, 0.5, 0.1, 0.5],
...     parameter_max_values=[20.0, 3.0, 1.0, 1.0])
{'equation_count': 4, 'equations': ['sig1 = ((price_t - SMA_t10) / vol_t10) * w1', 'sig2 = (vol_t / vol_t10) * w2', 'sig3 = exp(-alpha * ((price_t - SMA_t10)**2)) * w3', 'sig4 = (1 if price_t < SMA_t10 - threshold * vol_t10 else 0) * w4'], 'weight_factors': [0.4, 0.3, 0.2, 0.1], 'lookback_windows': [10, 10, 10, 10], 'normalization_methods': ['z-score', 'min-max', 'log', 'threshold'], 'output_signal_range': '0-1'}
```



---

## document_live_trading_plan

### Description
Create operational requirements

### Conceptual Info

The document_live_trading_plan node synthesizes operational guidelines for deploying a quantitative trading system into production. It consolidates latency benchmarks, fault‑tolerance strategies, and monitoring routines to ensure continuous, compliant execution.

### Docstring

**Summary:** Generate a set of operational requirements for a live trading deployment, including action list, latency thresholds, fallback mechanisms, monitoring tasks, and priority ranking.

**Returns:** Dict[str, Any] - Dictionary containing the 5 output fields. Each key maps to a list with 10 elements representing the corresponding deployment requirement.

**Raises:**

- ValueError: Raised if required dependency data (risk framework or deployment blueprint) is missing or incomplete.
- TypeError: Raised if any of the output lists are not of length 10 or contain mismatched data types.
**Examples:**

```python
>>> plan = document_live_trading_plan()
>>> print(plan['action_descriptions'][0])
'Deploy application to Kubernetes cluster'
```

```python
>>> print(plan['latency_requirements_ms'])
[200, 150, 120, 100, 80, 70, 60, 50, 45, 30]
```



---

## execute_backtesting

### Description
Apply algorithm to historical data

### Conceptual Info

Executes a walk-forward backtest of a quantitative strategy over the historical period 2018‑2022, incorporating transaction costs and slippage, to produce daily and cumulative performance metrics for later evaluation.

### Docstring

**Summary:** Simulate strategy execution over 2018‑2022 using walk‑forward analysis, generating position sizes, applying transaction costs and slippage, and producing daily and cumulative returns along with key performance indicators.

**Parameters:**

- price_data (object): Cleaned historical price series for all instruments (e.g., a DataFrame or nested list).
- fundamental_data (object): Cleaned fundamental metrics aligned with price data (e.g., earnings, revenue).
- signal_algo (object): Callable or object that implements the signal generation logic produced by `implement_signal_processing`.
**Returns:** dict - Dictionary mapping output keys (backtest_dates, strategy_positions, etc.) to their computed values.

**Raises:**

- ValueError: Raised when required input data is missing or improperly formatted.
- RuntimeError: Raised if the backtesting simulation fails (e.g., due to inconsistent dates or missing market data).
**Examples:**

```python
>>> price_data = {'prices': [100, 102, 101, 103, 104]}
>>> fundamental_data = {'eps': [3.2, 3.4, 3.5, 3.6, 3.7]}
>>> signal_algo = lambda dates: [1, 0, -1, 1, 0]
>>> results = execute_backtesting(price_data, fundamental_data, signal_algo)
{
  'backtest_dates': ['2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', '2018-01-06'],
  'strategy_positions': [0.5, 0.0, -0.5, 0.5, 0.0],
  'daily_returns': [0.01, 0.0, -0.015, 0.02, 0.0],
  'transaction_costs': [0.001, 0.001, 0.001, 0.001, 0.001],
  'slippage_costs': [0.0005, 0.0005, 0.0005, 0.0005, 0.0005],
  'cumulative_returns': [0.009, 0.009, -0.006, 0.014, 0.014],
  'trade_signals': [1, 0, -1, 1, 0],
  'number_of_trades': 4,
  'max_drawdown': 0.02,
  'backtest_success_flag': True
}
```



---

## execute_out_of_sample

### Description
Validate generalization capability of the strategy by executing it on an unseen 6-month data set, calculating out-of-sample performance metrics, and comparing them against the training period metrics.

### Conceptual Info

This node evaluates the strategy's generalization ability by applying it to a 6-month period that was not seen during training. It generates a full set of performance metrics for that period and then calculates the percentage differences between each metric and its counterpart from the training data, flagging any significant divergence.

### Docstring

**Summary:** Run the full strategy on a 6-month out-of-sample period and compare key performance metrics to the training period.

**Parameters:**

- training_cagr (float): CAGR of the training period (used for comparison).
- training_sharpe (float): Sharpe ratio of the training period (used for comparison).
- training_max_drawdown (float): Maximum drawdown of the training period (used for comparison).
- training_win_rate (float): Win rate (0-1) of the training period (used for comparison).
- training_ulcer_index (float): Ulcer index of the training period (used for comparison).
- training_calmar_ratio (float): Calmar ratio of the training period (used for comparison).
- strategy_config (dict): Dictionary containing strategy parameters and risk‑management rules to be applied during the out-of-sample run.
**Returns:** dict - Dictionary containing the out-of-sample performance metrics, the start/end dates, the percentage differences to training metrics, and a divergence flag.

**Raises:**

- ValueError: If any of the required training metric inputs are None or not numeric.
- RuntimeError: If the out-of-sample run fails due to missing data or internal errors.
**Examples:**

```python
>>> # Dummy training metrics
>>> train_cagr = 0.15
>>> train_sharpe = 1.5
>>> train_max_drawdown = 0.20
>>> train_win_rate = 0.55
>>> train_ulcer = 10.0
>>> train_calmar = 0.75
>>> # Run the node
>>> result = run_out_of_sample(train_cagr, train_sharpe, train_max_drawdown, train_win_rate, train_ulcer, train_calmar, {})
>>> print(result['out_of_sample_cagr'], result['cagr_difference_pct'])
0.142 -6.666666666666664
```

```python
>>> # Second example with a larger divergence
>>> train_cagr = 0.10
>>> train_sharpe = 1.2
>>> train_max_drawdown = 0.15
>>> train_win_rate = 0.60
>>> train_ulcer = 8.0
>>> train_calmar = 0.60
>>> # Simulated out-of-sample metrics: worse performance
>>> result = run_out_of_sample(train_cagr, train_sharpe, train_max_drawdown, train_win_rate, train_ulcer, train_calmar, {})
>>> print(result['performance_divergence_flag'])
True
```



---

## generate_deployment_blueprint

### Description
Prepare implementation guide

### Conceptual Info

Compiles a comprehensive deployment blueprint detailing API integration, platform, compute, monitoring, risk references, fallback, testing, and compliance requirements for a quant trading system.

### Docstring

**Summary:** Generates a deployment blueprint for the live trading system by aggregating API specifications, platform details, compute resources, deployment steps, monitoring dashboards, risk control references, fallback strategies, testing requirements, and compliance information. It validates that all required data from the test_overfitting and create_risk_framework outputs are present and uses them to populate the blueprint fields.

**Parameters:**

- test_overfitting_output (dict): Dictionary containing the output of the test_overfitting node.
- create_risk_framework_output (dict): Dictionary containing the output of the create_risk_framework node.
**Returns:** dict - A dictionary containing deployment blueprint fields.

**Raises:**

- ValueError: Raised if required keys are missing from the input dictionaries.
**Examples:**

```python
>>> generate_deployment_blueprint(
...     test_overfitting_output={
...         'metric_names': ['Sharpe'],
...         'baseline_values': [1.2],
...         'perturbed_mean_values': [1.0],
...         'perturbed_std_values': [0.2],
...         'perturbed_min_values': [0.8],
...         'perturbed_max_values': [1.4],
...         'perturbation_percentage': 20.0,
...         'sample_count': 5,
...         'overfitting_detected': False
...     },
...     create_risk_framework_output={
...         'position_sizing_rule': 'Fixed 1% per trade',
...         'max_exposure_per_instrument': 0.02,
...         'drawdown_threshold': 0.15,
...         'daily_pnl_limit': 1000.0,
...         'additional_control_rule': 'Volatility-based stop'
...     }
>>> )
{\n  'api_endpoints': ['https://api.example.com/v1/order', 'https://api.example.com/v1/quote'],\n  'api_authentication_methods': ['Bearer Token', 'API Key'],\n  'api_rate_limits': ['100 requests/min', '200 requests/sec'],\n  'platform_environment': 'Docker',\n  'platform_os': 'Ubuntu 20.04',\n  'required_packages': ['pandas', 'numpy', 'requests'],\n  'compute_requirements': '4 CPU cores, 8 GB RAM',\n  'deployment_steps': ['Build Docker image', 'Push to registry', 'Deploy to Kubernetes'],\n  'monitoring_dashboard_names': ['Prometheus Dashboard', 'Grafana Dashboard'],\n  'monitoring_dashboard_urls': ['http://monitoring.example.com/prometheus', 'http://monitoring.example.com/grafana'],\n  'risk_controls_reference': ['position_sizing_rule', 'max_exposure_per_instrument', 'drawdown_threshold', 'daily_pnl_limit', 'additional_control_rule'],\n  'fallback_strategies': ['Pause trading', 'Revert to cash', 'Switch to secondary broker'],\n  'testing_requirements': ['Unit tests for API client', 'Integration tests for deployment'],\n  'compliance_requirements': ['GDPR', 'FINRA']\n}
```

```python
>>> generate_deployment_blueprint(
...     test_overfitting_output={
...         'metric_names': ['Sharpe', 'CAGR'],
...         'baseline_values': [1.5, 0.12],
...         'perturbed_mean_values': [1.3, 0.10],
...         'perturbed_std_values': [0.15, 0.02],
...         'perturbed_min_values': [1.0, 0.08],
...         'perturbed_max_values': [1.8, 0.14],
...         'perturbation_percentage': 20.0,
...         'sample_count': 10,
...         'overfitting_detected': True
...     },
...     create_risk_framework_output={
...         'position_sizing_rule': 'Fixed 0.5% per trade',
...         'max_exposure_per_instrument': 0.015,
...         'drawdown_threshold': 0.12,
...         'daily_pnl_limit': 500.0,
...         'additional_control_rule': 'Volatility-based stop' }
>>> )
{\n  'api_endpoints': ['https://api.example.com/v1/order', 'https://api.example.com/v1/quote', 'https://api.example.com/v1/marketdata'],\n  'api_authentication_methods': ['Bearer Token', 'API Key', 'OAuth 2.0'],\n  'api_rate_limits': ['100 requests/min', '200 requests/sec', '500 requests/day'],\n  'platform_environment': 'Kubernetes',\n  'platform_os': 'RedHat Enterprise Linux 8',\n  'required_packages': ['pandas', 'numpy', 'requests', 'scipy'],\n  'compute_requirements': '8 CPU cores, 16 GB RAM',\n  'deployment_steps': ['Create Dockerfile', 'Build image', 'Push to registry', 'Deploy to cluster', 'Run health checks'],\n  'monitoring_dashboard_names': ['Prometheus Dashboard', 'Grafana Dashboard', 'New Relic'],\n  'monitoring_dashboard_urls': ['http://monitoring.example.com/prometheus', 'http://monitoring.example.com/grafana', 'http://monitoring.example.com/newrelic'],\n  'risk_controls_reference': ['position_sizing_rule', 'max_exposure_per_instrument', 'drawdown_threshold', 'daily_pnl_limit', 'additional_control_rule'],\n  'fallback_strategies': ['Pause trading', 'Revert to cash', 'Switch to secondary broker', 'Stop all orders'],\n  'testing_requirements': ['Unit tests for API client', 'Integration tests for deployment', 'Failover tests'],\n  'compliance_requirements': ['GDPR', 'FINRA', 'SEC Rule 15c3-5']\n}
```



---

## implement_signal_processing

### Description
Convert logic into executable algorithm

### Conceptual Info

This node transforms the abstract mathematical equations and logic from 'develop_algorithmic_logic' into a concrete, executable algorithmic pseudocode. It details how to process input data through sequential computation steps, including validation of inputs for correctness and robustness, and how to handle edge cases such as missing data or invalid parameter values. The output includes a full Python pseudocode listing, a decomposed list of stepwise pseudocode instructions, and boolean indicators that confirm inclusion of input validation and edge case handling.

### Docstring

**Summary:** Generate detailed Python pseudocode for calculating trading signals from mathematical equations, including input validation and edge case handling.

**Parameters:**

- equations (List[str]): Mathematical equations defining signal generation rules, each producing output values in the 0-1 range.
- weight_factors (List[float]): Weighting factors applied to each signal generation equation.
- lookback_windows (List[int]): Number of days to look back for calculating inputs in each equation.
- normalization_methods (List[str]): Normalization techniques (e.g., z-score, min-max) applied to equation outputs.
**Returns:** dict - Dictionary containing keys: 'pseudocode' (str) for full Python pseudocode, 'pseudocode_steps' (List[str]) enumerating calculation steps, 'input_validation_included' (bool), and 'edge_case_handling_included' (bool).

**Raises:**

- ValueError: If the input lists (equations, weight_factors, lookback_windows, normalization_methods) are empty or of unequal length.
- TypeError: If inputs are not of the expected types.
**Examples:**

```python
>>> signals = ['eq1 = (close_price - sma(close_price, 5)) / std(close_price, 5)',
...            'eq2 = min_max_norm(volume, 10)']
>>> weights = [0.6, 0.4]
>>> windows = [5, 10]
>>> norms = ['z-score', 'min-max']
>>> result = implement_signal_processing(equations=signals, weight_factors=weights,
...                                      lookback_windows=windows, normalization_methods=norms)
{'pseudocode': 'def calculate_signals(data):\n    # Validate inputs\n    ...',\n 'pseudocode_steps': ['Step 1: Validate inputs', 'Step 2: Fetch data with lookback windows', 'Step 3: Compute eq1 and eq2', 'Step 4: Normalize outputs', 'Step 5: Apply weights and aggregate', 'Step 6: Clamp final signal between 0 and 1'],\n 'input_validation_included': True,\n 'edge_case_handling_included': True}
```



---

## list_required_data_assets

### Description
Identify necessary data sources

### Conceptual Info

This node maps the chosen quantitative strategy type to a curated set of data assets that the strategy will depend on. It returns a concise list of required data types along with the data category for each type, enabling downstream nodes (e.g., data retrieval and cleaning) to fetch the appropriate datasets.

### Docstring

**Summary:** Generate a list of required data types and their categories based on a selected strategy type.

**Parameters:**

- strategy_type (str): The primary strategy category selected in the `choose_strategy_type` node. Expected values are one of: "market neutral", "statistical arbitrage", "momentum", "mean reversion", or "trend following".
**Returns:** Dict[str, List[str]] - A dictionary with two keys:

- `data_types`: a list of string identifiers for each data asset required by the strategy (4–8 items).
- `data_categories`: a list of string labels indicating the category of each asset (market data, orderflow, fundamentals, macro). The order of the two lists aligns element‑wise.


**Raises:**

- ValueError: Raised if `strategy_type` is not one of the supported strategy categories.
- TypeError: Raised if `strategy_type` is not a string.
**Examples:**

```python
>>> assets = list_required_data_assets('market neutral')
>>> print(assets['data_types'])
>>> print(assets['data_categories'])
['OHLC bars', 'Volume', 'Order book snapshots', 'Statistical spreads', 'Fundamental ratios']
['market data', 'market data', 'orderflow', 'market data', 'fundamentals']
```

```python
>>> assets = list_required_data_assets('statistical arbitrage')
>>> print(assets['data_types'])
>>> print(assets['data_categories'])
['Tick data', 'Volume', 'Implied volatility surface', 'Historical price series', 'Fundamental ratios']
['orderflow', 'market data', 'market data', 'market data', 'fundamentals']
```



---

## optimize_parameters

### Description
Refine model inputs

### Conceptual Info

This node applies a genetic algorithm to search the strategy parameter space defined by define_strategy_parameters, evaluating each candidate using performance metrics from calculate_performance_metrics to maximize the Sharpe ratio.

### Docstring

**Summary:** Optimizes strategy parameters via a genetic algorithm to maximize Sharpe ratio, using performance metrics as evaluation and respecting specified convergence and population settings.

**Parameters:**

- parameter_names (List[str]): Names of the strategy's core parameters to be optimized.
- parameter_min_values (List[float]): Minimum bounds for each parameter in the search space.
- parameter_max_values (List[float]): Maximum bounds for each parameter in the search space.
- population_size (int): Number of candidate solutions in each generation of the genetic algorithm.
- convergence_threshold (float): Relative improvement threshold on the Sharpe ratio between successive generations to declare convergence.
- max_generations (int): Maximum number of generations to run if convergence is not reached earlier.
**Returns:** Dict[str, Any] - A dictionary containing the optimized parameter values, achieved Sharpe ratio, convergence status, generations run, population size used, and parameter names.

**Raises:**

- ValueError: If the lengths of parameter lists do not match or if any min bound is greater than its corresponding max bound.
- RuntimeError: If the genetic algorithm fails to converge within the specified max_generations.
- Exception: If evaluation of a candidate parameter set fails due to invalid configuration or runtime errors.
**Examples:**

```python
>>> result = optimize_parameters(
...     parameter_names=['macd_fast', 'macd_slow', 'vol_decay', 'factor_weight', 'stop_loss'],
...     parameter_min_values=[5, 12, 0.01, 0.1, 0.01],
...     parameter_max_values=[20, 50, 0.5, 1.0, 0.1],
...     population_size=50,
...     convergence_threshold=0.01,
...     max_generations=100
>>> )
{'optimized_parameter_values': [12.3, 28.5, 0.123, 0.78, 0.045], 'sharpe_ratio_achieved': 2.45, 'convergence_reached': True, 'generations_run': 35, 'population_size': 50, 'parameter_names': ['macd_fast', 'macd_slow', 'vol_decay', 'factor_weight', 'stop_loss']}
```

```python
>>> result_small = optimize_parameters(
...     parameter_names=['param1', 'param2', 'param3'],
...     parameter_min_values=[1, 0.5, 0.1],
...     parameter_max_values=[10, 5, 1],
...     population_size=20,
...     convergence_threshold=0.02,
...     max_generations=50
>>> )
{'optimized_parameter_values': [5.2, 2.7, 0.45], 'sharpe_ratio_achieved': 1.78, 'convergence_reached': False, 'generations_run': 50, 'population_size': 20, 'parameter_names': ['param1', 'param2', 'param3']}
```



---

## retrieve_fundamental_data

### Description
Collect non-price financial information

### Conceptual Info

The `retrieve_fundamental_data` node gathers essential non‑price financial data—quarterly earnings, balance sheet items, and dividend history—for a set of company tickers. It consolidates the information from Bloomberg and Yahoo Finance into a single raw data file, providing metadata such as the file path, format, retrieval status, and record counts for downstream cleaning and analysis.

### Docstring

**Summary:** Collects quarterly earnings reports, balance sheet metrics, and dividend history for a list of company tickers from Bloomberg and Yahoo Finance APIs.

**Parameters:**

- tickers (List[str]): List of company ticker symbols to retrieve fundamental data for.
- data_sources (List[str]): Optional list of data source names to use. Defaults to ['Bloomberg', 'Yahoo Finance'].
**Returns:** dict - A dictionary containing metadata about the retrieved fundamental data, including file path, format, tickers retrieved/failed, record counts, timestamps, and sources used.

**Raises:**

- ValueError: If the tickers list is empty.
- RuntimeError: If any API call fails or data cannot be retrieved for all requested tickers.
- TimeoutError: If an API request times out.
- ConnectionError: If network connection errors occur.
**Examples:**

```python
>>> result = retrieve_fundamental_data(tickers=['AAPL', 'MSFT'])
{"raw_data_file_path": "/tmp/fundamental_data.parquet", "file_format": "Parquet", "tickers_retrieved": ["AAPL", "MSFT"], "missing_tickers": [], "total_earnings_records": 8, "total_balance_sheet_records": 8, "total_dividend_records": 4, "retrieval_success": true, "retrieval_start_time": "2023-12-01T10:00:00Z", "retrieval_end_time": "2023-12-01T10:02:00Z", "data_sources_used": ["Bloomberg", "Yahoo Finance"]}
```

```python
>>> result = retrieve_fundamental_data(tickers=['AAPL', 'FAKE'])
{"raw_data_file_path": "/tmp/fundamental_data.parquet", "file_format": "Parquet", "tickers_retrieved": ["AAPL"], "missing_tickers": ["FAKE"], "total_earnings_records": 4, "total_balance_sheet_records": 4, "total_dividend_records": 2, "retrieval_success": false, "retrieval_start_time": "2023-12-01T10:00:00Z", "retrieval_end_time": "2023-12-01T10:02:00Z", "data_sources_used": ["Bloomberg", "Yahoo Finance"]}
```



---

## retrieve_historical_price_data

### Description
Acquire historical price data from specified sources for a set of liquid equity instruments across multiple exchanges.

### Conceptual Info

This node retrieves granular price data for a selected set of liquid equity instruments from multiple exchanges over a defined period and granularity, storing the results locally for downstream analysis.

### Docstring

**Summary:** Retrieves historical price data for a list of instruments from multiple exchanges within a specified date range and granularity. Stores the data locally and returns metadata about the retrieval.

**Parameters:**

- instrument_ids (List[str]): Identifiers of the instruments to fetch price data for (e.g., ['AAPL', 'MSFT']).
- exchange_ids (List[str]): Identifiers of the exchanges to pull data from (e.g., ['NYSE', 'NASDAQ', 'BATS']).
- start_date (str): Start date of the data retrieval in ISO format 'YYYY-MM-DD'.
- end_date (str): End date of the data retrieval in ISO format 'YYYY-MM-DD'.
- timeframe (str): Granularity of the bars requested (e.g., '1m', '1d', '1w').
**Returns:** dict - Dictionary containing metadata and file path for the retrieved price data.

**Raises:**

- ValueError: Raised when start_date is later than end_date or when required parameters are missing.
- TimeoutError: Raised if the data source does not respond within the allotted time.
- ConnectionError: Raised when network connectivity or API credentials are invalid.
- RuntimeError: Raised for any non-recoverable data retrieval failures.
**Examples:**

```python
>>> prices = retrieve_historical_price_data(
...     instrument_ids=['AAPL', 'MSFT', 'GOOG', 'TSLA', 'AMZN'],
...     exchange_ids=['NYSE', 'NASDAQ'],
...     start_date='2010-01-01', end_date='2024-01-01', timeframe='1d')
{'data_file_path': '/data/prices_2010_2024_1d.csv', 'instrument_ids': ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'AMZN'], 'exchange_ids': ['NYSE', 'NASDAQ'], 'start_date': '2010-01-01', 'end_date': '2024-01-01', 'timeframe': '1d', 'total_records': 1234567, 'data_retrieved': True, 'retrieval_timestamp': '2024-01-01T12:00:00Z'}
```

```python
>>> prices = retrieve_historical_price_data(
...     instrument_ids=['AAPL'],
...     exchange_ids=['NASDAQ'],
...     start_date='2019-01-01', end_date='2019-12-31', timeframe='1m')
{'data_file_path': '/data/prices_2019_1m.csv', 'instrument_ids': ['AAPL'], 'exchange_ids': ['NASDAQ'], 'start_date': '2019-01-01', 'end_date': '2019-12-31', 'timeframe': '1m', 'total_records': 123456, 'data_retrieved': True, 'retrieval_timestamp': '2019-12-31T23:59:59Z'}
```



---

## test_overfitting

### Description
Detect excessive parameter fitting

### Conceptual Info

Evaluates the robustness of the optimized strategy to parameter perturbations by performing out‑of‑sample evaluations on randomly perturbed parameter sets, summarizing the performance distribution relative to the baseline optimized set.

### Docstring

**Summary:** Detects overfitting by perturbing strategy parameters and evaluating out-of-sample performance metrics.

**Parameters:**

- metric_names (List[str]): Names of the performance metrics to compare.
- baseline_values (List[float]): Baseline metric values obtained from the original optimized parameter set.
- optimized_params (List[float]): The optimized parameter values used to generate the baseline.
- sample_count (int): Number of random perturbed parameter sets to generate (default 5).
- perturbation_percentage (float): Magnitude of ± perturbation applied to each parameter (default 0.2 for 20%).
**Returns:** Dict[str, Any] - Dictionary containing performance metric statistics and overfitting detection flag.

**Raises:**

- ValueError: Raised if metric_names and baseline_values lists are of unequal length.
- RuntimeError: Raised if any perturbed evaluation fails.
**Examples:**

```python
>>> result = test_overfitting(metric_names=['cagr', 'sharpe'], baseline_values=[0.15, 1.5], optimized_params=[0.1, 0.2], sample_count=3, perturbation_percentage=0.2)
>>> print(result)
{'metric_names': ['cagr', 'sharpe'], 'baseline_values': [0.15, 1.5], 'perturbed_mean_values': [0.14, 1.48], 'perturbed_std_values': [0.01, 0.05], 'perturbed_min_values': [0.13, 1.42], 'perturbed_max_values': [0.16, 1.55], 'perturbation_percentage': 0.2, 'sample_count': 3, 'overfitting_detected': False}
```

```python
>>> result = test_overfitting(metric_names=['cagr'], baseline_values=[0.12], optimized_params=[0.05], sample_count=5, perturbation_percentage=0.2)
>>> print(result)
{'metric_names': ['cagr'], 'baseline_values': [0.12], 'perturbed_mean_values': [0.119], 'perturbed_std_values': [0.003], 'perturbed_min_values': [0.115], 'perturbed_max_values': [0.123], 'perturbation_percentage': 0.2, 'sample_count': 5, 'overfitting_detected': False}
```



---

## verify_backtest_integrity

### Description
Test results robustness

### Conceptual Info

The verify_backtest_integrity node performs a rigorous integrity check on a quantitative strategy by running an out‑of‑sample backtest on the latest market data, comparing the resulting performance metrics to those from the training period, evaluating the effect of ±20% parameter perturbations to quantify sensitivity, and determining whether the strategy passes predefined robustness thresholds.

### Docstring

**Summary:** Run out‑of‑sample backtesting on 2023‑2024 data, compare metrics with training period, compute parameter sensitivity, and return a comprehensive integrity report.

**Parameters:**

- training_backtest (dict): Dictionary containing the outputs from execute_backtesting (backtest_dates, strategy_positions, daily_returns, etc.) representing the training period results.
- risk_framework (dict): Dictionary containing the outputs from create_risk_framework (position_sizing_rule, max_exposure_per_instrument, etc.) to ensure risk rules are enforced during the out‑of‑sample run.
**Returns:** dict - A dictionary matching the node's output structure, containing the random seed, performance metrics for training and out‑of‑sample periods, differences, parameter sensitivity index, trade counts, and the integrity flag.

**Raises:**

- ValueError: If any required key is missing from the training_backtest or risk_framework inputs.
- RuntimeError: If the out‑of‑sample backtest fails to complete due to data or execution errors.
**Examples:**

```python
>>> # Example 1: Simple deterministic training data and risk framework
>>> training_backtest = {
...     'number_of_trades': 100,
...     'cumulative_returns': [0.1, 0.2, 0.15, 0.25],
...     'max_drawdown': 0.05,
...     'daily_returns': [0.01, 0.02, -0.015, 0.025],
...     'training_cagr': 0.12,
...     'training_sharpe': 1.5,
...     'training_win_rate': 0.55
>>> }
>>> risk_framework = {
...     'max_exposure_per_instrument': 0.02,
...     'drawdown_threshold': 0.1,
...     'daily_pnl_limit': 1000
>>> }
>>> result = verify_backtest_integrity(training_backtest, risk_framework)
>>> # Expected output (illustrative):
>>> print(result['backtest_integrity_passed'])
>>> True
True
```

```python
>>> # Example 2: Failure case when training data missing a key
>>> bad_training_backtest = { 'number_of_trades': 50 }
>>> risk_framework = { 'max_exposure_per_instrument': 0.02 }
>>> try:
...     verify_backtest_integrity(bad_training_backtest, risk_framework)
>>> except ValueError as e:
...     print(str(e))
>>> # Expected output:
>>> KeyError: 'training_cagr'
KeyError: 'training_cagr'
```

