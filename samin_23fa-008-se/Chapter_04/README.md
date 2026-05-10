# Chapter 04 — Message Passing Interface (MPI) with Python

> `mpi4py` — Distributed Memory Parallelism: Point-to-Point, Collective Communication & Virtual Topologies.

---

## 📁 Files Overview

| File | Concept | Description |
|------|---------|-------------|
| `helloworld_MPI.py` | MPI Basics | Minimal "Hello World" across all processes |
| `pointToPointCommunication.py` | Point-to-Point | `send()` and `recv()` between specific ranks |
| `broadcast.py` | Collective — Broadcast | `bcast()` — one process shares data to all |
| `scatter.py` | Collective — Scatter | `scatter()` — distributes array chunks to all processes |
| `gather.py` | Collective — Gather | `gather()` — collects data from all processes to root |
| `alltoall.py` | Collective — All-to-All | `Alltoall()` — every process sends & receives from all |
| `reduction.py` | Collective — Reduce | `Reduce()` with `MPI.SUM` — global aggregation |
| `deadLockProblems.py` | Pitfall — Deadlock | Blocking `send/recv` order mismatch causing hang |
| `virtualTopology.py` | Virtual Topology | 2D Cartesian grid with periodic boundaries |

---

## 🗂️ File Dependency Map

```mermaid
graph TD
    subgraph Basics ["🟢 MPI Foundations"]
        HW[helloworld_MPI.py\nHello World]
        P2P[pointToPointCommunication.py\nSend & Recv]
    end

    subgraph Collective ["🔵 Collective Communication"]
        BC[broadcast.py\nOne-to-All]
        SC[scatter.py\nDistribute Array]
        GA[gather.py\nCollect Results]
        AA[alltoall.py\nAll-to-All Exchange]
        RE[reduction.py\nParallel Sum]
    end

    subgraph Advanced ["🟣 Advanced Patterns"]
        DL[deadLockProblems.py\nDeadlock Demo]
        VT[virtualTopology.py\n2D Cartesian Grid]
    end

    HW --> P2P
    P2P --> BC
    BC --> SC
    SC --> GA
    GA --> AA
    AA --> RE
    RE --> DL
    DL --> VT

    style Basics fill:#064e3b,color:#6ee7b7,stroke:#10b981
    style Collective fill:#1e3a5f,color:#93c5fd,stroke:#2563eb
    style Advanced fill:#2d1b69,color:#c4b5fd,stroke:#7c3aed
    style HW fill:#14532d,color:#86efac,stroke:#22c55e
    style P2P fill:#14532d,color:#86efac,stroke:#22c55e
    style BC fill:#1e40af,color:#bfdbfe,stroke:#3b82f6
    style SC fill:#1e40af,color:#bfdbfe,stroke:#3b82f6
    style GA fill:#1e40af,color:#bfdbfe,stroke:#3b82f6
    style AA fill:#1e40af,color:#bfdbfe,stroke:#3b82f6
    style RE fill:#1e40af,color:#bfdbfe,stroke:#3b82f6
    style DL fill:#4c1d95,color:#c4b5fd,stroke:#7c3aed
    style VT fill:#4c1d95,color:#c4b5fd,stroke:#7c3aed
```

---

## ⏱️ Communication Pattern Comparison

```mermaid
gantt
    title MPI Collective Operations — Data Flow Timeline
    dateFormat  X
    axisFormat  Phase %s

    section 🔵 Broadcast (0→All)
    Root sends           :b1, 0, 1
    All receive          :b2, 1, 2

    section 🟢 Scatter (0→All chunks)
    Root splits array    :s1, 0, 1
    Each gets chunk      :s2, 1, 2

    section 🟡 Gather (All→0)
    All send to root     :g1, 0, 2
    Root assembles       :g2, 2, 3

    section 🟣 All-to-All
    All exchange data    :a1, 0, 3

    section 🔴 Reduce (All→0 SUM)
    All compute partial  :r1, 0, 1
    Root aggregates      :r2, 1, 2
```

