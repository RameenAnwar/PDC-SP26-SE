# Chapter 03 – Process Based Parallelism

## Chapter Overview

```mermaid
graph TD
    A[Process Based Parallelism]

    A --> B[Process Creation]
    A --> C[Process Management]
    A --> D[Communication & Synchronization]

    B --> E[Spawning Processes]
    B --> F[Process Subclassing]
    B --> G[Process Pool]

    C --> H[Naming Processes]
    C --> I[Daemon Processes]
    C --> J[Non-Daemon Processes]
    C --> K[Killing Processes]

    D --> L[Pipe Communication]
    D --> M[Queue Communication]
    D --> N[Barrier Synchronization]
```

---

## 1. Spawning Processes 

### Definition

Process spawning is the creation of new processes to execute tasks independently.

### Flow

```mermaid
flowchart TD
    A[Main Program]
    B[Create Process]
    C[Start Process]
    D[Execute Task]
    E[Join Process]
    F[End]

    A --> B --> C --> D --> E --> F
```

### Advantages

* True parallel execution
* Better CPU utilization
* Process isolation

### Disadvantages

* Higher memory usage
* Process creation overhead

---

## 2. Namespace Process Execution 

### Definition

Uses a function imported from another module and executes it inside separate processes.

### Flow

Import Function → Create Process → Execute Function → Join Process

### Advantages

* Better code organization
* Reusable functions

### Disadvantages

* Requires separate modules
* Slightly harder to debug

---

## 3. Custom Function

### Definition

A simple function executed by different processes to demonstrate multiprocessing.

### Flow

Receive Input → Print Process Number → Loop → Display Output

### Advantages

* Reusable function
* Easy to understand

### Disadvantages

* Limited functionality
* Used mainly for demonstration

---

## 4. Process Subclassing

### Definition

Creates a custom process by inheriting from the Process class.

### Flow

Create Subclass → Override run() Method → Start Process → Execute Task

### Advantages

* Cleaner object-oriented design
* Easy customization

### Disadvantages

* More code required
* Slightly complex for beginners

---

## 5. Naming Processes 

### Definition

Assigns custom names to processes for identification and debugging.

### Flow

Create Process → Assign Name → Start → Execute → End

### Advantages

* Easy monitoring
* Better debugging

### Disadvantages

* Extra configuration
* Names do not affect performance

---

## 6. Background Processes (Daemon) 

### Definition

Daemon processes run in the background and terminate automatically when the main process ends.

### Flow

```mermaid
graph TD
    A[Main Process]
    A --> B[Daemon Process]
    B --> C[Runs in Background]
    A --> D[Main Ends]
    D --> E[Daemon Stops Automatically]
```

### Advantages

* Useful for background services
* Automatic cleanup

### Disadvantages

* Can terminate unexpectedly
* Not suitable for critical tasks

---

## 7. Non-Daemon Processes 

### Definition

Processes continue running even if the parent process exits.

### Flow

```mermaid
graph TD
    A[Main Process]
    A --> B[Non-Daemon Process]
    A --> C[Main Ends]
    B --> D[Continues Running]
    D --> E[Task Complete]
```

### Advantages

* Reliable execution
* Completes assigned tasks

### Disadvantages

* Requires manual management
* May consume resources longer

---

## 8. Process Pool 

### Definition

A process pool manages multiple worker processes for executing tasks efficiently.

### Flow

```mermaid
graph TD
    A[Task Queue]
    A --> B[Process Pool]

    B --> C[Worker P1]
    B --> D[Worker P2]
    B --> E[Worker P3]

    C --> F[Results]
    D --> F
    E --> F
```

### Advantages

* Faster task execution
* Efficient resource management

### Disadvantages

* More memory usage
* Pool management overhead

---

## 9. Process Barrier Synchronization 

### Definition

A Barrier synchronizes multiple processes, forcing them to wait until all reach the same point.

### Flow

```mermaid
graph LR
    A[P1] --> D[Barrier]
    B[P2] --> D
    C[P3] --> D
    D --> E[Continue Together]
```

### Advantages

* Synchronization control
* Prevents timing issues

### Disadvantages

* Can cause delays
* More complex coordination

---

## 10. Inter-Process Communication Using Pipe 

### Definition

A Pipe allows two processes to communicate directly by sending and receiving data.

### Flow

```mermaid
graph LR
    A[Process A]
    B[Pipe]
    C[Process B]

    A --> B --> C
```

### Advantages

* Fast communication
* Simple implementation

### Disadvantages

* Limited scalability
* Suitable mainly for two processes

---

## 11. Inter-Process Communication Using Queue 

### Definition

A Queue allows multiple processes to safely exchange data.

### Flow

```mermaid
graph TD
    A[Producer]
    B[Queue]
    C[Consumer]

    A --> B --> C
```

### Advantages

* Thread-safe and process-safe
* Supports multiple producers and consumers

### Disadvantages

* Slight communication overhead
* Queue management required

---

## 12. Killing Processes 

### Definition

Demonstrates how to terminate a running process before completion.

### Flow

```mermaid
flowchart TD
    A[Start Process]
    B[Execute Task]
    C[Terminate Process]
    D[Join Process]
    E[End]

    A --> B --> C --> D --> E
```

### Advantages

* Stops unnecessary tasks
* Resource control

### Disadvantages

* Data loss risk
* Incomplete execution

---

# Process Communication Comparison

| Feature       | Pipe       | Queue           |
| ------------- | ---------- | --------------- |
| Communication | One-to-One | Many-to-Many    |
| Speed         | Faster     | Slightly Slower |
| Complexity    | Simple     | Flexible        |
| Scalability   | Limited    | High            |

---

# Final Summary

* Processes enable true parallel execution.
* Process spawning creates independent tasks.
* Process subclassing improves code structure.
* Named processes help debugging.
* Daemon processes run in the background.
* Process pools manage multiple workers efficiently.
* Barriers synchronize process execution.
* Pipes and Queues provide inter-process communication.
* Processes can be terminated when required.
* Multiprocessing improves performance for CPU-intensive tasks.

