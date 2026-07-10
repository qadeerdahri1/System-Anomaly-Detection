 # System Anomaly & Spam Detection AI

## Project Description
This is an Explainable Machine Learning system built to distinguish between normal system logs and malicious anomalies using the Naive Bayes algorithm and TF-IDF vectorization.

## Project Structure
- `core_logic.py`: Handles data loading, TF-IDF vectorization, model training, and evaluation metrics.
- `ui_visuals.py`: Generates Matplotlib bar charts for visual decision explainability.
- `app.py`: The main Streamlit web application that integrates the backend logic and frontend UI.
- `requirements.txt`: Contains all the necessary Python package dependencies.

## Setup & Running Instructions
1. Open your terminal in the project directory.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt