import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_input_text(text):
    """
    Preprocesses raw input text to prepare it for sentiment analysis.
    
    Args:
        text (str): Raw input text to be processed
    
    Returns:
        array: TF-IDF vectorized form of the input text
    """
    
    # Step 1: Clean the text
    # Remove special characters and punctuation
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Convert to lowercase
    cleaned_text = cleaned_text.lower()
    
    # Step 2: Tokenize the text
    tokens = word_tokenize(cleaned_text)
    
    # Step 3: Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Step 4: Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    
    # Join tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)
    
    # Step 5: Vectorize the text using TF-IDF
    # Initialize TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit the vectorizer to our training data and transform the input text
    # Note: In a real scenario, the vectorizer should be fitted on the training data
    # For this example, we'll fit it on the processed text
    tfidf_matrix = vectorizer.fit_transform([processed_text])
    
    return tfidf_matrix

# Example usage
sample_text = "I really enjoyed the new product! It's amazing."
preprocessed_text = preprocess_input_text(sample_text)
print("Preprocessed Text:")
print(preprocessed_text)