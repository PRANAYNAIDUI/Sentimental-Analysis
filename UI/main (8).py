# app.py
from flask import Flask, render_template, request
import pickle
from sentiment_model import SentimentModel  # From previous tasks

app = Flask(__name__)

# Load the saved model and vectorizer
model = SentimentModel()
model.load_model("sentiment_model.pkl")
model.load_vectorizer("vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form.get("text")
    sentiment, confidence = model.predict(text)
    return render_template("results.html", 
                         text=text, 
                         sentiment=sentiment,
                         confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)