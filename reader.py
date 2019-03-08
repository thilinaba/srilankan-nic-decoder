import datetime
import re

nic = input("Enter first 5 digits of the NIC number: ")

# Simple input validation
pattern = re.compile("^[0-9]{5}$")
if not pattern.match(nic):
    print("Invalid input.")
    print("Valid example: 94004")
    exit()


# born year
year = nic[:2]

# Day of the year to the birth day
days = int(nic[2:5])

#  Get the full year
if int(year) > 30 :
    year = int("19" + year)
else:
    year = int("20" + year)


# reduce one day if not a leap year
if year%4 != 0 and days > 59:
    days = days - 1

# They simply adds 500 to the days if the NIC owner is female
if days > 500:
    gender = "Female"
    days = days - 500
else:
    gender = "Male"


# datetime.datetime(year, 1, 1) = time to the 1st of jan of the year
# datetime.timedelta(days - 1) = time of the number of days. we -1 because 1st of jan is already included
birthday = datetime.datetime(year, 1, 1) + datetime.timedelta(days - 1)
age = int((datetime.datetime.now() - birthday) / datetime.timedelta(365))

print("Birthday: " + birthday.strftime("%A %d. %B %Y"))
print("Gender: " + gender)
print("Age: " + str(age) + " years")