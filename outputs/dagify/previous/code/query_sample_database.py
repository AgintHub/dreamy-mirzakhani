from pydantic import BaseModel, Field
from typing import List


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


class BuildSampleDatabaseOutput(BaseModel):
    """Pydantic model for build_sample_database node outputs."""
    database_id: str = (
        Field(..., description="Unique identifier for the sample database")
    )
    sample_count: int = (
        Field(..., description="Number of song samples in the database")
    )
    audio_features: List[str] = (
        Field(..., description="List of audio features extracted for each sample (e.g., spectrograms, MFCCs, chroma features)")
    )
    sample_ids: List[str] = (
        Field(..., description="List of unique identifiers for each song sample in the database")
    )


class QuerySampleDatabaseOutput(BaseModel):
    """Pydantic model for query_sample_database node outputs."""
    matching_samples: List[str] = (
        Field(..., description="List of potential matching song samples")
    )
    sample_confidence_scores: List[float] = (
        Field(..., description="List of confidence scores for each matching sample")
    )
    query_status: bool = (
        Field(..., description="Whether the query was successful")
    )


def query_sample_database(extract_audio_features_input: ExtractAudioFeaturesOutput, build_sample_database_input: BuildSampleDatabaseOutput, **kwargs) -> QuerySampleDatabaseOutput:
    """
    Query the sample database to find matching song samples based on extracted
    audio features.

    Parameters
    ----------
    audio_features : dict
        Dictionary containing spectrogram, mfccs, and chroma features of the
        audio snippet.
    database_id : str
        Unique identifier for the sample database.

    Returns
    -------
    dict
        Dictionary containing a list of potential matching song samples,
        their confidence scores, and query status.

    Raises
    ------
    ValueError
        If audio features or database ID are missing or invalid.

    Examples
    --------
    >>> audio_features = {'spectrogram': [1, 2, 3], 'mfccs': [4, 5, 6],
    'chroma_features': [7, 8, 9]}
    >>> database_id = 'sample_db_1'
    >>> result = query_sample_database(audio_features, database_id)
    {'matching_samples': ['song1', 'song2'], 'sample_confidence_scores': [0.8,
    0.9], 'query_status': True}

    """
    return QuerySampleDatabaseOutput(
        matching_samples=[],
        sample_confidence_scores=[],
        query_status=False,
    )