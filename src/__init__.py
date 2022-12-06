from download import Downloader
from parser import Parser
from data import some_logic
URL = "http://www.hmn.ru/index.php?index=8&value=22113&tz=3&start=2022-11-20&fin=2022-11-28&x=10&y=5"
FILE_PATH = "weather.html"
PARSED_FILE_PATH = "weather.json"
def process(url, web_page_path=None, data_path=None):
    Url = url.split('?')
    params = Url[1].split('&')
    d = {}
    for i in params:
        I = i.split('=')
        if I[1].isdigit():
            d[I[0]] = d.get(I[0], 0) + int(I[1])
        else:
            d[I[0]] = d.get(I[0], '') + I[1]
    if web_page_path == None:
        downloader = Downloader(Url[0], d)
        parser = Parser()
    else:
        downloader = Downloader(Url[0], d, web_page_path)
        parser = Parser(web_page_path)
    if data_path == None:
        d = some_logic()
    else:
        some_logic(data_path)
    return d
process(URL)