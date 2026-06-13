# Chapter 01: Foundations of Parallel Computing in Python

## Overview

Welcome to the **Parallel and Distributed Computing (PDC)** documentation for Chapter 01. This repository serves as the fundamental introduction to achieving high-performance execution in Python. 

This guide is designed for academic and professional study. It is strictly divided into two sections: **Part 1** covers the theoretical computer science concepts driving parallel architectures, and **Part 2** showcases the practical Python code implementations and their respective outputs.

---

## Table of Contents

### Part 1: Theoretical Foundations
1. [The Need for PDC](#1-the-need-for-pdc)
2. [Theoretical Architecture](#2-theoretical-architecture)
    - [Serial vs. Concurrent vs. Parallel](#serial-vs-concurrent-vs-parallel)
    - [The Memory Model: Threads vs. Processes](#the-memory-model-threads-vs-processes)
    - [The Global Interpreter Lock (GIL)](#the-global-interpreter-lock-gil)
3. [Academic Context & Key Takeaways](#3-academic-context--key-takeaways)

### Part 2: Practical Implementation
4. [Target Workload Analysis](#4-target-workload-analysis)
5. [Implementation Breakdown & Outputs](#5-implementation-breakdown--outputs)
    - [Serial Implementation](#serial-implementation)
    - [Multithreaded Implementation](#multithreaded-implementation)
    - [Multiprocessed Implementation](#multiprocessed-implementation)
6. [Foundation Modules](#6-foundation-modules)
7. [Execution Guide](#7-execution-guide)

---

# PART 1: THEORETICAL FOUNDATIONS

## 1. The Need for PDC

As modern software constraints evolve, the demand for **Parallel and Distributed Computing (PDC)** has become an industrial and scientific necessity for several key reasons:

- **The Plateau of Moore's Law & Dennard Scaling:** Historically, CPUs became naturally faster every generation via increased clock speeds and transistor density. However, thermal limitations have caused single-core clock frequencies to plateau (around 3.0GHz - 5.0GHz). Hardware manufacturers now scale *horizontally* (adding more cores). Software *must* be explicitly written in a parallel paradigm to leverage this multi-core architecture.
- **Big Data & Throughput Escalation:** Modern applications process massive payload volumes. Processing these terabytes of data sequentially across a single thread poses a critical bottleneck. PDC paradigms allow systems to fragment this data and process it concurrently, drastically reducing execution times.
- **Fault Tolerance & High Availability:** Particularly within Distributed Computing, redundancy is a core feature. If one hardware node experiences a critical failure, remaining clustered nodes can assume the computations—ensuring the application remains highly available.

---

## 2. Theoretical Architecture

Before diving into code, it is imperative to establish the theoretical definitions governing parallel execution.

### Serial vs. Concurrent vs. Parallel

```mermaid
graph TD
    subgraph Serial
        S1["Task 1 (Core 1)"] --> S2["Task 2 (Core 1)"]
        S2 --> S3["Task 3 (Core 1)"]
    end

    subgraph Multithreading
        T1["Thread 1 (Core 1)"] -.->|Context Switch| T2["Thread 2 (Core 1)"]
        T2 -.->|Context Switch| T3["Thread 3 (Core 1)"]
        T3 -.->|GIL locks| T1
    end

    subgraph Multiprocessing
        P1["Process 1 (Core 1)"]
        P2["Process 2 (Core 2)"]
        P3["Process 3 (Core 3)"]
    end
```

- **Serial Execution:** Instructions execute strictly sequentially. Task $N+1$ cannot commence until task $N$ has fully terminated. This guarantees determinism but underutilizes modern processors.
- **Concurrency (Multithreading):** The architectural illusion of simultaneous execution. The OS rapidly context-switches tasks on a single core. The system is dealing with multiple tasks at once, but not necessarily executing their instructions at the identical physical microsecond.
- **Parallelism (Multiprocessing):** True simultaneous execution. Multiple physical processing units (cores) execute independent tasks at the exact same physical microsecond.

### The Memory Model: Threads vs. Processes
- **Threads** exist within the boundary of a single operating system process. They share the same heap memory space. While this allows for extremely fast inter-thread communication, it introduces the severe risk of **race conditions**, necessitating synchronization (Mutexes, Semaphores).
- **Processes** are isolated execution environments. They do not share memory state by default. Inter-Process Communication (IPC) requires explicit mechanisms (pipes, queues), introducing higher latency.

### The Global Interpreter Lock (GIL)
> **Critical Architecture Constraint**
> The standard implementation of Python (CPython) utilizes the **Global Interpreter Lock (GIL)**. Because of the GIL, Python prevents multiple native threads from executing Python bytecodes simultaneously. 
> 
> Therefore, **Multithreading** is heavily bottlenecked for mathematical/CPU calculations. To utilize multiple cores for heavy math in Python, **Multiprocessing** (which spawns entirely new Python interpreters that bypass the GIL) is absolutely required.

---

## 3. Academic Context & Key Takeaways

Deriving metrics from parallel architectures yields practical demonstrations of core tenets:

1. **Amdahl’s Law:** A system will rarely achieve *perfect* linear speedup (e.g., 10 processes is not precisely 10x faster than serial). Latency overhead exists when initially spawning processes in memory, bounding theoretical speedup boundaries.
2. **Context Switching Overhead:** Because the GIL enforces sequential execution of threads on CPU-heavy workloads, an OS still attempts to context-switch them. This "thrashing" wastes CPU cycles, meaning a multithreaded script might actually run *slower* than a standard single-threaded serial script.

---
---

# PART 2: PRACTICAL IMPLEMENTATION

## 4. Target Workload Analysis

To benchmark performance, these scripts utilize a standardized workload located in `do_something.py`.

```python
def do_something(count, out_list):
    for i in range(count):
        out_list.append(random.random())
```
**Workload Behavior:** The function executes a tight loop. In each iteration, it runs the pseudo-random number generator and appends the float to a list. This represents a worst-case **CPU-Bound** scenario.

---

## 5. Implementation Breakdown & Outputs

The codebase executes the `do_something.py` workload 10 successive times across three distinct execution methodologies.

### Serial Implementation
**File:** `serial_test.py`

**Code Snippet:**
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

**Expected Output:**
```text
List processing complete.
serial time= 8.41101923...
```
*(Provides standard baseline determinism, utilizing only a single physical core).*

---

### Multithreaded Implementation
**File:** `multithreading_test.py`

**Code Snippet:**
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

**Expected Output:**
```text
List processing complete.
multithreading time= 8.52994012...
```
*(May execute slower than Serial due to context-switching thrashing and the Python GIL blocking parallelism).*

---

### Multiprocessed Implementation
**File:** `multiprocessing_test.py`

**Code Snippet:**
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

**Expected Output:**
```text
List processing complete.
multiprocesses time= 2.15822941...
```
*(Executes significantly faster due to bypassing the GIL and utilizing multiple physical machine cores).*

---

## 6. Foundation Modules
For students migrating from statically typed languages, the folder includes Python syntax refreshers:
- **`classes.py`**: Object-Oriented paradigms (self, __init__).
- **`lists.py`**: Dynamic arrays and indexing.
- **`flow.py`**: Control flow structures.
- **`dir.py` & `file.py`**: Filesystem I/O operations.

---

## 7. Execution Guide
To conduct the benchmark locally, execute the scripts sequentially via your terminal inside the `Chapter01` directory:

```bash
python serial_test.py
python multithreading_test.py
python multiprocessing_test.py
```
