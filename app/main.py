from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="MailSpam API")

# Load model
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

class EmailRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "MailSpam API is running"}

@app.post("/predict")
def predict(data: EmailRequest):
    vector = vectorizer.transform([data.text])
    prediction = model.predict(vector)[0]

    return {
        "prediction": "Spam" if prediction == 1 else "Not Spam"
    }