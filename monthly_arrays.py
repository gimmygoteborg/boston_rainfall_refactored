import pandas as pd
import calendar

def build_monthly_rainfall(csv_path, year):
    """
    Returns a dict mapping month number to list of daily rainfall inches.
    """
    df = pd.read_csv(csv_path, parse_dates=["Date"])
    df["Inches"] = pd.to_numeric(df["Inches"], errors="coerce").fillna(0.0)
    monthly = {i: [0.0]*calendar.monthrange(year, i)[1] for i in range(1,13)}
    for _, row in df.iterrows():
        date = row["Date"]
        if pd.notnull(date) and date.year == year:
            monthly[date.month][date.day-1] = row["Inches"]
    return monthly
