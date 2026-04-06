# Telegram Бот для расчёта курса валют и CASE-системы

Этот Telegram-бот предоставляет два основных функциональных модуля:

1. **Курс валют** — парсинг актуальных курсов с сайта [РБК](https://www.rbc.ru/) и отображение их в удобном формате.
2. **CASE-система** — последовательное применение трёх математических функций (√x, 1/x, e^x) к введённому числу.

Бот написан на Python с использованием библиотеки `aiogram` (v3.x) и поддерживает работу через прокси-сервер.

---

## 📁 Структура проекта
```text
project/
├── bot.py # Точка входа, запуск бота
├── config.py # Файл конфигурации (токен, прокси)
├── requirements.txt # Зависимости проекта
├── README.md # Документация
│
├── app/ # Основная логика бота
│ ├── handlers.py # Обработчики команд и callback-запросов
│ ├── keyboards.py # Генерация клавиатур (Reply и Inline)
│ │
│ ├── parsing/ # Модуль парсинга валют
│ │ └── parser.py # Парсинг, загрузка, сохранение данных
│ │
│ └── case/ # Модуль CASE-системы
│   ├── init.py # Инициализация модуля
│   └── state.py # Логика функций, FSM состояния
│
└── exports/ # Хранилище данных
    └── master.json # JSON-файл с курсами валют
```


---

## 🚀 Установка и запуск

### 1. Клонирование проекта

```bash
git clone <url-вашего-репозитория>
cd project
```
2. Создание виртуального окружения
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Установка зависимостей
```bash
pip install -r requirements.txt
```

4. Настройка config.py
Создайте в корне проекта файл config.py и добавьте:

```python
TOKEN = "ВАШ_ТОКЕН_БОТА"
PROXY_URL = "socks5://ваш_прокси:порт"   # Если прокси не нужен, оставьте пустую строку(Прикси модно взять с репозитория [)](https://github.com/databay-labs/free-proxy-list/blob/master/socks5.txt)
```
5. Запуск бота
```python
python bot.py
```
Вы увидите сообщение:
```text
Запускаем бота...
Бот успешно запущен: @your_bot_username
Бот готов к работе!
```
🧪 Использование
Курс валют
Нажмите «Курс валют»

Выберите валюту из списка

Для обновления данных — кнопка «Обновить»

CASE-система
Нажмите «CASE-система»

Последовательно выберите три функции (√x, 1/x, e^x)

Введите число x

Бот вычислит:
y = F₁( F₂( F₃( x ) ) )

⚙️ Требования
Python 3.9+

Доступ в интернет (для работы с Telegram API и парсинга)

📦 Зависимости (requirements.txt)
```text
aiogram==3.4.1
beautifulsoup4==4.12.3
requests==2.31.0
aiohttp==3.9.3
```

🧰 Краткая инструкция по запуску 
Если вы впервые запускаете проект:
```bash
# 1. Скачайте проект
git clone https://github.com/Amongassik/laba_bots
cd project

# 2. Создайте виртуальное окружение
python -m venv venv

# 3. Активируйте его
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Установите библиотеки
pip install -r requirements.txt

# 5. Создайте config.py с токеном бота
echo TOKEN=\"123456:ABC-DEF\" > config.py
echo PROXY_URL=\"\" >> config.py

# 6. Запустите бота
python bot.py
```