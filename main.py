# Imports
import os
import requests
import json
from dotenv import load_dotenv
from math import ceil

# Global Variables
API_KEY = None
SLACK_WEBHOOK_URL = None


def getWeatherDetails():
    # Make request to the OpenWeatherMap API and convert the JSON response into a dict
    response = requests.get("https://api.openweathermap.org/data/2.5/onecall?appid=" + API_KEY + "&lat=-37.9106&lon=145.1348&units=metric&exclude=minutely,hourly")
    weatherData = json.loads(json.dumps(response.json()))

    # Get the current weather data
    currentWeather = weatherData["current"]

    # Get the current day's forecast
    currentDayForecast = weatherData["daily"][0]

    return {
        "current": currentWeather,
        "forecast": currentDayForecast
    }


def createMessage(data):
    # Create the message
    weatherMessage = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":cloud: Today's Weather: " + data["forecast"]["weather"][0]["description"].title(),
                    "emoji": True
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Current Temperature*: " + str(
                        0.5 * ceil(2.0 * data["current"]["temp"])) + "° C\n\n*Feels Like Temperature*: " + str(
                        0.5 * ceil(2.0 * data["current"]["feels_like"])) + "° C\n\n*Forecasted Max*: " + str(
                        0.5 * ceil(2.0 * data["forecast"]["temp"]["max"])) + "° C\n\n*Forecasted Min*: " + str(
                        0.5 * ceil(2.0 * data["forecast"]["temp"]["min"])) + "° C\n\n*Chance of Rain?*: " + str(
                        int(data["forecast"]["pop"] * 100)) + "%"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "http://openweathermap.org/img/wn/" + data["forecast"]["weather"][0][
                        "icon"] + "@2x.png",
                    "alt_text": "Icon for today's weather"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Want to know more?"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": ":pushpin: See more at the BOM Site",
                        "emoji": True
                    },
                    "url": "http://www.bom.gov.au",
                    "action_id": "button-action"
                }
            }
        ]
    }

    return weatherMessage


def sendMessage(message):
    requests.post(SLACK_WEBHOOK_URL, data=json.dumps(message))


if __name__ == '__main__':
    load_dotenv()

    # Get the API key from the .env file
    API_KEY = os.getenv('API_KEY')
    SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

    if API_KEY is None or SLACK_WEBHOOK_URL is None:
        print("Missing environment variables. Please ensure you have both a value for API_KEY and SLACK_WEBHOOK_URL in your .env file.")
        exit(-1)
    else:
        details = getWeatherDetails()
        message = createMessage(details)
        sendMessage(message)
