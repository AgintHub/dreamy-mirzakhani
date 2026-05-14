from ._generate_story_setting.parse_general_input import parse_general_input
from ._generate_story_setting.extract_or_generate_location import extract_or_generate_location
from ._generate_story_setting.extract_or_generate_time_period import extract_or_generate_time_period
from ._generate_story_setting.extract_or_generate_environmental_details import extract_or_generate_environmental_details
from ._generate_story_setting.extract_or_generate_favorite_color import extract_or_generate_favorite_color
from ._generate_story_setting.validate_story_setting_components import validate_story_setting_components

from ._generate_story_setting.parse_general_input import parse_general_input
from ._generate_story_setting.extract_or_generate_location import extract_or_generate_location
from ._generate_story_setting.extract_or_generate_time_period import extract_or_generate_time_period
from ._generate_story_setting.extract_or_generate_environmental_details import extract_or_generate_environmental_details
from ._generate_story_setting.extract_or_generate_favorite_color import extract_or_generate_favorite_color
from ._generate_story_setting.validate_story_setting_components import validate_story_setting_components

from pydantic import BaseModel, Field


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


def generate_story_setting(general_input: str, **kwargs) -> GenerateStorySettingOutput:
    """
    Generate a story setting based on the input parameters.

    Parameters
    ----------
    location : str
        The geographic place where the story unfolds.
    time_period : str
        The historical or temporal setting of the narrative.
    environmental_details : str
        Key environmental factors—weather, terrain, societal norms—that
        influence the dog’s adventure.
    favorite_color : str
        A color favored by the protagonist, offering insight into
        personality or thematic symbolism.

    Returns
    -------
    [str, str, str, str]
        A list of strings representing the location, time period,
        environmental details, and favorite color.

    Raises
    ------
    TypeError
        If any of the input parameters are not of the correct type.

    Examples
    --------
    >>> location = 'New York City'
    >>> time_period = '1980s'
    >>> environmental_details = 'cold weather, urban terrain, hipster society'
    >>> favorite_color = 'blue'
    ['New York City', '1980s', 'cold weather, urban terrain, hipster society',
    'blue']

    """
    parsed_input: dict = parse_general_input(input_text=general_input)
    
    location: str = extract_or_generate_location(parsed_data=parsed_input, fallback_input=general_input)
    time_period: str = extract_or_generate_time_period(parsed_data=parsed_input, fallback_input=general_input)
    environmental_details: str = extract_or_generate_environmental_details(parsed_data=parsed_input, location=location, time_period=time_period)
    favorite_color: str = extract_or_generate_favorite_color(parsed_data=parsed_input, fallback_input=general_input)
    
    validated_setting: dict = validate_story_setting_components(location=location, time_period=time_period, environmental_details=environmental_details, favorite_color=favorite_color)
    
    return GenerateStorySettingOutput(
        location=validated_setting["location"],
        time_period=validated_setting["time_period"],
        environmental_details=validated_setting["environmental_details"],
        favorite_color=validated_setting["favorite_color"]
    )