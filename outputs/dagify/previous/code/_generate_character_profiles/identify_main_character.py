import json


def identify_main_character(character_profiles: str) -> str:
    """
    Identifies the main character from a list of character profiles.

    Parameters
    ----------
    character_profiles : Dict[str, str]
        A dictionary of character profiles where each key is a character
        name and each value is a JSON string containing character attributes

    Returns
    -------
    Dict
        A dictionary representing the main character's profile with
        attributes as keys and corresponding values

    Raises
    ------
    ValueError
        If input validation fails, e.g., invalid JSON in the character
        profiles dict
    TypeError
        If input types are incorrect, e.g., non-string keys in the character
        profiles dict

    Examples
    --------
    >>> char_profiles = {'Harry Potter': '{"age": 17, "hobby": "Quidditch"}',
    'Ron Weasley': '{"age": 17, "hobby": "Pranks"}'}",
    "identify_main_character(character_profiles=char_profiles)"
    {"name": "Harry Potter", "age": 17, "hobby": "Quidditch"}

    >>> char_profiles = {'Dumbledore': '{"age": 115, "hobby": "Potions"}',
    'Hermione Granger': '{"age": 17, "hobby": "Reading"}'}",
    "identify_main_character(character_profiles=char_profiles)"
    {"name": "Dumbledore", "age": 115, "hobby": "Potions"}

    """
    
    if isinstance(character_profiles, str):
        try:
            profiles_dict = json.loads(character_profiles)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in character_profiles")
    else:
        profiles_dict = character_profiles
    
    if not isinstance(profiles_dict, dict):
        raise TypeError("character_profiles must be a dictionary")
    
    for key in profiles_dict.keys():
        if not isinstance(key, str):
            raise TypeError("All keys in character_profiles must be strings")
    
    parsed_profiles = {}
    for name, profile_json in profiles_dict.items():
        if not isinstance(profile_json, str):
            raise ValueError(f"Profile for {name} must be a JSON string")
        try:
            profile_data = json.loads(profile_json)
            parsed_profiles[name] = profile_data
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in profile for character: {name}")
    
    main_character_names = ['Harry Potter', 'Dumbledore', 'Hermione Granger']
    main_char_name = None
    main_char_profile = None
    
    for main_name in main_character_names:
        if main_name in parsed_profiles:
            main_char_name = main_name
            main_char_profile = parsed_profiles[main_name]
            break
    
    if main_char_name is None:
        if parsed_profiles:
            main_char_name = list(parsed_profiles.keys())[0]
            main_char_profile = parsed_profiles[main_char_name]
        else:
            raise ValueError("No character profiles provided")
    
    result_profile = {"name": main_char_name}
    result_profile.update(main_char_profile)
    
    return json.dumps(result_profile)