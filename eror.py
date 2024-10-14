import threading
# from threading import Thread
import time

# def sone_func():
#     time.sleep(5)
#     raise Exception
#
# def tread_func():
#     try:
#         sone_func()
#     except Exception as e:
#         print("Привет я тут")
#
# t1 = threading.Thread(target=tread_func)
# t2 = threading.Thread(target=tread_func)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# def sone_func():
#     time.sleep(2)
#     raise Exception
# def excepthook(args):
#     print(args.thread.is_ alive)
#     print(args.thread.name)
#
# threading.excepthook = excepthook
#
# t1 = threading.Thread(target=sone_func)
# t2 = threading.Thread(target=sone_func)
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()

def producer(gueue): # gueue очередь
    while True:
        msg = "ping"
        gueue.put(msg) # put создает очередь
        time.sleep(1)

def worker(gueue):
    while True:
