import streamlit as st
import pandas as pd
import template as t

st.set_page_config(layout='wide')

if 'title' not in st.session_state:
  st.session_state['title'] = 'Greta Thunberg: A Year To Change The World'

df = pd.read_csv('Assignment/code/abc.csv')

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

st.subheader('Liked "' + selected_article['title'] + '"?')
st.subheader('You may also like:')

### First row of recommended article, based on the same cluster

# df_recommendations = df[(df['category_name'] == selected_article['category_name']) | (df['k_means'] == selected_article['k_means']) ].sample(10)
df_recommendations_similar = df[(df['k_means'] == selected_article['k_means'])].sample(8)
df_recommendations_diverse = df[(df['k_means'] != selected_article['k_means'])].sample(8)

t.recommendations(df_recommendations_similar)

### Second row of recommended article, based on a different cluster

st.subheader('Discover more:')
t.recommendations(df_recommendations_diverse)

# to run: streamlit run Assignment/app/app.py

