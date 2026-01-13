from typing import List


def get_candidate_jurisdictions() -> List[str]:
    """
    Returns a list of candidate jurisdictions for fund domicile.

    Returns
    -------
    List[str]
        List of candidate jurisdictions

    Raises
    ------
    ValueError
        When the list of candidate jurisdictions cannot be generated.
    TypeError
        When the output type is incorrect.

    Examples
    --------
    >>> get_candidate_jurisdictions()
    ['Cayman Islands', 'Luxembourg', 'Singapore']

    >>> get_candidate_jurisdictions()
    ['Ireland', 'Switzerland', 'Hong Kong']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")