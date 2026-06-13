# Parallel & Distributed Computing (PDC)
## Chapter 01: Core Concepts of Parallel Computing

## Course & Submission Details
- **Course Title:** Parallel and Distributed Computing (PDC)
- **Student Name:** Zaid Bhatti
- **Roll Number:** 23FA-014-SE
- **Chapter Focus:** Fundamentals of Parallelism, Concurrency, and CPython Execution Models

---

## 1. Overview of Computational Paradigms

In modern computing, optimizing the execution speed of software applications has transitioned from single-core performance scaling to multi-core utilization. This document reviews the foundational computing models of sequential execution, concurrent multithreading, and parallel multiprocessing in Python.

Understanding these paradigms is essential for building high-performance systems that efficiently distribute computational loads across available CPU hardware.

---

## 2. Technical Discussion & Architectural Foundations

### Sequential Execution Model
Sequential execution is the traditional programming model where instructions are executed one after the other in a single execution thread. Each statement must wait for the preceding one to finish. 
- **Advantage:** Simplicity. It is deterministic, easy to debug, and free of concurrency bugs like deadlocks or race conditions.
- **Disadvantage:** Inability to utilize multi-core processors, resulting in idle hardware during CPU-heavy tasks.

### Threading (Shared Memory Concurrency)
A thread is the smallest unit of execution that an operating system can schedule. In a multithreaded model, multiple threads run within the memory space of a single parent process, sharing the heap memory, global variables, and open file descriptors.
- **Advantage:** Low memory footprint and fast communication since threads share memory directly.
- **Disadvantage:** Python's Global Interpreter Lock (GIL) limits performance on CPU-bound tasks, and sharing memory introduces risks like data corruption and race conditions.

### Multiprocessing (Isolated Memory Parallelism)
Multiprocessing runs separate processes, each with its own virtual memory space, file descriptor tables, and independent Python interpreter.
- **Advantage:** True parallel execution on multi-core systems, bypassing the GIL for CPU-bound tasks.
- **Disadvantage:** Higher memory overhead and the need for explicit Inter-Process Communication (IPC) to share data.

---

## 3. CPython's Global Interpreter Lock (GIL)

In the standard implementation of Python (CPython), execution is regulated by the Global Interpreter Lock (GIL). The GIL is a mutex that prevents multiple threads from executing Python bytecode simultaneously.

### The Purpose of the GIL
CPython's memory management is not thread-safe. It uses reference counting to track objects and clean up memory. Without the GIL, concurrent threads could modify reference counts at the same time, leading to memory leaks or premature deallocation.

### Impact on Performance
Because of the GIL:
- **CPU-bound tasks** (e.g., heavy mathematical operations) do not run faster with multithreading. Instead, context-switching overhead can make them run slower than sequential execution.
- **I/O-bound tasks** (e.g., web requests or file operations) benefit from multithreading because threads yield the GIL while waiting for external resources.

For CPU-bound tasks, multiprocessing is required to achieve true parallel execution across multiple CPU cores.

---

## 4. Empirical Performance Benchmarks

To evaluate these execution models, we use a standard CPU-bound task defined in `do_something.py` that generates a large list of random numbers.

### Shared Utility Workload (`do_something.py`)
```python
import random

def do_something(count, out_list):
    for i in range(count):
        out_list.append(random.random())
```

---

### Sequential Benchmark (`serial_test.py`)
This script runs the target workload 10 times in sequence on a single thread.

```python
import time
from do_something import *

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   
    n_exec = 10
    
    for i in range(0, n_exec):
        out_list = list()
        do_something(size, out_list)
        
    print ("List processing complete.")
    end_time = time.time()
    print("serial time=", end_time - start_time)
```

**Expected Console Output:**
```text
List processing complete.
serial time= 8.45019381...
```

The script runs sequentially, using only one CPU core while the other cores remain idle.

---

### Multithreaded Benchmark (`multithreading_test.py`)
This script attempts to run the workload concurrently by spawning 10 separate threads.

```python
from do_something import *
import time
import threading

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000
    threads = 10  
    jobs = []
    
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=do_something(size, out_list))
        jobs.append(thread)
        
    for j in jobs:
        j.start()
        
    for j in jobs:
        j.join()

    print ("List processing complete.")
    end_time = time.time()
    print("multithreading time=", end_time - start_time)
```

**Expected Console Output:**
```text
List processing complete.
multithreading time= 8.6102931...
```

Due to the GIL, the threads cannot run in parallel. The overhead of context switching can make the threaded version run slower than the sequential baseline.

---

### Multiprocessing Benchmark (`multiprocessing_test.py`)
This script bypasses the GIL by spawning 10 independent operating system processes, allowing true parallel execution.

```python
from do_something import *
import time
import multiprocessing

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   
    procs = 10   
    jobs = []
    
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process\
                  (target=do_something,args=(size,out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print ("List processing complete.")
    end_time = time.time()
    print("multiprocesses time=", end_time - start_time)
```

**Expected Console Output:**
```text
List processing complete.
multiprocesses time= 2.2104928...
```

By using multiple CPU cores simultaneously, the execution time is reduced, demonstrating the benefit of multiprocessing for CPU-bound tasks.

---

## 5. Basic Syntax Reference Files

For students reviewing Python syntax, the following introductory files are included in the repository:

- **`classes.py`**: Explains object-oriented programming in Python.
- **`lists.py`**: Demonstrates list manipulation and operations.
- **`flow.py`**: Covers conditional statements and loops.
- **`dir.py` & `file.py`**: Explains basic file system and I/O operations.

---

## 6. Local Execution Guide

To run these tests, open your terminal and execute the scripts inside the `Chapter01` folder in the following order:

```bash
python serial_test.py
python multithreading_test.py
python multiprocessing_test.py
python classes.py
python lists.py
python flow.py
python file.py
python dir.py
```
