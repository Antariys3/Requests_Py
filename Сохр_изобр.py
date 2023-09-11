import requests
from PIL import Image
from io import BytesIO


def parse(q, page_count):
    header = {"Authorization": "pcHUnGe4b2fJN3qwPHInOLV5lmzKO7oME52yuuv7YEmuAxbs9AMJetWc"}
    url = f'https://api.pexels.com/v1/search?query={q}&per_page=1'
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        print(r.json())
        var = r.json()
        while int(var["page"]) <= int(page_count):
            print(var['page'])
            photo_url = var["photos"][0]["src"]["original"]  # url фото
            resp = requests.get(photo_url)  # байтовое состояние
            image = Image.open(BytesIO(resp.content))
            image.save(f"photo/{q}_{var['page']}.{photo_url.split('.')[-1]}")

            r = requests.get(var["next_page"], headers=header)
            var = r.json()
    else:
        print(r.status_code)


def main() -> None:
    q = input("Query ")
    page_count = input("Page count ")
    parse(q, page_count)


main()
