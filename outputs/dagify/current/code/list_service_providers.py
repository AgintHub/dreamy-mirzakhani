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


class ListServiceProvidersOutput(BaseModel):
    """Pydantic model for list_service_providers node outputs."""
    provider_categories: str = (
        Field(..., description="List of provider categories such as prime broker, fund administrator, auditor, legal counsel, compliance consultant, and custodian.")
    )
    num_providers: int = (
        Field(..., description="Number of service providers in each listed category.")
    )


def list_service_providers(select_jurisdiction_input: SelectJurisdictionOutput, **kwargs) -> ListServiceProvidersOutput:
    """
    Creates a list of mandatory third-party service provider categories for
    hedge fund setup and operation.

    Parameters
    ----------
    jurisdiction : str
        The legal jurisdiction selected for the fund, influencing the
        service provider landscape.

    Returns
    -------
    dict
        A dictionary containing provider categories and their counts.

    Raises
    ------
    ValueError
        If jurisdiction input is invalid or not provided.

    Examples
    --------
    >>> list_service_providers('Cayman')
    {

    """
    return ListServiceProvidersOutput(
        provider_categories="",
        num_providers=0,
    )