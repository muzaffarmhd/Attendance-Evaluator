from datetime import datetime, timedelta
import helperfuc
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


s=helperfuc.calculate_classes_as_of_today()
totalclassesoftoday=s
#data stored in dictionary: totalclassesoftoday


ss=["CHEM",
    "DENM",
    "BEE",
    "CE",
    "OOP-LAB",
    "CHEM-LAB",
    "OOP",
    "RnD-LAB",
    "BEE-LAB",
    "SPORTS",
    "MENTORING"]
input_attendance_dict={}
def enterattendance():
    try:
        input_attendance= [int(input(f"Enter number of {ss[i]} classes you attended :")) for i in range(11)  ]
        for i in range(11):
            input_attendance_dict[ss[i]]=input_attendance[i]
        print(input_attendance_dict)
        
    except:
        print("invalid attendance")
#input attendace stored in: input_attendace_dict  

# Specify the path to your JSON file
file_path = 'input_attendance.json'

# Read the JSON data from the file

data=totalclassesoftoday

# Write the updated data back to the file
with open(file_path, 'w+') as file:
    input_data=json.load(file)
    
    json.dump(data, file, indent=4)





def attendance_calculator(x,y):
    current_attendance={}
    for i in ss:
        current_attendance[i]=(input_attendance_dict[i]/totalclassesoftoday[i])*100
    pass


