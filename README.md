# inventory-discrepancy-tracker
A Python + Excel project for tracking and analyzing warehouse inventory discrepancies.

## How It Works

The project loads a warehouse inventory CSV file, compares expected quantity with counted quantity, and identifies items with discrepancies.

The script then creates a discrepancy report that can be used by inventory or operations teams.

## Current Output

The Python script calculates:

- Total items checked
- Number of items with discrepancies
- Discrepancy rate
- Difference between expected and counted quantity

## Files

- `data/inventory_sample.csv` — sample warehouse inventory data
- `src/analyze_discrepancies.py` — Python script for analysis
- `reports/discrepancy_report.csv` — generated discrepancy report
