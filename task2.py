import requests
from bs4 import BeautifulSoup as BS


def list_animal() -> list:  # Получаем список всех животных с википедии
    page = requests.get('https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:'
                        '%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0'
                        '%B0%D0%B2%D0%B8%D1%82%D1%83')
    soup = BS(page.text, 'lxml')
    animals = []
    count = 0
    while True:
        try:
            for animal in soup.find(class_='mw-category mw-category-columns'):
                for animal_1 in animal.find_all('a'):
                    animals.append(animal_1.get('title'))
            if count == 0:
                new_page = soup.find('div', id='mw-pages').find('a').get('href')
            else:
                new_page = soup.find('div', id='mw-pages').find_all('a')[1].get('href')
            count += 1
            page = requests.get(f'https://ru.wikipedia.org{new_page}')
            soup = BS(page.text, 'lxml')
        except TypeError:
            return animals


def dict_animal() -> dict:  # Считаем кол-во животных на каждую букву алфавита
    dict_animals = dict(zip('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ', [0 for i in range(59)]))
    for animal in list_animal():
        dict_animals[animal[0]] += 1
    return dict_animals


if __name__ == '__main__':
    print(dict_animal())
