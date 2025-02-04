import streamlit as st

# Set page layout to wide
st.set_page_config(layout='wide')

# Set header
st.header("Worldwide Analysis of Quality of Life and Economic Factors")

# Create subtitle.











































.
st.subheader("This app enables you to explore the relationships between poverty,\
            life expectancy, and GDP across various countries and years.\
            Use the panels to select options and interact with the data.")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Global Overview", "Country Deep Dive", "Data Explorer"])

# Content for each tab
with tab1:
    st.subheader("Global Overview")
    st.write("This section provides a broad analysis of quality of life and economic factors worldwide.")

with tab2:
    st.subheader("Country Deep Dive")
    st.write("Analyze specific countries in detail based on various indicators.")

with tab3:
    st.subheader("Data Explorer")
    st.write("Explore and interact with the raw data behind the analysis.")