from ._record_audio_snippet.initialize_microphone_capture import initialize_microphone_capture
from ._record_audio_snippet.check_microphone_permissions import check_microphone_permissions
from ._record_audio_snippet.capture_audio_from_microphone import capture_audio_from_microphone
from ._record_audio_snippet.normalize_audio_levels import normalize_audio_levels
from ._record_audio_snippet.trim_silence import trim_silence
from ._record_audio_snippet.apply_voice_activity_detection import apply_voice_activity_detection
from ._record_audio_snippet.extract_vad_confidence import extract_vad_confidence
from ._record_audio_snippet.encode_with_opus import encode_with_opus
from ._record_audio_snippet.convert_to_base64 import convert_to_base64
from ._record_audio_snippet.extract_audio_metadata import extract_audio_metadata
from ._record_audio_snippet.calculate_duration import calculate_duration
from ._record_audio_snippet.get_sample_rate import get_sample_rate
from ._record_audio_snippet.format_metadata_as_strings import format_metadata_as_strings

from pydantic import BaseModel, Field
from typing import List


class RecordAudioSnippetOutput(BaseModel):
    """Pydantic model for record_audio_snippet node outputs."""
    audio_data: str = (
        Field(..., description = (
            "Binary payload of the recorded audio snippet encoded with Opus")
        )
    )
    metadata: List[str] = (
        Field(..., description = (
            "List containing metadata information such as duration, sample rate, codec, and VAD confidence")
        )
    )
    duration: float = (
        Field(..., description = (
            "Duration of the recorded audio snippet in seconds")
        )
    )
    sample_rate: int = (
        Field(..., description="Sample rate of the recorded audio snippet")
    )
    codec: str = (
        Field(..., description="Codec used for encoding the audio snippet")
    )
    vad_confidence: float = (
        Field(..., description = (
            "Confidence score of the Voice Activity Detection")
        )
    )


def record_audio_snippet(general_input: str, **kwargs) -> RecordAudioSnippetOutput:
    """
    Records a short audio snippet from the user's microphone, normalizes and
    trims silence, optionally applies VAD, encodes the signal with Opus, and
    returns the binary payload with metadata.

    Returns
    -------
    dict
        Dictionary containing audio_data, metadata, duration, sample_rate,
        codec, and vad_confidence.

    Raises
    ------
    AudioCaptureError
        Raised when the audio capture hardware fails or the recording is
        interrupted.
    PermissionError
        Raised when the application does not have permission to access the
        microphone.

    Examples
    --------
    >>> result = record_audio_snippet()
    {
      "audio_data": "<binary base64>",
      "metadata": ["5.0", "48000", "Opus", "0.95"],
      "duration": 5.0,
      "sample_rate": 48000,
      "codec": "Opus",
      "vad_confidence": 0.95
    }

    >>> try:
  record_audio_snippet()
except PermissionError as e:
  print(e)
    PermissionError: Microphone access denied.

    """
    microphone_device = initialize_microphone_capture()
    check_microphone_permissions(device=microphone_device)
    
    raw_audio_data = capture_audio_from_microphone(device=microphone_device)
    normalized_audio = normalize_audio_levels(audio_data=raw_audio_data)
    trimmed_audio = trim_silence(audio_data=normalized_audio)
    
    vad_results = apply_voice_activity_detection(audio_data=trimmed_audio)
    vad_confidence_score: float = extract_vad_confidence(vad_results=vad_results)
    
    opus_encoded_data = encode_with_opus(audio_data=trimmed_audio)
    base64_audio: str = convert_to_base64(binary_data=opus_encoded_data)
    
    audio_metadata = extract_audio_metadata(audio_data=trimmed_audio)
    duration_seconds: float = calculate_duration(audio_data=trimmed_audio)
    sample_rate_hz: int = get_sample_rate(audio_data=trimmed_audio)
    
    metadata_list: List[str] = format_metadata_as_strings(
        duration=duration_seconds,
        sample_rate=sample_rate_hz,
        codec="Opus",
        vad_confidence=vad_confidence_score
    )
    
    return RecordAudioSnippetOutput(
        audio_data=base64_audio,
        metadata=metadata_list,
        duration=duration_seconds,
        sample_rate=sample_rate_hz,
        codec="Opus",
        vad_confidence=vad_confidence_score
    )