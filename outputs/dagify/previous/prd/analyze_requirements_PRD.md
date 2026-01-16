# analyze_requirements PRD

## Description
Extract testable requirements from documentation


## Conceptual Info

The analyze_requirements node consumes requirements documentation and outputs a structured list of testable acceptance criteria to seed downstream test case design and environment setup activities.

## Docstring

### Summary
Extract and return testable acceptance criteria from a requirements document.

### Parameters

- **requirements_doc** (str): Natural language documentation of system requirements and acceptance criteria.

### Returns

Tuple[List[str], int]: A tuple containing the list of extracted testable requirements and their total count.

### Raises

- ValueError: If requirements_doc is empty or None.
- TypeError: If requirements_doc is not a string.

### Examples

```python
>>> analyze_requirements("The system shall provide authentication. Acceptance criteria: 1) Users can login with valid credentials. 2) The system shall display an error message for invalid credentials. 3) Passwords must be at least 8 characters.")
(['Users can login with valid credentials', 'The system shall display an error message for invalid credentials', 'Passwords must be at least 8 characters'], 3)
```

```python
>>> analyze_requirements("System shall support password reset. Acceptance criteria: 1) User can reset password using email link. 2) Reset tokens expire after 15 minutes.")
(['User can reset password using email link', 'Reset tokens expire after 15 minutes'], 2)
```
