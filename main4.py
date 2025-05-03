import calendar

def display_months():
    months = list(calendar.month_name)[1:]  # Skip the empty string at index 0
    for month in months:
        print(month)

if __name__ == "__main__":
    display_months()