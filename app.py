import pickle
import requests
import streamlit as st

# Load data
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))

OMDB_API_KEY = "58287a73"

def fetch_movie_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['Poster'] if data.get('Response') == 'True' and data.get('Poster') != 'N/A' else None
    except:
        return None

def recommend(movie_title):
    if movie_title not in movies['title'].values:
        return []

    index = movies[movies['title'] == movie_title].index[0]
    distances = list(enumerate(similarity[index]))
    sorted_distances = sorted(distances, reverse=True, key=lambda x: x[1])
    recommended = []
    for i in sorted_distances[1:6]:
        title = movies.iloc[i[0]].title
        poster = fetch_movie_poster(title)
        recommended.append((title, poster))
    return recommended

# Streamlit UI
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    if recommendations:
        cols = st.columns(5)
        for i, (title, poster) in enumerate(recommendations):
            with cols[i]:
                st.text(title)
                if poster:
                    st.image(poster, use_container_width=True)
                else:
                    st.text("No Poster")
    else:
        st.error("No recommendations found.")
