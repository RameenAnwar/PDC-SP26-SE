# Chapter 3: Process-Based Parallelism

## Overview

This chapter explains process-based concurrency in Python using the `multiprocessing` module. Unlike threads, processes run independently and bypass the Global Interpreter Lock (GIL), making them suitable for CPU-intensive tasks that require true parallel execution.

The chapter covers both theoretical concepts and practical implementations, including process creation, communication, synchronization, and process pools.

---

## 1. Understanding Python's multiprocessing module

The `multiprocessing` module enables programs to create separate processes, each with its own Python interpreter and memory space.

### Key Points

- **Bypassing the GIL:** CPU-bound tasks can execute in parallel.
- **Process Isolation:** Processes do not share memory by default and communicate using Pipes and Queues.

---

## 2. Spawning a Process

A new process can be created using the `multiprocessing.Process` class and assigning a target function to execute.

### Important Methods

- `start()` launches the process.
- `join()` waits until the child process completes.

**Example Implementation:** `spawning_processes.py`

### 2.1 Spawning Processes from a Separate Module

Instead of defining the target function in the same file, it can be placed in another module and imported when needed.

**Worker Module:** `myFunc.py`

**Spawning Script:** `spawning_processes_namespace.py`

---

## 3. Naming a Process

Assigning names to processes makes debugging and monitoring easier.

**Example Implementation:** `naming_processes.py`

---

## 4. Running Processes in the Background

Processes can operate in the background by setting `daemon=True`.

A daemon process automatically terminates when the main program exits, even if its work is incomplete.

**Example Implementation:** `run_background_processes.py`

### 4.1 Non-Daemon Background Processes

When `daemon=False`, the main program waits for the process to finish before terminating.

**Example Implementation:** `run_background_processes_no_daemons.py`

---

## 5. Killing a Process

A running process can be stopped using `process.terminate()`.

The `is_alive()` method can be used to check whether the process is still active.

**Example Implementation:** `killing_processes.py`

---

## 6. Defining Processes in a Subclass

Processes can be created by inheriting from `multiprocessing.Process` and overriding the `run()` method.

**Example Implementation:** `process_in_subclass.py`

---

## 7. Using a Queue to Exchange Data

`multiprocessing.Queue` provides a secure way for processes to exchange information.

**Example Implementation:** `communicating_with_queue.py`

---

## 8. Using Pipes to Exchange Objects

`multiprocessing.Pipe()` creates two connected endpoints for communication between processes.

**Example Implementation:** `communicating_with_pipe.py`

---

## 9. Synchronizing Processes

The `multiprocessing` module provides synchronization tools such as:

- Lock
- Event
- Condition
- Barrier

**Example Implementation:** `processes_barrier.py`

---

## 10. Using a Process Pool

`multiprocessing.Pool` manages multiple worker processes and distributes tasks efficiently.

### Key Feature

- `pool.map()` executes tasks in parallel across multiple processes.

**Example Implementation:** `process_pool.py`

---

## Summary

The `multiprocessing` module enables true parallel execution in Python through separate processes and provides tools for communication, synchronization, and workload distribution.
