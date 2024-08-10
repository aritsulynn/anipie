import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from anipie import SearchByQuery, SearchByID, information

# search = SearchByQuery("Honey Lemon Soda", "manga")
# search = SearchByQuery(title="2.5 Jigen no Ririsa", type="manga")
# print(search.get_start_date)
# print(search.get_end_date)

search = SearchByID(1, "anime")
print(search.get_id)

search2 = SearchByQuery("Honey Lemon Soda", "manga")
print(search2.get_cover_image_url)
