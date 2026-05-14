def determine_plot_role(character_data: str) -> str:
    """
    Determine the character's role in the plot based on their characteristics.

    Parameters
    ----------
    character_data : str
        The character's name, age, personality traits, etc., formatted as a
        string.

    Returns
    -------
    str
        The character's functional role within the story, represented as a
        string.

    Raises
    ------
    ValueError
        When the input string is invalid or missing required information.
    TypeError
        When the input is not a string.

    Examples
    --------
    >>> function(input) -> expected output
    >>> determine_plot_role('John, 30, brave, loyal') -> 'protagonist'
    >>> determine_plot_role('Jane, 25, sweet, naive') -> 'sidekick'
    'protagonist'

    >>> function(input) -> expected output
    >>> determine_plot_role('Bob, 40, mean, stubborn') -> 'antagonist'
    'antagonist'

    """
    if not isinstance(character_data, str):
        raise TypeError("Input must be a string")
    
    if not character_data or not character_data.strip():
        raise ValueError("Input string is invalid or missing required information")
    
    parts = [part.strip().lower() for part in character_data.split(',')]
    
    if len(parts) < 3:
        raise ValueError("Input string is invalid or missing required information")
    
    traits = parts[2:]
    
    protagonist_traits = {'brave', 'heroic', 'loyal', 'determined', 'strong', 'courageous', 'noble'}
    antagonist_traits = {'mean', 'evil', 'cruel', 'stubborn', 'ruthless', 'wicked', 'malicious'}
    sidekick_traits = {'sweet', 'naive', 'helpful', 'supportive', 'friendly', 'loyal', 'kind'}
    
    protagonist_score = sum(1 for trait in traits if trait in protagonist_traits)
    antagonist_score = sum(1 for trait in traits if trait in antagonist_traits)
    sidekick_score = sum(1 for trait in traits if trait in sidekick_traits)
    
    if antagonist_score > 0 and antagonist_score >= protagonist_score and antagonist_score >= sidekick_score:
        return 'antagonist'
    elif protagonist_score > 0 and protagonist_score >= sidekick_score:
        return 'protagonist'
    elif sidekick_score > 0:
        return 'sidekick'
    else:
        return 'protagonist'