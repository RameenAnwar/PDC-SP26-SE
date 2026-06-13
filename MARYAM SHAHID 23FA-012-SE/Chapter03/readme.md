# README

## Overview

This repository contains Python programs that demonstrate **Process-Based Parallelism** using the `multiprocessing` module. The examples cover process creation, process communication, process synchronization, process pools, daemon processes, barriers, queues, pipes, and process management techniques.

---

## Files Description

### spawning_processes.py

Demonstrates how to create and start multiple processes using the `Process` class. Each process executes a function independently. 

### spawning_processes_namespace.py

Similar to the spawning process example, but imports the target function from a separate module to demonstrate process execution across multiple files. 

### myFunc.py

Contains a simple function used by other multiprocessing examples. The function prints process-specific output for demonstration purposes. 

### process_in_subclass.py

Demonstrates process creation by subclassing the `multiprocessing.Process` class and overriding the `run()` method. 

### naming_processes.py

Shows how to assign custom names to processes and retrieve process information during execution. 

### killing_processes.py

Demonstrates how to terminate a running process using the `terminate()` method and monitor its status. 

### run_background_processes.py

Illustrates daemon processes. A background process runs as a daemon while another process runs normally. 

### run_background_processes_no_daemons.py

Shows process execution when all processes are non-daemon, allowing them to complete normally before program termination. 

### communicating_with_pipe.py

Demonstrates inter-process communication using **Pipes**. One process generates data, while another receives and processes it through connected pipes. 

### communicating_with_queue.py

Implements a producer-consumer model using a **Multiprocessing Queue** for safe communication between processes. 

### processes_barrier.py

Demonstrates synchronization between multiple processes using a **Barrier**. Processes wait until all participants reach the synchronization point before continuing. 

### process_pool.py

Illustrates the use of a **Process Pool** to distribute tasks across multiple worker processes efficiently. 

---

## Concepts Covered

* Process Creation
* Process Lifecycle Management
* Process Communication
* Pipes
* Queues
* Process Synchronization
* Barriers
* Daemon Processes
* Process Pools
* Process Termination
* Custom Process Classes
* Parallel Task Execution

---

## Requirements

* Python 3.x

Standard libraries used:

* multiprocessing
* time
* random
* datetime

No external packages are required.

---

## Running the Programs

Execute any file using:

```bash
python filename.py
```

Examples:

```bash
python spawning_processes.py
```

```bash
python process_pool.py
```

```bash
python communicating_with_pipe.py
```

```bash
python communicating_with_queue.py
```

---

## Learning Outcomes

After completing these examples, you will understand:

* How processes are created and managed in Python.
* Differences between processes and threads.
* Methods for inter-process communication.
* Synchronization techniques for multiple processes.
* How daemon processes work.
* How process pools improve task execution efficiency.
* Techniques for controlling and terminating processes.

---

## Conclusion

These programs provide practical examples of Python multiprocessing and process synchronization. They help build a strong foundation in parallel programming and demonstrate how multiple processes can work together efficiently to perform computational tasks.
