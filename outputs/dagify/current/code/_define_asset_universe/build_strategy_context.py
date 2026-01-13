def build_strategy_context(category: str, rationale: str, risk_profile: str) -> str:
    """
    Creates a strategy context dictionary based on the provided investment
    strategy category, rationale, and risk profile.

    Parameters
    ----------
    category : str
        The primary investment strategy category.
    rationale : str
        A one-paragraph explanation aligning the strategy with the fund's
        objectives.
    risk_profile : str
        A concise description of the expected risk profile associated with
        the chosen strategy.

    Returns
    -------
    dict
        A dictionary representing the strategy context, containing the
        provided category, rationale, and risk profile.

    Raises
    ------
    ValueError
        When any of the input parameters are missing or empty.
    TypeError
        When the input parameters are of incorrect types.

    Examples
    --------
    >>> build_strategy_context(category='Growth', rationale='This is a growth
    strategy.', risk_profile='Moderate')
    {'category': 'Growth', 'rationale': 'This is a growth strategy.',
    'risk_profile': 'Moderate'}

    >>> build_strategy_context(category='Income', rationale='This is an income
    strategy.', risk_profile='Low')
    {'category': 'Income', 'rationale': 'This is an income strategy.',
    'risk_profile': 'Low'}

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")