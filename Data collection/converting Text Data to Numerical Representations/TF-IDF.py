from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Sample text data (assuming 'text_data' contains your preprocessed text)
text_data = [
    "This is a sample positive review",
    "Another example of negative feedback",
    "Neutral comment for testing purposes"
]

# Initialize the TF-IDF vectorizer
# Parameters explained:
# - max_features: Limit the number of features (words) to consider
# - stop_words: Remove common words like 'the', 'and' etc.
# - ngram_range: Consider both single words and bigrams
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words='english',
    ngram_range=(1, 2)
)

# Fit the vectorizer to the text data and transform it into TF-IDF vectors
tfidf_vectors = vectorizer.fit_transform(text_data)

# Convert the sparse matrix to a dense numpy array for easier manipulation
tfidf_vectors = tfidf_vectors.toarray()

print("TF-IDF Vector Shape:", tfidf_vectors.shape)
print("Sample TF-IDF Vectors:")
print(tfidf_vectors[:2, :4])  # Display first 4 features for first 2 samples