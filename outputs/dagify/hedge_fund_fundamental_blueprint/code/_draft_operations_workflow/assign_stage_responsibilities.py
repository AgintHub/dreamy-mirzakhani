from typing import List


def assign_stage_responsibilities(stages: str, providers: str) -> List[str]:
    """
    Map operational stages to responsible parties using the fixed provider
    order.

    Parameters
    ----------
    stages : str
        An ordered, comma‑separated string of operational stage names.
    providers : str
        An ordered, comma‑separated string of mandatory external service
        provider names in the order: prime broker, custodian, fund
        administrator, legal counsel, compliance consultant.

    Returns
    -------
    str
        A comma‑separated string of responsible parties, one for each stage,
        matching the input order.

    Raises
    ------
    ValueError
        Raised if the number of stages does not match the number of
        providers.
    TypeError
        Raised if either input is not a string.

    Examples
    --------
    >>> stages = 'Idea Generation,Structuring,Compliance,Execution,Settlement'
    >>> providers = 'Prime Broker,Custodian,Fund Administrator,Legal
    Counsel,Compliance Consultant'
    >>> result = assign_stage_responsibilities(stages, providers)
    >>> print(result)
    'Prime Broker,Custodian,Fund Administrator,Legal Counsel,Compliance
    Consultant'

    >>> assign_stage_responsibilities('Idea Generation,Execution', 'Prime
    Broker')
    ValueError: Number of stages (2) does not match number of providers (1).

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")