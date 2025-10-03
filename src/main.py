import os
from .utils import merge_rainfall_data
from .monthly_arrays import build_monthly_rainfall
from .load_holidays import load_holidays
from .plot_rainy_vs_working import plot_rainy_days_comparison
from .plot_weekend_distribution import plot_weekend_rain_distribution
from .plot_calendar_heatmap import plot_calendar_heatmap
from .plot_rainfall_by_weekday import plot_rainfall_by_weekday
from .plot_avg_precip_vs_days import plot_average_precipitation
from .bayes_stats import bayes_rain_weekend


# https://www.bwsc.org/environment-education/rainfall-garden

# === Configuration Variables ===
INPUT_DIR = "input"
BASE_CSV = "Rainfall_Garden_2025.csv"
HOLIDAYS_CSV = "holidays_2025.csv"
YEAR = 2025

def main():
    # Create year-based output directory
    OUTPUT_DIR = f"output/{YEAR}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Merge monthly CSVs
    merge_rainfall_data(INPUT_DIR, os.path.join(INPUT_DIR, BASE_CSV))

    # Build monthly arrays
    monthly = build_monthly_rainfall(os.path.join(INPUT_DIR, BASE_CSV), YEAR)

    # Load holidays
    holidays = load_holidays(os.path.join(INPUT_DIR, HOLIDAYS_CSV))

    # Generate plots
    plot_calendar_heatmap(monthly, holidays, YEAR, os.path.join(OUTPUT_DIR, "calendar_heatmap.png"))
    plot_rainy_days_comparison(monthly, holidays, YEAR, os.path.join(OUTPUT_DIR, "rainy_days_comparison.png"))
    plot_weekend_rain_distribution(monthly, holidays, YEAR, os.path.join(OUTPUT_DIR, "weekend_rain_distribution.png"))
    plot_rainfall_by_weekday(monthly, YEAR, os.path.join(OUTPUT_DIR, "rainfall_by_weekday.png"))
    plot_average_precipitation(monthly, holidays, YEAR, os.path.join(OUTPUT_DIR, "avg_precip_vs_days.png"))

    # Bayes statistics
    all_rain = [day for month in monthly.values() for day in month]
    bayes_rain_weekend(all_rain, holidays, YEAR)

if __name__ == "__main__":
    main()
