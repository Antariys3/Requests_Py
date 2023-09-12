"""
Это файл с функциями для файла "Save_in_excel". Тут реализовано три функции, с помощью генератора.
Функция get_url парсит сайт и возвращает список.
Функция array вытягивает имя, цену и ссылку на фото.
Функция download скачивает фото в папку photo.
"""
import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"}


def download(url):
    resp = requests.get(url, stream=True)
    with open(f"image/{url.split('/')[-1]}", "wb") as file:
        for value in resp.iter_content(1024 * 1024):
            file.write(value)


def get_url():
    for count in range(1, 7):
        print("Page", count)
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="w-full rounded border")
        for item in data:
            yield item


def array():
    for i in get_url():
        sleep(1)
        name = i.find("h4").text.strip()
        price = i.find("h5").text.strip()
        url_img = "https://scrapingclub.com" + i.find('img', class_='card-img-top img-fluid')['src']
        download(url_img)
        yield name, price, url_img
