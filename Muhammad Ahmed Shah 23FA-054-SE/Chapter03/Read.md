# Chapter 03 - Process Synchronization and Communication

## Introduction

Process synchronization is a fundamental concept in Parallel and Distributed Computing. When multiple processes execute concurrently, they often need to access shared resources. Without proper synchronization, processes may interfere with each other, leading to inconsistent data, race conditions, and unpredictable results.

This chapter focuses on techniques used to coordinate processes and manage their access to shared resources. Python provides several mechanisms for process synchronization, including locks, semaphores, queues, and pipes. These tools allow processes to communicate safely and work together without conflicts.

## Objectives of Chapter 03

1. Understand the need for process synchronization
2. Learn about race conditions and critical sections
3. Implement locks in Python
4. Implement semaphores for resource management
5. Use events for process signaling
6. Use queues for interprocess communication
7. Understand deadlock and starvation concepts
8. Compare different synchronization mechanisms

## Concepts Covered

### Race Condition

A race condition occurs when multiple processes access shared data concurrently and the final result depends on the order of execution. Race conditions are difficult to debug because they occur randomly.

Example:
- Process A reads value 5
- Process B reads value 5
- Process A writes 6
- Process B writes 6
- Final value is 6 instead of 7

### Critical Section

A critical section is a block of code that accesses shared resources. Rules for critical sections:

- Mutual Exclusion - Only one process in critical section at a time
- Progress - Processes outside critical section cannot block others
- Bounded Waiting - No process waits indefinitely

### Lock

Lock is the simplest synchronization primitive. Only one process can acquire a lock at a time.

Methods:
- acquire() - Gets the lock
- release() - Releases the lock

### RLock (Reentrant Lock)

RLock can be acquired multiple times by the same process. Useful when a process needs to re-enter a critical section.

### Semaphore

Semaphore allows a fixed number of processes to access a resource.

Types:
- Counting Semaphore - Allows N processes
- Binary Semaphore - Allows 1 process

### Event

Event allows processes to communicate state changes.

Methods:
- set() - Sets the event
- clear() - Clears the event
- wait() - Waits for event
- is_set() - Checks event state

### Condition

Condition allows processes to wait for specific conditions to become true. More flexible than Event.

### Queue

Queue provides thread-safe and process-safe data exchange. Multiple processes can put and get items from a queue.

### Pipe

Pipe provides a two-way communication channel between two processes.

## Python Modules Used

```python
import multiprocessing
from multiprocessing import Lock, Semaphore, Event, Condition, Queue, Pipe
import time
import random
