import pandas as pd

qrels = pd.read_csv(
    "data/raw/qrels2021.txt",
    sep=r"\s+",
    header=None,
    names=["patient_id", "iteration", "trial_id", "relevance"]
)

# Use first 10 patients
qrels = qrels[qrels["patient_id"].isin(range(1, 11))]

# Take up to 170 examples from each relevance class
prototype = (
    qrels
    .groupby("relevance", group_keys=False)
    .apply(lambda x: x.sample(min(len(x), 170), random_state=42))
)

print("Prototype rows:", len(prototype))
print("\nLabel counts:")
print(prototype["relevance"].value_counts())

print("\nUnique patients:")
print(prototype["patient_id"].nunique())

print("\nUnique trials:")
print(prototype["trial_id"].nunique())

prototype.to_csv(
    "data/processed/prototype_qrels.csv",
    index=False
)

print("\nSaved prototype_qrels.csv")