def validate_input_data(metric_names: str, target_values: str, rationale_texts: str, instrument_names: str, instrument_rationales: str) -> str:
    """
    Validate core input lists for consistency, types, and non‑emptiness.

    Parameters
    ----------
    metric_names : str
        Comma‑separated list of metric names (e.g., "Gross
        Return,Volatility").
    target_values : str
        Comma‑separated list of numeric target values corresponding to
        metric_names (e.g., "0.15,0.10").
    rationale_texts : str
        Comma‑separated list of brief rationales for each metric.
    instrument_names : str
        Comma‑separated list of selected instrument names.
    instrument_rationales : str
        Comma‑separated list of brief rationales for each instrument.

    Returns
    -------
    str
        A confirmation string of the form "Validation successful: X metrics,
        Y instruments."

    Raises
    ------
    ValueError
        If any list is empty or lengths of the lists do not match.
    TypeError
        If any argument is not a string or cannot be parsed into the
        expected list.

    Examples
    --------
    >>> result = validate_input_data(

    ...     metric_names="Gross Return,Volatility",

    ...     target_values="0.15,0.10",

    ...     rationale_texts="High return,Low volatility",

    ...     instrument_names="SPY,TLT",

    ...     instrument_rationales="Large cap equity,Long term Treasury"

    >>> )
    "Validation successful: 2 metrics, 2 instruments."

    >>> validate_input_data(

    ...     metric_names="",

    ...     target_values="0.15",

    ...     rationale_texts="High return",

    ...     instrument_names="SPY",

    ...     instrument_rationales="Large cap equity"

    >>> )
    ValueError: metric_names must not be empty

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")