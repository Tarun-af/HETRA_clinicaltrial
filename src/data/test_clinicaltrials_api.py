import requests

trial_id = "NCT00002569"

url = f"https://clinicaltrials.gov/api/v2/studies/{trial_id}"

response = requests.get(url)

print("Status code:", response.status_code)

data = response.json()

protocol = data["protocolSection"]

print("\n--- IDENTIFICATION ---")

print("NCT ID:")
print(protocol["identificationModule"]["nctId"])

print("\nTitle:")
print(protocol["identificationModule"]["briefTitle"])


print("\n--- ELIGIBILITY ---")

eligibility = protocol["eligibilityModule"]

print("Age:")
print(eligibility.get("minimumAge"), "to", eligibility.get("maximumAge"))

print("\nSex:")
print(eligibility.get("sex"))

print("\nHealthy volunteers:")
print(eligibility.get("healthyVolunteers"))

print("\nEligibility criteria:")
print(eligibility.get("eligibilityCriteria"))


print("\n--- CONDITIONS ---")

conditions = protocol.get("conditionsModule", {})

print(conditions.get("conditions"))