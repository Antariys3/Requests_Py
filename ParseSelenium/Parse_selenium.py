import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

url = "https://spb.zoon.ru/medical/"
cookies = {
    'locale': 'ru_RU',
    'sid': 'e75f7f536504fbe2a1912238258136',
    'city': 'spb',
    'anon_id': '20230916035043jGMB.dbce',
    '_ga': 'GA1.2.1768066762.1694825445',
    '_gid': 'GA1.2.1343487235.1694825445',
    '_ym_uid': '1694825445802235694',
    '_ym_d': '1694825445',
    '_ym_isad': '2',
    'AATestGlobal': 'variation',
    '_ga_KK9RGD935B': 'GS1.2.1694825445.1.1.1694831038.2.0.0',
}
cookies = {
    'locale': 'ru_RU',
    'sid': 'e75f7f536504fbe2a1912238258136',
    'city': 'spb',
    'anon_id': '20230916035043jGMB.dbce',
    '_ga': 'GA1.2.1768066762.1694825445',
    '_gid': 'GA1.2.1343487235.1694825445',
    '_ym_uid': '1694825445802235694',
    '_ym_d': '1694825445',
    '_ym_isad': '2',
    'AATestGlobal': 'variation',
    '_gat': '1',
    '_ga_KK9RGD935B': 'GS1.2.1694825445.1.1.1694830980.60.0.0',
}
headers = {
    'authority': 'spb.zoon.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'locale=ru_RU; sid=e75f7f536504fbe2a1912238258136; city=spb; anon_id=20230916035043jGMB.dbce; _ga=GA1.2.1768066762.1694825445; _gid=GA1.2.1343487235.1694825445; _ym_uid=1694825445802235694; _ym_d=1694825445; _ym_isad=2; _gat=1; _ga_KK9RGD935B=GS1.2.1694825445.1.1.1694829779.60.0.0',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}


def get_source_html(url):
    os.environ["PATH"] += os.pathsep + "/home/antar/Документы/Python/requests/ParseSelenium/chromedriver/chromedriver"
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        # driver.add_cookie(cookies)
        driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": headers})
        driver.get(url=url)
        time.sleep(5)
        for i in range(2, 6):
            # driver.add_cookie(cookies)
            driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": headers})
            driver.get(url=f"https://spb.zoon.ru/medical/page-{i}/")
            time.sleep(10)

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_source_html(url)


if __name__ == "__main__":
    main()
