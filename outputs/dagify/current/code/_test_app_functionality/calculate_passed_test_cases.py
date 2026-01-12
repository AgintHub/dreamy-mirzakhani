def calculate_passed_test_cases(unit_results: str, integration_results: str, ui_results: str) -> int:
    """
    Calculates the total number of passed test cases from various test results.

    Parameters
    ----------
    unit_results : str
        A string representing the results of unit tests, potentially
        containing pass/fail information.
    integration_results : str
        A string representing the results of integration tests, potentially
        containing pass/fail information.
    ui_results : str
        A string representing the results of UI tests, potentially
        containing pass/fail information.

    Returns
    -------
    int
        The total number of test cases that passed across all provided test
        results.

    Raises
    ------
    ValueError
        If any of the input test results are not in the expected format or
        contain invalid data.
    TypeError
        If the input parameters are not of the expected type (str).

    Examples
    --------
    >>> calculate_passed_test_cases(unit_results='10 passed, 2 failed',
    integration_results='8 passed, 1 failed', ui_results='5 passed, 0 failed')
    23

    >>> calculate_passed_test_cases(unit_results='5 passed, 0 failed',
    integration_results='3 passed, 2 failed', ui_results='2 passed, 1 failed')
    10

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")