from pydantic import BaseModel, Field
from typing import List


class GenerateStoryOutlineOutput(BaseModel):
    """Pydantic model for generate_story_outline node outputs."""
    title: str = Field(..., description="Title of the story.")
    chapter_titles: List[str] = (
        Field(..., description="List of chapter titles.")
    )
    chapter_1_bullet_points: List[str] = (
        Field(..., description="Three bullet points summarizing Chapter 1.")
    )
    chapter_2_bullet_points: List[str] = (
        Field(..., description="Three bullet points summarizing Chapter 2.")
    )
    chapter_3_bullet_points: List[str] = (
        Field(..., description="Three bullet points summarizing Chapter 3.")
    )
    favorite_color: str = (
        Field(..., description="The dog\u2019s favorite color, reflecting its personality.")
    )


def generate_story_outline(general_input: str, **kwargs) -> GenerateStoryOutlineOutput:
    """
    Generates a three-chapter outline for a dog story.

    Parameters
    ----------
    prompt : str
        A prompt for the story outline.

    Returns
    -------
    dict
        A dictionary with story outline details.

    Raises
    ------
    Exception
        If the prompt is invalid.

    Examples
    --------
    >>> generate_story_outline(prompt='A heartwarming dog story')
    >>> output = {'title': 'The Adventures of Buddy', 'chapter_titles':
    ['Chapter 1: Introduction', 'Chapter 2: The Journey', 'Chapter 3: The
    Return'], 'chapter_1_bullet_points': ['Buddy meets a new friend', 'Buddy
    goes on an adventure', 'Buddy returns home'], 'chapter_2_bullet_points':
    ['Buddy faces a challenge', 'Buddy finds a treasure', 'Buddy makes a new
    friend'], 'chapter_3_bullet_points': ['Buddy concludes his journey', 'Buddy
    says goodbye to friends', 'Buddy returns home happy'], 'favorite_color':
    'Blue'}
    {'title': 'The Adventures of Buddy', 'chapter_titles': ['Chapter 1:
    Introduction', 'Chapter 2: The Journey', 'Chapter 3: The Return'],
    'chapter_1_bullet_points': ['Buddy meets a new friend', 'Buddy goes on an
    adventure', 'Buddy returns home'], 'chapter_2_bullet_points': ['Buddy faces
    a challenge', 'Buddy finds a treasure', 'Buddy makes a new friend'],
    'chapter_3_bullet_points': ['Buddy concludes his journey', 'Buddy says
    goodbye to friends', 'Buddy returns home happy'], 'favorite_color': 'Blue'}

    >>> generate_story_outline(prompt='A dog story with a mystery')
    >>> output = {'title': 'The Mystery of the Missing Treats',
    'chapter_titles': ['Chapter 1: The Mysterious Scene', 'Chapter 2: The
    Investigation', 'Chapter 3: The Suspect Revealed'],
    'chapter_1_bullet_points': ['A treat goes missing', 'The scene is
    established', 'Clues are revealed'], 'chapter_2_bullet_points': ['The
    investigation begins', 'More clues are found', 'The plot thickens'],
    'chapter_3_bullet_points': ['The suspect is revealed', 'The mystery is
    solved', 'The dog returns home'], 'favorite_color': 'Red'}
    {'title': 'The Mystery of the Missing Treats', 'chapter_titles': ['Chapter
    1: The Mysterious Scene', 'Chapter 2: The Investigation', 'Chapter 3: The
    Suspect Revealed'], 'chapter_1_bullet_points': ['A treat goes missing', 'The
    scene is established', 'Clues are revealed'], 'chapter_2_bullet_points':
    ['The investigation begins', 'More clues are found', 'The plot thickens'],
    'chapter_3_bullet_points': ['The suspect is revealed', 'The mystery is
    solved', 'The dog returns home'], 'favorite_color': 'Red'}

    """
    return GenerateStoryOutlineOutput(
        title="",
        chapter_titles=[],
        chapter_1_bullet_points=[],
        chapter_2_bullet_points=[],
        chapter_3_bullet_points=[],
        favorite_color="",
    )