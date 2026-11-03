import pandas as pd
import re

data = pd.read_csv(
    "data/processed/final_prototype.csv"
)

criteria = []

for _, row in data.iterrows():

    text = str(row["eligibility"])

    # Find inclusion section
    inclusion = ""
    exclusion = ""

    match = re.search(
        r"inclusion criteria:(.*?)(?=exclusion criteria:|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        inclusion = match.group(1)

    # Find exclusion section
    match = re.search(
        r"exclusion criteria:(.*)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        exclusion = match.group(1)

    # Extract bullet points
    for criterion in re.split(r"\n", inclusion):

        criterion = criterion.strip()
        criterion = re.sub(r"^[*\-\d.)]+\s*", "", criterion)

        if len(criterion) > 10:
            criteria.append({
                "patient_id": row["patient_id"],
                "trial_id": row["trial_id"],
                "patient_text": row["patient_text"],
                "criterion": criterion,
                "criterion_type": "inclusion",
                "relevance": row["relevance"]
            })

    for criterion in re.split(r"\n", exclusion):

        criterion = criterion.strip()
        criterion = re.sub(r"^[*\-\d.)]+\s*", "", criterion)

        if len(criterion) > 10:
            criteria.append({
                "patient_id": row["patient_id"],
                "trial_id": row["trial_id"],
                "patient_text": row["patient_text"],
                "criterion": criterion,
                "criterion_type": "exclusion",
                "relevance": row["relevance"]
            })


criteria_df = pd.DataFrame(criteria)

print("Number of criteria:", len(criteria_df))

print("\nCriterion types:")
print(criteria_df["criterion_type"].value_counts())

print("\nExamples:")

for i in range(min(10, len(criteria_df))):

    row = criteria_df.iloc[i]

    print("\n----------------------")
    print("Patient:", row["patient_id"])
    print("Trial:", row["trial_id"])
    print("Type:", row["criterion_type"])
    print("Criterion:", row["criterion"])
    print("Trial label:", row["relevance"])


criteria_df.to_csv(
    "data/processed/criteria_dataset.csv",
    index=False
)

print("\nSaved to data/processed/criteria_dataset.csv")