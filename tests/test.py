import pytest
from unittest.mock import patch, Mock, MagicMock
import json
import requests
import sys
import os

# Add the parent directory to the Python path so we can import anipie
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from anipie import AnipieClient, AnimeMedia, MangaMedia


# Fixtures for test data
@pytest.fixture
def anime_sample_data():
    return {
        "id": 1,
        "title": {
            "romaji": "Cowboy Bebop",
            "english": "Cowboy Bebop",
            "native": "カウボーイビバップ"
        },
        "status": "FINISHED",
        "description": "Enter a world in the distant future...",
        "averageScore": 86,
        "startDate": {
            "year": 1998,
            "month": 4,
            "day": 3
        },
        "endDate": {
            "year": 1999,
            "month": 4,
            "day": 24
        },
        "coverImage": {
            "large": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx1-CXtrrkMpJ8Zq.png"
        },
        "genres": ["Action", "Adventure", "Drama", "Sci-Fi"],
        "siteUrl": "https://anilist.co/anime/1",
        "episodes": 26,
        "season": "SPRING",
        "format": "TV",
        "duration": 24,
        "studios": {
            "nodes": [
                {
                    "id": 14,
                    "name": "Sunrise"
                }
            ]
        },
        "isAdult": False
    }


@pytest.fixture
def manga_sample_data():
    return {
        "id": 13,
        "title": {
            "romaji": "One Piece",
            "english": "One Piece",
            "native": "ワンピース"
        },
        "status": "RELEASING",
        "description": "Gol D. Roger was known as the Pirate King...",
        "averageScore": 90,
        "startDate": {
            "year": 1997,
            "month": 7,
            "day": 22
        },
        "endDate": {
            "year": None,
            "month": None,
            "day": None
        },
        "coverImage": {
            "large": "https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx13-5jWAZYOOewe0.jpg"
        },
        "genres": ["Action", "Adventure", "Comedy", "Fantasy"],
        "siteUrl": "https://anilist.co/manga/13",
        "chapters": 1050,
        "volumes": 102,
        "format": "MANGA",
        "staff": {
            "edges": [
                {
                    "role": "Story & Art",
                    "node": {
                        "id": 96892,
                        "name": {
                            "full": "Eiichiro Oda"
                        }
                    }
                }
            ]
        }
    }


@pytest.fixture
def paged_anime_response():
    return {
        "data": {
            "Page": {
                "pageInfo": {
                    "hasNextPage": True,
                    "total": 50,
                    "perPage": 10,
                    "currentPage": 1,
                    "lastPage": 5
                },
                "media": [
                    {
                        "id": 1,
                        "title": {"romaji": "Naruto", "english": "Naruto", "native": "ナルト"},
                        "format": "TV",
                        "status": "FINISHED",
                        "description": "Naruto Uzumaki, a mischievous adolescent ninja...",
                        "averageScore": 79,
                        "coverImage": {"large": "https://example.com/naruto.jpg"}
                    },
                    {
                        "id": 2,
                        "title": {"romaji": "Naruto Shippuden", "english": "Naruto Shippuden", "native": "ナルト 疾風伝"},
                        "format": "TV",
                        "status": "FINISHED",
                        "description": "Naruto Shippuden continues the story of Naruto Uzumaki...",
                        "averageScore": 84,
                        "coverImage": {"large": "https://example.com/shippuden.jpg"}
                    }
                ]
            }
        }
    }


