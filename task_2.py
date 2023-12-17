# list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
# list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

import logging
import sys

class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        self.logger = logging.getLogger(__name__)

    def compare_lists(self):
        try:
            matching_numbers = []
            for num in self.list1:
                if num in self.list2:
                    matching_numbers.append(num)
            if len(matching_numbers) == 0:
                print("Совпадающих чисел нет.")
            else:
                print("Совпадающие числа:", matching_numbers)
                print("Количество совпадающих чисел:", len(matching_numbers))
        except Exception as e:
            self.logger.error("Ошибка при сравнении списков:", exc_info=True)
            raise e

if __name__ == "__main__":
    # Получаем аргументы командной строки
    args = sys.argv[1:]

    # Проверяем, что передано 2 списка
    if len(args) != 2:
        print("Необходимо передать 2 списка как аргументы командной строки.")
        sys.exit(1)

    # Преобразуем аргументы в списки чисел
    try:
        list1 = [int(num) for num in args[0].split(',')]
        list2 = [int(num) for num in args[1].split(',')]
    except ValueError:
        print("Неверный формат чисел в списках.")
        sys.exit(1)

    # Создаем экземпляр LotteryGame и вызываем метод compare_lists()
    game = LotteryGame(list1, list2)
    game.compare_lists()
