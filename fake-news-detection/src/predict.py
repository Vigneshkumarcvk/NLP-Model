import pickle
from preprocess import clean_text

model = pickle.load(open("models/fake_news_detection.pkl","rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl","rb"))

def predict_news(news):

    cleaned = clean_text(news)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)

    if prediction[0] == 0:
        return "Fake News"
    else:
        return "Real News"