from typing import List


def validate_objectives_bullets(objectives_bullets: str) -> List[str]:
    """
    Validate a string of bullet points representing investment objectives and
    return a list of validated bullets.

    Parameters
    ----------
    objectives_bullets : str
        A string containing bullet points to be validated, each representing
        an investment objective.

    Returns
    -------
    List[str]
        A list of validated bullet points, with each point being a string.

    Raises
    ------
    ValueError
        If the input string is not properly formatted or if any bullet point
        is empty or missing.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> validated_bullets = validate_objectives_bullets("\n- Objective 1\n-
    Objective 2\n")
    ["- Objective 1", "- Objective 2"]

    >>> try:\n    validate_objectives_bullets(123)\nexcept TypeError as e:\n
    print(e)
    Input must be a string.

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")