import pandas as pd

# Load inventory data
df = pd.read_csv("data/inventory_sample.csv")

# Calculate difference between counted and expected quantity
df["difference"] = df["counted_qty"] - df["expected_qty"]

# Categorize discrepancy type
def categorize_discrepancy(difference):
    if difference < 0:
        return "Shortage"
    elif difference > 0:
        return "Overage"
    else:
        return "No Issue"

df["discrepancy_type"] = df["difference"].apply(categorize_discrepancy)

# Filter only rows with a discrepancy
discrepancies = df[df["discrepancy_type"] != "No Issue"]

# Save report
discrepancies.to_csv("reports/discrepancy_report.csv", index=False)

# Print summary
print("Inventory Discrepancy Report")
print("----------------------------")
print(f"Total items checked: {len(df)}")
print(f"Items with discrepancies: {len(discrepancies)}")
print(f"Discrepancy rate: {len(discrepancies) / len(df) * 100:.2f}%")
print()
print("Discrepancy types:")
print(discrepancies["discrepancy_type"].value_counts())
