import time
import threading
import multiprocessing
import random

NUM_WORKERS = 10
size = 1000000  # reduced to avoid memory explosion

def do_something(count, out_list):
    temp = []
    for _ in range(count):
        temp.append(random.random())
    out_list.extend(temp)

# ------------------ SERIAL ------------------
out_list = []
start_time = time.time()

for _ in range(NUM_WORKERS):
    do_something(size, out_list)

end_time = time.time()
print("Serial time =", end_time - start_time)


# ------------------ MULTITHREADING ------------------
out_list = []
start_time = time.time()

jobs = []
for _ in range(NUM_WORKERS):
    thread = threading.Thread(target=do_something, args=(size, out_list))
    jobs.append(thread)

for j in jobs:
    j.start()

for j in jobs:
    j.join()

end_time = time.time()
print("Threading time =", end_time - start_time)


# ------------------ MULTIPROCESSING ------------------
def worker(count, queue):
    temp = []
    for _ in range(count):
        temp.append(random.random())
    queue.put(temp)

if __name__ == "__main__":
    start_time = time.time()

    jobs = []
    queue = multiprocessing.Queue()

    for _ in range(NUM_WORKERS):
        process = multiprocessing.Process(target=worker, args=(size, queue))
        jobs.append(process)

    for j in jobs:
        j.start()

    results = []
    for _ in range(NUM_WORKERS):
        results.extend(queue.get())

    for j in jobs:
        j.join()

    end_time = time.time()
    print("Processing time =", end_time - start_time)