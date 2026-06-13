# Chapter 2: Thread-Based Parallelism

## 2.1 What is a Thread?

A thread is an independent execution flow that can be executed in parallel and concurrently with other threads in the system.

**Thread Components:**
- Program counters
- Registers
- Stack

**Thread States:**

```
                    ┌─────────────────────────────────────┐
                    │                                     │
                    ▼                                     │
    [*] ──→ Ready ──→ Running ──→ [*]
              ↑          │
              │          │
              │          ▼
              └────── Blocked
```

**State Transitions:**

| Transition | Description |
|------------|-------------|
| Ready → Running | Thread is scheduled for execution |
| Running → Ready | Thread is preempted or times out |
| Running → Blocked | Thread waits for resource/event |
| Blocked → Ready | Resource/event becomes available |

**Thread Life Cycle:**

```
Create Thread → Ready → Scheduled → Running → Terminated
                              │
                              ▼
                          Blocked (Wait)
                              │
                              ▼
                          Ready (Resumed)
```

**Key Characteristics:**
- Multiple threads share data and resources within same process
- Threads have their own execution state
- Threads can be synchronized with other threads
- Context switch between threads is lighter than between processes

---

## 2.2 Python Threading Module

The `threading` module provides thread management capabilities:

**Major Components:**

```
threading Module
├── Thread object
├── Lock object
├── RLock object
├── Semaphore object
├── Condition object
├── Event object
└── Barrier object
```

### 2.2.1 Thread Class Parameters

```python
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={})
```

| Parameter | Description |
|-----------|-------------|
| group | Should be None (reserved for future) |
| target | Function to execute when thread starts |
| name | Thread name (default: Thread-N) |
| args | Tuple of arguments passed to target |
| kwargs | Dictionary of keyword arguments |

---

## 2.3 Defining a Thread

### Basic Thread Creation

```python
import threading

def my_func(thread_number):
    print(f'my_func called by thread {thread_number}')

def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()
```

**Output:**
```
my_func called by thread N0
my_func called by thread N1
my_func called by thread N2
my_func called by thread N3
my_func called by thread N4
my_func called by thread N5
my_func called by thread N6
my_func called by thread N7
my_func called by thread N8
my_func called by thread N9
```

**Key Points:**
- `start()` method begins thread execution (non-blocking)
- `join()` method waits for thread to complete (blocking)

---

## 2.4 Determining the Current Thread

```python
import threading
import time

def function_A():
    print(threading.current_thread().getName() + ' ---> starting')
    time.sleep(2)
    print(threading.current_thread().getName() + ' ---> exiting')

def function_B():
    print(threading.current_thread().getName() + ' ---> starting')
    time.sleep(2)
    print(threading.current_thread().getName() + ' ---> exiting')

def function_C():
    print(threading.current_thread().getName() + ' ---> starting')
    time.sleep(2)
    print(threading.current_thread().getName() + ' ---> exiting')

if __name__ == "__main__":
    t1 = threading.Thread(name='function_A', target=function_A)
    t2 = threading.Thread(name='function_B', target=function_B)
    t3 = threading.Thread(name='function_C', target=function_C)
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
```

**Output (order may vary):**
```
function_A ---> starting
function_B ---> starting
function_C ---> starting
function_A ---> exiting
function_B ---> exiting
function_C ---> exiting
```

**Methods for Current Thread:**
- `threading.current_thread().getName()` - Returns name of current thread
- `threading.current_thread().name` - Property access to thread name

---

## 2.5 Defining a Thread Subclass

```python
import time
import os
from random import randint
from threading import Thread

class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
    
    def run(self):
        print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
        time.sleep(self.duration)
        print(f"---> {self.name} over")

def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = MyThreadClass("Thread#1", randint(1,10))
    thread2 = MyThreadClass("Thread#2", randint(1,10))
    thread3 = MyThreadClass("Thread#3", randint(1,10))
    thread4 = MyThreadClass("Thread#4", randint(1,10))
    thread5 = MyThreadClass("Thread#5", randint(1,10))
    thread6 = MyThreadClass("Thread#6", randint(1,10))
    thread7 = MyThreadClass("Thread#7", randint(1,10))
    thread8 = MyThreadClass("Thread#8", randint(1,10))
    thread9 = MyThreadClass("Thread#9", randint(1,10))
    
    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    
    # Thread Joining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    
    print("End")
    print(f"--- {time.time() - start_time} seconds ---")

if __name__ == "__main__":
    main()
```

