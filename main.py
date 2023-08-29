import requests
import datetime as dt
from datetime import timedelta
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TIME_SERIES = "5min"

stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": TIME_SERIES,
    "apikey": STOCK_API_KEY,
    "extended_hours": "false",
}

today = dt.date.today()

if today.weekday() == 0:
    yesterday = dt.date.today() - timedelta(days=3)
    day_before = dt.date.today() - timedelta(days=4)
elif today.weekday() == 1:
    yesterday = dt.date.today() - timedelta(days=1)
    day_before = dt.date.today() - timedelta(days=4)
else:
    yesterday = dt.date.today() - timedelta(days=1)
    day_before = dt.date.today() - timedelta(days=2)

stock_response = requests.get(url=stock_url, params=stock_params)
stock_response.raise_for_status()

stock_data = stock_response.json()[f'Time Series ({TIME_SERIES})']

yesterday_start_day_stock_price = float(stock_data[f'{yesterday} 09:30:00']['4. close'])
day_before_end_day_stock_price = float(stock_data[f'{day_before} 15:55:00']['4. close'])

percentage_change = round((yesterday_start_day_stock_price - day_before_end_day_stock_price)
                          / day_before_end_day_stock_price * 100, 4)

news_url = "https://newsapi.org/v2/everything"
news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "from": day_before,
    "to": yesterday,
    "language": "en",
    "sortBy": "relevancy",
}

news_response = requests.get(url=news_url, params=news_params)
news_response.raise_for_status()

news_data = news_response.json()["articles"]

articles = news_data[:3]

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
from_phone_number = os.environ.get("TWILIO_PHONE_NUMBER")
my_phone_number = os.environ.get("MY_PHONE_NUMBER")

client = Client(account_sid, auth_token)

msg = "TSLA"
if percentage_change < 0:
    msg += f" 🔻{percentage_change}%\n"
else:
    msg += f" 🔺{percentage_change}%\n"

for article in articles:
    author = article["author"]
    title = article["title"]
    url = article["url"]
    msg += f"Author: {author}\n" \
           f"Title: {title}\n" \
           f"url: {url}\n\n"

message = client.messages.create(
    body=msg,
    from_=from_phone_number,
    to=my_phone_number
)

print(message.status)
