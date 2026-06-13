import pandas as pd

FILE = "orders.csv"  # change as needed

print("=" * 60)
print(f"Profiling: {FILE}")
print("=" * 60)

# Load
df = pd.read_csv(FILE)

# Basic Info
print("\n📊 Dataset Shape")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# Schema
print("\n📋 Schema")
print(df.dtypes)

# Sample
print("\n🔍 First 5 Rows")
print(df.head())

# Last Rows
print("\n🔍 Last 5 Rows")
print(df.tail())

# Duplicates
print("\n🧹 Duplicate Check")
print(f"Total Rows: {len(df)}")
print(f"Distinct Rows: {len(df.drop_duplicates())}")
print(f"Duplicate Rows: {len(df) - len(df.drop_duplicates())}")

# Null Analysis
print("\n❓ Null Counts")
for col in df.columns:
    print(f"{col}: {df[col].isna().sum()}")

# Distinct Counts
print("\n🔢 Distinct Values")
for col in df.columns:
    print(f"{col}: {df[col].nunique()}")

# String Cleanup Check
print("\n🧽 String Columns")
string_cols = df.select_dtypes(include=["object"]).columns

for col in string_cols:
    unique_vals = df[col].astype(str).str.strip().dropna().unique()[:10]
    print(f"\n{col}")
    print(unique_vals)

# File-specific checks
if "user_id" in df.columns:
    print(f"\nDistinct Users: {df['user_id'].nunique()}")

if "r_id" in df.columns:
    print(f"Distinct Restaurants: {df['r_id'].nunique()}")

if "restaurant_id" in df.columns:
    print(f"Distinct Restaurants: {df['restaurant_id'].nunique()}")

# Revenue Checks
if "sales_amount" in df.columns:
    print("\n💰 Revenue Statistics")
    print(df["sales_amount"].describe())

# Quantity Checks
if "sales_qty" in df.columns:
    print("\n📦 Quantity Statistics")
    print(df["sales_qty"].describe())

# Date Checks
if "order_date" in df.columns:
    print("\n📅 Date Range")

    dates = pd.to_datetime(df["order_date"], errors="coerce")

    print("Min Date:", dates.min())
    print("Max Date:", dates.max())

print("\n✅ Profiling Complete")