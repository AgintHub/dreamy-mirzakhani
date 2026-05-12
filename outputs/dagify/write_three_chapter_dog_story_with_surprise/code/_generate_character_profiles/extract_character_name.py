import json


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
    
    if not isinstance(character_data, str):
        raise TypeError("Input must be a string")
    
    if not character_data.strip():
        raise ValueError("Character data cannot be empty")
    
    try:
        data = json.loads(character_data)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in character data")
    
    if not isinstance(data, dict):
        raise ValueError("Character data must be a JSON object")
    
    if 'name' not in data:
        raise ValueError("Character name not found in data")
    
    name = data['name']
    if not isinstance(name, str):
        raise ValueError("Character name must be a string")
    
    name = name.strip()
    if not name:
        raise ValueError("Character name cannot be empty")
    
    return name