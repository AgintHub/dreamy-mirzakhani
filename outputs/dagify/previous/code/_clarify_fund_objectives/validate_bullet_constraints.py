from typing import List


def validate_bullet_constraints(bullets: str, max_count: str) -> List[str]:
    """
    Validates a list of bullet points against a maximum count constraint.

    Parameters
    ----------
    bullets : str
        Input list of bullet points as a string
    max_count : str
        Maximum allowed count of bullet points as a string

    Returns
    -------
    List[str]
        Validated list of bullet points

    Raises
    ------
    ValueError
        When the input list exceeds the maximum allowed count
    TypeError
        When input types are incorrect

    Examples
    --------
    >>> validate_bullet_constraints(bullets='a\nb\nc', max_count='2')
    ['a', 'b']

    >>> validate_bullet_constraints(bullets='a\nb\nc\nd', max_count='5')
    ['a', 'b', 'c', 'd']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")