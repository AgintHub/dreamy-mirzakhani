from typing import List


def extract_target_values(targets: str) -> List[float]:
    """
    Extracts target values from a dictionary of targets.

    Parameters
    ----------
    targets : dict
        A dictionary containing target values

    Returns
    -------
    List[float]
        A list of target values

    Raises
    ------
    ValueError
        When the input dictionary is empty or does not contain the expected
        keys.
    TypeError
        When the input is not a dictionary.

    Examples
    --------
    >>> targets = {'metric1': 0.1, 'metric2': 0.2}
    >>> extract_target_values(targets=targets)
    [0.1, 0.2]

    >>> targets = {}
    >>> extract_target_values(targets=targets)
    []

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")