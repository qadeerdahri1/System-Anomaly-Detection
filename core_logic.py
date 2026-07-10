# core_logic.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score

def load_data():
    # Lab project ke liye ek sample system logs & messages dataset 
    # (Normal system logs vs Malicious/Spam anomalies)
    data = {
        "log_text": [
            "User logged in successfully to the dashboard",
            "Database backup completed at 03:00 AM",
            "System rebooted normally after update",
            "Frontend page loaded in 200ms",
            "URGENT: Your server account is compromised click here to secure",
            "Multiple failed login attempts detected from unknown IP",
            "Win a free iPhone click the malicious link now!!",
            "Suspicious payload injection detected in backend API request"
        ],
        "label": [
            "Normal", "Normal", "Normal", "Normal",
            "Anomaly", "Anomaly", "Anomaly", "Anomaly"
        ]
    }
    return pd.DataFrame(data)

def train_model():
    df = load_data()
    
    # 1. Text processing using TF-IDF (Term Frequency-Inverse Document Frequency)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['log_text'])
    y = df['label']
    
    # 2. Training the Classification Model
    model = MultinomialNB()
    model.fit(X, y)
    
    # 3. Generating Evaluation Metrics for the UI Dashboard
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    # Precision batayega ke model ne anomaly detect karne mein kitni accuracy dikhayi
    precision = precision_score(y, predictions, pos_label="Anomaly")
    
    return vectorizer, model, accuracy, precision, model.classes_

def predict_anomaly(text, vectorizer, model):
    # Transform unseen text data
    X_input = vectorizer.transform([text])
    
    # Predict Normal or Anomaly
    prediction = model.predict(X_input)[0]
    
    # Get probability percentages for Explainability UI
    probabilities = model.predict_proba(X_input)[0]
    
    return prediction, probabilities