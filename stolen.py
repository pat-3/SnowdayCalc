import smtplib, ssl
from threading import local
import requests
import math

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = ""#add email inside the quotations
password = ""#Add password inside the quotations

def SendMessage(message):
    receiver_email = "" #add email you are sending it to inside the quotations

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


page = requests.get("https://weather.com/weather/tenday/l/a05baa5a94807b678c0d9403cbc131381e2b33af1f6264959d7543eaa3b8ed7e")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

temps = soup.find_all(class_="DailyContent--temp--3d4dn")
Names = soup.find_all(class_="DetailsSummary--daypartName--2FBp2")

data = {}

for x in range(1,11):
    page = math.floor((x+1)/2)
    data.update(
        {str(page): {
        "high": 0,
        "low": 0,
        "day": "Monday",
        }}
    )
    print(temps[1])
    data[str(page)]["high"] = temps[x].text[:-1]
    x += 1
    data[str(page)]["low"] = temps[x].text[:-1]
 

for day in range(1,6):
    data[str(day)]["day"] = Names[day].text

print(data)

for x in range(1,25):
    SendMessage("""
    """ + data["1"]["day"] + ": " + data["1"]["high"] + "/" + data["1"]["low"] + """ 
    """ + data["2"]["day"] + ": " + data["2"]["high"] + "/" + data["2"]["low"] + """ 
    """ + data["3"]["day"] + ": " + data["3"]["high"] + "/" + data["3"]["low"] + """ 
    """ + data["4"]["day"] + ": " + data["4"]["high"] + "/" + data["4"]["low"] + """ 
    """ + data["5"]["day"] + ": " + data["5"]["high"] + "/" + data["5"]["low"] + """ 
    """)
