# Chapter 02: Thread Synchronization Concepts in Python

## Overview

This chapter explains Thread Synchronization in Parallel and Distributed
Computing (PDC) using Python. It focuses on managing shared resources
safely when multiple threads execute at the same time.

The documentation is divided into two sections:

-   **Part 1: Theory** covers race conditions, shared memory problems,
    and synchronization techniques.
-   **Part 2: Practical Implementation** explains Python examples using
    threads, locks, semaphores, and queues.

------------------------------------------------------------------------

# PART 1: THEORETICAL CONCEPTS

## 1. Shared Memory Problem

Threads inside the same process share memory, variables, and resources.
This improves communication speed but can create problems when multiple
threads access the same data simultaneously.

## Race Condition

A race condition happens when multiple threads modify shared data at the
same time. Because thread execution order is unpredictable, the final
result may become incorrect.

## Critical Section

A critical section is a part of code that works with shared resources.
Synchronization ensures that only one thread can execute this section at
a time.

------------------------------------------------------------------------

# 2. Synchronization Techniques

## Locks and RLocks

A Lock allows only one thread to access a critical section at a time.

Process:

1.  A thread acquires the lock.
2.  It performs the required operation.
3.  It releases the lock.
4.  Another thread can continue.

RLock allows the same thread to acquire the same lock multiple times
without creating a deadlock.

------------------------------------------------------------------------

## Semaphores

A Semaphore controls access to resources using a counter.

Unlike a normal Lock, a Semaphore can allow multiple threads to access a
resource depending on its limit.

Example: A Semaphore with a value of 5 allows five threads to use a
resource at the same time.

------------------------------------------------------------------------

## Events and Conditions

An Event allows threads to communicate through signals.

A thread can wait until another thread completes a task and sends a
signal.

A Condition combines locking and waiting mechanisms to handle situations
where threads need to wait for specific changes.

------------------------------------------------------------------------

# 3. Producer-Consumer Pattern

The Producer-Consumer pattern is used when one thread creates data and
another thread processes it.

Producer: - Creates data - Adds data to a shared buffer

Consumer: - Takes data from the buffer - Processes the data

Synchronization prevents problems such as reading empty buffers or
adding data when storage is full.

Python Queue provides built-in thread safety for this pattern.

------------------------------------------------------------------------

# PART 2: PRACTICAL IMPLEMENTATION

## 4. Implementation Examples

## Basic Thread Creation

File: `Thread_definition.py`

This example demonstrates:

-   Creating threads
-   Passing parameters
-   Starting execution
-   Managing multiple threads

------------------------------------------------------------------------

## Lock Implementation

File: `MyThreadClass_lock.py`

This example shows how locks protect shared resources and prevent
multiple threads from modifying data at the same time.

------------------------------------------------------------------------

## Semaphore Implementation

File: `Semaphore.py`

This example demonstrates communication between threads where one thread
waits until another thread completes an action and sends a signal.

------------------------------------------------------------------------

## Thread-Safe Queue

File: `Threading_with_queue.py`

This example implements the Producer-Consumer model using Python Queue.

Benefits:

-   Safe communication between threads
-   Reduced chance of race conditions
-   Easier thread management

------------------------------------------------------------------------

# 5. Execution Guide

Run the following commands inside the Chapter02 directory:

``` bash
python Thread_definition.py
python MyThreadClass_lock.py
python Semaphore.py
python Threading_with_queue.py
```
