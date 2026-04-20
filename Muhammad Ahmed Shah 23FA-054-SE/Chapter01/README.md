# Chapter 01 - Fundamentals of Parallel and Distributed Computing

# Introduction

Parallel and Distributed Computing is an important area of Computer Science that focuses on solving computational problems efficiently by dividing tasks into multiple smaller subtasks and executing them simultaneously. Traditional systems perform operations sequentially, where one instruction executes after another. However, with the rapid growth of data and modern applications, sequential systems often fail to meet performance requirements.

This chapter introduces the foundational concepts of Parallel and Distributed Computing using Python. It explains the difference between serial execution, multithreading, and multiprocessing. The chapter also demonstrates how Python can be used to create concurrent programs for better performance.

The main purpose of this chapter is to build a conceptual understanding of concurrency and parallel execution.

---

# What is Parallel Computing

Parallel Computing is a technique in which multiple tasks are executed at the same time using multiple processors or cores. Instead of waiting for one task to finish before starting another, the system performs several tasks simultaneously.

Example:

- Task 1 executes on Core 1
- Task 2 executes on Core 2
- Task 3 executes on Core 3

This significantly reduces total execution time.

Parallel computing is commonly used in:

- Scientific simulations
- Machine learning
- Data analysis
- Rendering systems
- High performance computing

---

# What is Distributed Computing

Distributed Computing is a model where multiple independent computers communicate over a network and work together to solve a problem.

Each machine performs part of the task and shares results with others.

Examples include:

- Cloud computing systems
- Web servers
- Blockchain networks
- Distributed databases

---

# Need for Parallel and Distributed Computing

Modern applications require:

- Faster execution
- Real-time response
- Large data processing
- Efficient resource usage
- Scalability

Sequential systems become slow when handling large workloads. Parallel and distributed systems solve this problem.

---

# Python in Parallel Computing

Python provides built-in modules for concurrency and parallel programming such as:

- threading
- multiprocessing
- concurrent.futures
- asyncio

This chapter focuses on:

- threading
- multiprocessing

---

# Serial Execution

Serial execution means instructions are processed one by one in sequence.

Example:

Step 1 completes  
Step 2 starts  
Step 2 completes  
Step 3 starts

Advantages:

- Easy to implement
- Easy debugging
- Low complexity

Disadvantages:

- Slow for large tasks
- CPU underutilization
- No concurrency

File Related:

- serial_test.py

---

# Multithreading

Multithreading allows multiple threads within the same process.

A thread is the smallest unit of execution.

Threads share:

- Memory
- Variables
- Resources

Useful for:

- File handling
- Web requests
- Input/Output operations
- Waiting tasks

Advantages:

- Lightweight
- Faster context switching
- Better responsiveness

Disadvantages:

- Race conditions
- Synchronization complexity
- Limited CPU usage due to GIL in Python

File Related:

- multithreading_test.py

---

# Multiprocessing

Multiprocessing creates multiple independent processes.

Each process has:

- Separate memory
- Separate resources
- Independent execution

Useful for:

- CPU intensive calculations
- Mathematical operations
- Image processing
- Large computations

Advantages:

- Utilizes multiple CPU cores
- True parallelism
- Better for CPU bound tasks

Disadvantages:

- Higher memory usage
- Process creation overhead

File Related:

- multiprocessing_test.py

---

# Difference Between Threading and Multiprocessing

| Feature | Threading | Multiprocessing |
|--------|-----------|----------------|
| Memory | Shared | Separate |
| Speed | Faster startup | Slower startup |
| Best For | I/O tasks | CPU tasks |
| Isolation | Low | High |
| CPU Core Usage | Limited | Full |

---

# Python GIL Concept

Python uses the Global Interpreter Lock (GIL).

This means:

Only one thread executes Python bytecode at a time.

Because of GIL:

- Multithreading is better for I/O tasks
- Multiprocessing is better for CPU tasks

---

# Classes and Object-Oriented Concepts

The file `classes.py` demonstrates class concepts.

Topics included:

- Class creation
- Object creation
- Constructors
- Methods
- Encapsulation

Classes help organize code in reusable structures.

Example Uses:

- Employee systems
- Student records
- Banking systems

---

# Directory Handling

The file `dir.py` demonstrates directory operations.

Possible concepts:

- Current working directory
- Path creation
- Folder listing
- Navigation

Useful in distributed systems for:

- Log management
- File storage
- Dataset access

---

# File Handling

The file `file.py` demonstrates:

- Opening files
- Reading data
- Writing data
- Closing files

File handling is important in:

- Logging systems
- Data storage
- Result generation
- Input processing

---

# Control Flow

The file `flow.py` covers:

- if statements
- else statements
- nested conditions
- loops
- break
- continue

Flow control is essential for writing task logic.

---

# Lists in Python

The file `lists.py` explains list data structure.

Operations:

- append()
- remove()
- insert()
- pop()
- slicing
- iteration

Lists are used heavily in:

- Task queues
- Worker lists
- Job scheduling
- Result storage

---

# do_something.py

This file likely contains a common function used by multiple programs.

In threading or multiprocessing examples, functions are assigned as tasks.

Example:

- Sleep task
- Calculation task
- Print task

Reusable functions reduce duplication.

---

# serial_test.py

This program demonstrates sequential execution.

Tasks run one after another.

Used for comparison against:

- multithreading_test.py
- multiprocessing_test.py

Helps measure performance difference.

---

# multithreading_test.py

This file demonstrates thread creation.

Common steps:

1. Import threading
2. Define function
3. Create thread objects
4. Start threads
5. Join threads

Purpose:

Run tasks concurrently.

---

# multiprocessing_test.py

This file demonstrates process creation.

Common steps:

1. Import multiprocessing
2. Define target function
3. Create process objects
4. Start processes
5. Join processes

Purpose:

Achieve true parallel execution.

---

# thread_and_processes.py

This file compares both approaches.

Expected comparison:

- Execution time
- Resource usage
- Performance
- Use cases

---

# Why Concurrency Matters

Concurrency helps systems:

- Handle many users
- Serve web requests
- Download multiple files
- Process many tasks

Examples:

- Web browser tabs
- Video streaming
- Servers
- Banking apps

---

# CPU Bound vs I/O Bound Tasks

## CPU Bound Tasks

Require heavy computation.

Examples:

- Prime numbers
- Matrix multiplication
- Compression

Best solution:

Multiprocessing

## I/O Bound Tasks

Spend time waiting.

Examples:

- Reading files
- Downloading data
- Database requests

Best solution:

Multithreading

---

# Synchronization Concepts

When threads share data, issues occur:

- Race conditions
- Deadlocks
- Inconsistent results

Python tools:

- Lock
- Semaphore
- Event
- Queue

---

# Performance Measurement

Programs often compare time using:

```python
import time
