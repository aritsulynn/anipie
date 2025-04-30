"""
Models for Anipie (the AniList API wrapper.)
"""

from .animeMedia import AnimeMedia
from .mangaMedia import MangaMedia

__all__ = [
    'AnimeMedia',
    'MangaMedia'
]