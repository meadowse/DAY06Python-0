import bs4
import re
import requests
import json
FILE_PATH = "weather.html"
PARSED_FILE_PATH = "weather.json"
class Parser:
    def __init__(self, source=FILE_PATH):
        self.source = source
    def parse(self):
        with open(self.source, "r", encoding='koi8-r') as file:
            web_page = file.read()
        soup = bs4.BeautifulSoup(web_page, 'html.parser')
        table = soup.find_all("table", attrs={"class": "m80"})[0]
        time = []                  # создадим список, где будут храниться все значения времени по порядку в таблице
        wind = []                  # а сюда будем добавлять направление ветра
        tr = table.tr              # первый тег tr - это заголовок таблицы, он нам не нужен, поэтому сразу переходим к
                                   # циклу, где ищем следующий соседний тег <tr>
        while tr.find_next_sibling("tr"):  # если следующего тега нет, значит таблица кончилась, можно выходить из цикла
            tr = tr.find_next_sibling("tr")  # теперь tr - это следующий тег <tr> на странице
            if tr.td.b is not None and tr.td["class"][0] == "m11":  # последняя строка таблицы, оказывается, тоже содержит
                                              # тег <b>, поэтому еще и по классу будем фильтровать
                time.extend(tr.td.b)          # дописываем время в список результатов времени, если мы оказались в той
                                              # строке таблицы, где есть время (а таблица слегка криво построена)
                wind.extend(tr.find_all("td")[7])
        d = {}
        for t in time:
            for w in wind:
                d[t] = d.get(t, w)
        return d
    def save(self, parsed_file_path):
        d = self.parse()
        with open(parsed_file_path, "w") as f:
            json.dump(d, f, ensure_ascii=False, indent=4)
# parser = Parser(source=FILE_PATH)    # в конструкторе он принимает путь к файлу, сохраненному Downloader'ом
# parser.parse()                       # должен вернуться список или словарь данных, полученных из кода страницы
# parser.save(PARSED_FILE_PATH)        # сохраняет данные в виде json- или yaml-файла