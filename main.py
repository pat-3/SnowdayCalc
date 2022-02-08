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
temperature = temp[0].text


if temperature <= 32:
    print("It is very cold. It is currently " + temp[0].text + ". There is a chance school could be closed. Keep an eye on the news.")
elif temperature >= 65:
    print("It is going to be warm today. It is currently "  + temp[0].text + ". Make sure to drink water.")
else:
    print("It will be a normal day. It is currently "  + temp[0].text + ". Prepare for school as normal.")
