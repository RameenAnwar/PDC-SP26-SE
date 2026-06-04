# Chapter 03: Process-Based Parallelism

## Preface

Welcome to the academic documentation for Chapter 03 of the Parallel and Distributed Computing (PDC) course. This chapter covers **Multiprocessing** in Python, focusing on how to run independent processes to bypass the Global Interpreter Lock (GIL) and utilize multi-core processors.

This guide is divided into two sections: Section 1 explores the OS-level process management and communication theory, and Section 2 reviews the practical Python scripts and their execution outputs.

---

## Index of Topics

### Section 1: Multiprocessing Architecture
1. [The Multiprocessing Paradigm](#1-the-multiprocessing-paradigm)
2. [Operating System Process Management](#2-operating-system-process-management)
    - [Subclassing and Workers](#subclassing-and-workers)
    - [Process Pools](#process-pools)
    - [Daemon Processes](#daemon-processes)
3. [Inter-Process Communication (IPC) Mechanisms](#3-inter-process-communication-ipc-mechanisms)
    - [OS Pipes](#os-pipes)
    - [Process Barriers](#process-barriers)
    - [Process Termination Control](#process-termination-control)

### Section 2: Implementation & Code Benchmarks
4. [Basic Process Spawning](#4-basic-process-spawning)
5. [Configuring Background Daemons](#5-configuring-background-daemons)
6. [Worker Recycling with Pools](#6-worker-recycling-with-pools)
7. [IPC via Bidirectional Pipes](#7-ipc-via-bidirectional-pipes)
8. [Barrier Synchronization](#8-barrier-synchronization)
9. [Forceful Process Termination](#9-forceful-process-termination)
10. [Local Execution Guide](#10-local-execution-guide)

---

# SECTION 1: MULTIPROCESSING ARCHITECTURE

## 1. The Multiprocessing Paradigm

Unlike multithreading, which executes concurrent execution paths inside a shared process space, multiprocessing spawns completely isolated operating system processes. Each spawned process runs its own independent instance of the Python interpreter, maintains its own private memory space, and has its own Global Interpreter Lock (GIL).

This isolation provides two major advantages:
- **GIL Bypass:** Since each process runs its own CPython interpreter, they can execute bytecode in parallel across multiple CPU cores without being blocked by a single global lock.
- **Fault Isolation:** A crash or segmentation fault in one child process does not corrupt the memory space or cause the termination of the parent process.

However, this architecture introduces higher memory usage and startup latency compared to threads.

## 2. Operating System Process Management

Managing multiple processes efficiently requires using structured patterns provided by the operating system kernel and Python's `multiprocessing` library.

### Subclassing and Workers

Similar to threads, custom process behaviors can be defined by inheriting from `multiprocessing.Process` and overriding the `run()` method. This allows developers to wrap complex state and execution logic into reusable process-oriented objects.

### Process Pools

Spawning and destroying operating system processes is resource-intensive. To reduce this overhead, the `Pool` class maintains a set of pre-allocated worker processes. Instead of spawning a process for every task, workloads are queued and distributed among these active workers, optimizing CPU utilization.

### Daemon Processes

A daemon process is a child process that runs in the background. In Python, the main program waits for all non-daemon child processes to finish before exiting. If a child process is configured as a daemon, it will be forcefully terminated by the operating system the moment the main parent process completes.

## 3. Inter-Process Communication (IPC) Mechanisms

Since processes run in isolated memory spaces, they cannot share data directly. Instead, they must use explicit Inter-Process Communication (IPC) mechanisms.

### OS Pipes

A Pipe is a basic communication channel that connects two processes. It consists of two connection endpoints, allowing bidirectional data transfer. When a process sends a Python object through one end, the library serializes (pickles) the object and writes it to the pipe, where it is read and deserialized by the receiver.

### Process Barriers

A Barrier is a synchronization primitive used to coordinate the execution of a fixed number of processes. The barrier is initialized with a target count $N$. Processes arriving at the barrier block until all $N$ processes have reached it. Once the target count is reached, all waiting processes are unblocked simultaneously.

### Process Termination Control

Managing processes requires the ability to handle hung or unresponsive workers. While processes should ideally exit cleanly when their task is done, the parent process can send a SIGTERM signal to forcefully terminate a child process using the `terminate()` method.

---

# SECTION 2: IMPLEMENTATION & CODE BENCHMARKS

## 4. Basic Process Spawning

**Script name:** `spawning_processes.py`

This script demonstrates spawning multiple independent processes to run a target function concurrently.

```python
import multiprocessing

def myFunc(i):
    print(f'calling myFunc from process n°: {i}')

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()
```

**Expected Console Output:**
```text
calling myFunc from process n°: 0
calling myFunc from process n°: 1
...
calling myFunc from process n°: 5
```

Using `join()` ensures each process completes before the next one starts in this sequence.

---

## 5. Configuring Background Daemons

**Script name:** `run_background_processes.py`

This script demonstrates configuring a background daemon process that is automatically killed when the parent exits.

```python
import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Exiting {name}")

if __name__ == '__main__':
    background_process = multiprocessing.Process(name='background_process', target=foo)
    background_process.daemon = True
    background_process.start()
```

**Expected Console Output:**
```text
Starting background_process
```

Since the parent process finishes immediately and the child is a daemon, the child is terminated before it can print "Exiting background_process".

---

## 6. Worker Recycling with Pools

**Script name:** `process_pool.py`

This script uses a process pool to distribute a collection of mathematical tasks across 4 reusable worker processes.

```python
import multiprocessing

def function_square(data):
    return data * data

if __name__ == '__main__':
    inputs = list(range(0, 100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)
    pool.close() 
    pool.join()  
    print(f'Pool outputs: {pool_outputs}')
```

**Expected Console Output:**
```text
Pool outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81...]
```

The pool handles task distribution and worker recycling internally.

---

## 7. IPC via Bidirectional Pipes

**Script name:** `communicating_with_pipe.py`

This script demonstrates using a pipe to send data between processes.

```python
import multiprocessing

def create_items(pipe):
    output_pipe, _ = pipe
    for item in range(10):
        output_pipe.send(item)
    output_pipe.close()

def multiply_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            item = input_pipe.recv()
            output_pipe.send(item * item)
    except EOFError:
        output_pipe.close()

if __name__== '__main__':
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(target=create_items, args=(pipe_1,))
    process_pipe_1.start()
```

---

## 8. Barrier Synchronization

**Script name:** `processes_barrier.py`

This script coordinates multiple processes using a `Barrier`, ensuring they pass a synchronization point together.

```python
import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s ----> %s" %(name, datetime.fromtimestamp(now)))
```

**Expected Console Output:**
```text
process p3 - test_without_barrier ----> 2026-06-04 22:31:12.482019
process p1 - test_with_barrier ----> 2026-06-04 22:31:12.498112
process p2 - test_with_barrier ----> 2026-06-04 22:31:12.498112
```

---

## 9. Forceful Process Termination

**Script name:** `killing_processes.py`

This script demonstrates forcefully terminating an active process using the `terminate()` method.

```python
import multiprocessing
import time

def foo():
    print('Starting function')
    for i in range(10):
        time.sleep(1)

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    p.start()
    p.terminate()
    p.join()
    print('Process exit code:', p.exitcode)
```

**Expected Console Output:**
```text
Process exit code: -15
```

The exit code of `-15` indicates that the process was terminated by a SIGTERM signal.

---

## 10. Local Execution Guide

To run these multiprocessing tests, navigate to the `Chapter03` directory in your terminal and execute:

```bash
python spawning_processes.py
python run_background_processes.py
python process_pool.py
python communicating_with_pipe.py
python processes_barrier.py
python killing_processes.py
```
