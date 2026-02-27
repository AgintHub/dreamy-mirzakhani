from pydantic import BaseModel, Field


class ChooseInvestmentStrategyOutput(BaseModel):
    """Pydantic model for choose_investment_strategy node outputs."""
    chosen_investment_strategy: str = (
        Field(..., description="The chosen high-level investment strategy")
    )
    justification: str = (
        Field(..., description="A one-sentence justification for the chosen investment strategy")
    )


class DefineAssetUniverseOutput(BaseModel):
    """Pydantic model for define_asset_universe node outputs."""
    asset_classes_instruments: str = (
        Field(..., description="A list of specific asset classes or instruments that the strategy will trade, with a maximum of ten entries.")
    )


def define_asset_universe(choose_investment_strategy_input: ChooseInvestmentStrategyOutput, **kwargs) -> DefineAssetUniverseOutput:
    """
    Enumerate asset classes or instruments for the chosen investment strategy.

    Parameters
    ----------
    chosen_investment_strategy : str
        The chosen high-level investment strategy

    Returns
    -------
    LIST_STR
        A list of specific asset classes or instruments that the strategy
        will trade, with a maximum of ten entries.

    Examples
    --------
    >>> chosen_investment_strategy = 'Long-Short Equity'
    >>> asset_classes_instruments =
    define_asset_universe(chosen_investment_strategy)
    ['US large-cap equities', 'Euro-dollar futures', 'credit default swaps']

    """
    return DefineAssetUniverseOutput(
        asset_classes_instruments="",
    )