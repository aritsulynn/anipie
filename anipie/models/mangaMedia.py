import requests

class MangaMedia:
    """Class to represent a manga media object."""

    def __init__(self, media):
        """Initialize the MangaMedia object with media data."""
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
    def cover_large(self):
        """Get the large cover image of the media."""
        return self._media.get("coverImage", {}).get("large")
    
    @property
    def site_url(self):
        """Returns the site url of the manga."""
        return self._media.get("siteUrl")
    
    @property
    def genres(self):
        """Returns the genres of the manga."""
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
    def chapters(self) -> int:
        """Returns the number of chapters of the manga."""
        return self._media.get("chapters") or None

    @property
    def volumes(self) -> int:
        """Returns the number of volumes of the manga."""
        return self._media.get("volumes") or None
    
    @property
    def format(self) -> str:
        """Returns the format of the manga (e.g., MANGA, ONE_SHOT)."""
        return self._media.get("format") or None
    
    @property
    def staff(self) -> list:
        """Returns the staff (creators) of the manga."""
        if not self._media.get("staff", {}).get("edges"):
            return None
            
        staff_list = []
        for edge in self._media.get("staff", {}).get("edges", []):
            staff_list.append({
                "role": edge.get("role"),
                "name": edge.get("node", {}).get("name", {}).get("full")
            })
        return staff_list