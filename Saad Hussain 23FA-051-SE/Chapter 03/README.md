# Chapter 03 - Process Based Parallelism in Python

Course materials for **Parallel and Distributed Computing (PDC)**. This chapter focuses on Python's `multiprocessing` module and demonstrates how to create, name, manage, synchronize, and communicate between processes.

Repository path: [PDC-SP26-SE / Saad Hussain 23FA-051-SE / Chapter 03](https://github.com/saadh472/PDC-SP26-SE/tree/main/Saad%20Hussain%2023FA-051-SE/Chapter%2003).

## Folder structure

| Folder | Purpose |
|--------|---------|
| [`Code`](Code) | Python source files for Chapter 03 multiprocessing examples. |
| [`Screenshot Output`](<Screenshot Output>) | Output screenshots for the matching Python examples. |

## What is in this chapter

| File | Description | Output |
|------|-------------|--------|
| [`Code/spawning_processes.py`](Code/spawning_processes.py) | Spawns multiple processes and runs `myFunc` with different arguments. | [`Screenshot`](<Screenshot Output/spawning_processes.png>) |
| [`Code/spawning_processes_namespace.py`](Code/spawning_processes_namespace.py) | Imports `myFunc` from a separate file and uses it as a process target. | [`Screenshot`](<Screenshot Output/spawning_processes_namespace.png>) |
| [`Code/myFunc.py`](Code/myFunc.py) | Shared helper function used by the namespace spawning example. | [`Screenshot`](<Screenshot Output/myFunc.png>) |
| [`Code/naming_processes.py`](Code/naming_processes.py) | Demonstrates default and custom process names. | [`Screenshot`](<Screenshot Output/naming_processes.png>) |
| [`Code/run_background_processes.py`](Code/run_background_processes.py) | Compares daemon and non-daemon background process behavior. | [`Screenshot`](<Screenshot Output/run_background_processes.png>) |
| [`Code/run_background_processes_no_daemons.py`](Code/run_background_processes_no_daemons.py) | Runs background processes without daemon mode. | [`Screenshot`](<Screenshot Output/run_background_processes_no_daemons.png>) |
| [`Code/killing_processes.py`](Code/killing_processes.py) | Starts a process, terminates it, and checks its status. | [`Screenshot`](<Screenshot Output/killing_processes.png>) |
| [`Code/process_in_subclass.py`](Code/process_in_subclass.py) | Creates a process by subclassing `multiprocessing.Process`. | [`Screenshot`](<Screenshot Output/process_in_subclass.png>) |
| [`Code/process_pool.py`](Code/process_pool.py) | Uses a process pool to calculate square values in parallel. | [`Screenshot`](<Screenshot Output/process_pool.png>) |
| [`Code/processes_barrier.py`](Code/processes_barrier.py) | Synchronizes multiple processes with a `Barrier` and serializes output with a `Lock`. | [`Screenshot`](<Screenshot Output/processes_barrier.png>) |
| [`Code/communicating_with_queue.py`](Code/communicating_with_queue.py) | Implements producer and consumer processes using `multiprocessing.Queue`. | [`Screenshot`](<Screenshot Output/communicating_with_queue.png>) |
| [`Code/communicating_with_pipe.py`](Code/communicating_with_pipe.py) | Sends data between processes using `multiprocessing.Pipe`. | [`Screenshot`](<Screenshot Output/communicating_with_pipe.png>) |

## How to run

From this directory (`Chapter 03`):

```bash
cd Code
python spawning_processes.py
python process_pool.py
python communicating_with_queue.py
```

Run any other script in the same way. On Windows, use `python` or `py` depending on your Python installation.

## Concepts covered

- Creating processes with `multiprocessing.Process`.
- Passing arguments to process target functions.
- Naming and identifying child processes.
- Running daemon and non-daemon background processes.
- Terminating processes safely for demonstration purposes.
- Subclassing `multiprocessing.Process`.
- Using `multiprocessing.Pool` for parallel work distribution.
- Synchronizing processes with `Barrier` and `Lock`.
- Communicating between processes with `Queue` and `Pipe`.

## Requirements

- Python 3.x
- Standard library only (`multiprocessing`, `time`, `random`, etc.)

---

*PDC-SP26-SE - Saad Hussain 23FA-051-SE*
