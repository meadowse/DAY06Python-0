import requests
# URL = "http://www.hmn.ru/index.php"      # тут используйте адрес вашего сайта
# PARAMS = {                               # эти параметры также индивидуальны для страницы, которую вы скрапите
#     "index": 8,
#     "value": 22113,
#     "tz": 3,
#     "start": "2022-11-20",
#     "fin": "2022-11-28",
#     "x": 10,
#     "y": 5,
# }
FILE_PATH = "weather.html"               # используйте ваше название. Будет более понятно, если будете исполь-                  
class Downloader:                        # зовать расширение html, т.к. в этом файле будет код html-страницы
    def __init__(self, url, params, method="GET", file_path=FILE_PATH):
        self.url = url
        self.params = params
        self.method = method
        self._file_path = file_path
        self.save(file_path)
    def get_html(self):
        reg = requests.get(self.url, self.params, stream=True)
        text = reg.text
        return text
    def save(self, File_path):
        with open(File_path, "w", encoding='koi8-r') as file:
            file.write(self.get_html())
    def get_file_path(self):
        self.save(self._file_path)
        return self._file_path
    file_path = property(get_file_path)
# downloader = Downloader(url=URL, params=PARAMS, method="GET")
# print(downloader.get_html())       # этот метод возвращает строку с контентом, которую получил по запросу на URL
# downloader.save(FILE_PATH)  # метод сохраняет полученную строку в файл, путь к которому подается в аргументе