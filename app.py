import os
import streamlit as st
import pickle
import requests

# Auto-generate pkl files if missing
if not os.path.exists('movies.pkl') or not os.path.exists('similarity.pkl'):
    st.warning("Setting up for first time... please wait!")
    exec(open('setup.py').read())

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3b4852b9dcf3902e330382fb95a72fef"
        data = requests.get(url, timeout=5).json()
        poster_path = data.get('poster_path')
        if not poster_path:
            return "https://via.placeholder.com/500x750?text=No+Poster"
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception as e:
        print(f"Error: {e}")
        return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])