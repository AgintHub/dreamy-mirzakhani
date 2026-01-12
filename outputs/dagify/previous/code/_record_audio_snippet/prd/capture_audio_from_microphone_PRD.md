# capture_audio_from_microphone PRD

## Description
Captures raw audio data from the specified microphone device.


## Conceptual Info

This shim function is responsible for capturing raw audio data from a specified microphone device. It plays a crucial role in the audio processing pipeline by providing the initial raw audio data that will be further processed, normalized, and encoded.

## Docstring

### Summary
Captures raw audio data from the specified microphone device and returns it as a string.

### Parameters

- **device** (str): The name or identifier of the microphone device to capture audio from.

### Returns

str: The raw audio data captured from the microphone as a string.

### Raises

- ValueError: If the specified device is not a valid microphone device.
- RuntimeError: If there is an issue capturing audio from the device.

### Examples

```python
>>> capture_audio_from_microphone(device='default_microphone')
'raw_audio_data_as_string'
```

```python
>>> capture_audio_from_microphone(device='external_usb_microphone')
'another_raw_audio_data_as_string'
```
