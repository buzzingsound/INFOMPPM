import streamlit as st
import pandas as pd
import template as t

st.set_page_config(layout='wide')

if 'title' not in st.session_state:
  st.session_state['title'] = 'Cracking COVID'

df = pd.read_csv('data/abc.csv')

# the initial article
selected_article = df[df['title'] == st.session_state['title']].iloc[0]

col1, col2 = st.columns(2)

poster = selected_article['thumbnail']

with col1: 
  st.image(poster)

with col2:
  st.title(selected_article['title'])
  st.text(selected_article['description'])
  st.caption(selected_article['category_name'])


### First row of recommended article, based on the same cluster
st.subheader("Liked '" + selected_article['title'] + "'?")
st.subheader('Explore more in ' + selected_article['category_name'] + ':')

df_recommendations_similar = df[(df['category_name'] == selected_article['category_name'])].sample(8)

t.recommendations(df_recommendations_similar)

### Second row of recommended article, based on a different cluster
st.subheader('Why stop there? Discover more today:')

df_recommendations_diverse = df[(df['k_means'] != selected_article['k_means'])].sample(8)

t.recommendations(df_recommendations_diverse)

# to run: streamlit run app/app.py

