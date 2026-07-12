from queue import Queue
from threading import Lock, Thread, current_thread
from time import sleep


def worker(q, lock):
    while True:
        value = q.get()
        # processing
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()


if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10

    for _ in range(num_threads):
        thread = Thread(target=worker, args=[q, lock])
        thread.daemon = True
        thread.start()

    for i in range(20):
        q.put(i)

    q.join()

    # q.put(1)
    # q.put(2)
    # q.put(3)
    # q.put(4)

    # # 4 3 2 1 -->

    # first = q.get()
    # print(first)
