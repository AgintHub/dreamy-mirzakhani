# assemble_feature_matrix PRD

## Description
Combine all engineered features into a single matrix.


## Conceptual Info

Assemble the final feature matrix by combining the output of individual feature engineering nodes, handling missing values with median imputation, and exporting the result as a CSV file.

## Docstring

### Summary
Join multiple feature matrices into a single matrix, impute missing values, and export as CSV.

### Parameters

- **news_features** (List[float]): Features extracted from news articles.
- **market_features** (List[float]): Features generated from market data.
- **sentiment_features** (List[float]): Features derived from sentiment analysis.
- **date** (str): Date associated with the feature matrix.
- **asset** (str): Asset associated with the feature matrix.

### Returns

Tuple[List[float], List[str]]: The assembled feature matrix and date range covered by the matrix.

### Raises

- ValueError: If the input feature matrices have inconsistent shapes or missing values cannot be imputed.

### Examples

```python
>>> news_features = [...]
>>> market_features = [...]
>>> sentiment_features = [...]
>>> result = assemble_feature_matrix(news_features, market_features, sentiment_features, '2022-01-01', 'AAPL')
['[feature_matrix]', '['2022-01-01', '2022-01-02', ...']']
```
