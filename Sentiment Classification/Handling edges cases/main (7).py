import re
import string

def preprocess_text(text):
    """
    Preprocesses text by removing special characters and normalizing the text.
    """
    if not text:
        return ""
    
    # Remove special characters and punctuation
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def handle_edge_cases(text):
    """
    Checks for various edge cases and returns appropriate responses.
    """
    # Check for empty input
    if not text.strip():
        return {"error": "Empty input", "sentiment": "neutral"}
    
    # Check for non-English text (basic check)
    if not text.isalpha():
        return {"error": "Non-English text detected", "sentiment": "neutral"}
    
    # Check for very short text
    if len(text.split()) < 2:
        return {"error": "Text too short", "sentiment": "neutral"}
    
    return None

def predict_sentiment(text, model):
    """
    Makes predictions while handling edge cases.
    """
    edge_case_result = handle_edge_cases(text)
    if edge_case_result:
        return edge_case_result
    
    preprocessed_text = preprocess_text(text)
    if not preprocessed_text:
        return {"error": "Empty input after preprocessing", "sentiment": "neutral"}
    
    # Convert text to numerical representation (e.g., using TF-IDF)
    # This step depends on your specific preprocessing pipeline
    # For example:
    tfidf_vector = vectorizer.transform([preprocessed_text])
    
    # Make prediction
    prediction = model.predict(tfidf_vector)
    
    return {"sentiment": prediction[0]}