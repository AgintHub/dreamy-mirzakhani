from ._offer_playlist_to_user.validate_oauth_token import validate_oauth_token
from ._offer_playlist_to_user.fetch_track_metadata import fetch_track_metadata
from ._offer_playlist_to_user.calculate_total_duration import calculate_total_duration
from ._offer_playlist_to_user.analyze_genre_distribution import analyze_genre_distribution
from ._offer_playlist_to_user.render_playlist_ui import render_playlist_ui
from ._offer_playlist_to_user.enable_realtime_playback import enable_realtime_playback
from ._offer_playlist_to_user.save_to_user_library import save_to_user_library
from ._offer_playlist_to_user.log_user_interaction import log_user_interaction

from pydantic import BaseModel, Field
from typing import List


class CreatePlaylistOutput(BaseModel):
    """Pydantic model for create_playlist node outputs."""
    playlist_id: str = (
        Field(..., description="Unique identifier for the generated playlist")
    )
    track_ids: List[str] = (
        Field(..., description = (
            "List of track identifiers included in the playlist")
        )
    )
    playlist_name: str = (
        Field(..., description="Name of the generated playlist")
    )
    playlist_description: str = (
        Field(..., description = (
            "Description of the playlist, including its theme and coherence")
        )
    )
    artist_diversity_score: float = (
        Field(..., description = (
            "Score representing the diversity of artists in the playlist")
        )
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
        Field(..., description = (
            "Ordered list of genres represented in the playlist.")
        )
    )
    genre_counts: List[int] = (
        Field(..., description = (
            "Parallel list indicating the number of tracks per genre in genre_list.")
        )
    )
    playback_available: bool = (
        Field(..., description = (
            "Indicates whether real\u2011time playback is enabled for the playlist.")
        )
    )
    save_successful: bool = (
        Field(..., description = (
            "Indicates whether the save operation to the user\u2019s library succeeded.")
        )
    )
    telemetry_log_id: str = (
        Field(..., description = (
            "Identifier for the telemetry log entry created for this playlist interaction.")
        )
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
    oauth_token: str = validate_oauth_token(user_context=kwargs)
    track_details: List[dict] = fetch_track_metadata(track_ids=create_playlist_input.track_ids, token=oauth_token)
    total_duration: int = calculate_total_duration(track_details=track_details)
    genre_stats: dict = analyze_genre_distribution(track_details=track_details, existing_genres=create_playlist_input.genre_representation)
    ui_component: dict = render_playlist_ui(playlist_data=create_playlist_input, track_details=track_details)
    playback_status: bool = enable_realtime_playback(playlist_id=create_playlist_input.playlist_id, tracks=track_details, token=oauth_token)
    save_result: bool = save_to_user_library(playlist_data=create_playlist_input, user_token=oauth_token)
    log_id: str = log_user_interaction(playlist_id=create_playlist_input.playlist_id, ui_data=ui_component, playback_enabled=playback_status, save_status=save_result)
    return OfferPlaylistToUserOutput(
        playlist_id=create_playlist_input.playlist_id,
        total_duration_seconds=total_duration,
        track_count=len(create_playlist_input.track_ids),
        genre_list=genre_stats["genre_list"],
        genre_counts=genre_stats["genre_counts"],
        playback_available=playback_status,
        save_successful=save_result,
        telemetry_log_id=log_id,
    )