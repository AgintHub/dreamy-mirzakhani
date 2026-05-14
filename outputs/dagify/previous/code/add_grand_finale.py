from ._add_grand_finale.analyze_narrative_structure import analyze_narrative_structure
from ._add_grand_finale.identify_twist_opportunities import identify_twist_opportunities
from ._add_grand_finale.craft_shyamalan_style_twist import craft_shyamalan_style_twist
from ._add_grand_finale.enhance_emotional_depth import enhance_emotional_depth
from ._add_grand_finale.integrate_thematic_symbolism import integrate_thematic_symbolism
from ._add_grand_finale.polish_narrative_coherence import polish_narrative_coherence

from ._add_grand_finale.analyze_narrative_structure import analyze_narrative_structure
from ._add_grand_finale.identify_twist_opportunities import identify_twist_opportunities
from ._add_grand_finale.craft_shyamalan_style_twist import craft_shyamalan_style_twist
from ._add_grand_finale.enhance_emotional_depth import enhance_emotional_depth
from ._add_grand_finale.integrate_thematic_symbolism import integrate_thematic_symbolism
from ._add_grand_finale.polish_narrative_coherence import polish_narrative_coherence

from pydantic import BaseModel, Field


class WriteChapter3Output(BaseModel):
    """Pydantic model for write_chapter_3 node outputs."""
    chapter_title: str = Field(..., description="The title of Chapter 3.")
    chapter_content: str = (
        Field(..., description="The prose content of Chapter 3.")
    )
    chapter_summary: str = (
        Field(..., description="A summary of what happens in Chapter 3.")
    )


class AddGrandFinaleOutput(BaseModel):
    """Pydantic model for add_grand_finale node outputs."""
    final_chapter_text: str = (
        Field(..., description = (
            "The polished, finalized Chapter 3 text incorporating the M. Night Shyamalan-style twist, emotional depth, and thematic symbolism.")
        )
    )


def add_grand_finale(write_chapter_3_input: WriteChapter3Output, **kwargs) -> AddGrandFinaleOutput:
    """
    Adds a grand finale twist to Chapter 3, maintaining narrative coherence
    while surprising the reader.

    Returns
    -------
    str
        The revised final chapter with the grand finale twist and emotional
        resonance fully integrated.

    Examples
    --------
    >>> create_grand_finale_twist('write_chapter_3')
    The grand finale twist is crafted, enriching the narrative and deepening
    character connections.

    >>> create_grand_finale_twist('write_chapter_3')
    The emotional resonance of the twist enhances character psychology and
    thematic symbolism.

    """
    analyzed_narrative: dict = analyze_narrative_structure(content=write_chapter_3_input.chapter_content, summary=write_chapter_3_input.chapter_summary)
    twist_elements: dict = identify_twist_opportunities(narrative_data=analyzed_narrative, chapter_content=write_chapter_3_input.chapter_content)
    crafted_twist: str = craft_shyamalan_style_twist(twist_opportunities=twist_elements, existing_content=write_chapter_3_input.chapter_content)
    enhanced_emotions: str = enhance_emotional_depth(content=crafted_twist, character_connections=analyzed_narrative)
    thematic_integration: str = integrate_thematic_symbolism(content=enhanced_emotions, narrative_themes=analyzed_narrative)
    polished_finale: str = polish_narrative_coherence(content=thematic_integration, original_summary=write_chapter_3_input.chapter_summary)
    return AddGrandFinaleOutput(
        final_chapter_text=polished_finale,
    )