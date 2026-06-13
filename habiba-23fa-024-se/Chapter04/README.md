# Chapter 04 – MPI (Message Passing Interface)

## Chapter Overview

```mermaid
graph TD
    A[MPI Programming]

    A --> B[Basic MPI]
    A --> C[Point-to-Point Communication]
    A --> D[Collective Communication]
    A --> E[Advanced MPI]

    B --> F[Hello World MPI]

    C --> G[Send & Receive]
    C --> H[Deadlock Problems]

    D --> I[Broadcast]
    D --> J[Scatter]
    D --> K[Gather]
    D --> L[Reduction]
    D --> M[All-to-All]

    E --> N[Virtual Topology]
```

---

# 1. Hello World MPI 
### Definition

The simplest MPI program where each process prints its rank (ID).

### Flow

```mermaid
flowchart TD
    A[Start MPI Program]
    B[Initialize MPI]
    C[Get Process Rank]
    D[Print Hello World]
    E[End]

    A --> B --> C --> D --> E
```

### Advantages

* Easy introduction to MPI
* Demonstrates process ranks

### Disadvantages

* No communication between processes
* Limited functionality

---

# 2. Point-to-Point Communication 

### Definition

Allows one process to send data directly to another process using send() and recv().

### Flow

```mermaid
graph LR
    A[Process 0]
    B[Process 4]

    A -- Send Data --> B
```

### Advantages

* Simple communication model
* Direct data transfer

### Disadvantages

* Difficult to manage in large systems
* Requires sender and receiver coordination

---

# 3. Broadcast Communication 
### Definition

One process sends the same data to all other processes.

### Flow

```mermaid
graph TD
    A[Root Process]

    A --> B[P1]
    A --> C[P2]
    A --> D[P3]
    A --> E[P4]
```

### Advantages

* Efficient data sharing
* Reduces repeated sending operations

### Disadvantages

* All processes receive identical data
* Can increase network traffic

---

# 4. Scatter Communication 

### Definition

Scatter distributes different portions of data from one process to multiple processes.

### Flow

```mermaid
graph TD
    A[Root Process]
    A --> B[Data Part 1]
    A --> C[Data Part 2]
    A --> D[Data Part 3]
    A --> E[Data Part 4]
```

### Advantages

* Efficient workload distribution
* Supports parallel processing

### Disadvantages

* Requires data partitioning
* Uneven distribution may reduce efficiency

---

# 5. Gather Communication 

### Definition

Gather collects data from all processes and sends it to a root process.

### Flow

```mermaid
graph TD
    B[P1]
    C[P2]
    D[P3]
    E[P4]

    B --> A[Root Process]
    C --> A
    D --> A
    E --> A
```

### Advantages

* Centralized result collection
* Easy data aggregation

### Disadvantages

* Root process can become a bottleneck
* Increased communication overhead

---

# 6. Reduction Operation 

### Definition

Combines data from all processes using an operation such as SUM, MAX, MIN, or PRODUCT.

### Flow

```mermaid
graph TD
    B[P1]
    C[P2]
    D[P3]
    E[P4]

    B --> A[SUM]
    C --> A
    D --> A
    E --> A

    A --> F[Final Result]
```

### Advantages

* Efficient aggregation
* Optimized MPI implementation

### Disadvantages

* Limited to supported operations
* Requires synchronization

---

# 7. All-to-All Communication 

### Definition

Every process sends data to every other process and receives data from all processes.

### Flow

```mermaid
graph LR
    A[P1]
    B[P2]
    C[P3]
    D[P4]

    A <--> B
    A <--> C
    A <--> D
    B <--> C
    B <--> D
    C <--> D
```

### Advantages

* Complete data exchange
* Useful for distributed algorithms

### Disadvantages

* High communication cost
* Poor scalability for large systems

---

# 8. Deadlock Problems 

### Definition

A deadlock occurs when two or more processes wait indefinitely for each other to send or receive data.

### Flow

```mermaid
graph LR
    A[Process 1 Waiting]
    B[Process 5 Waiting]

    A --> B
    B --> A
```

### Advantages

* Demonstrates synchronization issues
* Helps understand communication ordering

### Disadvantages

* Program may freeze
* Difficult debugging

---

# 9. Virtual Topology 

### Definition

MPI can arrange processes into logical structures such as grids, rings, or meshes to simplify communication.

### Flow

```mermaid
graph TD
    A[P0] --- B[P1]
    B --- C[P2]

    D[P3] --- E[P4]
    E --- F[P5]

    A --- D
    B --- E
    C --- F
```

### Advantages

* Organized communication structure
* Simplifies neighbor communication

### Disadvantages

* More complex implementation
* Additional topology management

---

# MPI Communication Comparison

| Operation        | Purpose                     |
| ---------------- | --------------------------- |
| Send/Receive     | One-to-One Communication    |
| Broadcast        | One-to-All Communication    |
| Scatter          | Divide Data Among Processes |
| Gather           | Collect Data from Processes |
| Reduce           | Combine Results             |
| All-to-All       | Every Process Communicates  |
| Virtual Topology | Structured Communication    |

---

# MPI Collective Operations Overview

```mermaid
graph TD
    A[Root Process]

    A --> B[Broadcast]

    C[Scatter]
    C --> D[P1]
    C --> E[P2]
    C --> F[P3]

    G[P1]
    H[P2]
    I[P3]

    G --> J[Gather]
    H --> J
    I --> J

    K[P1]
    L[P2]
    M[P3]

    K --> N[Reduce]
    L --> N
    M --> N
```

---

# Final Summary

* MPI enables parallel computing across multiple processes.
* Process ranks identify individual processes.
* Point-to-point communication uses Send and Receive operations.
* Broadcast shares data with all processes.
* Scatter distributes data among processes.
* Gather collects results from processes.
* Reduction combines multiple values into a single result.
* All-to-All allows complete process communication.
* Deadlocks occur when processes wait indefinitely.
* Virtual topologies organize process communication structures.


