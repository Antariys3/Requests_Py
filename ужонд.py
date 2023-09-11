from requests import Session
# from bs4 import BeautifulSoup
from time import sleep
import certifi


url = "https://pio-przybysz.duw.pl/login"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "58",
    "Content-Type": "application/json",
    "Host": "api-przybysz.duw.pl",
    "Origin": "https://pio-przybysz.duw.pl",
    "Referer": "https://pio-przybysz.duw.pl/",
    "sec-ch-ua": "'Chromium';v='106', 'Yandex';v='22', 'Not;A=Brand';v='99'",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"
}
url_login = "https://api-przybysz.duw.pl/api/v1/token/obtain"

work = Session()
work.get(url, headers=headers, verify=certifi.where())
sleep(2)
response = work.get(url, headers=headers, verify=certifi.where())
print(response.status_code)
# sleep(1)
# data = {"login": "333antar333@gmail.com", "password": "An^Tariys33"}
# result = work.post(url_login, headers=headers, data=data, allow_redirects=True)
# print(result.text)


