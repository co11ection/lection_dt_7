""" Парсинг машин с сайта Turbo.kg
Задача:
вытащить первые 20 страниц и все данные о машинах
данные о автомобилях сохранять в CSV файлы


Какие данные нам нужны:
Название модели
цена
год выпуска
url - обьявления
url - на картинку

добавочно вытащить 13 характеристик (руль кузов, привод, пробег и тд)
- вые ссылки на фотографии
- дата и время создание публикации


Инструменты:
requests - HTTP запросы
BeatifulSoup4 - парсинг HTML
pandas -  экспорта данных в CSV файл
lxml - быстрый бекенд для BS4
"""
# ================================ Начало =====================================
import requests
from bs4 import BeautifulSoup
# BeautifulSoup - превращает строку HTML в определенный скрипт по которому мы можем пройтись и удобно
# искать как HTML теги так и CSS - селекторы
import pandas as pd
# хорошо обрабатывает разные виды ключей и если у одной нету
# определенного поля то сам создает пустую ячейку и заполняет ее None

import time 
# time - нужен для пауз между запросами
import re
# re - регулярные выражения (для очистки цены "1432123 сом" -> 1432123)
from urllib.parse import urljoin
# urljoin - кореектно склеивает относительный URL с базовым


#======================== Насттройки и Константы ================================

BASE_URL = "https://turbo.kg" # Базовая URL(ссылка) на сайт который мы парсим
OUTPUT_CSV = 'turbo_cars.csv' # название файла куда мы запишем наши данные
DELAY_SEC = 1.0 # Пауза между запросами, во избежения Ddos атак и получить бан или ошибюку 429
PAGE_TO_PARSE = 20 # Сколько страниц нам нажо обработать
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}
# HTTP  заголовки. User-Agent ---- ОБЯЗАТЕЛЕН без него выкидывает ошибку 403
# Прикидываемя обычными пользователями десктопным приложением Chrome
# Accept-Language - язык пользователя
# Accept - что сайт ожидает от нас и что мы ждем от сайта (ответ в каком формате)

#=============================== Загрузка HTML ====================================
SESSION = requests.Session()
SESSION.headers.update(HEADERS)
# requests.Session() - переиспользует TCP - соединение и cookies (кеш) между запросами
# для чего это нам:
# Ускоряет работу(не создаем новую ссесию каждый раз)(то не открываем новый браузер)
# автоматический сохраняет cookies, которые ставит при первом входе на сайт.
# бывают моменты когда cookies не приняты выкидывается ошибка 403

def fetch_html(url: str, retries: int = 3) -> str | None:
    """
    Скачивать HTML в виде строки
    
    использует общую SESSION (с cookies между запросами)
    таймаут 15 секунд чтобы не зависать
    """
    for attempt in range(1, retries+1):
        try:
            response = SESSION.get(url, timeout=15)
            #timeout=15 - не ждем дольше чем 15 секунд
            response.raise_for_status()
            # Если сервер вернул нам 4хх или 5хх ошибку - вызовется исключение
            return response.text
        except requests.RequestException as e:
            print(f"Попытка {attempt}/{retries} для {url}: {e}")
            
            # Если сервер не отвечает и это наша последняя попытка то мы сдаемся
            if attempt == retries:
                return None
            
            time.sleep(2 ** attempt)
            # Экспонциональная пауза: 2c, 4c, 9c -даем серверу остыть и смешиваемся с другими запросами
    return None


# print(fetch_html(url=BASE_URL))

# ==================== Вспомогательные функции для очистки ===============================

def extract_price(text: str) -> int | None:
    """
    Превращает строку с ценой в число
    для очистки цены "1432123 сом" -> 1432123
    
    Алгорит работы:
    1) Если в тексте есть слово 'сом' берем цифры, которые идут Непосредственно до него(перед ним) 
        с возможными пробелами между ними
        Это защищает нас от того что в тексте не будет год, обьем
    2) если 'сом' нет берем все цифры подряд
    """
    if not text:
        return None
    
    text = text.replace("\xa0", ' ')
    #Нормализовали неразрывные пробелы (\xa0) в обычные
    
    match = re.search(r'([\d\s]+)\s*сом', text)
    # Ищем цифры [пробелы цифры] ... сом
    if match:
        digits = re.sub(r'\D', '', match.group(1))
        return int(digits) if digits else None
    
    digits = re.sub(r'\D', '', text)
    return int(digits) if digits else None

def extract_year(text: str) -> int | None:
    """
    Достает год из строк
    берем 4 значное число в диапазоне 1900-2099
    """
    if not text:
        return None
    
    match =re.search(r"\b(19\d{2}|20\d{2})\b", text)
    return int(match.group(1)) if match else None

def extract_mileage(text: str) -> int | None:
    
    if not text:
        return None
    
    digits = re.sub(r'[^\d]', "", text)
    return int(digits) if digits else None




