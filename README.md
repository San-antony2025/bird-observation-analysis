
# 🕊️ Bird Species Observation Analysis Project

This is a comprehensive data analysis project exploring bird species observations across forest and grassland habitats. The project includes data cleaning, exploratory data analysis (EDA), insights discovery, and an interactive dashboard built using **Streamlit** and **Plotly**.

---

## 🧠 Objective

The goal of this project is to analyze bird activity patterns across different ecosystems (forest and grassland), understand seasonal and temporal trends, evaluate environmental impacts on sightings, and derive insights for conservation and biodiversity efforts.

---

## 📊 Project Components

### 1. Data Cleaning & Preparation
- Combined datasets from multiple Excel sheets (forest and grassland)
- Handled missing values, date/time conversions, and standardization
- Created derived columns like `Season`, `Hour`, `Month`, etc.

### 2. Exploratory Data Analysis (EDA)
- Species diversity analysis
- Observation trends by month, hour, and season
- Behavior analysis (e.g., flyover, distance from observer)
- Environmental impact (temperature, humidity, wind)
- Observer patterns and visit effects

### 3. Insights
- Peak bird activity occurs between **6–8 AM** during **summer months**
- Grassland plots had more frequent observations than forests
- Temperature and sky condition influenced bird sightings
- Flyovers were more common in open plots
- A few observers recorded a disproportionate number of sightings

### 4. Interactive Dashboard
- Built using Streamlit and Plotly
- Enables dynamic filtering, visualization, and exploration
- Includes charts for species, seasons, behaviors, and conditions

---

## 📁 Project Structure

```text
├── app.py                      # Streamlit dashboard script
├── cleaned_bird_data.csv       # Final cleaned dataset used for analysis & dashboard
├── bird_analysis.ipynb         # (Optional) Jupyter notebook with EDA & code exploration
├── requirements.txt            # List of Python dependencies
├── README.md                   # Project documentation

