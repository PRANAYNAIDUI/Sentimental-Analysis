import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import spacy

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

# Sample text data
text = "This is an example sentence for tokenization. It's a great tool for NLP tasks!"

# Using NLTK for word-level tokenization
word_tokens = word_tokenize(text)
print("Word Tokens (NLTK):", word_tokens)

# Using spaCy for tokenization
doc = nlp(text)
spacy_tokens = [token.text for token in doc]
print("Tokens (spaCy):", spacy_tokens)

# Sentence-level tokenization using NLTK
sent_tokens = sent_tokenize(text)
print("Sentence Tokens:", sent_tokens)