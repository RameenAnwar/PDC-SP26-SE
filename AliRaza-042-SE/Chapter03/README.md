# Chapter 3: Process-Based Parallelism

> **Comprehensive Theory and Practical Implementation Guide**
> This chapter focuses on concurrency using multiple processes in Python, bypassing the Global Interpreter Lock (GIL) to achieve true parallelism for CPU-bound tasks.

---

## Table of Contents
1. [Understanding Python's multiprocessing module](#1-understanding-pythons-multiprocessing-module)
2. [Spawning a process](#2-spawning-a-process)
   - [2.1 Spawning Processes from a Separate Module](#21-spawning-processes-from-a-separate-module)
3. [Naming a process](#3-naming-a-process)
4. [Running processes in the background](#4-running-processes-in-the-background)
   - [4.1 Non-Daemon Background Processes](#41-non-daemon-background-processes)
5. [Killing a process](#5-killing-a-process)
6. [Defining processes in a subclass](#6-defining-processes-in-a-subclass)
7. [Using a queue to exchange data](#7-using-a-queue-to-exchange-data)
8. [Using pipes to exchange objects](#8-using-pipes-to-exchange-objects)
9. [Synchronizing processes](#9-synchronizing-processes)
10. [Using a process pool](#10-using-a-process-pool)

---

## 1. Understanding Python's multiprocessing module
The `multiprocessing` module allows the creation of isolated processes, each running its own Python interpreter. 
- **Bypassing the GIL:** Unlike the `threading` module, `multiprocessing` sidesteps the Global Interpreter Lock (GIL). This makes it perfectly suited for CPU-bound tasks.
- **Process Isolation:** Each process has its own memory space, which avoids data corruption by race conditions but requires specialized mechanisms like Pipes or Queues to communicate.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart TD
    %% Premium Process Isolation Visual
    classDef process fill:#e0f2fe,stroke:#0ea5e9,stroke-width:2px,color:#0369a1,font-weight:bold
    classDef memory fill:#fef3c7,stroke:#f59e0b,stroke-width:2px,color:#78350f,font-weight:bold

    subgraph SYSTEM ["🖥️ Operating System Process Space"]
        direction LR
        P1("🏭 Process 1")
        P2("🏭 Process 2")
        P3("🏭 Process N")
        
        M1[("💾 Private Memory Space 1")]
        M2[("💾 Private Memory Space 2")]
        M3[("💾 Private Memory Space N")]
        
        P1 <--> M1
        P2 <--> M2
        P3 <--> M3
    end

    class P1,P2,P3 process
    class M1,M2,M3 memory
```

## 2. Spawning a process
A process is created by instantiating the `multiprocessing.Process` object and passing a target function.
- `start()` initiates the process.
- `join()` blocks the main process until the spawned process has completed.

**Example Implementation:** See [spawning_processes.py](Codes/spawning_processes.py)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart LR
    %% Premium Process Spawning Model
    classDef tMain fill:#ffe4e6,stroke:#e11d48,stroke-width:2.5px,color:#4c0519,font-weight:bold
    classDef tChild fill:#e0f2fe,stroke:#0ea5e9,stroke-width:2px,color:#0369a1,font-weight:bold

    Main("💻 Main Process")
    Main == "process.start()" ==> P_Child("⚙️ Child Process")
    P_Child -. "Execution" .-> Task("myFunc Target")
    Task == "process.join()" ==> Main

    class Main tMain
    class P_Child,Task tChild
```

### 2.1 Spawning Processes from a Separate Module
Instead of declaring the worker function in the same module, we can define the function in an external module and import it.

**Worker Module:** See [myFunc.py](Codes/myFunc.py)

**Spawning Script:** See [spawning_processes_namespace.py](Codes/spawning_processes_namespace.py)

## 3. Naming a process
Naming processes helps in debugging and identifying which process is executing. Use the `name` parameter in `multiprocessing.Process` or `multiprocessing.current_process().name` to differentiate them.

**Example Implementation:** See [naming_processes.py](Codes/naming_processes.py)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart TD
    %% Premium Naming Visual
    classDef processT fill:#fef3c7,stroke:#f59e0b,stroke-width:2.5px,color:#78350f,font-weight:bold

    Parent("💻 Main Process")
    Parent ==> Named["⚙️ Process: 'myFunc process'"]
    Parent ==> Default["⚙️ Process: 'Process-2'"]

    class Named,Default processT
```

## 4. Running processes in the background
Processes can be set as `daemon=True` to run in the background. A background (daemon) process will be terminated abruptly when the main program exits, without completing its tasks or cleaning up resources.

**Example Implementation:** See [run_background_processes.py](Codes/run_background_processes.py)

```mermaid
sequenceDiagram
    autonumber
    actor M as Main Process
    actor D as Daemon Process
    actor N as Non-Daemon Process

    M->>D: start()
    M->>N: start()
    Note over N: Main process waits for<br/>non-daemon to finish
    N-->>M: complete
    Note over M,D: Main completes.<br/>Daemon forcefully killed.
```
### 4.1 Non-Daemon Background Processes
If a process is explicitly set to `daemon=False`, the main process will block and wait for it to exit, ensuring its tasks complete fully.

**Example Implementation:** See [run_background_processes_no_daemons.py](Codes/run_background_processes_no_daemons.py)

## 5. Killing a process
To explicitly terminate a process, call `process.terminate()`. This sends a SIGTERM signal (on Unix) or TerminateProcess (on Windows) to immediately stop it. The process `is_alive()` method helps check status.

**Example Implementation:** See [killing_processes.py](Codes/killing_processes.py)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart LR
    %% Premium Kill Process Flow
    classDef running fill:#dcfce7,stroke:#22c55e,stroke-width:2px,color:#15803d,font-weight:bold
    classDef dead fill:#ffe4e6,stroke:#e11d48,stroke-width:2px,color:#4c0519,font-weight:bold

    Start["⚙️ Process Init"] --> Run["🟢 Running: is_alive() = True"]
    Run == "terminate()" ==> Killed["🔴 Terminated: is_alive() = False"]
    Killed --> Join["🏁 Joined & Cleaned Up"]

    class Run running
    class Killed dead
```

## 6. Defining processes in a subclass
Like threads, you can inherit from `multiprocessing.Process` and override its `run()` method. This object-oriented approach is ideal when you need to maintain state inside the process.

**Example Implementation:** See [process_in_subclass.py](Codes/process_in_subclass.py)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
classDiagram
    %% Premium Class Diagram
    class Process {
        +start()
        +join()
        +run()
    }
    class MyProcess {
        +run()
    }
    Process <|-- MyProcess : Inherits
```

## 7. Using a queue to exchange data
Because memory is isolated, sharing data requires inter-process communication (IPC) tools. `multiprocessing.Queue` operates identically to `queue.Queue` but is built for process-safe communication via locking mechanisms.

**Example Implementation:** See [communicating_with_queue.py](Codes/communicating_with_queue.py)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart LR
    %% Premium IPC Queue Visual
    classDef queue fill:#dcfce7,stroke:#22c55e,stroke-width:2.5px,color:#15803d,font-weight:bold
    classDef prod fill:#e0f2fe,stroke:#0ea5e9,stroke-width:2px,color:#0369a1,font-weight:bold
    classDef cons fill:#ffe4e6,stroke:#e11d48,stroke-width:2px,color:#4c0519,font-weight:bold

    P("📤 Producer Process")
    Q[("🛡️ Multiprocessing Queue")]
    C("📥 Consumer Process")
    
    P == "put(item)" ==> Q
    Q == "get()" ==> C

    class Q queue
    class P prod
    class C cons
```

## 8. Using pipes to exchange objects
Pipes are preferred for high-speed, two-way communication between exactly two processes. `multiprocessing.Pipe()` returns a pair of connection objects representing the ends of a pipe.

**Example Implementation:** See [communicating_with_pipe.py](Codes/communicating_with_pipe.py)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart LR
    %% Premium Pipe Connection Visual
    classDef pipe fill:#f3e8ff,stroke:#7c3aed,stroke-width:2.5px,color:#2e1065,font-weight:bold
    classDef process fill:#e0f2fe,stroke:#0ea5e9,stroke-width:2px,color:#0369a1,font-weight:bold

    P1("⚙️ Process A")
    Pipe{{"🔌 Duplex Pipe Link"}}
    P2("⚙️ Process B")

    P1 <== "send() / recv()" ==> Pipe
    Pipe <== "send() / recv()" ==> P2

    class Pipe pipe
    class P1,P2 process
```

## 9. Synchronizing processes
Like threads, processes can use synchronization primitives such as Lock, Event, Condition, and Barrier from the `multiprocessing` module to avoid resource contention.

**Example Implementation:** See [processes_barrier.py](Codes/processes_barrier.py)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart TD
    %% Premium Sync Visual
    classDef sync fill:#fef3c7,stroke:#f59e0b,stroke-width:2.5px,color:#78350f,font-weight:bold
    classDef pActive fill:#dcfce7,stroke:#22c55e,stroke-width:2px,color:#15803d,font-weight:bold

    subgraph SYNC_BARRIER ["🚧 Barrier Rendezvous"]
        B{{"🛑 Barrier Capacity = 2"}}
    end

    P1("⚙️ Sync Process 1") == "Wait" ==> B
    P2("⚙️ Sync Process 2") == "Wait" ==> B
    
    B == "Release Together" ==> Critical[("⚡ Critical Section")]

    class B sync
    class P1,P2 pActive
```

## 10. Using a process pool
The `multiprocessing.Pool` class abstraction offers a convenient way to parallelize a function across multiple input values, distributing the input data across processes efficiently (data parallelism).
- `pool.map()` behaves like the built-in map, but chops tasks into chunks and farms them out to processes.

**Example Implementation:** See [process_pool.py](Codes/process_pool.py)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'lineColor': '#475569', 'primaryColor': '#f8fafc', 'primaryTextColor': '#0f172a', 'primaryBorderColor': '#cbd5e1' }}}%%
flowchart TD
    %% Premium Pool Visual
    classDef poolTask fill:#e0f2fe,stroke:#0ea5e9,stroke-width:2.5px,color:#0369a1,font-weight:bold
    classDef pNodes fill:#f3e8ff,stroke:#7c3aed,stroke-width:2px,color:#2e1065,font-weight:bold

    Data[("💾 Input Data: 0 to 99")]
    Pool{{"⚙️ Process Pool (4 Workers)"}}
    
    Data == "pool.map(func)" ==> Pool
    
    subgraph WORKERS ["Worker Nodes"]
        W1("Worker 1")
        W2("Worker 2")
        W3("Worker 3")
        W4("Worker 4")
    end
    
    Pool --> W1
    Pool --> W2
    Pool --> W3
    Pool --> W4
    
    W1 -. "Results" .-> Out[("📦 Output List")]
    W2 -. "Results" .-> Out
    W3 -. "Results" .-> Out
    W4 -. "Results" .-> Out

    class Pool poolTask
    class W1,W2,W3,W4 pNodes
```
