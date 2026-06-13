# Parallel & Distributed Computing (PDC)
## Chapter 02: Thread Synchronization Primitives

## Course & Submission Details
- **Course Title:** Parallel and Distributed Computing (PDC)
- **Student Name:** Zaid Bhatti
- **Roll Number:** 23FA-014-SE
- **Chapter Focus:** Thread Synchronization and Concurrency Management

---

## 1. Overview of Thread Concurrency

Multithreading is an execution model where multiple threads run within the memory space of a single parent process, sharing resources such as heap memory and global variables. While this shared-memory model allows threads to communicate with minimal latency, it introduces the risk of concurrent read-write conflicts.

This document reviews the mechanisms used to synchronize thread execution and ensure data integrity in concurrent Python applications.

---

## 2. Technical Discussion & Architectural Foundations

### The Shared Address Space Challenge
In a multithreaded process, all threads share access to the same heap memory, static variables, and file descriptors. This eliminates the need for expensive inter-process communication layers but introduces the risk of data corruption if multiple threads attempt to modify the same memory location simultaneously.

### Race Conditions & Critical Sections
- **Race Condition:** Occurs when the program's output depends on the timing or order of thread execution. If two threads modify a shared variable at the same time, the final state becomes non-deterministic.
- **Critical Section:** A block of code that accesses a shared resource that must not be concurrently accessed by more than one thread.

To prevent race conditions, access to critical sections must be synchronized.

---

## 3. Synchronization Primitives

To coordinate access to critical sections, modern operating systems and runtime environments provide several synchronization primitives.

### Locks (Mutexes)
A Lock is a binary flag that represents the availability of a resource. It has two states: locked and unlocked.
- When a thread enters a critical section, it must acquire the lock. If the lock is already held by another thread, the requesting thread blocks until the lock is released.
- This ensures mutual exclusion, meaning only one thread can execute the critical section at a time.

### Reentrant Locks (RLocks)
A Reentrant Lock (RLock) is a variation of the standard lock that can be acquired multiple times by the same thread. It maintains an owner thread identifier and an acquisition count.
- This allows a thread to enter nested critical sections or recursive functions without causing a deadlock.
- The lock is only fully released when the acquisition count returns to zero.

### Semaphores
A Semaphore is a synchronization primitive that manages access to a pool of resources using a counter.
- A counting semaphore is initialized with a value $N$. Each time a thread acquires the semaphore, the counter decreases. When the counter reaches zero, any subsequent threads block until a slot is released.
- This is useful for managing resource-limited systems, such as database connection pools or network bandwidth limits.

### Events & Condition Variables
- **Events:** An event is a simple synchronization flag. Threads can block on an event until another thread sets the flag to true, signaling them to resume.
- **Condition Variables:** Allow threads to wait for a specific state condition to be met. It is always associated with a lock to ensure thread-safe condition checking.

---

## 4. The Producer-Consumer Pattern

The Producer-Consumer pattern is a common design pattern in concurrent systems. In this pattern:
- **Producers** generate data and place it into a shared buffer.
- **Consumers** retrieve data from the buffer and process it.

To keep this pattern stable, the buffer must be synchronized. If the buffer is full, producers must block. If the buffer is empty, consumers must block. This coordination is typically handled using thread-safe queues that manage locking and signaling internally.

---

## 5. Practical Implementation Analysis

### Spawning Threads (`Thread_definition.py`)
This script demonstrates how to define, initialize, and launch multiple threads in Python using the `threading` module.

```python
import threading

def my_func(thread_number):
    print('my_func called by thread N°{}'.format(thread_number))

def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
        t.join()
```

**Expected Console Output:**
```text
my_func called by thread N°0
my_func called by thread N°1
...
my_func called by thread N°9
```

Using `join()` forces the main thread to wait for each child thread to finish before launching the next one in sequence.

---

### Preventing Conflicts with Locks (`MyThreadClass_lock.py`)
This script demonstrates using a `Lock` object to coordinate critical section entry among multiple custom thread classes.

```python
import threading
import time

threadLock = threading.Lock()

class MyThreadClass(threading.Thread):
   def __init__(self, name, duration):
      threading.Thread.__init__(self)
      self.name = name
      self.duration = duration
      
   def run(self):
      threadLock.acquire()      
      print ("---> " + self.name + " running")
      time.sleep(self.duration) 
      print ("---> " + self.name + " over\n")
      threadLock.release()
```

**Expected Console Output:**
```text
---> Thread#1 running
---> Thread#1 over

---> Thread#2 running
---> Thread#2 over
```

Because of the lock, `Thread#2` cannot start running until `Thread#1` has released the lock.

---

### Signaling with Semaphores (`Semaphore.py`)
This script uses a `Semaphore` initialized to zero to coordinate execution order between a producer and consumer thread.

```python
import threading
import time

semaphore = threading.Semaphore(0)
item = 0

def consumer():
    print('Consumer is waiting')
    semaphore.acquire()
    print(f'Consumer notify: item number {item}')

def producer():
    global item
    time.sleep(1)
    item = 100
    print(f'Producer notify: item number {item}')
    semaphore.release()
```

**Expected Console Output:**
```text
Consumer is waiting
Producer notify: item number 100
Consumer notify: item number 100
```

The consumer thread blocks on `acquire()` until the producer thread calls `release()`, signaling that the data is ready.

---

### Thread-Safe Queue Buffers (`Threading_with_queue.py`)
This script uses Python's built-in, thread-safe `queue.Queue` class to implement a Producer-Consumer pattern.

```python
from threading import Thread
from queue import Queue
import time

class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        for i in range(5):
            self.queue.put(i)
            print(f'Producer appended {i} to queue')
            time.sleep(1)

class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        while True:
            item = self.queue.get()
            print(f'Consumer popped {item}')
            self.queue.task_done()
```

**Expected Console Output:**
```text
Producer appended 0 to queue
Consumer popped 0
Producer appended 1 to queue
Consumer popped 1
...
```

The queue manages thread synchronization internally, preventing race conditions without needing manual locking logic.

---

## 6. Local Execution Guide

To run these thread synchronization tests, navigate to the `Chapter02` directory in your terminal and execute:

```bash
python Thread_definition.py
python MyThreadClass_lock.py
python Semaphore.py
python Threading_with_queue.py
```