**Key Points about Subclassing:**
- Override `__init__` method to add parameters
- Override `run` method with thread logic
- Call parent `Thread.__init__()` in constructor
- `start()` method calls `run()` internally

---

## 2.6 Thread Synchronization with Lock

**Lock Mechanism:**

```
Thread 1 ──→ acquire() ──┐
                         │
Thread 2 ──→ acquire() ──┼── Lock Available? ──→ Critical Section ──→ release()
                         │
Thread 3 ──→ acquire() ──┘
                              │
                              ▼
                         Block/Wait
```

### Lock Example

```python
import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
    
    def run(self):
        # Acquire the Lock
        threadLock.acquire()
        print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
        time.sleep(self.duration)
        print(f"---> {self.name} over")
        # Release the Lock
        threadLock.release()

def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = MyThreadClass("Thread#1", randint(1,10))
    thread2 = MyThreadClass("Thread#2", randint(1,10))
    thread3 = MyThreadClass("Thread#3", randint(1,10))
    thread4 = MyThreadClass("Thread#4", randint(1,10))
    thread5 = MyThreadClass("Thread#5", randint(1,10))
    thread6 = MyThreadClass("Thread#6", randint(1,10))
    thread7 = MyThreadClass("Thread#7", randint(1,10))
    thread8 = MyThreadClass("Thread#8", randint(1,10))
    thread9 = MyThreadClass("Thread#9", randint(1,10))
    
    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    
    # Thread Joining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    
    print("End")
    print(f"--- {time.time() - start_time} seconds ---")

if __name__ == "__main__":
    main()
```

**Output (Sequential Execution):**
```
---> Thread#1 running, belonging to process ID 10632
---> Thread#1 over
---> Thread#2 running, belonging to process ID 10632
---> Thread#2 over
---> Thread#3 running, belonging to process ID 10632
---> Thread#3 over
... (continues sequentially)
```

**Lock Methods:**

| Method | Description |
|--------|-------------|
| `acquire()` | Acquires the lock (blocks if not available) |
| `acquire(False)` | Non-blocking, returns True/False |
| `release()` | Releases the lock |

---

## 2.7 Thread Synchronization with RLock (Reentrant Lock)

**RLock Characteristics:**
- Can be acquired multiple times by the same thread
- Must be released same number of times
- Only the owning thread can release it

### RLock Example

```python
import threading
import time
import random

class Box:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0
    
    def add(self):
        with self.lock:
            self.total_items += 1
    
    def remove(self):
        with self.lock:
            self.total_items -= 1
    
    def execute(self, value):
        with self.lock:
            self.total_items += value

def adder(box, items):
    print(f"N° {items} items to ADD")
    while items:
        box.add()
        time.sleep(1)
        items -= 1
        print(f"ADDED one item --> {items} items to ADD")

def remover(box, items):
    print(f"N° {items} items to REMOVE")
    while items:
        box.remove()
        time.sleep(1)
        items -= 1
        print(f"REMOVED one item --> {items} items to REMOVE")

def main():
    items = 10
    box = Box()
    t1 = threading.Thread(target=adder, args=(box, random.randint(10,20)))
    t2 = threading.Thread(target=remover, args=(box, random.randint(1,10)))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
```

**Lock vs. RLock:**

| Feature | Lock | RLock |
|---------|------|-------|
| Multiple acquisitions | No (deadlock) | Yes (by same thread) |
| Release by any thread | Yes | No (only owning thread) |
| Recursive calls | Not allowed | Allowed |
| Use case | Simple critical sections | Recursive functions, nested locks |

---

## 2.8 Thread Synchronization with Semaphore

**Semaphore Concept:**
- Manages access to a fixed number of resources
- Internal counter for available resources
- `acquire()` decreases counter, `release()` increases counter

**Producer-Consumer with Semaphore:**

