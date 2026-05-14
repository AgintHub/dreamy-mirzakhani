from datetime import datetime
import json


def determine_character_age(character_data: str) -> float:
    """
    Determine the age of a character given their data.

    Parameters
    ----------
    character_data : dict
        A dictionary containing the character's data, including birthdate,
        for accurate age calculation.

    Returns
    -------
    float
        The calculated age of the character

    Raises
    ------
    ValueError
        When invalid or missing data is provided, or when date calculations
        fail.
    TypeError
        When the input data is of an incorrect type, causing calculation
        errors.

    Examples
    --------
    >>> character_data = {'birthdate': '1990-01-01'}
    >>> character_age = determine_character_age(character_data)
    30

    >>> character_data = {'birthdate': '1980-01-01'}
    >>> character_age = determine_character_age(character_data)
    42

    """
    
    if not isinstance(character_data, (str, dict)):
        raise TypeError("Input data must be a string or dictionary")
    
    if isinstance(character_data, str):
        try:
            data = json.loads(character_data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON string provided")
    else:
        data = character_data
    
    if not isinstance(data, dict):
        raise TypeError("Character data must be a dictionary")
    
    if 'birthdate' not in data:
        raise ValueError("Missing birthdate in character data")
    
    birthdate_str = data['birthdate']
    if not isinstance(birthdate_str, str):
        raise TypeError("Birthdate must be a string")
    
    try:
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Invalid birthdate format. Expected YYYY-MM-DD") from e
    
    current_date = datetime.now()
    
    if birthdate > current_date:
        raise ValueError("Birthdate cannot be in the future")
    
    age_days = (current_date - birthdate).days
    age_years = age_days / 365.25
    
    return float(age_years)