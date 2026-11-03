import pandas as pd

patients = pd.read_csv(
    "data/processed/patients.csv"
)

qrels = pd.read_csv(
    "data/processed/prototype_qrels.csv"
)

trials = pd.read_csv(
    "data/processed/prototype_trials.csv"
)

# Add patient text
data = qrels.merge(
    patients,
    on="patient_id",
    how="left"
)

# Add trial information
data = data.merge(
    trials,
    on="trial_id",
    how="inner"
)

# Select useful columns
data = data[
    [
        "patient_id",
        "trial_id",
        "patient_text",
        "title",
        "conditions",
        "eligibility",
        "minimum_age",
        "maximum_age",
        "sex",
        "relevance"
    ]
]

print("Final dataset shape:")
print(data.shape)

print("\nRelevance counts:")
print(data["relevance"].value_counts())

print("\nMissing patient text:")
print(data["patient_text"].isna().sum())

print("\nMissing eligibility:")
print(data["eligibility"].isna().sum())

print("\nFirst example:")
print(data.iloc[0])

data.to_csv(
    "data/processed/final_prototype.csv",
    index=False
)

print("\nSaved to data/processed/final_prototype.csv")