> 🔵 **Broadcast** — 1→N: Root sends same data to everyone  
> 🟢 **Scatter** — 1→N: Root distributes *different* chunks to each  
> 🟡 **Gather** — N→1: Root collects data from everyone  
> 🟣 **All-to-All** — N↔N: Everyone exchanges with everyone  
> 🔴 **Reduce** — N→1: Root aggregates with operation (SUM, MAX, etc.)

---

## 🔄 MPI Communication Patterns Visualized

```mermaid
flowchart LR
    subgraph BROADCAST ["📢 Broadcast — One-to-All"]
        direction TB
        R0b[Root 0\nData = 100]
        P1b[Process 1\nGets 100]
        P2b[Process 2\nGets 100]
        P3b[Process 3\nGets 100]
        R0b --> P1b
        R0b --> P2b
        R0b --> P3b
    end

    subgraph SCATTER ["📤 Scatter — Distribute Chunks"]
        direction TB
        R0s[Root 0\nArray = 1,2,3,4]
        P1s[Process 1\nGets 1]
        P2s[Process 2\nGets 2]
        P3s[Process 3\nGets 3]
        P4s[Process 4\nGets 4]
        R0s --> P1s
        R0s --> P2s
        R0s --> P3s
        R0s --> P4s
    end

    subgraph GATHER ["📥 Gather — Collect to Root"]
        direction TB
        R0g[Root 0\nAssembles all]
        C1g[Process 1\nValue = 4]
        C2g[Process 2\nValue = 9]
        C3g[Process 3\nValue = 16]
        C1g --> R0g
        C2g --> R0g
        C3g --> R0g
    end

    subgraph ALLTOALL ["🔄 All-to-All — Everyone Exchanges"]
        direction TB
        A0[Process 0\nSend array] --> R1[Process 1\nRecv array]
        A1[Process 1\nSend array] --> R0[Process 0\nRecv array]
        A2[Process 2\nSend array] --> R3[Process 3\nRecv array]
        A3[Process 3\nSend array] --> R2[Process 2\nRecv array]
    end

    style BROADCAST fill:#1e3a5f,stroke:#2563eb,color:#93c5fd
    style SCATTER fill:#064e3b,stroke:#10b981,color:#6ee7b7
    style GATHER fill:#78350f,stroke:#f59e0b,color:#fcd34d
    style ALLTOALL fill:#2d1b69,stroke:#7c3aed,color:#c4b5fd
    style R0b fill:#1e40af,color:#bfdbfe,stroke:#3b82f6
    style R0s fill:#14532d,color:#86efac,stroke:#22c55e
    style R0g fill:#9a3412,color:#fdba74,stroke:#f97316
    style A0 fill:#4c1d95,color:#c4b5fd,stroke:#8b5cf6
```

---

## 💀 Deadlock Problem — Kya hota hai?

```mermaid
sequenceDiagram
    participant P1 as Process 1
    participant P5 as Process 5

    Note over P1: rank = 1
    Note over P5: rank = 5

    P1->>P1: data_send = "a"
    P5->>P5: data_send = "b"

    rect rgb(255, 200, 200)
        Note over P1,P5: 🔴 DEADLOCK ZONE
        P1-->>P5: ❌ recv(from P5) — BLOCKS
        P5-->>P5: send("b", to P1) in queue
    end

    Note over P1,P5: ❌ Both waiting forever\nP1 waits for recv → P5 waits for send completion
```

| Problem | Cause | Fix |
|---------|-------|-----|
| **Deadlock** | Both processes `recv()` before `send()` | Swap order: `send()` first, then `recv()` |
| **Blocking** | `send()`/`recv()` block until complete | Use `Isend()`/`Irecv()` non-blocking variants |
| **Order Mismatch** | Send/recv calls in wrong sequence | Match send/recv pairs correctly |

