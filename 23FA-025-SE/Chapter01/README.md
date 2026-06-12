# Chapter 01: Introduction to Parallel Computing in Python

## Overview

This chapter provides an introduction to Parallel and Distributed
Computing (PDC) using Python. It explains the basic concepts behind
improving software performance through parallel execution.

The documentation is divided into two sections:

-   **Part 1: Theoretical Concepts** explains the fundamentals of
    parallel computing, different execution models, memory management,
    and Python limitations.
-   **Part 2: Practical Implementation** demonstrates serial execution,
    multithreading, and multiprocessing with Python examples and
    performance comparisons.

------------------------------------------------------------------------

# Part 1: Theoretical Concepts

## 1. Importance of Parallel and Distributed Computing

Modern applications require faster processing, better performance, and
the ability to handle large amounts of data. Parallel and Distributed
Computing helps achieve these goals.

### Limitations of Traditional CPU Growth

Previously, processors became faster by increasing clock speed and
transistor count. However, physical limitations such as heat and power
consumption reduced the ability to keep increasing single-core
performance.

Modern processors improve performance by adding multiple cores. Software
must be designed to use these cores effectively through parallel
execution.

### Handling Large Data

Applications today process huge amounts of information. Running all
operations sequentially on one thread can create performance issues.

Parallel computing divides tasks into smaller parts and executes them
simultaneously, reducing overall processing time.

### Reliability and Availability

Distributed systems use multiple machines working together. If one
machine fails, other machines can continue processing, improving system
reliability.

------------------------------------------------------------------------

# 2. Understanding Execution Models

## Serial Execution

In serial execution, tasks are completed one after another.

Example:

Task 1 → Task 2 → Task 3

The next task starts only after the previous task finishes. It is simple
and predictable but does not fully utilize modern hardware.

## Concurrency

Concurrency allows multiple tasks to be managed at the same time.

The operating system switches between tasks quickly, creating the
feeling of simultaneous execution. However, tasks may not actually run
at the exact same moment.

## Parallelism

Parallelism means multiple tasks are executed at the same time using
multiple CPU cores.

Example:

Core 1 → Task A\
Core 2 → Task B\
Core 3 → Task C

This provides real performance improvement for suitable workloads.

------------------------------------------------------------------------

# Memory Model: Threads vs Processes

## Threads

Threads run inside the same process and share memory.

Advantages: - Faster communication between tasks - Lower memory usage

Disadvantages: - Shared memory can cause problems such as race
conditions - Requires synchronization techniques like locks and
semaphores

## Processes

Processes run independently with their own memory space.

Advantages: - Better isolation - Can utilize multiple CPU cores

Disadvantages: - Communication between processes requires extra
mechanisms - Creating processes has more overhead

------------------------------------------------------------------------

# Python Global Interpreter Lock (GIL)

Python's standard implementation (CPython) uses the Global Interpreter
Lock.

The GIL allows only one thread to execute Python code at a time. Because
of this, multithreading does not provide true parallel execution for
CPU-heavy tasks.

For heavy computational work, multiprocessing is usually preferred
because it creates separate Python processes that can run on different
CPU cores.

------------------------------------------------------------------------

# 3. Key Concepts

## Amdahl's Law

Amdahl's Law explains that parallel programs cannot always achieve
perfect speed improvement because some operations remain sequential and
additional overhead exists.

For example, using 10 processes does not always make a program exactly
10 times faster.

## Context Switching

When multiple threads compete for CPU time, the operating system
switches between them.

For CPU-intensive work, frequent switching can reduce performance
instead of improving it.

------------------------------------------------------------------------

# Part 2: Practical Implementation

## 4. Workload Description

The examples use a CPU-intensive function that repeatedly generates
random numbers and stores them in a list.

This workload is used to compare different execution methods.

------------------------------------------------------------------------

# 5. Execution Approaches

## Serial Execution

File: `serial_test.py`

Serial execution processes all tasks using a single flow.

Advantages: - Simple implementation - Predictable results

Limitation: - Uses only one CPU core

------------------------------------------------------------------------

## Multithreading

File: `multithreading_test.py`

Multithreading creates multiple threads to perform tasks.

For CPU-based operations in Python, performance may not improve because
of the GIL.

Possible result: - Similar or slower execution compared to serial
processing

------------------------------------------------------------------------

## Multiprocessing

File: `multiprocessing_test.py`

Multiprocessing creates separate processes that can run independently.

Advantages: - Uses multiple CPU cores - Avoids Python's GIL limitation

For CPU-heavy workloads, it usually provides better performance.

------------------------------------------------------------------------

# 6. Basic Python Modules

The chapter also includes basic Python examples:

-   `classes.py` demonstrates object-oriented programming concepts.
-   `lists.py` explains Python lists and indexing.
-   `flow.py` covers conditional statements and loops.
-   `dir.py` and `file.py` demonstrate file and directory operations.

------------------------------------------------------------------------

# 7. Running the Examples

Run the following commands inside the project folder:

python serial_test.py

python multithreading_test.py

python multiprocessing_test.py
