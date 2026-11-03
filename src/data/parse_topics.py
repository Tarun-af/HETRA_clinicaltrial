import xml.etree.ElementTree as ET
import pandas as pd

file_path = "data/raw/topics2021.xml"

tree = ET.parse(file_path)
root = tree.getroot()

patients = []

for topic in root.findall("topic"):

    patient_id = topic.get("number")
    patient_text = "".join(topic.itertext()).strip()

    patients.append({
        "patient_id": int(patient_id),
        "patient_text": patient_text
    })

patients_df = pd.DataFrame(patients)

print("Number of patients:", len(patients_df))

print("\nFirst 3 patients:")
print(patients_df.head(3))

patients_df.to_csv(
    "data/processed/patients.csv",
    index=False
)

print("\nSaved to data/processed/patients.csv")