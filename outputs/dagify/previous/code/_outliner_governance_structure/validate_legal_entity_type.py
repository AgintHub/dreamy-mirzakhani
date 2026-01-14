def validate_legal_entity_type(entity_type: str) -> str:
    """
    Validate the supplied legal entity type against an internal list of
    supported types and return a confirmation string.

    Parameters
    ----------
    entity_type : str
        The legal entity type to validate (e.g., 'LP', 'LLC', 'SICAV').

    Returns
    -------
    str
        A confirmation string such as "Entity type 'LLC' validated."

    Raises
    ------
    ValueError
        If the entity_type is not in the list of supported legal entity
        types.
    TypeError
        If entity_type is not a string.

    Examples
    --------
    >>> validate_legal_entity_type('LLC')
    "Entity type 'LLC' validated."

    >>> validate_legal_entity_type('Unknown')
    ValueError: Unsupported entity type 'Unknown'.

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")