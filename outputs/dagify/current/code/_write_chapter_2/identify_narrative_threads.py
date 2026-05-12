import re


def identify_narrative_threads(previous_chapter: str, outline: str, characters: str) -> str:
    """
    This function identifies narrative threads by analyzing the chapter, story
    outline, and character profiles.

    Parameters
    ----------
    previous_chapter : str
        Text of the previous chapter used as input for narrative thread
        identification.
    outline : str
        Story outline used as input for narrative thread identification.
    characters : str
        Character profiles used as input for narrative thread
        identification.

    Returns
    -------
    List[str]
        List of narrative threads extracted from the chapter, story outline,
        and character profiles.

    Raises
    ------
    ValueError
        Raised when the input chapter, outline, or characters do not match
        the expected format.
    TypeError
        Raised when the input types are not as expected.

    Examples
    --------
    >>> narrative_threads = identify_narrative_threads(chapter_text, outline,
    characters)
    >>> print(narrative_threads)
    [Thread 1, Thread 2, ...]

    >>> narrative_threads = identify_narrative_threads(chapter_text, outline,
    characters)
    >>> print(narrative_threads)
    [Thread A, Thread B, ...]

    """
    
    if not isinstance(previous_chapter, str):
        raise TypeError("previous_chapter must be a string")
    if not isinstance(outline, str):
        raise TypeError("outline must be a string")
    if not isinstance(characters, str):
        raise TypeError("characters must be a string")
    
    if not previous_chapter.strip() or not outline.strip() or not characters.strip():
        raise ValueError("Input chapter, outline, or characters do not match the expected format")
    
    threads = []
    
    character_lines = [line.strip() for line in characters.split('\n') if line.strip()]
    for line in character_lines:
        if any(keyword in line.lower() for keyword in ['conflict', 'goal', 'arc', 'motivation', 'relationship']):
            threads.append(f"Character thread: {line[:50]}..." if len(line) > 50 else f"Character thread: {line}")
    
    outline_sentences = re.split(r'[.!?]+', outline)
    for sentence in outline_sentences:
        sentence = sentence.strip()
        if sentence and any(keyword in sentence.lower() for keyword in ['plot', 'conflict', 'tension', 'mystery', 'romance', 'subplot']):
            threads.append(f"Plot thread: {sentence[:50]}..." if len(sentence) > 50 else f"Plot thread: {sentence}")
    
    chapter_sentences = re.split(r'[.!?]+', previous_chapter)
    for sentence in chapter_sentences:
        sentence = sentence.strip()
        if sentence and any(keyword in sentence.lower() for keyword in ['unresolved', 'mystery', 'question', 'tension', 'cliffhanger']):
            threads.append(f"Continuation thread: {sentence[:50]}..." if len(sentence) > 50 else f"Continuation thread: {sentence}")
    
    seen = set()
    unique_threads = []
    for thread in threads:
        if thread not in seen:
            seen.add(thread)
            unique_threads.append(thread)
    
    if not unique_threads:
        if 'character' in characters.lower():
            unique_threads.append("Character development thread")
        if 'plot' in outline.lower():
            unique_threads.append("Main plot thread")
        if previous_chapter:
            unique_threads.append("Story continuation thread")
    
    return str(unique_threads)