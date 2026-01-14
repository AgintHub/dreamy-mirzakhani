# compile_pitch_deck_outline PRD

## Description
Generates a concise list of 10 slide titles for an investor pitch deck, pulling key themes from related fund design nodes.


## Conceptual Info

The node consolidates critical fund attributes into a structured slide‑title list, enabling a clear, investor‑focused narrative.

## Docstring

### Summary
Generate a 10‑slide title list for an investor pitch deck.

### Parameters

- **investment_objectives** (List[str]): Bullet points from clarify_fund_objectives outlining the fund’s purpose, risk/reward, and market differentiation.
- **investor_profile_characteristics** (List[str]): Four key traits defining the target investor demographic, sourced from define_investor_profile.
- **chosen_strategy** (str): Primary hedge‑fund strategy selected in choose_investment_strategy.
- **alignment_explanation** (str): One‑sentence rationale linking the chosen strategy to the fund’s objectives.
- **annual_gross_return_target** (float): Target gross return (decimal) from set_performance_and_risk_targets.
- **volatility_limit_pct** (float): Maximum acceptable volatility (percentage) from set_performance_and_risk_targets.
- **sharpe_ratio_goal** (float): Desired Sharpe ratio from set_performance_and_risk_targets.
- **max_drawdown_pct** (float): Maximum acceptable drawdown (percentage) from set_performance_and_risk_targets.
- **management_fee_percent** (float): Management fee percentage (AUM) from draft_fee_structure.
- **performance_fee_percent** (float): Performance fee percentage (returns) from draft_fee_structure.
- **hurdle_rate_percent** (float): Hurdle rate percentage from draft_fee_structure.
- **control_name** (List[str]): Names of quantitative risk controls from design_risk_management_framework.
- **control_limit** (List[float]): Numerical limits for each risk control.
- **roles** (List[str]): Five leadership roles from outline_governance_structure.
- **duties** (List[str]): One‑sentence duty for each leadership role.

### Returns

List[str]: An ordered list of 10 slide titles.

### Raises

- ValueError: If any required input list is empty or contains fewer items than expected.

### Examples

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
