# Test with a positive sentiment
print(predict_sentiment("I love this product!"))  # Expected output: 'Positive'

# Test with a negative sentiment
print(predict_sentiment("This product is terrible."))  # Expected output: 'Negative'

# Test with a neutral sentiment
print(predict_sentiment("This product is okay."))  # Expected output: 'Neutral'

# Test batch processing
texts = [
    "I'm so happy with this service!",
    "This is the worst experience ever.",
    "The product is decent but not great."
]
print(predict_sentiments(texts))
# Expected output: ['Positive', 'Negative', 'Neutral']