
import streamlit
streamlit.title(' My Parents New Healthy diner')
streamlit.header('🥣 Breakfast Favroites')
streamlit.text(' 🥣Omega 3 and blueberry oatmeal')
streamlit.text(' 🥗Kale, spinach and Rocket smoothie')
streamlit.text('🐔Hard Boiled Free-Range egg')
streamlit.text('🥑🍞 Avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
         



