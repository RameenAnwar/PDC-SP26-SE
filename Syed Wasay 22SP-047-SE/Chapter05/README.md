# Chapter 05: Asynchronous I/O and Concurrent Execution Pools

## Preface

Welcome to the academic documentation for Chapter 05 of the Parallel and Distributed Computing (PDC) course. This chapter moves beyond traditional thread and process models to explore **asynchronous programming** and **executor-based concurrency** using Python's `asyncio` and `concurrent.futures` libraries.

Where Chapters 02 and 03 relied on preemptive multitasking managed by the operating system kernel, this chapter explores **cooperative multitasking**, where tasks voluntarily yield control to a central event loop. This approach is highly efficient for I/O-bound workloads and supports combining async flow with multi-core parallelism through executor pools.

---

## Index of Topics

### Section 1: Asynchronous Programming Theory
1. [Cooperative vs. Preemptive Multitasking](#1-cooperative-vs-preemptive-multitasking)
2. [The Event Loop Execution Model](#2-the-event-loop-execution-model)
3. [Coroutines, Futures, and Tasks](#3-coroutines-futures-and-tasks)
4. [Executor Pools for CPU-Bound Work](#4-executor-pools-for-cpu-bound-work)

### Section 2: Code Implementations
5. [Scheduling Callbacks on the Event Loop](#5-scheduling-callbacks-on-the-event-loop)
6. [Finite State Machine with Coroutines](#6-finite-state-machine-with-coroutines)
7. [Futures and Callback Hooks](#7-futures-and-callback-hooks)
8. [Concurrent Task Scheduling](#8-concurrent-task-scheduling)
9. [Executor Pool Benchmarks](#9-executor-pool-benchmarks)
10. [Local Execution Guide](#10-local-execution-guide)

---

# SECTION 1: ASYNCHRONOUS PROGRAMMING THEORY

## 1. Cooperative vs. Preemptive Multitasking

In **preemptive multitasking**, the operating system scheduler decides when to interrupt running tasks and switch to another. This approach is powerful but introduces overhead from context switching and memory protection requirements.

In **cooperative multitasking**, each task is responsible for voluntarily yielding control back to the event loop scheduler. This happens at explicit `await` checkpoints in the code. Since tasks share a single thread, no locks are required for memory protection, and context switching is cheaper than OS-level thread switching.

The trade-off is that if a task performs a long CPU-bound computation without awaiting, it blocks all other tasks from progressing — the entire event loop stalls.

## 2. The Event Loop Execution Model

The event loop is the core engine of asynchronous programming. It continuously monitors a queue of ready tasks and executes them one at a time:

1. A task runs until it hits an `await` expression.
2. The `await` registers a callback with the OS I/O selector and suspends the task.
3. The event loop immediately picks the next ready task from the queue.
4. When the I/O operation completes, the OS notifies the selector, and the suspended task is re-queued.

This allows thousands of I/O-bound operations (like HTTP requests) to be managed concurrently on a single thread without blocking.

## 3. Coroutines, Futures, and Tasks

Three core abstractions power Python's asynchronous model:

- **Coroutine:** A function declared with `async def`. Calling it returns a coroutine object. The body only executes when driven by an event loop. The `await` keyword suspends the coroutine at a checkpoint, allowing the event loop to run other tasks.

- **Future:** A low-level placeholder object representing a computation that has not yet completed. It transitions from `PENDING` to either `RESULT_SET` or `EXCEPTION_SET`. Code can attach callbacks that execute automatically once the future resolves.

- **Task:** A high-level wrapper that schedules a coroutine on the running event loop as a concurrent unit of work. Tasks are subclasses of `Future`, meaning they can also have callbacks and be `await`-ed.

## 4. Executor Pools for CPU-Bound Work

Since CPU-intensive logic stalls the single-threaded event loop, Python provides executor pools to offload such work:

- **ThreadPoolExecutor:** Manages a pool of operating system threads. Because the GIL restricts true parallelism, this is best suited for I/O-bound blocking calls (database queries, file access) rather than heavy computation.

- **ProcessPoolExecutor:** Manages a pool of independent OS processes. Each process has its own interpreter and GIL, enabling genuine CPU parallelism across multiple cores. Suitable for heavy numerical computation, though IPC serialization adds some overhead.

Both executors integrate with `asyncio` via `loop.run_in_executor()`, returning a Future that the event loop can await without blocking.

---

# SECTION 2: CODE IMPLEMENTATIONS

## 5. Scheduling Callbacks on the Event Loop

**Script name:** `asyncio_event_loop.py`

This script uses `call_later()` to schedule non-coroutine callback functions on the event loop, creating a chain of task transitions controlled by elapsed time.

```python
import asyncio
import time
import random

def task_A(end_time, loop):
    print("task_A called")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_B, end_time, loop)
    else:
        loop.stop()

def task_B(end_time, loop):
    print("task_B called")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_C, end_time, loop)
    else:
        loop.stop()

def task_C(end_time, loop):
    print("task_C called")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_A, end_time, loop)
    else:
        loop.stop()

loop = asyncio.new_event_loop()
end_loop = loop.time() + 60
loop.call_soon(task_A, end_loop, loop)
loop.run_forever()
loop.close()
```

**Expected Console Output:**
```text
task_A called
task_B called
task_C called
task_A called
...
```

Execution continues rotating through A → B → C until the 60-second budget is exhausted.

---

## 6. Finite State Machine with Coroutines

**Script name:** `asyncio_coroutine.py`

This script models a Finite State Machine (FSM) using coroutines. Each state is an `async def` function. Based on a random integer, execution `await`s transitions into the appropriate next state, simulating non-deterministic behavior.

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
    print('Resume of the Transition:\nStart State calling ' + result)

async def state1(transition_value):
    output_value = 'State 1 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    time.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)
    return output_value + 'State 1 calling %s' % result
```

**Expected Console Output:**
```text
Finite State Machine simulation with Asyncio Coroutine
Start State called

...evaluating...
...evaluating...
...stop computation...
Resume of the Transition:
Start State calling State 1 with transition value = 1
```

---

## 7. Futures and Callback Hooks

**Script name:** `asyncio_and_futures.py`

This script creates two `asyncio.Future` objects, associates coroutines with them as tasks, and registers `done_callback` hooks to print results when each future resolves.

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
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)
    await asyncio.wait([
        asyncio.create_task(first_coroutine(future1, 10)),
        asyncio.create_task(second_coroutine(future2, 5))
    ])

asyncio.run(main())
```

**Expected Console Output:**
```text
First coroutine (sum of N ints) result = 10
Second coroutine (factorial) result = 120
```

Both results print simultaneously after ~4 seconds, demonstrating concurrent event loop execution.

---

## 8. Concurrent Task Scheduling

**Script name:** `asyncio_task_manipulation.py`

This script wraps three mathematical coroutines — factorial, fibonacci, and binomial coefficient — as concurrent `asyncio.Task` objects, running them interleaved on the event loop.

```python
import asyncio

async def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        print('Asyncio.Task: Compute factorial(%s)' % i)
        await asyncio.sleep(1)
        fact *= i
    print('Asyncio.Task - factorial(%s) = %s' % (number, fact))

async def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print('Asyncio.Task: Compute fibonacci(%s)' % i)
        await asyncio.sleep(1)
        a, b = b, a + b
    print('Asyncio.Task - fibonacci(%s) = %s' % (number, a))

async def main():
    task_list = [
        asyncio.create_task(factorial(10)),
        asyncio.create_task(fibonacci(10))
    ]
    await asyncio.wait(task_list)

asyncio.run(main())
```

**Expected Console Output:**
```text
Asyncio.Task: Compute factorial(2)
Asyncio.Task: Compute fibonacci(0)
Asyncio.Task: Compute factorial(3)
Asyncio.Task: Compute fibonacci(1)
...
Asyncio.Task - factorial(10) = 3628800
Asyncio.Task - fibonacci(10) = 55
```

The output interleaves each iteration, as both tasks cooperatively yield at every `await asyncio.sleep(1)`.

---

## 9. Executor Pool Benchmarks

**Script name:** `concurrent_futures_pooling.py`

This benchmark runs a CPU-intensive counting function sequentially, then through a thread pool, then through a process pool, demonstrating the performance impact of each approach.

```python
import concurrent.futures
import time

number_list = list(range(1, 11))

def count(number):
    for i in range(0, 10000000):
        i += 1
    return i * number

def evaluate(item):
    result_item = count(item)
    print('Item %s, result %s' % (item, result_item))

if __name__ == '__main__':
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print("Thread Pool time: %.2f" % (time.time() - start))

    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print("Process Pool time: %.2f" % (time.time() - start))
```

**Expected Performance:**
```text
Thread Pool time: ~6.4 seconds  (GIL limits to 1 core)
Process Pool time: ~1.8 seconds (5 cores utilized in parallel)
```

The `ProcessPoolExecutor` distributes work across independent processes, each running on a separate CPU core, delivering a significant speedup over the thread pool for CPU-bound tasks.

---

## 10. Local Execution Guide

Navigate to the `Chapter05` directory and run each script using standard Python:

```bash
python asyncio_event_loop.py
python asyncio_coroutine.py
python asyncio_and_futures.py
python asyncio_task_manipulation.py
python concurrent_futures_pooling.py
```
