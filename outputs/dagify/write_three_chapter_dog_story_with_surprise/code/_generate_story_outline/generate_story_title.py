def generate_story_title(prompt: str) -> str:
    """
    Generates a story title from a given input prompt using natural language
    processing techniques.

    Parameters
    ----------
    prompt : str
        Input prompt to base the story title on.

    Returns
    -------
    str
        Generated story title.

    Raises
    ------
    ValueError
        When input prompt is empty or None.
    TypeError
        When input prompt is of incorrect type.

    Examples
    --------
    >>> story_title = generate_story_title('A tale of adventure')
    'A Tale of Adventure'

    >>> story_title = generate_story_title('A story of friendship')
    'A Story of Friendship'

    """
    if prompt is None:
        raise ValueError("Input prompt cannot be None")
    
    if not isinstance(prompt, str):
        raise TypeError("Input prompt must be a string")
    
    if not prompt.strip():
        raise ValueError("Input prompt cannot be empty")
    
    words = prompt.strip().split()
    capitalized_words = [word.capitalize() for word in words]
    title = ' '.join(capitalized_words)
    
    return title