# README

## Overview

This repository contains Python programs that demonstrate the fundamentals of **Multithreading** and **Thread Synchronization**. The examples cover thread creation, thread management, locks, semaphores, barriers, events, conditions, queues, and reentrant locks. These programs help in understanding how multiple threads can work together safely and efficiently within a Python application.

---

## Files Description

### thread_definition.py

A basic example of thread creation and execution. Multiple threads are created, started, and joined to demonstrate the thread lifecycle. 

### thread_determine.py

Demonstrates how to identify and display thread names while executing multiple functions concurrently. 

### thread_name_and_processes.py

Shows how threads can be created using a custom thread class and displays information about running threads. 

### MyThreadClass.py

Implements a custom thread class by extending Python's `Thread` class. Multiple threads execute concurrently with random durations to demonstrate parallel execution. 

### MyThreadClass_lock.py

Demonstrates the use of a **Lock** to ensure that only one thread accesses a critical section at a time. This prevents race conditions and synchronizes thread execution. 

### MyThreadClass_lock2.py

Another lock-based example where the lock is released immediately after entering the critical section, allowing other threads to continue execution while the current thread performs additional work. 

### Rlock.py

Demonstrates the use of a **Reentrant Lock (RLock)**. An RLock allows the same thread to acquire the lock multiple times without causing a deadlock. 

### semaphore.py

Illustrates synchronization using a **Semaphore**. A consumer thread waits until a producer thread signals that data is available. 

### event.py

Demonstrates the use of an **Event** object for communication between producer and consumer threads. Threads coordinate their actions based on event signals. 

### condition.py

Implements the **Producer-Consumer** problem using a **Condition Variable**. Producers and consumers coordinate access to shared resources while avoiding conflicts. 

### barrier.py

Demonstrates the use of a **Barrier**. Multiple threads wait at a synchronization point until all participating threads have reached the barrier before continuing. 

### threading_with_queue.py

Shows thread synchronization using a **Queue**. Producers place items into the queue, while consumers retrieve and process them safely. 

---

## Concepts Covered

* Thread Creation and Execution
* Thread Lifecycle Management
* Thread Synchronization
* Locks and Critical Sections
* Reentrant Locks (RLock)
* Semaphores
* Events
* Condition Variables
* Barriers
* Producer-Consumer Pattern
* Thread-safe Queues

---

## Requirements

* Python 3.x

Standard Python libraries used:

* threading
* time
* random
* queue
* logging
* os

No external packages are required.

---

## Running the Programs

Execute any file using:

```bash
python filename.py
```

Example:

```bash
python barrier.py
```

```bash
python semaphore.py
```

```bash
python condition.py
```

---

## Learning Outcomes

After completing these examples, you will understand:

* How threads are created and managed in Python.
* Different thread synchronization techniques.
* How locks prevent race conditions.
* Communication between producer and consumer threads.
* Safe sharing of resources among multiple threads.
* Practical usage of synchronization tools such as Locks, RLocks, Events, Semaphores, Conditions, Barriers, and Queues.

---

## Conclusion

These programs provide hands-on experience with Python multithreading and synchronization mechanisms. They serve as a foundation for building efficient concurrent applications and understanding common synchronization challenges in multi-threaded environments.
