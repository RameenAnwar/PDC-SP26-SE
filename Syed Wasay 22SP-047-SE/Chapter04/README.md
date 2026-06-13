# Chapter 04: Message Passing Interface (MPI) and Distributed Memory Systems

## Preface

Welcome to the academic documentation for Chapter 04 of the Parallel and Distributed Computing (PDC) course. In this chapter, we transition from single-machine parallel models (threading and multiprocessing) to distributed computing systems. 

Here, we explore the Message Passing Interface (MPI) standard using the `mpi4py` package. MPI allows multiple independent compute nodes to coordinate and execute tasks across network connections.

This document is divided into two sections: Section 1 explores the underlying theory of distributed memory and communication protocols, and Section 2 reviews the practical Python scripts and execution steps.

---

## Index of Topics

### Section 1: Distributed Computing Theory
1. [Distributed Memory Architectures](#1-distributed-memory-architectures)
    - [The Cluster Computing Model](#the-cluster-computing-model)
    - [Interconnection Topologies](#interconnection-topologies)
2. [The Message Passing Interface (MPI) Protocol](#2-the-message-passing-interface-mpi-protocol)
    - [Communicators, Ranks, and Sizes](#communicators-ranks-and-sizes)
    - [Python Serialization Constraints](#python-serialization-constraints)
3. [Communication Patterns](#3-communication-patterns)
    - [Point-to-Point Communication](#point-to-point-communication)
    - [Collective Operations](#collective-operations)
4. [Deadlocks in Message Passing](#4-deadlocks-in-message-passing)
5. [Virtual Topologies](#5-virtual-topologies)

### Section 2: Code Implementations
6. [Basic Environment Verification](#6-basic-environment-verification)
7. [Point-to-Point Messaging](#7-point-to-point-messaging)
8. [Broadcasting Values](#8-broadcasting-values)
9. [Scattering Arrays](#9-scattering-arrays)
10. [Gathering Data Pools](#10-gathering-data-pools)
11. [Matrix All-to-All Operations](#11-matrix-all-to-all-operations)
12. [Reduction Algorithms](#12-reduction-algorithms)
13. [Deadlock Demonstration](#13-deadlock-demonstration)
14. [Grid Virtual Topologies](#14-grid-virtual-topologies)
15. [Local Execution Guide](#15-local-execution-guide)

---

# SECTION 1: DISTRIBUTED COMPUTING THEORY

## 1. Distributed Memory Architectures

In a distributed memory system, individual compute nodes do not share physical memory. Each node has its own private processor and local random-access memory (RAM). A processor on Node A cannot directly read or write to a memory address on Node B.

### The Cluster Computing Model

To work together on a computational task, nodes must coordinate by sending messages over a network interface. This model requires that data be explicitly serialized (converted to a byte stream), sent over the network hardware, and then deserialized by the receiving node. Because network latency is significantly slower than local memory bus speeds, optimizing message-passing frequency is critical for performance.

### Interconnection Topologies

Compute nodes are connected using network switch architectures. Common physical configurations include Mesh, Ring, Torus, and Hypercube networks. The topology affects the speed and latency of communication between distant nodes.

## 2. The Message Passing Interface (MPI) Protocol

MPI is a standardized message-passing system designed for high-performance computing on parallel architectures. In Python, `mpi4py` provides bindings for C-based MPI implementations like OpenMPI or MPICH.

### Communicators, Ranks, and Sizes

- **Communicator:** A logical group of processes that can send messages to one another. The default communicator for all running processes is `MPI.COMM_WORLD`.
- **Rank:** A unique integer identifier assigned to each process in a communicator, starting from 0 (often designated as the root node).
- **Size:** The total number of active processes running within the communicator.

### Python Serialization Constraints

The `mpi4py` library uses two distinct sets of methods:
- **Lowercase Methods (`send`, `recv`, `bcast`):** These handle generic Python objects by serializing them with the `pickle` module. This is flexible but introduces processing overhead.
- **Uppercase Methods (`Send`, `Recv`, `Bcast`):** These transmit contiguous memory buffers (like NumPy arrays) directly using C-level pointers, maximizing throughput.

## 3. Communication Patterns

### Point-to-Point Communication

Point-to-point communication involves direct data transfer between exactly two processes: one sender and one receiver.
- **Blocking Communication:** The sending process halts until its message buffer is cleared, ensuring the data has been sent before proceeding.
- **Non-blocking Communication (`Isend`, `Irecv`):** Returns control immediately, allowing processes to continue computations while the data transfer occurs asynchronously.

### Collective Operations

Collective operations involve all processes within a communicator group simultaneously:
- **Broadcast:** The root process sends an identical copy of a single data value to all other processes.
- **Scatter:** The root process splits a contiguous array into equal segments and distributes one segment to each process in rank order.
- **Gather:** The inverse of scatter; the root process collects individual data segments from all processes and combines them into a single array.
- **All-to-All:** Every process sends and receives data segments to and from all other processes, performing a transposition of data across the network.
- **Reduction:** Processes combine their local values using a mathematical operation (such as addition or finding the maximum) as the data is collected, returning the final result to the root process.

## 4. Deadlocks in Message Passing

A deadlock occurs when processes are blocked indefinitely, each waiting for another to perform an action. In point-to-point communication, this typically happens when two processes both execute a blocking receive operation first, leaving no process available to send the corresponding data.

## 5. Virtual Topologies

While MPI ranks are naturally indexed as a linear array, physical simulations often map to multi-dimensional coordinate systems. MPI supports the creation of virtual Cartesian Topologies, allowing linear ranks to map to 2D or 3D grids to simplify neighbor calculations.

---

# SECTION 2: CODE IMPLEMENTATIONS

## 6. Basic Environment Verification

**Script name:** `helloworld_MPI.py`

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print(f"Hello world from process {rank} of {size}")
```

**Expected Console Output (with 4 processes):**
```text
Hello world from process 0 of 4
Hello world from process 2 of 4
Hello world from process 1 of 4
Hello world from process 3 of 4
```

The print statements arrive out of order due to independent scheduling by the operating system.

---

## 7. Point-to-Point Messaging

**Script name:** `pointToPointCommunication.py`

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
    print(f"Process {rank} sent data: {data}")
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print(f"Process {rank} received data: {data}")
```

**Expected Console Output:**
```text
Process 0 sent data: {'a': 7, 'b': 3.14}
Process 1 received data: {'a': 7, 'b': 3.14}
```

---

## 8. Broadcasting Values

**Script name:** `broadcast.py`

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    variable_to_share = 100
else:
    variable_to_share = None

variable_to_share = comm.bcast(variable_to_share, root=0)
print(f"Process {rank} has variable: {variable_to_share}")
```

**Expected Console Output:**
```text
Process 0 has variable: 100
Process 1 has variable: 100
Process 2 has variable: 100
Process 3 has variable: 100
```

---

## 9. Scattering Arrays

**Script name:** `scatter.py`

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = [(i+1)**2 for i in range(size)]
    print(f"Root generating data: {data}")
else:
    data = None

data = comm.scatter(data, root=0)
print(f"Process {rank} received data: {data}")
```

**Expected Console Output:**
```text
Root generating data: [1, 4, 9, 16]
Process 0 received data: 1
Process 1 received data: 4
...
```

---

## 10. Gathering Data Pools

**Script name:** `gather.py`

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = rank * 10
gathered_data = comm.gather(data, root=0)

if rank == 0:
    print(f"Root gathered data: {gathered_data}")
```

**Expected Console Output:**
```text
Root gathered data: [0, 10, 20, 30]
```

---

## 11. Matrix All-to-All Operations

**Script name:** `alltoall.py`

```python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

senddata = np.arange(size, dtype=int) * (rank + 1)
recvdata = np.empty(size, dtype=int)

comm.Alltoall(senddata, recvdata)
print(f"Rank {rank} send: {senddata} | recv: {recvdata}")
```

---

## 12. Reduction Algorithms

**Script name:** `reduction.py`

```python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

value = np.array([rank], dtype=float)
sum_val = np.array([0.0], dtype=float)

comm.Reduce(value, sum_val, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Global Sum is: {sum_val[0]}")
```

**Expected Console Output:**
```text
Global Sum is: 6.0
```

---

## 13. Deadlock Demonstration

**Script name:** `deadLockProblems.py`

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    data_recv = comm.recv(source=1, tag=2)
    comm.send(100, dest=1, tag=1)
elif rank == 1:
    data_recv = comm.recv(source=0, tag=1)
    comm.send(200, dest=0, tag=2)
```

Running this file will result in an infinite process hang due to mutually blocked calls.

---

## 14. Grid Virtual Topologies

**Script name:** `virtualTopology.py`

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

cartesian_communicator = comm.Create_cart(dims=[2, 2], periods=[False, False], reorder=False)
coords = cartesian_communicator.Get_coords(rank)

print(f"Rank {rank} is located at grid coordinates: {coords}")
```

---

## 15. Local Execution Guide

To run these distributed tests locally, you must use the `mpiexec` or `mpirun` tool to start the independent process instances. Navigate to the `Chapter04` directory and execute:

```bash
mpiexec -n 4 python helloworld_MPI.py
mpiexec -n 2 python pointToPointCommunication.py
mpiexec -n 4 python broadcast.py
mpiexec -n 4 python scatter.py
mpiexec -n 4 python gather.py
mpiexec -n 4 python alltoall.py
mpiexec -n 4 python reduction.py
mpiexec -n 4 python virtualTopology.py
```
