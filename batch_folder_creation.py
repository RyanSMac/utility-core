# To create a directory for all files for a new batch of utility cores

import os

static_path = "/Users/Ryan McConville/Documents"  # Declare Static Path for files
volatile_path = static_path  # Copied static path to variable path

client_name = input("Enter client initials: ")  # Gets client name for files creation
client_name = "/" + client_name  # Creates path name

batch_date = input("Enter batch date: ")  # Get date of batch

# Take date and break it into parts for file naming later
split_date = batch_date.split("/")  # Splits date into mouth and year
mouth = split_date[0] + "."  # Separates mouth and adds dot after
year = split_date[1]  # Separates Year
full_year = "20" + year  # Creates full year for file naming

# Dictionary for mouth and number pairs
number_mouth = {"01.": "JAN",
                "02.": "FED",
                "03.": "MAR",
                "04.": "APR",
                "05.": "MAY",
                "06.": "JUN",
                "07.": "JUL",
                "08.": "AUG",
                "09.": "SEP",
                "10.": "OCT",
                "11.": "NOV",
                "12": "DEC"}

word_mouth = " " + number_mouth[mouth]  # Adds spaces and matches num
mouth_path = "/" + mouth + word_mouth

try:
    os.mkdir("/Users/Ryan McConville/Documents" + client_name)  # Try to make file
except OSError:
    volatile_path = static_path + client_name  # if error chances volatile_path
else:
    volatile_path = volatile_path + client_name  # if files create chance path

try:
    os.mkdir(volatile_path + "/Utility Coring " + full_year)  # Try to make file
except OSError:
    volatile_path += "/Utility Coring " + full_year  # if error chances volatile_path
else:
    volatile_path += "/Utility Coring " + full_year  # if files create chance path

try:
    os.mkdir(volatile_path + mouth_path + " - Utility Cores")  # Try to make file
except OSError:
    volatile_path += mouth_path + " - Utility Cores" # if error chances volatile_path
else:
    volatile_path += mouth_path + " - Utility Cores"  # if files create chance path

try:
    os.mkdir(volatile_path + "/Air Voids")
    os.mkdir(volatile_path + "/Database")
    os.mkdir(volatile_path + "/Invoices")
    os.mkdir(volatile_path + "/Locations")
    os.mkdir(volatile_path + "/Photos")
    os.mkdir(volatile_path + "/Reports")
except OSError:
    print("Directory already exists")
else:
    print("Directory creation complete")

print("Exiting...")
