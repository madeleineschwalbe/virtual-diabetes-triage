from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import traceback

app = FastAPI(title="Virtual Diabetes Clinic")

# Load trained model
model = joblib.load("app/model.pkl")
MODEL_VERSION = "v0.1"

# Define input schema
class PatientFeatures(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

@app.get("/health")
def health():
    return {"status": "ok", "model_version": MODEL_VERSION}

@app.post("/predict")
def predict(features: PatientFeatures):
    try:
        data = [[
            features.age, features.sex, features.bmi, features.bp,
            features.s1, features.s2, features.s3, features.s4, features.s5, features.s6
        ]]
        prediction = model.predict(data)[0]
        return {"prediction": float(prediction)}
    except Exception:
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="Bad input format")