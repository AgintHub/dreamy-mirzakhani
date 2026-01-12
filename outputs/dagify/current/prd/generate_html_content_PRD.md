# generate_html_content PRD

## Description
Create HTML output structure


## Conceptual Info

This node generates a basic HTML5 document structure using metadata and musician links provided by its parent nodes.

## Docstring

### Summary
Assemble a basic HTML5 document structure using song metadata and musician links.

### Parameters

- **song_titles** (List[str]): Collection of matched song titles from `process_song_metadata`.
- **artist_names** (List[str]): Collection of artist names associated with the matches from `process_song_metadata`.
- **album_names** (List[str]): Collection of album names where the songs appear from `process_song_metadata`.
- **genre_tags** (List[str]): List of music genre tags inferred from the data by `process_song_metadata`.
- **musician_urls** (List[str]): Artist profile links constructed from database and web sources by `generate_musician_links`.
- **official_websites** (List[str]): Official band or artist web presences extracted from the same sources by `generate_musician_links`.

### Returns

str: A string representing the base HTML document skeleton.

### Raises

- ValueError: If any of the input lists are empty or inconsistent in length.
- TypeError: If the inputs are not of the expected type.

### Examples

```python
>>> song_titles = ['Song1', 'Song2']
>>> artist_names = ['Artist1', 'Artist2']
>>> album_names = ['Album1', 'Album2']
>>> genre_tags = ['Rock', 'Pop']
>>> musician_urls = ['http://artist1.com', 'http://artist2.com']
>>> official_websites = ['http://official1.com', 'http://official2.com']
>>> generate_html_content(song_titles, artist_names, album_names, genre_tags, musician_urls, official_websites)
<!DOCTYPE html><html><head></head><body>...</body></html>
```
