from ._build_app_interface.create_wireframes_and_user_flows import create_wireframes_and_user_flows
from ._build_app_interface.generate_interface_design_document import generate_interface_design_document
from ._build_app_interface.define_responsive_breakpoints import define_responsive_breakpoints
from ._build_app_interface.implement_accessibility_features import implement_accessibility_features
from ._build_app_interface.apply_performance_optimizations import apply_performance_optimizations
from ._build_app_interface.design_ui_components import design_ui_components
from ._build_app_interface.validate_output_types import validate_output_types

from pydantic import BaseModel, Field


class BuildAppInterfaceOutput(BaseModel):
    """Pydantic model for build_app_interface node outputs."""
    interface_design_document: str = (
        Field(..., description = (
            "A detailed document outlining the design decisions, wireframes, and user flows for the application interface.")
        )
    )
    responsive_breakpoints: str = (
        Field(..., description = (
            "List of CSS breakpoints used to ensure a responsive design across various screen sizes and devices.")
        )
    )
    accessibility_features: str = (
        Field(..., description = (
            "List of accessibility features implemented, such as WCAG 2.1 guidelines compliance, screen reader support, and keyboard navigation.")
        )
    )
    performance_optimization_techniques: str = (
        Field(..., description = (
            "List of techniques used to optimize the performance of the application interface, such as code splitting, lazy loading, and caching.")
        )
    )
    ui_components: str = (
        Field(..., description = (
            "List of UI components used in the application, such as buttons, forms, and navigation elements.")
        )
    )


def build_app_interface(general_input: str, **kwargs) -> BuildAppInterfaceOutput:
    """
    Designs and implements a modern, responsive web or mobile interface for the
    music sample identifier application, ensuring cross-browser or cross-
    platform compatibility and optimizing for performance.

    Returns
    -------
    {interface_design_document: str, responsive_breakpoints: List[str], accessibility_features: List[str], performance_optimization_techniques: List[str], ui_components: List[str]}
        A dictionary containing the interface design document, responsive
        breakpoints, accessibility features, performance optimization
        techniques, and UI components used in the application interface.

    Raises
    ------
    ValueError
        If the interface design document is empty or not provided.
    TypeError
        If the output structure types do not match the expected types.

    Examples
    --------
    >>> interface_data = build_app_interface()
    >>> print(interface_data['interface_design_document'])
    >>> print(interface_data['responsive_breakpoints'])
    >>> print(interface_data['accessibility_features'])
    >>> print(interface_data['performance_optimization_techniques'])
    >>> print(interface_data['ui_components'])
    interface_design_document_content
    ['breakpoint1', 'breakpoint2']
    ['feature1', 'feature2']
    ['technique1', 'technique2']
    ['component1', 'component2']

    """
    wireframes: str = create_wireframes_and_user_flows(input_requirements=general_input)
    design_document: str = generate_interface_design_document(wireframes=wireframes, app_type="music_sample_identifier")
    
    if not design_document or design_document.strip() == "":
        raise ValueError("If the interface design document is empty or not provided.")
    
    breakpoints: str = define_responsive_breakpoints(target_devices=["mobile", "tablet", "desktop"])
    accessibility: str = implement_accessibility_features(guidelines="WCAG_2.1")
    optimization: str = apply_performance_optimizations(techniques=["code_splitting", "lazy_loading", "caching"])
    components: str = design_ui_components(app_context="music_identifier")
    
    validated_output: BuildAppInterfaceOutput = validate_output_types(
        design_doc=design_document,
        breakpoints=breakpoints,
        accessibility=accessibility,
        optimization=optimization,
        components=components
    )
    
    return BuildAppInterfaceOutput(
        interface_design_document=design_document,
        responsive_breakpoints=breakpoints,
        accessibility_features=accessibility,
        performance_optimization_techniques=optimization,
        ui_components=components
    )