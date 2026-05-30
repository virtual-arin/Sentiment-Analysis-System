# Sentiment Analyzer App 🎭

A Machine Learning based Sentiment Analysis web application that predicts human emotions from text input.  
This project uses Natural Language Processing (NLP) techniques along with a trained machine learning model to classify emotions such as Joy, Sadness, Anger, Fear, Love, and Surprise.

---

## 🚀 Features

- Real-time sentiment prediction
- Interactive web interface using Streamlit
- Multi-class emotion classification
- Lightweight and fast prediction system
- User-friendly UI
- NLP-based text preprocessing

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Joblib
- Natural Language Processing (NLP)

---

## 📂 Project Structure

```bash
├── app.py                    
├── model.pkl 
├── README.md
├── requirements.txt
├── Sentiment_Analysis.ipynb  
├── train.txt
└── vectorizer.pkl                     
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/virtualarin/Sentiment-Analyzer.git
cd Sentiment-Analyzer
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters text in the Streamlit interface.
2. Text is transformed using the trained vectorizer.
3. The machine learning model predicts the sentiment.
4. Predicted emotion is displayed to the user.

---

## 🔮 Future Scope

- Implement Deep Learning models like LSTM and BERT
- Add multilingual sentiment analysis support
- Deploy using Docker and cloud platforms
- Add sentiment probability/confidence visualization
- Create REST API integration
- Store prediction history in a database
- Add voice-to-text sentiment prediction
- Improve UI/UX with advanced dashboards
