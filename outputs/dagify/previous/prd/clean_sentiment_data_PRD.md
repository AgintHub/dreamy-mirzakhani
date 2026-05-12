# clean_sentiment_data PRD

## Description
Clean raw sentiment data.


## Conceptual Info

This node aims to clean raw sentiment data by removing entries with null scores and aggregating the rest by day.

## Docstring

### Summary
Clean sentiment data by removing null scores and aggregating by day.

### Returns

Tuple[List[float], List[float]]: Returns cleaned sentiment scores after cleaning and aggregated sentiment scores by day.

### Raises

- ValueError: Raised if the input data contains non-numeric sentiment scores.

### Examples

```python
>>> import pandas as pd
cleaned_sentiment_data, aggregated_sentiment
```
