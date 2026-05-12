from ._write_chapter_1.validate_inputs import validate_inputs
from ._write_chapter_1.create_chapter_structure import create_chapter_structure
from ._write_chapter_1.extract_character_context import extract_character_context
from ._write_chapter_1.extract_setting_context import extract_setting_context
from ._write_chapter_1.integrate_color_themes import integrate_color_themes
from ._write_chapter_1.craft_opening_scene import craft_opening_scene
from ._write_chapter_1.develop_chapter_events import develop_chapter_events
from ._write_chapter_1.weave_chapter_prose import weave_chapter_prose
from ._write_chapter_1.validate_chapter_output import validate_chapter_output

from ._write_chapter_1.validate_inputs import validate_inputs
from ._write_chapter_1.create_chapter_structure import create_chapter_structure
from ._write_chapter_1.extract_character_context import extract_character_context
from ._write_chapter_1.extract_setting_context import extract_setting_context
from ._write_chapter_1.integrate_color_themes import integrate_color_themes
from ._write_chapter_1.craft_opening_scene import craft_opening_scene
from ._write_chapter_1.develop_chapter_events import develop_chapter_events
from ._write_chapter_1.weave_chapter_prose import weave_chapter_prose
from ._write_chapter_1.validate_chapter_output import validate_chapter_output

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
        Field(..., description = (
            "The dog\u2019s favorite color, reflecting its personality.")
        )
    )


class GenerateCharacterProfilesOutput(BaseModel):
    """Pydantic model for generate_character_profiles node outputs."""
    character_name: str = (
        Field(..., description="The character\u2019s full name.")
    )
    age: float = (
        Field(..., description = (
            "The character\u2019s age in years, if applicable.")
        )
    )
    personality_traits: str = (
        Field(..., description="A concise list of defining personality traits.")
    )
    role_in_plot: str = (
        Field(..., description = (
            "The character\u2019s functional role within the story.")
        )
    )
    favorite_color: str = (
        Field(..., description = (
            "A color that encapsulates the character\u2019s essence or aesthetic.")
        )
    )
    dog_profile: List[str] = (
        Field(..., description = (
            "A series of sentences detailing the dog\u2019s breed, background, quirks, and motivations.")
        )
    )


class GenerateStorySettingOutput(BaseModel):
    """Pydantic model for generate_story_setting node outputs."""
    location: str = (
        Field(..., description="The geographic place where the story unfolds.")
    )
    time_period: str = (
        Field(..., description = (
            "The historical or temporal setting of the narrative.")
        )
    )
    environmental_details: str = (
        Field(..., description = (
            "Key environmental factors\u2014weather, terrain, societal norms\u2014that influence the dog\u2019s adventure.")
        )
    )
    favorite_color: str = (
        Field(..., description = (
            "A color favored by the protagonist, offering insight into personality or thematic symbolism.")
        )
    )


class WriteChapter1Output(BaseModel):
    """Pydantic model for write_chapter_1 node outputs."""
    chapter_text: str = (
        Field(..., description = (
            "The complete, prose-formatted text of Chapter 1")
        )
    )
    valid_output: bool = (
        Field(..., description = (
            "True if the output is a well-formed, non-empty chapter; otherwise False")
        )
    )


def write_chapter_1(generate_story_outline_input: GenerateStoryOutlineOutput, generate_character_profiles_input: GenerateCharacterProfilesOutput, generate_story_setting_input: GenerateStorySettingOutput, **kwargs) -> WriteChapter1Output:
    """
    Crafts the opening chapter of a story by weaving together the provided story
    outline, character profiles with their favorite colors, and environmental
    context.

    Parameters
    ----------
    story_outline : dict
        The concise story outline for the narrative.
    character_profiles : list
        A list of richly detailed character biographies.
    story_setting : dict
        The comprehensive story setting including the geographic locale,
        temporal context, environmental conditions, and a favorite color
        that reflects character traits or thematic undercurrents.

    Returns
    -------
    dict
        {'chapter_text': 'The complete, prose-formatted text of Chapter 1',
        'valid_output': True/False}

    Raises
    ------
    ValueError
        If the input story outline, character profiles, or story setting is
        invalid or missing.

    Examples
    --------
    >>> story_outline = {'title': 'Story Title', 'chapter_titles': ['Chapter 1',
    'Chapter 2'], 'event_bullet_points': ['Point 1', 'Point 2', 'Point 3']}
    >>> character_profiles = [{'name': 'John', 'age': 30, 'personality_traits':
    'friendly', 'role_in_plot': 'protagonist', 'favorite_color': 'red'}]
    >>> story_setting = {'location': 'Park', 'time_period': 'Now',
    'environmental_details': 'sunny', 'favorite_color': 'blue'}
    >>> write_chapter_1(story_outline, character_profiles, story_setting)
    {'chapter_text': 'The complete, prose-formatted text of Chapter 1',
    'valid_output': True}

    """
    validate_inputs(story_outline=generate_story_outline_input, character_profiles=generate_character_profiles_input, story_setting=generate_story_setting_input)
    
    narrative_structure: dict = create_chapter_structure(chapter_bullet_points=generate_story_outline_input.chapter_1_bullet_points, story_title=generate_story_outline_input.title)
    
    character_context: dict = extract_character_context(character_profile=generate_character_profiles_input)
    
    setting_context: dict = extract_setting_context(story_setting=generate_story_setting_input)
    
    color_themes: dict = integrate_color_themes(outline_color=generate_story_outline_input.favorite_color, character_color=generate_character_profiles_input.favorite_color, setting_color=generate_story_setting_input.favorite_color)
    
    opening_scene: str = craft_opening_scene(character_context=character_context, setting_context=setting_context, color_themes=color_themes)
    
    chapter_body: str = develop_chapter_events(bullet_points=generate_story_outline_input.chapter_1_bullet_points, character_context=character_context, setting_context=setting_context)
    
    complete_chapter: str = weave_chapter_prose(opening_scene=opening_scene, chapter_body=chapter_body, color_themes=color_themes)
    
    is_valid: bool = validate_chapter_output(chapter_text=complete_chapter)
    
    return WriteChapter1Output(chapter_text=complete_chapter, valid_output=is_valid)