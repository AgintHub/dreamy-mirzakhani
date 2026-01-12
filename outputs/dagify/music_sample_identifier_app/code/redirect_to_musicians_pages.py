from ._redirect_to_musicians_pages.validate_input_consistency import validate_input_consistency
from ._redirect_to_musicians_pages.check_for_duplicate_ids import check_for_duplicate_ids
from ._redirect_to_musicians_pages.extract_musician_metadata import extract_musician_metadata
from ._redirect_to_musicians_pages.nlp_url_resolution import nlp_url_resolution
from ._redirect_to_musicians_pages.ml_url_prediction import ml_url_prediction
from ._redirect_to_musicians_pages.hybrid_url_ranking import hybrid_url_ranking
from ._redirect_to_musicians_pages.verify_official_url import verify_official_url
from ._redirect_to_musicians_pages.format_exception_message import format_exception_message
from ._redirect_to_musicians_pages.determine_overall_success import determine_overall_success

from pydantic import BaseModel, Field
from typing import List


class ListMusiciansOutput(BaseModel):
    """Pydantic model for list_musicians node outputs."""
    musician_ids: List[str] = (
        Field(..., description="List of unique identifiers for the musicians")
    )
    musician_names: List[str] = (
        Field(..., description="List of names of the musicians")
    )
    musician_aliases: List[str] = (
        Field(..., description = (
            "List of lists containing aliases for each musician")
        )
    )
    is_deduplicated: bool = (
        Field(..., description = (
            "Whether the list of musicians has been deduplicated")
        )
    )


class RedirectToMusiciansPagesOutput(BaseModel):
    """Pydantic model for redirect_to_musicians_pages node outputs."""
    redirection_results: List[str] = (
        Field(..., description = (
            "List of URLs successfully redirected to the official pages of musicians")
        )
    )
    successful_redirections_count: int = (
        Field(..., description = (
            "Number of successful redirections to musician profiles")
        )
    )
    redirection_exceptions: List[str] = (
        Field(..., description = (
            "List of exceptions or errors encountered during the redirection process")
        )
    )
    is_redirection_successful: bool = (
        Field(..., description = (
            "Whether the redirection process was successful overall")
        )
    )


def redirect_to_musicians_pages(list_musicians_input: ListMusiciansOutput, **kwargs) -> RedirectToMusiciansPagesOutput:
    """
    Redirects to the official online presence of identified musicians using a
    hybrid NLP and machine learning approach.

    Parameters
    ----------
    musician_ids : List[str]
        List of unique identifiers for the musicians
    musician_names : List[str]
        List of names of the musicians
    musician_aliases : List[List[str]]
        List of lists containing aliases for each musician

    Returns
    -------
    Tuple[List[str], int, List[str], bool]
        A tuple containing the list of URLs successfully redirected, the
        number of successful redirections, a list of exceptions encountered,
        and a boolean indicating overall success.

    Raises
    ------
    ValueError
        If the input lists are of different lengths or if there are
        duplicate musician IDs.
    ConnectionError
        If there is a failure in DNS lookup or HTTP requests during URL
        resolution.

    Examples
    --------
    >>> musician_ids = ['123', '456']
    >>> musician_names = ['Artist1', 'Artist2']
    >>> musician_aliases = [['Alias1'], ['Alias2']]
    >>> redirect_to_musicians_pages(musician_ids, musician_names,
    musician_aliases)
    (['https://officialartist1.com', 'https://officialartist2.com'], 2, [],
    True)

    """
    validate_input_consistency(musician_ids=list_musicians_input.musician_ids, musician_names=list_musicians_input.musician_names, musician_aliases=list_musicians_input.musician_aliases)
    
    check_for_duplicate_ids(musician_ids=list_musicians_input.musician_ids)
    
    successful_urls: List[str] = []
    exceptions_list: List[str] = []
    
    for i in range(len(list_musicians_input.musician_ids)):
        try:
            musician_metadata: dict = extract_musician_metadata(musician_id=list_musicians_input.musician_ids[i], musician_name=list_musicians_input.musician_names[i], aliases=list_musicians_input.musician_aliases[i])
            
            nlp_candidates: List[str] = nlp_url_resolution(metadata=musician_metadata)
            
            ml_predictions: List[str] = ml_url_prediction(metadata=musician_metadata)
            
            hybrid_urls: List[str] = hybrid_url_ranking(nlp_candidates=nlp_candidates, ml_predictions=ml_predictions)
            
            verified_url: str = verify_official_url(candidate_urls=hybrid_urls, musician_metadata=musician_metadata)
            
            successful_urls.append(verified_url)
            
        except Exception as e:
            exception_msg: str = format_exception_message(exception=e, musician_id=list_musicians_input.musician_ids[i])
            exceptions_list.append(exception_msg)
    
    successful_count: int = len(successful_urls)
    overall_success: bool = determine_overall_success(successful_count=successful_count, total_count=len(list_musicians_input.musician_ids), exceptions=exceptions_list)
    
    return RedirectToMusiciansPagesOutput(
        redirection_results=successful_urls,
        successful_redirections_count=successful_count,
        redirection_exceptions=exceptions_list,
        is_redirection_successful=overall_success
    )