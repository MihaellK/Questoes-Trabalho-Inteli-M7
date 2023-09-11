# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("api_adaBoost")

# Create input/output pydantic models
input_model = create_model("api_adaBoost_input", **{'rank': 312, 'Youtuber': 'Goldmines Cineplex', 'subscribers': 22500000, 'video views': 2431154432.0, 'category': 'Film & Animation', 'uploads': 3377, 'Country': 'India', 'channel_type': 'Film', 'video_views_rank': 3793.0, 'country_rank': 64.0, 'channel_type_rank': 23.0, 'video_views_for_the_last_30_days': 48740000.0, 'lowest_monthly_earnings': 12200.0, 'highest_monthly_earnings': 195000.0, 'lowest_yearly_earnings': 146200.0, 'subscribers_for_last_30_days': 200000.0, 'Gross tertiary education enrollment (%)': 28.100000381469727, 'Population': 1366417792.0, 'Unemployment rate': 5.360000133514404})
output_model = create_model("api_adaBoost_output", prediction=108400000.0)


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
