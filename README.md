# Tesla-Stock-Price-Notification

The Tesla Stock Price Notification project is a Python script that retrieves the stock price of Tesla from the Alpha Vantage API for the past two days, calculates the percentage change between these values, fetches recent news about Tesla using the News API, and sends an SMS containing the percentage change and the three most relevant news articles using the Twilio API.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- Alpha Vantage API key. You can obtain one by signing up on the [Alpha Vantage website](https://www.alphavantage.co/#page-top).
- News API key. You can obtain one by signing up on the [News API website](https://newsapi.org).
- Twilio account and phone number. You'll need to set up a Twilio account and get your account SID, auth token, and a Twilio phone number. You can obtain those signing up on the [Twilio website](https://www.twilio.com/en-us).

## Installation

1. Clone or download this repository to your local machine.

   ```bash
   git clone https://github.com/smereczniaq/Tesla-Stock-Price-Notification.git
2. Navigate to the project directory.
   ```bash
   cd Tesla-Stock-Price-Notification
3. Install the required dependencies using pip.
   ```bash
   pip install requests twilio

## Configuration
1. Create your own environment variables:
   - ALPHAVANTAGE_API_KEY - the value is the key generated for you by Alpha Vantage API
   - NEWS_API_KEY - the value is the key generated for you by News API
   - TWILIO_ACCOUNT_SID - the value is the Account SID generated for you by Twilio. Find it in Account Info section.
   - TWILIO_AUTH_TOKEN - the value is the Auth Token generated for you by Twilio. Find it in Account Info section.
   - TWILIO_PHONE_NUMBER - the value is the Twilio Phone number generated for you by Twilio.
   - MY_PHONE_NUMBER - your personal phone number. Must be verified and connected to your Twilio account.

## Usage
Now you can run your code using your own API keys and phone numbers.
