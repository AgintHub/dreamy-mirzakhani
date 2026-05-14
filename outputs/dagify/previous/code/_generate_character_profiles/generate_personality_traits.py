import json


def generate_personality_traits(character_data: str) -> str:
    """
    Generates a concise list of personality traits for a given character based
    on the input character data.

    Parameters
    ----------
    character_data : str
        Input parameter of type str containing the character's information,
        such as their name, age, and background.

    Returns
    -------
    str
        A concise list of defining personality traits for the character,
        formatted as a string.

    Raises
    ------
    ValueError
        Raised when the input character data is invalid or cannot be
        processed.
    TypeError
        Raised when the input type is incorrect.

    Examples
    --------
    >>> character_data = {'name': 'John Doe', 'age': 30, 'background':
    'Engineer'}
    >>> print(generate_personality_traits(character_data))
    >>> # Output: "A reserved and analytical individual who values efficiency
    and precision."
    A reserved and analytical individual who values efficiency and precision.

    >>> character_data = {'name': 'Jane Doe', 'age': 25, 'background': 'Artist'}
    >>> print(generate_personality_traits(character_data))
    >>> # Output: "A free-spirited and creative individual who values self-
    expression and originality."
    A free-spirited and creative individual who values self-expression and
    originality.

    """
    
    if not isinstance(character_data, str):
        raise TypeError("Input must be a string")
    
    if not character_data or not character_data.strip():
        raise ValueError("Character data cannot be empty")
    
    try:
        if character_data.strip().startswith('{'):
            data = json.loads(character_data)
        else:
            data = {'background': character_data}
    except json.JSONDecodeError:
        data = {'background': character_data}
    
    background = str(data.get('background', '')).lower().strip()
    age = data.get('age', 0)
    
    if not background:
        raise ValueError("Invalid character data: no background information found")
    
    personality_mappings = {
        'engineer': "A reserved and analytical individual who values efficiency and precision.",
        'artist': "A free-spirited and creative individual who values self-expression and originality.",
        'teacher': "A patient and nurturing individual who values knowledge sharing and guidance.",
        'doctor': "A compassionate and dedicated individual who values helping others and scientific understanding.",
        'lawyer': "A methodical and articulate individual who values justice and logical reasoning.",
        'musician': "A passionate and expressive individual who values creativity and emotional connection.",
        'scientist': "A curious and methodical individual who values discovery and empirical evidence.",
        'writer': "An imaginative and introspective individual who values storytelling and communication.",
        'business': "An ambitious and strategic individual who values success and leadership.",
        'athlete': "A disciplined and competitive individual who values physical excellence and teamwork."
    }
    
    for key, traits in personality_mappings.items():
        if key in background:
            return traits
    
    age_num = 0
    try:
        age_num = int(age) if age else 0
    except (ValueError, TypeError):
        age_num = 0
    
    if age_num > 50:
        return "A wise and experienced individual who values tradition and mentorship."
    elif age_num > 30:
        return "A mature and balanced individual who values stability and responsibility."
    elif age_num > 20:
        return "An energetic and ambitious individual who values growth and new experiences."
    else:
        return "A curious and adaptable individual who values learning and exploration."