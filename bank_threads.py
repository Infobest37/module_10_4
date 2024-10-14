import datetime
import json
from random import randint
from threading import Thread

res = []
treads = []
files = ["file.json", "file1.json", "file2.json", "file3.json", "file4.json", "file5.json"]

def worked(file):
    with open(file, "r") as f:
        js = json.load(f)
        res.extend(js)

def main():
    start = datetime.datetime.now()

    for i in range(len(files)):
        t = Thread(target=worked, args=(files[i],))
        t.start()
        treads.append(t)

    for i in treads:
        i.join()

    end = datetime.datetime.now()

    print(sum(res))  # Выводим сумму значений
    return end - start  # Возвращаем разницу времени выполнения

time_calk = []

# Запуск 100 итераций
for i in range(100):
    res = []
    time_calk.append(main())  # Добавляем разницу времени выполнения в список

# Рассчитываем среднее значение времени выполнения
average_time = sum([calc.microseconds for calc in time_calk]) / len(time_calk)

# Вывод среднего времени выполнения
print(f"Среднее время выполнения (микросекунды): {average_time}")
