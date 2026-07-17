import matplotlib.pyplot as plt

def create_threat_confidence_chart(probabilities, classes):
    # Sir ki requirement ke mutabiq visual bar chart
    fig, ax = plt.subplots(figsize=(7, 3.5))
    
    # Normal ke liye Green, Anomaly (Spam) ke liye Red color
    colors = ['#28a745' if c == 'Normal' else '#dc3545' for c in classes]
    
    bars = ax.barh(classes, probabilities * 100, color=colors)
    ax.set_xlabel('Model Confidence (%)')
    ax.set_title('Threat Detection Analysis (Explainability)')
    ax.set_xlim(0, 100)
    
    # Bars ke aagay percentage likhne ke liye
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 2, bar.get_y() + bar.get_height()/2, f'{width:.1f}%', va='center', fontweight='bold')
        
    plt.tight_layout()
    return fig

def generate_explanation_text(prediction, confidence):
    # Short natural-language explanation
    if prediction == "Anomaly":
        return f"🚨 **Alert:** AI model is {confidence:.1f}% confident that this input is an ANOMALY. It contains suspicious patterns, spam keywords, or unusual system activity."
    else:
        return f"✅ **Safe:** The input is classified as NORMAL with {confidence:.1f}% confidence. No malicious patterns were detected in the log."
