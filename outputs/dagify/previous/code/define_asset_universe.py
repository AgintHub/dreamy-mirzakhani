from pydantic import BaseModel, Field
from typing import List


class ChooseInvestmentStrategyOutput(BaseModel):
    """Pydantic model for choose_investment_strategy node outputs."""
    chosen_strategy: str = (
        Field(..., description="The specific hedge fund strategy selected from the predefined categories")
    )
    alignment_explanation: str = (
        Field(..., description="A one-sentence explanation of how the chosen strategy supports the fund's objectives")
    )


class DefineAssetUniverseOutput(BaseModel):
    """Pydantic model for define_asset_universe node outputs."""
    asset_classes: List[str] = (
        Field(..., description="List of specific asset classes/instruments that will constitute the investable universe")
    )
    number_of_assets: int = (
        Field(..., description="Number of asset classes listed")
    )


def define_asset_universe(choose_investment_strategy_input: ChooseInvestmentStrategyOutput, **kwargs) -> DefineAssetUniverseOutput:
    """
    Generate a list of tradable asset classes for the hedge fund’s investable
    universe.

    Parameters
    ----------
    chosen_strategy : str
        The specific hedge fund strategy selected from the predefined
        categories (e.g., long/short equity, market neutral, global macro,
        event-driven, arbitrage).

    Returns
    -------
    Dict[str, Union[List[str], int]]
        A dictionary containing two keys:  - ``asset_classes``: a list of
        specific asset classes/instruments that will constitute the
        investable universe. - ``number_of_assets``: an integer representing
        the count of asset classes listed.

    Raises
    ------
    ValueError
        If ``chosen_strategy`` is empty or not one of the supported strategy
        categories.

    Examples
    --------
    >>> define_asset_universe(chosen_strategy='long/short equity')
    {'asset_classes': ['US Equities', 'EU Equities', 'Emerging Market Equities',
    'US Equity Options', 'EU Equity Options'], 'number_of_assets': 5}

    >>> define_asset_universe(chosen_strategy='global macro')
    {'asset_classes': ['US Treasuries', 'Eurodollar Futures', 'Gold Futures',
    'USD/JPY FX', 'Commodities Futures'], 'number_of_assets': 5}

    """
    return DefineAssetUniverseOutput(
        asset_classes=[],
        number_of_assets=0,
    )