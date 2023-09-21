import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
APIKEY = "your api key"
NEWSAPIKEY = "your news api key"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": APIKEY,
}
response_stock = requests.get(STOCK_ENDPOINT, params=parameters)
response_stock.raise_for_status()
data = response_stock.json()

closing_price = [value for key, value in data["Time Series (Daily)"].items()]

yesterday = float(closing_price[0]["4. close"])
day_before = float(closing_price[1]["4. close"])

positive_difference = yesterday - day_before

up_down = None
if positive_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

average = (yesterday + day_before) / 2
percentage = round((positive_difference / average) * 100)

if abs(percentage) > 1:
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWSAPIKEY,
    }
    
    response_news = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response_news.raise_for_status()
    news_data = response_news.json()
    articles = news_data["articles"][:3]

    messages = []
    for article in articles:
        headline = article["title"]
        brief = article["description"]
        messages.append(f"{STOCK_NAME}: {up_down}{percentage}%\nHeadline: {headline}\nBrief: {brief}")

    account_sid = 'your sid'
    auth_token = 'your auth token'
    client = Client(account_sid, auth_token)

    for i in messages:
        message = client.messages.create(
            body=i,
            from_='your twilio number',
            to='your phone number'
        )
 


