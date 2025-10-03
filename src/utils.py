import os
import pandas as pd
import calendar
from datetime import datetime

# Safer date parser: handles both YYYY-MM-DD and M/D/YY
def safe_parse_date(date_str):
    for fmt in ("%Y-%m-%d", "%m/%d/%y"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Date {date_str} is not in a recognized format.")

def merge_rainfall_data(input_dir, base_csv_path):
    """
    Merges monthly rainfall CSV files in input_dir into base_csv_path,
    overwriting duplicates.
    """
    # Initialize or load base_df
    if os.path.exists(base_csv_path):
        base_df = pd.read_csv(base_csv_path, parse_dates=["Date"])
        base_df.set_index("Date", inplace=True)
    else:
        base_df = pd.DataFrame(columns=["Date", "Inches"]).set_index("Date")

    for filename in os.listdir(input_dir):
        if filename.endswith('.csv') and filename != os.path.basename(base_csv_path):
            try:
                df = pd.read_csv(os.path.join(input_dir, filename))
                df["Date"] = df["Date"].apply(safe_parse_date)
                df.set_index("Date", inplace=True)
                # Overwrite or add new rows
                base_df.update(df)
                base_df = pd.concat([base_df, df[~df.index.isin(base_df.index)]])
            except Exception as e:
                print(f"⚠️ Skipping {filename}: {e}")

    # Clean and normalize
    base_df = base_df[~base_df.index.duplicated(keep="last")].sort_index().reset_index()
    # Ensure 'Date' column is datetime
    base_df['Date'] = pd.to_datetime(base_df['Date'], errors='coerce')
    base_df["Date"] = base_df["Date"].dt.strftime("%Y-%m-%d")
    base_df.to_csv(base_csv_path, index=False)
    print(f"✅ Merged rainfall data saved to {base_csv_path}")
