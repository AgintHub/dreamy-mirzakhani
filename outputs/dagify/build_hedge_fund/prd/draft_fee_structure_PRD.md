# draft_fee_structure PRD

## Description
Define fee model parameters


## Conceptual Info

The draft_fee_structure node calculates the fee schedule for a hedge fund, translating strategic targets and cost assumptions into concrete percentage figures for management and performance fees, optionally incorporating a hurdle rate.

## Docstring

### Summary
Generate a fee model based on target returns, risk limits, and operating cost estimates.

### Parameters

- **annual_gross_return_target** (float): Target annual gross return expressed as a decimal (e.g., 0.12 for 12%).
- **volatility_limit_pct** (float): Maximum acceptable annual volatility in percent.
- **sharpe_ratio_goal** (float): Desired Sharpe ratio target for the fund.
- **max_drawdown_pct** (float): Maximum acceptable peak‑to‑trough drawdown in percent.
- **service_provider_cost_usd** (float): Estimated annual cost for all service providers.
- **technology_systems_cost_usd** (float): Estimated annual cost for all required technology systems.
- **office_human_infrastructure_cost_usd** (float): Estimated annual cost for office space, hardware, and human infrastructure.

### Returns

dict: A dictionary containing fee percentages and a brief commentary.

### Raises

- ValueError: If any numeric input is negative or missing.
- TypeError: If inputs are not of expected numeric types.

### Examples

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
