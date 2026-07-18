# Rain Alert Notifier ☔

An intermediate Python automation script that monitors local atmospheric conditions and ensures you never get caught in the rain without an umbrella.

## 🚀 Features
* **Live Forecast Tracking:** Fetches multi-layered, nested JSON weather data from the OpenWeatherMap API.
* **Automated SMS Alerts:** Interfaces with the Twilio cloud communications API to dispatch text alerts directly to a mobile device.
* **Production-Grade Security:** Utilizes environment variables (`os` module) to keep sensitive API keys and authentication tokens completely hidden from the source code.

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Libraries:** `requests`, `os`
* **APIs:** OpenWeatherMap, Twilio SMS Gateway
