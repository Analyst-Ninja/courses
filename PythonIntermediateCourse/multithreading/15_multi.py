# # ------------------- Multiprocessing ----------------------

# from multiprocessing import Process
# import os
# import time

# def square_numbers():
#     prodList = []
#     for i in range(100):
#         prodList.append(i * i)
#         time.sleep(.1)
#     return prodList

# processes = []
# num_process = os.cpu_count()

# # Create Processes
# for i in range(num_process):
#     p = Process(target=square_numbers)
#     processes.append(p)

# # Start Processes
# for p in processes:
#     p.start()

# # Join the processes
# for p in processes:
#     p.join()

# print('End Main')

# ------------------- Multithreading ----------------------

import os
import time
from threading import Thread


def square_numbers():
    prodList = []
    for i in range(100):
        prodList.append(i * i)
        time.sleep(0.1)
    return prodList


threads = []
num_threads = 10

# Create Processes
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# Start Threads
for t in threads:
    t.start()

# Join the threads
for t in threads:
    t.join()

print("End Main")
