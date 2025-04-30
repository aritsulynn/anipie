import requests
from anipie.models import AnimeMedia, MangaMedia

from .queries import (ANIME_QUERY, MANGA_QUERY, ANIME_BY_ID_QUERY, 
                     MANGA_BY_ID_QUERY, SEARCH_ANIME_PAGE_QUERY, SEARCH_MANGA_PAGE_QUERY)

class AnipieClient():
    """
    A comprehensive wrapper for the AniList GraphQL API.
    Returns object-oriented results for easy access to properties.
    
    This client uses the AniList GraphQL API (https://graphql.anilist.co)
    and provides methods to search for anime and manga.
    """

    def __init__(self) -> None:
        """Initialize the Anipie object."""
        self.url = "https://graphql.anilist.co"
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
        self.rate_limit = None
        self.rate_limit_remaining = None

    def _make_request(self, query, variables):
        """
        Make a request to the AniList GraphQL API.
        
        Args:
            query (str): The GraphQL query to execute
            variables (dict): The variables to include with the query
            
        Returns:
            dict: The JSON response from the API
            
        Raises:
            requests.exceptions.HTTPError: If the API returns an error
        """
        payload = {
            "query": query,
            "variables": variables,
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        
        # Store rate limiting information
        if 'X-RateLimit-Limit' in response.headers:
            self.rate_limit = int(response.headers['X-RateLimit-Limit'])
        
        if 'X-RateLimit-Remaining' in response.headers:
            self.rate_limit_remaining = int(response.headers['X-RateLimit-Remaining'])
        
        response.raise_for_status()
        
        # Check for GraphQL errors
        json_response = response.json()
        if 'errors' in json_response:
            # Extract and format error message
            error_msg = '; '.join([error.get('message', 'Unknown error') for error in json_response['errors']])
            raise ValueError(f"GraphQL Error: {error_msg}")
            
        return json_response

    def search_anime(self, search_term):
        """
        Search for anime by title.
        
        Args:
            search_term (str): The title to search for
            
        Returns:
            AnimeMedia: An object containing the anime information, or None if not found
        """
        variables = {"search": search_term, "type": "ANIME"}
        response = self._make_request(ANIME_QUERY, variables)
        media_data = response.get("data", {}).get("Media", [])
        return AnimeMedia(media_data) if media_data else None
    
    def search_manga(self, search_term):
        """
        Search for manga by title.
        
        Args:
            search_term (str): The title to search for
            
        Returns:
            MangaMedia: An object containing the manga information, or None if not found
        """
        variables = {"search": search_term, "type": "MANGA"}
        response = self._make_request(MANGA_QUERY, variables)
        media_data = response.get("data", {}).get("Media", [])
        return MangaMedia(media_data) if media_data else None
    
    def get_anime_by_id(self, anime_id):
        """
        Get anime by its AniList ID.
        
        Args:
            anime_id (int): The AniList ID of the anime
            
        Returns:
            AnimeMedia: An object containing the anime information, or None if not found
        """
        variables = {"id": anime_id}
        response = self._make_request(ANIME_BY_ID_QUERY, variables)
        media_data = response.get("data", {}).get("Media", [])
        return AnimeMedia(media_data) if media_data else None
    
    def get_manga_by_id(self, manga_id):
        """
        Get manga by its AniList ID.
        
        Args:
            manga_id (int): The AniList ID of the manga
            
        Returns:
            MangaMedia: An object containing the manga information, or None if not found
        """
        variables = {"id": manga_id}
        response = self._make_request(MANGA_BY_ID_QUERY, variables)
        media_data = response.get("data", {}).get("Media", [])
        return MangaMedia(media_data) if media_data else None
    
    def search_anime_paged(self, search_term, page=1, per_page=10):
        """
        Search for anime with pagination.
        
        Args:
            search_term (str): The title to search for
            page (int): The page number to fetch
            per_page (int): The number of results per page
            
        Returns:
            dict: Contains 'page_info' and 'results' keys
        """
        variables = {
            "search": search_term,
            "page": page,
            "perPage": per_page
        }
        response = self._make_request(SEARCH_ANIME_PAGE_QUERY, variables)
        page_data = response.get("data", {}).get("Page", {})
        
        if not page_data:
            return {
                "page_info": None,
                "results": []
            }
        
        results = []
        for media in page_data.get("media", []):
            results.append(AnimeMedia(media))
            
        return {
            "page_info": page_data.get("pageInfo", {}),
            "results": results
        }
    
    def search_manga_paged(self, search_term, page=1, per_page=10):
        """
        Search for manga with pagination.
        
        Args:
            search_term (str): The title to search for
            page (int): The page number to fetch
            per_page (int): The number of results per page
            
        Returns:
            dict: Contains 'page_info' and 'results' keys
        """
        variables = {
            "search": search_term,
            "page": page,
            "perPage": per_page
        }
        response = self._make_request(SEARCH_MANGA_PAGE_QUERY, variables)
        page_data = response.get("data", {}).get("Page", {})
        
        if not page_data:
            return {
                "page_info": None,
                "results": []
            }
        
        results = []
        for media in page_data.get("media", []):
            results.append(MangaMedia(media))
            
        return {
            "page_info": page_data.get("pageInfo", {}),
            "results": results
        }
        
    def get_rate_limit_info(self):
        """
        Get the current rate limit information.
        
        Returns:
            dict: A dictionary containing rate limit information
        """
        return {
            "limit": self.rate_limit,
            "remaining": self.rate_limit_remaining
        }
    
if __name__ == "__main__":
    client = AnipieClient()
    search_term = "Naruto"
    anime_results = client.search_anime(search_term)
    # get title
    print(anime_results.title)
    
    # Rate limit info
    print(f"Rate limit: {client.get_rate_limit_info()}")

