# validate_oauth_token PRD

## Description
Validates an OAuth token and returns a valid token or throws an error if validation fails.


## Conceptual Info

This shim node is responsible for validating an OAuth token provided in the user context. It ensures that the token is legitimate and usable for further operations.

## Docstring

### Summary
Validates an OAuth token based on the provided user context and returns the validated token.

### Parameters

- **user_context** (str): The user context containing the OAuth token to be validated.

### Returns

str: The validated OAuth token.

### Raises

- ValueError: If the OAuth token is invalid or cannot be validated.
- TypeError: If the user context is not of the expected type.

### Examples

```python
>>> validate_oauth_token(user_context='example_user_context')
'validated_oauth_token'
```

```python
>>> validate_oauth_token(user_context='invalid_user_context')
ValueError: Invalid OAuth token
```
