from flask import Flask, render_template, request
from your_sentiment_model import analyze_sentiment  # Import your model

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form.get('text')
        if not text:
            return render_template('index.html', result=None)
        
        # Here you would call your sentiment analysis function
        sentiment_result = analyze_sentiment(text)
        
        return render_template('index.html', result=sentiment_result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)