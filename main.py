#This webscraper is supposed to input weather data then output it so the user can understand it.
import requests
from bs4 import BeautifulSoup

def temp_finder():
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
temp_finder()

def temp_eval():
    if temp <= 32:
        print("It is very cold. There is a chance school could be closed. Keep an eye on the news.")
    elif temp >= 65:
        print("It is going to be warm today, make sure to drink water.")
    else:
        print("It will be a normal day, prepare for school as normal.")
temp_eval()

