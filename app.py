import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("energy_model.pkl")
feature_names = joblib.load("feature_names.pkl")

st.title("Energy Consumption Prediction App")

# User inputs
inputs = {}

for feature in feature_names:
    inputs[feature] = st.number_input(feature)

# Convert to dataframe
input_data = pd.DataFrame([inputs])

# Match exact feature order
input_data = input_data[feature_names]

# Predict
if st.button("Predict"):

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Energy Class: {prediction[0]}"
    )