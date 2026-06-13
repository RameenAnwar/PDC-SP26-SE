# MPI Programming with mpi4py

## Overview

This project demonstrates parallel programming using the Message Passing Interface (MPI) through the Python library **mpi4py**.

MPI is one of the most widely used standards for distributed-memory parallel computing. It allows multiple processes to communicate and cooperate while executing across one or more machines.

The examples in this chapter cover:

* MPI initialization
* Process ranks and communicators
* Point-to-point communication
* Broadcast
* Scatter
* Gather
* Reduction operations
* All-to-All communication
* Deadlock situations
* Virtual topologies

---

# Project Structure

```text
├── helloworld_MPI.py
├── pointToPointCommunication.py
├── broadcast.py
├── scatter.py
├── gather.py
├── reduction.py
├── alltoall.py
├── deadlockProblems.py
└── virtualTopology.py
```

---

# Requirements

## Software

* Python 3.x
* MPI Implementation (MPICH or OpenMPI)

## Python Libraries

```bash
pip install mpi4py numpy
```

---

# Learning Objectives

After completing this chapter, students will be able to:

* Understand MPI architecture
* Create MPI processes
* Exchange data between processes
* Use collective communication operations
* Perform parallel reductions
* Design virtual process topologies
* Identify and avoid deadlocks

---

# Basic MPI Concepts

## Communicator

A communicator is a group of MPI processes that can communicate with each other.

```python
comm = MPI.COMM_WORLD
```

---

## Rank

Every process has a unique identifier called a rank.

```python
rank = comm.Get_rank()
```

Example:

```text
Process 0
Process 1
Process 2
Process 3
```

---

## Size

Represents the total number of MPI processes.

```python
size = comm.Get_size()
```

---

# File Descriptions

---

## 1. helloworld_MPI.py

### Purpose

The simplest MPI program.

### Functionality

Each process prints its rank.

### Example Output

```text
hello world from process 0
hello world from process 1
hello world from process 2
hello world from process 3
```

### Learning Outcome

Understand MPI initialization and rank identification.

---

## 2. pointToPointCommunication.py

### Purpose

Demonstrates direct communication between specific processes.

### Concepts Covered

* send()
* recv()

### Workflow

* Process 0 sends data to Process 4.
* Process 1 sends data to Process 8.
* Processes 4 and 8 receive the messages.

### Learning Outcome

Understand basic point-to-point communication.

---

## 3. broadcast.py

### Purpose

Demonstrates Broadcast communication.

### Concepts Covered

* bcast()

### Workflow

1. Process 0 creates data.
2. MPI broadcasts the data.
3. Every process receives the same value.

### Example

```text
Process 0 → 100
Process 1 → 100
Process 2 → 100
Process 3 → 100
```

### Learning Outcome

Learn one-to-many communication.

---

## 4. scatter.py

### Purpose

Demonstrates Scatter communication.

### Concepts Covered

* scatter()

### Workflow

1. Process 0 owns an array.
2. Array elements are distributed among processes.
3. Each process receives one element.

### Example

```text
Array = [1,2,3,4]

Process 0 receives 1
Process 1 receives 2
Process 2 receives 3
Process 3 receives 4
```

### Learning Outcome

Understand data distribution.

---

## 5. gather.py

### Purpose

Demonstrates Gather communication.

### Concepts Covered

* gather()

### Workflow

1. Each process creates data.
2. All data is sent to Process 0.
3. Process 0 collects all results.

### Example

```text
P0 → 1
P1 → 4
P2 → 9
P3 → 16
```

Collected by Process 0:

```text
[1,4,9,16]
```

### Learning Outcome

Understand many-to-one communication.

---

## 6. reduction.py

### Purpose

Demonstrates Reduction operations.

### Concepts Covered

* Reduce()
* MPI.SUM

### Workflow

1. Every process generates an array.
2. MPI adds corresponding elements.
3. Result is stored in Process 0.

### Example

```text
P0 → [0,1,2]
P1 → [0,2,4]
P2 → [0,3,6]
```

Reduction Result:

```text
[0,6,12]
```

### Learning Outcome

Understand parallel aggregation operations.

---

## 7. alltoall.py

### Purpose

Demonstrates All-to-All communication.

### Concepts Covered

* Alltoall()

### Workflow

Every process:

* Sends data to every other process.
* Receives data from every other process.

### Example

```text
Process 0 sends to all
Process 1 sends to all
Process 2 sends to all
Process 3 sends to all
```

### Learning Outcome

Understand complete process communication.

---

## 8. deadlockProblems.py

### Purpose

Demonstrates a potential MPI deadlock scenario.

### Concepts Covered

* Blocking communication
* Communication ordering

### Workflow

Processes exchange messages.

Improper ordering of send() and recv() calls may cause processes to wait indefinitely.

### Learning Outcome

Understand deadlocks and how to avoid them.

---

## 9. virtualTopology.py

### Purpose

Demonstrates creation of a Cartesian Virtual Topology.

### Concepts Covered

* Create_cart()
* Shift()
* Neighbor discovery

### Workflow

1. Processes are arranged in a grid.
2. Each process identifies:

   * Upper neighbor
   * Lower neighbor
   * Left neighbor
   * Right neighbor

### Example

```text
0 1
2 3
```

Process 0:

```text
UP = 2
DOWN = 2
LEFT = 1
RIGHT = 1
```

### Learning Outcome

Understand process topologies used in scientific computing.

---

# MPI Collective Communication Summary

| Operation | Communication Type       |
| --------- | ------------------------ |
| Broadcast | One → All                |
| Scatter   | One → Many               |
| Gather    | Many → One               |
| Reduce    | Many → One (Computation) |
| Alltoall  | All ↔ All                |

---

# Running the Programs

## Hello World

```bash
mpiexec -n 4 python helloworld_MPI.py
```

---

## Broadcast

```bash
mpiexec -n 4 python broadcast.py
```

---

## Scatter

```bash
mpiexec -n 4 python scatter.py
```

---

## Gather

```bash
mpiexec -n 4 python gather.py
```

---

## Reduction

```bash
mpiexec -n 4 python reduction.py
```

---

## All-to-All

```bash
mpiexec -n 4 python alltoall.py
```

---

## Virtual Topology

```bash
mpiexec -n 4 python virtualTopology.py
```

---

# Key Concepts Learned

This chapter introduces:

* MPI Fundamentals
* Distributed Memory Computing
* MPI Communicators
* Process Ranks
* Point-to-Point Communication
* Collective Communication
* Data Distribution
* Parallel Reduction
* Deadlock Prevention
* Virtual Topologies

---

# Comparison of MPI Communication Methods

| Method    | Description                                         |
| --------- | --------------------------------------------------- |
| send/recv | Direct communication between two processes          |
| Broadcast | One process sends to all                            |
| Scatter   | Distribute data among processes                     |
| Gather    | Collect data from processes                         |
| Reduce    | Aggregate results                                   |
| Alltoall  | Every process communicates with every other process |

---

# Conclusion

This project provides hands-on experience with MPI programming using Python and mpi4py. Through practical examples, students learn how distributed processes communicate, synchronize, exchange data, and perform parallel computations. These concepts form the foundation of high-performance computing (HPC), scientific simulations, distributed systems, and large-scale parallel applications.
