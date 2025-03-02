# # #!/usr/bin/env python3
# # from fastapi import FastAPI, File, UploadFile
# # from pydantic import BaseModel
# # import io
# # import pandas as pd
# # from xgboost import XGBClassifier
# # import pickle
# # from fastapi.middleware.cors import CORSMiddleware

# # # Import your custom utility functions.
# # from utility import preprocess_data, get_top_features

# # app = FastAPI()


# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],  # or ["http://localhost:3000"] for a specific domain
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # -------------------------------------------------------------------------
# # # Define the response schema for the /predict endpoint.
# # # -------------------------------------------------------------------------
# # class Response(BaseModel):
# #     riskScore: float
# #     topFeatures: list

# # # -------------------------------------------------------------------------
# # # Model loading function
# # # -------------------------------------------------------------------------
# # def load_model(model_path: str) -> XGBClassifier:
# #     """
# #     Loads an XGBoost model from a JSON file using XGBClassifier's built-in load_model method.
# #     Make sure the model was saved with model.save_model("your_model.json").
# #     """
# #     model = XGBClassifier()  # Create a new XGBClassifier instance
# #     model.load_model(model_path)  # Load model parameters from the JSON file
# #     return model

# # # Set the correct absolute path to your model JSON file.
# # model_path = '/Users/muhammadrashid/Desktop/Mammu/Mammu/GeneSight/GeneSight/Backend/genesight_xgb_model.json'
# # model = load_model(model_path)

# # # -------------------------------------------------------------------------
# # # /predict endpoint
# # # -------------------------------------------------------------------------
# # @app.post("/predict", response_model=Response)
# # async def predict(file: UploadFile = File(...)):
# #     """
# #     Accepts a CSV file upload, preprocesses the data, runs the prediction,
# #     and returns the risk score along with the top features.
# #     """
# #     try:
# #         file_contents = await file.read()
# #         # Read the CSV data from the uploaded file
# #         data = pd.read_csv(io.StringIO(file_contents.decode('utf-8')))
# #     except Exception as e:
# #         return {"riskScore": 0.0, "topFeatures": [{"error": f"Failed to read CSV: {e}"}]}

# #     # Preprocess the data using your utility function.
# #     try:
# #         processed_data = preprocess_data(data)
# #     except Exception as e:
# #         return {"riskScore": 0.0, "topFeatures": [{"error": f"Preprocessing error: {e}"}]}

# #     # Run the model prediction and extract top features.
# #     try:
# #         riskScore = model.predict(processed_data)
# #         topFeatures = get_top_features(model, processed_data)
# #     except Exception as e:
# #         return {"riskScore": 0.0, "topFeatures": [{"error": f"Prediction error: {e}"}]}
    
# #     return {
# #         "riskScore": float(riskScore[0]),
# #         "topFeatures": topFeatures
# #     }

# # # -------------------------------------------------------------------------
# # # /stats endpoint
# # # -------------------------------------------------------------------------
# # @app.get("/stats")
# # async def stats():
# #     """
# #     A simple endpoint that returns usage statistics.
# #     """
# #     return {"profile": 100, "averageInferenceTime": "0.75s"}

# # # -------------------------------------------------------------------------
# # # Root endpoint
# # # -------------------------------------------------------------------------
# # @app.get("/")
# # async def root():
# #     """
# #     Root endpoint which provides a welcome message.
# #     """
# #     return {"message": "Welcome to GeneSight API"}


# #!/usr/bin/env python3
# from fastapi import FastAPI, File, UploadFile
# from pydantic import BaseModel
# import io
# import pandas as pd
# from xgboost import XGBClassifier
# from fastapi.middleware.cors import CORSMiddleware

# # Import your custom utility functions from utility.py
# from utility import preprocess_data, get_top_features

# app = FastAPI()

# # Enable CORS (adjust allow_origins as needed)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Change to specific domains if desired
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # -------------------------------------------------------------------------
# # Define the response schema for the /predict endpoint.
# # -------------------------------------------------------------------------
# class Response(BaseModel):
#     riskScore: float
#     topFeatures: list

# # -------------------------------------------------------------------------
# # Model loading function
# # -------------------------------------------------------------------------
# def load_model(model_path: str) -> XGBClassifier:
#     """
#     Loads an XGBoost model from a JSON file.
#     Make sure the model was saved with model.save_model("your_model.json").
#     """
#     model = XGBClassifier()  # Create a new XGBClassifier instance
#     model.load_model(model_path)  # Load model parameters from the JSON file
#     return model

# # Set the absolute path to your model JSON file.
# model_path = '/Users/muhammadrashid/Desktop/Mammu/Mammu/GeneSight/GeneSight/Backend/genesight_xgb_model.json'
# model = load_model(model_path)

