import streamlit as st
import numpy as np
import pandas as pd

# Set page layout to wide
st.set_page_config(layout='wide')

# Set header
st.header("Worldwide Analysis of Quality of Life and Economic Factors")

# Create subtitle.
st.subheader("This app enables you to explore the relationships between poverty,\
            life expectancy, and GDP across various countries and years.\
            Use the panels to select options and interact with the data.")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Global Overview", "Country Deep Dive", "Data Explorer"])

# Content for each tab
with tab1:
    st.subheader("Global Overview")
    st.write("This section provides a broad analysis of quality of life and economic factors worldwide.")
    ######## task 4 ################
    #   uploaded_file = st.file_uploader("global_development_data.csv", type=["csv"])
    uploaded_file1 = st.file_uploader("global_development_data.csv", type=["csv"], key='2')

    if uploaded_file1 is not None:
        df = pd.read_csv(uploaded_file1)
    required_cols = {"year", "Life Expectancy (IHME)", "GDP per capita", "headcount_ratio_upper_mid_income_povline", "country"}
    
    if not required_cols.issubset(df.columns):
        st.error("Dataset is missing one or more required columns: 'year', 'Life Expectancy', 'GDP per capita', 'headcount_ratio_upper_mid_income_povline', 'Country'")
    else:
        # Year selection slider
        selected_year = st.slider("Select a year", int(df["year"].min()), int(df["year"].max()), int(df["year"].max()))
        
        # Filter dataset by selected year
        filtered_df = df[df["year"] == selected_year]
        
        # Calculate metrics
        mean_life_exp = filtered_df["Life Expectancy (IHME)"].mean()
        median_gdp_per_capita = filtered_df["GDP per capita"].median()
        mean_poverty_rate = filtered_df["headcount_ratio_upper_mid_income_povline"].mean()
        num_countries = filtered_df["country"].nunique()
    

with tab2:
    st.subheader("Country Deep Dive")
    st.write("Analyze specific countries in detail based on various indicators.")

with tab3:
    st.subheader("Data Explorer")
    st.write("Explore and interact with the raw data behind the analysis.")
    
        #######################task 2##########################33
 #Upload CSV file
    uploaded_file = st.file_uploader("global_development_data.csv", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Show dataset preview
        #st.write("### Raw Dataset Preview")
        #st.dataframe(df.head())

        # Ensure "Country" and "Year" columns exist before filtering
        if "country" in df.columns and "year" in df.columns:
            # Country selection
            countries = st.multiselect("Select countries:", df["country"].unique())

            # Year selection
            min_year, max_year = int(df["year"].min()), int(df["year"].max())
            year_range = st.slider("Select Year Range:", min_year, max_year, (min_year, max_year))

            # Filter the dataset
            filtered_df = df[
                (df["year"] >= year_range[0]) & (df["year"] <= year_range[1])
            ]
            if countries:
                filtered_df = filtered_df[filtered_df["country"].isin(countries)]

            # Show filtered dataset
            st.write("### Filtered Dataset")
            st.dataframe(filtered_df)

            # Download button
            @st.cache_data
            def convert_df(df):
                return df.to_csv(index=False).encode("utf-8")

            csv = convert_df(filtered_df)
            st.download_button(
                label="Download filtered data as CSV",
                data=csv,
                file_name="filtered_data.csv",
                mime="text/csv",
            )
        else:
            st.error("The uploaded file must contain 'country' and 'Year' columns.")
            
