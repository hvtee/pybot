# Telegram Weather Bot

This repository contains a Python Telegram bot designed to provide **weather information** for Minsk, Belarus. The bot uses web scraping to fetch weather data from the website `https://world-weather.ru/pogoda/belarus/minsk/`. It offers users the ability to get current weather, today's weather, and tomorrow's weather, as well as interact with various callback buttons.

## Features

1. *Current Weather:* Users can inquire about the current weather in Minsk. The bot fetches and displays the weather conditions and temperature for multiple time slots within the current day.

2. *Today's Weather:* Users can request the weather forecast for the entire day. The bot provides the day and night temperatures, along with the current month and date.

3. *Tomorrow's Weather:* Similar to today's weather, users can receive a weather forecast for the following day. The bot displays day and night temperatures, along with the corresponding month and date.

4. *Interactive Callback Buttons:* The bot employs inline keyboards with callback buttons to provide a user-friendly interface. Users can easily choose between different weather options and information types.

5. *User Information:* The bot also offers the option to retrieve certain information about the user, such as their first name, last name, username, and chat ID.

6. *Greetings and Interaction:* The bot responds to common greetings and inquiries, engaging users in casual conversation.

## Technologies Used

1. **Python:** The bot is implemented using the Python programming language.

2. **Telebot Library:** The `telebot` library is used to interact with the Telegram Bot API.

3. **BeautifulSoup (BS4):** The `requests` library is used to fetch HTML content from the weather website, and `BeautifulSoup` (BS4) is employed for parsing the HTML data to extract weather information.

## Usage

1. Start a chat with the bot by searching for its username on Telegram.

2. Use the `/start` command to initiate the conversation and receive a welcome message.

3. Use the `/main` command to access the main menu with interactive options.

4. Choose between 'Get info', 'Get weather', or 'Test buttons'.

5. If you select 'Get info', you can inquire about your ID, first name, last name, or username.

6. If you select 'Get weather', you can choose between 'Now', 'Today', or 'Tomorrow' to receive corresponding weather information.

7. If you select 'Test buttons', you can experiment with sample buttons.

**Note:** As of my last training data in September 2021, this bot's functionality is accurate based on the provided code. However, please be aware that the Telegram Bot API and the structure of the weather website might change over time, potentially requiring adjustments to the code.
