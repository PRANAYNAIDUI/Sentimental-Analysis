import joblib

# Load the trained model
model = joblib.load('sentiment_model.pkl')

# Load the vectorizer
vectorizer = joblib.load('tfidf_vectorizer.pkl')