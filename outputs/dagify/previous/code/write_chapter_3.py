from ._write_chapter_3.validate_chapter_2_input import validate_chapter_2_input
from ._write_chapter_3.generate_chapter_title import generate_chapter_title
from ._write_chapter_3.prepare_story_context import prepare_story_context
from ._write_chapter_3.craft_final_chapter_content import craft_final_chapter_content
from ._write_chapter_3.generate_chapter_summary import generate_chapter_summary

from ._write_chapter_3.validate_chapter_2_input import validate_chapter_2_input
from ._write_chapter_3.generate_chapter_title import generate_chapter_title
from ._write_chapter_3.prepare_story_context import prepare_story_context
from ._write_chapter_3.craft_final_chapter_content import craft_final_chapter_content
from ._write_chapter_3.generate_chapter_summary import generate_chapter_summary

from pydantic import BaseModel, Field
from typing import List


class WriteChapter2Output(BaseModel):
    """Pydantic model for write_chapter_2 node outputs."""
    chapter_2_output: str = (
        Field(..., description="The complete Chapter 2 text in prose.")
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


class WriteChapter3Output(BaseModel):
    """Pydantic model for write_chapter_3 node outputs."""
    chapter_title: str = Field(..., description="The title of Chapter 3.")
    chapter_content: str = (
        Field(..., description="The prose content of Chapter 3.")
    )
    chapter_summary: str = (
        Field(..., description="A summary of what happens in Chapter 3.")
    )


def write_chapter_3(write_chapter_2_input: WriteChapter2Output, generate_story_outline_input: GenerateStoryOutlineOutput, generate_character_profiles_input: GenerateCharacterProfilesOutput, generate_story_setting_input: GenerateStorySettingOutput, **kwargs) -> WriteChapter3Output:
    """
    Generates the final chapter of the story, using the provided outline,
    character profiles, and setting to conclude the dog's adventure.

    Parameters
    ----------
    chapter_2_output : str
        The complete text of Chapter 2.

    Returns
    -------
    dict[str, str]
        Contains the title, content, and summary of the final chapter.

    Raises
    ------
    TypeError
        If chapter_2_output is not a string.

    Examples
    --------
    >>> final_chapter = write_chapter_3(chapter_2_output)
    >>> print(final_chapter['chapter_title'])
    >>> print(final_chapter['chapter_content'])
    >>> print(final_chapter['chapter_summary'])
    Chapter Title: The Final Chapter
    Chapter Content: The final chapter of the story.
    Chapter Summary: The dog's adventure concludes with ​​.

    """
    validate_chapter_2_input(chapter_2_text=write_chapter_2_input.chapter_2_output)
    
    chapter_3_title: str = generate_chapter_title(
        outline_title=generate_story_outline_input.title,
        chapter_titles=generate_story_outline_input.chapter_titles
    )
    
    story_context: dict = prepare_story_context(
        chapter_2_content=write_chapter_2_input.chapter_2_output,
        outline=generate_story_outline_input,
        characters=generate_character_profiles_input,
        setting=generate_story_setting_input
    )
    
    chapter_3_content: str = craft_final_chapter_content(
        story_context=story_context,
        chapter_3_bullet_points=generate_story_outline_input.chapter_3_bullet_points,
        dog_profile=generate_character_profiles_input.dog_profile,
        setting_details=generate_story_setting_input
    )
    
    chapter_3_summary: str = generate_chapter_summary(
        chapter_content=chapter_3_content,
        bullet_points=generate_story_outline_input.chapter_3_bullet_points
    )
    
    return WriteChapter3Output(
        chapter_title=chapter_3_title,
        chapter_content=chapter_3_content,
        chapter_summary=chapter_3_summary
    )