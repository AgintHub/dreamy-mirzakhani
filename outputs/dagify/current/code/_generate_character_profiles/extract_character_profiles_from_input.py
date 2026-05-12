from typing import List


import re
import json


def extract_character_profiles_from_input(input_data: str, kwargs: str) -> List[str]:
    """
    Extracts character profiles from the input data, validating the extracted
    data against a prescribed schema.

    Parameters
    ----------
    input_data : STR
        Input data containing character profile information.
    kwargs : STR
        Additional keyword arguments used to configure the extraction
        process.

    Returns
    -------
    List[dict]
        A list of dictionaries containing validated character profile data.
        Each dictionary represents a character with its associated
        attributes and values.

    Raises
    ------
    ValueError
        Raised when the input data fails to meet the prescribed structure
        and format requirements.
    TypeError
        Raised when the input data contains unexpected or malformed types.

    Examples
    --------
    >>> input_data = 'Character 1: John Doe, Age: 25, Traits: Extroverted',
    'Character 2: Jane Doe, Age: 30, Traits: Introverted'
    >>> # Example usage
    >>> character_profiles =
    extract_character_profiles_from_input(input_data=input_data,
    kwargs={'required_keys': ['Name', 'Age']})
    [
      {
        'Name': 'John Doe',
        'Age': 25,
        'Traits': ['Extroverted']
      },
      {
        'Name': 'Jane Doe',
        'Age': 30,
        'Traits': ['Introverted']
      }
    ]

    >>> # Invalid input data
    >>> input_data = 'Invalid character profile data'
    >>> # Attempting to extract character profiles with malformed input data
    raises a ValueError
    >>> try:
    ...     character_profiles =
    extract_character_profiles_from_input(input_data=input_data,
    kwargs={'required_keys': ['Name', 'Age']})
    ValueError: Input data does not conform to the prescribed structure and
    format.

    """
    
    if not isinstance(input_data, str):
        raise TypeError("Input data must be a string")
    
    if not isinstance(kwargs, str):
        raise TypeError("kwargs must be a string")
    
    try:
        config = json.loads(kwargs) if kwargs.strip() else {}
    except json.JSONDecodeError:
        try:
            config = eval(kwargs) if kwargs.strip() else {}
        except:
            config = {}
    
    required_keys = config.get('required_keys', [])
    
    if not input_data.strip():
        raise ValueError("Input data does not conform to the prescribed structure and format.")
    
    character_pattern = r'Character \d+:([^,]+)(?:,([^,]+))*'
    characters = []
    
    if 'Character' not in input_data:
        raise ValueError("Input data does not conform to the prescribed structure and format.")
    
    character_blocks = re.split(r'Character \d+:', input_data)
    character_blocks = [block.strip() for block in character_blocks if block.strip()]
    
    if not character_blocks:
        raise ValueError("Input data does not conform to the prescribed structure and format.")
    
    for block in character_blocks:
        character_dict = {}
        
        parts = [part.strip() for part in block.split(',')]
        
        if not parts or not parts[0]:
            continue
            
        character_dict['Name'] = parts[0]
        
        for part in parts[1:]:
            if ':' in part:
                key, value = part.split(':', 1)
                key = key.strip()
                value = value.strip()
                
                if key == 'Age':
                    try:
                        character_dict[key] = int(value)
                    except ValueError:
                        raise TypeError("Input data contains unexpected or malformed types.")
                elif key == 'Traits':
                    character_dict[key] = [value]
                else:
                    character_dict[key] = value
        
        for req_key in required_keys:
            if req_key not in character_dict:
                raise ValueError("Input data does not conform to the prescribed structure and format.")
        
        characters.append(str(character_dict))
    
    if not characters:
        raise ValueError("Input data does not conform to the prescribed structure and format.")
    
    return characters