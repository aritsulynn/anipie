# from .searchAnime import SearchAnime
# from .searchManga import SearchManga

from .search_by_query import SearchByQuery
from . import exceptions
from .exceptions import QueryTypeError, TitleNotFoundError

# Explicity export these when someone uses
# from anipie import *
__all__ = [
    "SearchByQuery",
    # exporting the module so the exceptions can be accessed as such:
    # from anipie.exceptions import TitleNotFoundError
    "exceptions",
    # Exporting the exceptions individually so they are also available as:
    # from anipie import TitleNotFoundError
    "QueryTypeError",
    "TitleNotFoundError",
]
