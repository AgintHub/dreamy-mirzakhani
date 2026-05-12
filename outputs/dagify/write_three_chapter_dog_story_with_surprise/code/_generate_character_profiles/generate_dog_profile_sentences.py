from typing import List


def generate_dog_profile_sentences(dog_data: str) -> List[str]:
    """
    Generate a list of sentences describing a dog's breed, background, quirks,
    and motivations.

    Parameters
    ----------
    dog_data : str
        Input parameter containing dog information to be used for generating
        profile sentences.

    Returns
    -------
    List[str]
        A list of sentences detailing the dog's characteristics.

    Raises
    ------
    TypeError
        When the input data is not a string.
    ValueError
        When the input data is empty or invalid.

    Examples
    --------
    >>> dog_data = 'Breed: Labrador, Age: 3, Personality: Friendly'
    [Breed: Labrador, Age: 3, Personality: Friendly]

    >>> dog_data = 'Breed: Golden Retriever, Age: 5, Personality: Loyal'
    [Breed: Golden Retriever, Age: 5, Personality: Loyal]

    """
    if not isinstance(dog_data, str):
        raise TypeError("Input data must be a string")
    
    if not dog_data or not dog_data.strip():
        raise ValueError("Input data cannot be empty")
    
    
    dog_data = dog_data.strip()
    
    pairs = []
    parts = dog_data.split(',')
    
    parsed_data = {}
    for part in parts:
        part = part.strip()
        if ':' in part:
            key, value = part.split(':', 1)
            parsed_data[key.strip().lower()] = value.strip()
    
    if not parsed_data:
        raise ValueError("Input data is invalid - no recognizable key-value pairs found")
    
    sentences = []
    
    if 'breed' in parsed_data:
        sentences.append(f"This dog is a {parsed_data['breed']}.")
    
    if 'age' in parsed_data:
        sentences.append(f"The dog is {parsed_data['age']} years old.")
    
    if 'personality' in parsed_data:
        sentences.append(f"This dog has a {parsed_data['personality'].lower()} personality.")
    
    for key, value in parsed_data.items():
        if key not in ['breed', 'age', 'personality']:
            sentences.append(f"The dog's {key} is {value}.")
    
    return sentences