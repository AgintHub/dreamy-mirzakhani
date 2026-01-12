# create_defect_template PRD

## Description
Standardize defect logging format


## Conceptual Info

Creates a unified defect record template to ensure consistency and traceability across all testing artifacts. The function produces a structured dictionary that includes all essential fields required by downstream defect tracking systems and reporting tools.

## Docstring

### Summary
Generate a standardized defect record template for consistent bug logging.

### Returns

Dict[str, Any]: A dictionary containing the complete defect record with all required fields.

### Raises

- ValueError: Raised if an internal validation fails (unlikely for a static template).

### Examples

```python
>>> record = create_defect_template()
>>> print(record['defect_title'])
'Sample Defect Title'
```

```python
>>> record = create_defect_template()
>>> print(record)
{'defect_title': 'Sample Defect Title', 'defect_description': 'A detailed description of the defect.', 'reproduction_steps': ['Step 1', 'Step 2', 'Step 3'], 'expected_result': 'Expected outcome.', 'actual_result': 'Actual outcome.', 'severity_level': 3, 'priority_level': 2, 'requirement_id': 'REQ-001', 'test_case_id': 'TC-001', 'reporter_name': 'Alice', 'date_reported': '2026-01-12', 'status': 'Open'}
```
