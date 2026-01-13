def count_line_items(service_names: str) -> int:
    """
    Return the count of unique service names supplied.

    Parameters
    ----------
    service_names : List[str]
        A list of service names; may contain duplicates.

    Returns
    -------
    int
        The number of unique service names in the input list.

    Raises
    ------
    ValueError
        Raised if service_names is empty.
    TypeError
        Raised if service_names is not a list of strings.

    Examples
    --------
    >>> count_line_items(['PrimeBroker', 'Custodian', 'PrimeBroker',
    'LegalCounsel'])
    3

    >>> count_line_items([])
    ValueError: service_names list cannot be empty

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")