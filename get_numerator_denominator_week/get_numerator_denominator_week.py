from datetime import datetime, timedelta


def get_current_week_type():
    # Define the start date and end date of the pattern
    start_date = datetime(2024, 2, 26)
    end_date = datetime(2024, 12, 31)

    # Get the current date
    current_date = datetime.now()

    # Initialize the pattern
    is_znamennik_week = True

    # Determine the week type based on the pattern
    while start_date <= end_date:
        if current_date <= start_date + timedelta(days=6):
            return f"{current_date.date()} - Знаменник" if is_znamennik_week else f"{current_date.date()} - Чисельник"

        # Move to the next Monday
        start_date += timedelta(days=(7 - start_date.weekday()))

        # Switch the label for the next week
        is_znamennik_week = not is_znamennik_week

    return "It`s time to update date bounds :)"
