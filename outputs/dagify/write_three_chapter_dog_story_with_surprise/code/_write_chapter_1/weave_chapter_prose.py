def weave_chapter_prose(opening_scene: str, chapter_body: str, color_themes: str) -> str:
    """
    Creates a chapter by weaving together opening scene, chapter body, and color
    themes.

    Parameters
    ----------
    opening_scene : str
        The opening scene of the chapter, setting the tone and introducing
        the main elements.
    chapter_body : str
        The body of the chapter, elaborating on the opening scene and
        advancing the plot.
    color_themes : str
        The color themes that permeate the chapter, adding a visual and
        emotional depth.

    Returns
    -------
    str
        A well-formatted chapter text, incorporating the provided inputs and
        meeting the requirements of a cohesive narrative.

    Raises
    ------
    ValueError
        Raised when the input parameters are invalid or incomplete,
        preventing the creation of a coherent chapter.
    TypeError
        Raised when the input parameters have incorrect types, hindering the
        formation of a well-structured chapter.

    Examples
    --------
    >>> weave_chapter_prose(opening_scene='The dark forest loomed before us.',
    chapter_body='As we ventured deeper, the trees seemed to close in, their
    branches creaking ominously.', color_themes='The red moon cast an eerie glow
    over the forest, while the trees seemed to absorb the faint light, making it
    almost invisible.')
    >>> complete_chapter = chapter_text
    The dark forest loomed before us. As we ventured deeper, the trees seemed to
    close in, their branches creaking ominously. The red moon cast an eerie glow
    over the forest, while the trees seemed to absorb the faint light, making it
    almost invisible.

    """
    if not isinstance(opening_scene, str):
        raise TypeError("opening_scene must be a string")
    if not isinstance(chapter_body, str):
        raise TypeError("chapter_body must be a string")
    if not isinstance(color_themes, str):
        raise TypeError("color_themes must be a string")
    
    if not opening_scene.strip():
        raise ValueError("opening_scene cannot be empty or whitespace")
    if not chapter_body.strip():
        raise ValueError("chapter_body cannot be empty or whitespace")
    if not color_themes.strip():
        raise ValueError("color_themes cannot be empty or whitespace")
    
    opening_scene = opening_scene.strip()
    chapter_body = chapter_body.strip()
    color_themes = color_themes.strip()
    
    chapter_parts = [opening_scene]
    
    if not opening_scene.endswith(('.', '!', '?')):
        chapter_parts[0] += '.'
    
    chapter_parts.append(chapter_body)
    
    if not chapter_body.endswith(('.', '!', '?')):
        chapter_parts[1] += '.'
    
    chapter_parts.append(color_themes)
    
    if not color_themes.endswith(('.', '!', '?')):
        chapter_parts[2] += '.'
    
    return ' '.join(chapter_parts)