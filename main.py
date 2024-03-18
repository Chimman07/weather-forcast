import streamlit as st
import plotly.express as pt

st.header("Weather Forecast for the next days")
place = st.text_input("Place")
days = st.slider("Days", min_value=1, max_value=5)
kind = st.selectbox("Select data to view", ('Temperature', 'Sky'))

if place:
    st.subheader(f"{kind} for the next {days} days for {place}")




