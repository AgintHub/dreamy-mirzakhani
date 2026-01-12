from pydantic import BaseModel, Field
from typing import List


class ExtractSongMetadataOutput(BaseModel):
    """Pydantic model for extract_song_metadata node outputs."""
    song_title: str = Field(..., description="Title of the sampled song")
    artist_names: str = (
        Field(..., description="List of artist names associated with the sampled song")
    )
    album_info: str = (
        Field(..., description="Album information for the sampled song")
    )
    release_date: str = (
        Field(..., description="Release date of the sampled song")
    )
    genre_classifications: str = (
        Field(..., description="List of genre classifications for the sampled song")
    )
    tempo: float = (
        Field(..., description="Tempo of the sampled song in beats per minute (BPM)")
    )
    key: str = Field(..., description="Key of the sampled song")
    loudness: float = (
        Field(..., description="Loudness of the sampled song in decibels (dB)")
    )


class ListMusiciansOutput(BaseModel):
    """Pydantic model for list_musicians node outputs."""
    musician_ids: List[str] = (
        Field(..., description="List of unique identifiers for the musicians")
    )
    musician_names: List[str] = (
        Field(..., description="List of names of the musicians")
    )
    musician_aliases: List[str] = (
        Field(..., description="List of lists containing aliases for each musician")
    )
    is_deduplicated: bool = (
        Field(..., description="Whether the list of musicians has been deduplicated")
    )


def list_musicians(extract_song_metadata_input: ExtractSongMetadataOutput, **kwargs) -> ListMusiciansOutput:
    """
    Aggregates and deduplicates musicians from sampled song metadata.

    Parameters
    ----------
    song_metadata : List[Dict]
        Metadata of the sampled songs, including artist names and other
        relevant details extracted by the `extract_song_metadata` node.

    Returns
    -------
    Tuple[List[str], List[str], List[List[str]], bool]
        A tuple containing lists of musician IDs, names, aliases, and a
        boolean indicating whether the list has been deduplicated.

    Raises
    ------
    ValueError
        If the input metadata is malformed or missing critical information.

    Examples
    --------
    >>> song_metadata = [{'artist_names': ['Artist1', 'Artist2']},
    {'artist_names': ['Artist2', 'Artist3']}]
    >>> list_musicians(song_metadata)
    (['id1', 'id2', 'id3'], ['Artist1', 'Artist2', 'Artist3'], [['Alias1'],
    ['Alias2'], ['Alias3']], True)

    """
    return ListMusiciansOutput(
        musician_ids=[],
        musician_names=[],
        musician_aliases=[],
        is_deduplicated=False,
    )