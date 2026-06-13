# Chapter 02: Thread Synchronization Primitives

## Preface

Welcome to the academic documentation for Chapter 02 of the Parallel and Distributed Computing (PDC) course. This chapter covers the mechanics of multithreaded systems, focusing on how threads share memory and the synchronization tools needed to prevent data corruption.

This document is divided into two sections: Section 1 discusses the theoretical challenges of concurrent memory access, and Section 2 reviews the practical Python code examples and their outputs.

---

## Index of Topics

### Section 1: Memory Models & Synchronization Theory
1. [The Shared Address Space Challenge](#1-the-shared-address-space-challenge)
2. [Race Conditions & Critical Sections](#2-race-conditions--critical-sections)
3. [Synchronization Primitives Explained](#3-synchronization-primitives-explained)
    - [Locks and Re-entrant Locks](#locks-and-re-entrant-locks)
    - [Semaphores and Counting States](#semaphores-and-counting-states)
    - [Events and Conditional Variables](#events-and-conditional-variables)
4. [The Producer-Consumer Architectural Pattern](#4-the-producer-consumer-architectural-pattern)

### Section 2: Practical Implementation Analysis
5. [Thread Spawning & Lifecycle](#5-thread-spawning--lifecycle)
6. [Preventing Conflicts with Locks](#6-preventing-conflicts-with-locks)
7. [Thread Signaling with Semaphores](#7-thread-signaling-with-semaphores)
8. [Thread-Safe Queue Buffers](#8-thread-safe-queue-buffers)
9. [Local Execution Guide](#9-local-execution-guide)

---

# SECTION 1: MEMORY MODELS & SYNCHRONIZATION THEORY

## 1. The Shared Address Space Challenge

When an operating system runs a process, it assigns it a designated segment of virtual memory. In a multithreaded design, all spawned threads run within this same process boundaries. As a result, they share access to the same heap memory, global variables, static variables, and file descriptors.

This shared architecture allows threads to communicate with minimal latency, as they do not need to use intermediate messaging layers. However, this convenience introduces the risk of concurrent read-write conflicts. If two threads access and modify the same memory address at the same time, the data can become corrupted.

## 2. Race Conditions & Critical Sections

Understanding concurrent conflicts requires defining two main concepts:

- **Race Conditions:** A race condition occurs when the correctness of a program's output depends on the order or timing of thread execution. If multiple threads modify a shared variable simultaneously without synchronization, the final value is non-deterministic.
- **Critical Sections:** A critical section is a block of code that accesses a shared resource (such as a variable, file, or database socket) that must not be concurrently accessed by more than one thread.

To prevent race conditions, execution within a critical section must be mutual, ensuring that only one thread can execute it at a time.

## 3. Synchronization Primitives Explained

To manage execution within critical sections, operating systems and programming frameworks provide synchronization objects, or primitives.

### Locks and Re-entrant Locks

A Lock (or Mutex) is a binary flag representing a resource's availability. It has two main states: locked and unlocked.
- When a thread enters a critical section, it must acquire the lock. If the lock is already held by another thread, the requesting thread blocks until the lock is released.
- A Re-entrant Lock (RLock) is a variation that allows the same thread to acquire the lock multiple times without causing a deadlock, which is useful in recursive functions.

### Semaphores and Counting States

A Semaphore is a synchronization primitive that manages access to a pool of resources using a counter.
- A counting semaphore is initialized with a value $N$. Each time a thread acquires the semaphore, the counter decreases. When the counter reaches zero, any subsequent threads block until a slot is released.
- This is useful for managing resource-limited systems, such as database connection pools or network bandwidth limits.

### Events and Conditional Variables

- **Events:** An event is a synchronization flag that allows threads to wait for a signal from another thread. A thread blocks until the event flag is set to true.
- **Condition Variables:** A condition variable is a more advanced primitive that allows a thread to wait for a specific condition to be met. It is always associated with a lock to ensure thread-safe condition checking.

## 4. The Producer-Consumer Architectural Pattern

The Producer-Consumer pattern is a common design pattern in parallel systems. In this pattern:
- **Producers** generate data and place it into a shared buffer.
- **Consumers** retrieve data from the buffer and process it.

To keep this pattern stable, the buffer must be synchronized. If the buffer is full, producers must block. If the buffer is empty, consumers must block. This coordination is typically handled using thread-safe queues that manage locking and signaling internally.

---

# SECTION 2: PRACTICAL IMPLEMENTATION ANALYSIS

## 5. Thread Spawning & Lifecycle

**Script name:** `Thread_definition.py`

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

Using `join()` forces the main thread to wait for each child thread to finish before launching the next one in this specific sequence.

---

## 6. Preventing Conflicts with Locks

**Script name:** `MyThreadClass_lock.py`

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

## 7. Thread Signaling with Semaphores

**Script name:** `Semaphore.py`

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

## 8. Thread-Safe Queue Buffers

**Script name:** `Threading_with_queue.py`

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

## 9. Local Execution Guide

To run these thread synchronization tests, navigate to the `Chapter02` directory in your terminal and execute:

```bash
python Thread_definition.py
python MyThreadClass_lock.py
python Semaphore.py
python Threading_with_queue.py
```
