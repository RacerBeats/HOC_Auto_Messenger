import datetime as dt
name = input("Enter your name: ")
course = input("Enter patron's registered course: ")
class_time = input("Enter appropriate course timeslots: ")

#The goal of this program is to automate the process for drafting text messages for potential students.
#Input your name, the patron's class, and the time scheduled.
#Output: The text message to be pasted.

class_schedule = {
    "Boxing (Teens / Adults)": 
    {
        "Monday": [(dt.time(8,30), dt.time(9,30)),(dt.time(18,15), dt.time(19,15))],
        "Tuesday": [(dt.time(19,15), dt.time(20,15))],
        "Wednesday": [(dt.time(8,30), dt.time(9,30)),(dt.time(18,15), dt.time(19,15))],
        "Thursday": [(dt.time(19,15), dt.time(20,15))]
    },
    "Silver Warrior":
    {
        "Monday": (dt.time(10,30), dt.time(11,30)),
        "Wednesday": (dt.time(10,30), dt.time(11,30))
    },
    "Karate (4-5 years)":
    {
        "Monday": (dt.time(15,30), dt.time(16,00)),
        "Wednesday": (dt.time(15,30), dt.time(16,00)),
        "Friday": (dt.time(15,30), dt.time(16,00))
    },
    "Karate (6-9 years)":
    {
        "Monday": (dt.time(16,00), dt.time(16,45)),
        "Wednesday": (dt.time(16,00), dt.time(16,45)),
        "Friday": (dt.time(16,00), dt.time(16,45))
    },
    "Karate (10-12 years)":
    {
        "Monday": (dt.time(16,45), dt.time(17,30)),
        "Wednesday": (dt.time(16,45), dt.time(17,30)),
        "Friday": (dt.time(16,45), dt.time(17,30))
    },
    "Karate (Teens / Adults)":
    {
        "Monday": (dt.time(17,30), dt.time(18,15)),
        "Wednesday": (dt.time(17,30), dt.time(18,15)),
        "Friday": (dt.time(17,30), dt.time(18,15))
    },
    "MMA (Teens / Adults)":
    {
        "Monday": (dt.time(18,15), dt.time(19,15)),
        "Wednesday": (dt.time(18,15), dt.time(19,15))
    },
    "Muay Thai Kickboxing (Teens)":
    {
        "Monday": (dt.time(19,15), dt.time(20,15)),
        "Tuesday": [(dt.time(8,30), dt.time(9,30)),(dt.time(17,30), dt.time(18,15)),(dt.time(18,15), dt.time(19,15))],
        "Wednesday": (dt.time(19,15), dt.time(20,15)),
        "Thursday": [(dt.time(8,30), dt.time(9,30)),(dt.time(17,30), dt.time(18,15)),(dt.time(18,15), dt.time(19,15))],
        "Saturday": (dt.time(9,30), dt.time(10,30))
    },
    "Muay Thai Kickboxing (Adults)":
    {
        "Monday": (dt.time(19,15), dt.time(20,15)),
        "Tuesday": [(dt.time(8,30), dt.time(9,30)),(dt.time(18,15), dt.time(19,15))],
        "Wednesday": (dt.time(19,15), dt.time(20,15)),
        "Thursday": [(dt.time(8,30), dt.time(9,30)),(dt.time(18,15), dt.time(19,15))],
        "Saturday": (dt.time(9,30), dt.time(10,30))
    },
    "Muay Thai Kickboxing (4-5 years)":
    {
        "Tuesday":(dt.time(15,30), dt.time(16,00)),
        "Thursday":(dt.time(15,30), dt.time(16,00))
    },
    "Muay Thai Kickboxing (6-9 years)":
    {
        "Tuesday":(dt.time(16,00), dt.time(16,45)),
        "Thursday":(dt.time(16,00), dt.time(16,45)),
        "Saturday":(dt.time(10,30), dt.time(11,15))
    },
    "Muay Thai Kickboxing (10-12 years)":
    {
        "Tuesday":(dt.time(16,45), dt.time(17,30)),
        "Thursday":(dt.time(16,45), dt.time(17,30)),
        "Saturday":(dt.time(11,15), dt.time(12,00))
    },
    "MMA (Kids)":
    {
        "Tuesday":(dt.time(17,30), dt.time(18,15)),
        "Thursday":(dt.time(17,30), dt.time(18,15))
    },
    "Open Floor":
    {
        "Tuesday": (dt.time(9,30), dt.time(12,00)),
        "Thursday": (dt.time(9,30), dt.time(12,00)),
        "Saturday": (dt.time(12,00), dt.time(13,30))
    },
    "HOC Hurricanes":
    {
        "Friday": (dt.time(18,15), dt.time(19,30))
    },
    "Escrima":
    {
        "Saturday": (dt.time(11,00), dt.time(12,00))
    },
    "Krav Maga":
    {
        "Monday": (dt.time(19,15), dt.time(20,15)),
        "Wednesday": (dt.time(19,15), dt.time(20,15)),
        "Saturday": (dt.time(9,30), dt.time(10,30))
    }
}

def createMessage(name, course, class_time):
    print(f"""Hi, this is {name} from House of Champions. We wanted to follow up with you to schedule an introduction session for our {course} class.
Our next available time is at {class_time}. Please let us know if that time works for you. Best regards.""")

createMessage(name, course, class_time)