# Asynchronous Programming and Concurrent Futures in Python

## Overview

This project introduces asynchronous programming in Python using **asyncio** and **concurrent.futures**.

Traditional programs execute tasks sequentially, meaning one task must finish before another starts. Asynchronous programming allows multiple tasks to make progress concurrently without blocking the entire program.

This chapter demonstrates:

* Event Loops
* Coroutines
* Futures
* Async Tasks
* Task Scheduling
* Finite State Machines with Coroutines
* Thread Pools
* Process Pools
* Concurrent Execution

These concepts are widely used in modern applications such as web servers, APIs, networking systems, real-time applications, and distributed systems.

---

# Project Structure

```text
├── asyncio_event_loop.py
├── asyncio_coroutine.py
├── asyncio_task_manipulation.py
├── asyncio_and_futures.py
└── concurrent_futures_pooling.py
```

---

# Requirements

## Software

* Python 3.x

## Libraries Used

Built-in Python modules:

* asyncio
* concurrent.futures
* random
* time
* sys

No additional installation is required.

---

# Learning Objectives

After completing this chapter, students will be able to:

* Understand asynchronous programming
* Work with asyncio event loops
* Create and execute coroutines
* Schedule asynchronous tasks
* Use Futures for result handling
* Execute tasks concurrently
* Use Thread Pools
* Use Process Pools
* Compare sequential and concurrent execution

---

# Introduction to Async Programming

## Synchronous Execution

```text
Task A → Task B → Task C
```

Each task waits for the previous task to finish.

---

## Asynchronous Execution

```text
Task A
Task B
Task C
```

Tasks can progress concurrently while waiting for resources.

This improves responsiveness and resource utilization.

---

# File Descriptions

---

## 1. asyncio_event_loop.py

### Purpose

Demonstrates how the Asyncio Event Loop schedules and manages tasks.

### Concepts Covered

* Event Loop
* Task Scheduling
* call_soon()
* call_later()

### Workflow

1. Event loop starts.
2. Task A executes.
3. Task A schedules Task B.
4. Task B schedules Task C.
5. Task C schedules Task A.
6. Loop continues until timeout.

### Learning Outcome

Understand how the event loop coordinates asynchronous execution.

---

## 2. asyncio_coroutine.py

### Purpose

Demonstrates coroutines through a Finite State Machine (FSM).

### Concepts Covered

* Coroutines
* yield from
* State transitions
* Async workflows

### States

```text
Start State
   ↓
State 1
State 2
State 3
   ↓
End State
```

### Workflow

1. Start state chooses a transition.
2. States call one another asynchronously.
3. Execution continues until End State.

### Learning Outcome

Understand coroutine-based state management.

---

## 3. asyncio_task_manipulation.py

### Purpose

Demonstrates running multiple mathematical computations concurrently.

### Tasks Executed

#### Factorial

```text
n!
```

#### Fibonacci Sequence

```text
0,1,1,2,3,5,...
```

#### Binomial Coefficient

```text
nCk
```

### Concepts Covered

* Async Tasks
* Task Scheduling
* Parallel Coroutine Execution

### Workflow

1. Create three tasks.
2. Register tasks with event loop.
3. Execute concurrently.
4. Collect results.

### Learning Outcome

Learn how asyncio manages multiple tasks simultaneously.

---

## 4. asyncio_and_futures.py

### Purpose

Demonstrates Futures and callback functions.

### Concepts Covered

* Future objects
* Asynchronous result handling
* Callback functions

### Calculations

#### First Coroutine

Computes:

```text
Sum of integers
```

#### Second Coroutine

Computes:

```text
Factorial
```

### Workflow

1. Create Future objects.
2. Execute coroutines.
3. Store results in Futures.
4. Trigger callbacks when complete.

### Learning Outcome

Understand how asynchronous results are managed.

---

## 5. concurrent_futures_pooling.py

### Purpose

Demonstrates task execution using Thread Pools and Process Pools.

### Concepts Covered

* ThreadPoolExecutor
* ProcessPoolExecutor
* Concurrent execution
* Performance comparison

### Execution Modes

#### Sequential Execution

```text
Task 1
Task 2
Task 3
...
```

#### Thread Pool

```text
5 worker threads
```

#### Process Pool

```text
5 worker processes
```

### Workflow

1. Execute tasks sequentially.
2. Execute using thread pool.
3. Execute using process pool.
4. Compare execution times.

### Learning Outcome

Understand different concurrency models and their performance implications.

---

# Asyncio Components Summary

| Component  | Purpose                        |
| ---------- | ------------------------------ |
| Event Loop | Coordinates async execution    |
| Coroutine  | Async function                 |
| Future     | Holds future result            |
| Task       | Scheduled coroutine            |
| Callback   | Executes after task completion |

---

# Concurrent Futures Components

| Executor            | Description                    |
| ------------------- | ------------------------------ |
| ThreadPoolExecutor  | Executes tasks using threads   |
| ProcessPoolExecutor | Executes tasks using processes |

---

# Running the Programs

Run any file using:

```bash
python filename.py
```

Examples:

```bash
python asyncio_event_loop.py
```

```bash
python asyncio_coroutine.py
```

```bash
python asyncio_task_manipulation.py
```

```bash
python asyncio_and_futures.py 10 5
```

```bash
python concurrent_futures_pooling.py
```

---

# Sample Output

## Event Loop

```text
task_A called
task_B called
task_C called
```

---

## Coroutine State Machine

```text
Start State called

...evaluating...

State 1 calling State 3

...stop computation...
```

---

## Async Tasks

```text
Asyncio.Task: Compute factorial(2)

Asyncio.Task: Compute fibonacci(1)

Asyncio.Task: Compute binomial_coefficient(1)
```

---

## Futures

```text
First coroutine (sum of N ints) result = 10

Second coroutine (factorial) result = 120
```

---

## Thread Pool / Process Pool

```text
Sequential Execution in 5.8 seconds

Thread Pool Execution in 2.1 seconds

Process Pool Execution in 1.3 seconds
```

(Execution times vary depending on system specifications.)

---

# Comparison of Concurrency Approaches

| Approach     | Best For                   |
| ------------ | -------------------------- |
| Sequential   | Simple tasks               |
| Asyncio      | I/O-bound operations       |
| Thread Pool  | Lightweight concurrency    |
| Process Pool | CPU-intensive computations |

---

# Key Concepts Learned

This chapter introduces:

* Asynchronous Programming
* Event Loops
* Coroutines
* Futures
* Async Tasks
* Task Scheduling
* Callback Functions
* Concurrent Execution
* Thread Pools
* Process Pools
* Performance Optimization

---

# Conclusion

This project provides practical experience with Python's asynchronous programming model and concurrent execution frameworks. Students learn how modern applications manage multiple tasks efficiently, coordinate asynchronous workflows, and improve performance using event-driven programming, thread pools, and process pools.

These concepts form the foundation of high-performance applications, web services, networking software, cloud systems, and scalable distributed applications.
