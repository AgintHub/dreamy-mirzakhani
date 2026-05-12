def compose_chapter_2_prose(narrative_threads: str, setting_elements: str, character_details: str, story_title: str) -> str:
    """
    Compose Chapter 2 of a story by integrating narrative threads, setting
    elements, character details, and the story's title into a well-written
    chapter.

    Parameters
    ----------
    narrative_threads : str
        A string containing narrative threads from the previous chapter and
        the story outline.
    setting_elements : str
        A string containing environmental details and other setting
        elements.
    character_details : str
        A string containing character profiles and details relevant to
        Chapter 2.
    story_title : str
        The title of the story that helps guide the narrative structure of
        Chapter 2.

    Returns
    -------
    str
        A well-written Chapter 2 text in prose format, incorporating the
        input parameters to create a cohesive narrative.

    Raises
    ------
    ValueError
        Raised when input validation fails, such as when narrative threads
        are not provided or the story title is not a string.
    TypeError
        Raised when input types do not match the expected format, such as
        when narrative threads are not a string.

    Examples
    --------
    >>> compose_chapter_2_prose(narrative_threads='...threads...',
    setting_elements='...elements...', character_details='...details...',
    story_title='My Story')
    >>> print(...)
    'Complete text of Chapter 2'.

    >>> compose_chapter_2_prose(narrative_threads='', setting_elements='',
    character_details='', story_title='')
    >>> print(...)
    Raises ValueError: 'Missing input parameters for Chapter 2 prose
    composition'.

    """
    if not isinstance(narrative_threads, str):
        raise TypeError("narrative_threads must be a string")
    if not isinstance(setting_elements, str):
        raise TypeError("setting_elements must be a string")
    if not isinstance(character_details, str):
        raise TypeError("character_details must be a string")
    if not isinstance(story_title, str):
        raise TypeError("story_title must be a string")
    
    if not narrative_threads.strip() or not story_title.strip():
        raise ValueError("Missing input parameters for Chapter 2 prose composition")
    
    chapter_2_text = f"# Chapter 2\n\n"
    
    if narrative_threads.strip():
        chapter_2_text += f"Building upon the events from the previous chapter, {narrative_threads.strip()} "
    
    if setting_elements.strip():
        chapter_2_text += f"The scene unfolds amidst {setting_elements.strip()}, creating an atmosphere that shapes the unfolding narrative. "
    
    if character_details.strip():
        chapter_2_text += f"Our characters, with their distinct personalities and motivations—{character_details.strip()}—continue their journey through this chapter. "
    
    chapter_2_text += f"As '{story_title}' progresses, the events in this chapter serve to deepen the plot and move the story toward its ultimate resolution. The narrative threads weave together seamlessly, creating a compelling continuation that builds momentum for the chapters that follow."
    
    return chapter_2_text