```
Producer                         Consumer
    │                                │
    │── create item ──┐              │
    │                 ▼              │
    │         ┌─────────────┐        │
    │         │  Semaphore  │        │
    │         │  Counter=0  │        │
    │         └─────────────┘        │
    │                 │              │
    │── release() ────┘              │
    │                      ┌─────────┘
    │                      │── acquire() ──┐
    │                      ▼              │
    │                 consume item ◄──────┘
```

### Semaphore Example

```python
import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

semaphore = threading.Semaphore(0)
item = 0

def consumer():
    logging.info('Consumer is waiting')
    semaphore.acquire()
    logging.info(f'Consumer notify: item number {item}')

def producer():
    global item
    time.sleep(3)
    item = random.randint(0, 1000)
    logging.info(f'Producer notify: item number {item}')
    semaphore.release()

def main():
    for i in range(10):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

if __name__ == "__main__":
    main()
```

**Output:**
```
2019-01-27 19:21:19,354 Thread-1 INFO Consumer is waiting
2019-01-27 19:21:22,360 Thread-2 INFO Producer notify: item number 388
2019-01-27 19:21:22,385 Thread-1 INFO Consumer notify: item number 388
...
```

**Semaphore Types:**

| Type | Initial Value | Use Case |
|------|---------------|----------|
| Binary Semaphore | 1 | Mutex (mutual exclusion) |
| Counting Semaphore | N | Resource pool (N resources) |
| Event Semaphore | 0 | Synchronization between threads |

---

## 2.9 Thread Synchronization with Condition

**Condition Workflow:**

```
Producer                         Consumer
    │                                │
    │── acquire() ──┐                │
    │               ▼                │
    │         ┌─────────────┐        │
    │         │  Condition  │        │
    │         │    Lock     │        │
    │         └─────────────┘        │
    │               │                │
    │    if buffer full:             │
    │         wait() ────────────────┼── if buffer empty: wait()
    │               │                │
    │── add item ───┘                │
    │               │                │
    │── notify() ────────────────────┼── remove item
    │               │                │
    │── release() ──┘                │
```

### Condition Example (Producer-Consumer)

```python
import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()

class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def consume(self):
        with condition:
            if len(items) == 0:
                logging.info('no items to consume')
                condition.wait()
            items.pop()
            logging.info('consumed 1 item')
            condition.notify()
    
    def run(self):
        for i in range(20):
            time.sleep(2)
            self.consume()

class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def produce(self):
        with condition:
            if len(items) == 10:
                logging.info(f'items produced {len(items)}. Stopped')
                condition.wait()
            items.append(1)
            logging.info(f'total items {len(items)}')
            condition.notify()
    
    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.produce()

# Main execution
# producer = Producer()
# consumer = Consumer()
# producer.start()
# consumer.start()
```

**Condition Methods:**

| Method | Description |
|--------|-------------|
| `acquire()` | Acquires the underlying lock |
| `release()` | Releases the underlying lock |
| `wait()` | Releases lock and blocks until notified |
| `notify()` | Wakes one waiting thread |
| `notify_all()` | Wakes all waiting threads |

---

## 2.10 Thread Synchronization with Event

**Event Workflow:**

```
Producer                         Consumer
    │                                │
    │── create item ──┐              │
    │                 ▼              │
    │         ┌─────────────┐        │
    │         │    Event    │        │
    │         │  Flag=False │        │
    │         └─────────────┘        │
    │                 │              │
    │── set() ────────┘              │
    │                      ┌─────────┘
    │                      │── wait() (blocks until set)
    │                      ▼
    │                 consume item
    │                      │
    │── clear() ───────────┘
```

### Event Example

