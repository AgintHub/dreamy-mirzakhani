from typing import List


import re


def generate_chapter_bullet_points(prompt: str, chapter_number: str, chapter_title: str) -> List[str]:
    """
    Generate three bullet points summarizing a chapter of a story, given a
    prompt, chapter number, and chapter title.

    Parameters
    ----------
    prompt : str
        A markdown prompt for the chapter.
    chapter_number : str
        The number of the chapter (e.g., 1 for Chapter 1).
    chapter_title : str
        The title of the chapter.

    Returns
    -------
    LIST_STR
        A list of three bullet points summarizing the chapter. Each point is
        a string.

    Raises
    ------
    ValueError
        If the prompt, chapter number, or chapter title is missing or
        invalid.
    TypeError
        If the input types (prompt, chapter number, and chapter title) are
        incorrect.

    Examples
    --------
    >>> generate_chapter_bullet_points('This is a chapter about ...', 1,
    'Chapter 1 Title')
    ["Bullet point 1", "Bullet point 2", "Bullet point 3"]

    >>> generate_chapter_bullet_points('This is another chapter about ...', 2,
    'Chapter 2 Title')
    ["Another bullet point 1", "Another bullet point 2", "Another bullet point
    3"]

    """
    if not isinstance(prompt, str):
        raise TypeError("prompt must be a string")
    if not isinstance(chapter_number, str):
        raise TypeError("chapter_number must be a string")
    if not isinstance(chapter_title, str):
        raise TypeError("chapter_title must be a string")
    
    if not prompt or not prompt.strip():
        raise ValueError("prompt cannot be empty or missing")
    if not chapter_number or not chapter_number.strip():
        raise ValueError("chapter_number cannot be empty or missing")
    if not chapter_title or not chapter_title.strip():
        raise ValueError("chapter_title cannot be empty or missing")
    
    
    clean_prompt = re.sub(r'[#*_`\[\]\(\)\-]', '', prompt)
    sentences = re.split(r'[.!?]+', clean_prompt)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    bullet_points = []
    
    if len(sentences) >= 3:
        bullet_points = sentences[:3]
    elif len(sentences) == 2:
        bullet_points = sentences + [f"Chapter {chapter_number} explores themes related to {chapter_title.lower()}"]
    elif len(sentences) == 1:
        bullet_points = [
            sentences[0],
            f"This chapter focuses on {chapter_title.lower()}",
            f"Key developments occur in chapter {chapter_number}"
        ]
    else:
        bullet_points = [
            f"Chapter {chapter_number}: {chapter_title}",
            f"This chapter develops the story further",
            f"Important events unfold in this section"
        ]
    
    for i in range(len(bullet_points)):
        if not bullet_points[i].endswith(('.', '!', '?')):
            bullet_points[i] += '.'
        bullet_points[i] = bullet_points[i].strip()
    
    return bullet_points[:3]