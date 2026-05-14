def prepare_story_context(chapter_2_content: str, outline: str, characters: str, setting: str) -> str:
    """
    Prepares a context dictionary containing chapter 2 content, outline,
    characters, and setting.

    Parameters
    ----------
    chapter_2_content : str
        The chapter 2 content to be included in the context dictionary.
    outline : str
        The outline to be included in the context dictionary.
    characters : str
        The characters to be included in the context dictionary.
    setting : str
        The setting to be included in the context dictionary.

    Returns
    -------
    dict
        A dictionary containing chapter 2 content, outline, characters, and
        setting.

    Raises
    ------
    ValueError
        When the input parameters do not conform to the required format.
    TypeError
        When the input parameters do not match the expected types.

    Examples
    --------
    >>> story_context = prepare_story_context(chapter_2_content='This is chapter
    2 content.',
    ...                           outline='This is the outline.',
    ...                           characters='These are the characters.',
    ...                           setting='This is the setting.')
    {'chapter_2_content': 'This is chapter 2 content.', 'outline': 'This is the
    outline.', 'characters': 'These are the characters.', 'setting': 'This is
    the setting.'}

    """
    if not isinstance(chapter_2_content, str):
        raise TypeError("chapter_2_content must be a string")
    if not isinstance(outline, str):
        raise TypeError("outline must be a string")
    if not isinstance(characters, str):
        raise TypeError("characters must be a string")
    if not isinstance(setting, str):
        raise TypeError("setting must be a string")
    
    if not chapter_2_content.strip():
        raise ValueError("chapter_2_content cannot be empty or whitespace only")
    if not outline.strip():
        raise ValueError("outline cannot be empty or whitespace only")
    if not characters.strip():
        raise ValueError("characters cannot be empty or whitespace only")
    if not setting.strip():
        raise ValueError("setting cannot be empty or whitespace only")
    
    context_dict = {
        'chapter_2_content': chapter_2_content,
        'outline': outline,
        'characters': characters,
        'setting': setting
    }
    
    return context_dict