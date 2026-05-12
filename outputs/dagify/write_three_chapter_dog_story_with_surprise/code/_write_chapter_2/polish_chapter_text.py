import re


def polish_chapter_text(raw_text: str, story_context: str) -> str:
    """
    Polishes the text of a chapter by processing its syntax and style, resulting
    in refined prose.

    Parameters
    ----------
    raw_text : str
        The raw chapter text in its original state
    story_context : str
        The narrative context of the chapter, including previous events and
        character interactions

    Returns
    -------
    STR
        The polished chapter text in prose format

    Raises
    ------
    ValueError
        When the input text is invalid or cannot be processed.
    TypeError
        When the input type is incorrect or missing.

    Examples
    --------
    >>> polished_chapter = polish_chapter_text('This is a raw chapter text.',
    'This is the narrative context.')
    'This is the polished chapter text.'

    >>> polished_chapter = polish_chapter_text('Another raw chapter text.', '')
    'Another polished chapter text.'

    """
    
    if not isinstance(raw_text, str):
        raise TypeError("raw_text must be a string")
    if not isinstance(story_context, str):
        raise TypeError("story_context must be a string")
    
    if not raw_text or not raw_text.strip():
        raise ValueError("Input text is invalid or cannot be processed")
    
    text = raw_text.strip()
    
    text = re.sub(r'\s+', ' ', text)
    
    sentences = re.split(r'(?<=[.!?])\s+', text)
    polished_sentences = []
    
    for sentence in sentences:
        if not sentence.strip():
            continue
            
        polished = sentence.strip()
        
        polished = re.sub(r'\b(very|really|quite|pretty|rather)\s+', '', polished, flags=re.IGNORECASE)
        
        polished = re.sub(r'\bthat\s+', '', polished, flags=re.IGNORECASE)
        
        polished = re.sub(r'\bin order to\b', 'to', polished, flags=re.IGNORECASE)
        
        polished = re.sub(r'\bdue to the fact that\b', 'because', polished, flags=re.IGNORECASE)
        
        if polished and not polished[0].isupper():
            polished = polished[0].upper() + polished[1:]
            
        if polished and polished[-1] not in '.!?':
            polished += '.'
            
        polished_sentences.append(polished)
    
    polished_text = ' '.join(polished_sentences)
    
    if story_context and story_context.strip():
        if 'action' in story_context.lower() or 'battle' in story_context.lower():
            polished_text = re.sub(r'\bwas\s+', '', polished_text)
            polished_text = re.sub(r'\bwere\s+', '', polished_text)
        elif 'dialogue' in story_context.lower() or 'conversation' in story_context.lower():
            polished_text = re.sub(r'\bsaid\b', 'replied', polished_text, count=1)
    
    return polished_text