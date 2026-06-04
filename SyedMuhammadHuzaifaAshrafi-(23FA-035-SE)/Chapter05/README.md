# Chapter 5: Asynchronous Programming

> **Comprehensive Theory and Practical Implementation Guide**
> This chapter focuses on asynchronous programming patterns in Python. It covers the high-level `concurrent.futures` module for executing code using pools of threads or processes, and explores `asyncio` for single-threaded cooperative multitasking, covering event loops, coroutines, task scheduling, and futures coordination.

---

## Table of Contents
1. [Using the `concurrent.futures` Python module](#1-using-the-concurrentfutures-python-module)
2. [Managing the event loop with `asyncio`](#2-managing-the-event-loop-with-asyncio)
3. [Handling coroutines with `asyncio`](#3-handling-coroutines-with-asyncio)
4. [Manipulating tasks with `asyncio`](#4-manipulating-tasks-with-asyncio)
5. [Dealing with `asyncio` and futures](#5-dealing-with-asyncio-and-futures)

---

## 1. Using the `concurrent.futures` Python module

### Getting ready
The `concurrent.futures` module provides a high-level interface for asynchronously executing callables in Python. It abstracts the complexity of managing threads and processes, allowing developers to implement concurrency patterns through simple, intuitive APIs. The module offers two primary executor classes:
- **ThreadPoolExecutor**: Optimized for I/O-bound tasks such as network requests, file operations, or database queries, where tasks spend time waiting for external resources.
- **ProcessPoolExecutor**: Designed for CPU-bound tasks like heavy computations or data processing, as it bypasses Python's Global Interpreter Lock (GIL) by using separate processes.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#2196F3', 'primaryColor': '#FFFFFF', 'clusterBkg':'#F5F5F5' }}}%%
flowchart TD
    %% concurrent.futures Architecture
    classDef client fill:#E3F2FD,stroke:#1E88E5,stroke-width:3px,color:#0D47A1,font-weight:bold,rx:8,ry:8
    classDef executor fill:#FFF3E0,stroke:#FB8C00,stroke-width:3px,color:#E65100,font-weight:bold,rx:8,ry:8
    classDef pool fill:#EDE7F6,stroke:#5E35B1,stroke-width:2px,color:#311B92,font-weight:bold,rx:5,ry:5
    classDef future fill:#E8F5E9,stroke:#4CAF50,stroke-width:2px,color:#1B5E20,font-weight:bold,rx:5,ry:5

    A["[Client Application] \n Submits Callables (Tasks 1..N)"] --> B{"concurrent.futures \n Executor Interface"}
    
    B -->|Instantiates| C["ThreadPoolExecutor \n (I/O-Bound Work)"]
    B -->|Instantiates| D["ProcessPoolExecutor \n (CPU-Bound Work)"]
    
    C -->|Spawns| E["Worker Threads \n (Shared Memory Space)"]
    D -->|Spawns| F["Worker Processes \n (Isolated Memory / GIL Bypass)"]
    
    B -->|Returns instantly| G(("Future Objects \n (Holds Pending Results)"))
    
    G -->|"as_completed() / result()"| H["Client retrieves outputs"]

    class A client
    class B,C,D executor
    class E,F pool
    class G future
```

### How to do it...
To use this module, you start by creating an executor instance. Tasks are then submitted to the executor using the `submit()` method, which returns a Future object representing the pending result. Alternatively, the `map()` method can be used to apply a function across an iterable of inputs. Results can be retrieved by calling `result()` on the Future, or by iterating over futures using `as_completed()` to process them in the order they finish, rather than the order they were submitted.

**Example implementation ([concurrent_futures_pooling.py](Codes/concurrent_futures_pooling.py)):**
```python
import concurrent.futures
import time

number_list = list(range(1, 11))


def count(number):
    for i in range(0, 10_000_000):
        i += 1
    return i * number


def evaluate(item):
    result_item = count(item)
    print(f'Item {item}, result {result_item}')
    return result_item


if __name__ == '__main__':

    # -------------------------
    # Sequential Execution
    # -------------------------
    start_time = time.perf_counter()

    for item in number_list:
        evaluate(item)

    print('Sequential Execution in', time.perf_counter() - start_time, 'seconds')


    # -------------------------
    # Thread Pool Execution
    # -------------------------
    start_time = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate, item) for item in number_list]

        for f in concurrent.futures.as_completed(futures):
            f.result()

    print('Thread Pool Execution in', time.perf_counter() - start_time, 'seconds')


    # -------------------------
    # Process Pool Execution
    # -------------------------
    start_time = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate, item) for item in number_list]

        for f in concurrent.futures.as_completed(futures):
            f.result()

    print('Process Pool Execution in', time.perf_counter() - start_time, 'seconds')
