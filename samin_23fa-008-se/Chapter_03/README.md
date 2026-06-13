# Chapter 03 — Process Based Parallelism in Python

> Multiprocessing with Python's `multiprocessing` module — spawning, managing, communicating, and synchronizing OS-level processes for true parallel execution.

---

## 📁 Files Overview

```mermaid
flowchart LR
    subgraph SPAWN["🚀 Spawning Processes"]
        A[spawning_processes.py\nBasic process spawn]
        B[spawning_processes_namespace.py\nImport from external file]
        C[myFunc.py\nShared helper function]
        B --> C
    end
    subgraph MANAGE["⚙️ Managing Processes"]
        D[naming_processes.py\nNamed vs default process]
        E[process_in_subclass.py\nProcess subclassing]
        F[killing_processes.py\nTerminate a process]
        G[run_background_processes.py\nDaemon vs non-daemon]
        H[run_background_processes_no_daemons.py\nBoth non-daemon]
    end
    subgraph COMM["📡 Communication"]
        I[communicating_with_pipe.py\nPipe — two processes]
        J[communicating_with_queue.py\nQueue — producer consumer]
    end
    subgraph SYNC["🔒 Sync & Pool"]
        K[processes_barrier.py\nBarrier + Lock]
        L[process_pool.py\nPool.map — 4 workers]
    end
    SPAWN --> MANAGE --> COMM --> SYNC
```

| File | Concept | Description |
|------|---------|-------------|
| `spawning_processes.py` | Basic Spawning | Spawns 6 processes calling `myFunc` with index |
| `spawning_processes_namespace.py` | Namespace Import | Same as above but imports `myFunc` from external module |
| `myFunc.py` | Helper Function | Prints loop output — shared across spawn examples |
| `naming_processes.py` | Process Naming | Named vs auto-named process using `current_process().name` |
| `process_in_subclass.py` | Process Subclass | Defines `MyProcess` by subclassing `multiprocessing.Process` |
| `killing_processes.py` | Terminate Process | Shows full process lifecycle — start, terminate, join |
| `run_background_processes.py` | Daemon Process | One daemon + one non-daemon — daemon dies with parent |
| `run_background_processes_no_daemons.py` | No Daemon | Both processes non-daemon — both run to completion |
| `communicating_with_pipe.py` | Pipe | Two processes communicate via `multiprocessing.Pipe` |
| `communicating_with_queue.py` | Queue | Producer/Consumer using `multiprocessing.Queue` |
| `processes_barrier.py` | Barrier + Lock | 2 processes sync at barrier; 2 run freely |
| `process_pool.py` | Process Pool | `Pool.map()` squares 0–99 using 4 worker processes |

---

##  Why Multiprocessing?


```mermaid
flowchart TD
    GIL["Python GIL\nGlobal Interpreter Lock"] -->|blocks| TH["Threads\nOnly 1 runs at a time\nfor CPU-bound work"]
    GIL -->|bypassed by| MP["multiprocessing.Process\nSeparate OS process\nSeparate memory\nSeparate GIL"]
    MP --> CORES["All CPU Cores\nUtilized in parallel"]
    CORES --> FAST["True Parallelism\nfor CPU-bound tasks"]
```

---

## 1. `spawning_processes.py` — Basic Process Spawn

Spawns 6 processes, each calling `myFunc(i)`. Each process prints its own loop output.

```mermaid
flowchart TD
    START([Main Process]) --> LOOP[for i in range 6]
    LOOP --> CREATE["Process(target=myFunc, args=(i,))"]
    CREATE --> S[process.start]
    S --> J[process.join]
    J --> LOOP
    LOOP -->|i = 6| END([All done])
    subgraph CHILD["Each Child Process"]
        CF["myFunc(i)\nprint calling from process i\nfor j in range i\nprint output j"]
    end
    CREATE -.spawns.-> CHILD
```

**Sample Output:**
```
calling myFunc from process n°: 0
calling myFunc from process n°: 1
output from myFunc is: 0
calling myFunc from process n°: 2
output from myFunc is: 0
output from myFunc is: 1
...
```

---

## 2. `spawning_processes_namespace.py` + `myFunc.py` — External Module

Same spawn logic but `myFunc` is imported from a separate file — demonstrates clean namespace separation.

```mermaid
flowchart LR
    MAIN["spawning_processes_namespace.py\nfrom myFunc import myFunc"] -->|imports| MF["myFunc.py\ndef myFunc(i):\n  print loop output"]
    MAIN --> P1["Process 0"]
    MAIN --> P2["Process 1"]
    MAIN --> P3["Process 2 ... 5"]
    P1 & P2 & P3 -->|calls| MF
```

> **Key Point:** Importing from a separate module keeps code reusable across multiple scripts without copy-pasting logic.

---

## 3. `naming_processes.py` — Named vs Default Process

