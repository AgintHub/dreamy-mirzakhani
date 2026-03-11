from pydantic import BaseModel, Field


class SelectJurisdictionOutput(BaseModel):
    """Pydantic model for select_jurisdiction node outputs."""
    chosen_jurisdiction: str = (
        Field(..., description="The selected jurisdiction for the fund (e.g., Cayman, Delaware, Luxembourg).")
    )
    advantages: str = (
        Field(..., description="A list containing two advantages of the chosen jurisdiction.")
    )
    disadvantages: str = (
        Field(..., description="A list containing two disadvantages of the chosen jurisdiction.")
    )
    rationale: str = (
        Field(..., description="The reasoning behind selecting this jurisdiction, including strategic, regulatory, and operational factors.")
    )


class ChooseLegalEntityTypeOutput(BaseModel):
    """Pydantic model for choose_legal_entity_type node outputs."""
    selected_entity_type: str = (
        Field(..., description="The selected legal vehicle structure for the fund's chosen jurisdiction.")
    )
    entity_type_rationale: str = (
        Field(..., description="A brief one-sentence explanation for the selected legal vehicle structure.")
    )


def choose_legal_entity_type(select_jurisdiction_input: SelectJurisdictionOutput, **kwargs) -> ChooseLegalEntityTypeOutput:
    """
    Selects the legal entity form for the fund based on the selected
    jurisdiction.

    Parameters
    ----------
    selected_jurisdiction : str
        The legal jurisdiction selected by the fund.

    Returns
    -------
    dict[str, str]
        A dictionary containing the selected legal vehicle structure and its
        brief explanation.

    Raises
    ------
    ValueError
        If the input jurisdiction is invalid or unsupported.

    Examples
    --------
    >>> selected_jurisdiction = 'Cayman'
    >>> chosen_entity = choose_legal_entity_type(selected_jurisdiction)
    >>> print(chosen_entity)
    {"selected_entity_type": 'LP', "entity_type_rationale": 'brief explanation'}

    """
    return ChooseLegalEntityTypeOutput(
        selected_entity_type="",
        entity_type_rationale="",
    )