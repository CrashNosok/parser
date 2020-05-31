import requests
from bs4 import BeautifulSoup as BS

# url1 = 'https://stopgame.ru/review/new/stopchoice/p1'
# url2 = 'https://stopgame.ru/review/new/stopchoice/p2'
# ...
# всего страниц: 4
# игр на странице: 30
# всего игр: 116

# кол-во страниц на сайте
max_page = 4
# список, в котором будут храниться все страницы с сайта
pages = []
# переменная, в которой хранится адрес страницы
url = 'https://stopgame.ru/review/new/stopchoice/p'

# запускаем цикл, который пройдётся по страницам сайта
for x in range(1, max_page+1):
    # делаем get запрос на адрес в переменной (url + x)
    # добавляем рузельтат в список pages
    pages.append(requests.get(url + str(x)))

# переменная для счёта всех записей
i = 1
# цикл по сохранённым страницам
for r in pages:
    # парсим html (получаем весь код с сайта)
    html = BS(r.content, 'html.parser')
    # print(html)
    # цикл элементам страницы с классом article-summary-card
    for el in html.select('.article-summary-card'):
        # достаём название из ссылки в классе caption
        title = el.select('.caption-bold > a')
        # выводим название статьи
        print(i, title[0].text)
        i += 1