@pytest.fixture
def paged_manga_response():
    return {
        "data": {
            "Page": {
                "pageInfo": {
                    "hasNextPage": True,
                    "total": 50,
                    "perPage": 10,
                    "currentPage": 1,
                    "lastPage": 5
                },
                "media": [
                    {
                        "id": 3,
                        "title": {"romaji": "Naruto", "english": "Naruto", "native": "ナルト"},
                        "format": "MANGA",
                        "status": "FINISHED",
                        "description": "Naruto manga description...",
                        "averageScore": 82,
                        "coverImage": {"large": "https://example.com/naruto-manga.jpg"},
                        "chapters": 700,
                        "volumes": 72
                    },
                    {
                        "id": 4,
                        "title": {"romaji": "Boruto", "english": "Boruto: Naruto Next Generations", "native": "BORUTO-ボルト-"},
                        "format": "MANGA",
                        "status": "RELEASING",
                        "description": "Boruto manga description...",
                        "averageScore": 75,
                        "coverImage": {"large": "https://example.com/boruto.jpg"},
                        "chapters": 60,
                        "volumes": 15
                    }
                ]
            }
        }
    }


class TestAnipieClient:
    """Tests for the AnipieClient class."""

    def test_client_initialization(self):
        """Test that client initializes with correct default values."""
        client = AnipieClient()
        assert client.url == "https://graphql.anilist.co"
        assert client.headers == {"Content-Type": "application/json", "Accept": "application/json"}
        assert client.rate_limit is None
        assert client.rate_limit_remaining is None

    @patch("requests.post")
    def test_make_request(self, mock_post):
        """Test the _make_request method with mocked response."""
        # Setup mock response
        mock_response = Mock()
        mock_response.json.return_value = {"data": {"test": "success"}}
        mock_response.headers = {
            'X-RateLimit-Limit': '90',
            'X-RateLimit-Remaining': '89'
        }
        mock_post.return_value = mock_response

        client = AnipieClient()
        result = client._make_request("test query", {"var": "value"})

        # Verify method called with correct parameters
        mock_post.assert_called_once_with(
            "https://graphql.anilist.co",
            json={"query": "test query", "variables": {"var": "value"}},
            headers={"Content-Type": "application/json", "Accept": "application/json"}
        )

        # Verify result and rate limiting info
        assert result == {"data": {"test": "success"}}
        assert client.rate_limit == 90
        assert client.rate_limit_remaining == 89

    @patch("requests.post")
    def test_make_request_error_handling(self, mock_post):
        """Test error handling in _make_request method."""
        # Setup mock response with GraphQL error
        mock_response = Mock()
        mock_response.json.return_value = {
            "errors": [{"message": "Not found"}]
        }
        mock_response.headers = {} # Empty dict instead of Mock object
        mock_post.return_value = mock_response

        client = AnipieClient()
        with pytest.raises(ValueError, match="GraphQL Error: Not found"):
            client._make_request("test query", {"var": "value"})

    @patch("anipie.client.AnipieClient._make_request")
    def test_search_anime(self, mock_make_request, anime_sample_data):
        """Test search_anime method."""
        # Setup mock response
        mock_make_request.return_value = {"data": {"Media": anime_sample_data}}

        client = AnipieClient()
        result = client.search_anime("Cowboy Bebop")

        # Verify method called with correct parameters
        mock_make_request.assert_called_once()
        assert isinstance(result, AnimeMedia)
        assert result.title == "Cowboy Bebop"
        assert result.episodes == 26

    @patch("anipie.client.AnipieClient._make_request")
    def test_search_manga(self, mock_make_request, manga_sample_data):
        """Test search_manga method."""
        # Setup mock response
        mock_make_request.return_value = {"data": {"Media": manga_sample_data}}

        client = AnipieClient()
        result = client.search_manga("One Piece")

        # Verify method called with correct parameters
        mock_make_request.assert_called_once()
        assert isinstance(result, MangaMedia)
        assert result.title == "One Piece"
        assert result.chapters == 1050

    @patch("anipie.client.AnipieClient._make_request")
    def test_get_anime_by_id(self, mock_make_request, anime_sample_data):
        """Test get_anime_by_id method."""
        # Setup mock response
        mock_make_request.return_value = {"data": {"Media": anime_sample_data}}

        client = AnipieClient()
        result = client.get_anime_by_id(1)

        # Verify method called with correct parameters
        mock_make_request.assert_called_once()
        assert isinstance(result, AnimeMedia)
        assert result.id == 1

    @patch("anipie.client.AnipieClient._make_request")
    def test_get_manga_by_id(self, mock_make_request, manga_sample_data):
        """Test get_manga_by_id method."""
        # Setup mock response
        mock_make_request.return_value = {"data": {"Media": manga_sample_data}}

        client = AnipieClient()
        result = client.get_manga_by_id(13)

        # Verify method called with correct parameters
        mock_make_request.assert_called_once()
        assert isinstance(result, MangaMedia)
        assert result.id == 13

    @patch("anipie.client.AnipieClient._make_request")
    def test_search_anime_paged(self, mock_make_request, paged_anime_response):
        """Test search_anime_paged method."""
        # Setup mock response
        mock_make_request.return_value = paged_anime_response

        client = AnipieClient()
        result = client.search_anime_paged("Naruto", page=1, per_page=10)

        # Verify method called with correct parameters
        mock_make_request.assert_called_once()
        assert "page_info" in result
        assert "results" in result
        assert len(result["results"]) == 2
        assert isinstance(result["results"][0], AnimeMedia)
        assert result["page_info"]["total"] == 50

    @patch("anipie.client.AnipieClient._make_request")
    def test_search_manga_paged(self, mock_make_request, paged_manga_response):
        """Test search_manga_paged method."""
        # Setup mock response
        mock_make_request.return_value = paged_manga_response

        client = AnipieClient()
        result = client.search_manga_paged("Naruto", page=1, per_page=10)

        # Verify method called with correct parameters
        mock_make_request.assert_called_once()
        assert "page_info" in result
        assert "results" in result
        assert len(result["results"]) == 2
        assert isinstance(result["results"][0], MangaMedia)
        assert result["page_info"]["total"] == 50

    def test_get_rate_limit_info(self):
        """Test get_rate_limit_info method."""
        client = AnipieClient()
        client.rate_limit = 90
        client.rate_limit_remaining = 85

        result = client.get_rate_limit_info()
        assert result == {"limit": 90, "remaining": 85}


