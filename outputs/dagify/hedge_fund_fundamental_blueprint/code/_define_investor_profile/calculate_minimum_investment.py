def calculate_minimum_investment(strategy_type: str, investor_base: str) -> int:
    """
    Calculates the minimum investment required based on the strategy type and
    investor base.

    Parameters
    ----------
    strategy_type : str
        The type of investment strategy.
    investor_base : str
        The type of investor.

    Returns
    -------
    int
        The minimum investment required in USD.

    Raises
    ------
    ValueError
        When the calculated minimum investment is not a positive integer.
    TypeError
        When the input strategy type or investor base is not a string.

    Examples
    --------
    >>> calculate_minimum_investment(strategy_type='conservative',
    investor_base='individual')
    >>> 100000
    100000

    >>> calculate_minimum_investment(strategy_type='aggressive',
    investor_base='institutional')
    >>> 500000
    500000

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")