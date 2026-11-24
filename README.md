# Nakuru Dairy Co-op — Monthly Summary by Zone

A pandas script that merges daily milk collection with farmer details and produces a clean summary table per zone.

## What it does
1. Merges milk_collection.csv and farmer_details.csv on farmer_name
2. Calculates payout: litres * rate_per_litre
3. Groups by zone to get Total Litres, Total Payout, Top Farmer per Zone
4. Prints a clean table + saves zone_summary.csv

## Files needed
- milk_collection.csv -> farmer_name, date, litres
- farmer_details.csv -> farmer_name, zone, rate_per_litre

## How to run
pip install pandas
python dairy_summary.py