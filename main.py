import pandas as pd  # Importing pandas for data manipulation
import numpy as np  # Importing numpy for numerical operations
import sklearn as skl  # Importing sklearn (though not explicitly used)

# Reading the dataset from a CSV file
with open('dataset.csv', mode='r') as f:
    movies = pd.read_csv('dataset.csv')  # Loading dataset into a pandas DataFrame
    
    # Creating a new column 'tags' by combining 'genre' and 'overview'
    movies['tags'] = movies['genre'] + movies['overview']
    
    # Selecting only relevant columns for recommendation
    new_df = movies[['id', 'title', 'tags']]

    from sklearn.feature_extraction.text import CountVectorizer  # Importing CountVectorizer for text processing
    cv = CountVectorizer(max_features=10000, stop_words='english')  # Limiting to 10,000 words and removing stopwords
    
    # Handling missing values and ensuring all tags are strings
    movies['tags'] = movies['tags'].fillna('').astype(str)
    
    # Converting text data into numerical feature vectors
    vec = cv.fit_transform(movies['tags']).toarray()

    from sklearn.metrics.pairwise import cosine_similarity  # Importing cosine similarity for similarity measurement
    
    # Calculating cosine similarity between movie tags
    similarity = cosine_similarity(vec)
    
    # Sorting movies based on similarity to the first movie in the dataset
    dist = sorted(list(enumerate(similarity[0])), reverse=True, key=lambda vec: vec[1])

    # Function to recommend similar movies based on the input movie title
    def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]  # Finding the index of the input movie
        
        # Sorting movies based on similarity to the input movie
        dist = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda vec: vec[1])
        
        # Printing the top 5 recommended movies (excluding the input movie itself)
        for i in dist[1:6]:
            suggested_movies = movies.iloc[i[0]].title
            print(suggested_movies)

    # Taking user input for movie recommendation
    user_input = input('Enter the movie you want to watch: ')
    recommend(user_input)  # Calling the recommend function
