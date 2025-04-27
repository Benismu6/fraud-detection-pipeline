import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('models/fraud_detection_model.pkl')

# Streamlit App
st.title("Fraud Detection Prediction App")

st.write("Enter transaction details below:")

# User inputs
amount = st.number_input("Transaction Amount ($)", min_value=0.0, step=0.01)
hour = st.number_input("Transaction Hour (0-23)", min_value=0, max_value=23, step=1)

# Predict button
if st.button("Predict Fraud"):
    input_data = np.array([[amount, hour]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Transaction is likely FRAUDULENT!")
    else:
        st.success("✅ Transaction appears NORMAL.")
