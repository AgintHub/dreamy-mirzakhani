from pydantic import BaseModel, Field
from typing import List


class SelectDataSourcesOutput(BaseModel):
    """Pydantic model for select_data_sources node outputs."""
    source_names: List[str] = (
        Field(..., description="Names of the selected market data sources")
    )
    time_ranges: List[str] = (
        Field(..., description="Time ranges for each source in ISO format (e.g., \"2020-01-01 to 2023-12-31\")")
    )
    frequencies: List[str] = (
        Field(..., description="Data frequencies for each source (e.g., \"tick\", \"1d\", \"1h\")")
    )
    source_types: List[str] = (
        Field(..., description="Classification of each source (e.g., \"tick\", \"OHLCV\", \"fundamental\")")
    )


class PreprocessDataOutput(BaseModel):
    """Pydantic model for preprocess_data node outputs."""
    array_shape: List[int] = (
        Field(..., description="Dimensions of the 4D numpy array (e.g., [n_assets, n_features, n_time_steps, n_channels])")
    )
    num_assets: int = (
        Field(..., description="Number of distinct assets included in the dataset")
    )
    num_time_steps: int = (
        Field(..., description="Total number of time steps after alignment")
    )
    price_normalized: bool = (
        Field(..., description="Indicates whether price values have been normalized")
    )
    volatility_calculated: bool = (
        Field(..., description="Indicates whether volatility metrics have been computed")
    )
    data_integrity: bool = (
        Field(..., description="True if the dataset passes all integrity checks (no missing values, consistent timestamps)")
    )


def preprocess_data(select_data_sources_input: SelectDataSourcesOutput, **kwargs) -> PreprocessDataOutput:
    """
    Preprocesses raw market data by normalizing prices, computing volatility,
    and aligning OHLCV into a 4‑D NumPy array.

    Parameters
    ----------
    raw_data : dict
        Dictionary mapping asset tickers to raw OHLCV time series. Each
        series is a list of dictionaries with keys ['timestamp', 'open',
        'high', 'low', 'close', 'volume'].
    config : dict
        Configuration dict containing preprocessing options:  -
        `normalization_method` (str): 'minmax' or 'zscore'; -
        `volatility_window` (int): Number of periods for rolling volatility;
        - `alignment_frequency` (str): Desired resampling frequency (e.g.,
        '1h', '1d'); - `features` (List[str]): Features to compute (e.g.,
        ['price', 'volatility', 'returns']); - `channels` (List[str]):
        Optional channels such as ['price', 'volume'].

    Returns
    -------
    dict
        Dictionary containing the processed data and metadata: - `data`: 4‑D
        NumPy array of shape [assets, features, time_steps, channels]; -
        `metadata`: Dict with keys 'array_shape', 'num_assets',
        'num_time_steps', 'price_normalized', 'volatility_calculated',
        'data_integrity'.

    Raises
    ------
    ValueError
        If any asset has fewer than 2 valid time steps after alignment.
    KeyError
        If required OHLCV keys are missing in raw data.
    RuntimeError
        If data integrity checks fail (e.g., NaNs remain after imputation).

    Examples
    --------
    >>> raw_data = {
    ...     'AAPL': [
    ...         {'timestamp': '2023-01-01T09:30:00', 'open': 150.0, 'high':
    152.0, 'low': 149.5, 'close': 151.0, 'volume': 1000000},
    ...         {'timestamp': '2023-01-01T10:30:00', 'open': 151.0, 'high':
    153.0, 'low': 150.0, 'close': 152.5, 'volume': 1200000}
    ...     ],
    ...     'MSFT': [
    ...         {'timestamp': '2023-01-01T09:30:00', 'open': 250.0, 'high':
    251.0, 'low': 249.0, 'close': 250.5, 'volume': 800000},
    ...         {'timestamp': '2023-01-01T10:30:00', 'open': 250.5, 'high':
    252.0, 'low': 250.0, 'close': 251.0, 'volume': 900000}
    ...     ]
    >>> }
    {
      'data': <4‑D array shape [2, 3, 2, 1]>,
      'metadata': {
        'array_shape': [2, 3, 2, 1],
        'num_assets': 2,
        'num_time_steps': 2,
        'price_normalized': true,
        'volatility_calculated': true,
        'data_integrity': true
      }
    }

    >>> config = {
    ...   'normalization_method': 'minmax',
    ...   'volatility_window': 10,
    ...   'alignment_frequency': '1h',
    ...   'features': ['price', 'volatility'],
    ...   'channels': ['price']
    >>> }
    {
      'data': <4‑D array shape [5, 2, 240, 1]>,
      'metadata': {
        'array_shape': [5, 2, 240, 1],
        'num_assets': 5,
        'num_time_steps': 240,
        'price_normalized': true,
        'volatility_calculated': true,
        'data_integrity': true
      }
    }

    """
    return PreprocessDataOutput(
        array_shape=[],
        num_assets=0,
        num_time_steps=0,
        price_normalized=False,
        volatility_calculated=False,
        data_integrity=False,
    )