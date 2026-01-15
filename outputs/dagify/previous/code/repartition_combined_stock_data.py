from pydantic import BaseModel, Field
from typing import List


class NormalizeCombinedStockDataOutput(BaseModel):
    """Pydantic model for normalize_combined_stock_data node outputs."""
    latency_annotation: float = (
        Field(..., description="The average latency of the combined stock data.")
    )
    datacenter_tag: str = (
        Field(..., description="The datacenter where the stock data was stored.")
    )
    schema_validated: bool = (
        Field(..., description="Whether the stock data schema is valid.")
    )


class RepartitionCombinedStockDataOutput(BaseModel):
    """Pydantic model for repartition_combined_stock_data node outputs."""
    storage_layout_name: str = (
        Field(..., description="Name of the chosen storage layout")
    )
    optimized_partitions_count: int = (
        Field(..., description="Number of optimized partitions")
    )
    total_data_size_gb: float = Field(..., description="Total data size in GB")
    latency_optimized_percentage: float = (
        Field(..., description="Percentage of latency optimized")
    )
    data_distribution_metrics: List[bool] = (
        Field(..., description="List of metrics for data distribution")
    )


def repartition_combined_stock_data(normalize_combined_stock_data_input: NormalizeCombinedStockDataOutput, **kwargs) -> RepartitionCombinedStockDataOutput:
    """
    Repartitions the normalized combined stock data into a distributed storage
    layout.

    Parameters
    ----------
    combined_stock_data : dict
        Normalized combined stock data

    Returns
    -------
    dict
        Storage layout name, optimized partitions count, total data size in
        GB, latency optimized percentage, and data distribution metrics

    Raises
    ------
    ValueError
        If the input data is malformed

    Examples
    --------
    >>> repartition_combined_stock_data(combined_stock_data={'stocks': [{'name':
    'AAPL', 'price': 100.0}, {'name': 'GOOG', 'price': 200.0}]})
    {'storage_layout_name': 'distributed_layout', 'optimized_partitions_count':
    2, 'total_data_size_gb': 1.0, 'latency_optimized_percentage': 0.8,
    'data_distribution_metrics': [True, True]}

    """
    return RepartitionCombinedStockDataOutput(
        storage_layout_name="",
        optimized_partitions_count=0,
        total_data_size_gb=0.0,
        latency_optimized_percentage=0.0,
        data_distribution_metrics=[],
    )