def get_provider_mapping_for_entity(entity_type: str) -> str:
    """
    Returns a JSON-formatted mapping of provider roles to provider details for
    the given entity type.

    Parameters
    ----------
    entity_type : str
        The validated legal entity type (e.g., 'LLC', 'LP', 'SICAV').

    Returns
    -------
    str
        A JSON string where keys are provider roles and values are
        dictionaries containing provider names and their core functions.

    Raises
    ------
    ValueError
        If the provided entity_type is not supported or recognized.
    TypeError
        If entity_type is not a string.

    Examples
    --------
    >>> output = get_provider_mapping_for_entity('LLC')
    >>> print(output)
    "{\n  \"prime_broker\": {\"name\": \"PrimeBrokerInc\", \"function\":
    \"Execution and clearing\"},\n  \"custodian\": {\"name\": \"CustodianLtd\",
    \"function\": \"Safekeeping and settlement\"},\n  \"fund_administrator\":
    {\"name\": \"AdminCorp\", \"function\": \"Reporting and NAV
    calculation\"},\n  \"legal_counsel\": {\"name\": \"LawPartners\",
    \"function\": \"Legal and regulatory advice\"},\n
    \"compliance_consultant\": {\"name\": \"ComplianceCo\", \"function\": \"Risk
    and compliance management\"}\n}"

    >>> output = get_provider_mapping_for_entity('SICAV')
    >>> print(output)
    "{\n  \"prime_broker\": {\"name\": \"SicavPrime\", \"function\": \"Execution
    and clearing\"},\n  \"custodian\": {\"name\": \"SicavCustodian\",
    \"function\": \"Safekeeping and settlement\"},\n  \"fund_administrator\":
    {\"name\": \"SicavAdmin\", \"function\": \"Reporting and NAV
    calculation\"},\n  \"legal_counsel\": {\"name\": \"SicavLegal\",
    \"function\": \"Legal and regulatory advice\"},\n
    \"compliance_consultant\": {\"name\": \"SicavCompliance\", \"function\":
    \"Risk and compliance management\"}\n}"

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")