```

### How it works...
When a task is submitted, the executor places it in an internal queue managed by worker threads or processes. The Future object acts as a placeholder that tracks the task's state—pending, running, completed, or cancelled—and holds the eventual result or exception. The `as_completed()` function yields futures as they complete, enabling responsive handling of results without waiting for all tasks to finish. Executors automatically manage worker lifecycle, resource cleanup, and exception propagation.

### There's more...
- The `max_workers` parameter allows you to control the level of parallelism based on your system's capabilities and task characteristics.
- Exceptions raised within tasks are captured by the Future and can be accessed via the `exception()` method, preventing unhandled errors from crashing the program.
- Tasks can be cancelled using the `cancel()` method, though cancellation only succeeds if the task has not yet started executing.
- For advanced coordination, `concurrent.futures.wait()` supports conditions like `FIRST_COMPLETED` or `ALL_COMPLETED` to synchronize multiple futures.

### See also
- Official Python documentation for `concurrent.futures`
- The `threading` and `multiprocessing` modules for lower-level concurrency control
- The `asyncio` module for single-threaded cooperative concurrency

**Output:**
```text
Sequential Execution:
Item 1, result 10000000
Item 2, result 20000000
Item 3, result 30000000
Item 4, result 40000000
Item 5, result 50000000
Item 6, result 60000000
Item 7, result 70000000
Item 8, result 80000000
Item 9, result 90000000
Item 10, result 100000000
Sequential Execution in 8.66234329999861 seconds

Thread Pool Execution:
Item 5, result 50000000
Item 1, result 10000000
Item 4, result 40000000
Item 2, result 20000000
Item 3, result 30000000
Item 7, result 70000000
Item 6, result 60000000
Item 8, result 80000000
Item 9, result 90000000
Item 10, result 100000000
Thread Pool Execution in 8.865503599998192 seconds

Process Pool Execution:
Item 5, result 50000000
Item 1, result 10000000
Item 4, result 40000000
Item 2, result 20000000
Item 3, result 30000000
Item 7, result 70000000
Item 6, result 60000000
Item 8, result 80000000
Item 9, result 90000000
Item 10, result 100000000
Process Pool Execution in 7.042000900000858 seconds
```

<p align="center">
  <img src="Output/concurrent_futures_pooling.png" alt="Concurrent Futures Pooling Output" width="80%">
</p>

---

## 2. Managing the event loop with `asyncio`

### Understanding event loops
The event loop is the central execution mechanism in `asyncio`. It operates on a single thread and enables cooperative multitasking by scheduling and running coroutines. The loop monitors I/O operations, timers, and callbacks, and switches between tasks whenever a coroutine reaches an `await` point. Unlike threading, coroutines voluntarily yield control, eliminating race conditions and reducing memory overhead.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#9C27B0', 'primaryColor': '#FFFFFF', 'clusterBkg':'#FDF8FF' }}}%%
flowchart LR
    %% Event Loop Architecture Diagram
    classDef loop fill:#ECEFF1,stroke:#37474F,stroke-width:3px,color:#263238,font-weight:bold,rx:10,ry:10
    classDef queue fill:#FFFDE7,stroke:#FBC02D,stroke-width:2px,color:#E65100,font-weight:bold
    classDef kernel fill:#E0F7FA,stroke:#00ACC1,stroke-width:2px,color:#006064,font-weight:bold
    classDef coro fill:#FCE4EC,stroke:#E91E63,stroke-width:2px,color:#880E4F,font-weight:bold

    subgraph ASYNC_ENV ["Asyncio Execution Thread"]
        direction TB
        EL[("Event Loop Engine \n (Single-Threaded Multiplexer)")]
        TQ["Task / Callback Queue \n (Runnable Coroutines)"]
        
        EL <-->|Fetches & Executes| TQ
    end

    C1["Coroutine A \n (Awaiting Socket I/O)"] -->|Yields control at await| EL
    EL -->|Registers File Descriptor| OS["OS Kernel \n (select/poll/epoll/IOCP)"]
    
    OS -->|"Data Arrives (Ready Event)"| EL
    EL -->|Appends callback to| TQ
    TQ -->|Resumes state| C2["Coroutine A \n (Completed Task)"]

    class EL loop
    class TQ queue
    class OS kernel
    class C1,C2 coro
```

