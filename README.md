# Parallel & Distributed Computing (PDC-SP26-SE)

Welcome to the **Parallel & Distributed Computing (PDC)** learning portfolio of Muhammad Affan. This repository documents key theoretical concepts, practical implementations, and programming paradigms covered from Chapter 1 through Chapter 7.

> [!NOTE]  
> **Course Assignment Submission**  
> This portfolio and implementation work has been developed as an assignment under the supervision of **Miss Rameen Anwar**.

---

## Table of Contents
1. [Chapter 1: Getting Started with Parallel Computing & Python](#chapter-1-getting-started-with-parallel-computing--python)
2. [Chapter 2: Thread-Based Parallelism](#chapter-2-thread-based-parallelism)
3. [Chapter 3: Process-Based Parallelism](#chapter-3-process-based-parallelism)
4. [Chapter 4: Message Passing (MPI)](#chapter-4-message-passing-mpi)
5. [Chapter 5: Asynchronous Programming](#chapter-5-asynchronous-programming)
6. [Chapter 6: Distributed Python](#chapter-6-distributed-python)
7. [Chapter 7: Cloud Computing, Containers, & Serverless](#chapter-7-cloud-computing-containers--serverless)

---

## Chapter 1: Getting Started with Parallel Computing & Python

Introduces the fundamentals of high-performance computing, the distinction between concurrency and parallelism, and Flynn's Taxonomy.

### Concurrency vs. Parallelism
- **Concurrency:** Dealing with multiple things at once (overlapping execution on a single core via time slicing).
- **Parallelism:** Doing multiple things at the same time (simultaneous execution on multiple CPU cores).

```mermaid
graph TD
    %% Styling Definition
    classDef concur fill:#E67E22,stroke:#D35400,stroke-width:2px,color:#fff;
    classDef paral fill:#2ECC71,stroke:#27AE60,stroke-width:2px,color:#fff;
    
    subgraph Concurrency_Model["Concurrency (Single Core - Context Switching)"]
        Core1[CPU Core] --> TaskA1[Task A]
        Core1 --> TaskB1[Task B]
        Core1 --> TaskA2[Task A]
    end
    
    subgraph Parallelism_Model["Parallelism (Multi-Core - Simultaneous Execution)"]
        CoreA[Core A] --> TaskA[Task A]
        CoreB[Core B] --> TaskB[Task B]
    end
    
    class Core1,TaskA1,TaskB1,TaskA2 concur;
    class CoreA,CoreB,TaskA,TaskB paral;
```

**Explore Chapter:** [Chapter01 Folder](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter01)

---

## Chapter 2: Thread-Based Parallelism

Focuses on utilizing multiple threads within a single process to execute tasks concurrently. It covers Python’s `threading` module, race conditions, synchronization primitives, and the Global Interpreter Lock (GIL).

### Thread Synchronization & Lock Mechanism
When multiple threads access shared resources, data corruption (race conditions) can occur. **Locks (Mutexes)** guarantee that only one thread accesses a critical section at any given time.

```mermaid
graph TD
    %% Styling Definition
    classDef thread fill:#3498DB,stroke:#2980B9,stroke-width:2px,color:#fff;
    classDef lock fill:#E74C3C,stroke:#C0392B,stroke-width:2px,color:#fff;
    classDef resource fill:#F1C40F,stroke:#D68910,stroke-width:2px,color:#000;

    T1[Thread 1] -->|1. Acquires Lock| Mutex{Lock/Mutex}:::lock
    T2[Thread 2] -->|2. Blocked / Waits| Mutex
    Mutex -->|3. Updates safely| Shared[Shared Resource/Variable]:::resource
    
    class T1,T2 thread;
```

**Explore Chapter:** [Chapter02 Folder](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter02)

---

## Chapter 3: Process-Based Parallelism

Since Python's GIL prevents multiple threads from running Python code in parallel on separate cores, Process-Based Parallelism runs tasks on completely separate operating system processes, bypassing the GIL.

### Memory Layout: Threading vs. Multiprocessing

```mermaid
graph TD
    %% Styling Definition
    classDef proc fill:#34495E,stroke:#2C3E50,stroke-width:2px,color:#fff;
    classDef mem fill:#1ABC9C,stroke:#16A085,stroke-width:2px,color:#fff;
    classDef child fill:#9B59B6,stroke:#8E44AD,stroke-width:2px,color:#fff;

    subgraph Threading_Model["Threading (Shared Memory Space)"]
        P1[Parent Process]:::proc --> SharedMem[Common Memory Space]:::mem
        SharedMem --> T1[Thread A]:::child
        SharedMem --> T2[Thread B]:::child
    end

    subgraph Multiprocessing_Model["Multiprocessing (Isolated Memory Spaces)"]
        ParentP[Parent Process]:::proc -->|Forks / Spawns| ChildP1[Child Process 1]:::child
        ParentP -->|Forks / Spawns| ChildP2[Child Process 2]:::child
        ChildP1 --> Mem1[Memory Space 1]:::mem
        ChildP2 --> Mem2[Memory Space 2]:::mem
    end
```

**Explore Chapter:** [Chapter03 Folder](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter03)

---

## Chapter 4: Message Passing (MPI)

Introduces distributed memory parallelism using the **Message Passing Interface (MPI)** via the `mpi4py` library. Processes execute independently and coordinate by exchanging messages.

### Collective Communication Operations
- **Broadcast (bcast):** A single master process sends data to all other processes.
- **Scatter:** A master process divides an array/list and distributes portions to each process.
- **Gather:** Reverses Scatter by collecting individual results back into a single array on the master.

```mermaid
graph TD
    %% Styling Definition
    classDef master fill:#E74C3C,stroke:#C0392B,stroke-width:2px,color:#fff;
    classDef worker fill:#3498DB,stroke:#2980B9,stroke-width:2px,color:#fff;

    subgraph Broadcast_Op["Broadcast (One-to-All)"]
        M0[Root Process <br/> Data: A]:::master -->|Sends Copy| W1[Process 1 <br/> Data: A]:::worker
        M0 -->|Sends Copy| W2[Process 2 <br/> Data: A]:::worker
    end

    subgraph Scatter_Op["Scatter (Divide & Distribute)"]
        M1[Root Process <br/> Data: A, B, C]:::master -->|Slice 1| W3[Process 1 <br/> Data: A]:::worker
        M1 -->|Slice 2| W4[Process 2 <br/> Data: B]:::worker
    end
```

**Explore Chapter:** [Chapter04 Folder](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter04)

---

## Chapter 5: Asynchronous Programming

Explores single-threaded concurrency using Python's `asyncio` module. Instead of multi-threading or multi-processing, asynchronous code runs in a loop (Event Loop) and yields control during slow I/O operations (web requests, disk access).

### Asynchronous Event Loop Workflow

```mermaid
graph TD
    %% Styling Definition
    classDef loop fill:#9B59B6,stroke:#8E44AD,stroke-width:2px,color:#fff;
    classDef io fill:#E67E22,stroke:#D35400,stroke-width:2px,color:#fff;
    classDef task fill:#2ECC71,stroke:#27AE60,stroke-width:2px,color:#fff;

    Queue[Task Queue] --> Loop((Event Loop)):::loop
    Loop -->|1. Run Task| ActiveTask[Task Running]:::task
    ActiveTask -->|2. Slow I/O Triggered| IO[Non-blocking I/O Operation]:::io
    IO -->|3. Yield Control| Loop
    IO -->|4. Complete event| Queue
```

**Explore Chapter:** [Chapter05 Folder](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter05)

---

## Chapter 6: Distributed Python

Covers distributed computing frameworks. Using **Pyro4** (Remote Method Invocation) and **Celery** (Distributed Task Queue), code execution is offloaded across distinct networked machines.

### Celery & Message Broker Architecture

```mermaid
graph LR
    %% Styling Definition
    classDef client fill:#E74C3C,stroke:#C0392B,stroke-width:2px,color:#fff;
    classDef broker fill:#F39C12,stroke:#D35400,stroke-width:2px,color:#fff;
    classDef worker fill:#2ECC71,stroke:#27AE60,stroke-width:2px,color:#fff;

    Producer[Flask Web App]:::client -->|Publish Task| Broker[(Redis / RabbitMQ Broker)]:::broker
    Broker -->|Fetch & Process| Worker1[Celery Worker 1]:::worker
    Broker -->|Fetch & Process| Worker2[Celery Worker 2]:::worker
```

**Explore Chapter:** [Chapter06 Folder](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter06)

---

## Chapter 7: Cloud Computing, Containers, & Serverless

Summarizes modern cloud deployment paradigms including Service Models (IaaS, PaaS, SaaS), deployment on PythonAnywhere, containerization using Docker, and event-driven Serverless (Lambda) computing.

### Docker Container Lifecycle
Docker builds code, runtimes, and configs into a static image template, which is spun up as an isolated execution container environment.

```mermaid
graph TD
    %% Styling
    classDef dockerfile fill:#F39C12,stroke:#D35400,stroke-width:2px,color:#fff;
    classDef engine fill:#3498DB,stroke:#2980B9,stroke-width:2px,color:#fff;
    classDef container fill:#2ECC71,stroke:#27AE60,stroke-width:2px,color:#fff;

    DF[Dockerfile]:::dockerfile -->|docker build| Img[Docker Image]:::engine
    Img -->|docker run| Container[Container Instance]:::container
```

**Explore Chapter:** [Chapter07 Folder](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter07)
