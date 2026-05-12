def validate_chapter_2_input(chapter_2_text: str) -> str:
    """
    Validates the input Chapter 2 text and provides the validated text, or an
    error message if validation fails.

    Parameters
    ----------
    chapter_2_text : str
        The Chapter 2 text to be validated.

    Returns
    -------
    str
        The validated Chapter 2 text, or an error message if validation
        fails.

    Raises
    ------
    ValueError
        When validation fails due to invalid input text.
    TypeError
        When input text is not of type str.

    Examples
    --------
    >>> validated_chapter2_text =
    validate_chapter_2_input(chapter_2_text='validated text')
    >>> print(validated_chapter2_text)
    'validated text'

    >>> try:
    ...     validated_chapter2_text = validate_chapter_2_input(chapter_2_text='
    invalid text')
    >>> except ValueError as e:
    ...     print(e)
    Validation failed due to invalid input text

    """
    if not isinstance(chapter_2_text, str):
        raise TypeError("When input text is not of type str.")
    
    stripped_text = chapter_2_text.strip()
    
    if not stripped_text:
        raise ValueError("Validation failed due to invalid input text.")
    
    if stripped_text.startswith(' '):
        raise ValueError("Validation failed due to invalid input text.")
    
    return stripped_text