### How to do it...
To manage the event loop, the recommended approach is to use `asyncio.run()`, which creates a new loop, executes your main coroutine, and properly shuts down the loop afterward. For more advanced scenarios, you can access the running loop via `asyncio.get_running_loop()` or create a custom loop using `asyncio.new_event_loop()` when you need finer control over lifecycle management.

**Example implementation ([asyncio_event_loop.py](Codes/asyncio_event_loop.py)):**
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


loop = asyncio.get_event_loop()
end_loop = loop.time() + 60
loop.call_soon(task_A, end_loop, loop)
loop.run_forever()
loop.close()
```

### How it works...
Internally, the event loop relies on I/O multiplexing mechanisms provided by the operating system, such as `select`, `poll`, `epoll` (Linux), or `IOCP` (Windows). When a coroutine awaits an I/O operation, the loop registers a callback for that operation and proceeds to execute other ready coroutines. Once the I/O completes, the loop resumes the waiting coroutine exactly where it left off, maintaining seamless asynchronous flow.

### There's more...
- Enabling debug mode provides detailed warnings about slow callbacks, unclosed resources, and common pitfalls during development.
- Third-party event loop implementations like `uvloop` (based on libuv) can significantly improve performance on Unix-like systems.
- The event loop can also integrate signal handlers, subprocesses, and inter-task communication primitives like queues and locks.

### See also
- Official `asyncio` documentation
- PEP 3156: Asynchronous IO Support Rebooted
- Alternative async frameworks like `trio` and `curio`

**Output:**
```text
task_A called
task_B called 
task_C called
task_A called
task_B called 
task_C called
task_A called
...
[Loop automatically stopped after 60 seconds of virtual time]
```

<p align="center">
  <img src="Output/asyncio_event_loop.png" alt="Asyncio Event Loop Output" width="80%">
</p>

---

## 3. Handling coroutines with `asyncio`

### Getting ready
Coroutines are defined using the `async def` syntax and return coroutine objects that do not execute until explicitly awaited or scheduled. The `await` keyword serves as a suspension point, allowing the coroutine to yield control back to the event loop while waiting for an operation to complete. `await` can only be used inside functions declared with `async def`.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#009688', 'primaryColor': '#FFFFFF', 'clusterBkg':'#E0F2F1' }}}%%
flowchart TD
    %% FSM Coroutine Transitions
    classDef start fill:#E3F2FD,stroke:#1E88E5,stroke-width:3px,color:#0D47A1,font-weight:bold,rx:8,ry:8
    classDef state fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px,color:#F57F17,font-weight:bold,rx:5,ry:5
    classDef stop fill:#FFEBEE,stroke:#E53935,stroke-width:3px,color:#C62828,font-weight:bold,rx:8,ry:8

    SS(["Start State \n (Entry point)"])
    S1(["State 1 \n (Awaiting 1 sec)"])
    S2(["State 2 \n (Awaiting 1 sec)"])
    S3(["State 3 \n (Awaiting 1 sec)"])
    ES(["End State \n (Computation Finished)"])

    SS -->|Input = 1| S1
    SS -->|Input = 0| S2

    S1 -->|Input = 1| S2
    S1 -->|Input = 0| S3

    S2 -->|Input = 0| S1
    S2 -->|Input = 1| S3

    S3 -->|Input = 0| S1
    S3 -->|Input = 1| ES

    class SS start
    class S1,S2,S3 state
    class ES stop
```

