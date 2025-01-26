import streamlit as st
import pandas as pd

def display():
    # Load dataset
    spotify_data = pd.read_csv("dataset.csv")

    # Sidebar for filters
    st.sidebar.header("Filters")
    selected_genre = st.sidebar.selectbox("Select Genre", spotify_data["track_genre"].unique())

    # Filter data
    filtered_data = spotify_data[spotify_data["track_genre"] == selected_genre]

    # Display data
    st.title(f"Spotify Trends - {selected_genre}")
    st.dataframe(filtered_data)

    # Plot
    st.line_chart(filtered_data.groupby("artists")["popularity"].mean())

display()

