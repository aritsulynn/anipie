# Anipie

<img src="https://anilist.co/img/icons/android-chrome-512x512.png" width="128"/>

> A modern, comprehensive wrapper for the AniList GraphQL API

Anipie is an easy-to-use Python library that provides object-oriented access to the AniList API. It handles GraphQL queries, rate limiting, and error handling for you.

## Installation

```bash
pip install anipie
```

## Features

- 🔍 Search for anime and manga by title or ID
- 📄 Paginated search results for large queries
- 🔄 Automatic rate limit handling
- 📊 Clean object-oriented API for accessing media properties
- ⚡ GraphQL-powered for efficient data retrieval
- 🛡️ Error handling with descriptive error messages

## Basic Usage

### Search for Anime

```python
from anipie import AnipieClient

# Create a client
client = AnipieClient()

# Search for an anime by title
anime = client.search_anime("Attack on Titan")

# Access anime properties
print(f"Title: {anime.title}")
print(f"Description: {anime.description}")
print(f"Episodes: {anime.episodes}")
print(f"Score: {anime.average_score}")
print(f"Cover: {anime.cover_large}")
```

### Search for Manga

```python
from anipie import AnipieClient

client = AnipieClient()

# Search for a manga by title
manga = client.search_manga("One Piece")

# Access manga properties
print(f"Title: {manga.title}")
print(f"Description: {manga.description}")
print(f"Chapters: {manga.chapters}")
print(f"Volumes: {manga.volumes}")
```

## Advanced Features

### Paginated Search

```python
from anipie import AnipieClient

client = AnipieClient()

# Get the first page with 10 results per page
results = client.search_anime_paged("dragon", page=1, per_page=10)

# Access page info
page_info = results["page_info"]
print(f"Has next page: {page_info['hasNextPage']}")
print(f"Total results: {page_info['total']}")

# Loop through results
for anime in results["results"]:
    print(anime.title)
```

### Fetch by ID

```python
from anipie import AnipieClient

client = AnipieClient()

# Get anime by ID
anime = client.get_anime_by_id(1)  # Cowboy Bebop

# Get manga by ID
manga = client.get_manga_by_id(13)  # One Piece
```

### Rate Limiting Information

```python
from anipie import AnipieClient

client = AnipieClient()
client.search_anime("Naruto")

# Check rate limit info
rate_info = client.get_rate_limit_info()
print(f"Rate limit: {rate_info['limit']}")
print(f"Remaining: {rate_info['remaining']}")
```

## Available Properties

### AnimeMedia Properties

- `id`: The unique identifier
- `title`: The romanized title
- `english_title`: The English title
- `native_title`: The native language title
- `description`: Detailed description
- `episodes`: Number of episodes
- `status`: Airing status
- `season`: Broadcasting season
- `format`: Format (TV, Movie, etc.)
- `genres`: List of genres
- `average_score`: Average user score
- `start_date`: Premiere date
- `end_date`: End date
- `duration`: Episode duration (minutes)
- `cover_large`: Cover image URL
- `site_url`: URL to AniList page
- `studios`: List of studio names
- `is_adult`: Whether content is marked as adult

### MangaMedia Properties

- `id`: The unique identifier
- `title`: The romanized title
- `english_title`: The English title
- `native_title`: The native language title
- `description`: Detailed description
- `chapters`: Number of chapters
- `volumes`: Number of volumes
- `status`: Publication status
- `format`: Format (Manga, Novel, etc.)
- `genres`: List of genres
- `average_score`: Average user score
- `start_date`: Initial publication date
- `end_date`: End date
- `cover_large`: Cover image URL
- `site_url`: URL to AniList page
- `staff`: List of staff members and roles

## Error Handling

Anipie provides helpful error messages for common issues:

```python
from anipie import AnipieClient

client = AnipieClient()

try:
    # Try to fetch a non-existent ID
    anime = client.get_anime_by_id(9999999)
except ValueError as e:
    print(f"Error: {e}")
```

## Rate Limiting

AniList API has rate limits that Anipie automatically tracks:

- 90 requests per minute for normal usage
- If you exceed the rate limit, the API will return a 429 error

You can monitor your rate limit usage with `get_rate_limit_info()` method.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
