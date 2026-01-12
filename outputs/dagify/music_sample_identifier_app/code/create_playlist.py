from pydantic import BaseModel, Field
from typing import List


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


class CreatePlaylistOutput(BaseModel):
    """Pydantic model for create_playlist node outputs."""
    playlist_id: str = (
        Field(..., description="Unique identifier for the generated playlist")
    )
    track_ids: List[str] = (
        Field(..., description="List of track identifiers included in the playlist")
    )
    playlist_name: str = (
        Field(..., description="Name of the generated playlist")
    )
    playlist_description: str = (
        Field(..., description="Description of the playlist, including its theme and coherence")
    )
    artist_diversity_score: float = (
        Field(..., description="Score representing the diversity of artists in the playlist")
    )
    genre_representation: List[str] = (
        Field(..., description="List of genres represented in the playlist")
    )


def create_playlist(list_musicians_input: ListMusiciansOutput, **kwargs) -> CreatePlaylistOutput:
    """
    Creates a playlist by analyzing sampled songs' metadata, applying NLP and
    collaborative filtering, and ranking tracks based on a graph-based model.

    Parameters
    ----------
    musician_ids : List[str]
        List of unique identifiers for the musicians, derived from the
        `list_musicians` node.
    musician_names : List[str]
        List of names of the musicians, used to inform the playlist's
        thematic coherence.
    musician_aliases : List[List[str]]
        List of lists containing aliases for each musician, aiding in
        disambiguation and comprehensive coverage.

    Returns
    -------
    Dict[str, Union[str, List[str], float]]
        A dictionary containing the generated playlist's details, including
        its ID, track IDs, name, description, artist diversity score, and
        genre representation.

    Raises
    ------
    ValueError
        If the input lists (`musician_ids`, `musician_names`,
        `musician_aliases`) are inconsistent or empty.
    RuntimeError
        If the graph-based ranking algorithm fails to converge or if there's
        an issue with the MIR framework.

    Examples
    --------
    >>> create_playlist(musician_ids=['M1', 'M2'], musician_names=['Artist1',
    'Artist2'], musician_aliases=[['A1'], ['A2']])
    {'playlist_id': 'P1', 'track_ids': ['T1', 'T2'], 'playlist_name': 'Diverse
    Playlist', 'playlist_description': 'A mix of genres',
    'artist_diversity_score': 0.8, 'genre_representation': ['Rock', 'Pop']}

    """
    return CreatePlaylistOutput(
        playlist_id="",
        track_ids=[],
        playlist_name="",
        playlist_description="",
        artist_diversity_score=0.0,
        genre_representation=[],
    )