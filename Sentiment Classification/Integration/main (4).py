def predict_sentiment(text):
    """
    Makes a sentiment prediction on the given text.
    
    Args:
        text (str): The input text to be analyzed.
    
    Returns:
        str: The predicted sentiment ('Positive', 'Negative', or 'Neutral').
    """
    # Convert the text into a numerical representation using the vectorizer
    text_vector = vectorizer.transform([text])
    
    # Make the prediction using the trained model
    prediction = model.predict(text_vector)
    
    # Convert the prediction to a sentiment label
    sentiment = 'Positive' if prediction[0] == 1 else \
                'Negative' if prediction[0] == -1 else 'Neutral'
    
    return sentiment