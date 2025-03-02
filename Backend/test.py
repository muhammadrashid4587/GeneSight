from fastapi import FastAPI,File,UploadFile
from pydantic import BaseModel
import io
import numpy as np
import pandas as pd 
from utility import get_top_features
from api import Response
import pickle
app=FastAPI()
@app.post("/predict",response_model=Response)
async def predict(file:UploadFile=File(...)):
    return {
        "riskScore":0.75,
        "topFeatures":[{"gene":"BRCA1","importance":0.2},{"gene":"TP53","importance":0.18}]
    }


def load_model(model_path):
    with open(model_path,'rb') as f:
        return pickle.load(f)
    
model=load_model('path/to/model.pkl')