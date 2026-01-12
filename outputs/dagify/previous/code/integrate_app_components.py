from pydantic import BaseModel, Field
from typing import List


class LoadAudioSnippetOutput(BaseModel):
    """Pydantic model for load_audio_snippet node outputs."""
    audio_file_path: str = (
        Field(..., description="Path to the loaded audio file")
    )
    audio_features: List[float] = (
        Field(..., description="Extracted audio features such as spectrograms or MFCCs")
    )
    loading_status: bool = (
        Field(..., description="Whether the audio file was loaded successfully")
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


class CreateAppInterfaceOutput(BaseModel):
    """Pydantic model for create_app_interface node outputs."""
    app_interface_design: str = (
        Field(..., description="The designed app interface layout and user experience")
    )
    upload_audio_snippet_functionality: bool = (
        Field(..., description="Whether the app interface supports uploading audio snippets")
    )
    display_matching_songs_functionality: bool = (
        Field(..., description="Whether the app interface supports displaying matching songs")
    )
    musician_page_link_generation: bool = (
        Field(..., description="Whether the app interface supports generating links to musicians' pages")
    )


class IntegrateAppComponentsOutput(BaseModel):
    """Pydantic model for integrate_app_components node outputs."""
    app_interface_status: bool = (
        Field(..., description="Whether the app interface has been successfully integrated")
    )
    audio_analysis_results: List[float] = (
        Field(..., description="List of audio analysis results")
    )
    sample_database_status: bool = (
        Field(..., description="Whether the sample database has been successfully integrated")
    )
    integration_errors: List[str] = (
        Field(..., description="List of errors encountered during integration")
    )
    app_performance_metrics: List[float] = (
        Field(..., description="List of performance metrics for the integrated app")
    )


def integrate_app_components(load_audio_snippet_input: LoadAudioSnippetOutput, generate_song_links_input: GenerateSongLinksOutput, create_app_interface_input: CreateAppInterfaceOutput, **kwargs) -> IntegrateAppComponentsOutput:
    """
    Integrate the app components into a seamless user experience.

    Parameters
    ----------
    audio_analysis_results : List[float]
        Results of the audio analysis
    sample_database : dict
        Sample database containing known song samples
    app_interface : dict
        App interface design and functionality

    Returns
    -------
    {app_interface_status: bool, audio_analysis_results: List[float], sample_database_status: bool, integration_errors: List[str], app_performance_metrics: List[float]}
        Integrated app components with their status and performance metrics

    Raises
    ------
    Exception
        If integration fails or errors occur

    Examples
    --------
    >>> integrate_app_components(audio_analysis_results=[1.0, 2.0],
    sample_database={'song1': 'artist1'}, app_interface={'design': 'layout'})
    {app_interface_status: True, audio_analysis_results: [1.0, 2.0],
    sample_database_status: True, integration_errors: [],
    app_performance_metrics: [0.9]}

    """
    return IntegrateAppComponentsOutput(
        app_interface_status=False,
        audio_analysis_results=[],
        sample_database_status=False,
        integration_errors=[],
        app_performance_metrics=[],
    )