def determine_geographic_focus(investor_demographics: str, regulatory_requirements: str) -> str:
    """
    Determine the geographic focus of a fund from investor demographics and
    regulatory requirements.

    Parameters
    ----------
    investor_demographics : str
        JSON‑encoded string representing the target investor base, e.g.,
        `{"types": ["family office", "pension fund"], "regions": ["North
        America", "Europe"]}`.
    regulatory_requirements : str
        JSON‑encoded string of applicable regulatory constraints, e.g.,
        `{"EU": true, "US": false}`.

    Returns
    -------
    str
        A plain‑text sentence stating the fund's geographic focus, such as
        "The fund will primarily invest in North America and Europe,
        complying with EU investment regulations."

    Raises
    ------
    ValueError
        Raised when either input string is empty or fails to provide
        required keys.
    TypeError
        Raised when the input types are not strings.

    Examples
    --------
    >>> investor_demographics = "{\"types\": [\"family office\", \"pension
    fund\"], \"regions\": [\"North America\", \"Europe\"]}"
    >>> regulatory_requirements = "{\"EU\": true, \"US\": false}"
    >>> result = determine_geographic_focus(investor_demographics,
    regulatory_requirements)
    >>> print(result)
    "The fund will primarily invest in North America and Europe, complying with
    EU investment regulations."

    >>> investor_demographics = "{\"types\": [\"family office\"], \"regions\":
    [\"Asia\"]}"
    >>> regulatory_requirements = "{\"EU\": false, \"US\": false}"
    >>> print(determine_geographic_focus(investor_demographics,
    regulatory_requirements))
    "The fund will primarily invest in Asia with no specific regulatory
    constraints."

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")