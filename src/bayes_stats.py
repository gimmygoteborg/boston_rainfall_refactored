import datetime

def bayes_rain_weekend(all_months_rainfall, holidays, year):
    """
    Applies Bayes' theorem to compute P(rain | weekend).
    """

    # Generate the dataset
    stats_data = []
    current_date = datetime.date(2025, 1, 1)  # Start from January 1, 2025

    for rainfall in all_months_rainfall:
        day_type = 'weekday' if current_date.weekday() < 5 else 'weekend'
        stats_data.append((day_type, rainfall))
        current_date += datetime.timedelta(days=1)

    # Display the first few entries of the dataset
    # print(stats_data[:10])

    # Count occurrences of each day type
    total_days = len(stats_data)
    weekday_count = sum(1 for day_type, _ in stats_data if day_type == 'weekday')
    weekend_count = sum(1 for day_type, _ in stats_data if day_type == 'weekend')
    holiday_count = sum(1 for day_type, _ in stats_data if day_type == 'holiday')

    # Calculate prior probabilities
    P_rain = sum(1 for _, rainfall in stats_data if rainfall > 0) / total_days
    P_weekend = weekend_count / total_days

    # Calculate likelihoods
    P_weekend_given_rain = sum(1 for day_type, rainfall in stats_data if day_type == 'weekend' and rainfall > 0) / sum(1 for _, rainfall in stats_data if rainfall > 0)

    # Apply Bayes' theorem
    P_rain_given_weekend = (P_weekend_given_rain * P_rain) / P_weekend

    print(f"P(rain|weekend) = {P_rain_given_weekend:.4f}")
