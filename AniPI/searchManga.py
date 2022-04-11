import requests

class SearchManga:
    
    def __init__(self, search):
        self.search = search
        self.response = None
        self.mangaSearch()

    def mangaSearch(self):
        self.query = '''
        query ($search: String! $type: MediaType!) { 
        Media (search: $search type: $type) { 
            id
            title {
                romaji
                english
            }
            status
            description
            averageScore
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
            coverImage {
                large  
            }
            genres
            siteUrl
            chapters
            volumes
        }
        }
        '''
        self.variables = {
            'search' : self.search,
            'type' : 'MANGA',
        }
        self.url = 'https://graphql.anilist.co'
        self.response = requests.post(self.url, json={'query': self.query, 'variables': self.variables})

    def getMangaData(self):
        return self.response.json()

    def getMangaRomajiName(self):
        return self.response.json()['data']['Media']['title']['romaji']
    
    def getMangaEnglishName(self):
        return self.response.json()['data']['Media']['title']['english']

    def getMangaStatus(self):
        return self.response.json()['data']['Media']['status']
    
    def getMangaDescription(self):
        des = self.response.json()['data']['Media']['description']
        for i in (('<br>',''), ('<i>', ''), ('</i>', ''), ('<br/>', '')):
          des = des.replace(*i)

        if len(des) > 800:
          des = des[:800] + "..."
        return  des

    def getMangaStartDate(self):
        if self.response.json()['data']['Media']['startDate'] == None:
            return "N/A"
        else:
            media = self.response.json()['data']['Media']
            yearStart = media['startDate']['year']
            monthStart = media['startDate']['month']
            dayStart = media['startDate']['day']
            return str(monthStart) + '/' + str(dayStart) + '/' + str(yearStart)

    def getMangaEndDate(self):
        if self.response.json()['data']['Media']['endDate'] == None:
            return "N/A"
        else:
            media = self.response.json()['data']['Media']
            yearEnd = media['endDate']['year']
            monthEnd = media['endDate']['month']
            dayEnd = media['endDate']['day']
            return str(monthEnd) + '/' + str(dayEnd) + '/' + str(yearEnd)

    def getMangaCoverImage(self):
        return self.response.json()['data']['Media']['coverImage']['large']

    def getMangaGenres(self):
        genres = self.response.json()['data']['Media']['genres']
        genres = ", ".join(genres)
        return genres
    
    def getMangaSiteUrl(self):
        return self.response.json()['data']['Media']['siteUrl']

    def getMangaVolumes(self):
        if self.response.json()['data']['Media']['volumes'] == None:
            return "N/A"
        return self.response.json()['data']['Media']['volumes']

    def getMangaChapters(self):
        if self.response.json()['data']['Media']['chapters'] == None:
            return "N/A"
        return self.response.json()['data']['Media']['chapters']

    def getMangaAverageScore(self):
        return int(self.response.json()['data']['Media']['averageScore']) / 10
