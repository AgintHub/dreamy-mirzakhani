from typing import List


def get_jurisdiction_candidates() -> List[str]:
    """
    Return a list of jurisdiction candidate dictionaries for scoring and
    selection.

    Returns
    -------
    LIST_STR
        A list of jurisdiction dictionaries, e.g., [{'name': 'Cayman
        Islands', 'tax_rate': 0, 'regulatory_flexibility': 9}, ...].

    Raises
    ------
    RuntimeError
        If the underlying data source is unreachable or returns malformed
        data.

    Examples
    --------
    >>> >>> candidates = get_jurisdiction_candidates()
    >>> >>> print(candidates[0]['name'])
    Cayman Islands

    >>> >>> for j in get_jurisdiction_candidates()[:2]:
    >>> ...     print(j['name'], j['tax_rate'])
    Cayman Islands 0\nBritish Virgin Islands 0

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")