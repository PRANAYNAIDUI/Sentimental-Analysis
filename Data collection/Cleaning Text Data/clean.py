import re
import pandas as pd

def clean_text(text):
    """
    Clean the input text by removing special characters, punctuation, 
    and standardizing the format.
    
    Args:
        text (str): Raw text input
    
    Returns:
        str: Cleaned text
    """
    
    # Remove special characters and punctuation except apostrophes
    text = re.sub(r"[^a-zA-Z0-9\s']", ' ', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading and trailing spaces
    text = text.strip()
    
    return text

# Example usage
if __name__ == "__main__":
    # Sample text data
    data = {
        "text": [
            "This is a great product! 😊",
            "I don't like this service...",
            "The food was amazing@",
            "Terrible experience!!",
            "Can't believe the quality..."
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Apply cleaning function to each text entry
    df['clean_text'] = df['text'].apply(clean_text)
    
    print("Original Text:")
    print(df['text'])
    print("\nCleaned Text:")
    print(df['clean_text'])