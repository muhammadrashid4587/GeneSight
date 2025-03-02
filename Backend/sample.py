import pandas as pd
df = pd.read_csv('/Users/muhammadrashid/Desktop/Mammu/Mammu/GeneSight/GeneSight/Backend/data/GSE33000_series_matrix.txt', sep='\t',comment='!')
print(df.head())