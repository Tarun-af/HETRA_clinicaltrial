import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv(
    "data/processed/final_prototype.csv"
)

patients = data["patient_id"].unique()

train_patients, test_patients = train_test_split(
    patients,
    test_size=0.2,
    random_state=42
)

train = data[
    data["patient_id"].isin(train_patients)
]

test = data[
    data["patient_id"].isin(test_patients)
]

print("Training patients:", len(train_patients))
print("Testing patients:", len(test_patients))

print("\nTraining rows:", len(train))
print("Testing rows:", len(test))

print("\nTraining labels:")
print(train["relevance"].value_counts())

print("\nTesting labels:")
print(test["relevance"].value_counts())

train.to_csv(
    "data/processed/train.csv",
    index=False
)

test.to_csv(
    "data/processed/test.csv",
    index=False
)

print("\nSaved train.csv and test.csv")