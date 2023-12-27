from datetime import datetime, timedelta


BUSY_INTERVALS = [
    {'start' : '10:30', 'stop' : '10:50'},
    {'start' : '18:40', 'stop' : '18:50'},
    {'start' : '14:40', 'stop' : '15:50'},
    {'start' : '16:40', 'stop' : '17:20'},
    {'start' : '20:05', 'stop' : '20:20'}
]
WORK_START = '09:00'
WORK_END = '21:00'
MINUTE_WINDOW_SIZE = 30
SECONDS_IN_MINUTE = 60
RUSULT_MESSAGE = 'Свободное окно с {start} до {stop}'
TIME_FORMATTER = '%H:%M'


def convert_busy_intervals(busy_intervals):

    """Конвертирование временных интервалов из формата строки
    в формат datetime.
    """

    return list(
        map(
            lambda interval: {
                'start': datetime.strptime(interval['start'], '%H:%M'),
                'stop': datetime.strptime(interval['stop'], '%H:%M')
            }, busy_intervals
        )
    )


def generate_free_windows():

    """Генерация свободных окон в заданном временном диапазоне."""

    pass


def generate_time_range():

    """Генерация интервалов с шагом window_size в заданном временном 
    диапазоне.
    """

    pass


def is_time_in_busy_intervals():

    """Проверяет, находится ли текущее время в занятых временных интервалах."""

    pass


def get_reception_windows(
    *,
    busy_intervals,
    work_start,
    work_end,
    window_size
):

    """Получение свободных окон в заданном временном диапазоне."""

    work_start_convert_dt = datetime.strptime(work_start, '%H:%M')
    work_end_convert_dt = datetime.strptime(work_end, '%H:%M')
    busy_intervals_convert_dt = [
        (
            datetime.strptime(interval['start'], TIME_FORMATTER),
            datetime.strptime(interval['stop'], TIME_FORMATTER)
        ) for interval in busy_intervals
    ]
    free_windows_list = [
        {
            'start': current_time.strftime(TIME_FORMATTER),
            'stop': (
                current_time + timedelta(
                    minutes=window_size
                )).strftime(TIME_FORMATTER)
        }
        for current_time in (
            work_start_convert_dt + timedelta(minutes=i)
            for i in range(
                0,
                (
                    work_end_convert_dt -
                    work_start_convert_dt
                ).seconds // SECONDS_IN_MINUTE,
                window_size
            )
        ) if not any(
            start <= current_time < stop
            or current_time <= start < current_time + timedelta(
                minutes=window_size
            )
            for start, stop in busy_intervals_convert_dt
        )
    ]

    return free_windows_list


if __name__ == '__main__':
    free_window_list = get_reception_windows(
        busy_intervals=BUSY_INTERVALS,
        work_start=WORK_START,
        work_end=WORK_END,
        window_size=MINUTE_WINDOW_SIZE
    )
    for window in free_window_list:
        print(
            RUSULT_MESSAGE.format(
                start=window['start'],
                stop=window['stop']
            )
        )
    
    # Проверка функции конвертирования времненных интервалов
    # в формат datetime
    assert all(
        isinstance(i['start'], datetime) and
        isinstance(i['stop'], datetime) 
        for i in convert_busy_intervals(BUSY_INTERVALS)
    )

