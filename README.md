# Movie Recommender System

A content-based movie recommender system built with Python, Streamlit and TMDB API that suggests similar movies based on your selection.

## Live Demo
https://content-based-movie-recommender-kxfa9wcru23so6gkd7yu6k.streamlit.app

## Features
- Select any movie from 5000+ movies
- Get 5 similar movie recommendations with posters
- Movie posters fetched live from TMDB API

## How It Works
1. Data Preprocessing - Merges movie and credits datasets, extracts genres, keywords, cast, crew and overview
2. Tag Generation - Combines all features into a single tags column per movie
3. Vectorization - Uses CountVectorizer to convert tags into 5000 feature vectors
4. Similarity - Computes Cosine Similarity between all movie vectors
5. Recommendation - Finds the 5 most similar movies based on cosine similarity score

## Dataset
- Source: TMDB 5000 Movie Dataset from Kaggle
- Link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
- Files: tmdb_5000_movies.csv and tmdb_5000_credits.csv
- Total movies: 5000

## Tech Stack
- Python, Streamlit, Pandas, Scikit-learn, NLTK, TMDB API

## How to Run Locally
1. Clone the repo
2. pip install -r requirements.txt
3. streamlit run app.py

## Note
movies.pkl and similarity.pkl are auto-generated on first run from the CSV files.