# # -------------------------------------------------------------------------
# # /predict endpoint
# # -------------------------------------------------------------------------
# @app.post("/predict", response_model=Response)
# async def predict(file: UploadFile = File(...)):
#     """
#     Accepts a CSV file upload, preprocesses the data, runs the prediction,
#     and returns the risk score along with the top features.
#     """
#     try:
#         file_contents = await file.read()
#         # Read CSV data from the uploaded file
#         data = pd.read_csv(io.StringIO(file_contents.decode('utf-8')))
#     except Exception as e:
#         return {"riskScore": 0.0, "topFeatures": [{"error": f"Failed to read CSV: {e}"}]}

#     # Preprocess the data using the custom function.
#     try:
#         processed_data = preprocess_data(data)
#     except Exception as e:
#         return {"riskScore": 0.0, "topFeatures": [{"error": f"Preprocessing error: {e}"}]}

#     # Run the model prediction and extract top features.
#     try:
#         riskScore = model.predict(processed_data)
#         topFeatures = get_top_features(model, processed_data)
#     except Exception as e:
#         return {"riskScore": 0.0, "topFeatures": [{"error": f"Prediction error: {e}"}]}
    
#     return {
#         "riskScore": float(riskScore[0]),
#         "topFeatures": topFeatures
#     }

# # -------------------------------------------------------------------------
# # /stats endpoint
# # -------------------------------------------------------------------------
# @app.get("/stats")
# async def stats():
#     """
#     A simple endpoint that returns usage statistics.
#     """
#     return {"profile": 100, "averageInferenceTime": "0.75s"}

# # -------------------------------------------------------------------------
# # Root endpoint
# # -------------------------------------------------------------------------
# @app.get("/")
# async def root():
#     """
#     Root endpoint which provides a welcome message.
#     """
#     return {"message": "Welcome to GeneSight API"}


#!/usr/bin/env python3
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import io
import pandas as pd
from xgboost import XGBClassifier
import pickle
from fastapi.middleware.cors import CORSMiddleware

# Import utility functions from our module.
from utility import preprocess_data, get_top_features

app = FastAPI()

# Enable CORS (adjust allowed origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, specify the domain, e.g., ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------------------
# Response schema for /predict
# -------------------------------------------------------------------------
class Response(BaseModel):
    riskScore: float
    topFeatures: list

# -------------------------------------------------------------------------
# Function to load the model from JSON file
# -------------------------------------------------------------------------
def load_model(model_path: str) -> XGBClassifier:
    """
    Loads an XGBoost model from a JSON file.
    The model should have been saved using model.save_model("your_model.json").
    """
    model = XGBClassifier()  # Create a new instance
    model.load_model(model_path)  # Load parameters from the JSON file
    return model

# Set your absolute model file path (update this as needed)
model_path = '/Users/muhammadrashid/Desktop/Mammu/Mammu/GeneSight/GeneSight/Backend/genesight_xgb_model.json'
model = load_model(model_path)

# -------------------------------------------------------------------------
# /predict endpoint
# -------------------------------------------------------------------------
@app.post("/predict", response_model=Response)
async def predict(file: UploadFile = File(...)):
    """
    Accepts a CSV file upload, preprocesses the data, runs prediction,
    and returns the risk score and top features.
    """
    try:
        file_contents = await file.read()
        # Read CSV data from uploaded file
        data = pd.read_csv(io.StringIO(file_contents.decode('utf-8')))
    except Exception as e:
        return {"riskScore": 0.0, "topFeatures": [{"error": f"Failed to read CSV: {e}"}]}
    
    try:
        # Preprocess the data
        processed_data = preprocess_data(data)
    except Exception as e:
        return {"riskScore": 0.0, "topFeatures": [{"error": f"Preprocessing error: {e}"}]}
    
    try:
        # Run model prediction and extract top features
        riskScore = model.predict(processed_data)
        topFeatures = get_top_features(model, processed_data)
    except Exception as e:
        return {"riskScore": 0.0, "topFeatures": [{"error": f"Prediction error: {e}"}]}
    
    return {
        "riskScore": float(riskScore[0]),
        "topFeatures": topFeatures
    }

# -------------------------------------------------------------------------
# /stats endpoint
# -------------------------------------------------------------------------
@app.get("/stats")
async def stats():
    """
    Returns simple usage statistics.
    """
    return {"profile": 100, "averageInferenceTime": "0.75s"}

# -------------------------------------------------------------------------
# Root endpoint
# -------------------------------------------------------------------------
@app.get("/")
async def root():
    """
    Returns a welcome message.
    """
    return {"message": "Welcome to GeneSight API"}
