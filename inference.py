import pickle
import os

BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))

def predict_news(text):

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]

    prob = model.predict_proba(vector)[0]
    confidence = max(prob)

    if prediction == 0:
        return "Fake", confidence
    else:
        return "Real", confidence