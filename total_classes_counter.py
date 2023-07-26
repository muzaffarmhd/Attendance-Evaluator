from datetime import datetime, timedelta

# Define the date range
start_date = datetime(2023, 4, 1)
end_date = datetime(2023, 8, 4)

# Initialize the counters for each weekday
weekday_counts = {
    0: 0,  # Monday
    1: 0,  # Tuesday
    2: 0,  # Wednesday
    3: 0,  # Thursday
    4: 0   # Friday
}

# Ask the user for holiday inputs
print("Please enter the holiday dates (YYYY-MM-DD). Enter 'done' to finish.")

while True:
    holiday_input = input("Holiday date: ")
    
    if holiday_input == "done":
        break
    
    try:
        holiday_date = datetime.strptime(holiday_input, "%Y-%m-%d")
        
        # Check if the holiday falls within the specified date range
        if start_date <= holiday_date <= end_date:
            # Check if the holiday falls on a weekday (Monday to Friday)
            weekday = holiday_date.weekday()
            if weekday in weekday_counts.keys():
                weekday_counts[weekday] += 1
        else:
            print("Holiday date is outside the specified date range.")
    
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Print the results
print("Number of Mondays that are holidays:", weekday_counts[0])
print("Number of Tuesdays that are holidays:", weekday_counts[1])
print("Number of Wednesdays that are holidays:", weekday_counts[2])
print("Number of Thursdays that are holidays:", weekday_counts[3])
print("Number of Fridays that are holidays:", weekday_counts[4])





def count_weekdays(start_date, end_date):
    count = [0] * 7  # Initialize count for each weekday
    current_date = start_date

    while current_date <= end_date:
        count[current_date.weekday()] += 1
        current_date += timedelta(days=1)

    return count

# Example usage

weekdays_count = count_weekdays(start_date, end_date)

weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i in range(7):
    print("Number of", weekday_names[i] + "s:", weekdays_count[i])

for i in range(5):
    print("Total no. of", weekday_names[i], "classes", weekdays_count[i]-weekday_counts[i])



