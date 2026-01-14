from typing import List


def extract_authority_scopes(template: str) -> List[str]:
    """
    Extracts authority scopes from a given governance template.

    Parameters
    ----------
    template : str
        The governance template as a string from which authority scopes will
        be extracted.

    Returns
    -------
    List[str]
        A list of authority scopes extracted from the governance template.

    Raises
    ------
    ValueError
        If the input template is invalid or does not contain authority
        scopes.
    TypeError
        If the input template is not a string.

    Examples
    --------
    >>> authority_scopes = extract_authority_scopes(template='{"roles":
    [{"name": "CEO", "authority": "Financial"}, {"name": "CTO", "authority":
    "Technical"}]}')
    ["Financial", "Technical"]

    >>> authority_scopes = extract_authority_scopes(template='Invalid template')
    ValueError: Invalid template

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")