from pydantic import BaseModel, Field
from typing import List


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


class GenerateSongLinksOutput(BaseModel):
    """Pydantic model for generate_song_links node outputs."""
    song_titles: List[str] = Field(..., description="List of song titles")
    artist_names: List[str] = Field(..., description="List of artist names")
    album_info: List[str] = Field(..., description="List of album information")
    musician_page_links: List[str] = (
        Field(..., description="List of links to the musicians' pages")
    )
    streaming_platform_links: List[str] = (
        Field(..., description="List of links to the songs on music streaming platforms")
    )


def generate_song_links(retrieve_song_metadata_input: RetrieveSongMetadataOutput, **kwargs) -> GenerateSongLinksOutput:
    """
    Generate links to musicians' pages using the retrieved metadata.

    Parameters
    ----------
    song_metadata : dict
        Dictionary containing song metadata (song titles, artist names,
        album information)

    Returns
    -------
    dict
        Dictionary containing song titles, artist names, album information,
        musician page links, and streaming platform links

    Raises
    ------
    ValueError
        If the input metadata is invalid or incomplete

    Examples
    --------
    >>> song_metadata = {
    ...     'song_titles': ['Song 1', 'Song 2'],
    ...     'artist_names': ['Artist 1', 'Artist 2'],
    ...     'album_info': ['Album 1', 'Album 2']
    >>> }
    >>> result = generate_song_links(song_metadata)
    {'song_titles': ['Song 1', 'Song 2'], 'artist_names': ['Artist 1', 'Artist
    2'], 'album_info': ['Album 1', 'Album 2'], 'musician_page_links':
    ['https://example.com/artist1', 'https://example.com/artist2'],
    'streaming_platform_links': ['https://example.com/song1',
    'https://example.com/song2']}

    """
    return GenerateSongLinksOutput(
        song_titles=[],
        artist_names=[],
        album_info=[],
        musician_page_links=[],
        streaming_platform_links=[],
    )