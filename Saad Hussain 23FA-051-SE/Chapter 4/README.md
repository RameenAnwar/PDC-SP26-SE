# Chapter 4 - Message Passing Interface in Python

Course materials for **Parallel and Distributed Computing (PDC)**. This chapter focuses on distributed-memory parallel programming using **MPI** with Python's `mpi4py` package.

Repository path: [PDC-SP26-SE / Saad Hussain 23FA-051-SE / Chapter 4](https://github.com/saadh472/PDC-SP26-SE/tree/main/Saad%20Hussain%2023FA-051-SE/Chapter%204).

## Folder structure

| Folder | Purpose |
|--------|---------|
| [`Code`](Code) | Python source files for Chapter 4 MPI examples. |
| [`Screenshots`](Screenshots) | Output screenshots for the matching Python examples. |

## What is in this chapter

| File | Description | Output |
|------|-------------|--------|
| [`Code/helloworld_MPI.py`](Code/helloworld_MPI.py) | Prints a hello-world message from each MPI process with its rank. | [`Screenshot`](Screenshots/helloworld_MPI.png) |
| [`Code/pointToPointCommunication.py`](Code/pointToPointCommunication.py) | Demonstrates point-to-point communication with `send()` and `recv()` between selected ranks. | [`Screenshot`](Screenshots/pointToPointCommunication.png) |
| [`Code/deadLockProblems.py`](Code/deadLockProblems.py) | Shows communication ordering between two ranks and why send/receive order matters. | [`Screenshot`](Screenshots/deadLockProblems.png) |
| [`Code/broadcast.py`](Code/broadcast.py) | Shares one value from the root process to all processes with `bcast()`. | [`Screenshot`](Screenshots/broadcast.png) |
| [`Code/scatter.py`](Code/scatter.py) | Distributes one element from an array to each process with `scatter()`. | [`Screenshot`](Screenshots/scatter.png) |
| [`Code/gather.py`](Code/gather.py) | Collects computed values from all processes at the root process with `gather()`. | [`Screenshot`](Screenshots/gather.png) |
| [`Code/reduction.py`](Code/reduction.py) | Performs element-wise summation across processes with `Reduce()` and `MPI.SUM`. | [`Screenshot`](Screenshots/reduction.png) |
| [`Code/alltoall.py`](Code/alltoall.py) | Sends data from every process to every other process with `Alltoall()`. | [`Screenshot`](Screenshots/alltoall.png) |
| [`Code/virtualTopology.py`](Code/virtualTopology.py) | Builds a Cartesian virtual topology and prints neighbor ranks. | [`Screenshot`](Screenshots/virtualTopology.png) |

## How to run

From this directory (`Chapter 4`):

```bash
cd Code
mpiexec -n 4 python helloworld_MPI.py
mpiexec -n 4 python broadcast.py
mpiexec -n 4 python gather.py
```

Some examples require specific process counts:

```bash
mpiexec -n 9 python pointToPointCommunication.py
mpiexec -n 10 python scatter.py
mpiexec -n 6 python deadLockProblems.py
```

On some systems, `mpirun` may be used instead of `mpiexec`.

## Concepts covered

- MPI communicator basics with `MPI.COMM_WORLD`.
- Process rank and communicator size.
- Point-to-point communication using `send()` and `recv()`.
- Collective communication using `bcast()`, `scatter()`, `gather()`, `Reduce()`, and `Alltoall()`.
- Data exchange with NumPy arrays.
- Cartesian virtual topologies and process neighbors.
- Common communication ordering issues.

## Requirements

- Python 3.x
- MPI runtime such as Microsoft MPI, MPICH, or Open MPI
- Python packages: `mpi4py`, `numpy`

---

*PDC-SP26-SE - Saad Hussain 23FA-051-SE*
