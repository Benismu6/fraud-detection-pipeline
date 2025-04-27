# Fraud Detection - End-to-End Machine Learning Project

## Overview
This project simulates a real-world fraud detection pipeline, covering the entire process from data collection to model training and deployment.

## Key Steps
- Pulled user data from a public API (DummyJSON Users API).
- Simulated transaction data per user (randomized amounts, hours, fraud labels).
- Performed data exploration, preprocessing, and visualization.
- Trained a Random Forest model to classify transactions as fraudulent or not.
- Evaluated the model using classification metrics and confusion matrix.
- Saved the trained model for future deployment.
- Built a simple Streamlit app for live fraud prediction.

## Outcomes
- Built an end-to-end fraud detection model from scratch.
- Achieved reasonable performance despite simulated data and class imbalance.
- Visualized key patterns in the data:
  - Transaction amount distribution
  - Fraud vs Non-fraud counts
  - Transaction amounts by fraud status (boxplot)
- Developed a basic Streamlit app for live fraud prediction.

## Project Structure

fraud_detection_project/
├── data/
│   ├── users.csv
│   └── transactions.csv
├── models/
│   └── fraud_detection_model.pkl
├── notebooks/
│   └── fraud_detection_end_to_end.ipynb
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

## Streamlit App
We created a lightweight Streamlit web app that allows users to input transaction details (amount and hour) and predict whether the transaction is likely fraudulent using the trained model.

To run the app locally:
```bash
streamlit run app.py
