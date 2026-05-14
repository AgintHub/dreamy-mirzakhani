import re


def generate_chapter_summary(chapter_content: str, bullet_points: str) -> str:
    """
    Generates a summary of a chapter in a story based on its content and bullet
    points.

    Parameters
    ----------
    chapter_content : str
        The content of the chapter to be summarized.
    bullet_points : str
        The bullet points of the chapter to be summarized.

    Returns
    -------
    tuple
        A tuple containing the generated chapter summary, chapter content,
        and bullet points.

    Raises
    ------
    ValueError
        When the input chapter content or bullet points are invalid.
    TypeError
        When the input types are incorrect or unsupported.

    Examples
    --------
    >>> chapter_content = 'This is the story of a brave knight.'
    >>> bullet_points = 'He fought many battles.', 'He defeated his enemies.'
    The brave knight fought many battles and defeated his enemies.

    >>> chapter_content = 'The little girl went to the store.'
    >>> bullet_points = 'She bought some milk.', 'She returned home.'
    The little girl went to the store, bought some milk, and returned home.

    """
    if not isinstance(chapter_content, str):
        raise TypeError("chapter_content must be a string")
    if not isinstance(bullet_points, str):
        raise TypeError("bullet_points must be a string")
    
    if not chapter_content.strip():
        raise ValueError("chapter_content cannot be empty")
    if not bullet_points.strip():
        raise ValueError("bullet_points cannot be empty")
    
    
    chapter_sentences = re.split(r'[.!?]+', chapter_content.strip())
    chapter_sentences = [s.strip() for s in chapter_sentences if s.strip()]
    
    bullet_list = re.split(r'[.!?]+|,\s*', bullet_points.strip())
    bullet_list = [b.strip() for b in bullet_list if b.strip()]
    
    if chapter_sentences:
        main_subject = chapter_sentences[0]
        subject_match = re.search(r'^(The\s+\w+\s+\w+|\w+\s+\w+)', main_subject)
        if subject_match:
            subject = subject_match.group(1)
        else:
            subject = "The story"
    else:
        subject = "The story"
    
    if len(bullet_list) >= 2:
        actions = bullet_list[:-1]
        last_action = bullet_list[-1]
        action_text = ", ".join(actions) + ", and " + last_action
    elif len(bullet_list) == 1:
        action_text = bullet_list[0]
    else:
        action_text = "continued the story"
    
    action_text = re.sub(r'^(He|She|It)\s+', '', action_text, flags=re.IGNORECASE)
    action_text = action_text.lower()
    
    summary = f"{subject} {action_text}."
    
    return summary