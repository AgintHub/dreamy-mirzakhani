import re


def integrate_thematic_symbolism(content: str, narrative_themes: str) -> str:
    """
    The integrate_thematic_symbolism shim function integrates thematic symbolism
    into the narrative to enhance its emotional depth and coherence. It takes
    two inputs: enhanced emotions and narrative themes, and returns the
    narrative with integrated thematic symbolism.

    Parameters
    ----------
    enhanced_emotions : str
        The narrative with enhanced emotions.
    narrative_themes : str
        The narrative themes to be integrated.

    Returns
    -------
    str
        The narrative with integrated thematic symbolism.
    """
    
    themes = [theme.strip().lower() for theme in narrative_themes.split(',') if theme.strip()]
    
    symbol_mappings = {
        'love': ['heart', 'rose', 'dove', 'light', 'warmth'],
        'death': ['shadow', 'winter', 'darkness', 'silence', 'void'],
        'hope': ['dawn', 'spring', 'star', 'bridge', 'seed'],
        'betrayal': ['serpent', 'mask', 'thorns', 'storm', 'mirror'],
        'redemption': ['phoenix', 'river', 'mountain', 'fire', 'journey'],
        'loss': ['autumn', 'rain', 'echo', 'empty chair', 'fading'],
        'freedom': ['bird', 'wind', 'open door', 'horizon', 'flight'],
        'fear': ['labyrinth', 'fog', 'chains', 'abyss', 'ice'],
        'growth': ['tree', 'butterfly', 'sunrise', 'bloom', 'path'],
        'isolation': ['island', 'wall', 'desert', 'silence', 'cage']
    }
    
    enhanced_content = content
    
    for theme in themes:
        if theme in symbol_mappings:
            symbols = symbol_mappings[theme]
            
            emotion_patterns = {
                'joy': r'\b(happy|joyful|elated|cheerful|delighted)\b',
                'sadness': r'\b(sad|sorrowful|melancholy|grief|despair)\b',
                'anger': r'\b(angry|furious|rage|irritated|enraged)\b',
                'fear': r'\b(afraid|terrified|anxious|scared|worried)\b',
                'love': r'\b(love|affection|adoration|cherish|devoted)\b'
            }
            
            for emotion, pattern in emotion_patterns.items():
                matches = list(re.finditer(pattern, enhanced_content, re.IGNORECASE))
                
                for i, match in enumerate(matches):
                    if i < len(symbols):
                        symbol = symbols[i % len(symbols)]
                        original_text = match.group()
                        
                        if theme == 'love' and emotion == 'love':
                            replacement = f"{original_text}, like a {symbol} blooming in moonlight,"
                        elif theme == 'death' and emotion == 'sadness':
                            replacement = f"{original_text}, as {symbol} crept through the silence,"
                        elif theme == 'hope' and emotion == 'joy':
                            replacement = f"{original_text}, bright as the {symbol} breaking through,"
                        else:
                            replacement = f"{original_text}, echoing with the essence of {symbol},"
                        
                        enhanced_content = enhanced_content[:match.start()] + replacement + enhanced_content[match.end():]
    
    sentences = re.split(r'(?<=[.!?])\s+', enhanced_content)
    
    for theme in themes:
        if theme in symbol_mappings and len(sentences) > 2:
            symbol = symbol_mappings[theme][0]
            middle_idx = len(sentences) // 2
            
            if not any(sym in sentences[middle_idx].lower() for sym in symbol_mappings[theme]):
                sentences[middle_idx] = sentences[middle_idx].rstrip('.!?') + f", where {symbol} seemed to whisper of {theme}."
    
    return ' '.join(sentences)