from pydantic import BaseModel, Field
from typing import List


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


def build_sample_database(general_input: str, **kwargs) -> BuildSampleDatabaseOutput:
    """
    Creates a database of known song samples with their corresponding audio
    features.

    Returns
    -------
    {database_id: str, sample_count: int, audio_features: List[str], sample_ids: List[str]}
        A dictionary containing the database_id, sample_count,
        audio_features, and sample_ids.

    Raises
    ------
    Exception
        If there is an issue gathering the dataset or storing it in the
        database.

    Examples
    --------
    >>> build_sample_database()
    {'database_id': 'db123', 'sample_count': 1000, 'audio_features':
    ['spectrogram', 'mfcc', 'chroma'], 'sample_ids': ['sample1', 'sample2',
    ...]}

    """
    return BuildSampleDatabaseOutput(
        database_id="",
        sample_count=0,
        audio_features=[],
        sample_ids=[],
    )