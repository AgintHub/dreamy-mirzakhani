# authenticate_pico_credentials PRD

## Description
Perform secure OAuth-based authentication to obtain and validate access tokens, enabling authorized access to the Pico datacenter’s resources in compliance with modern security standards.


## Conceptual Info

This node handles the OAuth 2.0 authentication process to securely acquire and validate access tokens using client credentials. It enables authorized, password-free access to the Pico datacenter's protected resources according to modern security best practices.

## Docstring

### Summary
Authenticate to the Pico datacenter by initiating an OAuth 2.0 client credentials flow, obtaining an access token and validating its correctness to enable secure access to resources.

### Parameters

- **client_id** (str): The OAuth 2.0 client identifier credential used to initiate authentication.
- **client_secret** (str): The OAuth 2.0 client secret credential corresponding to the client_id.
- **token_endpoint** (str): URL of the OAuth 2.0 token endpoint to request the access token.
- **scopes** (List[str]): List of OAuth scopes to request for the access token.

### Returns

dict: Dictionary containing access_token (str), token_type (str), expires_in (int), scopes (List[str]), and is_valid (bool) indicating token validity.

### Raises

- ConnectionError: Raised if there is a network error contacting the OAuth token endpoint.
- AuthenticationError: Raised if the client credentials are invalid or token request is denied.
- TokenValidationError: Raised if the obtained token fails validation checks.

### Examples

```python
>>> result = authenticate_pico_credentials(
...     client_id='abc123',
...     client_secret='secretXYZ',
...     token_endpoint='https://auth.pico.example.com/oauth2/token',
...     scopes=['read:data', 'write:data'])
{
```
