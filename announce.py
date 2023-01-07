from bs4 import BeautifulSoup
import requests
from datetime import date
import time
import telegram


bot = telegram.Bot(token="5464683460:AAFl5k_bNZhp_hyJCSUBF_N3NZVF6pxDqVg")
for i in bot.getUpdates():
    print(i.message)
response = requests.get("https://cafe.bithumb.com/view/boards/43")
html = response.text
soup = BeautifulSoup(html,"html.parser")
words = soup.select(".invisible-mobile.small-size")

for word in words:
    num = word.text
    if num != "■":
        title = word.find_parent("tr")
        num = word.text

        break
    
a = title.select(".one-line > a")
b = a[0].text
print(num,b)