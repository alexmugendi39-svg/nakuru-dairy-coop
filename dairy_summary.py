import pandas as pd

# 1. LOAD THE TWO INPUT FILES
# milk_collection.csv -> farmer_name, date, litres
# farmer_details.csv  -> farmer_name, zone, rate_per_litre
collection = pd.read_csv("milk_collection.csv")
farmers = pd.read_csv("farmer_details.csv")

# 2. MERGE ON FARMER NAME
merged = pd.merge(collection, farmers, on="farmer_name", how="left")

# 3. CALCULATE PAYOUT PER RECORD
merged["payout_kes"] = merged["litres"] * merged["rate_per_litre"]

# 4. TOTAL LITRES & TOTAL PAYOUT PER ZONE (pivot / groupby)
zone_summary = merged.groupby("zone").agg(
    total_litres=("litres", "sum"),
    total_payout_kes=("payout_kes", "sum"),
    num_farmers=("farmer_name", "nunique")
).reset_index()

# 5. TOP FARMER PER ZONE (by total litres)
farmer_totals = merged.groupby(["zone", "farmer_name"])["litres"].sum().reset_index()
top_farmers = farmer_totals.sort_values(["zone", "litres"], ascending=[True, False]).drop_duplicates("zone")
top_farmers = top_farmers.rename(columns={"farmer_name": "top_farmer", "litres": "top_farmer_litres"})

# 6. FINAL CLEAN SUMMARY TABLE
summary = pd.merge(zone_summary, top_farmers, on="zone")
summary = summary[["zone", "total_litres", "total_payout_kes", "top_farmer", "top_farmer_litres", "num_farmers"]]
summary = summary.sort_values("total_litres", ascending=False)

# 7. PRINT - CLEAN FOR SCREENSHOT / CLIENT
print("=" * 68)
print("NAKURU DAIRY CO-OP - MONTHLY SUMMARY BY ZONE | NOVEMBER 2026")
print("=" * 68)
print()
print(summary.to_string(index=False))
print()
print("-" * 68)
print(f"GRAND TOTAL: {summary['total_litres'].sum():,.0f} litres | Ksh {summary['total_payout_kes'].sum():,.0f} payout")
print(f"TOTAL FARMERS: {summary['num_farmers'].sum()}")
print("-" * 68)

# Optional: save for client
summary.to_csv("zone_summary.csv", index=False)
print("Saved -> zone_summary.csv")
