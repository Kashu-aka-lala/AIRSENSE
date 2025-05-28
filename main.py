from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel

app = FastAPI()

# Load your model
model = joblib.load("AQI_model.pkl")

# Define input schema
class PollutantInput(BaseModel):
    co: float
    no2: float
    o3: float
    so2: float
    pm2_5: float
    pm10: float

# Define a prediction endpoint
@app.post("/predict")
def predict_aqi(data: PollutantInput):
    try:
        input_data = [[
            data.co, data.no2, data.o3, data.so2, data.pm2_5, data.pm10
        ]]
        prediction = model.predict(input_data)
        return {"predicted_AQI": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
