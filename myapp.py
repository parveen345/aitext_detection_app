import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load model and vectorizer
model = joblib.load("logistic_model1.pkl")
vectorizer = joblib.load("tfidf_vectorizer1.pkl")

# Title and description
st.title("AI vs Human Text Detection")
st.write("This app detects whether a given text is written by a human or AI.")

# Input text box
user_input = st.text_area("Enter text to classify:")

# Prediction button
if st.button("Classify"):
    if user_input:
        # Preprocess the text (same preprocessing as during model training)
        input_tfidf = vectorizer.transform([user_input])
        
        # Make prediction using the trained model
        prediction = model.predict(input_tfidf)
        
        # Display result
        if prediction == 1:
            st.write("The text is generated by AI.")
        else:
            st.write("The text is written by a human.")
    else:
        st.write("Please enter some text to classify.")


