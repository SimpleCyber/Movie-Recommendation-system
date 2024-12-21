import pandas as pd
import streamlit as st
import pickle
import requests
import ast
import os
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster_path (obj):
    L=[]
    for i in ast.literal_eval(obj) : 
        if i['poster_path']:    
            L.append(i['name']) 
    return L

def recmmond(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recmmonded_movies = []
    recmmonded_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        print("mooooooooovie is",movie_id,"\n")
        # fetch poster from tmdb
        recmmonded_movies.append(movies.iloc[i[0]].title)
        recmmonded_movies_poster.append(ferch_poster(movie_id))
    return recmmonded_movies, recmmonded_movies_poster



def ferch_poster(movie_id):
    try:
        url = 'https://api.themoviedb.org/3/movie/{}?api_key=1f4efd04a20fb47cd4021f041fac3679&language=en-US'.format(movie_id)
        data = requests.get(url)
        data.raise_for_status()  # This will raise an exception for HTTP error codes
        data = data.json()
        #print ing path
        print("poster path from jason:",data['poster_path'],"\n")
        poster_path = data['poster_path']
        full_poster_path = 'https://image.tmdb.org/t/p/w500' + poster_path
        #print ing path
        print("full poster path :",full_poster_path,"\n")
        return full_poster_path
    except requests.exceptions.RequestException as e:
        # print(f"Error fetching poster for movie {movie_id}: {e}")
        return  'https://globaleducation.s3.ap-south-1.amazonaws.com/globaledu/no-image.png' # Or a default poster path


st.title('Movie Recmmonder System')
selected_movie_name = st.selectbox("Choose a Movie.....",(movies['title'].values))
if st.button('Recommend'):
    names, posters = recmmond(selected_movie_name)
    num_columns = 5
    cols = st.columns(num_columns)
    for i in range(min(num_columns, len(names))):
        with cols[i]:
            st.write(names[i])
            #1)
            st.image(posters[i])

            #4)
            # if posters[i] is not None:
            #     st.image(posters[i])
            # else:
            #     st.warning("Failed to fetch poster")


            # 3)
            # try:
            #     # Code to load or process images
            #     st.image(posters[i], use_column_width=True)
            # except Exception as e:
            #     st.error(f"Error loading image: {e}")





            # 2)
            # file_path = posters[i]
    
            # # Check the file extension
            # file_extension = os.path.splitext(file_path)[1].lower()

            # # Display image or gif based on the file extension
            # if file_extension in ['.png', '.jpg', '.jpeg']:
            #     st.image(file_path)
            # elif file_extension == '.gif':
            #     st.image(file_path)
            # else:
            #     st.warning(f"Unsupported file type for {file_path}")

