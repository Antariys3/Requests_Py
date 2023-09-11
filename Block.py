import requests
from bs4 import BeautifulSoup
import time

url = "https://brotorrent.net/352-factory-town.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"}


count = 0

start = time.time()
while count < 900000:
    count += 1
    response = requests.get(url, headers=headers)

    if count % 100 == 0:
        stop = time.time()
        print(count, stop - start)

print("конец")
