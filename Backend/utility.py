# # # import pandas as pd 
# # # import numpy as np
# # # def read_csv(filepath):
# # #     df=pd.read_csv(filepath)
# # #     return df

# # # def validate_columns(df,required_columns):
# # #     missing_col=[col for col in required_columns if col not in df.columns]
# # #     if missing_col:
# # #         raise ValueError(f"Missing values columns:{missing_col}")
# # #     return df



# # # def preprocess_data(df,log_transfrom=True,normalize=True):
# # #     if log_transfrom:
# # #         df=df.applymap(lambda x:np.log(x+1))
# # #     if normalize:
# # #         df=(df-df.mean())/df.std()
# # #     return df


# # # def load_preprocess(filepath,required_columns):
# # #     df=pd.read_csv(filepath,sep=None,engine='python')
# # #     validate_columns(df,required_columns)
# # #     df=preprocess_data(df)
# # #     return df


# # # def process_batch(filepath,model,log_transfrom=True,normalize=True):
# # #     df=read_csv(filepath)
# # #     df=validate_columns(df,required_columns=["gene_id","expression_value"])
# # #     df=preprocess_data(df,log_transfrom,normalize)
# # #     predictions=model.predict(df)

# # #     results=[]
# # #     for idx,prediction in enumerate(predictions):
# # #         results.append({"sample_id":df.index[idx],"riskScore":prediction,"topFeatures":get_top_features(model,df.iloc[idx])})
# # #     return results

# # # def get_top_features(model,sample_data):
# # #     priority=model.feature_importances_
# # #     top_genes=sorted(zip(sample_data.columns,priority),key=lambda x:x[1],reverse=True)
# # #     return [{"gene":gene,"importance":imp} for gene,imp in top_genes[:5]]

# # # Update your existing utility.py with these functions
# # # Keep any existing functions you already have in the file

# # import pandas as pd
# # import numpy as np
# # from typing import List, Dict, Any, Union

# # def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
# #     """
# #     Preprocess the input gene expression data for model prediction.
# #     If you already have preprocessing code in data_preprocessing.py,
# #     consider importing and using those functions instead.
    
# #     Args:
# #         data: Raw input data as a pandas DataFrame
        
# #     Returns:
# #         Preprocessed DataFrame ready for model prediction
# #     """
# #     # Make a copy to avoid modifying the original
# #     processed = data.copy()
    
# #     # Check if the dataframe has a 'Gene' or 'gene' column that needs to be set as index
# #     if 'Gene' in processed.columns:
# #         processed.set_index('Gene', inplace=True)
# #     elif 'gene' in processed.columns:
# #         processed.set_index('gene', inplace=True)
    
# #     # Handle missing values
# #     processed.fillna(0, inplace=True)
    
# #     # Ensure the data is in the expected format
# #     # If the data is transposed (genes as rows), we need to transpose it
# #     # This depends on how your model was trained - adjust as needed
# #     if processed.shape[0] > processed.shape[1]:
# #         # If there are more rows than columns, we likely need to transpose
# #         processed = processed.T
    
# #     return processed

# # def get_top_features(model, data: pd.DataFrame, top_n: int = 10) -> List[Dict[str, Any]]:
# #     """
# #     Extract the top contributing features/genes from the model prediction.
    
# #     Args:
# #         model: Trained XGBoost model
# #         data: Preprocessed input data
# #         top_n: Number of top features to return
        
# #     Returns:
# #         List of dictionaries containing gene names and their importance scores
# #     """
# #     try:
# #         # Get feature importance scores from the model
# #         importance_scores = model.get_booster().get_score(importance_type='gain')
        
# #         # Convert to a list of (feature, importance) tuples
# #         feature_importance = [(feature, score) for feature, score in importance_scores.items()]
        
# #         # Sort by importance (descending)
# #         feature_importance.sort(key=lambda x: x[1], reverse=True)
        
# #         # Take the top N features
# #         top_features = feature_importance[:top_n]
        
# #         # Normalize importance scores to [0-1] range
# #         if top_features:
# #             max_importance = max(score for _, score in top_features)
# #             # Return as list of dictionaries
# #             result = [
# #                 {
# #                     "gene": feature,
# #                     "importance": score / max_importance  # Normalize to [0-1]
# #                 }
# #                 for feature, score in top_features
# #             ]
# #         else:
# #             # Fallback if no features found
# #             result = [{"gene": "No significant features found", "importance": 0.0}]
            
