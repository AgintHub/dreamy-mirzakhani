def integrate_color_themes(outline_color: str, character_color: str, setting_color: str) -> str:
    """
    Integrate color themes from different story components.

    Parameters
    ----------
    outline_color : str
        The color theme from the story outline.
    character_color : str
        The color theme from the character profiles.
    setting_color : str
        The color theme from the story setting.

    Returns
    -------
    dict
        A dictionary containing the integrated color themes.

    Raises
    ------
    ValueError
        When the input colors are invalid or inconsistent.
    TypeError
        When the input colors have incorrect data types.

    Examples
    --------
    >>> integrate_color_themes(outline_color='blue', character_color='green',
    setting_color='yellow')
    >>> print(output)
    {}

    >>> integrate_color_themes(outline_color='red', character_color='orange',
    setting_color='red')
    >>> print(output)
    {"color": "red"}

    """
    if not isinstance(outline_color, str) or not isinstance(character_color, str) or not isinstance(setting_color, str):
        raise TypeError("All input colors must be strings")
    
    valid_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple', 'pink', 'brown', 'black', 'white', 'gray', 'grey'}
    
    if outline_color.lower() not in valid_colors or character_color.lower() not in valid_colors or setting_color.lower() not in valid_colors:
        raise ValueError("Invalid color provided")
    
    colors = [outline_color.lower(), character_color.lower(), setting_color.lower()]
    
    color_counts = {}
    for color in colors:
        color_counts[color] = color_counts.get(color, 0) + 1
    
    dominant_color = None
    max_count = 0
    for color, count in color_counts.items():
        if count > max_count:
            max_count = count
            dominant_color = color
    
    if max_count >= 2:
        return '{"color": "' + dominant_color + '"}'
    else:
        return '{}'