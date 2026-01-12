# extract_vad_confidence PRD

## Description
Extracts the confidence score from Voice Activity Detection results.


## Conceptual Info

This shim function is designed to process the output of a Voice Activity Detection algorithm and extract a confidence score, which is then used in further audio processing pipelines.

## Docstring

### Summary
Extracts the confidence score from the output of a Voice Activity Detection algorithm.

### Parameters

- **vad_results** (str): A string containing the results of the Voice Activity Detection algorithm.

### Returns

float: The confidence score extracted from the VAD results as a float value between 0 and 1.

### Raises

- ValueError: If the input string is not in the expected format or if the confidence score cannot be extracted.
- TypeError: If the input is not a string.

### Examples

```python
>>> vad_results = '{\"confidence\": 0.8, \"other_data\": \"some_value\"}'
>>> confidence_score = extract_vad_confidence(vad_results)
>>> print(confidence_score)
0.8
```

```python
>>> vad_results = '{\"confidence\": 0.4}'
>>> confidence_score = extract_vad_confidence(vad_results)
>>> print(confidence_score)
0.4
```
