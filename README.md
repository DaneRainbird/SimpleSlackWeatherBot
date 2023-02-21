# SENWWeatherBot
A super-simple Slack Webhook that sends the daily weather from OpenWeatherMap.

## Requirements
- Python,
- An [OpenWeatherMap API Key](https://openweathermap.org/appid), and
- A Slack App capable of using ["Incoming Webhooks"](https://api.slack.com/messaging/webhooks)

## Installation and Configuration
To "install", simply clone / download the script. 

From here, create a new file named `.env` in the same directory, then add your API key and webhook URL in the following format:

```
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
API_KEY=ABCDE1234
```

By default, this script will get the weather for Monash University's Clayton Campus. In order to change this, obtain the [latitude and longitude of your desired location](https://www.latlong.net/), and modify the URL that makes the API call to use those values.

## Running
The script can be run at any time by running `python main.py` in order to send the current weather. 

Optionally, you can configure a cronjob / scheduled task to run this script automatically / on a schedule. 

## License
[The Unlicense](https://unlicense.org/)
