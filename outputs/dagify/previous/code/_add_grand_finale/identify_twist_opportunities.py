import json
import re


def identify_twist_opportunities(narrative_data: str, chapter_content: str) -> str:
    """
    Identify potential plot twist opportunities within the narrative structure
    of Chapter 3, based on the provided narrative data and chapter content.

    Parameters
    ----------
    narrative_data : dict
        The analyzed narrative structure, containing connections,
        characters, and plot elements.
    chapter_content : str
        The prose content of Chapter 3, including any relevant details or
        clues for plot twists.

    Returns
    -------
    dict
        A dictionary containing twist opportunity elements, including
        potential plot threads and character arcs to be exploited.

    Raises
    ------
    TypeError
        Raised when either narrative_data or chapter_content is not of the
        expected type.

    Examples
    --------
    >>> twist_opportunities_dict =
    identify_twist_opportunities(narrative_data={'plot_structure': [...],
    'characters': [...]}, chapter_content='This is the content of Chapter 3.')
    >>> print(twist_opportunities_dict)
    {'thread1': {'description': 'Potential plot thread 1',
    'characters_involved': ['Character1', 'Character2']}, 'thread2':
    {'description': 'Potential plot thread 2', 'characters_involved':
    ['Character3', 'Character4']}}

    """
    
    if not isinstance(narrative_data, str) or not isinstance(chapter_content, str):
        raise TypeError("Both narrative_data and chapter_content must be strings")
    
    try:
        parsed_data = json.loads(narrative_data)
    except json.JSONDecodeError:
        parsed_data = {}
    
    twist_opportunities = {}
    
    characters = parsed_data.get('characters', [])
    plot_structure = parsed_data.get('plot_structure', [])
    
    character_names = []
    if isinstance(characters, list):
        for char in characters:
            if isinstance(char, dict) and 'name' in char:
                character_names.append(char['name'])
            elif isinstance(char, str):
                character_names.append(char)
    
    character_mentions = {}
    for char in character_names:
        mentions = len(re.findall(re.escape(char), chapter_content, re.IGNORECASE))
        character_mentions[char] = mentions
    
    thread_counter = 1
    
    if len(character_names) >= 2:
        sorted_chars = sorted(character_mentions.items(), key=lambda x: x[1], reverse=True)
        top_chars = [char[0] for char in sorted_chars[:4]]
        
        for i in range(0, len(top_chars), 2):
            if i + 1 < len(top_chars):
                thread_key = f'thread{thread_counter}'
                twist_opportunities[thread_key] = {
                    'description': f'Potential plot thread {thread_counter}',
                    'characters_involved': [top_chars[i], top_chars[i + 1]]
                }
                thread_counter += 1
    
    mystery_keywords = ['secret', 'hidden', 'mysterious', 'unknown', 'surprise', 'reveal']
    for keyword in mystery_keywords:
        if keyword.lower() in chapter_content.lower():
            thread_key = f'thread{thread_counter}'
            involved_chars = [char for char in character_names if char in chapter_content]
            if not involved_chars:
                involved_chars = character_names[:2] if len(character_names) >= 2 else character_names
            
            twist_opportunities[thread_key] = {
                'description': f'Potential plot thread {thread_counter}',
                'characters_involved': involved_chars[:2]
            }
            thread_counter += 1
            break
    
    if not twist_opportunities:
        twist_opportunities = {
            'thread1': {
                'description': 'Potential plot thread 1',
                'characters_involved': character_names[:2] if len(character_names) >= 2 else ['Character1', 'Character2']
            }
        }
    
    return json.dumps(twist_opportunities)