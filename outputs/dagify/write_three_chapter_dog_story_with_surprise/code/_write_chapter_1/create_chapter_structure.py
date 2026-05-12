import json


def create_chapter_structure(chapter_bullet_points: str, story_title: str) -> str:
    """
    Creates a dictionary representing a chapter based on bullet points and story
    title.

    Parameters
    ----------
    chapter_bullet_points : str
        String containing bullet points for the chapter.
    story_title : str
        String containing the story title.

    Returns
    -------
    dict
        A dictionary representing the chapter content with keys for bullet
        points and story title.

    Raises
    ------
    ValueError
        If the input parameters are not valid.
    TypeError
        If the input parameters are not strings.

    Examples
    --------
    >>> create_chapter_structure('Chapter 1 bullet points', 'Story Title')
    {'bullet_points': 'Chapter 1 bullet points', 'story_title': 'Story Title'}

    >>> create_chapter_structure('Another chapter bullet points', 'Another Story
    Title')
    {'bullet_points': 'Another chapter bullet points', 'story_title': 'Another
    Story Title'}

    """
    if not isinstance(chapter_bullet_points, str):
        raise TypeError("chapter_bullet_points must be a string")
    if not isinstance(story_title, str):
        raise TypeError("story_title must be a string")
    if not chapter_bullet_points.strip():
        raise ValueError("chapter_bullet_points cannot be empty")
    if not story_title.strip():
        raise ValueError("story_title cannot be empty")
    
    chapter_dict = {
        'bullet_points': chapter_bullet_points,
        'story_title': story_title
    }
    
    return json.dumps(chapter_dict)