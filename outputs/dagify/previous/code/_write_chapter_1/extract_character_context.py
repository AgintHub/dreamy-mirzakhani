import json


def extract_character_context(character_profile: str) -> str:
    """
    Extract character context from the given character profile input string.

    Parameters
    ----------
    character_profile : str
        The input character profile string, expected to be in the format of
        a JSON object.

    Returns
    -------
    STR
        A JSON object containing the character profile information, with
        specific fields such as character name, age, personality traits,
        role in the story, favorite color, and dog profile.

    Raises
    ------
    ValueError
        When the input character profile string is invalid or cannot be
        parsed.
    TypeError
        When the input character profile string is not in the expected
        format.

    Examples
    --------
    >>> import json

    >>> character_profile = '{{"name": "John Doe", "age": 30,
    "personality_traits": ["introvert", "creative"], "role": "protagonist",
    "favorite_color": "blue", "dog_profile": "labrador retriever"}}'
    >>> output = extract_character_context(character_profile)
    {
      "character_name": "John Doe",
      "age": 30,
      "personality_traits": ["introvert", "creative"],
      "role_in_plot": "protagonist",
      "favorite_color": "blue",
      "dog_profile": "labrador retriever"
    }

    >>> import json

    >>> character_profile = '{{"name": "Jane Smith", "age": 25,
    "personality_traits": ["outgoing", "ambitious"], "role": "supporting
    character", "favorite_color": "red", "dog_profile": "poodle"}}'
    >>> output = extract_character_context(character_profile)
    {
      "character_name": "Jane Smith",
      "age": 25,
      "personality_traits": ["outgoing", "ambitious"],
      "role_in_plot": "supporting character",
      "favorite_color": "red",
      "dog_profile": "poodle"
    }

    """
    
    if not isinstance(character_profile, str):
        raise TypeError("Input character profile must be a string")
    
    try:
        profile_data = json.loads(character_profile)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON string provided") from e
    
    if not isinstance(profile_data, dict):
        raise ValueError("Character profile must be a JSON object")
    
    output_data = {
        "character_name": profile_data.get("name", ""),
        "age": profile_data.get("age", 0),
        "personality_traits": profile_data.get("personality_traits", []),
        "role_in_plot": profile_data.get("role", ""),
        "favorite_color": profile_data.get("favorite_color", ""),
        "dog_profile": profile_data.get("dog_profile", "")
    }
    
    return json.dumps(output_data, indent=2)