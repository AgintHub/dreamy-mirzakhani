# engineer_news_features PRD

## Description
Create news‑based feature set.


## Conceptual Info

This node is responsible for taking in cleaned news data and leveraging NLP techniques to extract relevant news features, key topics, sentiment polarity, and keyword frequencies.

## Docstring

### Summary
Engineer news features by applying NLP techniques to cleaned news data.

### Parameters

- **clean_news_data** (PrimitiveType.LIST_STR): Cleaned news data in JSON format.

### Returns

PrimitiveType.LIST_FLOAT(feature_matrix) and PrimitiveType.LIST_STR(key_topics) and PrimitiveType.LIST_FLOAT(sentiment_polarity) and PrimitiveType.LIST_INT(keyword_frequencies): Extracted news features, key topics, sentiment polarity, and keyword frequencies for each asset in the universe.

### Raises

- ValueError: If input data is malformed or corrupted.

### Examples

```python
>>> clean_news_data = [
                  {'asset_id': 'AAPL', 'article_body': 'The company is doing well.'},
                  {'asset_id': 'AAPL', 'article_body': 'The company is doing poorly.'}
                ]
>>> engineer_news_features(clean_news_data)
feature_matrix: [0.4, 0.3], key_topics: ['financial performance'], sentiment_polarity: [0.4, -0.2], keyword_frequencies: [1, 2]
```
