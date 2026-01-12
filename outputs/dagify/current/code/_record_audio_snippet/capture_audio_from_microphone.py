def capture_audio_from_microphone(device: str) -> str:
    """
    Captures raw audio data from the specified microphone device and returns it
    as a string.

    Parameters
    ----------
    device : str
        The name or identifier of the microphone device to capture audio
        from.

    Returns
    -------
    str
        The raw audio data captured from the microphone as a string.

    Raises
    ------
    ValueError
        If the specified device is not a valid microphone device.
    RuntimeError
        If there is an issue capturing audio from the device.

    Examples
    --------
    >>> capture_audio_from_microphone(device='default_microphone')
    'raw_audio_data_as_string'

    >>> capture_audio_from_microphone(device='external_usb_microphone')
    'another_raw_audio_data_as_string'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")