from bs4.element import TemplateString
from bs4 import BeautifulSoup
import requests

prompt = input("Do you wish to search for the wather? (y/n/yes/no) ")
if prompt == "y":
    city = input("What city would you like to know the weather of? ")
    state = input("What state is the city in? ")
elif prompt == "n":
    print("See ya!")
else:
    print("ERROR! Please use proper syntax!")


url = f"https://www.google.com/search?q=weather+{city}+{state}"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
temp = soup.find_all('div', attrs={"class": "BNeawe iBp4i AP7Wnd"})

for div in temp:
    print(div.text)

