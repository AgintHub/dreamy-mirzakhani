def validate_inputs(story_outline: str, character_profiles: str, story_setting: str) -> str:
    """
    Validates the inputs from the generate_story_outline,
    generate_character_profiles, and generate_story_setting nodes before passing
    them to the write_chapter_1 function.

    Parameters
    ----------
    story_outline : str
        Input parameter representing the story outline from the
        generate_story_outline node.
    character_profiles : str
        Input parameter representing the character profiles from the
        generate_character_profiles node.
    story_setting : str
        Input parameter representing the story setting from the
        generate_story_setting node.

    Returns
    -------
    str
        A string indicating whether the inputs are valid or not. If valid,
        outputs 'Inputs are valid.'; otherwise, outputs an error message.

    Raises
    ------
    ValueError
        When any of the input parameters are empty.
    TypeError
        When the type of any of the input parameters does not match the
        expected type (i.e., string).

    Examples
    --------
    >>> validate_inputs('Valid story outline example', 'Valid character profiles
    example', 'Valid story setting example')
    >>> print(validate_inputs(...))
    'Inputs are valid.'

    >>> validate_inputs('', 'Invalid character profiles example', 'Valid story
    setting example')
    >>> print(validate_inputs(...))
    Error: Empty input parameter(s).

    """
    if not isinstance(story_outline, str) or not isinstance(character_profiles, str) or not isinstance(story_setting, str):
        raise TypeError("All input parameters must be strings")
    
    if not story_outline or not character_profiles or not story_setting:
        raise ValueError("All input parameters must be non-empty")
    
    if not story_outline.strip() or not character_profiles.strip() or not story_setting.strip():
        return "Error: Empty input parameter(s)."
    
    return "Inputs are valid."