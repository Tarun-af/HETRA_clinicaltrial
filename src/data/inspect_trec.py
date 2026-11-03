import pandas as pd

qrels = pd.read_csv(
    "data/raw/qrels2021.txt",
    sep=r"\s+",
    header=None,
    names=["patient_id", "iteration", "trial_id", "relevance"]
)

print("Shape:")
print(qrels.shape)

print("\nFirst 10 rows:")
print(qrels.head(10))

print("\nRelevance counts:")
print(qrels["relevance"].value_counts())

print("\nUnique patients:")
print(qrels["patient_id"].nunique())

print("\nUnique trials:")
print(qrels["trial_id"].nunique())