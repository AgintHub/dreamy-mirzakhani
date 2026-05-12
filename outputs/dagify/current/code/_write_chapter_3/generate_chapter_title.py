import re


def generate_chapter_title(outline_title: str, chapter_titles: str) -> str:
    """
    Generate a Chapter 3 title from the provided outline title and chapter
    titles.

    Parameters
    ----------
    outline_title : str
        The title of the story's outline.
    chapter_titles : str
        A list of chapter titles in the story, typically in the format
        'Chapter 1: Title', 'Chapter 2: Title', etc.

    Returns
    -------
    str
        A generated title for Chapter 3 in the format 'Chapter 3: Title'.

    Raises
    ------
    ValueError
        When input validation fails, such as when the provided outline title
        is empty or the chapter titles list is not in the correct format.
    TypeError
        When input types are incorrect, such as when the outline title is
        not a string or the chapter titles list is not a list of strings.

    Examples
    --------
    >>> generate_chapter_title('My Story Outline', 'Chapter 1: Title, Chapter 2:
    Title')
    'Chapter 3: Title'

    >>> generate_chapter_title('My Story Outline', 'Chapter 1: Title')
    'Chapter 2: Title' (Note: This would raise an error in the original code as
    it expects chapter_titles to be a list)

    """
    
    if not isinstance(outline_title, str):
        raise TypeError("outline_title must be a string")
    if not isinstance(chapter_titles, str):
        raise TypeError("chapter_titles must be a string")
    
    if not outline_title.strip():
        raise ValueError("outline_title cannot be empty")
    
    if not chapter_titles.strip():
        raise ValueError("chapter_titles cannot be empty")
    
    chapter_pattern = r'Chapter\s+\d+:\s*([^,]+)'
    matches = re.findall(chapter_pattern, chapter_titles)
    
    if len(matches) < 2:
        raise ValueError("chapter_titles must contain at least 2 chapters in the correct format")
    
    last_title = matches[-1].strip()
    
    if 'beginning' in last_title.lower() or 'start' in last_title.lower():
        generated_title = 'The Journey Continues'
    elif 'conflict' in last_title.lower() or 'problem' in last_title.lower():
        generated_title = 'Resolution'
    elif 'mystery' in last_title.lower() or 'secret' in last_title.lower():
        generated_title = 'Revelation'
    else:
        generated_title = 'New Developments'
    
    return f'Chapter 3: {generated_title}'