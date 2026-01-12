from pydantic import BaseModel, Field
from typing import List


class LoadAudioSnippetOutput(BaseModel):
    """Pydantic model for load_audio_snippet node outputs."""
    audio_file_path: str = (
        Field(..., description="Path to the loaded audio file")
    )
    audio_features: List[float] = (
        Field(..., description="Extracted audio features such as spectrograms or MFCCs")
    )
    loading_status: bool = (
        Field(..., description="Whether the audio file was loaded successfully")
    )


class ExtractAudioFeaturesOutput(BaseModel):
    """Pydantic model for extract_audio_features node outputs."""
    spectrogram: List[float] = (
        Field(..., description="Spectrogram features of the audio snippet")
    )
    mfccs: List[float] = (
        Field(..., description="Mel-frequency cepstral coefficients (MFCCs) of the audio snippet")
    )
    chroma_features: List[float] = (
        Field(..., description="Chroma features of the audio snippet")
    )
    feature_extraction_status: bool = (
        Field(..., description="Whether the feature extraction was successful")
    )


def extract_audio_features(load_audio_snippet_input: LoadAudioSnippetOutput, **kwargs) -> ExtractAudioFeaturesOutput:
    """
    Extracts spectrogram, MFCCs, and chroma features from an audio snippet.

    Parameters
    ----------
    audio_snippet : dict
        Loaded audio snippet with its path and features.

    Returns
    -------
    dict
        A dictionary containing spectrogram, MFCCs, chroma features, and
        feature extraction status.

    Raises
    ------
    Exception
        If there's an error in feature extraction.

    Examples
    --------
    >>> audio_snippet = {'audio_file_path': '/path/to/audio.wav',
    'audio_features': [...] }
    >>> features = extract_audio_features(audio_snippet)
    {'spectrogram': [...], 'mfccs': [...], 'chroma_features': [...],
    'feature_extraction_status': True}

    """
    return ExtractAudioFeaturesOutput(
        spectrogram=[],
        mfccs=[],
        chroma_features=[],
        feature_extraction_status=False,
    )