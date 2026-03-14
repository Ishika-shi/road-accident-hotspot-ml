# 🚦 Road Accident Hotspot & Severity Prediction Dashboard

An interactive **Machine Learning web application** that analyzes road accident data to detect accident-prone areas and predict accident severity using an intuitive dashboard.

This project combines **data science, geospatial visualization, and web deployment** to transform raw accident data into meaningful safety insights.

---

# 🌐 Live Application

🔗 **Try the deployed dashboard**

https://road-accident-hotspot-ml.streamlit.app

The application is deployed using Streamlit Cloud and allows users to explore accident data and generate predictions directly from a web interface.

---

# 📌 Project Overview

Road accidents are one of the leading causes of injuries and fatalities worldwide. Understanding accident patterns can help authorities implement better traffic safety strategies.

This project builds an interactive dashboard that:

• Visualizes accident locations on a map  
• Detects potential accident-prone regions  
• Predicts accident severity using a machine learning model  
• Provides an interactive interface for exploring accident data  

The aim is to demonstrate how **machine learning and visualization can support data-driven road safety analysis**.

---

# 🧠 Machine Learning Model

The accident severity prediction system uses a **Random Forest Classification Model**.

The model analyzes various accident-related features to estimate the likely severity level of an accident.

### Model Pipeline

1️⃣ Data collection and preprocessing  
2️⃣ Feature selection and encoding  
3️⃣ Train-test data split  
4️⃣ Model training using Random Forest  
5️⃣ Model serialization using Pickle  
6️⃣ Deployment inside a Streamlit dashboard  

Saved model file:

```
accident_severity_model.pkl
```

---

# 🗺️ Interactive Accident Map

The dashboard visualizes accident locations using an interactive map.

Each point on the map represents a recorded accident from the dataset.

Users can:

• identify accident clusters  
• observe geographic patterns  
• explore accident-prone locations  

This visual approach makes it easier to interpret accident data compared to traditional tables.

---

# ⚙️ Tech Stack

### Programming Language
• Python

### Machine Learning
• Scikit-learn  
• Pandas  
• NumPy  

### Data Visualization
• Plotly  
• Folium  

### Web Framework
• Streamlit

### Version Control
• Git  
• GitHub

---

# 🏗️ System Architecture

```
                Accident Dataset
                        │
                        ▼
                Data Preprocessing
                        │
                        ▼
              Feature Engineering
                        │
                        ▼
             Machine Learning Model
              (Random Forest Classifier)
                        │
                        ▼
               Model Serialization
                    (Pickle)
                        │
                        ▼
               Streamlit Web App
                        │
                        ▼
          Interactive Dashboard + Map
```

---

# 📂 Project Structure


road-accident-hotspot-ml

app/
   app.py
   accident_severity_model.pkl
   feature_columns.pkl

sample_data/
   accidents_sample.csv

notebooks/
   dataset_exploration.ipynb

requirements.txt
README.md


# 🚀 Features

### 📊 Accident Data Visualization
Interactive map displaying accident locations.

### 🤖 Accident Severity Prediction
Machine learning model predicts accident severity.

### 🌐 Web-based Dashboard
Accessible through a browser with no local setup required.

### 🔁 End-to-End ML Pipeline
Demonstrates the full lifecycle of a machine learning project:
Data → Model → Web App → Deployment.

---

# 📈 Current Limitations

Although the system works as a functional prototype, some limitations exist:

• Uses a **sample dataset** instead of a large real-world dataset  
• Accident clusters are visually inferred rather than statistically detected  
• The model does not yet provide **explainability** for predictions  

These limitations offer opportunities for future improvements.

---

# 🔮 Future Improvements

### 🔥 Accident Hotspot Detection
Use clustering algorithms such as **K-Means or DBSCAN** to automatically detect high-risk zones.

### 🌡 Heatmap Visualization
Introduce heatmaps to display accident density more clearly.

### 📊 Risk Score Prediction
Predict a numerical **accident risk score** rather than only categorical severity.

### 🧠 Explainable AI
Integrate feature importance or SHAP values to explain model predictions.

### 🌦 Real-Time Data Integration
Incorporate weather and traffic data for real-time risk prediction.

### 📍 Advanced Geospatial Analytics
Use spatial analysis techniques to identify dangerous road segments.

---

# 💡 Key Learning Outcomes

This project demonstrates hands-on experience with:

• Machine learning model development  
• data preprocessing and feature engineering  
• geospatial visualization  
• building interactive dashboards  
• deploying ML applications to the web  

# 👩‍💻 Author

**Ishika Goyal**

BTech – Computer Science & Engineering (Data Science)


---
