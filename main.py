import pandas as pd
import numpy as np
import sklearn as skl

with open('dataset.csv', mode='r') as f:
    movies =pd.read_csv('dataset.csv')
    movies['tags'] =movies ['genre'] + movies['overview']
    new_df = movies [['id','title','tags']]

    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(max_features=10000,stop_words='english')
    movies['tags'] = movies['tags'].fillna('').astype(str)
    vec = cv.fit_transform(movies['tags']).toarray()

    from sklearn.metrics.pairwise import cosine_similarity
    similarity = cosine_similarity(vec)
    dist = sorted(list(enumerate(similarity[0])),reverse=True,key = lambda vec:vec[1])

    def recommend(movie):
        movie_index = movies[movies['title']==movie].index[0]
        dist = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda vec:vec[1])
        for i in dist[1:6]:
            suggested_movies = (movies.iloc[i[0]].title)
            print(suggested_movies)

    user_input = input('Enter the movie you want to watch: ')
    recommend(user_input)        

