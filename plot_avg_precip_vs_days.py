import matplotlib.pyplot as plt
import calendar
import datetime

def plot_average_precipitation(monthly_rainfall, holidays, year, output_path):
    """
    Bar chart comparing average precipitation on weekends/holidays vs. working days.
    """

    # Weekend days (Saturday=5, Sunday=6)
    weekends = {5, 6}

    # Initialize accumulators
    weekend_holiday_total = 0.0
    weekend_holiday_count = 0

    weekday_total = 0.0
    weekday_count = 0

    # Iterate over all months and days
    for month in range(1, 13):
        rainfall_days = monthly_rainfall[month]
        _, last_day = calendar.monthrange(year, month)

        for day_index, precipitation in enumerate(rainfall_days):
            day = day_index + 1
            if day > last_day:
                continue  # Skip invalid days

            current_date = datetime.date(year, month, day)
            is_weekend = current_date.weekday() in weekends
            is_holiday = current_date in holidays

            if is_weekend or is_holiday:
                weekend_holiday_total += precipitation
                weekend_holiday_count += 1
            else:
                weekday_total += precipitation
                weekday_count += 1

    # Safeguard division
    avg_weekend_holiday = weekend_holiday_total / weekend_holiday_count if weekend_holiday_count else 0
    avg_weekday = weekday_total / weekday_count if weekday_count else 0

    # print(f"Weekend/Holiday Avg: {avg_weekend_holiday:.2f} in")
    # print(f"Weekday Avg: {avg_weekday:.2f} in")

    # Plotting
    categories = ['Weekends/Holidays', 'Weekdays']
    averages = [avg_weekend_holiday, avg_weekday]

    plt.bar(categories, averages, color=['red', 'green'])
    plt.xlabel('Day Type')
    plt.ylabel('Average Precipitation (inches)')
    plt.title('Average Daily Precipitation: Weekends/Holidays vs. Weekdays')

    for i, value in enumerate(averages):
        plt.text(i, value + 0.01, f'{value:.2f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    # plt.show()
    plt.close()
