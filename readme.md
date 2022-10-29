# Anipie

<img src="https://anilist.co/img/icons/android-chrome-512x512.png" width="128"/> 

> A wrapper for the AniList API

## Installation
```
pip install anipie
```

## Usage

  #### Example Code
  
  ```
  import anipie

  citrus = anipie.SearchAnime("Citrus")
  des = citrus.getAnimeDescription() # you can learn more in searchAnime.py, searchManga.py
  print(des)
  ```

  #### Output
  ```
Fashionable and friendly Yuzu Aihara is ready to face her brand-new school and find her first love. The only problem? It's an all-girls' school. Determined to make a good impression and lots of friends, Yuzu puts on her best looks—only to wind up in trouble on day-one! After 
a close encounter by the beautiful yet harsh student council president Mei and having her phone confiscated, Yuzu is losing hope that this will be a perfect high school story. But nothing compares to the shock when she gets home to find out Mei is her brand-new stepsister—who suddenly kisses her! With her heart beating wildly and her emotions 
a complete mess, Yuzu wonders something: Is she falling for Mei?     

Torn between being a good stepsister and dealing with her feelings, Yuzu does everything she can to become close to Mei. But can she melt 
the ice around Mei's heart and heal the pain she hides?

(Source: Funimation)
  ```
