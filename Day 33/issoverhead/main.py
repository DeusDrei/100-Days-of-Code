import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "your email"
MY_PASSWORD = "your password"

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


#-----------------------------------COMPARE------------------------------------#
def is_above_and_is_night(iss_lat, iss_long, my_lat, my_long, sunset, sunrise, current_hour):
    if (iss_lat <= my_lat + 5 and iss_lat >= my_lat - 5) and (iss_long <= my_long + 5 and iss_long >= my_long - 5):
        if current_hour >= sunset or current_hour <= sunrise:
            return True
        return False
    return False


#-------------------------------------ISS---------------------------------------#
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


#-------------------------------SUNRISE/SUNSET-----------------------------------#
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour


#---------------------------------EMAIL SENDER-----------------------------------#
while True:
    time.sleep(60)  # Runs every minute to check
    if is_above_and_is_night(iss_lat=iss_latitude, iss_long=iss_longitude, my_long=MY_LONG, my_lat=MY_LAT, sunset=sunset, 
                            sunrise=sunrise, current_hour=hour):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:LOOK UP!\n\nThe ISS is above you right now!")
    else:
        print("Not above")




