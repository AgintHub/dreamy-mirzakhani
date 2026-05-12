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
        Field(..., description="The polished, finalized Chapter 3 text incorporating the M. Night Shyamalan-style twist, emotional depth, and thematic symbolism.")
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
    return AddGrandFinaleOutput(
        final_chapter_text="",
    )