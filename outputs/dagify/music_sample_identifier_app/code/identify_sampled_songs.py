from ._identify_sampled_songs.validate_audio_data import validate_audio_data
from ._identify_sampled_songs.generate_audio_fingerprint import generate_audio_fingerprint
from ._identify_sampled_songs.extract_deep_learning_embeddings import extract_deep_learning_embeddings
from ._identify_sampled_songs.perform_similarity_search import perform_similarity_search
from ._identify_sampled_songs.select_best_candidate import select_best_candidate
from ._identify_sampled_songs.calculate_segment_timing import calculate_segment_timing
from ._identify_sampled_songs.fetch_track_metadata import fetch_track_metadata

from pydantic import BaseModel, Field
from typing import List


class PreprocessAudioDataOutput(BaseModel):
    """Pydantic model for preprocess_audio_data node outputs."""
    processed_audio_base64: str = (
        Field(..., description = (
            "Base64-encoded binary payload of the processed audio ready for downstream consumption.")
        )
    )
    duration_seconds: float = (
        Field(..., description = (
            "Total duration of the processed audio in seconds.")
        )
    )
    sample_rate_hz: int = (
        Field(..., description="Sampling rate of the processed audio in Hertz.")
    )
    codec: str = (
        Field(..., description = (
            "Audio codec used for encoding the processed audio (e.g., Opus, PCM).")
        )
    )
    vad_confidence: float = (
        Field(..., description = (
            "Confidence score (0.0\u20131.0) of Voice Activity Detection applied during preprocessing.")
        )
    )
    noise_reduction_method: str = (
        Field(..., description = (
            "Method used for noise reduction (e.g., spectral_subtraction, wiener_filter, deep_learning).")
        )
    )
    normalization_method: str = (
        Field(..., description = (
            "Method used for audio normalization (e.g., peak_normalization, loudness_normalization).")
        )
    )
    feature_vectors: List[float] = (
        Field(..., description = (
            "Flattened list of extracted audio feature vectors (e.g., MFCCs, chroma, spectral contrast).")
        )
    )
    processing_success: bool = (
        Field(..., description = (
            "Indicates whether the preprocessing pipeline completed successfully without critical errors.")
        )
    )


class IdentifySampledSongsOutput(BaseModel):
    """Pydantic model for identify_sampled_songs node outputs."""
    track_id: str = (
        Field(..., description = (
            "Unique identifier for the candidate track in the database.")
        )
    )
    confidence: float = (
        Field(..., description = (
            "Confidence score (0.0 to 1.0) indicating the likelihood that the candidate matches the sampled snippet.")
        )
    )
    start_time: float = (
        Field(..., description = (
            "Start timestamp (in seconds) of the matched segment within the sampled snippet.")
        )
    )
    end_time: float = (
        Field(..., description = (
            "End timestamp (in seconds) of the matched segment within the sampled snippet.")
        )
    )
    artist_name: str = (
        Field(..., description="Name of the artist of the candidate track.")
    )
    track_title: str = Field(..., description="Title of the candidate track.")
    release_date: str = (
        Field(..., description = (
            "Release date of the candidate track (ISO 8601 format).")
        )
    )


def identify_sampled_songs(preprocess_audio_data_input: PreprocessAudioDataOutput, **kwargs) -> IdentifySampledSongsOutput:
    """
    Identifies sampled songs by extracting features, generating fingerprints,
    and performing similarity search.

    Parameters
    ----------
    processed_audio_data : dict
        Preprocessed audio data containing base64 encoded audio, duration,
        sample rate, and feature vectors.

    Returns
    -------
    List[dict]
        A list of dictionaries containing track_id, confidence, start_time,
        end_time, and metadata for each identified candidate track.

    Raises
    ------
    ValueError
        If the input audio data is invalid or corrupted.
    RuntimeError
        If the similarity search or fingerprint generation fails.

    Examples
    --------
    >>> processed_audio_data = {'processed_audio_base64': '...',
    'duration_seconds': 10.0, 'sample_rate_hz': 44100, 'feature_vectors': [...]
    >>> identified_tracks = identify_sampled_songs(processed_audio_data)
    [{'track_id': 'TRK123', 'confidence': 0.9, 'start_time': 2.5, 'end_time':
    5.0, 'artist_name': 'Artist1', 'track_title': 'Track1', 'release_date':
    '2020-01-01'}]

    """
    validated_audio = validate_audio_data(audio_data=preprocess_audio_data_input)
    audio_fingerprint = generate_audio_fingerprint(audio_base64=validated_audio.processed_audio_base64, sample_rate=validated_audio.sample_rate_hz)
    embedding_features = extract_deep_learning_embeddings(feature_vectors=validated_audio.feature_vectors, audio_data=validated_audio)
    candidate_matches = perform_similarity_search(fingerprint=audio_fingerprint, embeddings=embedding_features, duration=validated_audio.duration_seconds)
    best_match = select_best_candidate(candidates=candidate_matches)
    segment_timing = calculate_segment_timing(match=best_match, audio_duration=validated_audio.duration_seconds)
    track_metadata = fetch_track_metadata(track_id=best_match["track_id"])
    return IdentifySampledSongsOutput(
        track_id=best_match["track_id"],
        confidence=best_match["confidence"],
        start_time=segment_timing["start_time"],
        end_time=segment_timing["end_time"],
        artist_name=track_metadata["artist_name"],
        track_title=track_metadata["track_title"],
        release_date=track_metadata["release_date"]
    )