import re


def develop_chapter_events(bullet_points: str, character_context: str, setting_context: str) -> str:
    """
    Crafts a chapter by integrating character context and setting details with
    given bullet points.

    Parameters
    ----------
    bullet_points : str
        Three bullet points summarizing the chapter's content.
    character_context : str
        Contextual background on the protagonist or main character in the
        chapter.
    setting_context : str
        Description of the setting or environment where the chapter takes
        place.

    Returns
    -------
    str
        Formatted chapter that accurately reflects the provided context.

    Raises
    ------
    ValueError
        Raised when input validation fails, such as missing or misformatted
        context.
    TypeError
        Raised when input types are incorrect or incompatible.

    Examples
    --------
    >>> develop_chapter_events(bullet_points='Point 1. Point 2. Point 3.',
    character_context='Context about main character.', setting_context='Setting
    details.')
    A well-structured chapter with character context, setting details, and
    bullet points.

    >>> develop_chapter_events(bullet_points='Another point 1. Another point 2.
    Another point 3.', character_context='Different context about main
    character.', setting_context='Different setting details.')
    Another well-structured chapter with different character context, setting
    details, and bullet points.

    """
    if not isinstance(bullet_points, str):
        raise TypeError("bullet_points must be a string")
    if not isinstance(character_context, str):
        raise TypeError("character_context must be a string")
    if not isinstance(setting_context, str):
        raise TypeError("setting_context must be a string")
    
    if not bullet_points.strip():
        raise ValueError("bullet_points cannot be empty")
    if not character_context.strip():
        raise ValueError("character_context cannot be empty")
    if not setting_context.strip():
        raise ValueError("setting_context cannot be empty")
    
    
    points = re.split(r'\d+\.', bullet_points)
    points = [point.strip() for point in points if point.strip()]
    
    if len(points) < 3:
        raise ValueError("bullet_points must contain at least three points")
    
    chapter = f"Chapter\n\n"
    chapter += f"Setting: {setting_context}\n\n"
    chapter += f"Character Background: {character_context}\n\n"
    chapter += f"Events:\n"
    
    for i, point in enumerate(points[:3], 1):
        chapter += f"{i}. {point}\n"
    
    chapter += f"\nIn this chapter, our protagonist navigates through {setting_context.lower()}, "
    chapter += f"drawing upon their {character_context.lower()} as they encounter the following developments: "
    chapter += f"{', '.join(points[:3])}. "
    chapter += f"These events shape the narrative and drive the story forward in meaningful ways."
    
    return chapter