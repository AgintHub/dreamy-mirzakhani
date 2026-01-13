def validate_entity_type(entity_type: str) -> str:
    """
    Validates the given entity type to ensure it meets specific requirements.

    Parameters
    ----------
    entity_type : str
        The entity type to be validated (e.g., LP, LLC, SICAV)

    Returns
    -------
    str
        Validation result or an error message

    Raises
    ------
    ValueError
        When the input entity type is invalid or unsupported
    TypeError
        When the input entity type is not a string

    Examples
    --------
    >>> validate_entity_type(entity_type='LLC')
    'LLC' is a valid entity type

    >>> validate_entity_type(entity_type='InvalidType')
    'InvalidType' is not a supported entity type

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")