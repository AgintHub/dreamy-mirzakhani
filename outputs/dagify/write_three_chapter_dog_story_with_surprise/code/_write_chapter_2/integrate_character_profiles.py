import re
import json


def integrate_character_profiles(character_profiles: str, dog_profile: str) -> str:
    """
    Combines character and dog profiles into a single output dictionary.

    Parameters
    ----------
    character_profiles : str
        A string containing the character's profile information.
    dog_profile : str
        A string containing the dog's profile information.

    Returns
    -------
    str
        A dictionary containing the integrated character and dog profiles,
        with the keys 'character_name', 'age', 'personality_traits',
        'role_in_plot', 'favorite_color', and 'dog_profile'.

    Raises
    ------
    ValueError
        If the provided input is invalid or cannot be parsed.
    TypeError
        If the provided input is not a string.

    Examples
    --------
    >>> shim_function('example character profile', 'example dog profile')
    >>> character_integration = integrate_character_profiles('example character
    profile', 'example dog profile')
    >>> print(character_integration)
    {
        'character_name': 'Example Character', 
        'age': 30, 
        'personality_traits': 'Example personality traits', 
        'role_in_plot': 'Example role', 
        'favorite_color': 'Example color', 
        'dog_profile': 'Example dog profile'
    }

    """
    
    if not isinstance(character_profiles, str):
        raise TypeError("character_profiles must be a string")
    if not isinstance(dog_profile, str):
        raise TypeError("dog_profile must be a string")
    
    if not character_profiles.strip() or not dog_profile.strip():
        raise ValueError("Input profiles cannot be empty")
    
    try:
        character_name_match = re.search(r'name[:\s]+([^\n,;]+)', character_profiles, re.IGNORECASE)
        character_name = character_name_match.group(1).strip() if character_name_match else "Unknown Character"
        
        age_match = re.search(r'age[:\s]+(\d+)', character_profiles, re.IGNORECASE)
        age = int(age_match.group(1)) if age_match else 25
        
        personality_match = re.search(r'personality[:\s]+([^\n;]+)', character_profiles, re.IGNORECASE)
        personality_traits = personality_match.group(1).strip() if personality_match else "Friendly and outgoing"
        
        role_match = re.search(r'role[:\s]+([^\n;]+)', character_profiles, re.IGNORECASE)
        role_in_plot = role_match.group(1).strip() if role_match else "Supporting character"
        
        color_match = re.search(r'(?:favorite\s+color|color)[:\s]+([^\n,;]+)', character_profiles, re.IGNORECASE)
        favorite_color = color_match.group(1).strip() if color_match else "Blue"
        
        result_dict = {
            'character_name': character_name,
            'age': age,
            'personality_traits': personality_traits,
            'role_in_plot': role_in_plot,
            'favorite_color': favorite_color,
            'dog_profile': dog_profile.strip()
        }
        
        return json.dumps(result_dict, indent=4)
        
    except Exception as e:
        raise ValueError(f"Failed to parse character profiles: {str(e)}")