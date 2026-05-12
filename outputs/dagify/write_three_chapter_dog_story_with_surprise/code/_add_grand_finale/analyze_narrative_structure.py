import re
import json


def analyze_narrative_structure(content: str, summary: str) -> str:
    """
    Analyzes the narrative structure of the provided chapter content and
    summary, returning a dictionary containing the analyzed results.

    Parameters
    ----------
    content : str
        The chapter content to analyze.
    summary : str
        A summary of the chapter content.

    Returns
    -------
    dict
        A dictionary containing the analyzed narrative structure.

    Raises
    ------
    ValueError
        When the input content or summary is empty or contains non-string
        values.
    TypeError
        When the input content or summary is not a string.

    Examples
    --------
    >>> analyzed_narrative = analyze_narrative_structure(content='The sun was
    shining brightly in the sky.', summary='The story begins on a sunny day.')
    >>> print(analyzed_narrative)
    { content: 'The sun was shining brightly in the sky.', summary: 'The story
    begins on a sunny day.', structure: {key: value} }

    >>> analyzed_narrative = analyze_narrative_structure(content='The cat sat on
    the mat.', summary='The cat is happy.')
    >>> print(analyzed_narrative)
    { content: 'The cat sat on the mat.', summary: 'The cat is happy.',
    structure: {key: value} }

    """
    if not isinstance(content, str):
        raise TypeError("Content must be a string")
    if not isinstance(summary, str):
        raise TypeError("Summary must be a string")
    
    if not content.strip():
        raise ValueError("Content cannot be empty")
    if not summary.strip():
        raise ValueError("Summary cannot be empty")
    
    
    sentences = re.split(r'[.!?]+', content.strip())
    sentences = [s.strip() for s in sentences if s.strip()]
    
    word_count = len(content.split())
    sentence_count = len(sentences)
    avg_sentence_length = word_count / max(sentence_count, 1)
    
    past_tense_indicators = len(re.findall(r'\b\w+ed\b', content.lower()))
    dialogue_indicators = len(re.findall(r'["\'].*?["\']', content))
    
    structure_analysis = {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'avg_sentence_length': round(avg_sentence_length, 2),
        'past_tense_indicators': past_tense_indicators,
        'dialogue_indicators': dialogue_indicators,
        'narrative_type': 'descriptive' if dialogue_indicators == 0 else 'dialogue_heavy'
    }
    
    result = {
        'content': content,
        'summary': summary,
        'structure': structure_analysis
    }
    
    return json.dumps(result)