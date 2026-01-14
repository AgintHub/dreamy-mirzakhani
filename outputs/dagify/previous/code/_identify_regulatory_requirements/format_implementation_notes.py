from typing import List


def format_implementation_notes(raw_notes: str) -> List[str]:
    """
    Formats the implementation notes for regulatory requirements into a list of
    strings.

    Parameters
    ----------
    raw_notes : str
        The raw implementation notes to be formatted.

    Returns
    -------
    List[str]
        A list of formatted implementation notes.

    Raises
    ------
    ValueError
        If the input raw_notes is not a string.
    TypeError
        If the input raw_notes is not a string or cannot be converted to a
        list of strings.

    Examples
    --------
    >>> formatted_notes = format_implementation_notes("Note 1, Note 2")
    ["Note 1", "Note 2"]

    >>> formatted_notes = format_implementation_notes("Single Note")
    ["Single Note"]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")