def predict_sentiments(texts):
    """
    Makes sentiment predictions on a list of texts.
    
    Args:
        texts (list): A list of texts to be analyzed.
    
    Returns:
        list: A list of predicted sentiments corresponding to each input text.
    """
    # Convert the texts into numerical representations using the vectorizer
    text_vectors = vectorizer.transform(texts)
    
    # Make predictions using the trained model
    predictions = model.predict(text_vectors)
    
    # Convert predictions to sentiment labels
    sentiments = []
    for pred in predictions:
        if pred == 1:
            sentiments.append('Positive')
        elif pred == -1:
            sentiments.append('Negative')
        else:
            sentiments.append('Neutral')
    
    return sentiments