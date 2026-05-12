from pydantic import BaseModel, Field
from typing import List


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


def generate_character_profiles(general_input: str, **kwargs) -> GenerateCharacterProfilesOutput:
    """
    Generate detailed character profiles.

    Parameters
    ----------
    character_profiles : List[dict]
        List of dictionaries containing character information for each
        person and the dog.

    Returns
    -------
    dict
        A dictionary containing the generated character profiles where each
        key is a character name and each value is a dictionary with their
        profile information.

    Raises
    ------
    TypeError
        If the input character_profiles is not a list of dictionaries.
    """
    return GenerateCharacterProfilesOutput(
        character_name="",
        age=0.0,
        personality_traits="",
        role_in_plot="",
        favorite_color="",
        dog_profile=[],
    )