# Chapter 02: Core Threading & Synchronization Mechanisms in Python


---

##  Course Information
**Course:** Parallel and Distributed Computing (PDC) 
**Student Name:** abdullah 
**Roll No:** 23FA-016-SE

---

## Overview

Welcome to Chapter 02 of the Parallel and Distributed Computing (PDC) lab series. This chapter focuses on building a deep, practical understanding of Python’s threading system and the synchronization tools required to coordinate concurrent execution safely.

Unlike simple multithreading examples, this chapter explores both low-level thread construction and advanced synchronization patterns, showing how Python manages shared resources, avoids race conditions, and enables structured concurrency.

The chapter is organized into two major parts:

- Part 1: Fundamental concepts of threading behavior and synchronization theory  
- Part 2: Hands-on Python implementations demonstrating real-world thread coordination patterns  

---

## Table of Contents

### Part 1: Theoretical Foundations
- Thread Lifecycle & Execution Model  
- Shared Memory in Multithreading  
- Race Conditions and Critical Sections  
- Synchronization Primitives Overview  
- Locks vs RLocks (Re-entrant Locks)  
- Semaphores and Resource Limiting  
- Events and Condition-based Signaling  
- Producer–Consumer Architecture  

### Part 2: Practical Implementation Modules
- Basic Thread Class Design  
- Thread Identification and Execution Flow  
- Lock-Based Synchronization Examples  
- Recursive Locking with RLock  
- Event Signaling Between Threads  
- Condition Variables for Controlled Execution  
- Semaphore-based Resource Control  
- Multi-thread Execution Patterns  

---

## PART 1: THEORETICAL FOUNDATIONS

### 1. Threading and Shared Execution Environment

In Python, threads run inside a single process and share the same memory space. This enables fast communication but introduces serious risks when multiple threads modify shared variables simultaneously.

Key Problem:
- Threads execute unpredictably due to CPU scheduling  
- Shared variables may be updated inconsistently  

Critical Section:
A section of code where shared resources are accessed. Without control mechanisms, this leads to inconsistent program states and unpredictable outputs.

---

### 2. Synchronization Mechanisms

#### Locks (Mutex)
A Lock ensures that only one thread executes a critical section at a time. Other threads are blocked until the lock is released.

#### RLock (Re-entrant Lock)
An advanced lock that allows the same thread to acquire the lock multiple times without deadlocking. Useful in recursive or nested function calls.

#### Events
Events act as signaling flags between threads. One thread signals completion or readiness, while others wait until the signal is triggered.

#### Conditions
Condition variables combine locking and signaling, allowing threads to wait until a specific state is met before continuing execution.

#### Semaphores
A Semaphore controls access to a resource pool using a counter instead of a binary lock. Example: allowing N threads to access a limited resource simultaneously.

---

### 3. Thread Communication using Queue

The Queue module provides a safe way for threads to exchange data.

Producer–Consumer Model:
- Producers generate data and insert it into the queue  
- Consumers retrieve and process data safely  
- Queue internally handles locking and synchronization  

This eliminates the need for manual lock management in many cases.

---

## PART 2: PRACTICAL IMPLEMENTATION MODULES

### 4. Basic Thread Execution Model
File: `Thread_definition.py`  
Introduces basic thread creation using Python’s threading system.

### 5. Thread Naming & Class-Based Execution
File: `Thread_name_and_processes.py`  
Improves traceability using thread identifiers.

### 6. Custom Thread Class Design
File: `MyThreadClass.py`  
Object-oriented thread implementation using class extension.

### 7. Lock-Based Synchronization
Files:
- `MyThreadClass_lock.py`  
- `MyThreadClass_lock_2.py`  
- `Rlock.py`  

Demonstrates mutual exclusion and recursive locking.

### 8. Event-Based Thread Coordination
File: `Event.py`  
Thread signaling and coordination using events.

### 9. Condition Variable Synchronization
File: `Condition.py`  
Threads wait for shared-state conditions.

### 10. Semaphore-Based Resource Control
File: `Semaphore.py`  
Controls access to limited resources using counters.

### 11. Threading with Queue (Producer–Consumer System)
File: `Threading_with_queue.py`  
Safe communication between threads using Queue.

### 12. Thread Execution Behavior Analysis
File: `Thread_determine.py`  
Shows unpredictability of thread scheduling.

### 13. Thread Lifecycle & Identity Tracking
Reinforces:
- Thread start/join behavior  
- Execution lifecycle  
- Scheduling unpredictability  

---

## Execution Guide

Run any script using:

```bash
python Thread_definition.py
python MyThreadClass.py
python MyThreadClass_lock.py
python MyThreadClass_lock_2.py
python Rlock.py
python Event.py
python Condition.py
python Semaphore.py
python Threading_with_queue.py
