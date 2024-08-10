import re
import requests
from anipie.information import Information
from anipie.queries import ANIME_QUERY, MANGA_QUERY, ANIME_API_URL


class SearchByQuery(Information):
    """A class that searches for an anime or manga by query."""

    def __init__(self, title, type="ANIME"):
        """Initialize the class."""
        self._title = title
        self._type = type.upper()
        if self._type not in ["ANIME", "MANGA"]:
            raise ValueError("Type must be either 'ANIME' or 'MANGA'")
        self._search()

    def _search(self) -> None:
        """Perform the search for the anime."""
        variables = {
            "search": self._title,
            "type": self._type,
        }
        query = ANIME_QUERY if self._type == "ANIME" else MANGA_QUERY
        try:
            response = requests.post(
                ANIME_API_URL,
                json={"query": query, "variables": variables},
                timeout=1,
                verify=True,
            )
            self._response = response.json()
            self._media = self._response.get("data").get("Media")
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            raise SystemExit(errh)
        except requests.exceptions.ReadTimeout as errrt:
            raise TimeoutError(errrt)
        except requests.exceptions.ConnectionError as conerr:
            raise ConnectionError(conerr)
        except requests.exceptions.RequestException as errex:
            raise RuntimeError(errex)
