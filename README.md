# Movie Recommender System

A content-based movie recommender system built with Python, Streamlit and TMDB API that suggests similar movies based on your selection.

## Live Demo
https://content-based-movie-recommender-kxfa9wcru23so6gkd7yu6k.streamlit.app

## Features

🎥 Massive Movie Library — Browse and select from a collection of 5000+ movies.
🤖 Smart Recommendations — Get 5 personalized similar movie suggestions instantly based on content similarity.
🖼️ Live Movie Posters — Posters are fetched in real time from the TMDB API for a rich visual experience.


## How It Works
The recommender uses a content-based filtering approach — it analyzes what a movie is about rather than relying on user ratings or watch history.

Data Preprocessing — Merges the movies and credits datasets, then extracts key attributes including genres, keywords, cast, crew, and plot overview.
Tag Generation — Combines all extracted features into a single unified tags column per movie, creating a rich text representation of each film.
Vectorization — Uses CountVectorizer from Scikit-learn to convert the tags into numerical feature vectors with a vocabulary of 5000 features.
Similarity Computation — Calculates Cosine Similarity between all movie vectors to measure how closely related any two movies are.
Recommendation — When you pick a movie, the system finds the 5 movies with the highest cosine similarity scores and returns them as recommendations.


## Dataset
DetailInfoSourceTMDB 5000 Movie DatasetPlatformKaggleFilestmdb_5000_movies.csv and tmdb_5000_credits.csvTotal Movies~5000

Tech Stack
TechnologyRolePythonCore programming languageStreamlitFrontend web interface for the appPandasData loading, merging, and preprocessingScikit-learnCountVectorizer and Cosine Similarity computationNLTKNatural language processing for tag cleaning and stemmingTMDB APIFetching live movie posters for recommendations

## Run Locally
Follow these steps to set up and run the project on your machine:
bash.
## 1. Clone the repository
git clone <your-repo-url>
cd <repo-folder>

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py

## Note: movies.pkl and similarity.pkl are auto-generated on the first run from the CSV files. This may take a moment — subsequent runs will load much faster from the cached pickle files.


Author
Rahul Kundu