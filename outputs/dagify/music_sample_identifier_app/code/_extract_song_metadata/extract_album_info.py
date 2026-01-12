def extract_album_info(metadata: str) -> str:
    """
    Extracts and formats album information from the provided metadata.

    Parameters
    ----------
    metadata : dict
        Dictionary containing metadata about a music track or album,
        including album title, artist, release date, etc.

    Returns
    -------
    str
        Formatted string containing the extracted album information.

    Raises
    ------
    KeyError
        If required keys are missing from the metadata dictionary.
    TypeError
        If the input metadata is not a dictionary.

    Examples
    --------
    >>> metadata = {'album': 'Thriller', 'artist': 'Michael Jackson',
    'release_date': '1982'}
    >>> album_info = extract_album_info(metadata=metadata)
    'Thriller by Michael Jackson (1982)'

    >>> metadata = {'album': 'Bad', 'artist': 'Michael Jackson', 'release_date':
    '1987'}
    >>> album_info = extract_album_info(metadata=metadata)
    'Bad by Michael Jackson (1987)'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")