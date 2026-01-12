from pydantic import BaseModel, Field
from typing import List


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


class OfferPlaylistToUserOutput(BaseModel):
    """Pydantic model for offer_playlist_to_user node outputs."""
    playlist_id: str = (
        Field(..., description="Unique identifier for the generated playlist.")
    )
    total_duration_seconds: int = (
        Field(..., description="Total duration of the playlist in seconds.")
    )
    track_count: int = (
        Field(..., description="Number of tracks included in the playlist.")
    )
    genre_list: List[str] = (
        Field(..., description="Ordered list of genres represented in the playlist.")
    )
    genre_counts: List[int] = (
        Field(..., description="Parallel list indicating the number of tracks per genre in genre_list.")
    )
    playback_available: bool = (
        Field(..., description="Indicates whether real\u2011time playback is enabled for the playlist.")
    )
    save_successful: bool = (
        Field(..., description="Indicates whether the save operation to the user\u2019s library succeeded.")
    )
    telemetry_log_id: str = (
        Field(..., description="Identifier for the telemetry log entry created for this playlist interaction.")
    )


def offer_playlist_to_user(create_playlist_input: CreatePlaylistOutput, **kwargs) -> OfferPlaylistToUserOutput:
    """
    Renders a playlist UI, enables playback and saving, and logs user
    interactions.

    Parameters
    ----------
    playlist_data : dict
        JSON payload from the 'create_playlist' node containing playlist
        details.

    Returns
    -------
    dict
        Output containing playlist ID, duration, track count, genre
        information, playback and save status, and telemetry log ID.

    Raises
    ------
    OAuth2Error
        If OAuth2 token is expired or invalid.
    PlaybackError
        If real-time playback fails.
    SaveError
        If saving to user's library fails.

    Examples
    --------
    >>> playlist_data = {'playlist_id': '123', 'tracks': [...]}
    >>> result = offer_playlist_to_user(playlist_data)
    {'playlist_id': '123', 'total_duration_seconds': 3600, 'track_count': 10,
    'genre_list': ['pop', 'rock'], 'genre_counts': [5, 5], 'playback_available':
    True, 'save_successful': True, 'telemetry_log_id': 'log_001'}

    """
    return OfferPlaylistToUserOutput(
        playlist_id="",
        total_duration_seconds=0,
        track_count=0,
        genre_list=[],
        genre_counts=[],
        playback_available=False,
        save_successful=False,
        telemetry_log_id="",
    )