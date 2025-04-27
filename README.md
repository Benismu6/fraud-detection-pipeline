# Fraud Detection - End-to-End Machine Learning Project

## Overview
This project simulates a real-world fraud detection pipeline, covering the entire process from data collection to model training and saving.

## Key Steps
- Pulled user data from a public API (DummyJSON Users API).
- Simulated transaction data per user (randomized amounts, hours, fraud labels).
- Performed data exploration and preprocessing.
- Trained a Random Forest model to classify transactions as fraudulent or not.
- Evaluated the model using classification metrics and confusion matrix.
- Saved the trained model for future deployment.

## Outcomes
- Built an end-to-end fraud detection model from scratch.
- Achieved reasonable performance despite simulated data and class imbalance.
- Set up a clean, professional project structure suitable for real-world applications.

## Project Structure

fraud_detection_project/
│
├── data/
│   ├── users.csv
│   └── transactions.csv
│
├── models/
│   └── fraud_detection_model.pkl
│
├── notebooks/
│   └── fraud_detection_end_to_end.ipynb
│
├── requirements.txt
├── .gitignore
└── README.md

## Future Improvements
- Deploy the model with a simple Streamlit app.
- Introduce real-time transaction streaming and prediction simulation.