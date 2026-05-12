# collect_sentiment_data PRD

## Description
Collect social media sentiment data for the assets.


## Conceptual Info

This node collects social media sentiment data for the assets by querying a social media platform and transforming the results into a CSV file.

## Docstring

### Summary
Collect sentiment scores for each asset and export to CSV.

### Parameters

- **selected_assets** (List[str]): List of asset symbols to collect sentiment data for.

### Returns

Dict[str, List[str]]: A dictionary containing the asset symbols and their corresponding sentiment scores, as well as a CSV string containing the sentiment data.

### Raises

- Error: If the asset symbols are invalid or the social media platform returns an error.

### Examples

```python
>>> sentiment_data = collect_sentiment_data(['AAPL', 'GOOG'])
{'asset_symbols': ['AAPL', 'GOOG'], 'sentiment_scores': [0.5, 0.3], 'csv_data': 'AAPL,GOOG,0.5,0.3'}
```

```python
>>> sentiment_data = collect_sentiment_data(['MSFT', 'AMZN'])
{'asset_symbols': ['MSFT', 'AMZN'], 'sentiment_scores': [0.2, 0.8], 'csv_data': 'MSFT,AMZN,0.2,0.8'}
```
