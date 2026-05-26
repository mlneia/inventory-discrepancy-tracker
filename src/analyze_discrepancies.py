import pandas as pd

# Load inventory data
df = pd.read_csv("data/inventory_sample.csv")

# Calculate discrepancy
df["difference"] = df["counted_qty"] - df["expected_qty"]

# Mark items with discrepancy
df["has_discrepancy"] = df["difference"] != 0

# Filter only problem items
discrepancies = df[df["has_discrepancy"] == True]

# Save report
discrepancies.to_csv("reports/discrepancy_report.csv", index=False)

# Print summary
print("Inventory Discrepancy Report")
print("----------------------------")
print(f"Total items checked: {len(df)}")
print(f"Items with discrepancies: {len(discrepancies)}")
print(f"Discrepancy rate: {len(discrepancies) / len(df) * 100:.2f}%")
