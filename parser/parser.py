import requests
from bs4 import BeautifulSoup

URL = "https://stopgame.ru/games"
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
    'accept': '*/*'}
HOST = 'https://stopgame.ru'

# https://bsgclub.admin.enes.tech/cashbox/o/2/073903/refill/check
# {
#    'user-agent': '(Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
#    'accept': '*/*'}
def get_html(url, params=None) -> requests.Response:
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('div', class_='item game-summary game-summary-horiz')
    cars = []

    for item in items:
        cars.append({
            'платформа': item.find('span', class_='value').get_text(strip=True),
            'Игра': item.find('div', class_='caption caption-bold').get_text(strip=True),
            'ссылка': HOST + item.find('a',  href=True).get('href'),
        })

    return cars
#{'platform': 'Платформа:', 'title': '\n\n#Funtime \n'}

def parse():
    html = get_html(URL)
    print(html.status_code)
    if html.status_code == 200:
       cars = get_content(html)
    else:
        print("error ")


parse()
