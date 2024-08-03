import requests
import smtplib

api_endpt = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your_api_key"

m_list =[]

weather_params={
    "lat":9.444080,
    "lon":77.559270,
    "appid":api_key,
    "cnt":4
}

response = requests.get(api_endpt,params=weather_params)
response.raise_for_status()

umbrella= False
for x in range(0,4):
    result = response.json()["list"][x]["weather"][0]["id"]
    if result<700:
        umbrella = True
if umbrella:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login("email", "password")
        for x in m_list:
            connection.sendmail(
                from_addr="email",
                to_addrs=x,
                msg="Subject: Rain alert!!\n\nThere is a chance of raining today. "
                    "Take Umbrella!! "

            )


