from requests import Session
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com"
url_log = "https://quotes.toscrape.com/login"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"}

work = Session()
work.get(url, headers=headers)
response = work.get(url_log, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
token = soup.find("input")["value"]
print(token)
data = {"csrf_token": token, "username": "123", "password": "123"}
result = work.post(url_log, headers=headers, data=data, allow_redirects=True)
print(result.text)
""" 
Дальше начинаем наш парсинг
"""
