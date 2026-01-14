def get_governance_template_for_entity(entity_type: str) -> str:
    """
    Retrieve a governance template for the specified legal entity type.

    Parameters
    ----------
    entity_type : str
        The legal entity type for which the governance template is requested
        (e.g., 'LLC', 'LP', 'SICAV').

    Returns
    -------
    str
        A JSON string that can be deserialised into a dict with keys:
        'role_names', 'responsibilities_level_1',
        'responsibilities_level_2', 'responsibilities_level_3', and
        'authority_scopes'.

    Raises
    ------
    ValueError
        If the requested entity_type is not supported.
    TypeError
        If entity_type is not a string.

    Examples
    --------
    >>> template_json = get_governance_template_for_entity(entity_type='LLC')
    >>> print(template_json)
    {\n  \"role_names\": [\"Director\", \"Secretary\"],\n
    \"responsibilities_level_1\": [\"Strategic Oversight\", \"Compliance\"],\n
    \"responsibilities_level_2\": [\"Financial Reporting\", \"Risk
    Management\"],\n  \"responsibilities_level_3\": [\"Operational Decision-
    Making\", \"Policy Development\"],\n  \"authority_scopes\": [\"Full\",
    \"Limited\"]\n}

    >>> try:
    ...     get_governance_template_for_entity(entity_type='UnknownEntity')
    >>> except ValueError as e:
    ...     print(e)
    "Unsupported entity type: UnknownEntity"

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")