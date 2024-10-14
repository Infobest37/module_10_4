

'''
Приимер работы гила GIL (Global Interpreter Lock)
'''
# from threading import Thread
#
#
# def count_up(name, n):
#     for i in range(n):
#         print(name, i, sep = ": " ) # sep - это разделитель который должен стоять через двое точие
#
# t1 = Thread(target=count_up, args=("T1", 100))
# t2 = Thread(target=count_up, args=("T2", 100))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

