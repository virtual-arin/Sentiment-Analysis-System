import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('models/model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Manual label mapping (adjust if needed)
label_map = {
    0: "Sad",
    1: "Anger",
    2: "Love",
    3: "Surprise",
    4: "Fear",
    5: "Joy"
}

st.title("Sentiment Analyzer")
st.write("This app predicts the sentiment of the provided text.")

user_input = st.text_area("Enter text here:")

if st.button("Predict Sentiment"):
    if user_input:
        user_input_vec = vectorizer.transform([user_input])
        prediction = model.predict(user_input_vec)[0]
            
        emotion = label_map.get(prediction, "Unknown")  # safe lookup
        
        st.success(f"Predicted Sentiment: {emotion}")
    else:
        st.warning("Please enter some text to analyze.")