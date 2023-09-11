"""
Программа загружает топ 10 песен на данный момент с сайта "https://muztok.net/"
Песни сохраняет в папке "media"
"""
import requests
from bs4 import BeautifulSoup
from time import sleep
import os

url_global = "https://muztok.net/"
url = "https://muztok.net/36453-krylata-kaminnya-u-krosah.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"}

try:  # создаём папку media, если есть вызываем исключение
    os.mkdir("media", 0o755)
except Exception as ex:
    print(ex)

list_files_media = os.listdir(path="media")  # считываем все файлы с папки медиа для сравнения
print(list_files_media)


def main():
    count = 0
    r = requests.get(url_global, headers=headers)  # Отправляем запрос на страницу
    # print(r.headers)
    # print(r.text)
    data = BeautifulSoup(r.text, "html.parser")
    data_all = data.find_all('a', class_='topside-in fx-1')
    data_url = [teg['href'] for teg in data_all]
    print(data_url)

    for i in data_url:
        response = requests.get(i, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")  # Парсим HTML-контент страницы
        download_link = soup.find('div', {'class': 'fright'})[
            'data-track']  # Находим элемент, содержащий URL для скачивания
        name = soup.find("div", class_='fright')['data-title']
        print(name)
        translation_table = str.maketrans('', '', '<>:/|?*')
        name = name.translate(translation_table)
        # print(download_link, "/n")
        file_response = requests.get(download_link, headers=headers, stream=True)  # Теперь можем загрузить файл

        name_mp3 = name + ".mp3"
        if name_mp3 not in list_files_media:
            with open(f"media/{name}.mp3", 'wb') as file:  # Сохраняем файл на диск
                file.write(file_response.content)
                count += 1
        sleep(1)

    print("Новых песен скачано", count)


if __name__ == "__main__":
    main()
