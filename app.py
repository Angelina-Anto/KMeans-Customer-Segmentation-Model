import streamlit as st
import joblib

# Load trained model
model = joblib.load("customer_segmentation_model.pkl")

# Title
st.title("Customer Segmentation App")

# Input 1
income = st.number_input(
    "Enter Annual Income (₹ Lakhs):",
    min_value=1.0,
    max_value=50.0,
    value=10.0
)

# Input 2
spending_score = st.number_input(
    "Enter Spending Score (1-100):",
    min_value=1.0,
    max_value=100.0,
    value=50.0
)

# Prediction
if st.button("Predict Customer Segment"):

    if 1 <= income <= 50 and 1 <= spending_score <= 100:

        prediction = model.predict([[income, spending_score]])

        st.success(
            f"Customer belongs to Cluster {prediction[0]}"
        )

    else:
        st.error("Please enter valid customer details.")
