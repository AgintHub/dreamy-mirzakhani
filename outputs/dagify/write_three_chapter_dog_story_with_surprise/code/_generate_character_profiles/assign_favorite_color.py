import json


def assign_favorite_color(character_data: str) -> str:
    """
    Calculates a character's favorite color based on their personality traits.

    Parameters
    ----------
    character_data : str
        A string representing the character's details.

    Returns
    -------
    STR
        A color that encapsulates the character's essence or aesthetic.

    Raises
    ------
    ValueError
        When input validation fails.
    TypeError
        When input types are incorrect.

    Examples
    --------
    >>> favorite_color = assign_favorite_color(character_data={'name': 'John',
    'personality': 'calm'})
    'blue'

    >>> favorite_color = assign_favorite_color(character_data={'name': 'Jane',
    'personality': 'adventurous'})
    'purple'

    """
    
    if not isinstance(character_data, str):
        raise TypeError("Input must be a string")
    
    if not character_data.strip():
        raise ValueError("Input string cannot be empty")
    
    try:
        data = json.loads(character_data)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in character_data")
    
    if not isinstance(data, dict):
        raise ValueError("Character data must be a dictionary")
    
    personality = data.get('personality', '').lower().strip()
    
    if not personality:
        raise ValueError("Personality trait is required")
    
    personality_color_map = {
        'calm': 'blue',
        'peaceful': 'blue',
        'serene': 'blue',
        'adventurous': 'purple',
        'bold': 'purple',
        'daring': 'purple',
        'energetic': 'red',
        'passionate': 'red',
        'fiery': 'red',
        'creative': 'orange',
        'artistic': 'orange',
        'imaginative': 'orange',
        'cheerful': 'yellow',
        'optimistic': 'yellow',
        'bright': 'yellow',
        'nature-loving': 'green',
        'balanced': 'green',
        'harmonious': 'green',
        'mysterious': 'black',
        'elegant': 'black',
        'sophisticated': 'black',
        'pure': 'white',
        'innocent': 'white',
        'simple': 'white',
        'romantic': 'pink',
        'gentle': 'pink',
        'caring': 'pink'
    }
    
    color = personality_color_map.get(personality, 'gray')
    
    return color