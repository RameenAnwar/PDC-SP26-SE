# Chapter 02: Thread Synchronization Primitives in Python

## Overview

Welcome to the **Parallel and Distributed Computing (PDC)** documentation for Chapter 02. This chapter dives strictly into **Threading** and the complex synchronization mechanisms required to manage shared memory safely.

This guide is strictly divided into two sections: **Part 1** covers the theoretical computer science concepts behind race conditions and synchronization objects, and **Part 2** showcases practical Python code implementations.

---

## Table of Contents

### Part 1: Theoretical Foundations
1. [The Shared Memory Problem](#1-the-shared-memory-problem)
2. [Synchronization Primitives](#2-synchronization-primitives)
    - [Locks (Mutex) & RLocks](#locks-mutex--rlocks)
    - [Semaphores](#semaphores)
    - [Events & Conditions](#events--conditions)
3. [The Producer-Consumer Pattern](#3-the-producer-consumer-pattern)

### Part 2: Practical Implementation
4. [Implementation Breakdown & Outputs](#4-implementation-breakdown--outputs)
    - [Basic Thread Definition](#basic-thread-definition)
    - [Implementing Locks](#implementing-locks)
    - [Implementing Semaphores](#implementing-semaphores)
    - [Thread-Safe Queues](#thread-safe-queues)
5. [Execution Guide](#5-execution-guide)

---

# PART 1: THEORETICAL FOUNDATIONS

## 1. The Shared Memory Problem

In a multithreaded environment, all threads exist within the exact same OS process. This means they physically share access to the same heap memory, variables, and data structures.

- **Race Conditions:** When two or more threads attempt to read, modify, and write to a shared variable at the exact same physical microsecond, the final state of the variable becomes unpredictable. This non-deterministic behavior is the most critical vulnerability in Parallel Computing.
- **Critical Sections:** A piece of architecture/code that accesses a shared resource. To prevent race conditions, a Critical Section must execute as an "atomic" operation—meaning only one thread can be inside the critical section at any given time.

## 2. Synchronization Primitives

To enforce atomic operations across Critical Sections, the OS and Python's `threading` library provide several architectural tools known as primitives.

### Locks (Mutex) & RLocks

```mermaid
graph TD
    subgraph Critical Section
        L[Lock Acquired]
        Work[Shared Resource Modification]
        R[Lock Released]
    end
    T1[Thread 1] --> L
    L --> Work --> R
    T2[Thread 2] -.->|Blocked until Release| L
```

- **Lock (Mutual Exclusion Object):** The simplest primitive. A thread "acquires" the lock before entering a critical section. If another thread tries to acquire it concurrently, it halts and waits until the first thread "releases" it. 
- **RLock (Re-entrant Lock):** A special Lock that can be acquired multiple times by the *same* thread without causing a deadlock (ideal for recursive functions).

### Semaphores

```mermaid
graph TD
    subgraph SemPool [Semaphore Pool N=2]
        S1[Slot 1: Connected]
        S2[Slot 2: Connected]
    end
    T1[Thread 1] --> S1
    T2[Thread 2] --> S2
    T3[Thread 3] -.->|Blocked until Slot opens| SemPool
```

A Semaphore is an advanced lock that maintains an internal counter rather than a strict binary True/False state. 
- **Use Case:** Instead of allowing exactly *one* thread into a critical section, a Semaphore initialized to $N$ allows exactly $N$ threads to access a resource pool simultaneously (e.g., limiting database connection pools).

### Events & Conditions
- **Event:** A simple communication mechanism where one thread signals an event, and other threads wait for that signal before continuing execution.
- **Condition:** A more complex primitive that couples a Lock with an Event. It allows threads to wait for a specific state change in shared data before proceeding.

## 3. The Producer-Consumer Pattern

A classic computer science paradigm in PDC. 

```mermaid
graph LR
    P[Producer Thread] -->|Generates Data| Q[(Thread-Safe Queue)]
    Q -->|Processes Data| C1[Consumer Thread 1]
    Q -->|Processes Data| C2[Consumer Thread 2]
```

- **Producers** generate data (e.g., retrieving web requests) and place it into a buffer.
- **Consumers** take data out of the buffer and process it.

To prevent the Producer from overflowing the buffer or the Consumer from reading empty memory, they must be rigorously synchronized. Python solves this robustly via the built-in `queue.Queue` object, which inherently utilizes Locks and Conditions under the hood to ensure thread-safe operations.

---
---

# PART 2: PRACTICAL IMPLEMENTATION

## 4. Implementation Breakdown & Outputs

The `Chapter02` directory contains empirical scripts proving these concepts. Below are the core highlights.

### Basic Thread Definition
**File:** `Thread_definition.py`

**Code Snippet:**
```python
import threading

def my_func(thread_number):
    print('my_func called by thread N°{}'.format(thread_number))

def main():
    threads = []
    # Spawning 10 threads pointing to the same function
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
        t.join()
```
**Expected Output:**
```text
my_func called by thread N°0
my_func called by thread N°1
...
my_func called by thread N°9
```
*(Demonstrates basic thread spawning, scheduling, and argument passing.)*

---

### Implementing Locks
**File:** `MyThreadClass_lock.py`

**Code Snippet:**
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
      # Critical Section Start
      threadLock.acquire()      
      print ("---> " + self.name + " running")
      time.sleep(self.duration) 
      print ("---> " + self.name + " over\n")
      # Critical Section End
      threadLock.release()
```
**Expected Output:**
```text
---> Thread#1 running
---> Thread#1 over

---> Thread#2 running
---> Thread#2 over
```
*(Notice how Thread 2 categorically cannot start "running" until Thread 1 prints "over" and releases the lock, effectively serializing the Critical Section to prevent race conditions).*

---

### Implementing Semaphores
**File:** `Semaphore.py`

**Code Snippet:**
```python
import threading
import time

semaphore = threading.Semaphore(0)
item = 0

def consumer():
    print('Consumer is waiting')
    semaphore.acquire()  # Will block here until semaphore is released by producer
    print(f'Consumer notify: item number {item}')

def producer():
    global item
    time.sleep(1)
    item = 100
    print(f'Producer notify: item number {item}')
    semaphore.release()  # Increments semaphore counter, unblocking consumer
```
**Expected Output:**
```text
Consumer is waiting
Producer notify: item number 100
Consumer notify: item number 100
```
*(Demonstrates signal synchronicity between threads; the consumer reliably halts until the producer finishes generating the data and increments the semaphore).*

---

### Thread-Safe Queues
**File:** `Threading_with_queue.py`

**Code Snippet:**
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
**Expected Output:**
```text
Producer appended 0 to queue
Consumer popped 0
Producer appended 1 to queue
Consumer popped 1
...
```
*(Demonstrates the ideal and robust Producer/Consumer architecture. By utilizing Python's thread-safe Queue, we avoid manually calling Lock.acquire() and prevent race conditions inherently).*

---

## 5. Execution Guide
To conduct these benchmarks locally, execute the corresponding scripts sequentially via your OS terminal. Ensure you are navigated inside the `Chapter02` directory:

```bash
python Thread_definition.py
python MyThreadClass_lock.py
python Semaphore.py
python Threading_with_queue.py
```
