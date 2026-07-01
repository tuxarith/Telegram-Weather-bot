# Telegram Weather Bot

## Ru (Русский)
Бот позволяет узнать погоду в Telegram. Отправляешь команду и название города — бот через внешний погодный API получает данные и отправляет результат в чат.
### Данный открытый код был сделан и опубликован из моего бота - @Weather1tuxBot
## Как пользоваться
1. Открой бота в Telegram.
2. Запусти командой: `/start`
3. Чтобы узнать погоду, используй: `/weather <город>`
   - пример: `/weather Moscow`


## Команды
- `/start` — запустить бота
- `/info` — информация о боте
- `/commands` — показывает команды для бота
- `/weather <город>` — показывает погоду в указанном городе

## Установка и запуск
сначала скопируй проект через git clone https://github.com/tuxarith/Telegram-Weather-bot.git
после чего зайди в директорию - cd Telegram-Weather-bot

### 1) Установи зависимости
В корне проекта:
```bash
pip install -r requirements.txt
```
### 2) Создай переменные окружения

Создай файлы в корне проекта:
```bash
bot_token.env
```
Пропиши в нем:
```bash
TOKEN=ваш_телеграм_бот_токен
```

Токен можно получить у @BotFather.

Далее создай:
```bash
apiweather.env
```
И пропиши в ней:
```bash
API=ваш_api_ключ_openweathermap
```
Ключ можно получить на openweathermap.org/api

### 3) Запусти бота
```bash
python main.py
```

## Eng (English)
### Bot lets you find out weather in Telegram. Send Command and name city - bot from external weather API get data and send this result in chat.
### And sorry by my english, im just learning it from the start.
### The open source from my bot - @Weather1tuxBot
### Bot messages, you can edit them yourself 

## How to use:
1. Open bot in Telegram.
2. to start command: `/start`
3. to find out, use: `/weather <city>`
     - Example: `/weather Moscow`
   
## Commands
 - `/start` - start the bot
 - `/info` - info of bot
 - `/commands` - shows commands for bot
 - `/weather` - shows weather in specfiled city

## Install and Start
First Copy project:
```bash
git clone https://github.com/tuxarith/Telegram-Weather-bot.git
```

Then open the Directory:
```bash
cd Telegram-Weather-bot
```

### 1) Install requirements

In root project:
```bash
pip install -r requirements.txt
```
### 2) Create environment variables
Create file in root project:
```bash
bot_token.env
```
And write it in:
```bash
TOKEN = your_telegram_bot_token
```
Token you can get @BotFather

next create:
```bash
apiweather.env
```
and write in her:
```bash
API = your_api_openweathermap
```
You can get api at the link openweathermap.org/api

### 3) Start the bot

```bash
python main.py
```
