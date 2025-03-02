#!/usr/bin/env python3
import pandas as pd
import joblib
from xgboost import XGBClassifier

# Prevention tips dictionary (same as in your model file)
PREVENTION_TIPS = {
    "AD": "Engage in regular cognitive exercises, maintain a balanced diet rich in antioxidants, and schedule regular check-ups.",
    "HD": "Consider genetic counseling, and explore physical therapy and stress reduction techniques.",
    "PD": "Regular exercise, a Mediterranean diet, and early neurologist consultation may help manage risk.",
    "ALS": "Avoid exposure to toxins, maintain a healthy lifestyle, and consult specialists if early symptoms appear.",
    "MS": "Avoid smoking, maintain vitamin D levels, and follow a healthy, balanced lifestyle.",
    "FTD": "Stay socially active, engage in mental exercises, and get regular medical evaluations.",
    "LBD": "Maintain a healthy diet, exercise regularly, and consult with healthcare providers early.",
    "SCZ": "Early intervention, consistent medication, and strong support networks are key.",
    "BP": "Following treatment plans including therapy and medication, as well as stress management, can help.",
    "Control": "Keep a balanced diet, exercise regularly, and maintain routine health check-ups."
}

def get_prevention_tips(disease_label):
    return PREVENTION_TIPS.get(disease_label, "No specific prevention tips available.")

def load_model_and_encoder(model_path, encoder_path):
    # Load your XGBoost model (saved with .json) and label encoder (via joblib)
    model = XGBClassifier()
    model.load_model(model_path)
    encoder = joblib.load(encoder_path)
    return model, encoder

def test_samples(sample_file, model, encoder):
    """
    Reads a sample file (in CSV/TSV format with the same gene columns as training data),
    predicts the disease label for each sample, and prints the prediction with risk probabilities and prevention tips.
    """
    # Load sample data – ensure this file has the same columns as the training features.
    # (Do not include the 'condition' column.)
    try:
        df_samples = pd.read_csv(sample_file, sep="\t")
    except Exception as e:
        print(f"Error reading sample file: {e}")
        return

    predictions = model.predict(df_samples)
    probabilities = model.predict_proba(df_samples)
    predicted_labels = encoder.inverse_transform(predictions)
    
    for i, label in enumerate(predicted_labels):
        print(f"\nSample {i+1}:")
        print(f"  Predicted Disease: {label}")
        print("  Risk probabilities:")
        for j, disease in enumerate(encoder.classes_):
            print(f"    {disease}: {probabilities[i][j]*100:.2f}%")
        tips = get_prevention_tips(label)
        print(f"  Prevention Tips for {label}: {tips}")

if __name__ == "__main__":
    # Update these paths to match where your model and encoder were saved.
    model_path = "models/multiclass_disease_model.json"
    encoder_path = "models/label_encoder.joblib"
    
    # Path to your sample file (should be formatted with the same gene feature columns as in training)
    sample_file = "sample_data.txt"  # Replace with your actual file name
    
    model, encoder = load_model_and_encoder(model_path, encoder_path)
    test_samples(sample_file, model, encoder)
