def convert_to_base64(binary_data: str) -> str:
    """
    Converts binary data to a base64-encoded string.

    Parameters
    ----------
    binary_data : str
        The binary data to be converted to base64 encoding.

    Returns
    -------
    str
        The base64-encoded string representation of the input binary data.

    Raises
    ------
    TypeError
        If the input binary_data is not of type str.
    ValueError
        If the input binary_data is not valid binary data.

    Examples
    --------
    >>> binary_data = 'Hello, World!'
    >>> base64_encoded =
    convert_to_base64(binary_data=binary_data.encode('utf-8'))
    >>> print(base64_encoded)
    'SGVsbG8sIFdvcmxkIQ=='

    >>> binary_data = 'example'
    >>> base64_encoded =
    convert_to_base64(binary_data=binary_data.encode('utf-8'))
    >>> print(base64_encoded)
    'ZXhhbXBsZQ=='

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")