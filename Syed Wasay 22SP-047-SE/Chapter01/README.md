# Chapter 01: Core Paradigms of Parallel Processing

## Preface

Welcome to the academic documentation for Chapter 01 of the Parallel and Distributed Computing (PDC) course. This study guide focuses on the fundamental concepts of parallel execution models in Python, explaining how modern CPU architectures are utilized to optimize program runtime.

This document is organized into two primary sections: Section 1 explores the underlying computer architecture and theory, and Section 2 breaks down the code implementations and their performance analysis.

---

## Index of Topics

### Section 1: Architectural Foundations
1. [The Growth of Parallel Computing](#1-the-growth-of-parallel-computing)
2. [Concurrency vs. Parallelism](#2-concurrency-vs-parallelism)
3. [The Memory Model & GIL Constraints](#3-the-memory-model--gil-constraints)
4. [Amdahl's Law and Performance Overhead](#4-amdahls-law-and-performance-overhead)

### Section 2: Empirical Benchmarks
5. [Standardized Benchmark Workload](#5-standardized-benchmark-workload)
6. [Sequential execution analysis](#6-sequential-execution-analysis)
7. [Threaded execution analysis](#7-threaded-execution-analysis)
8. [Process-based execution analysis](#8-process-based-execution-analysis)
9. [Basic Syntax Refreshers](#9-basic-syntax-refreshers)
10. [Local Execution Guide](#10-local-execution-guide)

---

# SECTION 1: ARCHITECTURAL FOUNDATIONS

## 1. The Growth of Parallel Computing

Historically, CPU performance scaled reliably by increasing the clock frequency and increasing the density of transistors on a single core. This trend, famously described by Moore's Law and Dennard Scaling, allowed sequential software programs to run faster without major architectural redesigns. However, physical constraints, such as high power consumption and thermal dissipation issues, eventually stopped the rise of clock rates. 

To continue improving performance, modern chip manufacturers shifted to horizontal scaling, putting multiple processing cores on a single chip. This structural change means that software must be explicitly designed for parallel execution to utilize the available hardware. In Parallel and Distributed Computing, we study how to partition a single application's workload so that multiple cores can work on it at the same time, reducing execution time.

## 2. Concurrency vs. Parallelism

It is important to distinguish between concurrency and parallelism, as they represent different execution models:

- **Concurrency** is the design technique of structuring a program to handle multiple tasks by interleaving their execution. In a concurrent model, the operating system kernel context-switches between different tasks on a single processing unit. This gives the illusion of simultaneous execution, but at any given microsecond, only one task is actively running.
- **Parallelism** is the physical execution of multiple tasks at the exact same time. This requires multiple physical cores or processors, where each core independently runs a distinct instruction stream.

While concurrency focuses on task structuring, parallelism focuses on hardware utilization.

## 3. The Memory Model & GIL Constraints

To understand how Python implements these concepts, we must analyze its execution model:

- **Threads** are light execution units within a single operating system process. All threads created by a process share its address space, heap memory, and open file descriptors. This shared memory allows threads to communicate quickly, but it introduces the risk of data corruption due to race conditions.
- **Processes** are fully isolated execution environments. Each process has its own address space, memory heap, and isolated system resources. Since processes do not share memory by default, they must use explicit Inter-Process Communication (IPC) mechanisms, which have higher overhead than thread communication.

In standard Python (CPython), execution is limited by the Global Interpreter Lock (GIL). The GIL is a mutual exclusion lock that ensures only one thread can execute Python bytecode at a time. This prevents CPU-bound threads from running in parallel, even on multi-core systems. To achieve true parallel execution on CPU-bound workloads, we must spawn multiple independent processes, each with its own interpreter and GIL.

## 4. Amdahl's Law and Performance Overhead

Spawning processes introduces performance trade-offs, which are governed by Amdahl's Law. This mathematical formula defines the theoretical speedup limit of a program:

$$\text{Speedup} = \frac{1}{(1 - P) + \frac{P}{S}}$$

Where $P$ is the parallelizable portion of the program, and $S$ is the speedup factor of that portion. 

In practice, starting and managing processes introduces operating system overhead, such as allocating memory spaces, copying data structures, and context switching. As a result, if the parallel workload is too small, the overhead of managing the processes can exceed the performance gains, making the program run slower than sequential execution.

---

# SECTION 2: EMPIRICAL BENCHMARKS

## 5. Standardized Benchmark Workload

To evaluate the execution models, a CPU-bound workload is defined in `do_something.py`. This workload generates random numbers and appends them to a list, simulating heavy computational tasks:

```python
import random

def do_something(count, out_list):
    for i in range(count):
        out_list.append(random.random())
```

This workload is executed 10 times across three different testing scripts.

---

## 6. Sequential execution analysis

**Script name:** `serial_test.py`

This script executes the workload sequentially on a single thread. It serves as the baseline for our performance tests.

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

## 7. Threaded execution analysis

**Script name:** `multithreading_test.py`

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

Due to the Global Interpreter Lock (GIL), the threads cannot run in parallel. Instead, they share a single core, and the overhead of context switching can make the threaded version run slower than the sequential baseline.

---

## 8. Process-based execution analysis

**Script name:** `multiprocessing_test.py`

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

## 9. Basic Syntax Refreshers

For students reviewing Python syntax, the following introductory files are included in the repository:

- **`classes.py`**: Outlines basic object-oriented programming, including class structures, attributes, and instance methods:
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      def display(self):
          print(f"Stored value is: {self.value}")
  ```
- **`lists.py`**: Demonstrates dynamic array operations, slice notation, and common methods.
- **`flow.py`**: Explains control flow structures, conditional branches, and loops.
- **`dir.py` & `file.py`**: Covers basic file input/output and directory management.

---

## 10. Local Execution Guide

To run these tests on your local machine, open your terminal and run the scripts in the following order inside the `Chapter01` folder:

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