```mermaid
flowchart LR
    subgraph WRONG ["❌ Deadlock — Wrong Order"]
        direction TB
        P1W[Process 1\nrecv(from 5) 🔒\nwaiting forever...]
        P5W[Process 5\nsend(to 1) ⏳\nqueued, no receiver yet\nrecv(from 1) 🔒\nwaiting forever...]
        P1W -.->|blocked| P5W
        P5W -.->|blocked| P1W
    end

    subgraph RIGHT ["✅ Correct Order — No Deadlock"]
        direction TB
        P1R[Process 1\nsend(to 5) ✅\nrecv(from 5) ✅]
        P5R[Process 5\nrecv(from 1) ✅\nsend(to 1) ✅]
        P1R -->|data flows| P5R
        P5R -->|data flows| P1R
    end

    style WRONG fill:#1a0a0a,stroke:#ef4444,color:#fca5a5
    style RIGHT fill:#022c1a,stroke:#10b981,color:#6ee7b7
    style P1W fill:#7f1d1d,color:#fca5a5,stroke:#ef4444
    style P5W fill:#7f1d1d,color:#fca5a5,stroke:#ef4444
    style P1R fill:#14532d,color:#86efac,stroke:#22c55e
    style P5R fill:#14532d,color:#86efac,stroke:#22c55e
```

---

## 📊 MPI Collective Operations Summary

```mermaid
xychart-beta horizontal
    title "MPI Operations — Data Distribution"
    x-axis ["Broadcast", "Scatter", "Gather", "Alltoall", "Reduce"]
    y-axis "Processes Involved" 1 --> 10
    bar [10, 10, 10, 10, 10]
```

| Operation | Direction | Data Flow | Root? | Use Case |
|-----------|-----------|-----------|:-----:|----------|
| `bcast` | 1 → N | Same data to all | ✅ Yes | Sharing config, model params |
| `scatter` | 1 → N | Different chunks to each | ✅ Yes | Distributing work items |
| `gather` | N → 1 | Collect all to root | ✅ Yes | Assembling results |
| `alltoall` | N ↔ N | Everyone exchanges with all | ❌ No | Matrix transpose, FFT |
| `reduce` | N → 1 | Aggregate with operation | ✅ Yes | Sum, max, min, avg |
| `allreduce` | N ↔ N | Reduce + broadcast result | ❌ No | Global sum for all |

---

## 🧠 MPI Communication Modes

```mermaid
quadrantChart
    title MPI Communication — When to Use What?
    x-axis Small Data --> Large Data
    y-axis All Need Result? No --> All Need Result? Yes
    quadrant-1 AllReduce
    quadrant-2 Reduce + Bcast
    quadrant-3 Point-to-Point
    quadrant-4 Scatter + Gather
    "Point-to-Point": [0.15, 0.15]
    "Scatter + Gather": [0.75, 0.25]
    "AllReduce": [0.75, 0.75]
    "Reduce + Bcast": [0.25, 0.75]
```

| Mode | Data Size | All Need? | Complexity |
|------|-----------|-----------|:----------:|
| **Point-to-Point** | Any | No | Low |
| **Collective** | Any | Yes | Medium |
| **Non-blocking** | Large | Depends | High |
| **One-sided (RMA)** | Large | No | Very High |

---

## 📐 MPI Performance Metrics