### How to do it...
To execute a coroutine, you can pass it directly to `asyncio.run()` for simple scripts. For concurrent execution of multiple coroutines, use `asyncio.gather()` to run them simultaneously and collect results, or `asyncio.wait()` for more granular control over completion conditions. Coroutines can also be scheduled as background tasks using `asyncio.create_task()`.

**Example implementation ([asyncio_coroutine.py](Codes/asyncio_coroutine.py)):**
```python
import asyncio
from random import randint


async def start_state():
    print('Start State called\n')

    input_value = randint(0, 1)

    await asyncio.sleep(1)

    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)

    print('Resume of the Transition:\nStart State calling ' + result)


async def state1(transition_value):
    output_value = f'State 1 with transition value = {transition_value}\n'

    input_value = randint(0, 1)

    await asyncio.sleep(1)

    print('...evaluating...')

    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)

    return output_value + 'State 1 calling ' + result


async def state2(transition_value):
    output_value = f'State 2 with transition value = {transition_value}\n'

    input_value = randint(0, 1)

    await asyncio.sleep(1)

    print('...evaluating...')

    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)

    return output_value + 'State 2 calling ' + result


async def state3(transition_value):
    output_value = f'State 3 with transition value = {transition_value}\n'

    input_value = randint(0, 1)

    await asyncio.sleep(1)

    print('...evaluating...')

    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)

    return output_value + 'State 3 calling ' + result


async def end_state(transition_value):
    output_value = f'End State with transition value = {transition_value}\n'

    print('...stop computation...')

    return output_value
async def main():
    await start_state()
if __name__ == '__main__':
    print('Finite State Machine simulation with Asyncio Coroutine')
    asyncio.run(main())
```

### How it works...
When a coroutine encounters an `await` expression, its execution pauses at that point, and control returns to the event loop. The loop then proceeds to run other pending coroutines. Once the awaited operation (such as I/O or a timer) completes, the loop resumes the original coroutine with the result of the operation. This cooperative scheduling model enables high concurrency without the complexity of thread synchronization.

### There's more...
- `asyncio.as_completed()` allows you to iterate over coroutines in the order they finish, useful for processing results as soon as they are available.
- Timeouts can be enforced using `asyncio.wait_for()`, which raises a `TimeoutError` if a coroutine does not complete within the specified duration.
- For safe data sharing between coroutines, `asyncio.Queue` provides a FIFO interface designed for asynchronous producers and consumers.

### See also
- Python documentation: Coroutines and Tasks
- `contextlib.asynccontextmanager` for managing asynchronous resources
- `aiohttp` for building asynchronous HTTP clients and servers

**Output:**
```text
Finite State Machine simulation with Asyncio Coroutine
Start State called

...evaluating...
...evaluating...
...evaluating...
...stop computation...

Resume of the Transition:
Start State calling State 1 with transition value = 1
State 2 calling State 2 with transition value = 1
State 3 calling State 3 with transition value = 1
End State with transition value = 1
```

<p align="center">
  <img src="Output/asyncio_coroutine.png" alt="Asyncio Coroutine Output" width="80%">
</p>

---

## 4. Manipulating tasks with `asyncio`

