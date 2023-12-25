#  Acception windows

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)

##  <span style="color:#D2691E">Описание:</span>
*Функционал*:<br>
	- Формирование свободных окон для приёма у врача.<br>		 	

*Входные данные*:<br>
	- Список занятых интервалов времени врача:<br>

```python
[
    {'start' : '10:30', 'stop' : '10:50'},
    {'start' : '18:40', 'stop' : '18:50'},
    {'start' : '14:40', 'stop' : '15:50'},
    {'start' : '16:40', 'stop' : '17:20'},
    {'start' : '20:05', 'stop' : '20:20'}
]
```

*Выходные данные*:<br>
	- Сообщения в терминале с указанием границ свободных окон в формате:<br>
```bash
Свободное окно с [время начала окна] до [время окончания окна]
```

## <span style="color:#D2691E">Использование:</span>
1. Склонируйте репозиторий:

    ```bash
    git clone git@github.com:bannybaks/acception_windows.git
    ```

2. Перейти в корень проекта:
    
    ```bash
    cd acception_windows
    ```

3. Запустить код из текущий дирректории:

    ```bash
    python main.py
    ```
<br/>

Разработчик: **Павел Смирнов**

[![Telegram Badge](https://img.shields.io/badge/-B1kas-blue?style=social&logo=telegram&link=https://t.me/B1kas)](https://t.me/B1kas) [![Yamail Badge](https://img.shields.io/badge/baksbannysmirnov@yandex.ru-FFCC00?style=flat&logo=ycombinator&logoColor=red&link=mailto:baksbannysmirnov@yandex.ru)](mailto:baksbannysmirnov@yandex.ru)
