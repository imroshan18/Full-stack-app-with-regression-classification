from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

# Initialize FastAPI app
app = FastAPI(title="SmartEvent Pro API", description="Combined Classification and Regression for Event Analysis")

# Load models
try:
    classifier = joblib.load('models/classifier.joblib')
    regressor = joblib.load('models/regressor.joblib')
except Exception as e:
    print(f"Error loading models: {e}")

# Define input schema
class EventInput(BaseModel):
    temp: float
    rain_prob: float
    social_reach: float
    is_weekend: int

# Define output schema
class PredictionOutput(BaseModel):
    status: str
    attendance: int
    message: str

@app.post("/predict", response_model=PredictionOutput)
async def predict(data: EventInput):
    # Prepare features for prediction
    features = [[data.temp, data.rain_prob, data.social_reach, data.is_weekend]]
    
    # 1. Classification prediction
    status_code = classifier.predict(features)[0]
    status = "Success" if status_code == 1 else "Cancelled"
    
    # 2. Regression prediction
    attendance = int(regressor.predict(features)[0])
    
    # Custom message logic
    if status == "Cancelled":
        message = "Warning: High risk of cancellation due to weather conditions."
        attendance = 0 # Force 0 if cancelled for consistency, though model might predict small values
    else:
        message = "Success: Weather conditions are favorable for the event."
    
    return {
        "status": status,
        "attendance": attendance,
        "message": message
    }

@app.get("/")
async def root():
    return {"message": "Welcome to SmartEvent Pro API. Use /predict for analysis."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
