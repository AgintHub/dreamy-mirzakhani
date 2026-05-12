# clean_news_data PRD

## Description
Clean raw news data.


## Conceptual Info

This node cleans raw news data by deduplicating items, removing non-English articles, and timestamping them.

## Docstring

### Summary
Clean news data by deduplicating items, removing non-English articles, and timestamping them.

### Parameters

- **news_data** (List[str]): Raw news data as a list of JSON files.

### Returns

Dict[str, List[str]]: Cleaned news data with deduplicated items, removed non-English articles, and timestamped.

### Examples

```python
>>> clean_news_data = clean_news_data(news_data)
{'cleaned_news': ['file1.json', 'file2.json'], 'count_duplicate_items': [2], 'count_non_english_articles': [1], 'timestamp_news': ['2022-01-01', '2022-01-02']}
```
