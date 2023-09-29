import requests
from bs4 import BeautifulSoup


def parser(url, headers):
    # поиск блока с текстом для сохранения
    response = requests.get(url, headers=headers)
    print(response.status_code)
    # print(response.headers)
    # print(response.text)
    page = BeautifulSoup(response.text, "lxml")
    reader_body = page.find("div", class_="readerbody-wg")

    # поиск URL для перехода на новую страницу
    data_all = page.find('div', class_='readernav-wg text-center')
    tag = data_all.find('a', class_='btn btn-success next')
    href = ""
    if tag:
        href = tag.get('href')
        href = "https://ru.noveldrama.com" + href
        # print("href", href)

    # # сохранение блока с текстом
    # with open("первая.html", "w", encoding="utf-8") as file:
    #     file.write(response.text)  # сохранение страницы HTML (response.text) or reader_body.prettify()
    #     print("Файл сохранён")

    return str(reader_body), href


def tag_definition(text, index=0):  # Определение(распознание) тега
    start_char = "<"
    end_char = ">"

    while True:
        start_pos_char = text.find(start_char, index)
        if start_pos_char == -1:
            break
        end_pos_char = text.find(end_char, start_pos_char)
        if end_pos_char == -1:
            break

        index = end_pos_char + len(end_char)
        yield text[start_pos_char:end_pos_char + 1], index


def extract_and_save_paragraphs(text):  # извлечь и сохранить абзацы
    paragraphs = []
    start_tag = "<p>"
    end_tag = "</p>"
    start_index = 0

    while True:
        start_pos = text.find(start_tag, start_index)
        if start_pos == -1:
            break
        end_pos = text.find(end_tag, start_pos)
        if end_pos == -1:
            break

        paragraph_text = text[start_pos + len(start_tag):end_pos]
        paragraphs.append(paragraph_text)
        start_index = end_pos + len(end_tag)

    for paragraph in paragraphs:
        print(paragraph)

    if paragraphs:
        with open("недотёпа1.txt", "w", encoding="utf-8") as file:
            for paragraph in paragraphs:
                file.write(paragraph + "\n")
    else:
        print("Параграфы не найдены в тексте.")


def tag_sorting(tag, index, text):
    if tag == "<p>":
        tag_p(index, text)
    elif tag == "<style>":
        tag_style(index, text)


def tag_p(index, text):
    end_tag = "</p>"
    end_string = text.find(end_tag, index)
    if end_string == -1:
        print("-1")
        return ""

    string_text = text[index:end_string]
    save_text(string_text)


def tag_style(index, text):
    tag_end = text.find("</style>", index)
    tag = text[index:tag_end]
    index_class = index
    index = 0

    while True:
        p_period = tag.find("p.", index)
        if p_period == -1:
            break
        p_sentence = tag.find("::", index)
        if p_sentence == -1:
            break
        p_class = tag[p_period + len("p."):p_sentence]

        before_start = tag.find("(", p_sentence)
        before_stop = tag.find(")", p_sentence)
        before = tag[before_start + 1:before_stop]

        after_start = tag.find("(", before_stop + 1)
        after_stop = tag.find(")", after_start)
        after = tag[after_start + 1:after_stop]
        index = after_stop

        arrange_text_tags(text, index_class, p_class, before, after)


def arrange_text_tags(text, index, p_class, before, after):  # расположить текстовые теги
    before = before + '="'
    after = after + '="'
    start_char = "<p "
    end_char = "</p>"

    while True:
        start_pos_char = text.find(start_char, index)
        if start_pos_char == -1:
            break
        end_pos_char = text.find(end_char, start_pos_char)
        if end_pos_char == -1:
            break

        tag_text = text[start_pos_char:end_pos_char + 1], index
        tag_text = str(tag_text)
        if p_class in tag_text:
            before_start = tag_text.find(before)
            before_end = tag_text.find('"', before_start + len(before))
            before_text = tag_text[before_start + len(before):before_end]

            p_start = tag_text.find(">", len(start_char))
            p_end = tag_text.find("<", p_start + 1)
            p_text = tag_text[p_start + 1:p_end]

            after_start = tag_text.find(after)
            after_end = tag_text.find('"', after_start + len(after))
            after_text = tag_text[after_start + len(after):after_end]

            text_string = before_text + p_text + after_text
            save_text(text_string)
        index = end_pos_char + len(end_char)


def save_text(text):
    if text:
        with open("Могущественный_недотёпа_5.txt", "a", encoding="utf-8") as file:
            file.write(text + "\n")


def main():
    url = "https://ru.noveldrama.com/mogushchestvennyi-nedotepa/r68290.html"
    headers = {
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/103.0.5060.53 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-platform': '"Linux"',
    }
    next_url = url
    count = 0
    while next_url and count < 250:
        print("Page", count, next_url)
        text, next_page = parser(next_url, headers)
        for tag, index in tag_definition(text):
            tag_sorting(tag, index, text)
        count += 1
        next_url = next_page


if __name__ == "__main__":
    main()
    print("Книга сохранена")