### How to do it...
Tasks are wrappers around coroutines that schedule them for execution on the event loop. You can create a task using `asyncio.create_task()` or `asyncio.ensure_future()`. Tasks support cancellation via the `cancel()` method, and you can attach completion handlers using `add_done_callback()` to trigger custom logic when the task finishes.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#FF9800', 'primaryColor': '#FFFFFF', 'clusterBkg':'#FFF3E0' }}}%%
flowchart TD
    %% Task Scheduling and Concurrent Execution
    classDef loop fill:#ECEFF1,stroke:#607D8B,stroke-width:3px,color:#37474F,font-weight:bold,rx:8,ry:8
    classDef task fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px,color:#F57F17,font-weight:bold,rx:5,ry:5
    classDef gather fill:#E8F5E9,stroke:#4CAF50,stroke-width:3px,color:#1B5E20,font-weight:bold,rx:8,ry:8

    EL[["asyncio Event Loop"]] -->|"create_task()"| T1["Task 1: factorial(10) \n (Runs concurrently)"]
    EL -->|"create_task()"| T2["Task 2: fibonacci(10) \n (Runs concurrently)"]
    EL -->|"create_task()"| T3["Task 3: binomial_coefficient(20, 10) \n (Runs concurrently)"]

    T1 -->|Yields control on await sleep| EL
    T2 -->|Yields control on await sleep| EL
    T3 -->|Yields control on await sleep| EL

    T1 & T2 & T3 -->|Awaited via| TG{"asyncio.gather"}
    TG -->|All finished| Out["Complete Execution & Output Results"]

    class EL loop
    class T1,T2,T3 task
    class TG gather
```

**Example implementation ([asyncio_task_manipulation.py](Codes/asyncio_task_manipulation.py)):**
```python
import asyncio


async def factorial(number):
    fact = 1

    for i in range(2, number + 1):
        print(f'Asyncio.Task: Compute factorial({i})')

        await asyncio.sleep(1)

        fact *= i

    print(f'Asyncio.Task - factorial({number}) = {fact}')


async def fibonacci(number):
    a, b = 0, 1

    for i in range(number):
        print(f'Asyncio.Task: Compute fibonacci({i})')

        await asyncio.sleep(1)

        a, b = b, a + b

    print(f'Asyncio.Task - fibonacci({number}) = {a}')


async def binomial_coefficient(n, k):
    result = 1

    for i in range(1, k + 1):
        result = result * (n - i + 1) / i

        print(f'Asyncio.Task: Compute binomial_coefficient({i})')

        await asyncio.sleep(1)

    print(f'Asyncio.Task - binomial_coefficient({n}, {k}) = {result}')


async def main():

    task1 = asyncio.create_task(factorial(10))
    task2 = asyncio.create_task(fibonacci(10))
    task3 = asyncio.create_task(binomial_coefficient(20, 10))

    await asyncio.gather(task1, task2, task3)


if __name__ == '__main__':
    asyncio.run(main())
```

### How it works...
A Task object implements the Future interface, meaning it supports methods like `result()`, `exception()`, and `done()` to inspect its state. When a task is cancelled, a `CancelledError` is raised inside the associated coroutine. Properly handling this exception is essential to ensure clean resource cleanup and avoid silent failures.

### There's more...
- Starting with Python 3.11, `asyncio.TaskGroup` provides structured concurrency, automatically waiting for all child tasks and propagating exceptions.
- Always use `try/finally` blocks or context managers when working with background tasks to guarantee cleanup even if cancellation occurs.
- Assigning descriptive names to tasks using the `name` parameter improves debugging and logging clarity.

### See also
- `asyncio.Task` class documentation
- Structured concurrency patterns and best practices
- `anyio` library for writing backend-agnostic asynchronous code

**Output:**
```text
Asyncio.Task: Compute factorial(2)
Asyncio.Task: Compute fibonacci(0)
Asyncio.Task: Compute binomial_coefficient(1)
Asyncio.Task: Compute factorial(3)
Asyncio.Task: Compute fibonacci(1)
Asyncio.Task: Compute binomial_coefficient(2)
Asyncio.Task: Compute factorial(4)
Asyncio.Task: Compute fibonacci(2)
Asyncio.Task: Compute binomial_coefficient(3)
...
Asyncio.Task - factorial(10) = 3628800
Asyncio.Task - fibonacci(10) = 34
Asyncio.Task - binomial_coefficient(20, 10) = 184756.0
```

<p align="center">
  <img src="Output/asyncio_task_manipulation.png" alt="Asyncio Task Manipulation Output" width="80%">
</p>

---

## 5. Dealing with `asyncio` and futures

### Getting ready
Both Futures and Tasks represent values that will be available at some point in the future. A Future is a low-level primitive for asynchronous result handling, while a Task is a specialized Future that wraps a coroutine. It is important to distinguish between `concurrent.futures.Future` (from the threading/process model) and `asyncio.Future` (from the async model), as they operate in different concurrency contexts.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#3F51B5', 'primaryColor': '#FFFFFF', 'clusterBkg':'#E8EAF6' }}}%%
flowchart LR
    %% Futures and Tasks Relationships
    classDef wrapper fill:#EDE7F6,stroke:#5E35B1,stroke-width:2px,color:#311B92,font-weight:bold,rx:5,ry:5
    classDef future fill:#E8EAF6,stroke:#3F51B5,stroke-width:2px,color:#1A237E,font-weight:bold,rx:8,ry:8
    classDef state fill:#E0F2F1,stroke:#009688,stroke-width:2px,color:#004D40,rx:5,ry:5

    subgraph CALLABLES ["Asynchronous Coroutines"]
        C1["first_coroutine(N) \n (Sum N integers)"]
        C2["second_coroutine(N) \n (Factorial of N)"]
    end

    subgraph TASKS ["asyncio.Task (Subclass of asyncio.Future)"]
        T1["Task 1 \n (Awaits C1, yields Sum)"]
        T2["Task 2 \n (Awaits C2, yields Fact)"]
    end

    C1 -->|Scheduled via create_task| T1
    C2 -->|Scheduled via create_task| T2

    T1 & T2 -->|State Lifecycle| FSTATE{"Future Resolution"}
    
    FSTATE -->|PENDING| S1["Running in Event Loop"]
    FSTATE -->|FINISHED| S2["Resolved with Result / Value"]

    class C1,C2 wrapper
    class T1,T2 future
    class S1,S2 state
```

