from pydantic import BaseModel, Field
from typing import List


class RecordAudioSnippetOutput(BaseModel):
    """Pydantic model for record_audio_snippet node outputs."""
    audio_data: str = (
        Field(..., description="Binary payload of the recorded audio snippet encoded with Opus")
    )
    metadata: List[str] = (
        Field(..., description="List containing metadata information such as duration, sample rate, codec, and VAD confidence")
    )
    duration: float = (
        Field(..., description="Duration of the recorded audio snippet in seconds")
    )
    sample_rate: int = (
        Field(..., description="Sample rate of the recorded audio snippet")
    )
    codec: str = (
        Field(..., description="Codec used for encoding the audio snippet")
    )
    vad_confidence: float = (
        Field(..., description="Confidence score of the Voice Activity Detection")
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
    return RecordAudioSnippetOutput(
        audio_data="",
        metadata=[],
        duration=0.0,
        sample_rate=0,
        codec="",
        vad_confidence=0.0,
    )