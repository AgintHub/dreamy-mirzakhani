def design_ui_components(app_context: str) -> str:
    """
    Creates a string listing UI components required for the specified app
    context.

    Parameters
    ----------
    app_context : str
        A string identifier or description of the application context for
        which UI components should be designed.

    Returns
    -------
    str
        A formatted string enumerating UI components, each separated by
        commas or newlines.

    Raises
    ------
    ValueError
        Raised when the shim cannot determine any UI components for the
        given context.
    TypeError
        Raised when app_context is not a string.

    Examples
    --------
    >>> components = design_ui_components(app_context='music_identifier')
    buttons, forms, navigation bar, search field

    >>> components = design_ui_components(app_context='ecommerce')
    product cards, filter panel, shopping cart icon, checkout form

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")