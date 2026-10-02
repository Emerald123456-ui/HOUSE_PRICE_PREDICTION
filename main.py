
from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel
import pandas as pd

with open("house_price_model.pkl", "rb") as file:
    model =pickle.load(file)


app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices using a machine learning pipeline",
    version="1.0.0"
)


class  HouseData(BaseModel):
    Id: int
    Area: int
    Bedrooms: int
    Bathrooms: int
    Floors: int
    YearBuilt: int
    Location: str
    Condition: str
    Garage: str

@app.get("/")
def home():
    return {"message":"welcome to the house price prediction API"}

 


@app.post("/predict")
def predict(house: HouseData):

    # Convert the validated input into a dictionary
    house_dict = {
        "Id": house.Id,
        "Area": house.Area,
        "Bedrooms": house.Bedrooms,
        "Bathrooms": house.Bathrooms,
        "Floors": house.Floors,
        "YearBuilt": house.YearBuilt,
        "Location": house.Location,
        "Condition": house.Condition,
        "Garage": house.Garage
    }
     # Convert dictionary into a one-row DataFrame
    house_data = pd.DataFrame([house_dict])

    # Make prediction using the trained pipeline
    prediction = model.predict(house_data)

    # Return the prediction
    return {
        "predicted_price": float(prediction[0])
    }

# basemodel is a class from pandrytic , we didnt form or make it
    