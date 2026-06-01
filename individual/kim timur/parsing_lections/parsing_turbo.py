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
    return int(match.group(1)) if match else None

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

# ====================== Парсинг одной страницы ========================

def parse_catalog_page(html: str) -> list[dict]:
    """
    Получаем HTMl и вытаскиваем из них данные
    отправляем запрос на https://turbo.kg/?page=page_number
    """
    soup = BeautifulSoup(html, "lxml")
    cars_by_url = {}
    
    for link in soup.select('a[href*="/cars/"]'):
        href = link.get("href", "")
        
        if not re.match(r"/cars/[A-Za-z0-9]+$", href):
            continue
        
        full_url = urljoin(BASE_URL, href)
        # Если full_url уже находится в нашей cars_by_url
        if full_url in cars_by_url:
            title_attr = link.get("title", "").strip()
            if title_attr and not cars_by_url[full_url].get("name"):
                cars_by_url[full_url]['name'] = title_attr
            continue
        
        # ============Название ====================
        name = link.get('title', '').strip() or link.get_text(" ", strip=True)
        # ================== Изображение=========
        img_url=''
        img_tag = link.find('img')
        if img_tag:
            img_url = img_tag.get("srs", "") or img_tag.get("data-src", "")
        
        # Сохраняем в бд или точнее наш словарь
        cars_by_url[full_url] = {
            "url": full_url,
            "name": name,
            "img_url": img_url,
            "price": None,
            "year_from_catalog": None
        }
        
        # ВЫтащить цену и год выпуска
        for link in soup.select('a[href*="/cars/"]'):
            href = link.get("href", '')
            if not re.match(r'^/cars/[A-Za-z0-9]+$', href):
                continue
            
            full_url = urljoin(BASE_URL, href)
            if full_url not in cars_by_url:
                continue
            
            text = link.get_text(" ", strip=True)
            print(text)

            if "сом" in text and cars_by_url[full_url]["price"] is None:
                cars_by_url[full_url]['price'] = extract_price(text)
                
            if cars_by_url[full_url]['year_from_catalog'] is None:
                cars_by_url[full_url]['year_from_catalog'] = extract_year(text)
                
            if not cars_by_url[full_url]["name"]:
                clean_text_from_years = re.sub(r'\d{4}\s*r\.?', '', text)
                clear_text_from_price = re.sub(r'~?\s[\d\s]+\s*сом', '', clean_text_from_years)
                cars_by_url[full_url]['name'] = clear_text_from_price.strip()
    return list(cars_by_url.values())
            
            
# ============ Детальный парсинг =================
def parse_car_page(html: str) -> dict:
    inner_html = extract_turbo_template(html)
    soup = BeautifulSoup(inner_html, 'lxml')
    result = {}
    
    title_tag = soup.select_one("h1.h5")
    if title_tag:
        result['full_name'] = title_tag.get_text(strip=True)
    
    price_tag = soup.select_one("div.h4 b")
    if price_tag:
        result["price"] = extract_price(price_tag.get_text())
        
    specs = {}
    dl = soup.select_one("dl.row")
    if dl:
        name_specs_list = dl.find_all("dt")
        value_specs_list = dl.find_all("dd")
        
        for name_specs, value_specs in zip(name_specs_list, value_specs_list):
            clear_name = name_specs.get_text(strip=True)
            clear_value = value_specs.get_text(strip=True)
            
            if clear_name:
                specs[clear_name] = clear_value
                
    for k, v in specs.items():
        result[f"specs_{k}"] = v
        
    if "Пробег" in specs:
        result["millage_km"] = extract_mileage(specs['Пробег'])
            
    photos_url = []
        
    for a in soup.select("a.d-block[href]"):
        href = a['href']
            
        if href.lower().endswith((".jpeg", ".jpg", ".png", ".webp")):
            photos_url.append(href)
                
    result['photos'] = " | ".join(photos_url)
    result['photos_count'] = len(photos_url)
        
        
    time_tag = soup.select_one("time[datetime]")
    if time_tag:
        result['published_at'] = time_tag["datetime"]
            
    return result
    
    
# =================   Оркестратор (главная функция) ================
def scrape_all_cars(num_pages: int) -> list[dict]:
    """
    главная функция которая проходится по всем страницам и вытаскивает нам данные по каждой машине
    """
    all_cars = []
    
    # 1 обойьти все страницы
    for page_num in range(1, num_pages+1):
        url = f"{BASE_URL}/?page={page_num}"
        
        html = fetch_html(url)
        if not html:
            print(f"Страница {page_num} пропускаем")
            continue
        page_items = parse_catalog_page(html)
        
        if not page_items:
            print("На этой страниуе нет обьявлений или не получили доступ")
            break
        all_cars.extend(page_items)
        
        time.sleep(DELAY_SEC)
        
    #2 вытащим детально данные машин
    for car in all_cars:
        html = fetch_html(car["url"])
        if html is None:
            continue
        details = parse_car_page(html)
        car.update(details)
        
        time.sleep(DELAY_SEC)
    
    return all_cars


def save_to_scv(cars, file_name):
    df = pd.DataFrame(cars)
    main_columns = [
        "url", "name", "full_name", "price", "year_from_catalog", "millage_km", "image_url", "photos", "photos_count", "published_at"
    ]
    specs_columns = sorted([
        column for column in df.columns if  column.startswith("specs_") 
    ])
    other_columns = [
        column for column in df.columns if column not in main_columns and not 
        column.startswith("specs_")
    ]
    final_columns = [column for column in main_columns if column in df.columns] + specs_columns + other_columns
    
    df = df[final_columns]
    
    df.to_csv(file_name, index=False, encoding="utf-8-sig")
    
    

if __name__ == "__main__":
    cars = scrape_all_cars(PARSE_TO_PAGE)
    save_to_scv(cars, OUTPUT_CSV)
    
    print("Конец")
    



            
            
# html = fetch_html(BASE_URL)
# clear_html = extract_turbo_template(html)
# print(parse_catalog_page(clear_html))
# html = fetch_html("https://turbo.kg/cars/O0Ka1jnm")
# print(parse_car_page(html))

