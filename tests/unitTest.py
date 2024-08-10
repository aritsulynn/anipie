import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from anipie.search_by_query import SearchByQuery

# , SearchManga
import re
import unittest
from unittest.mock import patch, Mock


# didn't update yet
class TestSearchByQuery(unittest.TestCase):
    """Test the SearchByQuery class."""

    def setUp(self):
        """Set up the test."""
        self.anime_test_response = {
            "data": {
                "Media": {
                    "id": 97832,
                    "title": {"romaji": "citrus", "english": "Citrus"},
                    "status": "FINISHED",
                    "description": "Fashionable and friendly Yuzu Aihara is ready to face her brand-new school and find her first love. The only problem? It's an all-girls' school. Determined to make a good impression and lots of friends, Yuzu puts on her best looks—only to wind up in trouble on day-one! After a close encounter by the beautiful yet harsh student council president Mei and having her phone confiscated, Yuzu is losing hope that this will be a perfect high school story. But nothing compares to the shock when she gets home to find out Mei is her brand-new stepsister—who suddenly kisses her! With her heart beating wildly and her emotions a complete mess, Yuzu wonders something: Is she falling for Mei?<br>\n<br>\nTorn between being a good stepsister and dealing with her feelings, Yuzu does everything she can to become close to Mei. But can she melt the ice around Mei's heart and heal the pain she hides?<br><br>\n\n(Source: Funimation)",
                    "averageScore": 60,
                    "startDate": {"year": 2018, "month": 1, "day": 6},
                    "endDate": {"year": 2018, "month": 3, "day": 24},
                    "coverImage": {
                        "large": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/nx97832-XPMLlgFULgJW.jpg"
                    },
                    "genres": ["Drama", "Romance"],
                    "siteUrl": "https://anilist.co/anime/97832",
                    "episodes": 12,
                    "season": "WINTER",
                    "format": "TV",
                }
            }
        }

        self.manga_test_response = {
            "data": {
                "Media": {
                    "id": 80145,
                    "title": {"romaji": "citrus", "english": "Citrus"},
                    "status": "FINISHED",
                    "description": "Yuzuko Aihara, a high school girl whose main interests are fashion, friends and having fun, is about to get a reality check. Due to her mom’s remarriage, Yuzu has transferred to a new, all-girls school that is extremely strict. Her real education is about to begin.\n<br><br>\nFrom Day One, happy-go-lucky Yuzu makes enemies, namely the beautiful yet stern Student Council President Mei. So what happens when a dejected Yuzu returns home and discovers the shock of her life: that Mei is actually her new step-sister who has come to live with her? Even more surprising, when Mei catches Yuzu off-guard and kisses her out of the blue, what does it all mean?\n<br><br>\n(Source: Seven Seas Entertainment)\n<br><br>\n<i>Note: Includes 9 bonus chapters.</i>",
                    "averageScore": 70,
                    "startDate": {"year": 2012, "month": 11, "day": 17},
                    "endDate": {"year": 2018, "month": 8, "day": 18},
                    "coverImage": {
                        "large": "https://s4.anilist.co/file/anilistcdn/media/manga/cover/medium/nx80145-PeU7lVLC4d4Z.jpg"
                    },
                    "genres": ["Drama", "Romance"],
                    "siteUrl": "https://anilist.co/manga/80145",
                    "chapters": 50,
                    "volumes": 10,
                    "format": "MANGA",
                }
            }
        }

    def assert_search_results(self, query, test_response):
        """Assert common search results for anime or manga."""

        self.assertEqual(query.get_raw_data(), test_response)
        test_response = test_response.get("data").get("Media")
        self.assertEqual(
            query.get_romanji_name, test_response.get("title").get("romaji")
        )
        self.assertEqual(
            query.get_english_name, test_response.get("title").get("english")
        )
        self.assertEqual(query.get_status, test_response.get("status"))
        self.assertEqual(
            query.get_description,
            (re.sub(re.compile("<.*?>"), "", test_response.get("description"))),
        )
        self.assertEqual(query.get_episodes, test_response.get("episodes"))
        self.assertEqual(
            query.get_cover_image_url, test_response.get("coverImage").get("large")
        )
        self.assertEqual(query.get_genres, ", ".join(test_response.get("genres")))
        self.assertEqual(query.get_site_url, test_response.get("siteUrl"))
        self.assertEqual(
            query.get_start_date,
            str(test_response.get("startDate").get("month"))
            + "/"
            + str(test_response.get("startDate").get("day"))
            + "/"
            + str(test_response.get("startDate").get("year")),
        )
        self.assertEqual(
            query.get_end_date,
            str(test_response.get("endDate").get("month"))
            + "/"
            + str(test_response.get("endDate").get("day"))
            + "/"
            + str(test_response.get("endDate").get("year")),
        )
        self.assertEqual(query.get_avg_score, test_response.get("averageScore") / 10)
        self.assertEqual(query.get_season, test_response.get("season"))
        self.assertEqual(query.get_format, test_response.get("format"))
        self.assertEqual(query.get_id, test_response.get("id"))
        self.assertEqual(query.get_chapters, test_response.get("chapters"))
        self.assertEqual(query.get_volumes, test_response.get("volumes"))

    def test_search_anime_by_query(self):
        """Test the search anime by query."""
        query = SearchByQuery("Citrus", "anime")
        self.assert_search_results(query, self.anime_test_response)

    def test_search_manga_by_query(self):
        """Test the search manga by query."""
        query = SearchByQuery("Citrus", "manga")
        self.assert_search_results(query, self.manga_test_response)


if __name__ == "__main__":
    unittest.main()
