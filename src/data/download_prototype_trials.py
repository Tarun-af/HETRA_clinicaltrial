import pandas as pd
import requests

qrels = pd.read_csv(
    "data/processed/prototype_qrels.csv"
)

trial_ids = qrels["trial_id"].unique()

print("Unique trials to download:", len(trial_ids))

session = requests.Session()

trials = []

for i, trial_id in enumerate(trial_ids):

    print(f"{i + 1}/{len(trial_ids)}: {trial_id}")

    url = f"https://clinicaltrials.gov/api/v2/studies/{trial_id}"

    try:
        response = session.get(url, timeout=10)

        if response.status_code != 200:
            print("  Failed:", response.status_code)
            continue

        data = response.json()
        protocol = data.get("protocolSection", {})

        identification = protocol.get(
            "identificationModule", {}
        )

        eligibility = protocol.get(
            "eligibilityModule", {}
        )

        conditions = protocol.get(
            "conditionsModule", {}
        )

        trials.append({
            "trial_id": identification.get("nctId"),
            "title": identification.get("briefTitle"),
            "conditions": ", ".join(
                conditions.get("conditions", [])
            ),
            "eligibility": eligibility.get(
                "eligibilityCriteria"
            ),
            "minimum_age": eligibility.get(
                "minimumAge"
            ),
            "maximum_age": eligibility.get(
                "maximumAge"
            ),
            "sex": eligibility.get(
                "sex"
            )
        })

    except Exception as e:
        print("  Error:", e)

trials_df = pd.DataFrame(trials)

print("\nDownloaded trials:", len(trials_df))

trials_df.to_csv(
    "data/processed/prototype_trials.csv",
    index=False
)

print("Saved to data/processed/prototype_trials.csv")