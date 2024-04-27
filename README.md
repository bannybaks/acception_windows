# Acceptance windows

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)

## <span style="color:#D2691E">Description:</span>
*Functional*:<br>
- Creation of free windows for doctor’s appointments.<br>

*Input data*:<br>
- List of busy doctor time slots:<br>

```python
[
     {'start' : '10:30', 'stop' : '10:50'},
     {'start' : '18:40', 'stop' : '18:50'},
     {'start' : '14:40', 'stop' : '15:50'},
     {'start' : '16:40', 'stop' : '17:20'},
     {'start' : '20:05', 'stop' : '20:20'}
]
```

*Imprint*:<br>
- Messages in the terminal indicating the boundaries of free windows in the format:<br>
```bash
Free window from [window start time] to [window end time]
```

## <span style="color:#D2691E">Usage:</span>
1. Clone the repository:

     ```bash
     git clone git@github.com:bannybaks/acception_windows.git
     ```

2. Go to the project root:
    
     ```bash
     cd acceptance_windows
     ```

3. Run the code from the current directory:

     ```bash
     python main.py
     ```
<br/>

Developer: **Pavel Smirnov**

[![Telegram Badge](https://img.shields.io/badge/-B1kas-blue?style=social&logo=telegram&link=https://t.me/B1kas)](https://t.me/B1kas)
[![Yamail Badge](https://img.shields.io/badge/baksbannysmirnov@yandex.ru-FFCC00?style=flat&logo=ycombinator&logoColor=red&link=mailto:baksbannysmirnov@yandex.ru)](mailto:baksbannysmirnov@yandex.ru)
