import re
import json


def extract_dog_information(character_profiles: str) -> str:
    """
    Extracts key information about a dog from the given character profiles.

    Parameters
    ----------
    character_profiles : str
        The character profiles input as a string.

    Returns
    -------
    dict
        A JSON object containing key information about the dog, such as its
        breed, background, quirks, and motivations.

    Raises
    ------
    ValueError
        When the input string is malformed or empty.
    TypeError
        When the input parameter is not a string.

    Examples
    --------
    >>> import json
    >>> from pydantic import BaseModel
    >>> def extract_dog_information(character_profiles: str) -> dict:
    ...     # Code to extract dog information from character profiles
    ...     return dog_info
    >>> output = extract_dog_information('character profiles string')
    >>> print(json.dumps(output, indent=4))
    {
      'dog_breed': 'Golden Retriever',
      'dog_background': 'Household',
      'dog_quirks': ['Fur', 'Tail Wags'],
      'dog_motivations': ['Get treats', 'Play fetch']
    }

    >>> import json
    >>> from pydantic import BaseModel
    >>> def extract_dog_information(character_profiles: str) -> dict:
    ...     # Code to extract dog information from character profiles
    ...     return dog_info
    >>> output = extract_dog_information('')
    >>> print(json.dumps(output, indent=4))
    {}

    """
    
    if not isinstance(character_profiles, str):
        raise TypeError("When the input parameter is not a string.")
    
    if not character_profiles or not character_profiles.strip():
        return json.dumps({})
    
    dog_info = {
        'dog_breed': '',
        'dog_background': '',
        'dog_quirks': [],
        'dog_motivations': []
    }
    
    breed_patterns = [
        r'breed[:\s]+([^\n,.]+)',
        r'([A-Z][a-z]+ [A-Z][a-z]+)(?:\s+dog|\s+breed)',
        r'Golden Retriever|Labrador|German Shepherd|Bulldog|Poodle|Beagle|Rottweiler|Yorkshire Terrier|Boxer|Dachshund'
    ]
    
    for pattern in breed_patterns:
        match = re.search(pattern, character_profiles, re.IGNORECASE)
        if match:
            dog_info['dog_breed'] = match.group(1).strip() if match.group(1) else match.group(0).strip()
            break
    
    background_patterns = [
        r'background[:\s]+([^\n,.]+)',
        r'lives?\s+in\s+([^\n,.]+)',
        r'from\s+(household|shelter|farm|street|rescue)',
        r'(household|domestic|wild|stray|rescue)'
    ]
    
    for pattern in background_patterns:
        match = re.search(pattern, character_profiles, re.IGNORECASE)
        if match:
            dog_info['dog_background'] = match.group(1).strip() if match.group(1) else match.group(0).strip()
            break
    
    quirk_patterns = [
        r'quirks?[:\s]+([^\n]+)',
        r'habits?[:\s]+([^\n]+)',
        r'(fur|tail wags?|barks?|howls?|jumps?|runs?|plays?)'
    ]
    
    quirks_found = set()
    for pattern in quirk_patterns:
        matches = re.finditer(pattern, character_profiles, re.IGNORECASE)
        for match in matches:
            quirk_text = match.group(1) if match.group(1) else match.group(0)
            quirks = [q.strip() for q in re.split(r'[,;]', quirk_text) if q.strip()]
            quirks_found.update(quirks)
    
    dog_info['dog_quirks'] = list(quirks_found)
    
    motivation_patterns = [
        r'motivations?[:\s]+([^\n]+)',
        r'wants?\s+to\s+([^\n,.]+)',
        r'likes?\s+to\s+([^\n,.]+)',
        r'(get treats|play fetch|go for walks?|please owner|find food)'
    ]
    
    motivations_found = set()
    for pattern in motivation_patterns:
        matches = re.finditer(pattern, character_profiles, re.IGNORECASE)
        for match in matches:
            motivation_text = match.group(1) if match.group(1) else match.group(0)
            motivations = [m.strip() for m in re.split(r'[,;]', motivation_text) if m.strip()]
            motivations_found.update(motivations)
    
    dog_info['dog_motivations'] = list(motivations_found)
    
    return json.dumps(dog_info)