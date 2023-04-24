import requests
import json
import os

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=02130894c7824cc599b163028232404&q={city}&aqi=no"

r = requests.get(url)
# print(r.text)
# print(type(r.text))
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
# print(wdic["current"]["temp_c"])
os.system(f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('The current weather in {city} is {w} degrees')")