```mermaid
flowchart TD
    MAIN([Main]) --> PN["Process(name='myFunc process'\ntarget=myFunc)"]
    MAIN --> PD["Process(target=myFunc)\nauto-named: Process-1"]
    PN --> START1[process_with_name.start]
    PD --> START2[process_with_default_name.start]
    START1 --> NAME1["current_process().name\n→ 'myFunc process'"]
    START2 --> NAME2["current_process().name\n→ 'Process-1'"]
    NAME1 & NAME2 --> SLEEP[sleep 3s]
    SLEEP --> EXIT[Exiting process name = ...]
```

**Sample Output:**
```
Starting process name = myFunc process
Starting process name = Process-1
Exiting process name = myFunc process
Exiting process name = Process-1
```

---

## 4. `process_in_subclass.py` — Subclassing Process

Defines a custom `MyProcess` class by subclassing `multiprocessing.Process` and overriding `run()`.

```mermaid
classDiagram
    class Process {
        +start()
        +join()
        +run()
        +name
        +pid
    }
    class MyProcess {
        +run()
    }
    Process <|-- MyProcess : subclass
    note for MyProcess "run() overridden:\nprints self.name\nthen returns"
```

**Sample Output:**
```
called run method in MyProcess-1
called run method in MyProcess-2
...
called run method in MyProcess-10
```

---

## 5. `killing_processes.py` — Process Lifecycle + Terminate

![Process Lifecycle](images/03_process_lifecycle.svg)

```mermaid
stateDiagram-v2
    [*] --> Created : Process(target=foo)
    Created --> Running : p.start()
    Running --> Terminated : p.terminate()
    Terminated --> Joined : p.join()
    Joined --> [*]

    note right of Created : is_alive() = False
    note right of Running : is_alive() = True
    note right of Terminated : is_alive() = False\nexitcode = -15
    note right of Joined : exitcode confirmed
```

**Sample Output:**
```
Process before execution: <Process ...> False
Process running:          <Process ...> True
Process terminated:       <Process ...> False
Process joined:           <Process ...> False
Process exit code: -15
```

> **Exit code `-15`** means the process was killed by `SIGTERM` signal via `p.terminate()`.

---

## 6. `run_background_processes.py` — Daemon vs Non-Daemon

![Daemon vs Non-Daemon](images/05_daemon_vs_nodaemon.svg)

```mermaid
flowchart TD
    MAIN([Main Process starts]) --> BP["background_process\ndaemon = True"]
    MAIN --> NBP["NO_background_process\ndaemon = False"]
    BP --> BP_RUN["prints 0 to 4\nsleep 1s"]
    NBP --> NBP_RUN["prints 5 to 9\nsleep 1s"]
    MAIN --> EXIT_MAIN([Main exits])
    EXIT_MAIN -->|kills daemon| BP_DEAD["background_process\nKILLED — may not finish"]
    NBP_RUN --> NBP_DONE["NO_background_process\nRuns to completion"]
```

| | `daemon=True` | `daemon=False` |
|---|---|---|
| Killed when parent exits? | Yes | No |
| Can spawn child processes? | No | Yes |
| Use case | Background helper tasks | Independent worker processes |

---

## 7. `run_background_processes_no_daemons.py` — Both Non-Daemon

Identical to above but **both** processes have `daemon=False` — both run to full completion regardless of parent.

```mermaid
flowchart LR
    MAIN([Main]) --> BP["background_process\ndaemon = False\nprints 0 to 4"]
    MAIN --> NBP["NO_background_process\ndaemon = False\nprints 5 to 9"]
    BP --> DONE1[Exits normally]
    NBP --> DONE2[Exits normally]
    DONE1 & DONE2 --> END([Both complete])
```

---

## 8. `communicating_with_pipe.py` — Pipe Communication

```mermaid
flowchart LR
    subgraph P1["Process 1: create_items"]
        C1["sends 0 to 9\ninto pipe_1"]
    end
    subgraph PIPE1["pipe_1"]
        direction TB
        OUT1["output end"] --> IN1["input end"]
    end
    subgraph P2["Process 2: multiply_items"]
        C2["reads from pipe_1\nsends item x item\ninto pipe_2"]
    end
    subgraph PIPE2["pipe_2"]
        direction TB
        OUT2["output end"] --> IN2["input end"]
    end
    subgraph MAIN["Main Process"]
        C3["reads from pipe_2\nprints squared values"]
    end
    C1 --> OUT1
    IN1 --> C2
    C2 --> OUT2
    IN2 --> C3
```

**Sample Output:**
```
0  1  4  9  16  25  36  49  64  81  End
```

> `EOFError` is caught to detect when the pipe is closed — clean way to signal end of stream.

---

## 9. `communicating_with_queue.py` — Queue (Producer/Consumer)

```mermaid
sequenceDiagram
    participant Producer
    participant Queue
    participant Consumer

    loop 10 times
        Producer->>Producer: random item = randint(0,256)
        Producer->>Queue: queue.put(item)
        Producer->>Producer: sleep(1s)
        Producer->>Producer: print queue size
    end

    loop until queue empty
        Consumer->>Queue: queue.empty()?
        alt queue has items
            Consumer->>Consumer: sleep(2s)
            Consumer->>Queue: queue.get()
            Consumer->>Consumer: print item popped
        else queue empty
            Consumer->>Consumer: print empty, break
        end
    end
```

