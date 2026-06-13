# Chapter 01 — Getting Started with Parallel Computing and Python

> Serial vs Threading vs Multiprocessing — a hands-on comparison exploring Python's GIL and true parallelism.

---

## 📁 Files Overview

| File | Concept | Description |
|------|---------|-------------|
| `dir.py` | Help & Flow | Checks if a number is positive/negative/zero; sums a list using a for loop |
| `flow.py` | Flow Control | Demonstrates `if/elif/else`, `for` loop, and `while` loop |
| `lists.py` | Data Types | Shows usage of lists, dictionaries, tuples, and function references |
| `classes.py` | OOP / Classes | Demonstrates class variables, instance variables, and inheritance |
| `do_something.py` | Functions | Helper function that generates random numbers into a list |
| `file.py` | File I/O | Writes and reads a text file using `open()` |
| `serial_test.py` | Serial Execution | Runs `do_something()` 10 times sequentially and measures time |
| `multithreading_test.py` | Multithreading | Runs `do_something()` across 10 threads and measures time |
| `multiprocessing_test.py` | Multiprocessing | Runs `do_something()` across 10 processes and measures time |
| `thread_and_processes.py` | Combined Comparison | Compares multithreading vs multiprocessing in a single script |

---

## 🗂️ File Dependency Map

```mermaid
graph TD
    DS[do_something.py\nGenerates 10M random floats]

    DS --> ST[serial_test.py\nSequential - ~38s]
    DS --> MT[multithreading_test.py\nThreads - ~40s]
    DS --> MP[multiprocessing_test.py\nProcesses - ~10s]

    TP[thread_and_processes.py\nSide-by-side comparison]

    subgraph Basics
        D[dir.py]
        F[flow.py]
        L[lists.py]
        C[classes.py]
        FI[file.py]
    end

    subgraph Performance Tests
        ST
        MT
        MP
        TP
    end

    style DS fill:#064e3b,color:#6ee7b7,stroke:#10b981
    style ST fill:#1e3a5f,color:#93c5fd,stroke:#2563eb
    style MT fill:#2d1b69,color:#c4b5fd,stroke:#7c3aed
    style MP fill:#064e3b,color:#6ee7b7,stroke:#10b981
    style TP fill:#78350f,color:#fcd34d,stroke:#f59e0b
```

---

## ⏱️ Execution Flow Comparison

```mermaid
gantt
    title Execution Timeline — 10 Tasks (CPU-bound)
    dateFormat  X
    axisFormat  t=%ss

    section 🔵 Serial
    Task 1          :s1, 0, 4
    Task 2          :s2, 4, 8
    Task 3          :s3, 8, 12
    Task 4          :s4, 12, 16
    Task 5          :s5, 16, 20
    Task 6          :s6, 20, 24
    Task 7          :s7, 24, 28
    Task 8          :s8, 28, 32
    Task 9          :s9, 32, 36
    Task 10         :s10, 36, 40

    section 🟣 Threading (GIL)
    Th-1 running    :t1, 0, 40
    Th-2 wait+run   :t2, 1, 40
    Th-3 wait+run   :t3, 2, 40

    section 🟢 Multiprocessing
    Process 1       :p1, 0, 10
    Process 2       :p2, 0, 10
    Process 3       :p3, 0, 10
    Process 4       :p4, 0, 10
```

> 🔵 **Serial** — ek kaam khatam, phir agla. Total ~38s  
> 🟣 **Threading** — sab threads chalte hain par GIL ki wajah se sirf ek hi execute hota hai. Total ~40s  
> 🟢 **Multiprocessing** — sab processes truly parallel chalte hain. Total ~10s

---

## 🔒 GIL (Global Interpreter Lock) — Kya hota hai?

```mermaid
flowchart LR
    subgraph THREADING ["🔴 Multithreading — GIL Bottleneck"]
        direction TB
        G[🔒 GIL\nSirf 1 thread\nek waqt]
        T1[Thread 1\n✅ Running]
        T2[Thread 2\n⏸ Waiting]
        T3[Thread 3\n⏸ Waiting]
        T4[Thread 4\n⏸ Waiting]
        G --> T1
        G -.->|blocked| T2
        G -.->|blocked| T3
        G -.->|blocked| T4
    end

    subgraph MULTIPROC ["🟢 Multiprocessing — True Parallel"]
        direction TB
        C0[Core 0\n✅ Process 1]
        C1[Core 1\n✅ Process 2]
        C2[Core 2\n✅ Process 3]
        C3[Core 3\n✅ Process 4]
    end

    style THREADING fill:#1a0a0a,stroke:#ef4444,color:#fca5a5
    style MULTIPROC fill:#022c1a,stroke:#10b981,color:#6ee7b7
    style G fill:#7f1d1d,color:#fca5a5,stroke:#ef4444
    style T1 fill:#14532d,color:#86efac,stroke:#22c55e
    style T2 fill:#1c1917,color:#78716c,stroke:#57534e
    style T3 fill:#1c1917,color:#78716c,stroke:#57534e
    style T4 fill:#1c1917,color:#78716c,stroke:#57534e
    style C0 fill:#14532d,color:#86efac,stroke:#22c55e
    style C1 fill:#14532d,color:#86efac,stroke:#22c55e
    style C2 fill:#14532d,color:#86efac,stroke:#22c55e
    style C3 fill:#14532d,color:#86efac,stroke:#22c55e
```

| | Threading | Multiprocessing |
|---|---|---|
| GIL | ❌ Affected (bottleneck) | ✅ Bypassed |
| True Parallelism | ❌ No (CPU-bound) | ✅ Yes |
| Memory | Shared | Separate per process |
| Best For | I/O-bound tasks | CPU-bound tasks |

