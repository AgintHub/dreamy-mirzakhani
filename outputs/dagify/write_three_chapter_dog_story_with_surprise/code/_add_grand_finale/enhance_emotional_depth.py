import re


def enhance_emotional_depth(content: str, character_connections: str) -> str:
    """
    This shim function enhances the emotional depth of a narrative by using
    character connections to create a more engaging and relatable story.

    Parameters
    ----------
    content : str
        The input narrative content to be enhanced.
    character_connections : str
        The character connections to leverage for emotional depth
        enhancement.

    Returns
    -------
    dict
        A dictionary containing the enhanced narrative content and input
        parameters for transparency and traceability.

    Raises
    ------
    ValueError
        Raised when the input content or character connections are invalid
        or contradictory.
    TypeError
        Raised when the input types are incorrect or do not match the
        expected structure.

    Examples
    --------
    >>> shim = enhance_emotional_depth(data={'content': 'example prose',
    'character_connections': 'example connections'})
    >>> output = shim.output
    >>> print(output)
    {output: example prose with enhanced emotional depth, content: example
    prose, character_connections: example connections}

    >>> shim = enhance_emotional_depth(data={'content': 'another prose',
    'character_connections': 'another connections'})
    >>> output = shim.output
    >>> print(output)
    {output: another prose with enhanced emotional depth, content: another
    prose, character_connections: another connections}

    """
    
    if not isinstance(content, str) or not isinstance(character_connections, str):
        raise TypeError("Input types must be strings")
    
    if not content.strip() or not character_connections.strip():
        raise ValueError("Content and character connections cannot be empty")
    
    connections_list = [conn.strip() for conn in character_connections.split(',') if conn.strip()]
    
    enhanced_content = content
    
    for connection in connections_list:
        if connection.lower() in enhanced_content.lower():
            pattern = re.compile(re.escape(connection), re.IGNORECASE)
            enhanced_content = pattern.sub(f"{connection} (whose bond runs deeper than mere words)", enhanced_content, count=1)
    
    sentences = re.split(r'[.!?]+', enhanced_content)
    emotional_phrases = [
        "with a heavy heart", 
        "feeling the weight of emotion",
        "touched by profound connection",
        "moved by an inexplicable bond"
    ]
    
    enhanced_sentences = []
    for i, sentence in enumerate(sentences):
        if sentence.strip():
            if i % 2 == 0 and len(connections_list) > 0:
                enhanced_sentences.append(sentence.strip() + f" - {emotional_phrases[i % len(emotional_phrases)]}")
            else:
                enhanced_sentences.append(sentence.strip())
    
    final_enhanced = '. '.join(enhanced_sentences)
    if not final_enhanced.endswith('.'):
        final_enhanced += '.'
    
    return final_enhanced