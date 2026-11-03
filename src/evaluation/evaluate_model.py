import sys
sys.path.append("src")

import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics import ndcg_score

from models.hierarchical_model import (
    HierarchicalModel,
    encoder,
    split_evidence
)


# =========================
# LOAD TEST DATA
# =========================

data = pd.read_csv(
    "data/processed/test.csv"
)

criteria = pd.read_csv(
    "data/processed/criteria_dataset.csv"
)

criteria = criteria[
    criteria["patient_id"].isin(
        data["patient_id"].unique()
    )
]


# =========================
# LOAD ENCODER
# =========================

encoder = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# =========================
# LOAD OUR MODEL
# =========================

model = HierarchicalModel()

model.load_state_dict(
    torch.load(
        "models/hierarchical_model.pt",
        weights_only=True
    )
)

model.eval()


# =========================
# PREDICT
# =========================

results = []


print("Evaluating model...")


for _, row in data.iterrows():

    patient_id = row["patient_id"]
    trial_id = row["trial_id"]

    trial_criteria = criteria[
        criteria["trial_id"] == trial_id
    ]

    if len(trial_criteria) == 0:
        continue

    evidence = split_evidence(
        row["patient_text"]
    )

    criterion_text = (
        trial_criteria["criterion"]
        .astype(str)
        .tolist()
    )

    evidence_embeddings = torch.tensor(
        encoder.encode(evidence)
    ).float()

    criterion_embeddings = torch.tensor(
        encoder.encode(criterion_text)
    ).float()

    with torch.no_grad():

        score, _ = model(
            evidence_embeddings,
            criterion_embeddings
        )

    results.append({
        "patient_id": patient_id,
        "trial_id": trial_id,
        "relevance": row["relevance"],
        "model_score": score.item(),
        "title": row["title"]
    })


results = pd.DataFrame(results)


# =========================
# NDCG@10
# =========================

scores = []


for patient_id, group in results.groupby(
    "patient_id"
):

    y_true = group["relevance"].values

    y_score = group["model_score"].values

    if len(group) > 1:

        score = ndcg_score(
            [y_true],
            [y_score],
            k=min(10, len(group))
        )

        scores.append(score)


mean_ndcg = sum(scores) / len(scores)


# =========================
# RESULTS
# =========================

print("\n==============================")
print("OUR MODEL RESULTS")
print("==============================")

print(
    "Patients evaluated:",
    len(scores)
)

print(
    "Mean NDCG@10:",
    round(mean_ndcg, 4)
)


# =========================
# EXAMPLE RANKING
# =========================

patient_id = results[
    "patient_id"
].iloc[0]

example = results[
    results["patient_id"] == patient_id
].sort_values(
    "model_score",
    ascending=False
).head(10)


print(
    "\nRanking for patient:",
    patient_id
)

print(
    example[
        [
            "trial_id",
            "model_score",
            "relevance",
            "title"
        ]
    ].to_string(index=False)
)


# =========================
# SAVE
# =========================

results.to_csv(
    "data/processed/model_results.csv",
    index=False
)

print(
    "\nSaved to "
    "data/processed/model_results.csv"
)