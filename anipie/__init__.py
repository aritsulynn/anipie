"""
Anipie - A comprehensive wrapper for the AniList GraphQL API.
"""

from .client import AnipieClient
from .models.animeMedia import AnimeMedia
from .models.mangaMedia import MangaMedia

__version__ = "0.1.0"

__all__ = [
    "AnipieClient",
    "AnimeMedia",
    "MangaMedia"
]