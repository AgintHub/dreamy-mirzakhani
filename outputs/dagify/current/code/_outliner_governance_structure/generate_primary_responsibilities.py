from typing import List


def generate_primary_responsibilities(entity_type: str, role_names: str) -> List[str]:
    """
    Generate primary responsibilities for roles based on the entity type.

    Parameters
    ----------
    entity_type : str
        The type of entity (e.g., LP, LLC, SICAV)
    role_names : str
        Comma-separated list of role names

    Returns
    -------
    List[str]
        List of primary responsibilities for each role

    Raises
    ------
    ValueError
        When the entity type is not supported
    TypeError
        When the input types are incorrect

    Examples
    --------
    >>> generate_primary_responsibilities(entity_type='LLC',
    role_names='CEO,CTO,CFO')
    >>> => ['Manage company operations', 'Oversee technology strategy', 'Manage
    financials']
    ['Manage company operations', 'Oversee technology strategy', 'Manage
    financials']

    >>> generate_primary_responsibilities(entity_type='LP', role_names='General
    Partner, Limited Partner')
    >>> => ['Manage fund operations', 'Invest in fund']
    ['Manage fund operations', 'Invest in fund']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")