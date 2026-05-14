from typing import List


import re


def generate_chapter_titles(prompt: str, story_title: str) -> List[str]:
    """
    Generate chapter titles given a prompt and story title.

    Parameters
    ----------
    prompt : str
        Input prompt used to generate chapter titles.
    story_title : str
        Story title used to generate chapter titles.

    Returns
    -------
    List[str]
        A list of chapter titles.

    Raises
    ------
    ValueError
        If either prompt or story title is empty.
    TypeError
        If prompt or story title is not a string.

    Examples
    --------
    >>> from story_gen_shims import generate_chapter_titles
    >>> chapter_titles = generate_chapter_titles('Example prompt', 'Example
    story title')
    >>> print(chapter_titles)
    ['Chapter 1', 'Chapter 2', 'Chapter 3']

    """
    if not isinstance(prompt, str):
        raise TypeError("prompt must be a string")
    if not isinstance(story_title, str):
        raise TypeError("story_title must be a string")
    if not prompt.strip():
        raise ValueError("prompt cannot be empty")
    if not story_title.strip():
        raise ValueError("story_title cannot be empty")
    
    
    chapter_count_match = re.search(r'(\d+)\s*chapters?', prompt.lower())
    num_chapters = int(chapter_count_match.group(1)) if chapter_count_match else 5
    
    chapter_titles = []
    
    is_fantasy = any(word in prompt.lower() for word in ['fantasy', 'magic', 'dragon', 'wizard', 'quest'])
    is_mystery = any(word in prompt.lower() for word in ['mystery', 'detective', 'crime', 'murder', 'investigation'])
    is_romance = any(word in prompt.lower() for word in ['romance', 'love', 'relationship', 'wedding', 'heart'])
    is_adventure = any(word in prompt.lower() for word in ['adventure', 'journey', 'travel', 'explore', 'expedition'])
    
    for i in range(1, num_chapters + 1):
        if is_fantasy:
            titles = ["The Call to Adventure", "The Magical Discovery", "Trials and Tribulations", "The Dark Hour", "Victory and Return"]
        elif is_mystery:
            titles = ["The Crime", "First Clues", "Deeper Investigation", "The Revelation", "Justice Served"]
        elif is_romance:
            titles = ["First Meeting", "Growing Closer", "Complications Arise", "The Truth Revealed", "Love Conquers All"]
        elif is_adventure:
            titles = ["The Journey Begins", "Into the Unknown", "Facing Challenges", "The Greatest Test", "Home Again"]
        else:
            titles = ["The Beginning", "Rising Action", "The Turning Point", "The Climax", "Resolution"]
        
        if i <= len(titles):
            chapter_titles.append(f"Chapter {i}: {titles[i-1]}")
        else:
            chapter_titles.append(f"Chapter {i}")
    
    return chapter_titles[:num_chapters]