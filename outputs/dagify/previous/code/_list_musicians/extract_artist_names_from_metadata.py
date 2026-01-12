from typing import List


def extract_artist_names_from_metadata(metadata: str) -> List[str]:
    """
    Extracts artist names from the provided metadata string and returns them as
    a list.

    Parameters
    ----------
    metadata : str
        The input metadata string containing artist information.

    Returns
    -------
    List[str]
        A list of artist names extracted from the metadata string.

    Raises
    ------
    ValueError
        If the input metadata is not a valid string or is empty.
    TypeError
        If the input metadata is not of type string.

    Examples
    --------
    >>> metadata = 'Song by Artist1, Artist2, and Artist3'
    >>> artist_names = extract_artist_names_from_metadata(metadata=metadata)
    ['Artist1', 'Artist2', 'Artist3']

    >>> metadata = 'Artists: ArtistX, ArtistY'
    >>> artist_names = extract_artist_names_from_metadata(metadata=metadata)
    ['ArtistX', 'ArtistY']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")