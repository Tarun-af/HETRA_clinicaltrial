import pandas as pd

qrels = pd.read_csv(
    "data/raw/qrels2021.txt",
    sep=r"\s+",
    header=None,
    names=["patient_id", "iteration", "trial_id", "relevance"]
)

trial_ids = qrels["trial_id"].drop_duplicates()

print("Unique trials:", len(trial_ids))

trial_ids.to_csv(
    "data/processed/trial_ids.csv",
    index=False,
    header=["trial_id"]
)

print("Saved to data/processed/trial_ids.csv")