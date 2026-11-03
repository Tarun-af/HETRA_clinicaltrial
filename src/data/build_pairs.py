import pandas as pd

patients = pd.read_csv(
    "data/processed/patients.csv"
)

qrels = pd.read_csv(
    "data/raw/qrels2021.txt",
    sep=r"\s+",
    header=None,
    names=["patient_id", "iteration", "trial_id", "relevance"]
)

pairs = qrels.merge(
    patients,
    on="patient_id",
    how="left"
)

pairs = pairs[
    ["patient_id", "patient_text", "trial_id", "relevance"]
]

print("Shape:")
print(pairs.shape)

print("\nFirst 10 rows:")
print(pairs.head(10))

print("\nMissing patient text:")
print(pairs["patient_text"].isna().sum())

pairs.to_csv(
    "data/processed/patient_trial_pairs.csv",
    index=False
)

print("\nSaved to data/processed/patient_trial_pairs.csv")