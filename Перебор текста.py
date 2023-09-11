import requests
from bs4 import BeautifulSoup

url = "https://ru.noveldrama.com/mogushchestvennyi-nedotepa/r1614.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"}
response = requests.get(url, headers=headers)

# print(response.headers, "headers")
print(response.status_code, "status_code")
# print(response.request, "request")
# print(response.text)


html_content = response.content
soup = BeautifulSoup(html_content, 'lxml')
# print(soup)

# Извлечение текста из параграфов
paragraphs = soup.find_all('p')
# print(paragraphs.text)

# Пройдитесь по каждому элементу <p>
for paragraph in paragraphs:
    # Получите текстовое содержимое элемента <p>
    paragraph_text = paragraph.get_text()

    # Выведите содержимое элемента <p>
    print(paragraph_text)

#
# with open("Недотёпа.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     for line in lines:
#         line = line.replace("", "").replace("Ceneo.pl", "").replace("ENERG: E", "").replace("Najlepsza porównywarka", "")
#
#
# with open("Могущественный недотёпа.txt", "w", encoding="utf-8") as file:
#     text_to_write = "\n".join(lines)
#     file.write(text_to_write)

