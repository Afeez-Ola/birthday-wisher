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
import pandas as pd
import datetime
import random
from dotenv import dotenv_values

# Load environment variables
env_vars = dotenv_values('.env')
my_email = env_vars['MY_EMAIL']
password = env_vars['PASSWORD']

# Read birthday data from CSV file
birthday_file = pd.read_csv("birthdays.csv")
today_month = datetime.datetime.now().month
today_day = datetime.datetime.now().day

# Filter birthdays for today
birthday_df = birthday_file[(birthday_file["month"] == today_month) & (birthday_file["day"] == today_day)]

if not birthday_df.empty:
    birthday_celebrant = birthday_df.iloc[0]["name"]
    letter_templates = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    random_number = random.randint(0, len(letter_templates) - 1)

    with open(letter_templates[random_number]) as letters_file:
        letters_list = letters_file.readlines()

        if birthday_celebrant:
            letter_salutation = letters_list[0].replace("[NAME]", birthday_celebrant)
            letters_list[0] = letter_salutation

    final_letter = "".join(letters_list)

    # Create an SMTP connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as connection:
            connection.starttls()
            connection.login(my_email, password)

            # Send an email
            recipient = "afeezmobolajiola@example.com"
            subject = "BIRTHDAY WISHES"

            message = f"Subject: {subject}\n\n{final_letter}"

            connection.sendmail(my_email, recipient, message)
            print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("Failed to send email:", str(e))
else:
    print("No birthdays today.")
