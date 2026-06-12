#  PDC Learning Portfolio — Muhammad Bilal Imtiaz
### Parallel & Distributed Computing · SP26-SE · Supervised by Miss Rameen Anwar

---

> *"Sequential code is a bottleneck. Parallelism is the escape."*

This portfolio documents the theoretical foundations and practical implementations from **Chapters 1–7** of the PDC course — covering everything from Python threads to cloud-native serverless architectures.

---

## 🗂 Index

| # | Topic | Core Concept |
|---|-------|-------------|
| 01 | [Getting Started](#01--getting-started) | Concurrency vs Parallelism, Flynn's Taxonomy |
| 02 | [Thread-Based Parallelism](#02--thread-based-parallelism) | `threading`, GIL, Locks |
| 03 | [Process-Based Parallelism](#03--process-based-parallelism) | `multiprocessing`, Memory Isolation |
| 04 | [Message Passing (MPI)](#04--message-passing-mpi) | `mpi4py`, Scatter / Gather / Broadcast |
| 05 | [Async Programming](#05--async-programming) | `asyncio`, Event Loop, Non-blocking I/O |
| 06 | [Distributed Python](#06--distributed-python) | Pyro4, Celery, Message Brokers |
| 07 | [Cloud & Containers](#07--cloud--containers) | Docker, IaaS/PaaS/SaaS, Serverless |

---

## 01 · Getting Started

**Concurrency** and **parallelism** look similar but are fundamentally different:

- **Concurrency** → one core, multiple tasks interleaved via context switching
- **Parallelism** → multiple cores, multiple tasks running *simultaneously*

```
CONCURRENCY (Single Core)         PARALLELISM (Multi-Core)
─────────────────────────         ────────────────────────
Core: [A][B][A][B][A]             Core 1: [A][A][A]
       ↑ interleaved              Core 2: [B][B][B]
                                          ↑ simultaneous
```

Flynn's Taxonomy classifies computer architectures by instruction and data streams (SISD → MIMD).

 [Chapter 01](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter01)

---

## 02 · Thread-Based Parallelism

Python's `threading` module enables concurrent execution within a **single process**. However, the **GIL (Global Interpreter Lock)** ensures only one thread executes Python bytecode at a time — making threads best suited for **I/O-bound** tasks.

**The Race Condition Problem:**
Two threads incrementing the same counter without coordination → unpredictable results.

**The Fix — Mutex Lock:**
```
Thread 1 ──► acquires Lock ──► reads/writes shared variable ──► releases Lock
Thread 2 ──►     BLOCKED     ──────────────────────────────► acquires Lock
```

Key primitives: `Lock`, `RLock`, `Semaphore`, `Event`, `Condition`, `Barrier`

 [Chapter 02](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter02)

---

## 03 · Process-Based Parallelism

To truly bypass the GIL, spawn **separate OS processes**. Each process gets its own memory space — no sharing, no corruption.

**Memory Model Comparison:**

```
THREADING                         MULTIPROCESSING
──────────────────────            ──────────────────────────────
 Parent Process                    Parent Process
     └── Shared Memory                 ├── Child 1 → [Mem A]
           ├── Thread A                └── Child 2 → [Mem B]
           └── Thread B               (completely isolated)
```

Use `multiprocessing.Pool` for parallel map operations, `Queue` / `Pipe` for IPC.

 [Chapter 03](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter03)

---

## 04 · Message Passing (MPI)

`mpi4py` brings **MPI (Message Passing Interface)** to Python — the standard for distributed-memory HPC clusters where processes on different machines communicate via messages.

**Collective Operations at a Glance:**

| Operation | Direction | What it does |
|-----------|-----------|--------------|
| `bcast` | 1 → All | Root sends the same data to every process |
| `scatter` | 1 → All | Root splits data; each process gets a unique chunk |
| `gather` | All → 1 | All processes send results back to root |
| `reduce` | All → 1 | Gather + apply an operation (sum, max, etc.) |

 [Chapter 04](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter04)

---

## 05 · Async Programming

`asyncio` achieves **concurrency without threads** — a single thread drives an event loop that switches between tasks whenever one is waiting on I/O.

**Event Loop Lifecycle:**
```
  ┌──────────────────────────────────────────┐
  │              EVENT LOOP                  │
  │                                          │
  │  Task Queue → pick task → run until      │
  │  await hit → suspend → pick next task    │
  │  I/O done? → resume suspended task       │
  └──────────────────────────────────────────┘
```

Best for: network requests, file I/O, websockets — anything **I/O-bound** with many simultaneous operations.

 [Chapter 05](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter05)

---

## 06 · Distributed Python

Scale beyond a single machine using two approaches:

**Pyro4** — Remote Method Invocation: call methods on objects living on other machines as if they were local.

**Celery** — Distributed Task Queue:
```
Flask App (Producer)
    │
    ▼  publish task
Redis / RabbitMQ (Broker)
    │
    ├──► Celery Worker 1
    └──► Celery Worker 2
```

Workers pick up tasks from the broker independently — enabling horizontal scaling and background job processing.

 [Chapter 06](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter06)

---

## 07 · Cloud & Containers

Modern deployment paradigms — from managing raw infrastructure to abstracting it away entirely.

**Service Model Spectrum:**

```
More Control ◄──────────────────────────► Less Control
    IaaS              PaaS                   SaaS
  (VMs, storage)  (runtime + platform)   (ready-to-use app)
  AWS EC2          PythonAnywhere          Gmail
```

**Docker in 3 Steps:**
```
Dockerfile  ──[docker build]──►  Image  ──[docker run]──►  Container
(blueprint)                   (template)               (running instance)
```

**Serverless (Lambda):** No server management — deploy a function, pay only when it runs. Triggered by events (HTTP, queue, timer).

 [Chapter 07](file:///c:/Semester6/Parallel%20Distributed%20and%20Computing/Muhammad-Affan-23FA-003-SE/Muhammad-Affan-23FA-003-SE/Chapter07)

---

*Muhammad Bilal Imtiaz · 23FA-025-SE · PDC-SP26*
