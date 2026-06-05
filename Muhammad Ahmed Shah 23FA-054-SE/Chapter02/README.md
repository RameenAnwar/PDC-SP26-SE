# PDC Chapter 2: Threading in Python

## Introduction to Multithreading

Multithreading is a programming concept that allows multiple threads to execute independently within a single process. In Python, the `threading` module provides a high-level interface for working with threads. Each thread runs a separate flow of execution while sharing the same memory space of the parent process.

Multithreading is widely used in operating systems, network programming, simulations, and applications requiring concurrent execution.

---

## Importance of Multithreading in PDC

Parallel and Distributed Computing (PDC) relies on concurrency to improve performance and resource utilization. Multithreading helps in:

* Improving application responsiveness
* Performing multiple tasks simultaneously
* Efficient CPU utilization
* Managing asynchronous tasks
* Handling I/O-bound operations efficiently

---

## Python Threading Module Overview

Python provides the `threading` module to create and manage threads. It includes:

* Thread class
* Synchronization primitives
* Communication tools
* Thread lifecycle management methods

---

## Thread Lifecycle

A thread in Python goes through several states:

* New
* Runnable
* Running
* Blocked/Waiting
* Terminated

---

## Thread Creation Methods

Threads in Python can be created using:

1. Function-based threading
2. Class-based threading (extending Thread class)

---

## Thread Synchronization

Synchronization is required to prevent race conditions when multiple threads access shared resources.

---

## barrier.py

Barrier is a synchronization primitive used to block a set of threads until all threads reach a common execution point.

Concepts:

* thread coordination
* synchronization point
* simultaneous release

Working:
Threads wait at barrier until all participants arrive, then proceed together.

---

## condition.py

Condition variables are used to allow threads to wait for certain conditions to be met.

Concepts:

* condition variable
* wait and notify mechanism

Working:
Producer produces data and notifies consumer. Consumer waits until notification is received.

---

## event.py

Event objects provide a simple mechanism for communication between threads.

Concepts:

* event flag
* signaling between threads

Working:
One thread waits for event signal while another sets the event.

---

## mythreadclass.py

This demonstrates creating a thread by extending the Thread class.

Concepts:

* class-based thread creation
* overriding run method

Working:
Thread behavior is defined inside run method.

---

## mythreadclasslock.py

This file demonstrates thread synchronization using Lock.

Concepts:

* mutual exclusion
* critical section

Working:
Lock ensures only one thread modifies shared data at a time.

---

## mythreadclasslock2.py

This file demonstrates usage of multiple locks.

Concepts:

* nested locks
* multiple resource synchronization

Working:
Thread acquires multiple locks to access different shared resources safely.

---

## rlock.py

Reentrant Lock allows a thread to acquire the same lock multiple times.

Concepts:

* recursive locking
* deadlock prevention

Working:
Same thread can re-enter locked region safely.

---

## semaphore.py

Semaphore controls access to a shared resource with a limited number of permits.

Concepts:

* counting semaphore
* resource limitation

Working:
Only defined number of threads can access critical section at a time.

---

## threaddefinition.py

Basic thread creation using function target.

Concepts:

* simple thread execution
* function-based threads

Working:
Thread runs a function independently.

---

## threaddetermine.py

This file checks thread execution status.

Concepts:

* thread lifecycle check
* is_alive method

Working:
Thread reports whether it is currently active.

---

## threadnameandprocess.py

This demonstrates thread naming and process identification.

Concepts:

* thread identification
* process ID retrieval

Working:
Each thread prints its name and process ID.

---

## threadingwithqueue.py

Queue is used for safe communication between threads.

Concepts:

* producer consumer model
* thread-safe queue

Working:
Producer adds items to queue, consumer retrieves items safely.

---

## Synchronization Problems in Multithreading

Common issues include:

* race conditions
* deadlocks
* starvation
* livelocks

---

## Race Condition

Occurs when multiple threads access shared data simultaneously without proper synchronization.

---

## Deadlock

Occurs when two or more threads are waiting for each other to release resources.

---

## Lock Mechanism

Locks ensure only one thread accesses critical section at a time.

---

## Reentrant Lock

Allows a thread to acquire a lock multiple times without blocking itself.

---

## Semaphore Usage

Used when a limited number of threads should access a resource.

---

## Event Mechanism

Used for signaling between threads.

---

## Condition Variables

Used when threads need to wait for a specific condition.

---

## Barrier Synchronization

Used when multiple threads must wait for each other before continuing execution.

---

## Queue in Multithreading

Queue provides safe data sharing between threads without explicit locking.

---

## Producer Consumer Problem

Classic example of synchronization where:

* Producer generates data
* Consumer processes data
* Queue ensures safe communication

---

## Thread Scheduling

Python thread scheduling is managed by the operating system and Global Interpreter Lock (GIL).

---

## Global Interpreter Lock (GIL)

GIL ensures only one thread executes Python bytecode at a time in CPython.

---

## Advantages of Multithreading

* Better CPU utilization
* Improved performance in I/O tasks
* Efficient resource sharing
* Responsive applications

---

## Disadvantages of Multithreading

* Complexity in debugging
* Risk of deadlocks
* Race conditions
* Overhead of synchronization

---

## Best Practices

* Use locks carefully
* Avoid unnecessary shared resources
* Prefer queues for communication
* Minimize critical section size
* Avoid nested locking where possible

---

## Summary

This chapter covers the core concepts of multithreading in Python including thread creation, synchronization, communication, and management. It explains how multiple threads can be coordinated safely to perform concurrent operations effectively in parallel and distributed computing environments.

---

## Conclusion

Understanding threading is essential for developing high-performance applications. Proper use of synchronization primitives ensures safe execution of concurrent programs while minimizing errors such as race conditions and deadlocks.
