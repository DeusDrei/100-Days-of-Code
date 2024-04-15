from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = ''
smtp_password = ''

amazon_url = "https://www.amazon.com/SAMSUNG-Factory-Unlocked-Smartphone-Adaptive/dp/B0BLP4J9RR?ref_=Oct_DLandingS_D_469bf428_0&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(amazon_url, headers=headers)
item = response.text

soup = BeautifulSoup(item, "html.parser")
price = soup.find(name="span", class_="a-offscreen").text
price_no_currency = float(price.split("$")[1])

if price_no_currency < 1000:
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() 

        server.login(smtp_username, smtp_password)

        subject = 'SAMSUNG Galaxy S23+ Plus Price Update'
        sender_email = ''
        receiver_email = ''
        message_text = f'SAMSUNG Galaxy S23+ Plus is now ${price_no_currency}.\n{amazon_url}'

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_text, 'plain'))
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        server.quit()
        
