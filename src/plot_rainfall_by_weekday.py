import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_rainfall_by_weekday(monthly_rainfall, year, output_path):
    """
    Bar chart of total rainfall by day of the week.
    """
    from datetime import date

    # Flatten all rainfall data into daily list by date
    daily_data = []
    for month in range(1, 13):
        for day_index, rainfall in enumerate(monthly_rainfall[month]):
            try:
                day_date = date(year, month, day_index + 1)
                daily_data.append((day_date, rainfall))
            except ValueError:
                continue

    # Initialize dictionary for weekdays
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    total_rainfall_by_day = {day: 0.0 for day in days_of_week}

    # Accumulate rainfall by weekday
    for day_date, rainfall in daily_data:
        day_name = days_of_week[day_date.weekday()]
        total_rainfall_by_day[day_name] += rainfall

    # Print results
    print("\n🌧️ Total Rainfall by Weekday:\n")
    for day, total in total_rainfall_by_day.items():
        print(f"{day:<10}: {total:.2f} inches")

    # Plot
    days = days_of_week
    values = [total_rainfall_by_day[day] for day in days]

    plt.bar(days, values, color='blue')
    plt.xlabel('Day of the Week')
    plt.ylabel('Total Rainfall (inches)')
    plt.title('Total Rainfall by Day of the Week')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    # plt.show()
    plt.close()
