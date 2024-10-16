import random
import time
from asyncio import Queue
from threading import Thread


class Table:

    def __init__(self, *table):
        self.guest = None
        self.table = table

class Guest(Thread):
    def __init__(self, name: str):
        Thread.__init__(self)
        self.name = name

    def run(self):
       food_eat = random.randint(1, 6)
       time.sleep(food_eat)

class Cafe():
    def __init__(self, *tables):
        self.tables = list(tables)
        self.gueue = Queue()



    gueue = 9
    def guest_arrival(self,*guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None) # это функция, которая
            # возвращает следующий элемент из генератора (в данном случае, первый найденный свободный стол). Если
            # генератор не находит ни одного подходящего стола (например, все столы заняты), функция next() вернёт значение по умолчанию — None.

            if free_table:  # Если есть свободный стол
                free_table.guest = guest  # Сажаем гостя за стол
                guest.start()  # Запускаем поток (гость начинает есть)
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:  # Если свободных столов нет
                self.queue.put(guest)  # Гость в очереди
                print(f"{guest.name} в очереди")

'''None здесь используется для того, чтобы программа знала, что свободных столов нет и дальше могла обработать этот 
случай, например, поставить гостя в очередь.'''


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