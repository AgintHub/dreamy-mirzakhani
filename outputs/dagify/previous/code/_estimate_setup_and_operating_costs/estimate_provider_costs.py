from typing import List


def estimate_provider_costs(provider_names: str, provider_functions: str) -> List[float]:
    """
    Estimate the monthly cost for each service provider based on its name and
    core function.

    Parameters
    ----------
    provider_names : List[str]
        Ordered list of external service provider names (e.g., prime broker,
        custodian).
    provider_functions : List[str]
        Corresponding core function descriptions for each provider, matching
        the order of provider_names.

    Returns
    -------
    List[float]
        A list of floating‑point numbers representing the estimated monthly
        cost (USD) for each provider in the same order as the input lists.

    Raises
    ------
    ValueError
        If the two input lists are of unequal length or any element is empty
        or null.
    TypeError
        If provider_names or provider_functions are not lists of strings.

    Examples
    --------
    >>> estimated_costs = estimate_provider_costs(

    ...     provider_names=["Prime Broker", "Custodian"],

    ...     provider_functions=["Execution services", "Asset safekeeping"]

    >>> )
    [12000.0, 3500.0]

    >>> try:
    ...     estimate_provider_costs([], [])
    >>> except ValueError as e:
    ...     print(e)
    "provider_names and provider_functions must be non‑empty lists of equal
    length."

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")