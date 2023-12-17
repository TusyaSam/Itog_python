import time
import logging
from datetime import datetime
import sys

class MyStr(str):


    """
    Класс для создания строки с информацией об авторе и времени создания.

    Атрибуты:
    value (str): строковое значение.
    author (str): имя автора.
    time (float): время создания.

    Dunder методы:
    new(cls, value, author): создает новый объект класса.
    str(): возвращает строковое представление объекта класса.
    repr(): возвращает строковое представление объекта класса для отладки.

    """

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        formatted_time = datetime.fromtimestamp(self.time).strftime('%Y-%m-%d %H:%M')
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {formatted_time})"

    def __repr__(self):
        return f"MyStr('{super().__str__()}', '{self.author}')"

def main():
    # Включаем логирование
    logging.basicConfig(filename='log.txt', level=logging.ERROR)
    logger = logging.getLogger(__name__)

    try:
        # Получаем параметры из командной строки
        value = sys.argv[1]
        author = sys.argv[2]

        # Создаем объект MyStr
        mystr = MyStr(value, author)

        # Выводим на экран
        print(mystr)

    except IndexError:
        logger.error("Не переданы все необходимые параметры")
    
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    main()