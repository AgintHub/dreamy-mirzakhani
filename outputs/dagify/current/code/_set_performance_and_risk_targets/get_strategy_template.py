def get_strategy_template(strategy_category: str) -> str:
    """
    Retrieves a strategy template based on the provided strategy category.

    Parameters
    ----------
    strategy_category : str
        The primary investment strategy category.

    Returns
    -------
    dict
        A dictionary containing the strategy template, including metric
        names and target values.

    Raises
    ------
    ValueError
        When the input strategy category is invalid or not supported.
    TypeError
        When the input strategy category is not a string.

    Examples
    --------
    >>> get_strategy_template(strategy_category='conservative')
    {'metric_names': ['Gross Return', 'Volatility'], 'target_values': [0.05,
    0.10]}

    >>> get_strategy_template(strategy_category='aggressive')
    {'metric_names': ['Gross Return', 'Volatility'], 'target_values': [0.10,
    0.20]}

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")