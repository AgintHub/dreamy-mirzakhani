from ._integrate_features.initialize_redux_state import initialize_redux_state
from ._integrate_features.extract_sample_id_from_kwargs import extract_sample_id_from_kwargs
from ._integrate_features.extract_musician_ids_from_kwargs import extract_musician_ids_from_kwargs
from ._integrate_features.set_loading_state import set_loading_state
from ._integrate_features.process_sample_identification import process_sample_identification
from ._integrate_features.get_identified_tracks_count import get_identified_tracks_count
from ._integrate_features.determine_sample_identified_status import determine_sample_identified_status
from ._integrate_features.update_redux_state import update_redux_state
from ._integrate_features.process_musician_listing import process_musician_listing
from ._integrate_features.get_musician_count import get_musician_count
from ._integrate_features.update_redux_state import update_redux_state
from ._integrate_features.handle_profile_redirection import handle_profile_redirection
from ._integrate_features.process_playlist_offering import process_playlist_offering
from ._integrate_features.get_playlist_creation_status import get_playlist_creation_status
from ._integrate_features.get_playlist_track_count import get_playlist_track_count
from ._integrate_features.update_redux_state import update_redux_state
from ._integrate_features.manage_snackbar_notifications import manage_snackbar_notifications
from ._integrate_features.handle_integration_error import handle_integration_error
from ._integrate_features.manage_snackbar_notifications import manage_snackbar_notifications

from pydantic import BaseModel, Field
from typing import List


class BuildAppInterfaceOutput(BaseModel):
    """Pydantic model for build_app_interface node outputs."""
    interface_design_document: str = (
        Field(..., description = (
            "A detailed document outlining the design decisions, wireframes, and user flows for the application interface.")
        )
    )
    responsive_breakpoints: str = (
        Field(..., description = (
            "List of CSS breakpoints used to ensure a responsive design across various screen sizes and devices.")
        )
    )
    accessibility_features: str = (
        Field(..., description = (
            "List of accessibility features implemented, such as WCAG 2.1 guidelines compliance, screen reader support, and keyboard navigation.")
        )
    )
    performance_optimization_techniques: str = (
        Field(..., description = (
            "List of techniques used to optimize the performance of the application interface, such as code splitting, lazy loading, and caching.")
        )
    )
    ui_components: str = (
        Field(..., description = (
            "List of UI components used in the application, such as buttons, forms, and navigation elements.")
        )
    )


