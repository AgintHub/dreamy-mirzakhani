# generate_html_content PRD

## Description
Create HTML output structure


## Conceptual Info

Builds a minimal but extensible HTML5 document skeleton that incorporates song metadata and musician navigation links, ready for subsequent CSS/JS injections.

## Docstring

### Summary
Construct an HTML5 document skeleton using provided music metadata and artist links.

### Parameters

- **song_titles** (List[str]): Ordered list of matched song titles.
- **artist_names** (List[str]): Ordered list of artist names corresponding to the songs.
- **album_names** (List[str]): Ordered list of album names where the songs appear.
- **genre_tags** (List[str]): List of music genre tags inferred from the data.
- **musician_urls** (List[str]): Artist profile links constructed from database and web sources.
- **official_websites** (List[str]): Official band or artist web presences extracted from the same sources.

### Returns

str: A complete HTML5 document string with placeholders for metadata and navigation links.

### Raises

- ValueError: Raised when any input list is empty or misaligned (different lengths).

### Examples

```python
>>> html = build_html_structure(
...     song_titles=['Imagine'],
...     artist_names=['John Lennon'],
...     album_names=['Imagine'],
...     genre_tags=['Rock'],
...     musician_urls=['https://en.wikipedia.org/wiki/John_Lennon'],
...     official_websites=['https://johnlennon.com']
>>> )
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Imagine - John Lennon</title>
</head>
<body>
    <h1>Imagine</h1>
    <p>Artist: John Lennon</p>
    <p>Album: Imagine</p>
    <p>Genre: Rock</p>
    <nav>
        <ul>
            <li><a href="https://en.wikipedia.org/wiki/John_Lennon">John Lennon Profile</a></li>
        </ul>
    </nav>
    <footer>
        <p>Official site: <a href="https://johnlennon.com">johnlennon.com</a></p>
    </footer>
</body>
</html>
```

```python
>>> html = build_html_structure(
...     song_titles=['Song A', 'Song B'],
...     artist_names=['Artist X', 'Artist Y'],
...     album_names=['Album X', 'Album Y'],
...     genre_tags=['Pop', 'Jazz'],
...     musician_urls=['https://artistx.com', 'https://artisty.com'],
...     official_websites=['https://artistx.com', 'https://artisty.com']
>>> )
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Song A – Song B by Artist X – Artist Y</title>
</head>
<body>
    <section>
        <h1>Song A</h1>
        <p>Artist: Artist X</p>
        <p>Album: Album X</p>
        <p>Genre: Pop</p>
    </section>
    <section>
        <h1>Song B</h1>
        <p>Artist: Artist Y</p>
        <p>Album: Album Y</p>
        <p>Genre: Jazz</p>
    </section>
    <nav>
        <ul>
            <li><a href="https://artistx.com">Artist X Profile</a></li>
            <li><a href="https://artisty.com">Artist Y Profile</a></li>
        </ul>
    </nav>
    <footer>
        <p>Official sites: <a href="https://artistx.com">artistx.com</a>, <a href="https://artisty.com">artisty.com</a></p>
    </footer>
</body>
</html>
```
