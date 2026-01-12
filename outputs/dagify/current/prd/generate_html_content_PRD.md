# generate_html_content PRD

## Description
Create HTML output structure


## Conceptual Info

Creates a minimal HTML5 skeleton populated with metadata and navigation links for the identified songs and artists, serving as the foundation for subsequent styling and scripting.

## Docstring

### Summary
Generates a foundational HTML5 document string from song metadata and musician links.

### Parameters

- **song_titles** (List[str]): List of song titles returned by the process_song_metadata node.
- **artist_names** (List[str]): List of artist names returned by the process_song_metadata node.
- **album_names** (List[str]): List of album names returned by the process_song_metadata node.
- **genre_tags** (List[str]): List of genre tags returned by the process_song_metadata node.
- **musician_urls** (List[str]): List of deep links to musician profiles returned by generate_musician_links.
- **official_websites** (List[str]): List of official web presences for the artists returned by generate_musician_links.

### Returns

str: A complete HTML5 document string containing a header, a list of songs with metadata, and a navigation section for musicians.

### Raises

- ValueError: Raised if any of the required input lists is missing or empty.

### Examples

```python
>>> html = generate_html_content(
...     song_titles=['Song A'],
...     artist_names=['Artist X'],
...     album_names=['Album Y'],
...     genre_tags=['Rock'],
...     musician_urls=['https://music.com/artistx'],
...     official_websites=['https://artistx.com']
>>> )
>>> print(html[:200])
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Song Metadata</title>
</head>
<body>
<h1>Song List</h1>
<ul>
  <li>Song A – Artist X (Album Y) [Rock]</li>
</ul>
<nav>
  <h2>Artists</h2>
  <ul>
    <li><a href="https://music.com/artistx">Artist X</a> – <a href="https://artistx.com">Official Website</a></li>
  </ul>
</nav>
</body>
</html>
```

```python
>>> html = generate_html_content(
...     song_titles=['Song A', 'Song B'],
...     artist_names=['Artist X', 'Artist Y'],
...     album_names=['Album Y', 'Album Z'],
...     genre_tags=['Rock', 'Jazz'],
...     musician_urls=['https://music.com/artistx', 'https://music.com/artisty'],
...     official_websites=['https://artistx.com', 'https://artisty.com']
>>> )
>>> print(html.count('<li>'))
4
```
