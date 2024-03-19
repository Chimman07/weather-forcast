import streamlit as st
import plotly.express as pt
import beckend

st.header("Weather Forecast for the next days")
place = st.text_input("Place")
days = st.slider("Days", min_value=1, max_value=5)
kind = st.selectbox("Select data to view", ('Temperature', 'Sky'))

try:
    if place:
        st.subheader(f"{kind} for the next {days} days in {place}")
        record = beckend.get_data(place, days)

        if kind == "Temperature":
            temperature = [dict['main']['temp']/10 for dict in record]
            date = [dict['dt_txt'] for dict in record]
            figure = pt.line(x=date, y=temperature, labels={"x": "date", "y": "Temperature(C)"})
            st.plotly_chart(figure)

        if kind == "Sky":
            sky = [dict['weather'][0]['main'] for dict in record]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Snow": "images/snow.png",
                      "Rain": "images/rain.png"}
            images_path = [images[condition] for condition in sky]
            st.image(images_path, width=115)

except KeyError:
    st.info("Please enter a valid city name")
