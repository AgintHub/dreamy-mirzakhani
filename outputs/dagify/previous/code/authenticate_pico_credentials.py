from pydantic import BaseModel, Field
from typing import List


class EstablishPicoConnectionOutput(BaseModel):
    """Pydantic model for establish_pico_connection node outputs."""
    access_token: str = (
        Field(..., description="OAuth 2.0 access token for authenticating with the pico datacenter.")
    )
    token_type: str = (
        Field(..., description="Type of token, typically 'Bearer'.")
    )
    expires_in: int = (
        Field(..., description="Time in seconds until the access token expires.")
    )
    connection_status: str = (
        Field(..., description="Status of the connection attempt, e.g., 'connected' or 'failed'.")
    )
    is_connected: bool = (
        Field(..., description="True if connection was successfully established, False otherwise.")
    )
    connection_id: str = (
        Field(..., description="Unique identifier for the established connection session.")
    )
    error_message: str = (
        Field(..., description="Error message if the connection attempt failed; empty string otherwise.")
    )


class AuthenticatePicoCredentialsOutput(BaseModel):
    """Pydantic model for authenticate_pico_credentials node outputs."""
    access_token: str = (
        Field(..., description="OAuth 2.0 access token used to authenticate requests to the Pico datacenter.")
    )
    token_type: str = (
        Field(..., description="Type of the token (e.g., Bearer).")
    )
    expires_in: int = (
        Field(..., description="Number of seconds until the token expires.")
    )
    scopes: List[str] = (
        Field(..., description="List of OAuth scopes granted by the token.")
    )
    is_valid: bool = (
        Field(..., description="Indicates whether the token was successfully validated.")
    )


def authenticate_pico_credentials(establish_pico_connection_input: EstablishPicoConnectionOutput, **kwargs) -> AuthenticatePicoCredentialsOutput:
    """
    Authenticate to the Pico datacenter by initiating an OAuth 2.0 client
    credentials flow, obtaining an access token and validating its correctness
    to enable secure access to resources.

    Parameters
    ----------
    client_id : str
        The OAuth 2.0 client identifier credential used to initiate
        authentication.
    client_secret : str
        The OAuth 2.0 client secret credential corresponding to the
        client_id.
    token_endpoint : str
        URL of the OAuth 2.0 token endpoint to request the access token.
    scopes : List[str]
        List of OAuth scopes to request for the access token.

    Returns
    -------
    dict
        Dictionary containing access_token (str), token_type (str),
        expires_in (int), scopes (List[str]), and is_valid (bool) indicating
        token validity.

    Raises
    ------
    ConnectionError
        Raised if there is a network error contacting the OAuth token
        endpoint.
    AuthenticationError
        Raised if the client credentials are invalid or token request is
        denied.
    TokenValidationError
        Raised if the obtained token fails validation checks.

    Examples
    --------
    >>> result = authenticate_pico_credentials(
    ...     client_id='abc123',
    ...     client_secret='secretXYZ',
    ...     token_endpoint='https://auth.pico.example.com/oauth2/token',
    ...     scopes=['read:data', 'write:data'])
    {

    """
    return AuthenticatePicoCredentialsOutput(
        access_token="",
        token_type="",
        expires_in=0,
        scopes=[],
        is_valid=False,
    )