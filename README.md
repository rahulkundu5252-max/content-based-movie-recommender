# Movie Recommender System

A content-based movie recommender system built with Python, 
Streamlit and TMDB API that suggests similar movies based on your selection.

## Features
- Select any movie from 5000+ movies
- Get 5 similar movie recommendations
- Shows movie posters fetched from TMDB API

## Tech Stack
- Python
- Streamlit
- Pandas
- Scikit-learn (CountVectorizer, Cosine Similarity)
- TMDB API

## How to Run
1. Install dependencies: pip install -r requirements.txt
2. Run: streamlit run app.py

## ⚠️ Note
The `movies.pkl` and `similarity.pkl` files are not included 
in this repo due to GitHub's file size limit (176MB).

To generate them locally:
1. Download the dataset from Kaggle:
   https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
2. Run `main.ipynb` notebook first
3. It will generate movies.pkl and similarity.pkl automatically
4. Then run: streamlit run app.py