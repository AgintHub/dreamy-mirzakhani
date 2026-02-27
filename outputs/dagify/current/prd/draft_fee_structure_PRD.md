# draft_fee_structure PRD

## Description
Sets the fund's fee schedule by defining management fees, performance fees, hurdle rate, and fee payment structures to optimize revenue while remaining competitive.


## Conceptual Info

This node establishes the fund's fee schedule, balancing revenue needs with market competitiveness by setting management and performance fee percentages, incorporating hurdle rates if applicable, and detailing the payment structures.

## Docstring

### Summary
Define the management and performance fee percentages, hurdle rate, and fee structures for the fund, considering market standards and internal cost recovery goals.

### Parameters

- **set_performance_and_risk_targets** (dict): Outputs from the parent node defining risk and performance targets, influencing fee structure decisions.
- **estimate_setup_and_operating_costs** (dict): Outputs from the parent node estimating annual setup and operating costs that need to be covered by fund fees.

### Returns

dict: A dictionary containing the 'management_fees', 'performance_fees', 'hurdle_rate', and 'fee_schedules' as string descriptions of the fee arrangements.

### Raises

- ValueError: If fee components are missing or ill-formatted, indicating incomplete or inconsistent inputs.

### Examples

```python
>>> draft_fee_structure()
>>> # Management fees: '2%', Performance fees: '20%', Hurdle rate: '5%', Payment structure: 'Standard tiered fees'
{'management_fees': '2%', 'performance_fees': '20%', 'hurdle_rate': '5%', 'fee_schedules': 'Standard tiered fees'}
```

```python
>>> draft_fee_structure()
>>> # Management fees: '1.5%', Performance fees: '15%', Hurdle rate: 'None', Payment structure: 'High-water mark with clawback'
{'management_fees': '1.5%', 'performance_fees': '15%', 'hurdle_rate': 'None', 'fee_schedules': 'High-water mark with clawback'}
```
