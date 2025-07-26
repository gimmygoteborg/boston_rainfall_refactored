import pandas as pd

def load_holidays(csv_path):
    """
    Loads holiday dates from a CSV with a 'Date' column.
    Returns a list of datetime.date objects.
    """
    df = pd.read_csv(csv_path, parse_dates=["Date"])
    holidays = [d.date() for d in df["Date"]]

    # print(f"✅ Loaded {len(holidays)} holidays from {csv_path}")
    # print("Sample holidays:", holidays[:5])

    return holidays
