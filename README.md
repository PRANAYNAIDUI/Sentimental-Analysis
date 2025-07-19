# 💬 Sentimental Analysis using Machine Learning 🧠💡

Welcome to the **Sentimental Analysis** project! 🎯  
This repo is a complete machine learning pipeline that classifies text data as **positive 😊**, **negative 😠**, or **neutral 😐**. It's perfect for analyzing reviews, tweets, feedback, and more.  

Whether you're a beginner exploring NLP or a data scientist building emotion-aware products — this project has you covered! 💪🚀

---

## 📌 Features

✨ Clean & preprocess raw text  
✨ Train multiple ML models  
✨ Predict sentiment for new inputs  
✨ Evaluate results with metrics & plots  
✨ Modular & extensible design  

---

## 📂 Dataset

- 📁 Source: IMDb reviews or custom CSV
- 📄 Fields: `text`, `label`
- 🏷️ Labels:
  - ✅ Positive (`1`)
  - ❌ Negative (`0`)
  - 😐 Neutral (`optional`, depending on dataset)

---

## ⚙️ Technologies Used

- 🐍 Python 3.8+
- 🔤 NLTK for text preprocessing
- 📦 Pandas & NumPy
- 📈 Scikit-learn (ML Models, Metrics)
- 📊 Seaborn & Matplotlib (Visualizations)
- 🧪 Jupyter Notebook (for exploration)

---
Enter your text: I love this movie. It was amazing and emotional!

Cleaned Text: love movie amazing emotional
Predicted Sentiment: ✅ Positive

---

Enter your text: This product is terrible. Waste of money.

Cleaned Text: product terrible waste money
Predicted Sentiment: ❌ Negative

---

Enter your text: The service was okay, nothing special.

Cleaned Text: service okay nothing special
Predicted Sentiment: 😐 Neutral

▶️ How to Run
📒 Option 1: Jupyter Notebook

jupyter notebook sentiment_analysis.ipynb

🐍 Option 2: Python Script

python sentiment_analysis.py

## 🛠️ Installation & Setup

```bash
# 📥 Clone the repo
git clone https://github.com/PRANAYNAIDUI/Sentimental-Analysis.git
cd Sentimental-Analysis

# 🧪 Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 📦 Install dependencies
pip install -r requirements.txt
--- 
