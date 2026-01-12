from ._create_playlist.validate_musician_inputs import validate_musician_inputs
from ._create_playlist.expand_musician_aliases import expand_musician_aliases
from ._create_playlist.fetch_sampled_songs_metadata import fetch_sampled_songs_metadata
from ._create_playlist.extract_nlp_features import extract_nlp_features
from ._create_playlist.apply_collaborative_filtering import apply_collaborative_filtering
from ._create_playlist.build_graph_based_model import build_graph_based_model
from ._create_playlist.rank_tracks_with_graph_algorithm import rank_tracks_with_graph_algorithm
from ._create_playlist.select_final_tracks import select_final_tracks
from ._create_playlist.generate_playlist_metadata import generate_playlist_metadata
from ._create_playlist.calculate_artist_diversity_score import calculate_artist_diversity_score
from ._create_playlist.extract_genre_representation import extract_genre_representation
from ._create_playlist.generate_playlist_id import generate_playlist_id

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


class CreatePlaylistOutput(BaseModel):
    """Pydantic model for create_playlist node outputs."""
    playlist_id: str = (
        Field(..., description="Unique identifier for the generated playlist")
    )
    track_ids: List[str] = (
        Field(..., description = (
            "List of track identifiers included in the playlist")
        )
    )
    playlist_name: str = (
        Field(..., description="Name of the generated playlist")
    )
    playlist_description: str = (
        Field(..., description = (
            "Description of the playlist, including its theme and coherence")
        )
    )
    artist_diversity_score: float = (
        Field(..., description = (
            "Score representing the diversity of artists in the playlist")
        )
    )
    genre_representation: List[str] = (
        Field(..., description="List of genres represented in the playlist")
    )


def create_playlist(list_musicians_input: ListMusiciansOutput, **kwargs) -> CreatePlaylistOutput:
    """
    Creates a playlist by analyzing sampled songs' metadata, applying NLP and
    collaborative filtering, and ranking tracks based on a graph-based model.

    Parameters
    ----------
    musician_ids : List[str]
        List of unique identifiers for the musicians, derived from the
        `list_musicians` node.
    musician_names : List[str]
        List of names of the musicians, used to inform the playlist's
        thematic coherence.
    musician_aliases : List[List[str]]
        List of lists containing aliases for each musician, aiding in
        disambiguation and comprehensive coverage.

    Returns
    -------
    Dict[str, Union[str, List[str], float]]
        A dictionary containing the generated playlist's details, including
        its ID, track IDs, name, description, artist diversity score, and
        genre representation.

    Raises
    ------
    ValueError
        If the input lists (`musician_ids`, `musician_names`,
        `musician_aliases`) are inconsistent or empty.
    RuntimeError
        If the graph-based ranking algorithm fails to converge or if there's
        an issue with the MIR framework.

    Examples
    --------
    >>> create_playlist(musician_ids=['M1', 'M2'], musician_names=['Artist1',
    'Artist2'], musician_aliases=[['A1'], ['A2']])
    {'playlist_id': 'P1', 'track_ids': ['T1', 'T2'], 'playlist_name': 'Diverse
    Playlist', 'playlist_description': 'A mix of genres',
    'artist_diversity_score': 0.8, 'genre_representation': ['Rock', 'Pop']}

    """
    validate_musician_inputs(musician_ids=list_musicians_input.musician_ids, musician_names=list_musicians_input.musician_names, musician_aliases=list_musicians_input.musician_aliases)
    
    expanded_musician_data: dict = expand_musician_aliases(musician_ids=list_musicians_input.musician_ids, musician_names=list_musicians_input.musician_names, aliases=list_musicians_input.musician_aliases)
    
    sampled_songs_metadata: List[dict] = fetch_sampled_songs_metadata(musician_data=expanded_musician_data)
    
    nlp_features: dict = extract_nlp_features(songs_metadata=sampled_songs_metadata)
    
    collaborative_filtering_scores: dict = apply_collaborative_filtering(musician_data=expanded_musician_data, songs_metadata=sampled_songs_metadata)
    
    graph_model: dict = build_graph_based_model(nlp_features=nlp_features, cf_scores=collaborative_filtering_scores, songs_metadata=sampled_songs_metadata)
    
    ranked_tracks: List[str] = rank_tracks_with_graph_algorithm(graph_model=graph_model)
    
    selected_track_ids: List[str] = select_final_tracks(ranked_tracks=ranked_tracks, diversity_threshold=0.7)
    
    playlist_metadata: dict = generate_playlist_metadata(selected_tracks=selected_track_ids, musician_names=list_musicians_input.musician_names)
    
    diversity_score: float = calculate_artist_diversity_score(track_ids=selected_track_ids)
    
    genre_representation: List[str] = extract_genre_representation(track_ids=selected_track_ids)
    
    playlist_id: str = generate_playlist_id()
    
    return CreatePlaylistOutput(
        playlist_id=playlist_id,
        track_ids=selected_track_ids,
        playlist_name=playlist_metadata["name"],
        playlist_description=playlist_metadata["description"],
        artist_diversity_score=diversity_score,
        genre_representation=genre_representation
    )