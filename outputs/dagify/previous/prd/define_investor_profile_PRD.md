# define_investor_profile PRD

## Description
Specify target investor characteristics


## Conceptual Info

The node translates the fund's business objectives into a concrete investor persona, outlining the financial size, risk appetite, liquidity needs, and geographic origin that align with the strategy.

## Docstring

### Summary
Derives a target investor profile from clarified fund objectives.

### Parameters

- **investment_purpose** (str): The investment purpose defined in clarify_fund_objectives.
- **competitive_edge** (str): The competitive edge description from clarify_fund_objectives.
- **long_term_vision** (str): The long-term vision statement from clarify_fund_objectives.

### Returns

dict: Dictionary containing typical_ticket_size (int), risk_tolerance (str), liquidity_preference (str), and geographic_focus (str).

### Raises

- ValueError: If any of the objective strings are empty or missing.
- TypeError: If the input types do not match the expected string types.

### Examples

```python
>>> profile = define_investor_profile(
...     investment_purpose='Generate alpha in emerging markets',
...     competitive_edge='Unique macro insights and rapid execution',
...     long_term_vision='Be the leading global macro fund by 2035'"
                ")
{
  'typical_ticket_size': 2000000,
  'risk_tolerance': 'high',
  'liquidity_preference': 'annual',
  'geographic_focus': 'North America & Europe'
}
```

```python
>>> profile = define_investor_profile(
...     investment_purpose='Diversify portfolio with low correlation assets',
...     competitive_edge='Access to niche commodity markets',
...     long_term_vision='Build a 5% IRR hedge fund portfolio by 2040'"
                ")
{
  'typical_ticket_size': 1000000,
  'risk_tolerance': 'medium',
  'liquidity_preference': 'quarterly',
  'geographic_focus': 'Global, with a focus on Asia-Pacific'
```
