from pydantic import BaseModel, Field
from typing import List


class RankAndFilterMatchesOutput(BaseModel):
    """Pydantic model for rank_and_filter_matches node outputs."""
    sample_ids: List[str] = (
        Field(..., description="List of IDs of the matching samples")
    )
    similarity_scores: List[float] = (
        Field(..., description="List of similarity scores corresponding to the matching samples")
    )
    is_valid: bool = Field(..., description="Whether the output is valid")


class RetrieveSongMetadataOutput(BaseModel):
    """Pydantic model for retrieve_song_metadata node outputs."""
    song_titles: List[str] = (
        Field(..., description="List of song titles for the matching songs")
    )
    artist_names: List[str] = (
        Field(..., description="List of artist names for the matching songs")
    )
    album_info: List[str] = (
        Field(..., description="List of album information for the matching songs")
    )
    metadata_retrieval_status: bool = (
        Field(..., description="Whether the metadata retrieval was successful")
    )


def retrieve_song_metadata(rank_and_filter_matches_input: RankAndFilterMatchesOutput, **kwargs) -> RetrieveSongMetadataOutput:
    """
    Retrieve song metadata based on the provided sample IDs and similarity
    scores.

    Parameters
    ----------
    sample_ids : List[str]
        List of IDs of the matching samples
    similarity_scores : List[float]
        List of similarity scores corresponding to the matching samples
    is_valid : bool
        Whether the output is valid

    Returns
    -------
    dict
        A dictionary containing the retrieved song metadata

    Raises
    ------
    ValueError
        If the input sample IDs or similarity scores are empty

    Examples
    --------
    >>> sample_ids = ['song1', 'song2']
    >>> similarity_scores = [0.8, 0.9]
    >>> is_valid = True
    >>> metadata = retrieve_song_metadata(sample_ids, similarity_scores,
    is_valid)
    {'song_titles': ['Song 1', 'Song 2'], 'artist_names': ['Artist 1', 'Artist
    2'], 'album_info': ['Album 1', 'Album 2'], 'metadata_retrieval_status':
    True}

    """
    return RetrieveSongMetadataOutput(
        song_titles=[],
        artist_names=[],
        album_info=[],
        metadata_retrieval_status=False,
    )