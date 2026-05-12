from pydantic import BaseModel, Field
from typing import List


class WriteChapter1Output(BaseModel):
    """Pydantic model for write_chapter_1 node outputs."""
    chapter_text: str = (
        Field(..., description="The complete, prose-formatted text of Chapter 1")
    )
    valid_output: bool = (
        Field(..., description="True if the output is a well-formed, non-empty chapter; otherwise False")
    )


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


class GenerateCharacterProfilesOutput(BaseModel):
    """Pydantic model for generate_character_profiles node outputs."""
    character_name: str = (
        Field(..., description="The character\u2019s full name.")
    )
    age: float = (
        Field(..., description="The character\u2019s age in years, if applicable.")
    )
    personality_traits: str = (
        Field(..., description="A concise list of defining personality traits.")
    )
    role_in_plot: str = (
        Field(..., description="The character\u2019s functional role within the story.")
    )
    favorite_color: str = (
        Field(..., description="A color that encapsulates the character\u2019s essence or aesthetic.")
    )
    dog_profile: List[str] = (
        Field(..., description="A series of sentences detailing the dog\u2019s breed, background, quirks, and motivations.")
    )


class GenerateStorySettingOutput(BaseModel):
    """Pydantic model for generate_story_setting node outputs."""
    location: str = (
        Field(..., description="The geographic place where the story unfolds.")
    )
    time_period: str = (
        Field(..., description="The historical or temporal setting of the narrative.")
    )
    environmental_details: str = (
        Field(..., description="Key environmental factors\u2014weather, terrain, societal norms\u2014that influence the dog\u2019s adventure.")
    )
    favorite_color: str = (
        Field(..., description="A color favored by the protagonist, offering insight into personality or thematic symbolism.")
    )


class WriteChapter2Output(BaseModel):
    """Pydantic model for write_chapter_2 node outputs."""
    chapter_2_output: str = (
        Field(..., description="The complete Chapter 2 text in prose.")
    )


def write_chapter_2(write_chapter_1_input: WriteChapter1Output, generate_story_outline_input: GenerateStoryOutlineOutput, generate_character_profiles_input: GenerateCharacterProfilesOutput, generate_story_setting_input: GenerateStorySettingOutput, **kwargs) -> WriteChapter2Output:
    """
    Writes Chapter 2 using the provided inputs.

    Parameters
    ----------
    chapter_1_output : str
        The text of the first chapter, used as a basis for the second
        chapter's writing.
    outline : dict
        A structured dictionary containing the story outline, including
        title, chapter titles, event bullet points, and the dog's favorite
        color.
    character_profiles : dict
        A dictionary containing the richly detailed character biographies,
        including each character's name, age, personality traits, plot role,
        and favorite color.
    story_setting : dict
        A dictionary describing the rich, immersive setting of the
        narrative, including geographic locale, temporal context,
        environmental conditions, and the protagonist's favorite color.

    Returns
    -------
    str
        The complete text of Chapter 2.

    Raises
    ------
    ValueError
        If any of the input parameters are missing or invalid.

    Examples
    --------
    >>> write_chapter_2(chapter_1_output='<text>', outline={'title': 'The
    Story', 'chapter_titles': ['Chapter 1', 'Chapter 2', 'Chapter 3']},
    character_profiles={'dog': {'name': 'Max', 'age': 2, 'personality_traits':
    'Friendly', 'role_in_plot': 'Protagonist', 'favorite_color': 'Blue'}},
    story_setting={'location': 'Beach', 'time_period': 'Summer',
    'environmental_details': 'Sunny', 'favorite_color': 'Red'})
    <text of Chapter 2>

    >>> write_chapter_2(chapter_1_output='<text>', outline={'title': 'The
    Story', 'chapter_titles': ['Chapter 1', 'Chapter 2', 'Chapter 3']},
    character_profiles={'dog': {'name': 'Max', 'age': 2, 'personality_traits':
    'Friendly', 'role_in_plot': 'Protagonist', 'favorite_color': 'Blue'}},
    story_setting={'location': 'Forest', 'time_period': 'Fall',
    'environmental_details': 'Rainy', 'favorite_color': 'Green'})
    <text of Chapter 2>

    """
    return WriteChapter2Output(
        chapter_2_output="",
    )