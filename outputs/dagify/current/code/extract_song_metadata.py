from pydantic import BaseModel, Field


class IdentifySampledSongsOutput(BaseModel):
    """Pydantic model for identify_sampled_songs node outputs."""
    track_id: str = (
        Field(..., description="Unique identifier for the candidate track in the database.")
    )
    confidence: float = (
        Field(..., description="Confidence score (0.0 to 1.0) indicating the likelihood that the candidate matches the sampled snippet.")
    )
    start_time: float = (
        Field(..., description="Start timestamp (in seconds) of the matched segment within the sampled snippet.")
    )
    end_time: float = (
        Field(..., description="End timestamp (in seconds) of the matched segment within the sampled snippet.")
    )
    artist_name: str = (
        Field(..., description="Name of the artist of the candidate track.")
    )
    track_title: str = Field(..., description="Title of the candidate track.")
    release_date: str = (
        Field(..., description="Release date of the candidate track (ISO 8601 format).")
    )


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


def extract_song_metadata(identify_sampled_songs_input: IdentifySampledSongsOutput, **kwargs) -> ExtractSongMetadataOutput:
    """
    Extracts detailed metadata for each sampled song candidate.

    Parameters
    ----------
    candidate_tracks : List[dict]
        List of candidate track objects returned by identify_sampled_songs.
        Each object must contain at least 'track_id', 'confidence',
        'start_time', 'end_time', and 'metadata' (which includes
        'artist_name', 'track_title', 'release_date').

    Returns
    -------
    List[dict]
        A list of metadata dictionaries, each containing the fields:
        song_title (str), artist_names (List[str]), album_info (str),
        release_date (str), genre_classifications (List[str]), tempo
        (float), key (str), loudness (float).

    Raises
    ------
    ValueError
        If candidate_tracks is empty or missing required fields.
    RuntimeError
        If external API calls (Discogs, MusicBrainz, Spotify) fail or return
        inconsistent data.

    Examples
    --------
    >>> candidate_tracks = [{
    ...   'track_id': '12345',
    ...   'confidence': 0.92,
    ...   'start_time': 12.3,
    ...   'end_time': 45.6,
    ...   'metadata': {
    ...     'artist_name': 'The Sample Artists',
    ...     'track_title': 'Sample Tune',
    ...     'release_date': '2020-07-15'
    ...   }
    >>> }
    [{\n  'song_title': 'Sample Tune',\n  'artist_names': ['The Sample
    Artists'],\n  'album_info': 'Unknown Album',\n  'release_date':
    '2020-07-15',\n  'genre_classifications': ['Electronic', 'House'],\n
    'tempo': 128.0,\n  'key': 'C minor',\n  'loudness': -5.2\n}]

    >>> candidate_tracks = [{
    ...   'track_id': '67890',
    ...   'confidence': 0.85,
    ...   'start_time': 0.0,
    ...   'end_time': 30.0,
    ...   'metadata': {
    ...     'artist_name': 'Another Artist',
    ...     'track_title': 'Another Sample',
    ...     'release_date': '2018-03-22'
    ...   }
    >>> }
    [{\n  'song_title': 'Another Sample',\n  'artist_names': ['Another
    Artist'],\n  'album_info': 'Unknown Album',\n  'release_date':
    '2018-03-22',\n  'genre_classifications': ['Pop'],\n  'tempo': 110.0,\n
    'key': 'G major',\n  'loudness': -7.8\n}]

    """
    return ExtractSongMetadataOutput(
        song_title="",
        artist_names="",
        album_info="",
        release_date="",
        genre_classifications="",
        tempo=0.0,
        key="",
        loudness=0.0,
    )