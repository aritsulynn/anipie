"""
GraphQL queries for the AniList API.
Based on official AniList GraphQL API documentation.
"""

ANIME_QUERY = """
query ($search: String! $type: MediaType!) { 
            Media (search: $search type: $type) { 
                id
                title {
                    romaji
                    english
                    native
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
                season
                format
                duration
                studios {
                    nodes {
                        id
                        name
                    }
                }
                isAdult
            }
        }
"""

MANGA_QUERY = """
query ($search: String! $type: MediaType!) { 
    Media (search: $search type: $type) { 
        id
        title {
            romaji
            english
            native
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
        format
        staff {
            edges {
                role
                node {
                    id
                    name {
                        full
                    }
                }
            }
        }
    }
}
"""

ANIME_BY_ID_QUERY = """
query ($id: Int!) { 
    Media (id: $id type: ANIME) { 
        id
        title {
            romaji
            english
            native
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
        season
        format
        duration
        studios {
            nodes {
                id
                name
            }
        }
    }
}
"""

MANGA_BY_ID_QUERY = """
query ($id: Int!) { 
    Media (id: $id type: MANGA) { 
        id
        title {
            romaji
            english
            native
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
        format
    }
}
"""

SEARCH_ANIME_PAGE_QUERY = """
query ($search: String!, $page: Int = 1, $perPage: Int = 10) {
    Page(page: $page, perPage: $perPage) {
        pageInfo {
            hasNextPage
            total
            perPage
            currentPage
            lastPage
        }
        media(search: $search, type: ANIME) {
            id
            title {
                romaji
                english
                native
            }
            format
            status
            description
            averageScore
            coverImage {
                large
            }
        }
    }
}
"""

SEARCH_MANGA_PAGE_QUERY = """
query ($search: String!, $page: Int = 1, $perPage: Int = 10) {
    Page(page: $page, perPage: $perPage) {
        pageInfo {
            hasNextPage
            total
            perPage
            currentPage
            lastPage
        }
        media(search: $search, type: MANGA) {
            id
            title {
                romaji
                english
                native
            }
            format
            status
            description
            averageScore
            coverImage {
                large
            }
            chapters
            volumes
        }
    }
}
"""
