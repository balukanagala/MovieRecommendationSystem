# flask can be used
# but we use streamlit, it is a library, work will be easier
# importing pickle to load file
import streamlit as st
import pickle as pi
import numpy as np
import pandas as pd

def recommend(movie):
  movie_index = movies.loc[movies.title==movie].index[0]
  similarity_rates = similarity[movie_index]
  sorted_similarity_rates = sorted(similarity_rates,reverse=True)
  top5_similar_rate = sorted_similarity_rates[1:6]
  rec_movies = []
  for similar_rate in top5_similar_rate:
    rec_movie_id = np.where(similarity_rates == similar_rate)[0][0]
    rec_movies.append(movies.iloc[rec_movie_id].title)
  return rec_movies

#Title of our WebApp
st.title('Movie Recommender System')

#Loading the movies_dict as Loading a dataframe did not work
movies_dict = pi.load(open('movie_dict.pkl','rb'))

# loading similarity array(check what is it)
similarity = pi.load(open('similarity.pkl','rb'))

#converting a dict to dataframe
movies = pd.DataFrame(movies_dict)

selected_movie_name = st.selectbox(
    'Select a Movie',
    movies['title'].values
)

if st.button('Recommend'):
    recommended_movies = recommend(selected_movie_name)
    for i in range(5):
      st.write(recommended_movies[i])
    st.write("**Note : This Machine Learning model is trained on less amount of data**")