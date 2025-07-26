import calendar
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import datetime
import numpy as np
import seaborn as sns

def plot_calendar_heatmap(monthly_rainfall, holidays, year, output_path):
    """
    Calendar heatmap highlighting weekends and holidays.
    """

    # Function to check if a date is in the future
    def is_future_date(year, month, day):
        date_to_check = datetime.date(year, month, day)
        return date_to_check > current_date

    # Function to check if a date is a holiday
    def is_holiday(date):
        return date in holidays

    # Get the current date
    current_date = datetime.date.today()

    # Create subplots
    fig, axes = plt.subplots(4, 3, figsize=(15, 15))
    axes = axes.flatten()

    # Define the colors for the colormap
    colors = ['white', 'blue']
    cmap = cm.colors.LinearSegmentedColormap.from_list('custom_cmap', colors)

    # Iterate over each month
    for month in range(1, 13):
        # Create a calendar for the current month
        cal = calendar.monthcalendar(2025, month)

        # Create a matrix of the rainfall data corresponding to the current month
        matrix = []
        for week in cal:
            row = []
            for day in week:
                if day == 0:
                    row.append(np.nan)  # Replace None values with NaN
                else:
                    if day <= len(monthly_rainfall[month]):
                        row.append(monthly_rainfall[month][day - 1])
                    else:
                        row.append(np.nan)
            matrix.append(row)

        # Create the heatmap for the current month
        sns.heatmap(matrix, cmap=cmap, annot=True, fmt=".2f", cbar=False, ax=axes[month-1])

        # Customize the color of future dates and today
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                day = cal[i][j]
                if day != 0:
                    date_to_check = datetime.date(2025, month, day)
                    if is_future_date(2025, month, day) or date_to_check == current_date:
                        axes[month-1].add_patch(plt.Rectangle((j, i), 1, 1, fill=True, facecolor='grey', edgecolor='black', lw=2))

                    # color = 'grey' if current_date != datetime.date.today() else 'darkgrey'
                    # axes[month-1].add_patch(plt.Rectangle((j, i), 1, 1, fill=True, facecolor=color, edgecolor='black', lw=2))

        axes[month-1].set_xticklabels(calendar.weekheader(3).split())
        axes[month-1].set_yticklabels(range(1, len(matrix) + 1))
        axes[month-1].set_title(f'{calendar.month_name[month]} 2025')

        # Add thicker borders for weekends and holidays
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                day = cal[i][j]
                if day != 0:
                    # Check if it's a weekend or a holiday
                    if calendar.weekday(2025, month, day) >= 5 or is_holiday(datetime.date(2025, month, day)):
                        axes[month-1].add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black', lw=2))

    # Adjust the spacing between subplots
    plt.subplots_adjust(hspace=0.6, wspace=0.3)

    # plt.savefig("Calendar Heatmap.png", bbox_inches="tight", dpi=300)

    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    # plt.show()
    plt.close()
