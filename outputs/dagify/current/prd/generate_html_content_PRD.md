# generate_html_content PRD

## Description
Create HTML output structure


## Conceptual Info

The `generate_html_content` node composes a minimal HTML5 document that lists the extracted song metadata and provides navigation links to the associated musicians. It accepts ordered lists of titles, artists, albums, and genre tags produced by `process_song_metadata`, as well as the musician profile URLs and official website URLs from `generate_musician_links`, and returns a single string containing the full HTML skeleton.

## Docstring

### Summary
Assembles a basic HTML5 skeleton incorporating song metadata and musician navigation links.

### Parameters

- **song_titles** (List[str]): Ordered list of song titles.
- **artist_names** (List[str]): Ordered list of artist names corresponding to the titles.
- **album_names** (List[str]): Ordered list of album names where the songs appear.
- **genre_tags** (List[str]): Ordered list of genre tags associated with each song.
- **musician_urls** (List[str]): Ordered list of deep links to musician profiles.
- **official_websites** (List[str]): Ordered list of official websites for the musicians.

### Returns

str: A complete HTML5 document as a string, ready to be injected with CSS and JavaScript.

### Raises

- ValueError: Raised when any of the input lists are empty or the list lengths differ, which would lead to mismatched metadata entries.

### Examples

```python
>>> html = generate_html_content(
...     song_titles=['Song A', 'Song B'],
...     artist_names=['Artist A', 'Artist B'],
...     album_names=['Album A', 'Album B'],
...     genre_tags=['Rock', 'Jazz'],
...     musician_urls=['https://music.com/artistA', 'https://music.com/artistB'],
...     official_websites=['https://artistA.com', 'https://artistB.com']
>>> )
<!DOCTYPE html>\n<html>\n<head>\n<title>Song Catalog</title>\n</head>\n<body>\n<h1>Song Catalog</h1>\n<ul>\n<li>Song A by Artist A (Album A) - Genres: Rock</li>\n<li>Song B by Artist B (Album B) - Genres: Jazz</li>\n</ul>\n<nav>\n<a href='https://music.com/artistA'>Artist A</a> | <a href='https://music.com/artistB'>Artist B</a>\n</nav>\n</body>\n</html>
```

```python
>>> generate_html_content([], [], [], [], [], [])
ValueError: All input lists must be non‑empty and of equal length.
```
