import sys
sys.path.append("src")

import pandas as pd
import torch

from models.hierarchical_model import (
    HierarchicalModel,
    encoder,
    split_evidence
)


# =========================
# LOAD DATA
# =========================

data = pd.read_csv(
    "data/processed/train.csv"
)

criteria = pd.read_csv(
    "data/processed/criteria_dataset.csv"
)


# =========================
# CREATE MODEL
# =========================

model = HierarchicalModel()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)


# =========================
# TRAIN
# =========================

print("Training model...")


for epoch in range(10):

    total_loss = 0

    for _, row in data.iterrows():

        trial_criteria = criteria[
            criteria["trial_id"] == row["trial_id"]
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

        with torch.no_grad():

            evidence_embeddings = torch.tensor(
                encoder.encode(evidence)
            ).float()

            criterion_embeddings = torch.tensor(
                encoder.encode(criterion_text)
            ).float()

        score, criterion_scores = model(
            evidence_embeddings,
            criterion_embeddings
        )

        target = torch.tensor(
            [float(row["relevance"]) / 2.0]
        )

        prediction_loss = (
            score.reshape(1) - target
        ).pow(2).mean()

        if row["relevance"] == 2:

            contrastive_loss = (
                1 - criterion_scores.sigmoid()
            ).mean()

        elif row["relevance"] == 0:

            contrastive_loss = (
                criterion_scores.sigmoid()
            ).mean()

        else:

            contrastive_loss = torch.tensor(
                0.0
            )

        loss = (
            prediction_loss
            + 0.2 * contrastive_loss
        )

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(
        f"Epoch {epoch + 1}/10 "
        f"Loss: {total_loss:.4f}"
    )


# =========================
# SAVE MODEL
# =========================

torch.save(
    model.state_dict(),
    "models/hierarchical_model.pt"
)

print("\nModel saved.")