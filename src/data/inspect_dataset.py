import pandas as pd

data = pd.read_csv(
    "data/processed/final_prototype.csv"
)

print("Dataset shape:")
print(data.shape)

print("\nLabel distribution:")
print(data["relevance"].value_counts())

print("\nExamples:")
for i in range(5):
    row = data.iloc[i]

    print("\n==============================")
    print("PATIENT:", row["patient_id"])
    print("TRIAL:", row["trial_id"])
    print("LABEL:", row["relevance"])

    print("\nPatient:")
    print(row["patient_text"][:500])

    print("\nTrial:")
    print(row["title"])

    print("\nEligibility:")
    print(str(row["eligibility"])[:1000])