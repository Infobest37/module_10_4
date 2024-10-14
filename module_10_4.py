import random
import time
from threading import Thread
from queue import Queue


# Класс Table
class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None  # Гость, который сидит за столом (по умолчанию None)


# Класс Guest (наследуется от Thread)
class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name  # Имя гостя

    def run(self):
        # Имитация времени, которое гость тратит на еду (от 3 до 10 секунд)
        time_to_eat = random.randint(3, 10)
        time.sleep(time_to_eat)


# Класс Cafe
class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)  # Столы в кафе
        self.queue = Queue()  # Очередь гостей

    # Метод прибытия гостей
    def guest_arrival(self, *guests):
        for guest in guests:
            # Ищем свободный стол
            free_table = next((table for table in self.tables if table.guest is None), None)

            if free_table:  # Если есть свободный стол
                free_table.guest = guest  # Сажаем гостя за стол
                guest.start()  # Запускаем поток (гость начинает есть)
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:  # Если свободных столов нет
                self.queue.put(guest)  # Гость в очереди
                print(f"{guest.name} в очереди")

    # Метод обслуживания гостей
    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():  # Проверяем, покушал ли гость
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    # Если очередь не пуста, сажаем гостя из очереди за стол
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()  # Запускаем поток (гость начинает есть)
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(1)  # Небольшая задержка для имитации времени между проверками


# Тестирование программы
if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Viktoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]

    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    # Создание кафе с 5 столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()
