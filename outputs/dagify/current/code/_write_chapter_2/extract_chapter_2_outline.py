import re
import json


def extract_chapter_2_outline(outline: str, bullet_points: str) -> str:
    """
    Extracts the chapter 2 outline from a given story outline and bullet points.

    Parameters
    ----------
    outline : str
        The story outline as a string
    bullet_points : str
        The chapter 2 bullet points as a string

    Returns
    -------
    PRIMITIVEType.STR dict
        The extracted chapter 2 outline as a dictionary with string values

    Raises
    ------
    ValueError
        When the input outline or bullet points are invalid
    TypeError
        When the input type is incorrect

    Examples
    --------
    >>> output = extract_chapter_2_outline('story_outline',
    'chapter_2_bullet_points')
    >>> print(output)
    {'chapter_2_heading': 'Chapter 2 Heading', 'chapter_2_subheading': 'Chapter
    2 Subheading'}

    >>> output = extract_chapter_2_outline('story_outline_with_error',
    'chapter_2_bullet_points_with_error')
    >>> print(output)
    ValueError: Invalid input outline

    """
    
    if not isinstance(outline, str) or not isinstance(bullet_points, str):
        raise TypeError("Input type is incorrect")
    
    if not outline.strip() or not bullet_points.strip():
        raise ValueError("Invalid input outline")
    
    outline_lines = outline.strip().split('\n')
    bullet_lines = bullet_points.strip().split('\n')
    
    chapter_2_heading = ""
    chapter_2_subheading = ""
    
    for line in outline_lines:
        if re.search(r'chapter\s*2', line, re.IGNORECASE):
            chapter_2_heading = line.strip()
            break
    
    if not chapter_2_heading:
        chapter_2_heading = "Chapter 2"
    
    for line in bullet_lines:
        clean_line = line.strip()
        if clean_line and not clean_line.startswith('-') and not clean_line.startswith('*'):
            chapter_2_subheading = clean_line
            break
    
    if not chapter_2_subheading:
        for line in bullet_lines:
            clean_line = line.strip().lstrip('-*').strip()
            if clean_line:
                chapter_2_subheading = clean_line
                break
    
    if not chapter_2_subheading:
        chapter_2_subheading = "Chapter 2 Content"
    
    result = {
        "chapter_2_heading": chapter_2_heading,
        "chapter_2_subheading": chapter_2_subheading
    }
    
    return json.dumps(result)