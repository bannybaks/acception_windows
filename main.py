from datetime import datetime, timedelta
from typing import List, Dict


BUSY_TIME_START = ('10:30', '18:40', '14:40', '16:40', '20:05')
BUSY_TIME_STOP = ('10:50', '18:50', '15:50', '17:20', '20:20')
BUSY_INTERVALS_PACK = [
    dict(start=start_time, stop=stop_time) 
    for start_time, stop_time in zip(BUSY_TIME_START, BUSY_TIME_STOP)
]
WORK_START = '09:00'
WORK_END = '21:00'
MINUTE_WINDOW_SIZE = 30
SECONDS_IN_MINUTE = 60
RUSULT_MESSAGE = 'Свободное окно с {start} до {stop}'
TIME_FORMATTER = '%H:%M'


def convert_busy_intervals(
    busy_intervals: List[Dict[str, str]]
) -> List[tuple[datetime, datetime]]:

    """Конвертирование занятых временных интервалов из формата строки
    в формат datetime.

    Args:
        busy_intervals (List[Dict[str, str]]):
            Список временных интервалов.
    
    Returns:
        List[tuple[datetime, datetime]]:
            Список временных интервалов в виде объектов datetime
    """

    return list(
        map(
            lambda interval: (
                datetime.strptime(interval['start'], '%H:%M'),
                datetime.strptime(interval['stop'], '%H:%M')
            ), busy_intervals
        )
    )


def generate_free_windows(
    work_start: datetime,
    work_end: datetime,
    window_size: int,
    busy_intervals_convert_dt: List[tuple[datetime, datetime]]
) -> List[Dict[str, str]]:

    """Генерация свободных окон в заданном временном диапазоне.
    
    Args:
        work_start (datetime):
            Время начала рабочего дня.
        work_end (datetime):
            Время окончания рабочего дня.
        window_size (int):
            Длительность свободных окон в минутах.
        busy_intervals_convert_dt (List[tuple[datetime, datetime]]):
            Занятые временные интервалы.
    
    Returns:
        List[Dict[str, str]]:
            Список свободных окон с указанием временных границ.
    """

    return [
        dict(
            start=current_time.strftime(TIME_FORMATTER),
            stop=(
                current_time + timedelta(
                    minutes=window_size
                )
            ).strftime(TIME_FORMATTER)
        ) for current_time in generate_time_range(
            work_start, work_end, window_size
        ) if not is_time_in_busy_intervals(
            current_time, busy_intervals_convert_dt, window_size
        )
    ]


def generate_time_range(
    time_work_start: datetime,
    time_work_end: datetime,
    duration_window: int
) -> List[datetime]:

    """Генерация интервалов с шагом window_size в заданном временном 
    диапазоне.

    Args:
        time_work_start (datettime):
            начальное время в диапазоне.
        time_work_end (datetime):
            Конечное время в диапазоне.
        duration_window (int):
            Шаг в минутах до следующего интервала.
    
    Returns:
        List[datetime]:
            Список с интервалами в пределах всего рабочего дня с шагом
            duration_window.
    """

    return [
        time_work_start + timedelta(minutes=i) for i in range(
            0,
            (time_work_end - time_work_start).seconds // SECONDS_IN_MINUTE,
            duration_window
        )
    ]


def is_time_in_busy_intervals(
    current_time,
    busy_intervals_convert_dt,
    window_size
):

    """Проверяет, находится ли текущее время в занятых временных интервалах."""
    
    return any(
        start <= current_time < stop
        or current_time <= start < current_time + timedelta(
            minutes=window_size
        ) for start, stop in busy_intervals_convert_dt
    )


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
        busy_intervals=BUSY_INTERVALS_PACK,
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
        all(isinstance(item, datetime) for item in in_tuple)
        for in_tuple in convert_busy_intervals(BUSY_INTERVALS_PACK)
    )

    # Проверка функции генерации 24 окон по 30 минут в промежутке
    # с 09:00 до 21:00
    result_generate_intervals = generate_time_range(
        datetime.strptime(WORK_START, TIME_FORMATTER),
        datetime.strptime(WORK_END, TIME_FORMATTER),
        MINUTE_WINDOW_SIZE
    )
    expected_count_intervals = (
        datetime.strptime(
            WORK_END, TIME_FORMATTER
        ) - datetime.strptime(WORK_START, TIME_FORMATTER)
    ).seconds // (SECONDS_IN_MINUTE * MINUTE_WINDOW_SIZE)

    assert len(result_generate_intervals) == expected_count_intervals, (
        f'Ожидаемое количество временных окон: {expected_count_intervals}. '
        f'Фактическое количество: {len(result_generate_intervals)}'
    )

    # Проверка функции генерации только свободных окон в промежутке
    # с 09:00 до 21:00 
    result_free_windows = generate_free_windows(
        datetime.strptime(WORK_START, TIME_FORMATTER),
        datetime.strptime(WORK_END, TIME_FORMATTER),
        MINUTE_WINDOW_SIZE,
        convert_busy_intervals(BUSY_INTERVALS_PACK)
    )
    for window in result_free_windows:
        start_time = datetime.strptime(window['start'], TIME_FORMATTER)
        stop_time = datetime.strptime(window['stop'], TIME_FORMATTER)
        work_start = datetime.strptime(WORK_START, TIME_FORMATTER)
        work_end = datetime.strptime(WORK_END, TIME_FORMATTER)

        assert work_start <= start_time <= work_end
        assert work_start <= stop_time <= work_end


        assert not all(
            start <= start_time < stop or start <= stop_time < stop
            for start, stop in convert_busy_intervals(BUSY_INTERVALS_PACK)
        )