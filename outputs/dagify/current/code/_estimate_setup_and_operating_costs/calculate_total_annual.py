def calculate_total_annual(annual_costs: str) -> float:
    """
    Return the total of a list of annual cost amounts.

    Parameters
    ----------
    annual_costs : List[float]
        A list of annual cost values (USD) for each service provider or cost
        category.

    Returns
    -------
    float
        The sum of all numbers in `annual_costs`. If the list is empty,
        returns 0.0.

    Raises
    ------
    ValueError
        Raised when any element in `annual_costs` is negative, indicating an
        invalid cost value.
    TypeError
        Raised when `annual_costs` is not a list or contains non-numeric
        elements.

    Examples
    --------
    >>> calculate_total_annual(annual_costs=[12000.0, 24000.5, 18000.25])
    54000.75

    >>> calculate_total_annual(annual_costs=[])
    0.0

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")