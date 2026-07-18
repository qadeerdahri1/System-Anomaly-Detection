# app.py
import streamlit as st
from core_logic import train_model, predict_anomaly
from ui_visuals import create_threat_confidence_chart, generate_explanation_text

# 1. Page Setup & UI Header
st.set_page_config(page_title="Threat Detection AI", layout="wide")
st.title("🛡️ System Anomaly & Spam Detection AI")
st.markdown("This system uses Machine Learning (Naive Bayes) to find the difference between normal system logs and dangerous anomalies.")

# 2. Load and Train Model (Get data from backend)
vectorizer, model, accuracy, precision, classes = train_model()

# 3. Evaluation Module (Show metrics in the sidebar)
with st.sidebar:
    st.header("⚙️ Evaluation Metrics")
    st.write(f"**Model Accuracy:** {accuracy * 100:.1f}%")
    st.write(f"**Anomaly Precision:** {precision * 100:.1f}%")
    st.info("Algorithm: Multinomial Naive Bayes\nFeature Extraction: TF-IDF")

# 4. Problem Setup Module (User Input Box)
st.subheader("🔍 Threat Analysis Engine")
user_input = st.text_area("Enter a System Log or Message (e.g., 'URGENT: account compromised click here'):")

# 5. Core Logic Trigger (When the button is clicked)
if st.button("Run Analysis"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze!")
    else:
        # Get the prediction from the model
        prediction, probabilities = predict_anomaly(user_input, vectorizer, model)
        
        # Calculate the confidence percentage
        pred_index = list(classes).index(prediction)
        confidence = probabilities[pred_index] * 100
        
        # UI Layout: Divide into 2 Columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Final Result")
            if prediction == "Anomaly":
                st.error("🚨 THREAT / ANOMALY DETECTED!")
            else:
                st.success("✅ SYSTEM NORMAL")
            
            # Show a simple English explanation
            explanation = generate_explanation_text(prediction, confidence)
            st.write(explanation)
            
        with col2:
            st.subheader("Visual Explainability Chart")
            # Draw the Matplotlib Chart
            fig = create_threat_confidence_chart(probabilities, classes)
            st.pyplot(fig)