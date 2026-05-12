import re


def extract_or_generate_environmental_details(parsed_data: str, location: str, time_period: str) -> str:
    """
    Extracts or generates environmental details from input data. If data lacks
    sufficient information, the function will attempt to generate the missing
    details.

    Parameters
    ----------
    parsed_data : str
        String of input data to be processed, including story setting
        information.
    location : str
        Geographical place where the story unfolds, used if missing from
        parsed_data.
    time_period : str
        Timeframe or temporal setting of the narrative, used if missing from
        parsed_data.

    Returns
    -------
    str
        A formatted string containing the extracted environmental details,
        including location and time period, along with relevant narrative
        context.

    Raises
    ------
    ValueError
        Raised if the input data fails validation or lacks sufficient
        information to generate environmental details.

    Examples
    --------
    >>> extract_or_generate_environmental_details(parsed_data='data containing
    environmental details', location='fallback_location',
    time_period='fallback_time_period')
    Formated string with environmental details ('location', 'time period') and
    relevant narrative context.

    >>> extract_or_generate_environmental_details(parsed_data='data lacking
    environmental details', location='location_example',
    time_period='time_period_example')
    Formated string with generated environmental details ('location', 'time
    period') and relevant narrative context.

    """
    
    if not parsed_data or not isinstance(parsed_data, str):
        raise ValueError("Input data fails validation or lacks sufficient information to generate environmental details.")
    
    extracted_location = None
    extracted_time_period = None
    
    location_patterns = [
        r'(?i)(?:location|place|setting|city|town|country)\s*:?\s*([^\n,.;]+)',
        r'(?i)(?:in|at|near)\s+([A-Z][a-zA-Z\s]+(?:City|Town|Village|State|Country)?)'
    ]
    
    for pattern in location_patterns:
        match = re.search(pattern, parsed_data)
        if match:
            extracted_location = match.group(1).strip()
            break
    
    time_patterns = [
        r'(?i)(?:time|period|era|year|century|decade)\s*:?\s*([^\n,.;]+)',
        r'(?i)(?:during|in)\s+(\d{4}|\d{1,2}(?:st|nd|rd|th)\s+century|medieval|ancient|modern|contemporary|[^\n,.;]+\s+(?:era|period|age))'
    ]
    
    for pattern in time_patterns:
        match = re.search(pattern, parsed_data)
        if match:
            extracted_time_period = match.group(1).strip()
            break
    
    final_location = extracted_location if extracted_location else location
    final_time_period = extracted_time_period if extracted_time_period else time_period
    
    if not final_location or not final_time_period:
        raise ValueError("Input data fails validation or lacks sufficient information to generate environmental details.")
    
    environmental_details = f"Environmental Setting: The story unfolds in {final_location} during {final_time_period}. This setting provides the backdrop for the narrative, influencing the characters' experiences and the overall atmosphere of the story. The geographical location of {final_location} and the temporal context of {final_time_period} together create a unique environmental framework that shapes the storytelling elements."
    
    return environmental_details