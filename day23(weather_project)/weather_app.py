import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def get_weather():
       location=input("Enter Location : ")
       if location.strip()=="":
              return "🗺️ Please enter Location"
       try:
         api_key = os.getenv("API_KEY")
         if not api_key:
             return f"😵api key environment variable not set"
         url=f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
         response = requests.get(url,timeout=10)
         data = response.json()
         if "error" in data:
             return "Please enter Valid Location"
         response.raise_for_status()
       except requests.exceptions.ConnectionError as e:
           return f"📡 Connection Error : {e}"
       except requests.exceptions.Timeout:
           return f"⏱️Error: The request timed out."
       except requests.exceptions.HTTPError as e:
           return f"HTTP error occurred : {e}"
       except requests.exceptions.RequestException as e:
           return f"An Error Occured : {e}"

       with open("weather_report.txt","a",encoding="utf-8") as f:
           f.write(f"""
☁️ WEATHER REPORT
----------------------------------
🏙️ City           : {data['location']['name']}
🌎 Condition      : {data['current']['condition']['text']}
🌡️ Temperature    : {data['current']['temp_c']}°C
🍃 Wind           : {data['current']['wind_kph']} Km/h
🌧️ Precipitation  : {data['current']['precip_mm']}mm
💧 Humidity       : {data['current']['humidity']}%
⏱️Date&Time       : {datetime.now().strftime("%d-%m-%Y %I:%M:%S:%p")}
--------------------------------
""")
           return "✅ Weather data successfully fetched and saved"
print(get_weather())

