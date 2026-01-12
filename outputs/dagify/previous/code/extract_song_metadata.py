from ._extract_song_metadata.validate_track_data import validate_track_data
from ._extract_song_metadata.fetch_discogs_metadata import fetch_discogs_metadata
from ._extract_song_metadata.fetch_musicbrainz_metadata import fetch_musicbrainz_metadata
from ._extract_song_metadata.fetch_spotify_metadata import fetch_spotify_metadata
from ._extract_song_metadata.merge_metadata_sources import merge_metadata_sources
from ._extract_song_metadata.extract_audio_features import extract_audio_features
from ._extract_song_metadata.normalize_artist_names import normalize_artist_names
from ._extract_song_metadata.extract_album_info import extract_album_info
from ._extract_song_metadata.classify_genres import classify_genres
from ._extract_song_metadata.validate_metadata_consistency import validate_metadata_consistency

from pydantic import BaseModel, Field


class IdentifySampledSongsOutput(BaseModel):
    """Pydantic model for identify_sampled_songs node outputs."""
    track_id: str = (
        Field(..., description = (
            "Unique identifier for the candidate track in the database.")
        )
    )
    confidence: float = (
        Field(..., description = (
            "Confidence score (0.0 to 1.0) indicating the likelihood that the candidate matches the sampled snippet.")
        )
    )
    start_time: float = (
        Field(..., description = (
            "Start timestamp (in seconds) of the matched segment within the sampled snippet.")
        )
    )
    end_time: float = (
        Field(..., description = (
            "End timestamp (in seconds) of the matched segment within the sampled snippet.")
        )
    )
    artist_name: str = (
        Field(..., description="Name of the artist of the candidate track.")
    )
    track_title: str = Field(..., description="Title of the candidate track.")
    release_date: str = (
        Field(..., description = (
            "Release date of the candidate track (ISO 8601 format).")
        )
    )


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
    validate_track_data(track_data=identify_sampled_songs_input)
    
    discogs_data: dict = fetch_discogs_metadata(track_id=identify_sampled_songs_input.track_id, artist=identify_sampled_songs_input.artist_name, title=identify_sampled_songs_input.track_title)
    
    musicbrainz_data: dict = fetch_musicbrainz_metadata(track_id=identify_sampled_songs_input.track_id, artist=identify_sampled_songs_input.artist_name, title=identify_sampled_songs_input.track_title)
    
    spotify_data: dict = fetch_spotify_metadata(track_id=identify_sampled_songs_input.track_id, artist=identify_sampled_songs_input.artist_name, title=identify_sampled_songs_input.track_title)
    
    merged_metadata: dict = merge_metadata_sources(discogs=discogs_data, musicbrainz=musicbrainz_data, spotify=spotify_data)
    
    audio_features: dict = extract_audio_features(track_id=identify_sampled_songs_input.track_id, start_time=identify_sampled_songs_input.start_time, end_time=identify_sampled_songs_input.end_time)
    
    normalized_artists: str = normalize_artist_names(raw_artists=merged_metadata.get('artists', identify_sampled_songs_input.artist_name))
    
    album_info: str = extract_album_info(metadata=merged_metadata)
    
    genre_list: str = classify_genres(metadata=merged_metadata, audio_features=audio_features)
    
    validated_metadata: dict = validate_metadata_consistency(metadata=merged_metadata, audio_features=audio_features)
    
    return ExtractSongMetadataOutput(
        song_title=identify_sampled_songs_input.track_title,
        artist_names=normalized_artists,
        album_info=album_info,
        release_date=identify_sampled_songs_input.release_date,
        genre_classifications=genre_list,
        tempo=audio_features.get('tempo', 120.0),
        key=audio_features.get('key', 'C major'),
        loudness=audio_features.get('loudness', -6.0)
    )