### How to do it...
To bridge the two models, use `asyncio.wrap_future()` to convert a `concurrent.futures.Future` into an `asyncio.Future`, allowing it to be awaited in async code. Conversely, to run blocking code from within an async context, use `loop.run_in_executor()` to delegate the work to a thread or process pool and receive an awaitable result.

**Example implementation ([asyncio_and_futures.py](Codes/asyncio_and_futures.py)):**
```python
import asyncio
import sys
async def first_coroutine(num):
    count = 0
    for i in range(1, num + 1):
        count += 1
    await asyncio.sleep(4)
    return f'First coroutine (sum of N ints) result = {count}'
async def second_coroutine(num):
    count = 1
    for i in range(2, num + 1):
        count *= i
    await asyncio.sleep(4)

    return f'Second coroutine (factorial) result = {count}'


async def main():
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    task1 = asyncio.create_task(first_coroutine(num1))
    task2 = asyncio.create_task(second_coroutine(num2))

    result1 = await task1
    result2 = await task2

    print(result1)
    print(result2)


if __name__ == '__main__':
    asyncio.run(main())
```

> **Execution Note:** Since this script accesses `sys.argv`, run it by passing two integer arguments:
> ```bash
> python asyncio_and_futures.py 100 5
> ```

### How it works...
`wrap_future()` creates an asyncio-compatible Future that automatically resolves when the original concurrent.futures Future completes. This enables seamless integration between thread-based or process-based concurrency and asynchronous code. Similarly, `run_in_executor()` schedules a blocking function in a separate thread or process and returns a Future that can be awaited, keeping the main event loop responsive.

### There's more...
- When mixing executors with async code, ensure thread-safety for any shared resources or data structures.
- Python 3.9+ introduces `asyncio.to_thread()`, a convenient way to run a blocking function in a separate thread without manually managing an executor.
- Properly propagate cancellation signals between Futures and Tasks to avoid resource leaks or inconsistent states.

### See also
- Guides on mixing threads and asyncio
- `aiomultiprocess` for asynchronous multiprocessing patterns
- Best practices for combining async/await with traditional concurrency models

**Output:**
```text
$ python asyncio_and_futures.py 100 5
First coroutine (sum of N ints) result = 5050
Second coroutine (factorial) result = 120
```

<p align="center">
  <img src="Output/asyncio_and_futures.png" alt="Asyncio and Futures Output" width="80%">
</p>
