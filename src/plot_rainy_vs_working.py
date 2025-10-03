from datetime import date, timedelta
import matplotlib.pyplot as plt

def plot_rainy_days_comparison(monthly_rainfall, holidays, year, output_path):
    """
    Aggregated bar chart: rainy vs non-rainy days on working vs holidays/weekends.
    """
    # Flatten rainfall data into daily list by date
    daily_data = []
    current_date = date(year, 1, 1)

    for month in range(1, 13):
        for day_index, rainfall in enumerate(monthly_rainfall[month]):
            try:
                day_date = date(year, month, day_index + 1)
            except ValueError:
                continue  # Skip invalid dates
            daily_data.append((day_date, rainfall))

    # Initialize counters
    working_days = holidays_weekends = 0
    working_days_rainy = holidays_weekends_rainy = 0

    for day_date, rainfall in daily_data:
        is_weekend = day_date.weekday() >= 5  # Saturday=5, Sunday=6
        is_holiday = day_date in holidays

        if is_weekend or is_holiday:
            holidays_weekends += 1
            if rainfall > 0:
                holidays_weekends_rainy += 1
        else:
            working_days += 1
            if rainfall > 0:
                working_days_rainy += 1

    # Avoid division by zero
    if working_days == 0 or holidays_weekends == 0:
        print("⚠️ Not enough data to compute rainy day statistics.")
        return

    # Calculate percentages
    percentage_working_days_rainy = (working_days_rainy / working_days) * 100
    percentage_working_days_non_rainy = 100 - percentage_working_days_rainy

    percentage_holidays_weekends_rainy = (holidays_weekends_rainy / holidays_weekends) * 100
    percentage_holidays_weekends_non_rainy = 100 - percentage_holidays_weekends_rainy


    print("\n🟨 Holiday and Weekend Days with Rainfall (2025)\n")
    print(f"{'Date':<12} {'Type':<10} {'Rainfall (in)':>15}")

    for day_date, rainfall in daily_data:
        if rainfall > 0:
            is_weekend = day_date.weekday() >= 5  # Saturday=5, Sunday=6
            is_holiday = day_date in holidays

            if is_holiday:
                print(f"{day_date}  {'Holiday':<10} {rainfall:>15.2f}")
            elif is_weekend:
                print(f"{day_date}  {'Weekend':<10} {rainfall:>15.2f}")

    print("\n✅ Total holidays loaded:", len(holidays))
    print("✅ Sample holidays:", sorted(holidays)[:5], "...")


    # Plot
    categories = ['Working Days', 'Holidays/Weekends']
    rainy_values = [percentage_working_days_rainy, percentage_holidays_weekends_rainy]
    non_rainy_values = [percentage_working_days_non_rainy, percentage_holidays_weekends_non_rainy]

    plt.bar(categories, rainy_values, color='blue', label='Rainy Days', edgecolor='black')
    plt.bar(categories, non_rainy_values, bottom=rainy_values, color='lightgrey', label='Non-Rainy Days', edgecolor='black')

    plt.xlabel('Category')
    plt.ylabel('Percentage of Days')
    plt.title('Rainy Days Comparison: Working Days vs. Holidays/Weekends (Aggregated)')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 0.9))
    plt.ylim(0, 100)
    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    # plt.show()
    plt.close()