```mermaid
flowchart TD
    A[MPI Program runs on\nN processes] --> B[Measure T_serial\nSingle process time]
    A --> C[Measure T_parallel\nN processes time]

    B --> D["⚡ Speedup\nS(N) = T_s / T_p"]
    C --> D

    D --> E["📊 Efficiency\nE = S(N) / N"]
    D --> F["📉 Communication Overhead\nT_comm = T_p - T_s/N"]
    D --> G["📈 Scalability\nWeak vs Strong"]

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
| `S = T_serial / T_parallel` | Speedup | Kitna fast hua multiple processes se? |
| `E = S / N` | Efficiency | Kitne efficiently processes use hue? |
| `T_comm = T_parallel - T_serial/N` | Communication Overhead | Message pass karne mein kitna time waste? |
| **Strong Scaling** | Fixed problem, more processes | Problem same, processes badhao |
| **Weak Scaling** | Fixed work per process | Processes badhao, problem bhi badhao |

---

## 🗺️ Virtual Topology — 2D Cartesian Grid

```mermaid
graph TB
    subgraph Grid ["🧩 3×3 Cartesian Grid (Periodic Boundaries)"]
        direction TB
        subgraph Row0 ["Row 0"]
            P0["P0\n(0,0)\n▲P6 ▼P3 ◄P2 ►P1"]
            P1["P1\n(0,1)\n▲P7 ▼P4 ◄P0 ►P2"]
            P2["P2\n(0,2)\n▲P8 ▼P5 ◄P1 ►P0"]
        end
        subgraph Row1 ["Row 1"]
            P3["P3\n(1,0)\n▲P0 ▼P6 ◄P5 ►P4"]
            P4["P4\n(1,1)\n▲P1 ▼P7 ◄P3 ►P5"]
            P5["P5\n(1,2)\n▲P2 ▼P8 ◄P4 ►P3"]
        end
        subgraph Row2 ["Row 2"]
            P6["P6\n(2,0)\n▲P3 ▼P0 ◄P8 ►P7"]
            P7["P7\n(2,1)\n▲P4 ▼P1 ◄P6 ►P8"]
            P8["P8\n(2,2)\n▲P5 ▼P2 ◄P7 ►P6"]
        end
    end

    style Grid fill:#1e1b4b,stroke:#6366f1,color:#c7d2fe
    style Row0 fill:#1e3a5f,stroke:#2563eb,color:#93c5fd
    style Row1 fill:#1e3a5f,stroke:#2563eb,color:#93c5fd
    style Row2 fill:#1e3a5f,stroke:#2563eb,color:#93c5fd
    style P0 fill:#4c1d95,color:#c4b5fd,stroke:#8b5cf6
    style P1 fill:#4c1d95,color:#c4b5fd,stroke:#8b5cf6
    style P2 fill:#4c1d95,color:#c4b5fd,stroke:#8b5cf6
    style P3 fill:#4c1d95,color:#c4b5fd,stroke:#8b5cf6
    style P4 fill:#5b21b6,color:#ddd6fe,stroke:#7c3aed
    style P5 fill:#4c1d95,color:#c4b5fd,stroke:#8b5cf6
    style P6 fill:#4c1d95,color:#c4b5fd,stroke:#8b5cf6
    style P7 fill:#4c1d95,color:#c4b5fd,stroke:#8b5cf6
    style P8 fill:#4c1d95,color:#c4b5fd,stroke:#8b5cf6
```

> 🔗 **Periodic boundaries** — top wraps to bottom, left wraps to right  
> 🧭 **Neighbors:** UP, DOWN, LEFT, RIGHT accessed via `cartesian_communicator.Shift()`

---

## ▶️ How to Run

```bash
# Prerequisite: mpi4py install karo
pip install mpi4py

# MPICH ya OpenMPI install hona zaroori hai (system-level)

# Hello World — 4 processes
mpiexec -n 4 python helloworld_MPI.py

# Point-to-Point — 9 processes (ranks 0,1,4,8 used)
mpiexec -n 9 python pointToPointCommunication.py

# Broadcast — 4 processes
mpiexec -n 4 python broadcast.py

# Scatter — 10 processes (10 elements array)
mpiexec -n 10 python scatter.py

# Gather — 4 processes
mpiexec -n 4 python gather.py

# All-to-All — 4 processes
mpiexec -n 4 python alltoall.py

# Reduce (SUM) — 3 processes
mpiexec -n 3 python reduction.py

