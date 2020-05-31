import requests
from bs4 import BeautifulSoup as BS

# email
# login: kakoetoimya90@mail.ru
# password: Plovchik90

# smartprogress
# login: kakoetoimya90@mail.ru
# password: Plovchik90

# при входе на сайт, сайт шлёт POST запрос на адрес
# при этом генерируется CSRF токен

# делаем не просто запрос, а ещё храним кукисы на время работы с ним
s = requests.Session()
# получаем CSRF
# делаем запрос к странице
auth_html = s.get('https://smartprogress.do/')
# достаём html код из запроса
auth_bs = BS(auth_html.content, 'html.parser')
# достаём CSRF токен
csrf = auth_bs.select('input[name=YII_CSRF_TOKEN]')[0]['value']

# делаем логин на сайт
# это словарь с данными для POST запроса (берётся из инструментов разработчика в браузере)
payload = {
    'YII_CSRF_TOKEN': csrf,
    'returnUrl': '/',
    'UserLoginForm[email]': 'kakoetoimya90@mail.ru',
    'UserLoginForm[password]': 'Plovchik90',
    'UserLoginForm[rememberMe]': 1,
}

# делаем post запрос на данный url (он тожн достаётся из инструментов разработчика)
asnw = s.post('https://smartprogress.do/user/login/', data=payload)
# получаем html код
anw_bs = BS(asnw.content, 'html.parser')

# выводим имя, уровень, опыт
print('Имя: ' + anw_bs.select('.user-menu__name')[0].text.strip())
print('Уровень: ' + anw_bs.select('.user-menu__info-text--lvl')[0].text.strip())
print('Опыт: ' + anw_bs.select('.user-menu__info-text--exp')[0].text.strip())

