from ._generate_character_profiles.extract_character_profiles_from_input import extract_character_profiles_from_input
from ._generate_character_profiles.validate_character_profiles_input import validate_character_profiles_input
from ._generate_character_profiles.identify_main_character import identify_main_character
from ._generate_character_profiles.extract_character_name import extract_character_name
from ._generate_character_profiles.determine_character_age import determine_character_age
from ._generate_character_profiles.generate_personality_traits import generate_personality_traits
from ._generate_character_profiles.determine_plot_role import determine_plot_role
from ._generate_character_profiles.assign_favorite_color import assign_favorite_color
from ._generate_character_profiles.extract_dog_information import extract_dog_information
from ._generate_character_profiles.generate_dog_profile_sentences import generate_dog_profile_sentences

from ._generate_character_profiles.extract_character_profiles_from_input import extract_character_profiles_from_input
from ._generate_character_profiles.validate_character_profiles_input import validate_character_profiles_input
from ._generate_character_profiles.identify_main_character import identify_main_character
from ._generate_character_profiles.extract_character_name import extract_character_name
from ._generate_character_profiles.determine_character_age import determine_character_age
from ._generate_character_profiles.generate_personality_traits import generate_personality_traits
from ._generate_character_profiles.determine_plot_role import determine_plot_role
from ._generate_character_profiles.assign_favorite_color import assign_favorite_color
from ._generate_character_profiles.extract_dog_information import extract_dog_information
from ._generate_character_profiles.generate_dog_profile_sentences import generate_dog_profile_sentences

from pydantic import BaseModel, Field
from typing import List


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
    character_profiles: List[dict] = extract_character_profiles_from_input(input_data=general_input, kwargs=kwargs)
    validate_character_profiles_input(character_profiles=character_profiles)
    
    main_character: dict = identify_main_character(character_profiles=character_profiles)
    character_name: str = extract_character_name(character_data=main_character)
    character_age: float = determine_character_age(character_data=main_character)
    personality_traits: str = generate_personality_traits(character_data=main_character)
    role_in_plot: str = determine_plot_role(character_data=main_character)
    favorite_color: str = assign_favorite_color(character_data=main_character)
    
    dog_data: dict = extract_dog_information(character_profiles=character_profiles)
    dog_profile: List[str] = generate_dog_profile_sentences(dog_data=dog_data)
    
    return GenerateCharacterProfilesOutput(
        character_name=character_name,
        age=character_age,
        personality_traits=personality_traits,
        role_in_plot=role_in_plot,
        favorite_color=favorite_color,
        dog_profile=dog_profile
    )