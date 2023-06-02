##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


import smtplib
import random
import datetime as Datetime
import pandas

birthday_file = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    "month": birthday_file["month"].values,
    "date": birthday_file["day"].values

}

today_month = Datetime.datetime.now().month
today_date = Datetime.datetime.now().day

print(birthday_file["month"].values)
print(birthdays_dict["month"])

birthday_months = birthdays_dict["month"].tolist()

letter_templates = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]
random_number = random.randint(0,len(letter_templates))
