#MultiThreading
import time


start_time = time.time()
jobs = []

for i in range(0, NUM_WORKERS):
    thread = threading.Thread(target=do_something,
                              args=(size, out_list))
    jobs.append(thread)

for j in jobs:
    j.start()

for j in jobs:
    j.join()

print("List processing complete.")
end_time = time.time()
print("threading time=", end_time - start_time)