from pydantic import BaseModel, Field
from typing import List


class ListServiceProvidersOutput(BaseModel):
    """Pydantic model for list_service_providers node outputs."""
    provider_categories: str = (
        Field(..., description="List of provider categories such as prime broker, fund administrator, auditor, legal counsel, compliance consultant, and custodian.")
    )
    num_providers: int = (
        Field(..., description="Number of service providers in each listed category.")
    )


class EstimateSetupAndOperatingCostsOutput(BaseModel):
    """Pydantic model for estimate_setup_and_operating_costs node outputs."""
    service_provider_costs: List[float] = (
        Field(..., description="Estimated annual costs in USD for each service provider category listed in 'list_service_providers'. The order corresponds to the list of provider categories.")
    )
    internal_overhead_costs: List[float] = (
        Field(..., description="Estimated annual costs in USD for internal overhead categories such as office, technology, staffing, etc., corresponding to internal cost components.")
    )


def estimate_setup_and_operating_costs(list_service_providers_input: ListServiceProvidersOutput, **kwargs) -> EstimateSetupAndOperatingCostsOutput:
    """
    Estimate and summarize costs required for hedge fund operations based on
    listed service providers and internal overhead categories.

    Parameters
    ----------
    provider_categories_list : str
        Output list from 'list_service_providers' node or other relevant
        data source.
    internal_overhead_categories : str
        User-provided list of internal overhead categories.

    Returns
    -------
    Dict[str, Union[List[float], float]]
        Cost estimates for each service provider category and internal
        overhead category.

    Raises
    ------
    ValueError
        If 'provider_categories_list' or 'internal_overhead_categories' is
        invalid or empty.

    Examples
    --------
    >>> provider_categories_list = ['prime broker', 'fund administrator',
    'auditor']
    >>> internal_overhead_categories = ['office', 'technology', 'staffing']
    >>> estimate_setup_and_operating_costs(provider_categories_list,
    internal_overhead_categories)
    {"
                  "  'service_provider_costs': [100000, 50000, 20000],"
                  "  'internal_overhead_costs': [30000, 20000, 40000]"
                  

    """
    return EstimateSetupAndOperatingCostsOutput(
        service_provider_costs=[],
        internal_overhead_costs=[],
    )