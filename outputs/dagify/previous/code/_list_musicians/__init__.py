from .deduplicate_artist_list import deduplicate_artist_list
from .fetch_musician_aliases import fetch_musician_aliases
from .extract_artist_names_from_metadata import extract_artist_names_from_metadata
from .validate_metadata_structure import validate_metadata_structure
from .normalize_artist_names import normalize_artist_names
from .generate_musician_ids import generate_musician_ids
from .check_deduplication_occurred import check_deduplication_occurred


__all__ = [
    'deduplicate_artist_list',
    'fetch_musician_aliases',
    'extract_artist_names_from_metadata',
    'validate_metadata_structure',
    'normalize_artist_names',
    'generate_musician_ids',
    'check_deduplication_occurred'
]
