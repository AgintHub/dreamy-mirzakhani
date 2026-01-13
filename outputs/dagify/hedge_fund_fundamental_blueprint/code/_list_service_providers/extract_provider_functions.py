from typing import List


def extract_provider_functions(mapping: str, providers: str) -> List[str]:
    """
    Retrieve ordered provider functions from a mapping.

    Parameters
    ----------
    mapping : str
        A JSON-serialised dictionary where keys are provider names and
        values are strings describing their core functions.
    providers : str
        A JSON-serialised list of provider names in the desired order. The
        function will return a list of corresponding function descriptions.

    Returns
    -------
    str
        A JSON-serialised list of function descriptions corresponding to the
        input providers list.

    Raises
    ------
    ValueError
        Raised if a provider name in `providers` is missing from `mapping`.
    TypeError
        Raised if either `mapping` or `providers` is not a valid JSON string
        or does not represent a dictionary/list respectively.

    Examples
    --------
    >>> import json
    >>> mapping = json.dumps({"prime broker": "Execute trades", "custodian":
    "Safeguard assets"})
    >>> providers = json.dumps(["prime broker", "custodian"])
    >>> result = extract_provider_functions(mapping, providers)
    >>> print(json.loads(result))
    ["Execute trades", "Safeguard assets"]

    >>> mapping = json.dumps({"prime broker": "Execute trades"})
    >>> providers = json.dumps(["prime broker", "custodian"])
    >>> extract_provider_functions(mapping, providers)
    ValueError: Provider 'custodian' not found in mapping.

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")