import streamlit as st
import joblib
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=fbb18fe9735d1a3e0ad1531398ed1b13'.format(movie_id))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+ data['poster_path']


movies_list=joblib.load(open('movies.joblib','rb'))

def recommend(movies_list,movie):
    movie_index=movies_list[movies_list['title']== movie].index[0]
    distances=similarity[movie_index]
    movie_list= sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id= movies_list.iloc[i[0]].id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        ##fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters




similarity=joblib.load(open('similarity.joblib','rb'))

st.title('Movie Recommender System')

selected_movie_name= st.selectbox(
    'What do you want to see?',
    movies_list['title'].values
)

if st.button('Recommend'):
    names,posters=recommend(movies_list,selected_movie_name)
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