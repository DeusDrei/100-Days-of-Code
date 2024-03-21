from datetime import datetime
import pandas as pd
import random
import smtplib

MY_EMAIL = "youremail"
MY_PASSWORD = "yourpassword"

now = datetime.now()
date_today = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
birthdays = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}
if date_today in birthdays:
    birthday_person = birthdays[date_today]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as f:
        contents = f.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}")

