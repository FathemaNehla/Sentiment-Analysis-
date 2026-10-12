from datasets import load_dataset
import pandas as pd

dataset = load_dataset("syedkhalid0/Sentiment-Analysis")

data = pd.DataFrame(dataset["train"])

print("Dataset loaded successfully!")
print("Number of rows:", len(data))
print("Columns:", data.columns.tolist())
print(data.head())
