# Chapter 1: Getting Started with Parallel Computing and Python

> [!NOTE]
> **Comprehensive Foundations**
> This chapter establishes the critical theoretical foundations of parallel computing and introduces Python's powerful toolkit for concurrent programming.

---

## Table of Contents
1. [Why Do We Need Parallel Computing?](#1-why-do-we-need-parallel-computing)
2. [Flynn's Taxonomy](#2-flynns-taxonomy)
3. [Memory Organization](#3-memory-organization)
4. [Parallel Programming Models](#4-parallel-programming-models)
5. [Designing a Parallel Program](#5-designing-a-parallel-program)
6. [Evaluating the Performance of a Parallel Program](#6-evaluating-the-performance-of-a-parallel-program)
7. [Introducing Python](#7-introducing-python)
8. [Introducing Python Parallel Programming](#8-introducing-python-parallel-programming)

---

## 1. Why Do We Need Parallel Computing?

Parallel computing is the simultaneous execution of multiple computations to solve a problem faster or to solve larger problems.
- **Performance Limitations of Single-Core:** Historically, processor performance increased through higher clock speeds. However, physical limitations (power consumption, heat dissipation) halted this trend around the mid-2000s.
- **Multi-Core Era:** Manufacturers shifted to multi-core processors. To utilize this hardware, software must be written to execute tasks concurrently.
- **Problem Size:** Some problems are too large or complex for a single processor to handle in reasonable time (e.g., weather forecasting, genomic analysis, large-scale simulations).
- **Throughput:** Parallel computing increases system throughput, allowing more tasks to be completed in a given time period.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart TD
    %% Premium Styled Serial vs Parallel Comparison
    classDef serial fill:#ffe4e6,stroke:#e11d48,stroke-width:2px,color:#4c0519,font-weight:bold
    classDef parallel fill:#d1fae5,stroke:#059669,stroke-width:2px,color:#064e3b,font-weight:bold
    classDef core fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0c4a6e,font-weight:bold
    classDef task fill:#f1f5f9,stroke:#64748b,stroke-width:1.5px,color:#0f172a

    subgraph Dashboard ["⚡ Parallel vs Serial Performance Dashboard"]
        direction TB
        
        subgraph S_TRACK ["🔴 Single-Core Serial Pipeline"]
            direction LR
            S1[Task 1] ==> S2[Task 2] ==> S3[Task 3] ==> S4[Task 4]
        end
        
        subgraph P_TRACK ["🟢 Multi-Core Parallel Tracks"]
            direction LR
            subgraph CORE_A ["💻 Core 1"]
                T1[Parallel Task A]
            end
            subgraph CORE_B ["💻 Core 2"]
                T2[Parallel Task B]
            end
            subgraph CORE_C ["💻 Core 3"]
                T3[Parallel Task C]
            end
            subgraph CORE_D ["💻 Core 4"]
                T4[Parallel Task D]
            end
        end
    end

    class S_TRACK serial
    class P_TRACK parallel
    class CORE_A,CORE_B,CORE_C,CORE_D core
    class S1,S2,S3,S4,T1,T2,T3,T4 task
```

## 2. Flynn's Taxonomy

Flynn's Taxonomy classifies computer architectures based on the number of instruction streams and data streams they can process simultaneously.

### 2.1 Single Instruction Single Data (SISD)
- **Definition:** A traditional von Neumann architecture with one processor executing one instruction stream on one data stream at a time.
- **Characteristics:** Sequential execution. No parallelism at the hardware level.
- **Example:** Classic single-core processors.

### 2.2 Multiple Instruction Single Data (MISD)
- **Definition:** Multiple processors execute different instructions on the same data stream simultaneously.
- **Characteristics:** Rare in practice. Theoretical use in fault-tolerant systems where multiple processors perform different computations on the same input to verify results.
- **Example:** Spacecraft control systems with redundant processors for error checking.

### 2.3 Single Instruction Multiple Data (SIMD)
- **Definition:** A single instruction is executed by multiple processors, each operating on different data elements simultaneously.
- **Characteristics:** Ideal for data-parallel tasks where the same operation is applied to large datasets.
- **Example:** Graphics Processing Units (GPUs), vector processors, and multimedia instruction sets like SSE or AVX in modern CPUs.

### 2.4 Multiple Instruction Multiple Data (MIMD)
- **Definition:** Multiple processors execute different instruction streams on different data streams independently.
- **Characteristics:** Most flexible and common architecture for general-purpose parallel computing. Processors can work on completely different tasks.
- **Example:** Multi-core CPUs, distributed computing clusters, and modern supercomputers.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart TD
    %% Premium Styled Flynn's Taxonomy
    classDef title fill:#e0e7ff,stroke:#4f46e5,stroke-width:2.5px,color:#1e1b4b,font-weight:bold
    classDef axis fill:#f1f5f9,stroke:#94a3b8,stroke-width:1.5px,color:#334155
    classDef sisd fill:#fee2e2,stroke:#ef4444,stroke-width:2px,color:#7f1d1d,font-weight:bold
    classDef simd fill:#dcfce7,stroke:#22c55e,stroke-width:2px,color:#14532d,font-weight:bold
    classDef misd fill:#e0f2fe,stroke:#0ea5e9,stroke-width:2px,color:#0c4a6e,font-weight:bold
    classDef mimd fill:#fef3c7,stroke:#f59e0b,stroke-width:2.5px,color:#78350f,font-weight:bold

    TITLE["📊 Flynn's Classification Matrix"]

    subgraph InstructionAxis ["Instruction Stream"]
        direction TB
        SingleI["Single Stream"]
        MultiI["Multiple Streams"]
    end

    subgraph DataAxis ["Data Stream"]
        direction LR
        SingleD["Single Stream"]
        MultiD["Multiple Streams"]
    end

    Matrix_SISD["SISD: Single Instruction Single Data (Traditional CPU)"]
    Matrix_SIMD["SIMD: Single Instruction Multiple Data (Vector/GPU)"]
    Matrix_MISD["MISD: Multiple Instruction Single Data (Fault-Tolerant)"]
    Matrix_MIMD["MIMD: Multiple Instruction Multiple Data (Multi-Core)"]

    SingleI --- SingleD --> Matrix_SISD
    SingleI --- MultiD --> Matrix_SIMD
    MultiI --- SingleD --> Matrix_MISD
    MultiI --- MultiD --> Matrix_MIMD

    class TITLE title
    class SingleI,MultiI,SingleD,MultiD axis
    class Matrix_SISD sisd
    class Matrix_SIMD simd
    class Matrix_MISD misd
    class Matrix_MIMD mimd
```

## 3. Memory Organization

Memory organization defines how processors access memory in a parallel system.

### 3.1 Shared Memory
- **Definition:** All processors share a single, unified address space. Any processor can access any memory location.
- **Advantages:** Simple programming model. Data sharing is implicit and fast (via memory reads/writes).
- **Disadvantages:** Scalability limitations due to memory bus contention. Requires synchronization mechanisms (locks, semaphores) to prevent race conditions.
- **Hardware Implementation:** Uniform Memory Access (UMA) where all processors have equal access time to memory, or Non-Uniform Memory Access (NUMA) where access time depends on memory location relative to the processor.

### 3.2 Distributed Memory
- **Definition:** Each processor has its own private memory. Processors cannot directly access each other's memory.
- **Communication:** Processors exchange data by sending messages over a network.
- **Advantages:** Highly scalable. No memory contention issues.
- **Disadvantages:** Complex programming model. Programmer must explicitly manage data distribution and communication.
- **Example:** Computer clusters, distributed systems.

### 3.3 Massively Parallel Processing (MPP)
- **Definition:** A distributed memory architecture with a large number of processors (hundreds to thousands), each with its own memory and operating system.
- **Characteristics:** Designed for high-performance computing. Processors are interconnected via high-speed networks.
- **Use Case:** Scientific computing, big data analytics, and large-scale simulations.

### 3.5 Clusters of Workstations
- **Definition:** A collection of independent, commodity computers (workstations or servers) connected via a network to work as a single parallel system.
- **Characteristics:** Cost-effective alternative to specialized supercomputers. Often use message-passing libraries like MPI.
- **Challenge:** Network latency and bandwidth can become bottlenecks.

### 3.6 Heterogeneous Architectures
- **Definition:** Systems that combine different types of processing units, such as CPUs, GPUs, FPGAs, or specialized accelerators.
- **Characteristics:** Different units excel at different tasks (e.g., CPUs for control logic, GPUs for parallel data processing).
- **Programming Challenge:** Requires managing data movement and task allocation across different architectures with different instruction sets and memory spaces.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart LR
    %% Premium Shared vs Distributed Memory
    classDef proc fill:#e0f2fe,stroke:#0ea5e9,stroke-width:2px,color:#0369a1,font-weight:bold
    classDef mem fill:#dcfce7,stroke:#22c55e,stroke-width:2px,color:#15803d,font-weight:bold
    classDef bus fill:#fef3c7,stroke:#f59e0b,stroke-width:2px,color:#b45309,font-weight:bold

    subgraph SHARED_SCHEMA ["🧠 Shared Address Architecture"]
        direction TB
        subgraph COMPUTE_POOL ["Processors"]
            C1(Processor 1) ~~~ C2(Processor 2) ~~~ C3(Processor n)
        end
        BUS{{"🚀 High-Speed System Bus"}}
        RAM[("💾 Unified Shared Memory")]
        
        COMPUTE_POOL === BUS === RAM
    end

    subgraph DIST_SCHEMA ["🌐 Distributed Memory Schematic"]
        direction TB
        subgraph NODE_1 ["Computing Node 1"]
            P1(CPU) --- M1[("💾 Local RAM")]
        end
        subgraph NODE_2 ["Computing Node 2"]
            P2(CPU) --- M2[("💾 Local RAM")]
        end
        NET{{"🔌 Network Interconnect"}}
        
        NET <---> NODE_1
        NET <---> NODE_2
    end

    class C1,C2,C3,P1,P2 proc
    class RAM,M1,M2 mem
    class BUS,NET bus
```

## 4. Parallel Programming Models

A programming model defines how parallelism is expressed and managed in software.

### 4.1 Shared Memory Model
- **Concept:** Threads or processes share a common address space. Parallelism is expressed through threads that execute concurrently and communicate via shared variables.
- **Synchronization:** Requires explicit synchronization primitives (locks, condition variables) to coordinate access to shared data.
- **API Examples:** POSIX threads (pthreads), OpenMP, Python threading module.

### 4.2 Multithread Model
- **Concept:** A specific case of the shared memory model where a single process contains multiple threads of execution.
- **Characteristics:** Threads are lightweight compared to processes. Context switching between threads is faster.
- **Challenge:** Thread safety. Shared data must be protected to avoid race conditions and deadlocks.

### 4.3 Message Passing Model
- **Concept:** Processes have private memory and communicate exclusively by sending and receiving messages.
- **Characteristics:** Explicit communication. Well-suited for distributed memory systems.
- **API Examples:** Message Passing Interface (MPI), sockets.
- **Advantage:** Clear separation of data reduces unintended side effects.

### 4.4 Data-Parallel Model
- **Concept:** The same operation is applied simultaneously to multiple data elements. The focus is on distributing data across processors.
- **Characteristics:** Ideal for SIMD architectures and array-based computations.
- **API Examples:** OpenMP parallel for directives, CUDA kernels, NumPy vectorized operations.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart TD
    %% Premium Programming Models
    classDef container fill:#f8fafc,stroke:#cbd5e1,stroke-width:2px,color:#0f172a
    classDef thread fill:#e0f2fe,stroke:#0ea5e9,stroke-width:2px,color:#0369a1,font-weight:bold
    classDef data fill:#dcfce7,stroke:#22c55e,stroke-width:2px,color:#15803d

    subgraph SHARED_MODEL ["🧵 Threads: Shared Address Space"]
        direction LR
        subgraph SHARED_MEM ["Common Address Space"]
            direction TB
            DATA[("💾 Shared Variables")]
        end
        T1(Thread 1) --- DATA
        T2(Thread 2) --- DATA
        T3(Thread 3) --- DATA
    end

    subgraph PROC_MODEL ["🏭 Processes: Private Address Space"]
        direction LR
        subgraph P1_NODE ["Process A"]
            direction TB
            A_MEM[("💾 Private RAM")]
        end
        subgraph P2_NODE ["Process B"]
            direction TB
            B_MEM[("💾 Private RAM")]
        end
        P1_NODE <== "🔌 IPC: Message Passing" ==> P2_NODE
    end

    class SHARED_MODEL,PROC_MODEL container
    class T1,T2,T3,P1_NODE,P2_NODE thread
    class DATA,A_MEM,B_MEM data
```

## 5. Designing a Parallel Program

A systematic approach to parallel program design involves four key steps.

### 5.1 Task Decomposition
- **Definition:** Breaking down the overall computation into smaller, independent tasks that can potentially execute concurrently.
- **Approaches:**
  - *Domain Decomposition:* Partitioning the data, and each task processes a subset of the data.
  - *Functional Decomposition:* Partitioning the computation based on different functions or operations.

### 5.2 Task Assignment
- **Definition:** Assigning decomposed tasks to processors or threads.
- **Goal:** Balance the workload to ensure all processors are utilized efficiently and minimize idle time.

### 5.3 Agglomeration
- **Definition:** Combining small tasks into larger ones to reduce overhead.
- **Rationale:** Creating and managing many fine-grained tasks incurs communication and synchronization overhead. Agglomeration trades off some parallelism for reduced overhead.

### 5.4 Mapping
- **Definition:** Assigning the agglomerated tasks to specific physical processors.
- **Static Mapping:** Tasks are assigned to processors before execution. Suitable when task execution times are predictable.
- **Dynamic Mapping (5.5):** Tasks are assigned to processors at runtime. Suitable when task execution times are unpredictable or when the system is heterogeneous. Improves load balancing but adds scheduling overhead.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1', 'actorBorder': '#4f46e5', 'actorBkg': '#e0e7ff', 'actorTextColor': '#1e1b4b' }}}%%
sequenceDiagram
    autonumber
    actor Problem as 1. The Problem
    actor Decomp as 2. Decomposition
    actor Agglom as 3. Agglomeration
    actor Map as 4. Mapping
    
    Note over Problem,Map: Professional Parallel Design Lifecycle
    
    Problem->>Decomp: Identify Independent Tasks
    Decomp->>Agglom: Group Tasks for Performance
    Agglom->>Map: Allocate to Hardware Cores
    
    loop Real-time Tuning
        Map-->>Map: Optimization Loop
    end
```

## 6. Evaluating the Performance of a Parallel Program

Metrics to quantify the effectiveness of parallelization.

### 6.1 Speedup
- **Definition:** The ratio of the execution time of the best sequential algorithm to the execution time of the parallel algorithm on p processors.
- **Formula:** `S(p) = T(1) / T(p)`
- **Ideal Speedup:** Linear speedup (`S(p) = p`) means the program runs p times faster on p processors. Rarely achieved in practice due to overhead.

### 6.2 Efficiency
- **Definition:** Measures how well the processors are utilized. It is the speedup divided by the number of processors.
- **Formula:** `E(p) = S(p) / p = T(1) / (p * T(p))`
- **Interpretation:** Efficiency of 1 (or 100%) means perfect utilization. Values less than 1 indicate overhead from communication, synchronization, or load imbalance.

### 6.3 Scaling
- **Strong Scaling:** The problem size is fixed, and the number of processors is increased. Measures how much faster a fixed problem can be solved with more resources.
- **Weak Scaling:** The problem size per processor is fixed, and the total problem size grows with the number of processors. Measures the ability to solve larger problems with more resources.

### 6.4 Amdahl's Law
- **Statement:** The maximum speedup achievable by parallelizing a program is limited by the fraction of the program that must execute sequentially.
- **Formula:** `S(p) <= 1 / (f + (1-f)/p)`, where `f` is the sequential fraction.
- **Implication:** Even with infinite processors, speedup is bounded by `1/f`. If 10% of a program is sequential, maximum speedup is 10x.

### 6.5 Gustafson's Law
- **Statement:** As the number of processors increases, the problem size can also increase, allowing the parallel portion to dominate.
- **Formula:** `S(p) = p - f*(p-1)`
- **Implication:** For scalable problems, speedup can grow linearly with the number of processors by increasing the workload. Contrasts with Amdahl's Law by assuming the problem size scales with resources.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart TD
    %% Premium Performance Metrics
    classDef measure fill:#e0f2fe,stroke:#0ea5e9,stroke-width:2px,color:#0369a1,font-weight:bold
    classDef scaling fill:#dcfce7,stroke:#22c55e,stroke-width:2px,color:#15803d,font-weight:bold
    classDef bottleneck fill:#ffe4e6,stroke:#e11d48,stroke-width:2px,color:#4c0519,font-weight:bold

    subgraph EVAL_KPI ["📈 System Measurements"]
        direction TB
        S_RATIO["Speedup Ratio: S = T(1) / T(p)"]
        E_RATIO["Efficiency Index: E = S / p"]
    end

    subgraph SCALE_PATH ["⚖️ Scaling Dynamics"]
        direction LR
        STRONG["Strong Scaling: Fixed Problem Size"]
        WEAK["Weak Scaling: Scaled Problem Size"]
    end

    subgraph LIMITS ["⚠️ Critical Bottlenecks"]
        AMDAHL["Amdahl's Law: Sequential Limit"]
        GUSTAFSON["Gustafson's Law: Parallel Limit"]
    end

    EVAL_KPI ==> SCALE_PATH
    SCALE_PATH ==> LIMITS

    class S_RATIO,E_RATIO measure
    class STRONG,WEAK scaling
    class AMDAHL,GUSTAFSON bottleneck
```

## 7. Introducing Python

A brief overview of Python features relevant to parallel programming.

### 7.1 Help Functions
- `help()`: Provides interactive documentation for modules, classes, and functions.
- `dir()`: Lists the attributes and methods of an object.
- Essential for exploring libraries and understanding APIs without leaving the interpreter.

**Example Implementation:** See [dir.py](Codes/dir.py)

### 7.2 Syntax
- Python uses indentation (whitespace) to define code blocks, not braces.
- Simple, readable syntax reduces development time and improves code maintainability.

### 7.3 Comments
- Single-line: `# This is a comment`
- Multi-line: Enclosed in triple quotes (`"""` or `'''`), though these are technically string literals often used as docstrings.

### 7.4 Assignments
- Dynamic typing: Variables do not need explicit type declarations. Type is inferred from the assigned value.
- Multiple assignment: `a, b = 1, 2`
- Augmented assignment: `x += 1`

### 7.5 Data Types
- Built-in types: `int`, `float`, `bool`, `str`, `list`, `tuple`, `dict`, `set`.
- Mutable vs Immutable: Lists, dicts, sets are mutable (can be changed). Strings, tuples, numbers are immutable (cannot be changed after creation). Important for understanding behavior in concurrent contexts.

### 7.6 Strings
- Immutable sequences of characters.
- Support slicing, formatting, and a rich set of methods for manipulation.

### 7.7 Flow Control
- Conditional: `if`, `elif`, `else`
- Loops: `for` (iterates over sequences), `while` (condition-based)
- Loop control: `break`, `continue`, `pass`

**Example Implementation:** See [flow.py](Codes/flow.py)

### 7.8 Functions
- Defined using `def` keyword.
- Support default arguments, variable-length arguments (`*args`, `**kwargs`), and keyword-only arguments.
- First-class objects: Functions can be passed as arguments, returned from other functions, and assigned to variables.

**Example Implementation:** See [do_something.py](Codes/do_something.py)

### 7.9 Classes
- Python supports Object-Oriented Programming with classes.
- Key concepts: inheritance, encapsulation, polymorphism.
- Special methods (e.g., `__init__`, `__str__`) enable customization of object behavior.

**Example Implementation:** See [classes.py](Codes/classes.py)

### 7.10 Exceptions
- Error handling using `try`, `except`, `else`, `finally` blocks.
- Built-in exception hierarchy (`Exception`, `ValueError`, `TypeError`, etc.).
- Custom exceptions can be defined by inheriting from `Exception`.
- Critical for writing robust parallel programs that can handle errors in individual threads or processes.

### 7.11 Importing Libraries
- `import module`: Imports an entire module.
- `from module import name`: Imports specific names from a module.
- `import module as alias`: Imports with an alias for convenience.
- Modules are the primary mechanism for code organization and reuse in Python.

### 7.12 Managing Files
- `open()` function to open files with modes: `'r'` (read), `'w'` (write), `'a'` (append), `'b'` (binary).
- Context manager (`with` statement) ensures files are properly closed: `with open('file.txt', 'r') as f: ...`
- Essential for I/O-bound parallel tasks.

**Example Implementation:** See [file.py](Codes/file.py)

### 7.13 List Comprehensions
- Concise syntax for creating lists: `[x**2 for x in range(10) if x % 2 == 0]`
- More efficient and readable than equivalent for-loops with `append()`.
- Can be parallelized using libraries like multiprocessing for large datasets.

**Example Implementation:** See [lists.py](Codes/lists.py)

### 7.14 Running Python Scripts
- Command line: `python script.py`
- Shebang line (`#!/usr/bin/env python3`) allows direct execution on Unix-like systems.
- `__name__ == "__main__"` idiom: Code inside this block runs only when the script is executed directly, not when imported as a module. Crucial for parallel programming to avoid unintended process/thread spawning on import.

### 7.15 Installing Python Packages Using pip
- `pip` is the standard package installer for Python.
- Installing pip (7.16): Usually bundled with modern Python installations. Can be installed via `get-pip.py` if missing.
- Updating pip (7.17): `python -m pip install --upgrade pip`
- Using pip (7.18):
  - Install: `pip install package_name`
  - Uninstall: `pip uninstall package_name`
  - List: `pip list`
  - Requirements file: `pip install -r requirements.txt` (for reproducible environments)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#4f46e5', 'primaryColor': '#e0e7ff', 'primaryTextColor': '#1e1b4b', 'primaryBorderColor': '#818cf8' }}}%%
mindmap
  root("🐍 Python Parallelism Ecosystem")
    Architecture
      Dynamic Typing
      Indentation Logic
      Interpreted Nature
    Introspection
      Help Utility
      Dir Inspector
    Data Handling
      Mutable Collections
      Immutable Containers
    Standard Toolkit
      Pip Package Manager
      Multiprocessing
      Threading
```

## 8. Introducing Python Parallel Programming

### 8.1 Processes and Threads
- **Process:** An independent program in execution with its own memory space. Created using the multiprocessing module. Inter-process communication (IPC) requires explicit mechanisms (pipes, queues, shared memory).
- **Thread:** A lightweight unit of execution within a process. Created using the threading module. Threads share memory, enabling fast communication but requiring synchronization to avoid race conditions.
- **Choice Between Them:**
  - Use threads for I/O-bound tasks (network, disk) where the GIL is released during I/O operations.
  - Use processes for CPU-bound tasks to bypass the GIL and achieve true parallelism on multi-core systems.
- **Global Interpreter Lock (GIL):** A mutex in CPython that allows only one thread to execute Python bytecode at a time. It simplifies memory management but limits CPU-bound multi-threaded performance. Multiprocessing circumvents the GIL by using separate processes, each with its own Python interpreter and GIL.

**Serial Execution Implementation:** See [serial_test.py](Codes/serial_test.py)

**Multi-Threading Implementation:** See [multithreading_test.py](Codes/multithreading_test.py)

**Multi-Processing Implementation:** See [multiprocessing_test.py](Codes/multiprocessing_test.py)

**Combined Threads & Processes Benchmarking Implementation:** See [thread_and_processes.py](Codes/thread_and_processes.py)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart TD
    %% Premium Python Parallel Architecture
    classDef threadBox fill:#fffbeb,stroke:#d97706,stroke-width:2px,color:#451a03,font-weight:bold
    classDef procBox fill:#f0fdf4,stroke:#16a34a,stroke-width:2px,color:#14532d,font-weight:bold
    classDef lock fill:#fee2e2,stroke:#ef4444,stroke-width:2px,color:#7f1d1d,font-weight:bold
    classDef threadNode fill:#e0f2fe,stroke:#0ea5e9,stroke-width:1.5px,color:#0369a1

    subgraph MultiThreading ["🧵 Python Multi-Threading"]
        direction TB
        Mem[("💾 Shared RAM")]
        Mem --- GIL{{"🔒 GIL Lock"}}
        GIL ==> T1(("Thread 1"))
        GIL ==> T2(("Thread 2"))
        note1["*Concurrency via GIL Interweaving*"]
    end
    
    subgraph MultiProcessing ["🏭 Python Multi-Processing"]
        direction TB
        subgraph P1 ["Process 1"]
            G1["🔒 GIL"] --- Th1(("Main Thread"))
        end
        subgraph P2 ["Process 2"]
            G2["🔒 GIL"] --- Th2(("Main Thread"))
        end
        note2["*Parallelism via Isolated Interpreters*"]
    end

    class MultiThreading threadBox
    class MultiProcessing procBox
    class GIL,G1,G2 lock
    class T1,T2,Th1,Th2 threadNode
```
