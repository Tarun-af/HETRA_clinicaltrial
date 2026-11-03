import pandas as pd
from sklearn.metrics import ndcg_score


data = pd.read_csv(
    "data/processed/baseline_results.csv"
)


scores = []


for patient_id, group in data.groupby("patient_id"):

    # Actual relevance
    y_true = group["relevance"].values

    # Model's ranking score
    y_score = group["similarity"].values

    if len(group) > 1:

        score = ndcg_score(
            [y_true],
            [y_score],
            k=min(10, len(group))
        )

        scores.append(score)


mean_ndcg = sum(scores) / len(scores)


print("==============================")
print("BASELINE EVALUATION")
print("==============================")

print("Patients evaluated:", len(scores))

print(
    "Mean NDCG@10:",
    round(mean_ndcg, 4)
)