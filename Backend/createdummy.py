import pandas as pd
import numpy as np

# Replace with your model's actual feature names
features = ["Gene_101", "Gene_245", "Gene_500"]
data = {gene: [np.random.rand()] for gene in features}
dummy_df = pd.DataFrame(data)
dummy_df.to_csv("dummy_sample.csv", index=False)
print("Dummy CSV file created as dummy_sample.csv")
