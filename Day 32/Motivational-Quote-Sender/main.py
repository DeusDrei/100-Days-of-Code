import smtplib
import random
import datetime as dt

my_email = "uremail@gmail.com"
my_password = "samplepassword"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as f:
        quotes = [line.strip() for line in f.readlines()]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=my_email, 
                            msg=f"Subject:Monday Motivational Quote\n\n{random.choice(quotes)}")


