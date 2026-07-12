import os
from multiprocessing import Array, Lock, Process, Value
from time import sleep


def add_100(number, lock):
    for i in range(100):
        sleep(0.01)
        with lock:
            number.value += 1


if __name__ == "__main__":
    shared_number = Value("i", 0)
    # 'i' --> DataType as String
    # 0 --> Start Value

    lock = Lock()

    print(f"Number at begining {shared_number.value}")

    p1 = Process(target=add_100, args=[shared_number, lock])
    p2 = Process(target=add_100, args=[shared_number, lock])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Number at the end {shared_number.value}")