class TestAnimeMedia:
    """Tests for the AnimeMedia class."""

    def test_properties(self, anime_sample_data):
        """Test property accessors for AnimeMedia."""
        anime = AnimeMedia(anime_sample_data)

        # Test basic properties
        assert anime.id == 1
        assert anime.title == "Cowboy Bebop"
        assert anime.english_title == "Cowboy Bebop"
        assert anime.native_title == "カウボーイビバップ"
        assert anime.status == "FINISHED"
        assert anime.description == "Enter a world in the distant future..."
        assert anime.episodes == 26
        assert anime.cover_large == "https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx1-CXtrrkMpJ8Zq.png"
        assert anime.site_url == "https://anilist.co/anime/1"
        assert anime.genres == "Action, Adventure, Drama, Sci-Fi"
        assert anime.start_date == "4/3/1998"
        assert anime.end_date == "4/24/1999"
        assert anime.average_score == 8.6
        assert anime.season == "SPRING"
        assert anime.format == "TV"
        assert anime.duration == 24
        assert anime.is_adult is False

        # Test studios property
        studios = anime.studios
        assert isinstance(studios, list)
        assert len(studios) == 1
        assert studios[0]["name"] == "Sunrise"

    def test_missing_data(self):
        """Test handling of missing data."""
        # Create anime with minimal data
        minimal_data = {
            "id": 2,
            "title": {"romaji": "Test Anime"}
        }
        anime = AnimeMedia(minimal_data)

        # Test that properties handle missing data gracefully
        assert anime.id == 2
        assert anime.title == "Test Anime"
        assert anime.english_title is None
        assert anime.native_title is None
        assert anime.status is None
        assert anime.description is None
        assert anime.episodes is None
        assert anime.cover_large is None
        assert anime.site_url is None
        assert anime.genres is None
        assert anime.start_date is None
        assert anime.end_date is None
        assert anime.average_score is None
        assert anime.season is None
        assert anime.format is None
        assert anime.duration is None
        assert anime.studios is None