# Deadlock Demo — 6+ processes (ranks 1 & 5 used)
mpiexec -n 6 python deadLockProblems.py

# Virtual Topology — 9 processes (3×3 grid)
mpiexec -n 9 python virtualTopology.py
```

> ⚠️ **Important Notes:**
> - MPI programs **cannot** run with plain `python` — always use `mpiexec` / `mpirun`
> - Process count (`-n`) must be ≥ highest rank used in script
> - `deadLockProblems.py` **will hang forever** (runs `Ctrl+C` se stop karo) — yeh intentional hai!

---

## 🔒 Shared Memory vs Distributed Memory

```mermaid
flowchart LR
    subgraph SHARED ["🟢 Shared Memory (Threading)"]
        direction TB
        MEM1[💾 Single Memory Space]
        T1[Thread 1] --> MEM1
        T2[Thread 2] --> MEM1
        T3[Thread 3] --> MEM1
        note1[⚠️ GIL in Python\nSynchronization needed]
    end

    subgraph DISTRIBUTED ["🔵 Distributed Memory (MPI)"]
        direction TB
        P1[Process 1\n💾 Own Memory] <-->|📨 Messages| P2[Process 2\n💾 Own Memory]
        P2 <-->|📨 Messages| P3[Process 3\n💾 Own Memory]
        P1 <-->|📨 Messages| P3
        note2[✅ No GIL\nExplicit communication]
    end

    style SHARED fill:#022c1a,stroke:#10b981,color:#6ee7b7
    style DISTRIBUTED fill:#1e3a5f,stroke:#2563eb,color:#93c5fd
    style MEM1 fill:#14532d,color:#86efac,stroke:#22c55e
    style T1 fill:#166534,color:#86efac,stroke:#22c55e
    style T2 fill:#166534,color:#86efac,stroke:#22c55e
    style T3 fill:#166534,color:#86efac,stroke:#22c55e
    style P1 fill:#1e40af,color:#bfdbfe,stroke:#3b82f6
    style P2 fill:#1e40af,color:#bfdbfe,stroke:#3b82f6
    style P3 fill:#1e40af,color:#bfdbfe,stroke:#3b82f6
```

| Feature | Threading (Shared) | MPI (Distributed) |
|---------|-------------------|-------------------|
| **Memory** | Shared, single space | Separate per process |
| **GIL** | ❌ Affected (Python) | ✅ No GIL |
| **Communication** | Via shared variables | Explicit messages |
| **Synchronization** | Locks, semaphores | Send/Recv, Barriers |
| **Scaling** | Single machine | Multi-node clusters |
| **Overhead** | Low (thread create) | Higher (message passing) |

---

## 📋 MPI Patterns Summary

| Pattern | Communication | When to Use | Example File |
|---------|:---:|-------------|--------------|
| **Hello World** | None | Verify MPI setup | `helloworld_MPI.py` |
| **Point-to-Point** | 1 ↔ 1 | Specific process communication | `pointToPointCommunication.py` |
| **Broadcast** | 1 → All | Share config, model, constants | `broadcast.py` |
| **Scatter** | 1 → All (chunks) | Distribute work items | `scatter.py` |
| **Gather** | All → 1 | Collect results at master | `gather.py` |
| **All-to-All** | All ↔ All | Matrix transpose, data shuffle | `alltoall.py` |
| **Reduce** | All → 1 (aggregate) | Global sum, max, min | `reduction.py` |
| **Deadlock** | ❌ Wrong order | **Avoid!** — learn correct pattern | `deadLockProblems.py` |
| **Virtual Topology** | Grid neighbors | Stencil computation, PDE solvers | `virtualTopology.py` |

> **Key Insight:** MPI Python ke GIL ko **bypass** karta hai alag processes use karke — har process ka apna Python interpreter hota hai. CPU-bound scientific computing ke liye MPI best choice hai, especially multi-node clusters ke liye jahan shared memory possible nahi.