import re
import json


def analyze_chapter_1_context(chapter_1_text: str) -> str:
    """
    Analyzes Chapter 1 text and extracts narrative context.

    Parameters
    ----------
    chapter_1_text : str
        The complete, prose-formatted text of Chapter 1.

    Returns
    -------
    dict
        A dictionary containing the narrative context of Chapter 1,
        including character traits, story themes, settings, and plot
        threads.

    Raises
    ------
    ValueError
        When input validation fails.
    TypeError
        When input types are incorrect.

    Examples
    --------
    >>> analyze_chapter_1_context(chapter_1_text='The dog ran across the green
    field.')
    {'context': {'dog_trait': 'adventurous', 'story_theme': 'nature', 'setting':
    'outdoor', 'plot_thread': 'escape'}

    """
    
    if not isinstance(chapter_1_text, str):
        raise TypeError("Input must be a string")
    
    if not chapter_1_text or not chapter_1_text.strip():
        raise ValueError("Chapter text cannot be empty")
    
    text = chapter_1_text.lower().strip()
    
    character_traits = []
    if re.search(r'\b(ran|running|rushed|hurried)\b', text):
        character_traits.append('adventurous')
    if re.search(r'\b(slowly|carefully|cautiously)\b', text):
        character_traits.append('careful')
    if re.search(r'\b(smiled|laughed|happy)\b', text):
        character_traits.append('cheerful')
    
    story_themes = []
    if re.search(r'\b(field|forest|mountain|ocean|nature|trees|grass)\b', text):
        story_themes.append('nature')
    if re.search(r'\b(love|friendship|family|together)\b', text):
        story_themes.append('relationships')
    if re.search(r'\b(adventure|journey|quest|explore)\b', text):
        story_themes.append('adventure')
    
    settings = []
    if re.search(r'\b(field|forest|mountain|outside|outdoor)\b', text):
        settings.append('outdoor')
    if re.search(r'\b(house|room|building|indoor)\b', text):
        settings.append('indoor')
    if re.search(r'\b(city|town|street|urban)\b', text):
        settings.append('urban')
    
    plot_threads = []
    if re.search(r'\b(ran|escape|fled|away)\b', text):
        plot_threads.append('escape')
    if re.search(r'\b(found|discovered|search)\b', text):
        plot_threads.append('discovery')
    if re.search(r'\b(meet|met|encounter)\b', text):
        plot_threads.append('encounter')
    
    context = {
        'character_trait': character_traits[0] if character_traits else 'unknown',
        'story_theme': story_themes[0] if story_themes else 'general',
        'setting': settings[0] if settings else 'unspecified',
        'plot_thread': plot_threads[0] if plot_threads else 'introduction'
    }
    
    result = {'context': context}
    return json.dumps(result)