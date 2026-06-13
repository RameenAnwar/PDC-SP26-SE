# Chapter 05 — Asynchronous Programming with Python

> `async`/`await`, Futures, Tasks &amp; Concurrency Patterns — mastering non-blocking I/O and cooperative multitasking in Python.

---

## 📁 Files Overview

| File | Concept | Description |
|------|---------|-------------|
| `asyncio_and_futures.py` | Futures &amp; Callbacks | Creates `Future` objects; resolves sum/factorial via coroutines with `done_callback` |
| `asyncio_coroutine.py` | Coroutine State Machine | Nested `await` calls forming a probabilistic finite state machine |
| `asyncio_event_loop.py` | Manual Event Loop | Demonstrates `call_soon`, `call_later`, and manual loop lifecycle |
| `asyncio_task_manipulation.py` | Parallel Task Execution | Runs factorial, Fibonacci, and binomial coefficient concurrently via `asyncio.Task` |
| `concurrent_futures_pooling.py` | Thread &amp; Process Pools | Compares sequential vs `ThreadPoolExecutor` vs `ProcessPoolExecutor` performance |

---

## 🗂️ File Dependency Map

```mermaid
graph TD
    subgraph Async_Core ["🔵 asyncio Core — Cooperative Multitasking"]
        AF[asyncio_and_futures.py\nFutures & Callbacks]
        AC[asyncio_coroutine.py\nCoroutine State Machine]
        EL[asyncio_event_loop.py\nManual Event Loop]
        AT[asyncio_task_manipulation.py\nParallel Task Execution]
    end

    subgraph Pooling ["🟢 concurrent.futures — True Parallel"]
        CP[concurrent_futures_pooling.py\nThread vs Process Pool]
    end

    AF --> AT
    AT --> CP
    AC --> AF
    EL --> AF

    style Async_Core fill:#1e3a5f,color:#93c5fd,stroke:#2563eb
    style Pooling fill:#064e3b,color:#6ee7b7,stroke:#10b981
    style AF fill:#2d1b69,color:#c4b5fd,stroke:#7c3aed
    style AC fill:#78350f,color:#fcd34d,stroke:#f59e0b
    style EL fill:#1c1917,color:#d6d3d1,stroke:#57534e
    style AT fill:#2d1b69,color:#c4b5fd,stroke:#7c3aed
    style CP fill:#064e3b,color:#6ee7b7,stroke:#10b981
```

---

## ⏱️ Execution Flow Comparison

```mermaid
gantt
    title Execution Timeline — 3 Tasks (I/O-bound)
    dateFormat  X
    axisFormat  — t=%ss

    section 🔵 Serial (Blocking)
    Task A (factorial)      :s1, 0, 10
    Task B (fibonacci)      :s2, 10, 20
    Task C (binomial)       :s3, 20, 30

    section 🟣 asyncio (Cooperative)
    Task A (await sleep)    :a1, 0, 1
    Task B (await sleep)    :a2, 1, 2
    Task C (await sleep)    :a3, 2, 3
    Task A (resume)         :a4, 3, 4
    Task B (resume)         :a5, 4, 5
    Task C (resume)         :a6, 5, 6

    section 🟢 Multiprocessing
    Process 1 (Task A)      :p1, 0, 10
    Process 2 (Task B)      :p2, 0, 10
    Process 3 (Task C)      :p3, 0, 10
```

> 🔵 **Serial** — each task waits for previous to complete. Total ~30s  
> 🟣 **asyncio** — tasks yield at `await`, letting others run. Total ~6s  
> 🟢 **Multiprocessing** — tasks truly run in parallel. Total ~10s

---

## 🔒 GIL vs asyncio — Kya farak hai?

