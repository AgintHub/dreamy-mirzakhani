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


def load_audio_snippet(general_input: str, **kwargs) -> LoadAudioSnippetOutput:
    """
    Loads an input audio file, extracts its audio features, and returns the file
    path, audio features, and loading status.

    Parameters
    ----------
    audio_file : str
        Path to the input audio file

    Returns
    -------
    {audio_file_path: str, audio_features: List[float], loading_status: bool}
        A dictionary containing the path to the loaded audio file, its
        extracted audio features, and the loading status.

    Raises
    ------
    FileNotFoundError
        If the input audio file does not exist.
    Exception
        If there is an issue loading or processing the audio file.

    Examples
    --------
    >>> load_audio_snippet('path/to/audio/file.wav')
    {'audio_file_path': 'path/to/audio/file.wav', 'audio_features': [1.0, 2.0,
    3.0], 'loading_status': True}

    >>> load_audio_snippet('non_existent_file.wav')
    Raises FileNotFoundError

    """
    return LoadAudioSnippetOutput(
        audio_file_path="",
        audio_features=[],
        loading_status=False,
    )