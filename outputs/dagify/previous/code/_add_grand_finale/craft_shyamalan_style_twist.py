import re


def craft_shyamalan_style_twist(twist_opportunities: str, existing_content: str) -> str:
    """
    Generates a twist in the style of M. Night Shyamalan based on narrative
    structure and chapter content.

    Parameters
    ----------
    twist_opportunities : str
        Input parameter for identifying narrative twist opportunities.
    existing_content : str
        Input parameter for incorporating existing chapter content into the
        twist.

    Returns
    -------
    str
        The crafted M. Night Shyamalan-style twist and input parameters
        (twist_opportunities and existing_content).

    Raises
    ------
    ValueError
        When input validation fails.
    TypeError
        When input types are incorrect.

    Examples
    --------
    >>> twist_opportunities = 'example narrative twist opportunities'
    >>> existing_content = 'existing chapter content'
    >>> output = craft_shyamalan_style_twist(twist_opportunities,
    existing_content)
    Example narrative twist (crafted based on input parameters)

    >>> twist_opportunities = 'another narrative twist opportunities'
    >>> existing_content = 'another chapter content'
    >>> output = craft_shyamalan_style_twist(twist_opportunities,
    existing_content)
    Another narrative twist (crafted based on input parameters)

    """
    if not isinstance(twist_opportunities, str):
        raise TypeError("twist_opportunities must be a string")
    if not isinstance(existing_content, str):
        raise TypeError("existing_content must be a string")
    
    if not twist_opportunities.strip():
        raise ValueError("twist_opportunities cannot be empty")
    if not existing_content.strip():
        raise ValueError("existing_content cannot be empty")
    
    
    characters = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', existing_content)
    locations = re.findall(r'\b(?:at|in|near)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b', existing_content)
    
    twist_templates = [
        "The {character} you've been following was actually {revelation} all along. The signs were there: {clues}.",
        "What seemed like {surface_reality} was actually {hidden_truth}. Every {element} was a carefully placed clue.",
        "The {location} isn't what it appears to be. {character} has been {twist_reveal} since the beginning.",
        "The supernatural events weren't supernatural at all - {character} has been {psychological_twist} the entire time.",
        "Everyone in {location} shares {shared_secret}. {character} is the only one who doesn't know {revelation}."
    ]
    
    opportunity_words = twist_opportunities.lower().split()
    
    if any(word in opportunity_words for word in ['death', 'dead', 'ghost', 'spirit']):
        twist_type = "supernatural"
    elif any(word in opportunity_words for word in ['memory', 'forget', 'remember', 'past']):
        twist_type = "psychological"
    elif any(word in opportunity_words for word in ['identity', 'who', 'secret', 'hidden']):
        twist_type = "identity"
    else:
        twist_type = "reality"
    
    if twist_type == "supernatural":
        character = characters[0] if characters else "the protagonist"
        twist = f"The {character} you've been following was actually dead all along. The signs were there: the way others barely acknowledged them, the lack of physical interaction, the selective memory of events. {existing_content[:100]}... was all experienced from beyond the veil."
    
    elif twist_type == "psychological":
        character = characters[0] if characters else "the main character"
        twist = f"What seemed like multiple personalities was actually {character} experiencing dissociative episodes. Every 'other person' was a carefully constructed aspect of their fractured psyche. The {twist_opportunities} were manifestations of repressed trauma."
    
    elif twist_type == "identity":
        character = characters[0] if characters else "the narrator"
        location = locations[0] if locations else "this place"
        twist = f"Everyone in {location} shares the same terrible secret. {character} is the only one who doesn't know they are {twist_opportunities}. The seemingly random events in the existing content were actually coordinated attempts to protect this truth."
    
    else:  # reality twist
        twist = f"The supernatural events weren't supernatural at all - what appeared to be {twist_opportunities} was actually an elaborate psychological experiment. Every detail in '{existing_content[:50]}...' was carefully orchestrated to test human perception and belief."
    
    twist += f" The truth was hidden in plain sight, woven through every interaction and every seemingly innocent detail of the narrative."
    
    return twist