#!/usr/bin/env python3
import pandas as pd
import numpy as np
import os
import joblib
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from xgboost import XGBClassifier

# -------------------------------------------------------------------------
# 1) DISEASE MAPPINGS + PARSING
# -------------------------------------------------------------------------
DISEASE_MAPPINGS = {
    "alzheimer": "AD",
    "huntington": "HD", 
    "parkinson": "PD",
    "als": "ALS",
    "multiple sclerosis": "MS",
    "frontotemporal dementia": "FTD",
    "lewy body": "LBD",
    "schizophrenia": "SCZ",
    "bipolar": "BP",
    "non-demented": "Control",
    "healthy": "Control",
    "normal": "Control"
}

def parse_diseases_columnwise(file_path):
    """
    Reads lines from a GEO Series Matrix file to map each sample (GSM####) 
    to a disease label. It looks for:
      - !Sample_geo_accession  -> GSM IDs
      - !Sample_characteristics_ch2 -> disease text
    Then matches the disease text with DISEASE_MAPPINGS.
    """
    sample_accessions = []
    disease_strings = []
    
    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("!Sample_geo_accession"):
                    tokens = line.split("\t")
                    sample_accessions = [t.strip().strip('"') for t in tokens[1:]]
                elif line.startswith("!Sample_characteristics_ch2"):
                    tokens = line.split("\t")
                    disease_strings = [t.strip().strip('"').lower() for t in tokens[1:]]
    except Exception as e:
        print(f"Error reading {file_path} in parse_diseases_columnwise: {e}")
        return {}
    
    print(f"DEBUG: Found {len(sample_accessions)} sample accessions.")
    print(f"DEBUG: Found {len(disease_strings)} disease entries.")
    
    sample_labels = {}
    for i, accession in enumerate(sample_accessions):
        if i < len(disease_strings):
            text = disease_strings[i]
            assigned = False
            for keyword, label in DISEASE_MAPPINGS.items():
                if keyword in text:
                    sample_labels[accession] = label
                    assigned = True
                    break
            if not assigned:
                sample_labels[accession] = None
        else:
            sample_labels[accession] = None
    
    return sample_labels

def load_and_prepare_data(file_path):
    """
    Loads a GEO Series Matrix file into a DataFrame with rows as samples and 
    columns as gene expression values, plus a 'condition' column (from metadata).
    If an error occurs or the file is missing expected columns, returns an empty DataFrame.
    """
    try:
        df = pd.read_csv(file_path, sep="\t", comment="!", on_bad_lines='skip')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.DataFrame()
    
    if df.empty:
        print(f"Dataset {file_path} is empty after reading.")
        return pd.DataFrame()
    
    if "ID_REF" not in df.columns:
        print(f"Dataset {file_path} does not contain the expected 'ID_REF' column.")
        return pd.DataFrame()
    
    df.set_index("ID_REF", inplace=True)
    df_t = df.transpose()
    df_t.index = df_t.index.str.strip().str.strip('"')
    print("\nDEBUG df_t.index[:5]:", list(df_t.index[:5]))
    
    labels_dict = parse_diseases_columnwise(file_path)
    df_t["condition"] = df_t.index.map(labels_dict)
    df_t.dropna(subset=["condition"], inplace=True)
    print("\nLabel counts (all diseases):\n", df_t["condition"].value_counts())
    
    return df_t

# -------------------------------------------------------------------------
# 2) COMBINE DATASETS USING UNION OF FEATURES
# -------------------------------------------------------------------------
def combine_datasets(file_paths):
    """
    Loads each dataset and reindexes each DataFrame to the union of all gene columns.
    Missing values are filled later using median imputation.
    """
    dfs = []
    for fp in file_paths:
        print(f"\n=== Loading: {fp} ===")
        df = load_and_prepare_data(fp)
        if df.empty:
            print(f"Skipping {fp} (empty or invalid).")
            continue
        dfs.append(df)
    
    if not dfs:
        print("No valid data to combine.")
        return pd.DataFrame()
    
    # Create the union of all gene columns (exclude 'condition')
    union_genes = set()
    for df in dfs:
        union_genes |= set(df.columns)
    if "condition" in union_genes:
        union_genes.remove("condition")
    union_genes = list(union_genes)
    
    # Reindex each dataframe to have the same columns
    new_dfs = []
    for df in dfs:
        df_reindexed = df.reindex(columns=union_genes + ["condition"])
        new_dfs.append(df_reindexed)
    
    combined_df = pd.concat(new_dfs, axis=0)
    combined_df.reset_index(drop=True, inplace=True)
    
    print("\nCombined dataset shape (before imputation):", combined_df.shape)
    print("Combined label counts:\n", combined_df["condition"].value_counts())
    
    # Fill missing values with median imputation for each gene column
    gene_columns = [col for col in combined_df.columns if col != "condition"]
    for col in gene_columns:
        median_val = combined_df[col].median()
        combined_df[col] = combined_df[col].fillna(median_val)
    
    print("\nCombined dataset shape (after imputation):", combined_df.shape)
    return combined_df

# -------------------------------------------------------------------------
# 3) TRAIN A MULTI-CLASS MODEL ON COMBINED DATA
# -------------------------------------------------------------------------
def train_multiclass_model(df):
    """
    Trains a multi-class model for disease prediction on the combined dataset.
    """
    X = df.drop(columns=["condition"])
    y = df["condition"]
    
    if y.nunique() < 2:
        print("Not enough classes for multi-class training. Skipping.")
        return None, None
    
    le = LabelEncoder()
    y_enc = le.fit_transform(y)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_enc, test_size=0.2, random_state=42
    )
    
    model = XGBClassifier(
        use_label_encoder=False,
        objective='multi:softprob',
        eval_metric='mlogloss'
    )
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print("\nCombined Multi-class Accuracy:", acc)
    print("Confusion Matrix:\n", confusion_matrix(y_test, preds))
    print("Classification Report:\n", classification_report(
        y_test, preds, target_names=le.classes_
    ))
    
    return model, le

