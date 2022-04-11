from searchAnime import SearchAnime as sa
from searchManga import SearchManga as sm
from searchUser import SearchUser as su

# s = sa('one piece')


print("=========================================")

# anime = sa('Citrus')

# # print(anime.getAnimeData())
# print(anime.getAnimeEnglishName())
# print(anime.getAnimeRomajiName())
# print(anime.getAnimeDescription())

# print(anime.getAnimeEpisodes())
# print(anime.getAnimeStatus())
# print(anime.getAnimeStartDate())
# print(anime.getAnimeEndDate())
# print(anime.getAnimeAverageScore())
# print(anime.getAnimeGenres())
# print(anime.getAnimeCoverImage())
# print(anime.getAnimeSiteUrl())

print("=========================================")

# manga = sm('Citrus')

# # print(manga.getMangaData())
# print(manga.getMangaEnglishName()) # 1
# print(manga.getMangaRomajiName())   #2
# print(manga.getMangaDescription()) 
# print(manga.getMangaStatus())
# print(manga.getMangaStartDate())
# print(manga.getMangaEndDate())
# print(manga.getMangaAverageScore())
# print(manga.getMangaGenres())
# print(manga.getMangaCoverImage())
# print(manga.getMangaSiteUrl())
# print(manga.getMangaChapters())
# print(manga.getMangaVolumes())

print("=========================================")

user = su('Rintsu')
# print(user.getUserData())
print(user.getUserAvatar())
print(user.getUserAbout())
print(user.getUserName())
print(user.getUserFavouritesAnime())
print(user.getUserFavouritesManga())

print("=========================================")