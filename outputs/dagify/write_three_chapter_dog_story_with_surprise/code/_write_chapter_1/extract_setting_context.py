import json


def extract_setting_context(story_setting: str) -> str:
    """
    This function takes a story setting string as input and returns a dictionary
    containing the extracted setting context.

    Parameters
    ----------
    story_setting : str
        The story setting string from which the setting context will be
        extracted.

    Returns
    -------
    dict
        A dictionary containing the setting context, with keys representing
        the different setting elements and values representing their
        corresponding values.

    Raises
    ------
    ValueError
        If the input story setting string is malformed or missing required
        elements.
    TypeError
        If the input story setting string cannot be properly converted to a
        dictionary.

    Examples
    --------
    >>> extract_setting_context('location: city, time_period: past,
    environmental_details: sunny')
    >>> print(extract_setting_context('location: forest, time_period: present,
    environmental_details: rainy'))
    {"location": "forest", "time_period": "present", "environmental_details":
    "rainy"}

    >>> extract_setting_context('invalid setting string')
    >>> print(extract_setting_context('missing required elements'))
    ValueError: Invalid story setting string

    """
    
    if not isinstance(story_setting, str):
        raise TypeError("Input story setting string cannot be properly converted to a dictionary.")
    
    if not story_setting.strip():
        raise ValueError("Invalid story setting string")
    
    pairs = story_setting.split(',')
    setting_dict = {}
    
    required_keys = {'location', 'time_period', 'environmental_details'}
    
    for pair in pairs:
        pair = pair.strip()
        if ':' not in pair:
            raise ValueError("Invalid story setting string")
        
        key, value = pair.split(':', 1)
        key = key.strip()
        value = value.strip()
        
        if not key or not value:
            raise ValueError("Invalid story setting string")
        
        setting_dict[key] = value
    
    if not required_keys.issubset(setting_dict.keys()):
        raise ValueError("Invalid story setting string")
    
    return json.dumps(setting_dict)