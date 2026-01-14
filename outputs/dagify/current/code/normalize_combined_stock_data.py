from pydantic import BaseModel, Field


class StoreCombinedStockDataOutput(BaseModel):
    """Pydantic model for store_combined_stock_data node outputs."""
    schema_validated: bool = (
        Field(..., description="Whether the data is schema-validated")
    )
    versioning_status: str = (
        Field(..., description="Current versioning status of the data lake")
    )
    ingestion_latency_ms: int = (
        Field(..., description="Latency of data ingestion in milliseconds")
    )
    data_lake_region: str = (
        Field(..., description="Region where the data lake is located")
    )
    data_lake_size_gb: float = (
        Field(..., description="Current size of the data lake in GB")
    )


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


def normalize_combined_stock_data(store_combined_stock_data_input: StoreCombinedStockDataOutput, **kwargs) -> NormalizeCombinedStockDataOutput:
    """
    Normalize the unified stock dataset and annotate provenance to produce a
    clean, schema-validated Parquet archive.

    Parameters
    ----------
    consolidated_dataset_uri : str
        URI to the consolidated stock dataset created by
        store_combined_stock_data.

    Returns
    -------
    tuple[float, str, bool]
        A tuple containing (latency_annotation in ms, datacenter_tag,
        schema_validated).

    Raises
    ------
    ValueError
        If the input URI is invalid or points to a non-stock dataset.
    FileNotFoundError
        If the dataset cannot be located.
    RuntimeError
        If schema validation fails or required metadata is missing.

    Examples
    --------
    >>> normalize_combined_stock_data({'consolidated_dataset_uri': 's3://data-
    lake/combined_stock_v1.parquet'})
    (latency_annotation=12.5, datacenter_tag='us-east-1', schema_validated=True)

    >>> normalize_combined_stock_data({'consolidated_dataset_uri':
    'gs://bucket/combined_v2.parquet'})
    (latency_annotation=48.7, datacenter_tag='eu-west-2', schema_validated=True)

    """
    return NormalizeCombinedStockDataOutput(
        latency_annotation=0.0,
        datacenter_tag="",
        schema_validated=False,
    )