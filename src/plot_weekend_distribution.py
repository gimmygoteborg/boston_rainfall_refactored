import datetime
import matplotlib.pyplot as plt
import numpy as np

def generate_long_weekends_fixed(year, holidays):
    """
    Returns a list of (start_date, end_date) tuples for each distinct weekend
    or long weekend (including adjacent holidays).
    """
    weekends = []
    seen_days = set()  # Avoid overlapping ranges

    for month in range(1, 13):
        for day in range(1, 32):
            try:
                current_date = datetime.date(year, month, day)
            except ValueError:
                continue

            if current_date in seen_days:
                continue

            if current_date.weekday() == 5:  # Saturday
                sunday = current_date + datetime.timedelta(days=1)
                friday = current_date - datetime.timedelta(days=1)
                monday = current_date + datetime.timedelta(days=2)

                start = current_date
                end = sunday

                # Extend backwards or forwards if holiday
                if friday in holidays:
                    start = friday
                if monday in holidays:
                    end = monday

                # Mark days as seen
                for offset in range((end - start).days + 1):
                    seen_days.add(start + datetime.timedelta(days=offset))

                weekends.append((start, end))

    return weekends

def count_rainy_days(rainfall_data, start_date, end_date):
    rainy_days = 0
    current_date = start_date

    while current_date <= end_date:
        month = current_date.month
        day_index = current_date.day - 1

        if month in rainfall_data and 0 <= day_index < len(rainfall_data[month]):
            if rainfall_data[month][day_index] > 0:
                rainy_days += 1

        current_date += datetime.timedelta(days=1)

    return rainy_days

def plot_weekend_rain_distribution(rainfall_data, holidays, year, output_path):
    long_weekends = generate_long_weekends_fixed(year, holidays)

    rainy_days_counts = {}

    for start_date, end_date in long_weekends:
        rainy = count_rainy_days(rainfall_data, start_date, end_date)
        rainy_days_counts[rainy] = rainy_days_counts.get(rainy, 0) + 1

    # Plot
    labels = [f"{i} Rainy Day{'s' if i != 1 else ''}" for i in sorted(rainy_days_counts)]
    sizes = [rainy_days_counts[i] for i in sorted(rainy_days_counts)]
    colors = ['lightgrey', 'lightgreen', 'lightblue', 'blue', 'navy']

    plt.figure(figsize=(6, 6))
    plt.pie(
        sizes,
        labels=labels,
        autopct=lambda p: f'{int(round(p * sum(sizes) / 100))}',
        startangle=140,
        colors=colors[:len(sizes)]
    )
    plt.title("Distribution of Rainy Days in Weekends/Long Weekends")
    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    # plt.show()
    plt.close()
