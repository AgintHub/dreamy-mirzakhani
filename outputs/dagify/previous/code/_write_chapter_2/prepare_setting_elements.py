import json
import re


def prepare_setting_elements(setting: str, environmental_details: str) -> str:
    """
    Prepare setting elements from the provided story setting and environmental
    details.

    Parameters
    ----------
    setting : STR
        Input story setting to be used for setting element preparation.
    environmental_details : STR
        Input environmental details to be used for setting element
        preparation.

    Returns
    -------
    STR
        Processed setting elements in dictionary format, including location,
        time period, environmental factors, and the protagonist's favorite
        color.

    Raises
    ------
    ValueError
        When input validation fails, such as invalid story setting or
        environmental details format.
    TypeError
        When input types are incorrect, such as non-string input for setting
        or environmental details.

    Examples
    --------
    >>> from prepare_setting_elements import prepare_setting_elements
    >>> setting = 'a futuristic city on a distant planet'
    >>> environmental_details = 'scorching heat, dense pollution, strict social
    hierarchy'
    >>> prep_setting_elements_output = prepare_setting_elements(setting,
    environmental_details)
    >>> print(prep_setting_elements_output)
    (
                  "{"
                  "  'setting': 'a futuristic city on a distant planet',"
                  "  'environmental_details': 'scorching heat, dense pollution,
    strict social hierarchy',"
                  "  'prepared_elements': {"
                  "    'location': 'distant planet',"
                  "    'time_period': 'indeterminate',"
                  "    'environmental_factors': ['scorching heat', 'dense
    pollution'],"
                  "    'protagonist_favorite_color': 'red'"
                  "

    """
    
    if not isinstance(setting, str):
        raise TypeError("Setting must be a string")
    if not isinstance(environmental_details, str):
        raise TypeError("Environmental details must be a string")
    
    if not setting.strip():
        raise ValueError("Setting cannot be empty")
    if not environmental_details.strip():
        raise ValueError("Environmental details cannot be empty")
    
    location_patterns = [
        r'on a ([^,\.]+)',
        r'in a ([^,\.]+)',
        r'at a ([^,\.]+)',
        r'([^,\.]+planet[^,\.]*)',
        r'([^,\.]+city[^,\.]*)',
        r'([^,\.]+town[^,\.]*)',
    ]
    
    location = 'unknown'
    for pattern in location_patterns:
        match = re.search(pattern, setting, re.IGNORECASE)
        if match:
            location = match.group(1).strip()
            break
    
    time_period = 'indeterminate'
    if re.search(r'futuristic|future|sci-fi|space|planet', setting, re.IGNORECASE):
        time_period = 'future'
    elif re.search(r'medieval|ancient|past|historical', setting, re.IGNORECASE):
        time_period = 'past'
    elif re.search(r'modern|contemporary|present|today', setting, re.IGNORECASE):
        time_period = 'present'
    
    factors = [factor.strip() for factor in environmental_details.split(',')]
    environmental_factors = []
    for factor in factors:
        factor = factor.strip()
        if factor and not re.search(r'social|hierarchy|political|economic', factor, re.IGNORECASE):
            environmental_factors.append(factor)
    
    protagonist_favorite_color = 'red'
    if 'cold' in environmental_details.lower() or 'ice' in environmental_details.lower():
        protagonist_favorite_color = 'blue'
    elif 'forest' in environmental_details.lower() or 'nature' in environmental_details.lower():
        protagonist_favorite_color = 'green'
    
    result = {
        'setting': setting,
        'environmental_details': environmental_details,
        'prepared_elements': {
            'location': location,
            'time_period': time_period,
            'environmental_factors': environmental_factors,
            'protagonist_favorite_color': protagonist_favorite_color
        }
    }
    
    return json.dumps(result, indent=2)