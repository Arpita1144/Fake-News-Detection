from fastapi import FastAPI
from pydantic import BaseModel
from ml.inference import predict_news
from backend.database import init_db
from backend.database import insert_prediction

app = FastAPI()

init_db()

class NewsInput(BaseModel):
    text: str

@app.post("/predict")
def predict(news: NewsInput):
   
    #1️ Run model prediction
    prediction, prob = predict_news(news.text)

    #2️ Save prediction to SQLite  ← ADD HERE
    insert_prediction(news.text, prediction, prob)

    #3️ Return result to frontend
    return {
        "prediction": "Fake" if prediction == 1 else "Real",
        "confidence": float(prob)
    }