class TestMangaMedia:
    """Tests for the MangaMedia class."""

    def test_properties(self, manga_sample_data):
        """Test property accessors for MangaMedia."""
        manga = MangaMedia(manga_sample_data)

        # Test basic properties
        assert manga.id == 13
        assert manga.title == "One Piece"
        assert manga.english_title == "One Piece"
        assert manga.native_title == "ワンピース"
        assert manga.status == "RELEASING"
        assert manga.description == "Gol D. Roger was known as the Pirate King..."
        assert manga.cover_large == "https://s4.anilist.co/file/anilistcdn/media/manga/cover/large/bx13-5jWAZYOOewe0.jpg"
        assert manga.site_url == "https://anilist.co/manga/13"
        assert manga.genres == "Action, Adventure, Comedy, Fantasy"
        assert manga.start_date == "7/22/1997"
        assert manga.end_date is None  # Since end date is null
        assert manga.average_score == 9.0
        assert manga.chapters == 1050
        assert manga.volumes == 102
        assert manga.format == "MANGA"

        # Test staff property
        staff = manga.staff
        assert isinstance(staff, list)
        assert len(staff) == 1
        assert staff[0]["name"] == "Eiichiro Oda"
        assert staff[0]["role"] == "Story & Art"

    def test_missing_data(self):
        """Test handling of missing data."""
        # Create manga with minimal data
        minimal_data = {
            "id": 14,
            "title": {"romaji": "Test Manga"}
        }
        manga = MangaMedia(minimal_data)

        # Test that properties handle missing data gracefully
        assert manga.id == 14
        assert manga.title == "Test Manga"
        assert manga.english_title is None
        assert manga.native_title is None
        assert manga.status is None
        assert manga.description is None
        assert manga.cover_large is None
        assert manga.site_url is None
        assert manga.genres is None
        assert manga.start_date is None
        assert manga.end_date is None
        assert manga.average_score is None
        assert manga.chapters is None
        assert manga.volumes is None
        assert manga.format is None
        assert manga.staff is None


# Integration tests with mocked responses
class TestAnipieIntegration:
    """Integration tests for Anipie using mocked responses."""

    @patch("requests.post")
    def test_full_anime_lookup_flow(self, mock_post, anime_sample_data):
        """Test a full flow of looking up and using anime data."""
        # Setup mock response
        mock_response = Mock()
        mock_response.json.return_value = {"data": {"Media": anime_sample_data}}
        mock_response.headers = {'X-RateLimit-Limit': '90', 'X-RateLimit-Remaining': '89'}
        mock_post.return_value = mock_response

        client = AnipieClient()
        anime = client.search_anime("Cowboy Bebop")

        # Verify rate limit info is saved
        rate_info = client.get_rate_limit_info()
        assert rate_info["limit"] == 90
        assert rate_info["remaining"] == 89

        # Verify anime object has correct data
        assert anime.title == "Cowboy Bebop"
        assert anime.episodes == 26
        assert anime.format == "TV"
        assert anime.studios[0]["name"] == "Sunrise"

    @patch("requests.post")
    def test_error_handling_with_nonexistent_anime(self, mock_post):
        """Test error handling with a non-existent anime."""
        # Setup mock response with GraphQL error
        mock_response = Mock()
        mock_response.json.return_value = {
            "errors": [{"message": "Not Found"}]
        }
        mock_response.headers = {}
        mock_post.return_value = mock_response

        client = AnipieClient()
        with pytest.raises(ValueError, match="GraphQL Error: Not Found"):
            client.search_anime("NonexistentAnime12345")