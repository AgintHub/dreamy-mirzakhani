from typing import List


def generate_implementation_notes(entity_type: str, jurisdiction: str, requirement: str) -> List[str]:
    """
    Generate one or two short notes that explain how to implement or comply with
    a given regulatory requirement for a specified legal entity type and
    jurisdiction.

    Parameters
    ----------
    entity_type : str
        The legal entity type (e.g., 'LLC', 'LP', 'SICAV').
    jurisdiction : str
        The regulatory jurisdiction or country where the entity operates.
    requirement : str
        The specific regulatory filing, registration, or compliance action
        required.

    Returns
    -------
    List[str]
        A list containing one or two brief textual notes that describe
        actionable steps to implement or comply with the requirement.

    Raises
    ------
    ValueError
        Raised if any of the input strings are empty or None.
    TypeError
        Raised if any input is not of type `str`.

    Examples
    --------
    >>> notes = generate_implementation_notes(
    ...     entity_type='LLC',
    ...     jurisdiction='United States',
    ...     requirement='File annual report with the Secretary of State')
    >>> print(notes)
    ['Submit the annual report by the deadline indicated on the Secretary of
    State website.', 'Ensure all shareholders’ information is current before
    filing.']

    >>> notes = generate_implementation_notes(
    ...     entity_type='SICAV',
    ...     jurisdiction='Switzerland',
    ...     requirement='Register with FINMA under Article 3.1')
    >>> print(notes)
    ['Complete the FINMA registration form and submit required financial
    statements.', 'Maintain the register of beneficial owners as per Article
    3.1.']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")