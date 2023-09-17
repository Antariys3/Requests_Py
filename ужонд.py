import requests
# from bs4 import BeautifulSoup
# from time import sleep

cookies = {
    '_gid': 'GA1.2.1129379420.1694789566',
    '_ga': 'GA1.1.388693999.1694789566',
    '_ga_ZRZLNC2FN6': 'GS1.1.1694789565.1.1.1694789593.0.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_gid=GA1.2.1129379420.1694789566; _ga=GA1.1.388693999.1694789566; _ga_ZRZLNC2FN6=GS1.1.1694789565.1.1.1694789593.0.0.0',
    'If-Modified-Since': 'Tue, 14 Jun 2022 10:00:28 GMT',
    'If-None-Match': '"62a85c3c-529"',
    'Referer': 'https://przybysz.duw.pl/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

response = requests.get('https://pio-przybysz.duw.pl/login', cookies=cookies, headers=headers)
print(response.status_code)
# sleep(1)
# data = {"login": "333antar333@gmail.com", "password": "An^Tariys33"}
# result = work.post(url_login, headers=headers, data=data, allow_redirects=True)
# print(result.text)
