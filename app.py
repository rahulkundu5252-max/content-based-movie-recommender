import os
import ast
import pandas as pd
import streamlit as st
import pickle
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem.porter import PorterStemmer
 

@st.cache_resource(show_spinner="🎬 Setting up for first time... please wait!")
def load_model():
    # ── If pkl files already exist, just load them
    if os.path.exists('movies.pkl') and os.path.exists('similarity.pkl'):
        movies     = pickle.load(open('movies.pkl', 'rb'))
        similarity = pickle.load(open('similarity.pkl', 'rb'))
        return movies, similarity
 
    movies_df = pd.read_csv('tmdb_5000_movies.csv')
    credits_df = pd.read_csv('tmdb_5000_credits.csv')
 
    movies_df = movies_df.merge(credits_df, on='title')
 
    movies_df = movies_df[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
    movies_df.dropna(inplace=True)
 
    
    def convert(obj):
        return [i['name'] for i in ast.literal_eval(obj)]
 
    def convert_cast(obj):
        return [i['name'] for i in ast.literal_eval(obj)[:3]]
 
    def fetch_director(obj):
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                return [i['name']]
        return []
 
    movies_df['genres']   = movies_df['genres'].apply(convert)
    movies_df['keywords'] = movies_df['keywords'].apply(convert)
    movies_df['cast']     = movies_df['cast'].apply(convert_cast)
    movies_df['crew']     = movies_df['crew'].apply(fetch_director)
    movies_df['overview'] = movies_df['overview'].apply(lambda x: x.split())
 
    
    for col in ['genres', 'keywords', 'cast', 'crew']:
        movies_df[col] = movies_df[col].apply(lambda x: [i.replace(" ", "") for i in x])
 
    # Build tags
    movies_df['tags'] = (
        movies_df['overview'] +
        movies_df['genres'] +
        movies_df['keywords'] +
        movies_df['cast'] +
        movies_df['crew']
    )
 
    new_df = movies_df[['movie_id', 'title', 'tags']].copy()
    new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x).lower())
 
    # Stem tags
    nltk.download('punkt', quiet=True)
    ps = PorterStemmer()
    new_df['tags'] = new_df['tags'].apply(
        lambda x: " ".join(ps.stem(w) for w in x.split())
    )
 
    # Vectorize & compute similarity
    cv  = CountVectorizer(max_features=5000, stop_words='english')
    vec = cv.fit_transform(new_df['tags']).toarray()
    similarity = cosine_similarity(vec)
 
    # Save pkl files
    pickle.dump(new_df, open('movies.pkl', 'wb'))
    pickle.dump(similarity, open('similarity.pkl', 'wb'))
 
    return new_df, similarity
 
 
# 2. FETCH POSTER

def fetch_poster(movie_id):
    try:
        url  = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3b4852b9dcf3902e330382fb95a72fef"
        data = requests.get(url, timeout=5).json()
        poster_path = data.get('poster_path')
        if not poster_path:
            return "https://via.placeholder.com/500x750?text=No+Poster"
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception as e:
        print(f"Error: {e}")
        return "https://via.placeholder.com/500x750?text=No+Poster"
 
 
# 3. RECOMMEND

def recommend(movie, movies, similarity):
    movie_index = movies[movies['title'] == movie].index[0]
    distances   = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
 
    recommended_movies  = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
 
    return recommended_movies, recommended_posters
 
 

st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title('🎬 Movie Recommender System')
 
# Load model (cached — only runs once)
movies, similarity = load_model()
 
selected_movie = st.selectbox('Select a movie', movies['title'].values)
 
if st.button('Recommend'):
    names, posters = recommend(selected_movie, movies, similarity)
    col1, col2, col3, col4, col5 = st.columns(5)
    for col, name, poster in zip([col1, col2, col3, col4, col5], names, posters):
        with col:
            st.text(name)
            st.image(poster)