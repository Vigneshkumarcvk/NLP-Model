import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from preprocess import clean_text

# Load dataset
df = pd.read_csv("../data/fake_news_dataset_4000_rows.csv")

# Combine title and text
df["content"] = df["title"].fillna("") + " " + df["text"].fillna("")

# Clean text
df["content"] = df["content"].apply(clean_text)

# Split data
x = df["content"]
y = df["label"]

# TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=5000)
x = vectorizer.fit_transform(x)

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(x_train, y_train)

# Predictions
y_pred = model.predict(x_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Save model
pickle.dump(model, open("../models/fake_news_detection.pkl", "wb"))
pickle.dump(vectorizer, open("../models/vectorizer.pkl", "wb"))