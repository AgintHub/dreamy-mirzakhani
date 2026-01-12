# rank_and_filter_matches PRD

## Description
Rank and filter the matching samples based on similarity


## Conceptual Info

This node ranks and filters matching samples based on their similarity to the input audio snippet.

## Docstring

### Summary
Ranks and filters the matching samples based on their similarity to the input audio snippet.

### Parameters

- **matching_samples** (List[str]): List of potential matching song samples from the query_sample_database node
- **sample_confidence_scores** (List[float]): List of confidence scores for each matching sample from the query_sample_database node

### Returns

tuple: A tuple containing the list of IDs of the matching samples, the list of similarity scores corresponding to the matching samples, and a boolean indicating whether the output is valid

### Raises

- ValueError: If the input lists are empty or of different lengths

### Examples

```python
>>> matching_samples = ['sample1', 'sample2', 'sample3']
>>> sample_confidence_scores = [0.8, 0.6, 0.4]
>>> sample_ids, similarity_scores, is_valid = rank_and_filter_matches(matching_samples, sample_confidence_scores)
(['sample1', 'sample2'], [0.8, 0.6], true)
```