class RedirectToMusiciansPagesOutput(BaseModel):
    """Pydantic model for redirect_to_musicians_pages node outputs."""
    redirection_results: List[str] = (
        Field(..., description = (
            "List of URLs successfully redirected to the official pages of musicians")
        )
    )
    successful_redirections_count: int = (
        Field(..., description = (
            "Number of successful redirections to musician profiles")
        )
    )
    redirection_exceptions: List[str] = (
        Field(..., description = (
            "List of exceptions or errors encountered during the redirection process")
        )
    )
    is_redirection_successful: bool = (
        Field(..., description = (
            "Whether the redirection process was successful overall")
        )
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


class IntegrateFeaturesOutput(BaseModel):
    """Pydantic model for integrate_features node outputs."""
    sample_id: str = (
        Field(..., description="Identifier of the audio sample being processed")
    )
    sample_identified: bool = (
        Field(..., description = (
            "Whether the sample has been successfully identified")
        )
    )
    identified_tracks_count: int = (
        Field(..., description = (
            "Number of candidate tracks returned by identification")
        )
    )
    musician_ids: List[str] = (
        Field(..., description = (
            "List of unique musician identifiers extracted from identified tracks")
        )
    )
    musician_count: int = (
        Field(..., description="Total number of musicians in the list")
    )
    playlist_id: str = (
        Field(..., description="Identifier of the generated playlist")
    )
    playlist_created: bool = (
        Field(..., description="Whether the playlist was successfully created")
    )
    playlist_track_count: int = (
        Field(..., description="Number of tracks in the created playlist")
    )
    error_message: str = (
        Field(..., description = (
            "Error message if any operation failed, \u043d\u0430\u0448\u0438\u043c otherwise")
        )
    )
    snackbar_visible: bool = (
        Field(..., description = (
            "Whether a snackbar notification is currently visible")
        )
    )
    snackbar_message: str = (
        Field(..., description="Content of the snackbar notification")
    )
    loading_state: str = (
        Field(..., description = (
            "Current loading state of the UI (e.g., idle, loading, success, error)")
        )
    )


def integrate_features(build_app_interface_input: BuildAppInterfaceOutput, redirect_to_musicians_pages_input: RedirectToMusiciansPagesOutput, offer_playlist_to_user_input: OfferPlaylistToUserOutput, **kwargs) -> IntegrateFeaturesOutput:
    """
    Implements a React component that orchestrates sample identification,
    musician listing, profile redirection, and playlist offering flows, managing
    state with Redux and using Material-UI components.

    Parameters
    ----------
    sampleId : str
        Identifier of the audio sample being processed
    musicianIds : List[str]
        List of unique musician identifiers extracted from identified tracks

    Returns
    -------
    {sample_id: str, sample_identified: bool, identified_tracks_count: int, musician_ids: List[str], musician_count: int, playlist_id: str, playlist_created: bool, playlist_track_count: int, error_message: str, snackbar_visible: bool, snackbar_message: str, loading_state: str}
        Object containing the state of the sample identification, musician
        listing, and playlist generation processes, along with any error
        messages or loading state information.

    Raises
    ------
    Error
        If any of the Redux actions fail or if there's an issue with the UI
        components

    Examples
    --------
    >>> const sampleId = '12345';
    >>> const musicianIds = ['musician1', 'musician2'];
    >>> const result = integrateFeatures(sampleId, musicianIds);
    >>> console.log(result);
    {sample_id: '12345', sample_identified: true, identified_tracks_count: 5,
    musician_ids: ['musician1', 'musician2'], musician_count: 2, playlist_id:
    'playlist1', playlist_created: true, playlist_track_count: 10,
    error_message: '', snackbar_visible: false, snackbar_message: '',
    loading_state: 'success'}

    """
    initial_state: dict = initialize_redux_state()
    sample_id: str = extract_sample_id_from_kwargs(**kwargs)
    musician_ids: List[str] = extract_musician_ids_from_kwargs(**kwargs)
    
    set_loading_state(state=initial_state, loading="loading")
    
    try:
        sample_identification_result: dict = process_sample_identification(sample_id=sample_id)
        identified_tracks_count: int = get_identified_tracks_count(result=sample_identification_result)
        sample_identified: bool = determine_sample_identified_status(tracks_count=identified_tracks_count)
        
        update_redux_state(state=initial_state, sample_data=sample_identification_result)
        
        musician_list_result: dict = process_musician_listing(musician_ids=musician_ids)
        musician_count: int = get_musician_count(musician_ids=musician_ids)
        
        update_redux_state(state=initial_state, musician_data=musician_list_result)
        
        redirection_status: bool = handle_profile_redirection(redirection_input=redirect_to_musicians_pages_input)
        
        playlist_result: dict = process_playlist_offering(playlist_input=offer_playlist_to_user_input)
        playlist_created: bool = get_playlist_creation_status(result=playlist_result)
        playlist_track_count: int = get_playlist_track_count(playlist_input=offer_playlist_to_user_input)
        
        update_redux_state(state=initial_state, playlist_data=playlist_result)
        
        snackbar_data: dict = manage_snackbar_notifications(state=initial_state, success=True)
        
        set_loading_state(state=initial_state, loading="success")
        
        return IntegrateFeaturesOutput(
            sample_id=sample_id,
            sample_identified=sample_identified,
            identified_tracks_count=identified_tracks_count,
            musician_ids=musician_ids,
            musician_count=musician_count,
            playlist_id=offer_playlist_to_user_input.playlist_id,
            playlist_created=playlist_created,
            playlist_track_count=playlist_track_count,
            error_message="",
            snackbar_visible=snackbar_data.get("visible", False),
            snackbar_message=snackbar_data.get("message", ""),
            loading_state="success"
        )
        
    except Exception as e:
        error_message: str = handle_integration_error(error=e)
        snackbar_error_data: dict = manage_snackbar_notifications(state=initial_state, success=False, error=error_message)
        set_loading_state(state=initial_state, loading="error")
        
        return IntegrateFeaturesOutput(
            sample_id=sample_id,
            sample_identified=False,
            identified_tracks_count=0,
            musician_ids=musician_ids,
            musician_count=len(musician_ids),
            playlist_id="",
            playlist_created=False,
            playlist_track_count=0,
            error_message=error_message,
            snackbar_visible=snackbar_error_data.get("visible", True),
            snackbar_message=snackbar_error_data.get("message", error_message),
            loading_state="error"
        )