```python
import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()

class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def run(self):
        while True:
            time.sleep(2)
            event.wait()
            if items:
                item = items.pop()
                logging.info(f'Consumer notify: {item} popped by {self.name}')
            event.clear()

class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def run(self):
        for i in range(5):
            time.sleep(2)
            item = random.randint(0, 100)
            items.append(item)
            logging.info(f'Producer notify: item {item} appended by {self.name}')
            event.set()

if __name__ == "__main__":
    t1 = Producer()
    t2 = Consumer()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

**Output:**
```
2019-02-02 18:23:35,125 Thread-1 INFO Producer notify: item 68 appended by Thread-1
2019-02-02 18:23:35,133 Thread-2 INFO Consumer notify: 68 popped by Thread-2
2019-02-02 18:23:37,138 Thread-1 INFO Producer notify: item 45 appended by Thread-1
2019-02-02 18:23:37,143 Thread-2 INFO Consumer notify: 45 popped by Thread-2
```

**Event Methods:**

| Method | Description |
|--------|-------------|
| `set()` | Sets internal flag to True |
| `clear()` | Sets internal flag to False |
| `is_set()` | Returns current flag value |
| `wait()` | Blocks until flag is True |

---

## 2.11 Thread Synchronization with Barrier

**Barrier Concept:**
- Synchronizes a fixed number of threads at a specific point
- Threads that reach the barrier wait until all threads arrive

**Barrier Workflow:**

```
Thread 1 ──→ Barrier ──┐
Thread 2 ──→ Barrier ──┼── All threads arrived ──→ Continue
Thread 3 ──→ Barrier ──┘
```

### Barrier Example (Race Simulation)

```python
from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']

def runner():
    name = runners.pop()
    sleep(randrange(2, 5))
    print(f'{name} reached the barrier at: {ctime()}')
    finish_line.wait()

def main():
    threads = []
    print('START RACE!!!!')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Race over!')

if __name__ == "__main__":
    main()
```

**Output:**
```
START RACE!!!!
Dewey reached the barrier at: Sat Feb 2 21:44:48 2019
Huey reached the barrier at: Sat Feb 2 21:44:49 2019
Louie reached the barrier at: Sat Feb 2 21:44:50 2019
Race over!
```

**Barrier Methods:**

| Method | Description |
|--------|-------------|
| `wait(timeout=None)` | Wait for barrier, returns when all threads arrive |
| `abort()` | Puts barrier into broken state |
| `reset()` | Resets barrier to initial state |

---

## 2.12 Thread Communication Using Queue

**Queue Communication Pattern:**

```
                    ┌─────────────────────────────────────┐
                    │                                     │
Producer 1 ──put()──→  Queue (Thread-safe FIFO)  ──get()──→ Consumer 1
                    │                                     │
Producer 2 ──put()──→  ┌─────────────────────────────┐    ──get()──→ Consumer 2
                    │  │  Internal Lock/ Synchronization │
                    └─────────────────────────────────────┘
```

### Queue Example

```python
from threading import Thread
from queue import Queue
import time
import random

class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f'Producer notify: item N°{item} appended to queue by {self.name}')
            time.sleep(1)

class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        while True:
            item = self.queue.get()
            print(f'Consumer notify: {item} popped from queue by {self.name}')
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue()
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
```

**Output:**
```
Producer notify: item N°186 appended to queue by Thread-1
Consumer notify: 186 popped from queue by Thread-2
Producer notify: item N°16 appended to queue by Thread-1
Consumer notify: 16 popped from queue by Thread-3
...
```

**Queue Methods:**

| Method | Description |
|--------|-------------|
| `put(item, block=True, timeout=None)` | Adds item to queue |
| `get(block=True, timeout=None)` | Removes and returns item |
| `task_done()` | Indicates item has been processed |
| `join()` | Blocks until all items processed |
| `qsize()` | Returns approximate queue size |
| `empty()` | Returns True if queue is empty |
| `full()` | Returns True if queue is full |

---

## Chapter Summary

**Synchronization Primitives Summary:**

| Primitive | Use Case | Key Features |
|-----------|----------|--------------|
| Lock | Simple critical sections | Mutual exclusion |
| RLock | Recursive/nested locks | Reentrant, same thread |
| Semaphore | Resource pools | Counting mechanism |
| Condition | Complex coordination | Wait/Notify pattern |
| Event | Simple signaling | Flag-based |
| Barrier | Phased execution | Synchronize multiple threads |
| Queue | Data exchange | Thread-safe FIFO |

**Best Practices:**

1. **Choose the right primitive:** Use Queue for data exchange, Lock for simple mutual exclusion, Condition for complex producer-consumer

2. **Avoid deadlocks:** Always acquire locks in same order, use timeouts

3. **Minimize lock scope:** Keep critical sections as small as possible

4. **Prefer higher-level abstractions:** Queue > Condition > Lock

5. **Consider GIL limitations:** Threads are best for I/O-bound tasks

