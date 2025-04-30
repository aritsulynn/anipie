import requests

class AnimeMedia:
    """Class to represent an anime media object."""

    def __init__(self, media):
        """Initialize the AnimeMedia object with media data."""
        self._media = media

    @property
    def id(self):
        """Get the ID of the media."""
        return self._media.get("id")
    
    @property
    def title(self):
        """Get the title of the media."""
        return self._media.get("title", {}).get("romaji")
    
    @property
    def english_title(self):
        """Get the English title of the media."""
        return self._media.get("title", {}).get("english")
    
    @property
    def native_title(self):
        """Get the native title of the media."""
        return self._media.get("title", {}).get("native")
    
    @property
    def status(self):
        """Get the status of the media."""
        return self._media.get("status")
    
    @property
    def description(self):
        """Get the description of the media."""
        return self._media.get("description")
    
    @property
    def episodes(self):
        """Get the number of episodes of the media."""
        return self._media.get("episodes")
    
    @property
    def cover_large(self):
        """Get the large cover image of the media."""
        return self._media.get("coverImage", {}).get("large")
    
    @property
    def site_url(self):
        """Returns the site url of the anime."""
        return self._media.get("siteUrl")
    
    @property
    def genres(self):
        """Returns the genres of the anime."""
        genres = self._media.get("genres", [])
        return ", ".join(genres) if genres else None

    def __handle_date(self, date) -> str:
        """Handle the date."""
        if not date:
            return None

        month = date.get("month")
        day = date.get("day")
        year = date.get("year")

        return (
            f"{month}/{day}/{year}"
            if month is not None and day is not None and year is not None
            else None
        )
    
    @property
    def start_date(self):
        """Get the start date of the media."""
        return self.__handle_date(self._media.get("startDate"))
    
    @property
    def end_date(self):
        """Get the end date of the media."""
        return self.__handle_date(self._media.get("endDate"))
    
    @property
    def average_score(self):
        """Get the average score of the media."""
        average_score = self._media.get("averageScore")
        return (int(average_score) / 10) if average_score else None
    
    @property
    def season(self):
        """Get the season of the media."""
        return self._media.get("season")
    
    @property
    def format(self):
        """Get the format of the anime (e.g., TV, MOVIE)."""
        return self._media.get("format")
    
    @property
    def duration(self):
        """Get the duration of each episode in minutes."""
        return self._media.get("duration")
    
    @property
    def studios(self):
        """Get the studios that produced the anime."""
        if not self._media.get("studios", {}).get("nodes"):
            return None
            
        studios_list = []
        for node in self._media.get("studios", {}).get("nodes", []):
            studios_list.append({
                "id": node.get("id"),
                "name": node.get("name")
            })
        return studios_list
    
    @property
    def is_adult(self):
        """Check if the anime is marked as adult content."""
        return self._media.get("isAdult", False)

