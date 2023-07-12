from anipie import SearchAnime, SearchManga

def testSearchAnime(name):
    anime = SearchAnime(name)

    print(anime.getAnimeData())
    # print(anime.getAnimeID())
    print(anime.getAnimeEnglishName())
    print(anime.getAnimeRomajiName())
    print(anime.getAnimeDescription())
    print(anime.getAnimeEpisodes())
    print(anime.getAnimeStatus())
    print(anime.getAnimeStartDate())
    print(anime.getAnimeEndDate())
    print(anime.getAnimeAverageScore())
    print(anime.getAnimeGenres())
    print(anime.getAnimeCoverImage())
    print(anime.getAnimeSiteUrl())
    print(anime.getAnimeSeason())
    print(anime.getAnimeFormat())

print("=========================================")

def testSearchManga(name):
    manga = SearchManga(name)
    # print(manga.getMangaData())
    print(manga.getMangaEnglishName())
    print(manga.getMangaRomajiName())
    print(manga.getMangaDescription())
    print(manga.getMangaStatus())
    print(manga.getMangaStartDate())
    print(manga.getMangaEndDate())
    print(manga.getMangaAverageScore())
    print(manga.getMangaGenres())
    print(manga.getMangaCoverImage())
    print(manga.getMangaSiteUrl())
    print(manga.getMangaChapters())
    print(manga.getMangaVolumes())
    print(manga.getMangaFormat())

    print("=========================================")
