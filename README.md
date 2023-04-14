# SHVS
### smart home voice system

## Обзор
Библиотека позволяет работать с устройствами через единый интерфейс - голосовой помошник. 

<img src="https://github.com/HackTeam87/SHVS/blob/main/img/relay2.jpg" width="55">

### Поддерживаемые интерфейсы 
* WEB
* Telnet
* SSH 


### Поддерживаемые вендоры
- [x] raspberry pi 4


### Необходимо для начала работы   
Python >= 3.8    
Модули Python :vosk, sounddevice, pyttsx3, scikit-learn, requests, pyyaml


### Подключение к вашему проекту
pip install -r requirements.txt

### Как использовать
python3 app.py

### Разработка
#### Основные файлы и каталоги
* **modules/experience.py** - содержит список функций для работы с API
* **app.py** - логика работы голосового помошника