# -------------------------------------------------------------------------
# 4) DEMO PREDICTION ON TRAINING DATA (For demonstration)
# -------------------------------------------------------------------------
def demo_prediction(model, label_encoder, df):
    """
    Runs a demo prediction on one sample from the combined dataset.
    Also prints the prediction probabilities and prevention tips.
    """
    if model is None or label_encoder is None or df.empty:
        print("No model or data for demo prediction.")
        return
    
    sample = df.drop(columns=["condition"]).iloc[0:1]
    true_label = df["condition"].iloc[0]
    
    pred_class = model.predict(sample)[0]
    predicted_disease = label_encoder.inverse_transform([pred_class])[0]
    
    print(f"\nDemo Prediction on first sample:")
    print(f"True label: {true_label}")
    print(f"Predicted: {predicted_disease}")
    
    probs = model.predict_proba(sample)[0]
    for i, disease in enumerate(label_encoder.classes_):
        print(f"  {disease}: {probs[i]*100:.2f}%")
    
    # Print prevention tips for the predicted disease
    tips = get_prevention_tips(predicted_disease)
    print("\nPrevention Tips:")
    for tip in tips:
        print("  -", tip)

# -------------------------------------------------------------------------
# 5) PREVENTION TIPS FUNCTION
# -------------------------------------------------------------------------
def get_prevention_tips(disease):
    tips = {
        "AD": [
            "Maintain a healthy diet rich in antioxidants.",
            "Engage in regular physical activity.",
            "Keep mentally active and socially engaged."
        ],
        "HD": [
            "Consult with a neurologist regularly.",
            "Consider genetic counseling if at risk."
        ],
        "PD": [
            "Monitor and manage environmental risk factors.",
            "Engage in regular exercise."
        ],
        "ALS": [
            "Seek early specialist care and monitor symptoms closely."
        ],
        "MS": [
            "Consider vitamin D supplements and regular physical activity.",
            "Stay in close contact with your healthcare provider."
        ],
        "FTD": [
            "Maintain cognitive activities and social engagement."
        ],
        "LBD": [
            "Follow a balanced lifestyle and regular medical check-ups."
        ],
        "SCZ": [
            "Maintain a structured routine and seek therapy if needed."
        ],
        "BP": [
            "Monitor mood changes and maintain a regular sleep schedule."
        ],
        "Control": [
            "Maintain a balanced diet and regular exercise to stay healthy."
        ]
    }
    return tips.get(disease, ["No specific prevention tips available."])

# -------------------------------------------------------------------------
# 6) FUNCTIONS FOR TESTING PREDICTION ON NEW SAMPLES
# -------------------------------------------------------------------------
def create_dummy_sample_csv(filepath, feature_names):
    """
    Creates a dummy CSV file with one sample containing random gene expression values.
    The CSV will have columns as specified in feature_names.
    """
    data = {gene: [np.random.rand()] for gene in feature_names}
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"Dummy sample CSV created at {filepath}")

def test_sample_prediction(model, label_encoder, sample_filepath):
    """
    Loads a sample CSV file, runs the model prediction, and prints the predicted
    disease along with risk probabilities and prevention tips.
    Assumes the CSV contains only gene expression columns matching the model's training features.
    """
    df_sample = pd.read_csv(sample_filepath)
    pred_class = model.predict(df_sample)[0]
    predicted_disease = label_encoder.inverse_transform([pred_class])[0]
    print("\nTest Sample Prediction:")
    print("Predicted Disease:", predicted_disease)
    probs = model.predict_proba(df_sample)[0]
    for i, d in enumerate(label_encoder.classes_):
        print(f"  {d}: {probs[i]*100:.2f}%")
    tips = get_prevention_tips(predicted_disease)
    print("\nPrevention Tips:")
    for tip in tips:
        print("  -", tip)

# -------------------------------------------------------------------------
# 7) MAIN
# -------------------------------------------------------------------------
def main():
    # List of file paths for the training datasets.
    # Update these paths as needed to point to your data files.
    files = [
    "GSE33000_series_matrix.txt",
    "GSE4595 Series Matrix.txt",
    "GSE19188 Series Matrix.txt",
    "GSE20966 Series Matrix.txt",
    "GSE21942 Series Matrix.txt",
    "GSE47561 RMA Renormalized Data.txt",
    "GDS2821 Full Data",
    "GSE4588 Series Matrix.txt"
]


    combined_df = combine_datasets(files)
    if combined_df.empty:
        print("Combined dataset is empty. Exiting.")
        return
    
    model, label_encoder = train_multiclass_model(combined_df)
    if model is None:
        print("Could not train a multi-class model (not enough classes).")
        return
    
    demo_prediction(model, label_encoder, combined_df)
    
    # --- OPTIONAL: Test prediction on a dummy new sample ---
    # # For testing, we take a subset (first 10 genes) of the training features.
    # sample_features = combined_df.drop(columns=["condition"]).columns.tolist()[:10]  # adjust as needed
    # dummy_sample_path = "dummy_sample.csv"
    # create_dummy_sample_csv(dummy_sample_path, sample_features)
    # test_sample_prediction(model, label_encoder, dummy_sample_path)

if __name__ == "__main__":
    main()
