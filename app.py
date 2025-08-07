import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Bird Observation Dashboard", layout="wide")
st.title("🕊️ Bird Observation Dashboard")

# Load your cleaned CSV
df = pd.read_csv("cleaned_bird_data.csv")

# Date & Time Conversion
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Hour'] = pd.to_datetime(df['Start_Time'], errors='coerce').dt.hour
df['Month'] = df['Date'].dt.month

# Add Season
def get_season(month):
    if month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Fall'
    else:
        return 'Winter'
df['Season'] = df['Month'].apply(get_season)

# Top 10 Species
st.subheader("🔝 Top 10 Most Observed Bird Species")
top_species = df['Common_Name'].value_counts().head(10).reset_index()
top_species.columns = ['Species', 'Count']
fig1 = px.bar(top_species, x='Species', y='Count', color='Species')
st.plotly_chart(fig1, use_container_width=True)

# Observations by Season
st.subheader("📅 Observations by Season")
season_count = df['Season'].value_counts().reset_index()
season_count.columns = ['Season', 'Count']
fig2 = px.bar(season_count, x='Season', y='Count', color='Season')
st.plotly_chart(fig2, use_container_width=True)

# Activity by Hour
st.subheader("⏰ Observation Activity by Hour")
hour_count = df['Hour'].value_counts().sort_index().reset_index()
hour_count.columns = ['Hour', 'Count']
fig3 = px.bar(hour_count, x='Hour', y='Count')
st.plotly_chart(fig3, use_container_width=True)

habitats = ['All'] + sorted(df['Location_Type'].dropna().unique())
selected_habitat = st.selectbox("Filter by Habitat Type", habitats)

if selected_habitat != 'All':
    df = df[df['Location_Type'] == selected_habitat]

st.subheader("👤 Top 5 Observers")
top_obs = df['Observer'].value_counts().head(5).reset_index()
top_obs.columns = ['Observer', 'Records']
fig4 = px.bar(top_obs, x='Observer', y='Records', color='Observer')
st.plotly_chart(fig4, use_container_width=True)

st.subheader("🕊️ Flyover vs Stationary Birds")
flyover_count = df['Flyover_Observed'].value_counts().reset_index()
flyover_count.columns = ['Flyover_Observed', 'Count']
fig5 = px.pie(flyover_count, names='Flyover_Observed', values='Count', title="Flyover Observations")
st.plotly_chart(fig5)

# Section: Dynamic Scatter Plot of Bird Species by Plot and Distance
st.subheader("📍 Scatter Plot of Species Across Plots")

# Create a dropdown to select a bird species
species_list = sorted(df['Common_Name'].dropna().unique())
selected_species = st.selectbox("Choose a species to visualize:", species_list)

# Filter data for the selected species
filtered_df = df[df['Common_Name'] == selected_species]

# Plot scatter of Distance vs Plot_Name for the selected species
if not filtered_df.empty:
    fig = px.scatter(
        filtered_df,
        x='Plot_Name',
        y='Distance',
        color='Sex',  # Color points by bird's sex
        hover_data=['Scientific_Name', 'Start_Time', 'Flyover_Observed'],
        title=f"{selected_species} Observation Distance by Plot"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data available for the selected species.")

# Section: Monthly Distribution of Bird Species
st.subheader("📊 Monthly Distribution of Observed Species")

# Group by Month and Species to get counts
monthly_species = df.groupby(['Month', 'Common_Name']).size().reset_index(name='Count')

# Dropdown to choose species
selected_species_bar = st.selectbox("Select a species for monthly trends:", species_list)

# Filter data for the selected species
species_monthly = monthly_species[monthly_species['Common_Name'] == selected_species_bar]

# Plot bar chart of monthly counts
fig_bar = px.bar(
    species_monthly,
    x='Month',
    y='Count',
    title=f"Monthly Observation Count for {selected_species_bar}",
    labels={'Month': 'Month', 'Count': 'Number of Observations'}
)
st.plotly_chart(fig_bar, use_container_width=True)

# Section: Heatmap of Bird Observations by Year and Month
st.subheader("🌡️ Heatmap of Observations by Year and Month")

# Extract year from the Date column
df['Year'] = df['Date'].dt.year

# Group data by Year and Month
heatmap_data = df.groupby(['Year', 'Month']).size().reset_index(name='Count')

# Create heatmap using density
fig_heat = px.density_heatmap(
    heatmap_data,
    x='Month',
    y='Year',
    z='Count',
    color_continuous_scale='Viridis',
    title='Observation Density Heatmap (Year vs Month)'
)
st.plotly_chart(fig_heat, use_container_width=True)

# Section: Mapping Bird Observations by Latitude & Longitude
st.subheader("🗺️ Bird Observations Map")

# Check if Latitude and Longitude columns exist
if 'Latitude' in df.columns and 'Longitude' in df.columns:
    st.map(df[['Latitude', 'Longitude']])  # Streamlit's built-in map
else:
    st.warning("Geographic location data (Latitude & Longitude) not available.")

# Section: Histogram of Bird Observations by Temperature
st.subheader("🌦️ Bird Observations by Temperature")

# Check if temperature data is available
if 'Temperature' in df.columns:
    fig_temp = px.histogram(
        df,
        x='Temperature',
        title='Bird Observations by Temperature',
        nbins=30
    )
    st.plotly_chart(fig_temp, use_container_width=True)
else:
    st.warning("Temperature data not found.")
