import streamlit as st
import pandas as pd
from src.load_data import load_event_data
from src.xg_model import calculate_xg
from src.pressing import calculate_pressing_intensity

st.title("Football Event Data Analytics")

uploaded_file = st.file_uploader("Upload StatsBomb event JSON")
if uploaded_file:
    df = load_event_data(uploaded_file)
    df['xG'] = df.apply(calculate_xg, axis=1)
    pressing_score = calculate_pressing_intensity(df)

    st.subheader("xG Distribution")
    st.bar_chart(df['xG'])

    st.subheader("Pressing Intensity")
    st.metric(label="Pressures per 90", value=round(pressing_score, 2))
