#This webscraper is supposed to input weather data then output it so the user can understand it.
import requests
from bs4 import BeautifulSoup

print("Current Weather Search:")
city = input("Please enter the city you would like to search: ")
state = input("Please enter the State that your city is in: ")

url = f"https://www.google.com/search?q=weather+{city}+{state}"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
temp = soup.find_all('div', attrs={"class": "BNeawe iBp4i AP7Wnd"})
print("################################################")
print(f"Tempature outside in {city}, {state} currently is: " + temp[0].text + ".")
print("################################################")
