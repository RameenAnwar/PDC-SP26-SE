# Parallel & Distributed Computing (PDC)
## Chapter 05: Asynchronous Programming and Task Pooling

## Course & Submission Details
- **Course Title:** Parallel and Distributed Computing (PDC)
- **Student Name:** Zaid Bhatti
- **Roll Number:** 23FA-014-SE
- **Chapter Focus:** Cooperative Multitasking and Asynchronous Execution Pools

---

## 1. Overview of Asynchronous Concurrency

Asynchronous programming is a concurrency design pattern that structures code around non-blocking execution paths. Unlike multithreading or multiprocessing, which rely on the operating system kernel scheduler to context-switch threads preemptively, asynchronous execution relies on **cooperative multitasking**.

This document reviews how to manage concurrency on a single thread using Python's `asyncio` module and how to integrate external worker pools.

---

## 2. Technical Discussion & Architectural Foundations

### Cooperative vs. Preemptive Multitasking
- **Preemptive Multitasking:** The operating system scheduler allocates CPU time slices to active threads and processes. It can interrupt execution at any point. This can lead to race conditions and lock contention.
- **Cooperative Multitasking:** Tasks run sequentially on a single thread and voluntarily yield control to a central loop at specified `await` checkpoints. This design eliminates context-switching overhead and thread-safety bugs on the main execution thread.

### The Event Loop Architecture
The event loop is the core driver of asynchronous execution. It runs continuously in a single thread, monitoring I/O tasks and timers:
- When a task awaits a network call, it yields control and registers a callback.
- The event loop executes other ready tasks in the queue.
- Once the underlying I/O completes, the task is marked as ready and scheduled to resume.

---

## 3. Coroutines, Tasks, and Futures

Python's `asyncio` library uses three core abstractions to manage asynchronous execution:

- **Coroutine:** A function defined using `async def`. Calling a coroutine returns a coroutine object. It only executes when scheduled on an event loop and driven using the `await` keyword.
- **Future:** A low-level object representing a result that has not yet been computed. Code can register callback hooks that fire when the future completes.
- **Task:** A subclass of `Future` that wraps a coroutine and registers it with the event loop, scheduling it to run in the background.

---

## 4. Task Pooling with Executors

While asynchronous programming is efficient for I/O-bound tasks, executing heavy, CPU-bound computations on the event loop will block the thread and stall the application. To prevent this, the `concurrent.futures` module allows offloading work to external pools:

- **ThreadPoolExecutor:** Spawns a pool of worker threads. This is useful for blocking I/O calls but is limited by the GIL for CPU-bound tasks.
- **ProcessPoolExecutor:** Spawns a pool of independent processes, each with its own Python interpreter. This allows true parallel execution for CPU-heavy tasks.

---

## 5. Practical Implementation Analysis

### Event Loop Scheduling (`asyncio_event_loop.py`)
This script schedules standard functions (`task_A`, `task_B`, `task_C`) to run sequentially on the event loop. Each task schedules the next using the loop's `call_later` method, yielding control for a random duration.

```python
import asyncio
import time
import random

def task_A(end_time, loop):
    print ("task_A called")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_B, end_time, loop)
    else:
        loop.stop()

def task_B(end_time, loop):
    print ("task_B called ")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_C, end_time, loop)
    else:
        loop.stop()

def task_C(end_time, loop):
    print ("task_C called")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_A, end_time, loop)
    else:
        loop.stop()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
end_loop = loop.time() + 60
loop.call_soon(task_A, end_loop, loop)
loop.run_forever()
loop.close()
```

---

### Finite State Machine (`asyncio_coroutine.py`)
This implementation uses coroutines to simulate transitions between states in a Finite State Machine (FSM). States are modeled as asynchronous functions. They utilize `await` to hand off execution dynamically to target states based on random variables.

```python
import asyncio
import time
from random import randint

async def start_state():
    print('Start State called\n')
    input_value = randint(0, 1)
    time.sleep(1)

    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)

    print('Resume of the Transition : \nStart State calling ' + result)
```

---

### Asyncio Futures (`asyncio_and_futures.py`)
This script demonstrates low-level `asyncio.Future` instantiation, binding computation tasks to future resolutions, and handling completions using callback hooks.

```python
import asyncio

async def first_coroutine(future, num):
    count = 0
    for i in range(1, num + 1):
        count += 1
    await asyncio.sleep(4)
    future.set_result('First coroutine (sum of N ints) result = %s' % count)

async def second_coroutine(future, num):
    count = 1
    for i in range(2, num + 1):
        count *= i
    await asyncio.sleep(4)
    future.set_result('Second coroutine (factorial) result = %s' % count)

def got_result(future):
    print(future.result())

async def main():
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    task1 = asyncio.create_task(first_coroutine(future1, 10))
    task2 = asyncio.create_task(second_coroutine(future2, 5))

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    await asyncio.wait([task1, task2])

asyncio.run(main())
```

---

### Parallel Tasks (`asyncio_task_manipulation.py`)
This program wraps coroutines doing factorial, fibonacci, and binomial coefficient calculations into concrete `asyncio.Task` instances. It executes them concurrently and handles state synchronization via `asyncio.wait()`.

```python
import asyncio

async def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        print('Asyncio.Task: Compute factorial(%s)' % i)
        await asyncio.sleep(1)
        fact *= i
    print('Asyncio.Task - factorial(%s) = %s' % (number, fact))
```

---

### Pooling Benchmarks (`concurrent_futures_pooling.py`)
This script executes CPU-bound mathematical operations sequentially, then uses a `ThreadPoolExecutor`, and finally a `ProcessPoolExecutor` to benchmark execution performance.

```python
import concurrent.futures
import time

number_list = list(range(1, 11))

def count(number):
    for i in range(0,10000000):
        i += 1
    return i*number

def evaluate(item):
    result_item = count(item)
    print('Item %s, result %s' % (item, result_item))
```

**Expected Performance Patterns:**
- **Sequential:** Standard execution time using 1 core.
- **Thread Pool:** Similar speed to sequential execution. The CPU-bound tasks block the threads, and the GIL limits execution to a single core.
- **Process Pool:** Executes much faster by distributing the tasks across 5 distinct OS processes, utilizing multiple CPU cores.

---

## 6. Local Execution Guide

To execute these scripts, navigate to the `Chapter05` directory and run them using standard Python:

```bash
python asyncio_event_loop.py
python asyncio_coroutine.py
python asyncio_and_futures.py
python asyncio_task_manipulation.py
python concurrent_futures_pooling.py
```
