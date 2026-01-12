# hybrid_url_ranking PRD

## Description
Ranks URLs based on hybrid predictions from NLP candidates and ML predictions.


## Conceptual Info

This shim node is responsible for combining NLP candidates and ML predictions to rank URLs, playing a crucial role in determining the most likely official URLs for musicians.

## Docstring

### Summary
Ranks URLs by integrating NLP candidates and ML predictions into a hybrid ranking system.

### Parameters

- **nlp_candidates** (str): Serialized string representing a list of NLP candidates for URL resolution.
- **ml_predictions** (str): Serialized string representing a list of ML predictions for URL resolution.

### Returns

List[str]: A list of URLs ranked according to the hybrid prediction model.

### Raises

- ValueError: If the input strings cannot be deserialized into lists.
- TypeError: If the input parameters are not strings.

### Examples

```python
>>> import json
>>> nlp_cands = json.dumps(['https://example1.com', 'https://example2.com'])
>>> ml_preds = json.dumps(['https://example1.com', 'https://example3.com'])
>>> hybrid_url_ranking(nlp_candidates=nlp_cands, ml_predictions=ml_preds)
['https://example1.com', 'https://example2.com', 'https://example3.com']
```

```python
>>> import json
>>> nlp_cands = json.dumps(['https://test1.com'])
>>> ml_preds = json.dumps(['https://test1.com', 'https://test2.com'])
>>> hybrid_url_ranking(nlp_candidates=nlp_cands, ml_predictions=ml_preds)
['https://test1.com', 'https://test2.com']
```
