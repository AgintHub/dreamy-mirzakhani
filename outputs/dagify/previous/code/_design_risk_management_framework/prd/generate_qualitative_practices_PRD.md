# generate_qualitative_practices PRD

## Description
Generates a list of qualitative risk practice descriptions based on risk profile, portfolio complexity, and number of instruments.


## Conceptual Info

In a portfolio risk management workflow, this shim supplies contextual qualitative controls that complement quantitative metrics, enabling practitioners to embed governance, monitoring, and review practices aligned with the risk profile and portfolio structure.

## Docstring

### Summary
Return a list of qualitative risk practice descriptions for a portfolio.

### Parameters

- **risk_profile** (str): A brief text label (e.g., 'Conservative', 'Moderate', 'Aggressive') describing the portfolio's overall risk appetite.
- **portfolio_complexity** (str): A label indicating the structural complexity of the portfolio (e.g., 'Low', 'Medium', 'High').
- **num_instruments** (str): A string representation of the integer number of distinct tradable instruments included in the portfolio.

### Returns

LIST_STR: A list where each element is a sentence or short paragraph describing a qualitative risk practice relevant to the supplied inputs.

### Raises

- ValueError: Raised if any required input is empty or None.
- TypeError: Raised if inputs are not of type str.

### Examples

```python
>>> generate_qualitative_practices(risk_profile='Moderate', portfolio_complexity='High', num_instruments='12')
["Implement a quarterly independent audit of all major risk controls.", "Establish a risk review committee composed of senior portfolio managers and compliance staff.", "Maintain a documented incident response plan for significant risk events."]
```

```python
>>> generate_qualitative_practices(risk_profile='Aggressive', portfolio_complexity='Low', num_instruments='5')
["Conduct bi‑annual risk appetite reviews with senior leadership.", "Ensure all trades are pre‑cleared by an independent risk officer."]
```
