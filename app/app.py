import streamlit as st
import pandas as pd
import pickle
import folium
from streamlit_folium import st_folium
import plotly.express as px

feature_columns = pickle.load(open("app/feature_columns.pkl","rb"))

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Dashboard Overview", "Accident Heatmap", "Severity Prediction"]
)

st.set_page_config(page_title="Road Accident Risk Dashboard", layout="wide")

st.title("🚦 Road Accident Risk Analysis Dashboard")

st.write(
"""
This dashboard analyzes UK road accident data and predicts accident severity using a machine learning model.
"""
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/raw/accidents.csv")

data = load_data()

st.sidebar.header("Filters")

year_filter = st.sidebar.selectbox(
    "Select Year",
    sorted(data["Year"].unique())
)

day_filter = st.sidebar.selectbox(
    "Select Day",
    sorted(data["Day_of_Week"].unique())
)
filtered_data = data[
    (data["Year"] == year_filter) &
    (data["Day_of_Week"] == day_filter)
]

# Load trained model
@st.cache_resource
def load_model():
    return pickle.load(open("app/accident_severity_model.pkl", "rb"))

model = load_model()

if page == "Dashboard Overview":

    st.subheader("Dataset Overview")
    st.metric("Accidents in selected filter", len(filtered_data))

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Accidents", len(filtered_data))
    col2.metric("Total Casualties", filtered_data["Number_of_Casualties"].sum())
    col3.metric("Total Vehicles", filtered_data["Number_of_Vehicles"].sum())

    st.subheader("Dataset Preview")

    st.dataframe(filtered_data.head())

    st.subheader("Accident Severity Distribution")

    severity_counts = filtered_data["Accident_Severity"].value_counts().reset_index()
    severity_counts.columns = ["Severity", "Count"]

    fig = px.bar(
       severity_counts,
       x="Severity",
       y="Count",
       color="Severity",
       title="Distribution of Accident Severity"
    )
    st.plotly_chart(fig)

    st.subheader("Accident Hotspot Map")

    map_data = filtered_data[["Latitude","Longitude"]].dropna().sample(2000)

     # rename columns for streamlit
    map_data = map_data.rename(columns={
       "Latitude": "latitude",
       "Longitude": "longitude"
    })

st.map(map_data)

if page == "Accident Heatmap":

    st.subheader("UK Road Accident Heatmap")

    # Use a subset for faster rendering
    map_data = data[["Latitude", "Longitude"]].dropna().sample(5000)

    # Create map centered roughly in UK
    m = folium.Map(location=[54.5, -3], zoom_start=6)

    for _, row in map_data.iterrows():
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=2,
            color="red",
            fill=True
        ).add_to(m)

    st_folium(m, width=900, height=500)    

if page == "Severity Prediction":

    st.subheader("Accident Severity Prediction")
    st.write("Enter accident conditions and the model will predict the severity.")

    # User inputs
    col1, col2 = st.columns(2)

    with col1:
        speed_limit = st.slider("Speed Limit", 20, 70, 40)
        vehicles = st.number_input("Number of Vehicles", 1, 10, 2)
        casualties = st.number_input("Number of Casualties", 0, 10, 1)

    with col2:
        hour = st.slider("Hour of Day", 0, 23, 12)
        day = st.selectbox(
            "Day of Week",
            ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        )

    # Prediction button
    if st.button("Predict Severity"):

        # create empty row with all model features
        input_row = pd.DataFrame(columns=feature_columns)
        input_row.loc[0] = 0

        # fill important values
        if "Speed_limit" in input_row.columns:
            input_row["Speed_limit"] = speed_limit

        if "Number_of_Vehicles" in input_row.columns:
            input_row["Number_of_Vehicles"] = vehicles

        if "Number_of_Casualties" in input_row.columns:
            input_row["Number_of_Casualties"] = casualties

        if "Hour" in input_row.columns:
            input_row["Hour"] = hour

        # handle one-hot encoded day columns
        day_column = f"Day_of_Week_{day}"
        if day_column in input_row.columns:
            input_row[day_column] = 1

        # make prediction
        prediction = model.predict(input_row)

        severity_map = {
            1: "Fatal / Severe Accident",
            2: "Serious Accident",
            3: "Slight Accident"
        }

        result = severity_map.get(prediction[0], "Unknown")

        st.success(f"Predicted Accident Severity: {result}")

        

    