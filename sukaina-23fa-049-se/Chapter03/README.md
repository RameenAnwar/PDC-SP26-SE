# README – Chapter 03

# Python Parallel Programming Cookbook (Multiprocessing)

This chapter focuses on **Process-Based Parallelism using Python Multiprocessing**. Unlike threads, processes have separate memory spaces and can fully utilize multiple CPU cores for parallel execution.

---

## Chapter 03 


# spawning_processes.py

## Architecture

```mermaid
flowchart LR

Main --> Process1
Main --> Process2
Main --> Process3

Process1 --> End
Process2 --> End
Process3 --> End
```

## Overview

Demonstrates **basic process creation using multiprocessing.Process**.

## What I Learned

* Creating processes
* Starting and joining processes
* Difference between threads and processes

## What This Program Does

1. Creates multiple processes
2. Assigns work to each process
3. Executes independently
4. Waits for all processes to finish

## How to Execute

```bash
python spawning_processes.py
```

## Advantages

* True parallel execution
* Utilizes CPU cores

## Disadvantages

* Higher memory usage

## Use Cases

* Data processing
* Scientific computing

## Summary

Shows how to create and run multiple processes.

---

# spawning_processes_namespace.py

## Architecture

```mermaid
flowchart TD

MainProcess --> ImportFunction
ImportFunction --> Process1
ImportFunction --> Process2
ImportFunction --> Process3
```

## Overview

Demonstrates executing imported functions inside processes.

## What I Learned

* Namespace handling
* Modular multiprocessing

## What This Program Does

1. Imports a function from another file
2. Creates multiple processes
3. Executes imported function

## How to Execute

```bash
python spawning_processes_namespace.py
```

## Advantages

* Modular code
* Reusability

## Disadvantages

* Requires external modules

## Summary

Shows how multiprocessing works with imported functions.

---

# myFunc.py

## Architecture

```mermaid
flowchart TD

Input --> myFunc
myFunc --> Output
```

## Overview

Reusable function called by multiprocessing examples.

## What I Learned

* Function parameter passing
* Reusable modules

## Summary

Provides helper functions for process examples.

---

# naming_processes.py

## Architecture

```mermaid
graph TD

Main

Main --> Process_A
Main --> Process_B
Main --> Process_C
```

## Overview

Demonstrates custom process names.

## What I Learned

* Naming processes
* Process identification

## How to Execute

```bash
python naming_processes.py
```

## Summary

Shows how custom names improve debugging.

---

# process_in_subclass.py

## Architecture

```mermaid
classDiagram

Process <|-- MyProcess

class Process{
start()
run()
join()
}

class MyProcess{
custom run()
}
```

## Overview

Demonstrates subclassing Process.

## What I Learned

* OOP with multiprocessing
* Overriding run()

## How to Execute

```bash
python process_in_subclass.py
```

## Summary

Shows custom process implementation using inheritance.

---

# process_pool.py

## Architecture

```mermaid
flowchart TD

Tasks[100 Tasks]

Tasks --> P1[Worker 1]
Tasks --> P2[Worker 2]
Tasks --> P3[Worker 3]
Tasks --> P4[Worker 4]

P1 --> Results
P2 --> Results
P3 --> Results
P4 --> Results
```

## Overview

Demonstrates Process Pool.

## What I Learned

* Worker pools
* Task distribution

## How to Execute

```bash
python process_pool.py
```

## Advantages

* Efficient parallel processing
* Automatic worker management

## Disadvantages

* Pool setup overhead

## Summary

Shows how tasks are distributed across worker processes.

---

# communicating_with_queue.py

## Architecture

```mermaid
flowchart LR

Producer --> Queue
Queue --> Consumer1
Queue --> Consumer2
```

## Overview

Demonstrates Queue-based communication.

## What I Learned

* Producer-consumer model
* Shared queues

## How to Execute

```bash
python communicating_with_queue.py
```

## Summary

Shows safe communication using multiprocessing queues.

---

# communicating_with_pipe.py

## Architecture

```mermaid
flowchart LR

Process_A <-->|Pipe| Process_B
```

## Overview

Demonstrates Pipe communication.

## What I Learned

* Inter-process communication
* Bidirectional messaging

## How to Execute

```bash
python communicating_with_pipe.py
```

## Summary

Shows data exchange using multiprocessing pipes.

---

# run_background_processes.py

## Architecture

```mermaid
graph TD

Main --> Daemon

Main --> Normal

Main --> Exit

Exit --> DaemonStopped
```

## Overview

Demonstrates daemon processes.

## What I Learned

* Background execution
* Daemon behavior

## How to Execute

```bash
python run_background_processes.py
```

## Summary

Shows how daemon processes terminate when the main process exits.

---

# run_background_processes_no_daemons.py

## Architecture

```mermaid
graph TD

Main --> Process1
Main --> Process2

Main --> Exit

Process1 --> Finish
Process2 --> Finish
```

## Overview

Demonstrates non-daemon processes.

## What I Learned

* Independent process execution

## How to Execute

```bash
python run_background_processes_no_daemons.py
```

## Summary

Shows that normal processes continue until completion.

---

# killing_processes.py

## Architecture

```mermaid
stateDiagram-v2

[*] --> Created
Created --> Running
Running --> Terminated
Terminated --> [*]
```

## Overview

Demonstrates process termination.

## What I Learned

* Process lifecycle
* Terminate operation

## How to Execute

```bash
python killing_processes.py
```

## Summary

Shows how running processes can be stopped programmatically.

---

# processes_barrier.py

## Architecture

```mermaid
flowchart TD

P1[Process 1] --> Barrier
P2[Process 2] --> Barrier
P3[Process 3] --> Barrier

Barrier --> Continue
```

## Overview

Demonstrates Barrier synchronization.

## What I Learned

* Synchronization points
* Coordinated execution

## How to Execute

```bash
python processes_barrier.py
```

## Summary

Shows how processes wait until all participants arrive.

---

# FINAL CHAPTER SUMMARY

## Topics Covered


---

## Chapter 02 vs Chapter 03

```mermaid
flowchart LR

Threading --> SharedMemory
Threading --> Lightweight

Multiprocessing --> SeparateMemory
Multiprocessing --> TrueParallelism
```

| Chapter 02 | Chapter 03 |
|------------|------------|
| Threading | Multiprocessing |
| Shared Memory | Separate Memory |
| Lightweight | Higher Resource Usage |
| Good for I/O Tasks | Good for CPU Tasks |
| Uses threading | Uses multiprocessing |

---

## Overall Understanding

Chapter 03 teaches how Python processes:

* Run in parallel
* Use multiple CPU cores
* Communicate through Queues and Pipes
* Synchronize with Barriers
* Execute background tasks
* Manage worker pools efficiently

This chapter provides the foundation for building scalable multiprocessing applications in Python.