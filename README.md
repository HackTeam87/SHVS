## Smart Home Voice System (SHVS)
### Обзор
Приложение Smart Home Voice System устанавливается на любую операционную систему поддерживающую Python >= 3.8 позволяет работать с устройствами через единый интерфейс - голосовой помошник. 
В нашем случае это миникомпьютер Raspberry Pi 4 Model B - четвертое поколение основной линейки.

### Поддерживаемые интерфейсы 
* WEB (открытие интернет странички голосовой командой)
* Telnet (работа с сетевыми протоколами telnet, ssh для упрощения работы сетевого инженера)
* Голосовое управление световыми приборами 


### Поддерживаемые вендоры
- [x] raspberry pi 4


### Необходимо для начала работы   
Python >= 3.8    
Модули Python :vosk, sounddevice, pyttsx3, scikit-learn, requests, pyyaml


### Подключение
pip install -r requirements.txt

### Как использовать
python3 app.py


### Разработка
#### Перечень используемых библиотек:
* Для работы приложения SHVS:
  + Vosk - это автономный набор инструментов для распознавания речи с открытым исходным кодом. Он обеспечивает распознавание речи для 20 языков и диалектов: английского, индийского английского, немецкого, французского, испанского, португальского, китайского, русского, турецкого, вьетнамского, итальянского, голландского, каталонского, арабского, греческого, фарси, филиппинского, украинского, казахского, шведского. , японский, эсперанто, хинди, чешский, польский. Еще не все. Модели Vosk небольшие (50 МБ), но обеспечивают непрерывную транскрипцию большого словаря, отклик с нулевой задержкой с потоковым API, реконфигурируемый словарь и идентификацию говорящего.
  + Sounddevice - этот модуль Python предоставляет привязки для библиотеки PortAudio и несколько удобных функций для воспроизведения и записи массивов NumPy, содержащих аудиосигналы. Модуль звукового устройства доступен для Linux, macOS и Windows.
  + Pyttsx3 - это библиотека преобразования текста в речь на Python. В отличие от альтернативных библиотек, он работает в автономном режиме и совместим как с Python 2, так и с Python 3.
  + Scikit-learn - это модуль Python для машинного обучения, созданный на основе SciPy. Простые и эффективные инструменты для прогнозного анализа данных
  + Requests — это простая, но элегантная библиотека HTTP
  + Pyyaml YAML — это формат сериализации данных, разработанный для удобочитаемости и взаимодействия с языками сценариев.
  + 
* Для Шилд реле:
  + RPi.GPIO - модуль на языке Python, который предназначен для управления каналами GPIO в мини-компьютере Raspberry Pi. Важно заметить, что данный модуль нельзя использовать в приложениях реального времени и там, где время выполнения и реакции является одним из важнейших факторов.

#### Основные файлы и каталоги
* **modules/experience.py** - содержит список функций для работы с API
* **app.py** - логика работы голосового помошника


### Работа с микрокомпьютером
### Raspberry Pi 4 Model B - это четвертое поколение основной линейки миникомпьютеров от Raspberry Pi Foundation. 
На данный момент существует три варианта комплектации, различающиеся между собой объемом оперативной памяти: 2G, 4G и 8G LPDDR4-3200 SDRAM. Сердцем данных платформ является 4х ядерный Х64-bit Cortex-A72 Broadcom ( BCM2711B0 ) ARM-v8 SoC 1.5GHz процессор. Обновления коснулись не только центрального процессора и оперативной памяти. На борту появились два USB порта 3.0, теперь в распоряжении пользователя два USB 2.0 и два USB 3.0 против четырех USB 2.0 установленных на Rpi 3 B/B+. Изменению подвергся и HDMI разъем, его сменили два micro-HDMI с поддержкой разрешения 4Kp60. Так же модуль беспроводной связи получил поддержку двух-диапазонного Wi-Fi ( стандарт IEEE 802.11ac ) с поддержкой Bluetooth 5.0. И в завершении, разъем питания USB-Type-C сменил своего предшественника micro-USB.

<img src="https://github.com/HackTeam87/SHVS/blob/main/img/relay2.jpg" width="300">      <img src="https://github.com/HackTeam87/SHVS/blob/main/img/relay1.jpg" width="450">
#### Основные конструктивные отличия от предыдущих моделей:
- [x] Увеличенный объём оперативной памяти до 4ГБайт
- [x] Металлическая крышка, закрывающая модуль беспроводной передачи данных
- [x] Металлический радиатор на процессоре для улучшенной теплоотдачи
- [x] Увеличенный объём оперативной памяти
- [x] 4-пиновый разъем для подключения дополнительного PoE модуля
- [x] Два USB 3.0 разъёма
- [x] Два micro-HDMI разъёма выдеовыхода
- [x] Разъём питания USB-C

### Распиновка GPIO разъема  Raspberry Pi 4 Model B:
<img src="https://github.com/HackTeam87/SHVS/blob/main/img/Raspberry-Pi-3B-Model-B-Plus-pin-headers.jpg" width="800"> 








<img src="https://github.com/HackTeam87/SHVS/blob/main/img/RPi-Relay-Board-intro.jpg" width="300">      <img src="https://github.com/HackTeam87/SHVS/blob/main/img/RPi-Relay-Board-4.gif" width="450">
### Шилд реле для Raspberry Pi
позволяет программно управлять мощной нагрузкой из пользовательской программы на Raspberry. На плате установлены три реле с максимальным током коммутации до 10А и напряжением до 250В. 
Для индикации состояния статуса реле в модуле предусмотрены светодиоды.
### Особенности шилда реле:
- [x] Совместимость со всеми моделями Raspberry Pi
- [x] Качественные реле с коммутацией нагрузки 250VAC/5A, 30VDC/5A
- [x] Оптоизоляция для обеспечения качественной высоковольтной изоляции
- [x] Встроенные индикаторы состояния реле
- [x] Перемычки управления реле с возможностью подключения внешнего сигнала управления
- [x] Поддержка средствами разработки в wiringPi, WebioPi, shell, python и bcm2835




#### Используемые источники
* Для написание приложения 
  + https://www.youtube.com/watch?v=ZZVWae8E9K0&ab_channel=PythonToday
* Для Шилд реле:
  + https://www.waveshare.com/wiki/RPi_Relay_Board
  + https://arduino.ua/ru/prod2535-shild-3-h-rele-dlya-raspberry-pi
  + https://ph0en1x.net/106-rpi-gpio-installation-working-with-inputs-outputs-interrupts.html

