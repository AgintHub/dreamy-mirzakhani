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


class PreprocessAudioDataOutput(BaseModel):
    """Pydantic model for preprocess_audio_data node outputs."""
    processed_audio_base64: str = (
        Field(..., description = (
            "Base64-encoded binary payload of the processed audio ready for downstream consumption.")
        )
    )
    duration_seconds: float = (
        Field(..., description = (
            "Total duration of the processed audio in seconds.")
        )
    )
    sample_rate_hz: int = (
        Field(..., description="Sampling rate of the processed audio in Hertz.")
    )
    codec: str = (
        Field(..., description = (
            "Audio codec used for encoding the processed audio (e.g., Opus, PCM).")
        )
    )
    vad_confidence: float = (
        Field(..., description = (
            "Confidence score (0.0\u20131.0) of Voice Activity Detection applied during preprocessing.")
        )
    )
    noise_reduction_method: str = (
        Field(..., description = (
            "Method used for noise reduction (e.g., spectral_subtraction, wiener_filter, deep_learning).")
        )
    )
    normalization_method: str = (
        Field(..., description = (
            "Method used for audio normalization (e.g., peak_normalization, loudness_normalization).")
        )
    )
    feature_vectors: List[float] = (
        Field(..., description = (
            "Flattened list of extracted audio feature vectors (e.g., MFCCs, chroma, spectral contrast).")
        )
    )
    processing_success: bool = (
        Field(..., description = (
            "Indicates whether the preprocessing pipeline completed successfully without critical errors.")
        )
    )


def preprocess_audio_data(record_audio_snippet_input: RecordAudioSnippetOutput, **kwargs) -> PreprocessAudioDataOutput:
    """
    Executes a multi-stage audio preprocessing pipeline on recorded audio data,
    applying noise reduction, normalization, and feature extraction.

    Parameters
    ----------
    audio_data : str
        Base64-encoded binary payload of the recorded audio snippet.
    metadata : List[str]
        List containing metadata information such as duration, sample rate,
        codec, and VAD confidence.

    Returns
    -------
    Dict[str, Union[str, float, int, List[float], bool]]
        A dictionary containing the processed audio data, metadata, and
        processing results.

    Raises
    ------
    ValueError
        If the input audio data is invalid or corrupted.
    RuntimeError
        If an error occurs during the preprocessing pipeline.

    Examples
    --------
    >>> audio_data = 'base64_encoded_audio_data'
    >>> metadata = ['duration: 5.0', 'sample_rate: 48000', 'codec: Opus',
    'vad_confidence: 0.8']
    >>> result = preprocess_audio_data(audio_data, metadata)
    {'processed_audio_base64': 'processed_base64_data', 'duration_seconds': 5.0,
    'sample_rate_hz': 48000, 'codec': 'Opus', 'vad_confidence': 0.8,
    'noise_reduction_method': 'spectral_subtraction', 'normalization_method':
    'peak_normalization', 'feature_vectors': [0.1, 0.2, 0.3],
    'processing_success': True}

    """
    return PreprocessAudioDataOutput(
        processed_audio_base64="",
        duration_seconds=0.0,
        sample_rate_hz=0,
        codec="",
        vad_confidence=0.0,
        noise_reduction_method="",
        normalization_method="",
        feature_vectors=[],
        processing_success=False,
    )