import requests
from typing import Union

from anipie.information import Information


class SearchByID(Information):

    def __init__(self, id: int, type: str = "ANIME") -> None:
        """Initialize the class."""
        self._id = id
        self._type = type.upper()
        if self._type not in ["ANIME", "MANGA"]:
            raise ValueError("Type must be either 'ANIME' or 'MANGA'")
        self._search()

    def _search(self) -> None:
        variables = {
            "id": self._id,
            "type": self._type,
        }
        query = """
        query ($id: Int, $type: MediaType) {
            Media(id: $id, type: $type) {
                id
                title {
                    romaji
                    english
                }
                type
                status
                description
                episodes
                chapters
                volumes
                coverImage {
                    extraLarge
                }
                genres
                siteUrl
                startDate {
                    year
                    month
                    day
                }
                endDate {
                    year
                    month
                    day
                }
                averageScore
                season
                format
            }
        }
        """
        try:
            response = requests.post(
                "https://graphql.anilist.co",
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
