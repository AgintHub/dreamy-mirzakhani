# update_redux_state PRD

## Description
Updates the Redux state with new data based on the input parameters.


## Conceptual Info

This shim function is responsible for updating the Redux state with new data, such as sample identification results, musician listing data, or playlist information.

## Docstring

### Summary
Updates the Redux state with the provided data and returns the updated state.

### Parameters

- **state** (str): The current Redux state as a string.
- **playlist_data** (str): The playlist data used to update the Redux state.

### Returns

str: The updated Redux state as a string.

### Raises

- TypeError: If the input state or playlist_data is not a string.
- ValueError: If the input state is not a valid Redux state.

### Examples

```python
>>> updated_state = update_redux_state(state='{"sample_id": "123"}', playlist_data='{"playlist_id": "456"}')
>>> print(updated_state)
{"sample_id": "123", "playlist_id": "456"}
```

```python
>>> update_redux_state(state='invalid_state', playlist_data='{"playlist_id": "789"}')
>>> print(updated_state)
ValueError: Invalid Redux state
```
