# format_metadata_as_strings PRD

## Description
Converts audio metadata into a list of string representations.


## Conceptual Info

This shim node is responsible for taking in various audio metadata parameters and formatting them into a list of string representations, which can be used for further processing or output.

## Docstring

### Summary
Formats the given audio metadata into a list of string representations.

### Parameters

- **duration** (float): The duration of the audio snippet in seconds.
- **sample_rate** (int): The sample rate of the audio snippet in Hz.
- **codec** (str): The codec used for encoding the audio snippet.
- **vad_confidence** (float): The confidence score of the Voice Activity Detection.

### Returns

List[str]: A list containing string representations of the input metadata in the order they were received.

### Raises

- TypeError: If any of the input parameters are of the wrong type.
- ValueError: If any of the input values are invalid (e.g., negative duration or sample rate).

### Examples

```python
>>> format_metadata_as_strings(duration=3.2, sample_rate=48000, codec='Opus', vad_confidence=0.85)
['Duration: 3.2 seconds', 'Sample Rate: 48000 Hz', 'Codec: Opus', 'VAD Confidence: 0.85']
```

```python
>>> format_metadata_as_strings(duration=1.1, sample_rate=16000, codec='Opus', vad_confidence=0.92)
['Duration: 1.1 seconds', 'Sample Rate: 16000 Hz', 'Codec: Opus', 'VAD Confidence: 0.92']
```
