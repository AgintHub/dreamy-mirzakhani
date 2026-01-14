# _estimate_setup_and_operating_costs - Complete PRD Documentation

## Overview
PRDs for nodes in the '_estimate_setup_and_operating_costs' module.

## Table of Contents

- [validate_input_data](#validate_input_data)

- [estimate_provider_costs](#estimate_provider_costs)

- [estimate_technology_costs](#estimate_technology_costs)

- [estimate_governance_costs](#estimate_governance_costs)

- [consolidate_service_names](#consolidate_service_names)

- [consolidate_monthly_costs](#consolidate_monthly_costs)

- [calculate_annual_costs](#calculate_annual_costs)

- [calculate_total_monthly](#calculate_total_monthly)

- [calculate_total_annual](#calculate_total_annual)

- [count_line_items](#count_line_items)

- [generate_budget_overview](#generate_budget_overview)



---

## validate_input_data

### Description
Validate that the input service provider, technology stack, and governance data are consistent and complete before proceeding with cost estimation.

### Conceptual Info

The validate_input_data shim ensures that the service provider list, technology stack, and governance structure are well‑formed, non‑empty, and internally consistent before the estimation logic runs. It acts as a gatekeeper that prevents downstream functions from operating on malformed data.

### Docstring

**Summary:** Validate the integrity and completeness of service provider, technology stack, and governance inputs for cost estimation.

**Parameters:**

- providers (ListServiceProvidersOutput): Pydantic model containing provider names and their corresponding core functions.
- tech_stack (DefineTechnologyStackOutput): Pydantic model detailing workflow stages, technology solutions, and in‑house/outsource flags.
- governance (OutlinerGovernanceStructureOutput): Pydantic model describing roles, responsibilities, and authority scopes.
**Returns:** str - Returns a confirmation string such as "Validation successful" when all inputs pass checks.

**Raises:**

- ValueError: Raised when any of the input models contain missing required fields, empty lists, or mismatched lengths.
- TypeError: Raised when the provided arguments do not match the expected Pydantic model types.
**Examples:**

```python
>>> from pydantic import BaseModel, Field
>>> from typing import List
>>> class ListServiceProvidersOutput(BaseModel):
...     provider_names: List[str] = Field([...])
...     provider_functions: List[str] = Field([...])
>>> class DefineTechnologyStackOutput(BaseModel):
...     workflow_stages: List[str] = Field([...])
...     technology_solutions: List[str] = Field([...])
...     vendor_in_house_flags: List[bool] = Field([...])
>>> class OutlinerGovernanceStructureOutput(BaseModel):
...     role_names: List[str] = Field([...])
...     role_responsibility_1: List[str] = Field([...])
...     role_responsibility_2: List[str] = Field([...])
...     role_responsibility_3: List[str] = Field([...])
...     role_authority_scope: List[str] = Field([...])
>>> validate_input_data(providers=ListServiceProvidersOutput(...),
...                     tech_stack=DefineTechnologyStackOutput(...),
...                     governance=OutlinerGovernanceStructureOutput(...))
"Validation successful"
```

```python
>>> validate_input_data(providers=ListServiceProvidersOutput(...),
...                     tech_stack=DefineTechnologyStackOutput(...),
...                     governance=OutlinerGovernanceStructureOutput(...))
"Validation successful"
```



---

## estimate_provider_costs

### Description
Estimates monthly costs for each external service provider based on their names and core functions.

### Conceptual Info

This shim calculates a monthly cost estimate for each external service provider, enabling the larger budgeting process to aggregate provider, technology, and governance costs into a comprehensive financial overview.

### Docstring

**Summary:** Estimate the monthly cost for each service provider based on its name and core function.

**Parameters:**

- provider_names (List[str]): Ordered list of external service provider names (e.g., prime broker, custodian).
- provider_functions (List[str]): Corresponding core function descriptions for each provider, matching the order of provider_names.
**Returns:** List[float] - A list of floating‑point numbers representing the estimated monthly cost (USD) for each provider in the same order as the input lists.

**Raises:**

- ValueError: If the two input lists are of unequal length or any element is empty or null.
- TypeError: If provider_names or provider_functions are not lists of strings.
**Examples:**

```python
>>> estimated_costs = estimate_provider_costs(

...     provider_names=["Prime Broker", "Custodian"],

...     provider_functions=["Execution services", "Asset safekeeping"]

>>> )
[12000.0, 3500.0]
```

```python
>>> try:
...     estimate_provider_costs([], [])
>>> except ValueError as e:
...     print(e)
"provider_names and provider_functions must be non‑empty lists of equal length."
```



---

## estimate_technology_costs

### Description
Estimates technology costs based on workflow stages, technology solutions, and vendor flags.

### Conceptual Info

The estimate_technology_costs shim function provides a placeholder for estimating technology costs based on workflow stages, technology solutions, and vendor flags. Its purpose is to facilitate the calculation of technology costs in the larger system.

### Docstring

**Summary:** Estimates technology costs based on workflow stages, technology solutions, and vendor flags.

**Parameters:**

- workflow_stages (str): Ordered list of workflow stages (e.g., Idea Generation, Signal Generation, Order Entry, Execution Management, Position Monitoring, Reconciliation, Settlement).
- technology_solutions (str): Corresponding technology solution for each stage (e.g., Data Analytics Platform, Portfolio Management System, OMS, FIX Gateway, Risk Engine, Reconciliation Tool).
- vendor_flags (str): Boolean flag for each stage indicating whether the solution is implemented in-house (true) or outsourced to a vendor (false).
**Returns:** List[float] - List of estimated technology costs.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> estimate_technology_costs(workflow_stages=['Idea Generation', 'Signal Generation'], technology_solutions=['Data Analytics Platform', 'Portfolio Management System'], vendor_flags=['in-house', 'outsourced'])
[1000.0, 2000.0]
```

```python
>>> estimate_technology_costs(workflow_stages=['Order Entry', 'Execution Management'], technology_solutions=['OMS', 'FIX Gateway'], vendor_flags=['outsourced', 'in-house'])
[1500.0, 2500.0]
```



---

## estimate_governance_costs

### Description
Estimates governance costs based on role names, responsibilities, and authority scopes.

### Conceptual Info

This shim function estimates governance costs based on role names, responsibilities, and authority scopes.

### Docstring

**Summary:** Estimates governance costs based on role names, responsibilities, and authority scopes.

**Parameters:**

- role_names (str): Names of the roles
- responsibilities (str): Responsibilities for each role
- authority_scopes (str): Authority scopes for each role
**Returns:** List[float] - List of estimated governance costs

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> estimate_governance_costs(role_names='CEO', responsibilities='strategy, finance', authority_scopes='company-wide')
[10000.0, 5000.0, 2000.0]
```

```python
>>> estimate_governance_costs(role_names='CTO', responsibilities='technology, innovation', authority_scopes='departmental')
[5000.0, 2000.0, 1000.0]
```



---

## consolidate_service_names

### Description
This shim function consolidates service provider names, technology names, and governance names into a single list of service names.

### Conceptual Info

The consolidate_service_names shim function plays a crucial role in integrating and standardizing service names across different domains, ensuring consistency and clarity in the overall system.

### Docstring

**Summary:** Consolidates service provider names, technology names, and governance names into a single list of service names.

**Parameters:**

- provider_names (str): A string of service provider names separated by commas.
- technology_names (str): A string of technology names separated by commas.
- governance_names (str): A string of governance names separated by commas.
**Returns:** List[str] - A list of consolidated service names.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> consolidate_service_names(provider_names='Prime Broker, Custodian, Fund Administrator', technology_names='Data Analytics Platform, Portfolio Management System', governance_names='Risk Management, Compliance')
['Prime Broker', 'Custodian', 'Fund Administrator', 'Data Analytics Platform', 'Portfolio Management System', 'Risk Management', 'Compliance']
```



---

## consolidate_monthly_costs

### Description
This shim function consolidates monthly costs from provider, technology, and governance costs into a single list of floats.

### Conceptual Info

The consolidate_monthly_costs shim function aggregates monthly costs from various sources, including service providers, technology, and governance, into a unified list for easier budgeting and analysis.

### Docstring

**Summary:** Consolidates monthly costs from provider, technology, and governance costs into a single list of floats.

**Parameters:**

- provider_costs (str): A string representing provider costs
- technology_costs (str): A string representing technology costs
- governance_costs (str): A string representing governance costs
**Returns:** List[float] - A list of consolidated monthly costs

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> consolidate_monthly_costs(provider_costs='[100.0, 200.0]', technology_costs='[50.0, 75.0]', governance_costs='[25.0, 50.0]')
[175.0, 325.0]
```

```python
>>> consolidate_monthly_costs(provider_costs='[500.0]', technology_costs='[250.0]', governance_costs='[100.0]')
[850.0]
```



---

## calculate_annual_costs

### Description
Calculates the annual costs from a list of monthly costs.

### Conceptual Info

This shim function takes a list of monthly costs and returns a list of corresponding annual costs.

### Docstring

**Summary:** Calculates the annual costs from a list of monthly costs.

**Parameters:**

- monthly_costs (str): A string representation of a list of monthly costs.
**Returns:** List[float] - A list of annual costs corresponding to the input monthly costs.

**Raises:**

- ValueError: When the input string is not a valid list of numbers.
- TypeError: When the input is not a string.
**Examples:**

```python
>>> calculate_annual_costs(monthly_costs='[100.0, 200.0, 300.0]')
[1200.0, 2400.0, 3600.0]
```

```python
>>> calculate_annual_costs(monthly_costs='[50.0, 75.0, 100.0]')
[600.0, 900.0, 1200.0]
```



---

## calculate_total_monthly

### Description
Calculates the total monthly cost from a list of monthly costs.

### Conceptual Info

The calculate_total_monthly shim function takes a string of monthly costs and returns the total monthly cost as a float.

### Docstring

**Summary:** Calculates the total monthly cost from a string of monthly costs.

**Parameters:**

- monthly_costs (str): A string representation of the monthly costs.
**Returns:** float - The total monthly cost.

**Raises:**

- ValueError: When the input string is not a valid representation of monthly costs.
- TypeError: When the input is not a string.
**Examples:**

```python
>>> calculate_total_monthly('100,200,300')
600.0
```

```python
>>> calculate_total_monthly('500')
500.0
```



---

## calculate_total_annual

### Description
Sums a list of annual costs to produce the total annual budget.

### Conceptual Info

This shim aggregates individual annual cost items into a single total, enabling downstream budgeting calculations.

### Docstring

**Summary:** Return the total of a list of annual cost amounts.

**Parameters:**

- annual_costs (List[float]): A list of annual cost values (USD) for each service provider or cost category.
**Returns:** float - The sum of all numbers in `annual_costs`. If the list is empty, returns 0.0.

**Raises:**

- ValueError: Raised when any element in `annual_costs` is negative, indicating an invalid cost value.
- TypeError: Raised when `annual_costs` is not a list or contains non-numeric elements.
**Examples:**

```python
>>> calculate_total_annual(annual_costs=[12000.0, 24000.5, 18000.25])
54000.75
```

```python
>>> calculate_total_annual(annual_costs=[])
0.0
```



---

## count_line_items

### Description
Counts the number of unique service names provided.

### Conceptual Info

The shim determines how many distinct service names exist in a given list, which is essential for budget line item enumeration in the overall cost estimation workflow.

### Docstring

**Summary:** Return the count of unique service names supplied.

**Parameters:**

- service_names (List[str]): A list of service names; may contain duplicates.
**Returns:** int - The number of unique service names in the input list.

**Raises:**

- ValueError: Raised if service_names is empty.
- TypeError: Raised if service_names is not a list of strings.
**Examples:**

```python
>>> count_line_items(['PrimeBroker', 'Custodian', 'PrimeBroker', 'LegalCounsel'])
3
```

```python
>>> count_line_items([])
ValueError: service_names list cannot be empty
```



---

## generate_budget_overview

### Description
Creates a concise textual summary of the overall budget, highlighting major cost drivers and key service categories.

### Conceptual Info

The shim generates a human‑readable budget overview that condenses numeric totals and service names into a single paragraph suitable for executive reporting.

### Docstring

**Summary:** Generate a budget overview string summarizing annual cost totals per service category.

**Parameters:**

- total_annual (str): Total annual budget as a formatted string (e.g., "$12,345,678").
- service_names (str): Comma‑separated list of service names corresponding to the annual costs.
- annual_costs (str): Comma‑separated list of annual costs per service, matching the order of service_names.
**Returns:** str - A single paragraph string summarizing the budget, including the total annual amount and the top three cost drivers.

**Raises:**

- ValueError: Raised if the numbers of service names and costs do not match.
- TypeError: Raised if any argument is not a string.
**Examples:**

```python
>>> result = generate_budget_overview(
...     total_annual='$12,345,678',
...     service_names='Prime Broker,Custodian,Legal Counsel',
...     annual_costs='5,000,000;2,500,000;1,000,000')
>>> print(result)
"Total annual budget is $12,345,678. The largest cost drivers are Prime Broker ($5,000,000), Custodian ($2,500,000), and Legal Counsel ($1,000,000)."
```

```python
>>> generate_budget_overview('','$','')
"Total annual budget is $0. No cost drivers to report."
```