```mermaid
flowchart LR
    subgraph THREADING ["🔴 Threading — GIL Bottleneck"]
        direction TB
        G[🔒 GIL\nSirf 1 thread\nek waqt]
        T1[Thread 1\n✅ Running]
        T2[Thread 2\n⏸ Waiting]
        T3[Thread 3\n⏸ Waiting]
        G --> T1
        G -.->|blocked| T2
        G -.->|blocked| T3
        note1[CPU-bound tasks\nNo speedup]
    end

    subgraph ASYNCIO ["🔵 asyncio — Cooperative"]
        direction TB
        EL[🔄 Event Loop\nSingle-threaded]
        C1[Coroutine 1\n✅ Running]
        C2[Coroutine 2\n⏳ await sleep]
        C3[Coroutine 3\n⏳ await sleep]
        EL --> C1
        C1 -.->|yields| C2
        C2 -.->|yields| C3
        note2[I/O-bound tasks\nNon-blocking]
    end

    subgraph MULTIPROC ["🟢 Multiprocessing — True Parallel"]
        direction TB
        C0[Core 0\n✅ Process 1]
        C1[Core 1\n✅ Process 2]
        C2[Core 2\n✅ Process 3]
        note3[CPU-bound tasks\nGIL bypassed]
    end

    style THREADING fill:#1a0a0a,stroke:#ef4444,color:#fca5a5
    style ASYNCIO fill:#1e3a5f,stroke:#2563eb,color:#93c5fd
    style MULTIPROC fill:#022c1a,stroke:#10b981,color:#6ee7b7
    style G fill:#7f1d1d,color:#fca5a5,stroke:#ef4444
    style T1 fill:#14532d,color:#86efac,stroke:#22c55e
    style T2 fill:#1c1917,color:#78716c,stroke:#57534e
    style T3 fill:#1c1917,color:#78716c,stroke:#57534e
    style EL fill:#1e40af,color:#bfdbfe,stroke:#3b82f6
    style C1 fill:#14532d,color:#86efac,stroke:#22c55e
    style C2 fill:#422006,color:#fde68a,stroke:#f59e0b
    style C3 fill:#422006,color:#fde68a,stroke:#f59e0b
    style C0 fill:#14532d,color:#86efac,stroke:#22c55e
    style C1 fill:#14532d,color:#86efac,stroke:#22c55e
    style C2 fill:#14532d,color:#86efac,stroke:#22c55e
```

| | Threading | asyncio | Multiprocessing |
|---|---|---|---|
| GIL | ❌ Affected | ✅ Single-thread (not needed) | ✅ Bypassed |
| True Parallelism | ❌ No | ❌ No (concurrent) | ✅ Yes |
| Memory | Shared | Shared | Separate per process |
| Best For | I/O-bound (thread-safe libs) | I/O-bound (async libs) | CPU-bound tasks |
| Overhead | Medium (context switch) | Low (cooperative yield) | High (process spawn) |

---

## 📊 Performance Benchmark

```mermaid
xychart-beta horizontal
    title "Execution Time — 3 async tasks vs pools (seconds)"
    x-axis ["Serial", "asyncio (I/O)", "ThreadPool", "ProcessPool"]
    y-axis "Time (seconds)" 0 --> 35
    bar [30, 6, 8, 12]
```

> ✅ **asyncio is ~5× faster** than serial for I/O-bound async tasks.  
> ✅ **ProcessPool is ~2.5× faster** than serial for CPU-bound counting.

---

## 🧠 Async Programming Models

```mermaid
quadrantChart
    title Concurrency Models — When to Use What?
    x-axis Low I/O --> High I/O
    y-axis Low CPU --> High CPU
    quadrant-1 asyncio
    quadrant-2 Multiprocessing
    quadrant-3 Simple Scripts
    quadrant-4 Threading / asyncio
    "asyncio (async/await)": [0.75, 0.25]
    "Multiprocessing (CPU)": [0.75, 0.75]
    "Simple Serial Scripts": [0.25, 0.25]
    "Threading (I/O-bound)": [0.25, 0.75]
```

| Model | Best For | Example |
|-------|----------|---------|
| **Serial** | Simple, quick scripts | File reader, CLI tools |
| **Threading** | I/O-bound with blocking libs | `requests`, file I/O (older APIs) |
| **asyncio** | High-concurrency I/O | Web servers, APIs, scraping |
| **Multiprocessing** | CPU-bound computation | Data processing, ML, encryption |

---

## 📐 Async Performance Metrics

