# generate_html_content PRD

## Description
Create HTML output structure


## Conceptual Info

Builds a minimal HTML5 document skeleton that displays song metadata and provides navigation links to musician profiles.

## Docstring

### Summary
Assemble a basic HTML5 skeleton incorporating song metadata and musician navigation links.
The function aggregates lists of titles, artists, albums, genres, musician URLs, and official websites into a single HTML string ready for further styling and scripting.

### Parameters

- **song_titles** (List[str]): Ordered list of matched song titles.
- **artist_names** (List[str]): Ordered list of artist names corresponding to the titles.
- **album_names** (List[str]): Ordered list of album names where the songs appear.
- **genre_tags** (List[str]): Ordered list of inferred music genre tags.
- **musician_urls** (List[str]): List of deep links to artist profile pages.
- **official_websites** (List[str]): List of official band or artist web presences.

### Returns

str: A string containing a complete but minimal HTML5 document skeleton. The document includes a <head> section with a title derived from the first song/artist pair, and a <body> section that lists each song with its album and genre, followed by navigation links to each musician profile and official website.

### Raises

- ValueError: Raised if any of the input lists are empty or if the input lists are of unequal length.
- TypeError: Raised if any of the input parameters are not of type List[str].

### Examples

```python
>>> html = generate_html_content(

...     ['Song A'],

...     ['Artist X'],

...     ['Album Y'],

...     ['Pop'],

...     ['https://artistx.com/profile'],

...     ['https://artistx.com']

>>> )
>>> print(html)
<!DOCTYPE html>\n<html>\n<head>\n<title>Song A - Artist X</title>\n</head>\n<body>\n<h1>Song A</h1>\n<p><strong>Artist:</strong> Artist X</p>\n<p><strong>Album:</strong> Album Y</p>\n<p><strong>Genre:</strong> Pop</p>\n<h2>Musician Links</h2>\n<ul>\n<li><a href="https://artistx.com/profile">Artist Profile</a></li>\n<li><a href="https://artistx.com">Official Website</a></li>\n</ul>\n</body>\n</html>
```

```python
>>> html = generate_html_content(

...     ['Song 1', 'Song 2'],

...     ['Band A', 'Band B'],

...     ['Album X', 'Album Y'],

...     ['Rock', 'Jazz'],

...     ['https://banda.com', 'https://bandb.com'],

...     ['https://banda.com', 'https://bandb.com']

>>> )
>>> print(html.split('\n')[0])
<!DOCTYPE html>
```
