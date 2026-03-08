import pickle
import os
from preprocess import clean_text

# Get project root directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))

model_path = os.path.join(project_root, "models", "fake_news_detection.pkl")
vectorizer_path = os.path.join(project_root, "models", "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

def predict_news(news):

    cleaned = clean_text(news)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)

    if prediction[0] == 0:
        return "Fake News"
    else:
        return "Real News"