---

## 📊 Performance Benchmark

```mermaid
xychart-beta horizontal
    title "Execution Time — 10M floats × 10 tasks (seconds)"
    x-axis ["Serial", "Multithreading", "Multiprocessing"]
    y-axis "Time (seconds)" 0 --> 45
    bar [38.45, 40.12, 9.87]
```

> ✅ **Multiprocessing is ~4× faster** than serial on a 4-core machine.  
> ⚠️ Multithreading is even **slower** than serial due to GIL switching overhead.

---

## 🧠 Flynn's Taxonomy

```mermaid
quadrantChart
    title Flynn's Taxonomy — Parallel Architecture Classification
    x-axis Single Data --> Multiple Data
    y-axis Single Instruction --> Multiple Instruction
    quadrant-1 MIMD
    quadrant-2 SIMD
    quadrant-3 SISD
    quadrant-4 MISD
    SISD - Classic CPU: [0.25, 0.25]
    SIMD - GPU / AVX: [0.75, 0.25]
    MIMD - Multicore / Clusters: [0.75, 0.75]
    MISD - Fault Tolerant Systems: [0.25, 0.75]
```

| Taxonomy | Full Name | Description | Example |
|----------|-----------|-------------|---------|
| **SISD** | Single Instruction, Single Data | Traditional serial — one CPU, one stream | Classic single-core CPU |
| **SIMD** | Single Instruction, Multiple Data | Same instruction on many data elements | GPU, SSE, AVX |
| **MISD** | Multiple Instruction, Single Data | Multiple instructions, same data — rare | Fault-tolerant systems |
| **MIMD** | Multiple Instruction, Multiple Data | Most common parallel model | Multicore CPUs, clusters |

---

## 📐 Performance Metrics

```mermaid
flowchart TD
    A[Program runs on\np processors] --> B[Measure T_1\nSerial time]
    A --> C[Measure T_p\nParallel time]

    B --> D["⚡ Speedup\nS(p) = T(1) / T(p)"]
    C --> D

    D --> E["📊 Efficiency\nE(p) = S(p) / p"]
    D --> F["📉 Amdahl's Law\nS = 1 / (f + (1-f)/p)\nLimited by serial fraction f"]
    D --> G["📈 Gustafson's Law\nS = p - f·(p-1)\nOptimistic — scales with problem size"]

    style A fill:#1e3a5f,color:#93c5fd,stroke:#2563eb
    style B fill:#1c1917,color:#d6d3d1,stroke:#57534e
    style C fill:#1c1917,color:#d6d3d1,stroke:#57534e
    style D fill:#064e3b,color:#6ee7b7,stroke:#10b981
    style E fill:#2d1b69,color:#c4b5fd,stroke:#7c3aed
    style F fill:#78350f,color:#fcd34d,stroke:#f59e0b
    style G fill:#1e3a5f,color:#93c5fd,stroke:#2563eb
```

| Formula | Name | Meaning |
|---------|------|---------|
| `S(p) = T(1) / T(p)` | Speedup | Kitna fast hua parallel se? |
| `E(p) = S(p) / p` | Efficiency | Processors kitne efficiently use hue? |
| `S = 1 / (f + (1-f)/p)` | Amdahl's Law | Serial fraction `f` speedup ko limit karta hai |
| `S = p - f(p-1)` | Gustafson's Law | Problem size bade to parallel portion dominant hota hai |

---

## 🔄 Python Class Inheritance Flow

```mermaid
classDiagram
    class Myclass {
        +int common = 10
        +int myvariable
        +myfunction(arg1, arg2)
    }

    class AnotherClass {
        +myfunction(arg1, arg2)
    }

    Myclass <|-- AnotherClass : inherits
```

---

## 🗃️ File I/O Flow (`file.py`)

```mermaid
flowchart LR
    A[🖊️ open\ntest.txt - w] --> B[f.write\nfirst line]
    B --> C[f.write\nsecond line]
    C --> D[f.close]
    D --> E[📖 open\ntest.txt - r]
    E --> F[f.read]
    F --> G[🖥️ print output]

    style A fill:#1e3a5f,color:#93c5fd,stroke:#2563eb
    style E fill:#064e3b,color:#6ee7b7,stroke:#10b981
    style G fill:#2d1b69,color:#c4b5fd,stroke:#7c3aed
```

---

## ▶️ How to Run

```bash
# Basic Python concepts
python dir.py
python flow.py
python lists.py
python classes.py
python file.py

# Performance tests — do_something.py must be in same folder
python serial_test.py           # baseline benchmark   ~38s
python multithreading_test.py   # GIL demo             ~40s
python multiprocessing_test.py  # true parallelism     ~10s
python thread_and_processes.py  # side-by-side compare
```

> ⚠️ `serial_test.py`, `multithreading_test.py`, and `multiprocessing_test.py` — teeno files ke saath `do_something.py` **same folder** mein hona zaroori hai.

---

## 📋 Performance Summary

| Method | GIL Affected? | True Parallelism? | Best For | Time |
|--------|:---:|:---:|----------|------|
| Serial | — | ❌ | Baseline | ~38s |
| Multithreading | ❌ Yes | ❌ No | I/O-bound tasks | ~40s |
| Multiprocessing | ✅ No | ✅ Yes | CPU-bound tasks | ~10s |

> **Key Insight:** CPU-bound tasks (jaise millions of random numbers generate karna) ke liye multiprocessing best hai kyunki yeh Python ke GIL ko bypass karta hai alag processes use karke.
