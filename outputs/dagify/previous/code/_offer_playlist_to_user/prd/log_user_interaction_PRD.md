# log_user_interaction PRD

## Description
Logs user interaction with a generated playlist and returns a telemetry log identifier.


## Conceptual Info

This shim node is responsible for logging user interactions with generated playlists, capturing key details about the interaction, and returning a unique identifier for the telemetry log entry.

## Docstring

### Summary
Logs user interaction with a playlist and returns a telemetry log identifier.

### Parameters

- **playlist_id** (str): Unique identifier for the generated playlist that was interacted with.
- **ui_data** (str): Data representing the UI component rendered for the playlist.
- **playback_enabled** (str): Boolean indicating whether real-time playback was enabled for the playlist.
- **save_status** (str): Boolean indicating whether the save operation to the user's library was successful.

### Returns

str: Unique identifier for the telemetry log entry created for this user interaction.

### Raises

- ValueError: If any of the input parameters are invalid or missing.
- TypeError: If the input parameter types are not as expected.

### Examples

```python
>>> log_user_interaction(playlist_id='12345', ui_data='{"playlist_name": "My Playlist"}', playback_enabled='True', save_status='True')
"log_id_12345"
```

```python
>>> log_user_interaction(playlist_id='67890', ui_data='{"playlist_name": "Another Playlist"}', playback_enabled='False', save_status='False')
"log_id_67890"
```
