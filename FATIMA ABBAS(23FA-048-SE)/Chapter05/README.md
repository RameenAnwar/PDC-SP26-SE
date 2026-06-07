# Chapter 05 – Synchronization and Communication in Parallel Programming

## Chapter Overview

```mermaid
graph TD
    A[Parallel Programming]

    A --> B[Threading]
    A --> C[Multiprocessing]
    A --> D[Pipes]
    A --> E[Semaphores]
    A --> F[Events]
    A --> G[Conditions]
    A --> H[Barriers]
    A --> I[RLocks]
```
---

# 1. Threading

### Definition

Threading allows multiple threads to execute within a single process.

### Flow

```mermaid
flowchart TD
    A[Main Thread]
    B[Create Threads]
    C[Execute Tasks]
    D[Wait for Completion]
    E[End]

    A --> B --> C --> D --> E
```

### Advantages

- Lightweight
- Shared memory
- Fast context switching

### Disadvantages

- Race conditions
- Synchronization issues

---

# 2. Multiprocessing

### Definition

Multiprocessing uses separate processes to achieve true parallel execution.

### Flow

```mermaid
flowchart TD
    A[Main Process]
    B[Create Child Processes]
    C[Execute Tasks]
    D[Collect Results]
    E[Terminate]

    A --> B --> C --> D --> E
```

### Advantages

- Utilizes multiple CPU cores
- Better performance for CPU-bound tasks

### Disadvantages

- Higher memory usage
- Inter-process communication required

---

# 3. Pipes

### Definition

Pipes provide communication between processes.

### Flow

```mermaid
graph LR
    A[Process A] -->|Send Data| B[Pipe]
    B -->|Receive Data| C[Process B]
```

### Advantages

- Simple IPC mechanism
- Fast communication

### Disadvantages

- Limited flexibility
- Mainly for related processes

---

# 4. Semaphore

### Definition

A semaphore controls access to shared resources.

### Flow

```mermaid
flowchart TD
    A[Thread Request]
    B{Semaphore Available?}
    C[Access Resource]
    D[Wait]
    E[Release Resource]

    A --> B
    B -->|Yes| C --> E
    B -->|No| D
```

### Advantages

- Prevents resource conflicts
- Controls concurrent access

### Disadvantages

- Deadlock possibility
- Difficult debugging

---

# 5. Event

### Definition

An Event is used for signaling between threads.

### Flow

```mermaid
flowchart TD
    A[Waiting Thread]
    B[Event Triggered]
    C[Continue Execution]

    A --> B --> C
```

### Advantages

- Easy thread coordination
- Clear signaling mechanism

### Disadvantages

- Limited synchronization capability

---

# 6. Condition

### Definition

A Condition allows threads to wait until a specific condition becomes true.

### Flow

```mermaid
flowchart TD
    A[Thread Wait]
    B[Condition Met]
    C[Notify Thread]
    D[Resume Execution]

    A --> B --> C --> D
```

### Advantages

- Efficient waiting
- Supports producer-consumer pattern

### Disadvantages

- Complex implementation

---

# 7. Barrier

### Definition

A Barrier blocks threads until all participating threads reach the same point.

### Flow

```mermaid
graph TD
    A[Thread 1]
    B[Thread 2]
    C[Thread 3]

    A --> D[Barrier]
    B --> D
    C --> D

    D --> E[Continue Together]
```

### Advantages

- Synchronizes groups of threads
- Useful in parallel algorithms

### Disadvantages

- One slow thread delays all others

---

# 8. RLock

### Definition

An RLock (Reentrant Lock) allows the same thread to acquire a lock multiple times.

### Flow

```mermaid
flowchart TD
    A[Acquire Lock]
    B[Acquire Again]
    C[Execute Code]
    D[Release Lock]
    E[Release Again]

    A --> B --> C --> D --> E
```

### Advantages

- Prevents self-deadlock
- Useful for nested locking

### Disadvantages

- Slightly higher overhead

---

# Synchronization Architecture

```mermaid
graph TD
    A[Shared Resource]

    B[Thread 1]
    C[Thread 2]
    D[Thread 3]

    B --> E[Semaphore/Lock]
    C --> E
    D --> E

    E --> A
```

---

# Threading vs Multiprocessing

| Feature | Threading | Multiprocessing |
|----------|-----------|----------------|
| Memory | Shared | Separate |
| Speed | Faster Creation | Slower Creation |
| CPU Usage | Limited by GIL | True Parallelism |
| Communication | Easy | Complex |
| Best For | I/O Tasks | CPU Tasks |

---

# Final Summary

- Threading enables lightweight concurrency.
- Multiprocessing provides true parallel execution.
- Pipes support inter-process communication.
- Semaphores control resource access.
- Events provide thread signaling.
- Conditions enable waiting for specific states.
- Barriers synchronize multiple threads.
- RLocks allow repeated locking by the same thread.
- Synchronization mechanisms prevent race conditions and improve program reliability.
