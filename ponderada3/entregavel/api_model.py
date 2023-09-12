# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("api_model")

# Create input/output pydantic models
input_model = create_model("api_model_input", **{'video_views_for_the_last_30_days': 180020992.0, 'lowest_monthly_earnings': 45000.0, 'highest_monthly_earnings': 720100.0, 'lowest_yearly_earnings': 540100.0})
output_model = create_model("api_model_output", prediction=108400000.0)


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
