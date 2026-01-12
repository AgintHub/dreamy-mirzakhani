from ._list_musicians.validate_metadata_structure import validate_metadata_structure
from ._list_musicians.extract_artist_names_from_metadata import extract_artist_names_from_metadata
from ._list_musicians.normalize_artist_names import normalize_artist_names
from ._list_musicians.deduplicate_artist_list import deduplicate_artist_list
from ._list_musicians.generate_musician_ids import generate_musician_ids
from ._list_musicians.fetch_musician_aliases import fetch_musician_aliases
from ._list_musicians.check_deduplication_occurred import check_deduplication_occurred

from pydantic import BaseModel, Field
from typing import List


class ExtractSongMetadataOutput(BaseModel):
    """Pydantic model for extract_song_metadata node outputs."""
    song_title: str = Field(..., description="Title of the sampled song")
    artist_names: str = (
        Field(..., description = (
            "List of artist names associated with the sampled song")
        )
    )
    album_info: str = (
        Field(..., description="Album information for the sampled song")
    )
    release_date: str = (
        Field(..., description="Release date of the sampled song")
    )
    genre_classifications: str = (
        Field(..., description = (
            "List of genre classifications for the sampled song")
        )
    )
    tempo: float = (
        Field(..., description = (
            "Tempo of the sampled song in beats per minute (BPM)")
        )
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
        Field(..., description = (
            "List of lists containing aliases for each musician")
        )
    )
    is_deduplicated: bool = (
        Field(..., description = (
            "Whether the list of musicians has been deduplicated")
        )
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
    validated_metadata: dict = validate_metadata_structure(metadata=extract_song_metadata_input)
    raw_artist_names: List[str] = extract_artist_names_from_metadata(metadata=validated_metadata)
    normalized_names: List[str] = normalize_artist_names(names=raw_artist_names)
    deduplicated_names: List[str] = deduplicate_artist_list(names=normalized_names)
    musician_ids: List[str] = generate_musician_ids(names=deduplicated_names)
    musician_aliases: List[str] = fetch_musician_aliases(names=deduplicated_names)
    is_deduplicated: bool = check_deduplication_occurred(original=normalized_names, deduplicated=deduplicated_names)
    return ListMusiciansOutput(
        musician_ids=musician_ids,
        musician_names=deduplicated_names,
        musician_aliases=musician_aliases,
        is_deduplicated=is_deduplicated
    )