def extract_character_name(character_data: str) -> str:
    """
    Extracts the character's full name from the main character's data.

    Parameters
    ----------
    character_data : str
        The input character data containing the character's name.

    Returns
    -------
    str
        The extracted character name as a string, formatted and processed
        for further use in character profile generation.

    Raises
    ------
    ValueError
        When input validation fails, e.g., character name not found.
    TypeError
        When input types are incorrect, e.g., non-string input.

    Examples
    --------
    >>> main_character = {'name': 'John Doe', 'age': 30, 'traits':
    ['introverted']}
    >>> character_name = extract_character_name(character_data=main_character)
    >>> print(character_name)
    'John Doe'

    >>> main_character = {'name': 'Jane Smith', 'age': 25, 'traits':
    ['outgoing']}
    >>> character_name = extract_character_name(character_data=main_character)
    >>> print(character_name)
    'Jane Smith'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")