**Sample Output:**
```
Process Producer : item 173 appended to queue producer-1
The size of queue is 1
Process Consumer : item 173 popped from by consumer-1
...
the queue is empty
```

---

## 10. `processes_barrier.py` — Barrier + Lock

![Barrier Synchronization](images/06_barrier_lock.svg)

```mermaid
flowchart TD
    subgraph WITH["With Barrier — p1, p2"]
        W1["p1: test_with_barrier"] --> B["synchronizer.wait()\nBarrier n=2"]
        W2["p2: test_with_barrier"] --> B
        B -->|both arrived| LOCK["with serializer Lock\nprint timestamp"]
    end
    subgraph WITHOUT["Without Barrier — p3, p4"]
        W3["p3: test_without_barrier"] --> PRINT3["print timestamp immediately"]
        W4["p4: test_without_barrier"] --> PRINT4["print timestamp immediately"]
    end
```

**Sample Output:**
```
process p3 - test_without_barrier ----> 2024-04-02 12:00:00.123
process p4 - test_without_barrier ----> 2024-04-02 12:00:00.124
process p1 - test_with_barrier    ----> 2024-04-02 12:00:00.201
process p2 - test_with_barrier    ----> 2024-04-02 12:00:00.201
```

> p1 and p2 print **identical timestamps** — held at barrier until both arrived, then released together.

---

## 11. `process_pool.py` — Process Pool

![Process Pool](images/07_process_pool.svgg)

```mermaid
flowchart TD
    MAIN([Main]) --> INPUT["inputs = list 0 to 99\n100 numbers"]
    INPUT --> POOL["Pool(processes=4)\n4 worker processes"]
    POOL --> W1["Worker 1\nfunction_square 0,4,8..."]
    POOL --> W2["Worker 2\nfunction_square 1,5,9..."]
    POOL --> W3["Worker 3\nfunction_square 2,6,10..."]
    POOL --> W4["Worker 4\nfunction_square 3,7,11..."]
    W1 & W2 & W3 & W4 --> COLLECT["pool_outputs\ncollected results in order"]
    COLLECT --> CLOSE["pool.close()\npool.join()"]
    CLOSE --> PRINT["print pool_outputs\n[0,1,4,9,16,...,9801]"]
```

**Sample Output:**
```
Pool: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, ..., 9801]
```

---

## 📡 Communication Methods — Pipe vs Queue

![Pipe vs Queue](images/04_pipe_vs_queue.svg)

| | `Pipe` | `Queue` |
|---|---|---|
| Processes supported | 2 only | Many |
| Thread-safe? | No (by default) | Yes |
| Speed | Faster | Slightly slower |
| Use case | Simple pipeline | Multi-producer/consumer |

---

## 🔄 Process Lifecycle — Full Picture

![Process Lifecycle Full](images/03_process_lifecycle.svg)

```mermaid
stateDiagram-v2
    [*] --> Created : Process()
    Created --> Ready : process.start()
    Ready --> Running : OS scheduler
    Running --> Waiting : I/O or sleep
    Waiting --> Ready : I/O done
    Running --> Terminated : completes or p.terminate()
    Terminated --> Joined : p.join()
    Joined --> [*]

    note right of Running : is_alive() = True
    note right of Terminated : exitcode set\n0 = normal\n-15 = SIGTERM
```

---

## 📋 Quick Reference — Which Tool to Use?

```mermaid
flowchart TD
    Q([What do you need?]) --> Q1{Goal}
    Q1 -->|Run a function\nin a new process| SP["multiprocessing.Process\ntarget=func, args=(...)"]
    Q1 -->|Reuse process logic\nacross scripts| NS["Import from myFunc.py\nspawning_processes_namespace.py"]
    Q1 -->|Custom process\nbehavior| SC["Subclass Process\noverride run()"]
    Q1 -->|Kill a running\nprocess| KP["p.terminate()\np.join()"]
    Q1 -->|Background helper\ntask| DP["daemon=True\nprocess dies with parent"]
    Q1 -->|Send data between\n2 processes| PP["multiprocessing.Pipe\nfast, point-to-point"]
    Q1 -->|Multiple producers\nor consumers| QQ["multiprocessing.Queue\nthread + process safe"]
    Q1 -->|Distribute work\nacross N workers| PL["multiprocessing.Pool\npool.map()"]
    Q1 -->|Wait for all processes\nto reach a point| BR["multiprocessing.Barrier\nsynchronizer.wait()"]
```

---

## ▶ How to Run

```bash
# Spawning
python spawning_processes.py
python spawning_processes_namespace.py   # requires myFunc.py in same folder

# Managing
python naming_processes.py
python process_in_subclass.py
python killing_processes.py
python run_background_processes.py
python run_background_processes_no_daemons.py

# Communication
python communicating_with_pipe.py
python communicating_with_queue.py

# Sync & Pool
python processes_barrier.py
python process_pool.py
```

> ⚠️ `spawning_processes_namespace.py` requires `myFunc.py` to be in the **same folder**.
>
> 💡 **Tip:** Run `run_background_processes.py` and `run_background_processes_no_daemons.py` back to back to clearly see the daemon difference.