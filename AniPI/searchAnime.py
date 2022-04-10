import requests

class SearchAnime:

    def __init__(self, search):
        self.search = search
        self.animeSearch()


    def animeSearch(self):
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
                episodes
            }
        }
        '''
        self.variables = {
            'search' : self.search,
            'type' : 'ANIME',
        }
        self.url = 'https://graphql.anilist.co'
        self.response = requests.post(self.url, json={'query': self.query, 'variables': self.variables})
    

    def getAnimeData(self):
        return self.response.json()

    def getAnimeRomajiName(self):
        return self.response.json()['data']['Media']['title']['romaji']

    def getAnimeEnglishName(self):
        return self.response.json()['data']['Media']['title']['english']
    
    def getAnimeStatus(self):
        return self.response.json()['data']['Media']['status']
    
    def getAnimeDescription(self):
        des = self.response.json()['data']['Media']['description']
        for i in (('<br>',''), ('<i>', ''), ('</i>', ''), ('<br/>', '')):
          des = des.replace(*i)

        if len(des) > 800:
          des = des[:800] + "..."
        return  des
    
    def getAnimeEpisodes(self):
        return self.response.json()['data']['Media']['episodes']

    def getAnimeCoverImage(self):
        return self.response.json()['data']['Media']['coverImage']['large']
    
    def getAnimeGenres(self):
        genres = self.response.json()['data']['Media']['genres']
        genres = ", ".join(genres)
        return genres
    
    def getAnimeSiteUrl(self):
        return self.response.json()['data']['Media']['siteUrl']

    def getAnimeStartDate(self):
        if self.response.json()['data']['Media']['startDate'] == None:
            return "Unknown"
        else:
            media = self.response.json()['data']['Media']
            yearStart = media['startDate']['year']
            monthStart = media['startDate']['month']
            dayStart = media['startDate']['day']
            return str(monthStart) + '/' + str(dayStart) + '/' + str(yearStart)

    def getAnimeEndDate(self):
        if self.response.json()['data']['Media']['endDate'] == None:
            return "Unknown"
        else:
            media = self.response.json()['data']['Media']
            yearEnd = media['endDate']['year']
            monthEnd = media['endDate']['month']
            dayEnd = media['endDate']['day']
            return str(monthEnd) + '/' + str(dayEnd) + '/' + str(yearEnd)

    def getAnimeAverageScore(self):
        return int(self.response.json()['data']['Media']['averageScore']) / 10
