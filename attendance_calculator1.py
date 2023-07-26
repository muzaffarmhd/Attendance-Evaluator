from datetime import datetime, timedelta
import json


today=datetime.now()
today_date=today.date()
today_day=today.strftime('%A')

'''Enter your class time table here'''
weekclasslist=[#monday_classes=
    {"CHEM":1,"DENM":1,"BEE":1,"CE":3},
            #    tuesday_classes=
            {"OOP-LAB":2,"CHEM-LAB":3},
            #    wednesday_classes=
            {"OOP":1,"CHEM":1,"BEE":1,"RnD-LAB":3},
            #    thursday_classes=
               {"OOP":2,"DENM":1,"CHEM":1,"BEE-LAB":2},
            #    friday_classes=
               {"DENM":2,"BEE":1,"RnD-LAB":1,"SPORTS":1,"MENTORING":1}
               ]

#Holidays in current semester
holidays_list= ['2023-04-05', '2023-04-07',
                '2023-04-14', '2023-04-22', '2023-05-29',
                '2023-05-30', '2023-05-31', '2023-06-01',
                '2023-06-02', '2023-06-03', '2023-06-04',
                '2023-06-05', '2023-06-06', '2023-06-07',
                '2023-06-08', '2023-06-09', '2023-06-10',
                '2023-06-29', '2023-07-17', '2023-07-29']

# starting the code
tc_file = open('full_classes.json', 'r')
total_sem_dict_classes=json.load(tc_file)

'''calculating total number of classes that has been completed as of yesterday'''

def calculate_classes_as_of_today():


    # Define the date range
    start_date = datetime(2023, 4, 1)
    end_date = datetime.now()

    # Initialize the counters for each weekday
    weekday_counts = {
        0: 0,  # Monday
        1: 0,  # Tuesday
        2: 0,  # Wednesday
        3: 0,  # Thursday
        4: 0   # Friday
    }


    #print("Please enter the holiday dates (YYYY-MM-DD). Enter 'done' to finish.")

    for i in holidays_list:

               
        try:
            holiday_date = datetime.strptime(i, "%Y-%m-%d")
            
            # Check if the holiday falls within the specified date range
            if start_date <= holiday_date <= end_date:
                # Check if the holiday falls on a weekday (Monday to Friday)
                weekday = holiday_date.weekday()
                if weekday in weekday_counts.keys():
                    weekday_counts[weekday] += 1
            else:
                pass
                # print("Holiday date is outside the specified date range.")
        
        except ValueError:
            pass
            # print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    # Print the results
    # print("Number of Mondays that are holidays:", weekday_counts[0])
    # print("Number of Tuesdays that are holidays:", weekday_counts[1])
    # print("Number of Wednesdays that are holidays:", weekday_counts[2])
    # print("Number of Thursdays that are holidays:", weekday_counts[3])
    # print("Number of Fridays that are holidays:", weekday_counts[4])





    def count_weekdays(start_date, end_date):
        count = [0] * 7  # Initialize count for each weekday
        current_date = start_date

        while current_date <= end_date:
            count[current_date.weekday()] += 1
            current_date += timedelta(days=1)

        return count

    # Example usage

    weekdays_count = count_weekdays(start_date, end_date)
    global totalweekdayvalues
    totaldaysasoftoday={}

    weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # for i in range(7):
    #     print("Number of", weekday_names[i] + "s:", weekdays_count[i])

    for i in range(5):
        # print("Total no. of", weekday_names[i], "classes", weekdays_count[i]-weekday_counts[i])
        totaldaysasoftoday[weekday_names[i]]=weekdays_count[i]-weekday_counts[i]
    #print(totaldaysasoftoday)
    totalweekdayvalues=totaldaysasoftoday

#weekdaysasoftoday()
#data stored in dictionary: totalweekdayvalues

#def calculate_classes_as_of_today(weekclasslist,dic2):
    dic2_as_list=[]
    for i in totalweekdayvalues:
        dic2_as_list.append(totalweekdayvalues[i])
    def multiplier(dictionary,value):
        for i in dictionary:
            dictionary[i]=value*dictionary[i]
        # print(dictionary)
    for i in range(5):
        multiplier(weekclasslist[i],dic2_as_list[i])



    global totalclassesoftoday
    total_classes_of_today = {}

    def add_to_combined(dictionary):
        for key, value in dictionary.items():
            if key in total_classes_of_today:
                total_classes_of_today[key] += value
            else:
                total_classes_of_today[key] = value
    for i in range(5):
        add_to_combined(weekclasslist[i])
    totalclassesoftoday=total_classes_of_today
calculate_classes_as_of_today()
#data stored in dictionary: totalclassesoftoday
print(totalclassesoftoday)



def enterattendance():
    pass