# #         return result
        
# #     except Exception as e:
# #         # Fallback in case of error
# #         print(f"Error in get_top_features: {e}")
# #         return [{"gene": f"Error: {str(e)}", "importance": 0.0}]

# import pandas as pd
# import numpy as np
# from typing import List, Dict, Any

# def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
#     """
#     Preprocess the input gene expression data for model prediction.
#     This function:
#       - Sets the index if 'Gene' (or 'gene') is available,
#       - Fills missing values with 0,
#       - Transposes the data if it appears to be in the wrong shape.
    
#     Adjust this function as needed based on your training pipeline.
#     """
#     processed = data.copy()

#     # Set gene names as index if available
#     if 'Gene' in processed.columns:
#         processed.set_index('Gene', inplace=True)
#     elif 'gene' in processed.columns:
#         processed.set_index('gene', inplace=True)
    
#     # Fill missing values
#     processed.fillna(0, inplace=True)
    
#     # If there are more rows than columns, assume genes are rows; transpose to get samples as rows
#     if processed.shape[0] > processed.shape[1]:
#         processed = processed.T
    
#     return processed

# def get_top_features(model, data: pd.DataFrame, top_n: int = 10) -> List[Dict[str, Any]]:
#     """
#     Extract the top contributing features (genes) based on the model's importance scores.
    
#     Args:
#         model: Trained XGBoost model.
#         data: Preprocessed input data (pandas DataFrame).
#         top_n: Number of top features to return.
        
#     Returns:
#         A list of dictionaries with keys "gene" and "importance".
#     """
#     try:
#         # Retrieve feature importances using the booster (importance_type 'gain')
#         importance_scores = model.get_booster().get_score(importance_type='gain')
#         feature_importance = [(feature, float(score)) for feature, score in importance_scores.items()]
#         # Sort by importance descending
#         feature_importance.sort(key=lambda x: x[1], reverse=True)
#         top_features = feature_importance[:top_n]
        
#         # Normalize scores
#         if top_features:
#             max_score = max(score for _, score in top_features)
#             result = [{"gene": feature, "importance": score / max_score} for feature, score in top_features]
#         else:
#             result = [{"gene": "No significant features found", "importance": 0.0}]
        
#         return result
#     except Exception as e:
#         print(f"Error in get_top_features: {e}")
#         return [{"gene": f"Error: {str(e)}", "importance": 0.0}]


import pandas as pd
import numpy as np
from typing import List, Dict, Any

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the input gene expression data for model prediction.
    This function:
      - Sets the index if 'Gene' (or 'gene') is available,
      - Fills missing values with 0,
      - Transposes the data if genes appear as rows.
    
    Adjust this function as needed based on your training pipeline.
    """
    processed = data.copy()

    # If a column for gene names exists, set it as the index.
    if 'Gene' in processed.columns:
        processed.set_index('Gene', inplace=True)
    elif 'gene' in processed.columns:
        processed.set_index('gene', inplace=True)
    
    # Fill missing values with 0
    processed.fillna(0, inplace=True)
    
    # If there are more rows than columns, assume genes are rows and transpose.
    if processed.shape[0] > processed.shape[1]:
        processed = processed.T
    
    return processed

def get_top_features(model, data: pd.DataFrame, top_n: int = 10) -> List[Dict[str, Any]]:
    """
    Extract the top contributing features (genes) from the model's importance scores.
    
    Args:
        model: Trained XGBoost model.
        data: Preprocessed input data (pandas DataFrame).
        top_n: Number of top features to return.
        
    Returns:
        A list of dictionaries with keys "gene" and "importance".
    """
    try:
        # Use the booster to retrieve feature importances (using 'gain' as the importance type)
        importance_scores = model.get_booster().get_score(importance_type='gain')
        # Convert the scores to a list of tuples
        feature_importance = [(feature, float(score)) for feature, score in importance_scores.items()]
        # Sort by score descending
        feature_importance.sort(key=lambda x: x[1], reverse=True)
        top_features = feature_importance[:top_n]
        
        # Normalize the scores to a [0,1] range
        if top_features:
            max_score = max(score for _, score in top_features)
            result = [{"gene": feature, "importance": score / max_score} for feature, score in top_features]
        else:
            result = [{"gene": "No significant features found", "importance": 0.0}]
        
        return result
    except Exception as e:
        print(f"Error in get_top_features: {e}")
        return [{"gene": f"Error: {str(e)}", "importance": 0.0}]
