import os
from multiprocessing import Array, Process, Value


def square_numbers():
    for i in range(100):
        print(i * i)


if __name__ == "__main__":
    processes = []

    num_process = os.cpu_count()

    for i in range(num_process):
        process = Process(target=square_numbers)
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()
