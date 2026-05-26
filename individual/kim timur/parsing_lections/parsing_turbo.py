""" 
Парсинг машин с сайта turbo.kg
будем вытаскивать первые 20 страниц 
и все данные о машинах и сохранять их в CSV файл

Какие данные нужны:
название автомобиля модель
цена
год выпуска
url - обьявления
url-картинок

добавочно вытащить 13 характеристик (руль, кузов, пробег)
- все ссылки на карти картинки
- дата и время публикации

Интсрументы:
requests - HTTP запросов
BeatifulSoup4 - парсинг HTML
pandas - чтобы записать в CSV файлы
lxml - бекенд для быстрой обработки работает с BS4
"""

#=========================== Начало ========================
import requests
from bs4 import BeautifulSoup

import pandas as pd

import time

import re
# re - регулярные выражения (для очистки цены 12000 сом - 12000)
from urllib.parse import urljoin

#======================== настройка и константы ==============
BASE_URL = "https://turbo.kg" # Базовая URL на сайт который мы парсим
OUTPUT_CSV = 'turbo_cars.csv' # файл куда запишем результат
DELAY_SEC = 1.0 # Пауза между запросами
PARSE_TO_PAGE = 20

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}
# User-Agent - нужен чтобы сайт думал что запрос 
# делается от человека а не от машины

#Accept-Language - показать на каком языке мы хотим получить данные
# Accept - какой вид формата ответ мы хотим получить


# ======================= Загрузка HTML ================
SESSION = requests.Session()
SESSION.headers.update(HEADERS)
# requests.Session() - Переиспользует TCP соединение и cookies между запросами
# для чего:
# Ускоряет работу
# автоматический сохраняет cookies

def fetch_html(url: str, retries: int = 3) -> str | None:
    """
    Скачивает HTML
    использовать Session 
    установим таймаут ожиданий ответа от запроса 15 секунд
    """
    for attempt in range(1, retries+1):
        try:
            response = SESSION.get(url, timeout=15)
            # Если мы получаем ошибку 400/500
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Попытка {attempt} из {retries} для {url}: {e}")
            
            if attempt == retries:
                return None
            
            time.sleep(2 ** attempt)
            # Экспонциональная пауза - даем передохнуть серверу 
            # и смешиваемя с запросами других пользователей
            
    return None


# print(fetch_html(url=BASE_URL))

# ================== Вспомогательные функции ===============
def extract_price(text: str) -> int | None:
    """
    Превращает строку в число
    очищаем цену 12345 сом -> 12345
    
    Алгоритм работы:
    1) Если в тексте есть слово 'сом' берем числа которые идут до него(пееред ним)
    2) Если сом нету, берем все цифры подряд
     """

    if not text:
        return None
    
    text = text.replace("\xa0", " ")
    
    match = re.search(r'([\d\s]+)\s*сом', text)
    if match:
        digits = re.sub(r'\D', "", match.group(1))
        return int(digits) if digits else None
    
    digits = re.sub(r'\D', '', text)
    return int(digits) if digits else None


def extract_year(text: str) -> int | None:
    """
    Достает год из строки
    """
    if not text:
        return None
    
    match = re.search(r'\b(19\d{2}|20\d{2})\b', text)
    return int(match.group(1) if match else None)

def extract_mileage(text: str) -> int | None:
    if not text:
        return None
    
    digits = re.sub(r'[^\d]', "", text)
    return int(digits) if digits else None

# ================= Парсинг turbo-stream ответа ==============
"""
<turbo-sream>
<templatte>
Контент
</template>
"""

def extract_turbo_template(html:str) -> str:
    match = re.search(r'<template>(.*?)</template>', html, flags=re.DOTALL)
    return match.group(1) if match else html