```mermaid
flowchart TD
    A[Coroutine launched\non Event Loop] --> B[Measure T_serial\nBlocking time]
    A --> C[Measure T_async\nNon-blocking time]

    B --> D["⚡ Concurrency Gain\nC = T_serial / T_async"]
    C --> D

    D --> E["📊 Throughput\nRequests per second"]
    D --> F["📉 Latency\nTime to first response"]
    D --> G["📈 Scalability\nHandled under load"]

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
| `C = T(serial) / T(async)` | Concurrency Gain | Kitna fast hua async se? |
| `Throughput = N / T` | Throughput | Kitne tasks per second? |
| `Latency = T(resp)` | Latency | Pehla response kitni der mein? |
| Scalability | Load handling | Load badhne par performance? |

---

## 🔄 Coroutine State Machine Flow (`asyncio_coroutine.py`)

```mermaid
stateDiagram-v2
    [*] --> Start_State
    Start_State --> State1: rand=1
    Start_State --> State2: rand=0
    State1 --> State3: rand=0
    State1 --> State2: rand=1
    State2 --> State1: rand=0
    State2 --> State3: rand=1
    State3 --> State1: rand=0
    State3 --> End_State: rand=1
    End_State --> [*]

    note right of Start_State
        async def start_state()
        randint(0,1)
    end note

    note right of State1
        async def state1()
        await asyncio.sleep(1)
    end note
```

---

## 🗃️ Future & Task Lifecycle (`asyncio_and_futures.py`)

```mermaid
flowchart LR
    A[🟡 Future Created\nasyncio.Future] --> B[🔗 Callback Attached\nadd_done_callback]
    B --> C[🟢 Task Created\ncreate_task]
    C --> D[⏳ coroutine runs]
    D --> E[💤 await asyncio.sleep]
    E --> D
    D --> F[✅ future.set_result]
    F --> G[🔔 got_result called]
    G --> H[🖥️ print result]

    style A fill:#78350f,color:#fcd34d,stroke:#f59e0b
    style C fill:#1e3a5f,color:#93c5fd,stroke:#2563eb
    style F fill:#064e3b,color:#6ee7b7,stroke:#10b981
    style G fill:#2d1b69,color:#c4b5fd,stroke:#7c3aed
    style H fill:#1e3a5f,color:#93c5fd,stroke:#2563eb
```

---

## ▶️ How to Run

```bash
# 1. Futures & Callbacks — requires two numbers as args
python asyncio_and_futures.py 10 5

# 2. Coroutine State Machine — no args, random transitions
python asyncio_coroutine.py

# 3. Manual Event Loop control
python asyncio_event_loop.py

# 4. Parallel coroutine tasks — factorial, fibonacci, binomial
python asyncio_task_manipulation.py

# 5. ThreadPool vs ProcessPool benchmark
python concurrent_futures_pooling.py
```

> ⚠️ **Note:** `asyncio_event_loop.py` uses `time.sleep()` (blocking) instead of `await asyncio.sleep()` — this is intentional to demonstrate event loop timer control, but in real async code, **always** `await asyncio.sleep()`.

---

## 📋 Async Patterns Summary

| Pattern | Mechanism | Blocking? | Best For | Example File |
|---------|-----------|:---:|----------|--------------|
| **Serial** | One after another | ✅ Yes | Baseline | — |
| **Callback (Future)** | `future.add_done_callback()` | ❌ No | Legacy APIs | `asyncio_and_futures.py` |
| **Coroutine** | `async/await` | ❌ No | Modern async code | `asyncio_coroutine.py` |
| **Task** | `asyncio.create_task()` | ❌ No | Concurrent coroutines | `asyncio_task_manipulation.py` |
| **Event Loop** | `loop.call_soon/later` | ❌ No | Fine-grained control | `asyncio_event_loop.py` |
| **ThreadPool** | `ThreadPoolExecutor` | ⚠️ GIL | I/O-bound | `concurrent_futures_pooling.py` |
| **ProcessPool** | `ProcessPoolExecutor` | ❌ No | CPU-bound | `concurrent_futures_pooling.py` |

> **Key Insight:** I/O-bound tasks (network calls, file reads) ke liye `asyncio` best hai kyunki yeh single thread mein **cooperative multitasking** karta hai bina GIL overhead ke. CPU-bound tasks ke liye **multiprocessing** hi sahi choice hai. Threading sirf tab use karo jab async libraries available na ho.