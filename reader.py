import datetime
import re

nic = input("Enter the NIC number: ")

# Simple input validation
pattern = re.compile("^[0-9]{9}[V,v,X,x]$")
if not pattern.match(nic):
    print("Invalid NIC number.")
    print("Valid example: 940041234V, 940041234X")
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
if year%4 != 0:
    days = days - 1


if days > 500:
    gender = "Female"
    days = days - 500
else:
    gender = "Male"


birthday = (datetime.datetime(year, 1, 1) + datetime.timedelta(days - 1)).strftime("%A %d. %B %Y")


print ("Birthday: " + birthday)
print ("Gender: " + gender)