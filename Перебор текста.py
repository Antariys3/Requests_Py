import os
import time

import requests
from selenium import webdriver

url = "https://ru.noveldrama.com/mogushchestvennyi-nedotepa/r1614.html"
cookies = {
    'PHPSESSID': '6urmug8h8c6me2h7dtousb8kf4',
    'pmvid': 'ed068b67-51df-4a98-b447-3ea138052cff',
}

headers = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/103.0.5060.53 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-platform': '"Linux"',
}


def get_source_html(url):
    os.environ["PATH"] += os.pathsep + "/home/antar/Документы/Python/requests/ParseSelenium/chromedriver/chromedriver"
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        # driver.add_cookie(cookies)
        driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": headers})
        driver.get(url=url)
        time.sleep(20)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_source_html(url)


if __name__ == '__main__':
    main()
