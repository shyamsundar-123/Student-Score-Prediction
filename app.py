import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("student_score_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit App Title
st.title("Student Score Prediction App 📊")

# User Input
hours = st.number_input("Enter study hours (between 1 to 10):", min_value=1.0, max_value=10.0, step=1.0)

# Predict Button
if st.button("Predict Score"):
    prediction = model.predict(np.array([[hours]]))  # Convert input to 2D array
    st.success(f"Predicted Score: {prediction[0]:.2f}")