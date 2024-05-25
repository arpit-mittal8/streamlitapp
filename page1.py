# page1.py
import streamlit as st
import plotly.express as px
import pandas as pd
import pydeck as pdk

# Function to navigate to different pages
def navigate_to(page):
    st.session_state.page = page

st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Page content
def main():
    st.title("Welcome to HealthTrack")
    st.subheader("Your Comprehensive Health Management Solution")
    st.markdown("""
    **HealthTrack** is designed to help you take control of your health with ease. 
    From tracking your daily health metrics to scheduling appointments and accessing reliable health resources, 
    HealthTrack is your all-in-one healthcare companion.
    """)

    # Buttons to navigate to other pages
    if st.button('Brain Tumor Classification'):
        navigate_to('brain_tumor_classification')

    # Check the session state and navigate
    elif st.session_state.page == 'brain_tumor_classification':
        st.experimental_rerun()

    # Display graphs related to brain diseases
    st.subheader("Graphs Related to Brain Diseases")

    # Example data for brain disease statistics (can be replaced with real data)
    data = pd.DataFrame({
        'Year': [2015, 2016, 2017, 2018, 2019],
        'Number of Cases': [1000, 1200, 1100, 1300, 1400],
        'Disease Type': ['Alzheimer\'s', 'Parkinson\'s', 'Brain Tumor', 'Stroke', 'Epilepsy']
    })

    # Create bar chart showing number of cases per year for different brain diseases
    fig = px.bar(data, x='Year', y='Number of Cases', color='Disease Type',
                 title='Number of Cases of Different Brain Diseases Over Time')
    st.plotly_chart(fig, use_container_width=True)

   # Display world map
    st.subheader("World Map")
    st.write("This is a world map:")
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=0,
            longitude=0,
            zoom=1,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data='https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv',
                get_position='[lng, lat]',
                auto_highlight=True,
                elevation_scale=50,
                pickable=True,
                extruded=True,
            ),
        ],
    ))

    # Display graphs related to brain diseases
    st.subheader("Graphs Related to Brain Diseases")

    # Example data for brain disease cases by country (can be replaced with real data)
    data = pd.DataFrame({
        'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
        'Number of Cases': [500, 400, 300, 200, 100]
    })

    # Create choropleth map showing distribution of brain disease cases by country
    fig = px.choropleth(data, locations='Country', locationmode='country names', color='Number of Cases',
                        hover_name='Country', color_continuous_scale='Viridis',
                        title='Distribution of Brain Disease Cases by Country')
    st.plotly_chart(fig, use_container_width=True)
    # Optionally add social media links or additional information
    st.markdown("""
    Follow us on:
    - [Twitter](https://twitter.com/HealthTrack)
    - [Facebook](https://facebook.com/HealthTrack)
    - [Instagram](https://instagram.com/HealthTrack)
    """)

        # Footer
    st.markdown("---")
    st.markdown("© 2024 HealthTrack. All rights reserved.")

if __name__ == "__main__":
    main()


