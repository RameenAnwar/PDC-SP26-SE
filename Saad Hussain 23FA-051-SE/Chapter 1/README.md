# Chapter 1 — Python Foundations & Parallelism Intro

Course materials for **Parallel and Distributed Computing (PDC)**. This chapter pairs basic Python with introductory experiments comparing **serial execution**, **multithreading**, and **multiprocessing**.

Repository path: [PDC-SP26-SE / Saad Hussain 23FA-051-SE](https://github.com/saadh472/PDC-SP26-SE/tree/main/Saad%20Hussain%2023FA-051-SE).

## What’s in this folder

| Path | Purpose |
|------|---------|
| [`Code/do_something.py`](Code/do_something.py) | Shared helper: fills a list with random floats in a loop (CPU-style work unit). |
| [`Code/serial_test.py`](Code/serial_test.py) | Runs `do_something` **10 times in sequence**; prints total wall-clock time. |
| [`Code/multithreading_test.py`](Code/multithreading_test.py) | Spawns **10 threads**, each with its own list; times total execution. |
| [`Code/multiprocessing_test.py`](Code/multiprocessing_test.py) | Spawns **10 processes** with the same pattern; times total execution. |
| [`Code/thread_and_processes.py`](Code/thread_and_processes.py) | Combined demo: threading then multiprocessing on one script (see note below). |
| [`Code/lists.py`](Code/lists.py) | Lists, dicts, tuples, and using a function as a value (`len`). |
| [`Code/flow.py`](Code/flow.py) / [`Code/dir.py`](Code/dir.py) | Control flow: `if` / `for` / `while`. |
| [`Code/classes.py`](Code/classes.py) | Classes, instance vs class attributes, inheritance. |
| [`Code/file.py`](Code/file.py) | Write and read [`Code/test.txt`](Code/test.txt). |

## How to run

From this directory (`Chapter 1`):

```bash
cd Code
python serial_test.py
python multithreading_test.py
python multiprocessing_test.py
```

Scripts that import `do_something` expect to be run with `Code` as the working directory (or Python path including `Code`).

On **Windows**, use `python` or `py` as appropriate.

## Concepts covered

- **Python syntax**: variables, collections, control flow, classes, file I/O.
- **Concurrency vocabulary**: thread vs process; why CPU-bound loops often don’t speed up with threads in CPython (GIL), while processes can use multiple cores (with proper data handling).
- **Measurement**: timing serial vs parallel setups to compare wall-clock behavior.

## Note on `thread_and_processes.py`

This file is written as a single demo that runs threading and then multiprocessing. As written, the threading section uses `Thread(target=do_something(size, out_list))`, which **calls** `do_something` immediately instead of passing `target` and `args` to the thread—worth fixing if you use it for serious benchmarks. The multiprocessing section also shares one `out_list` across processes, which is not the usual safe pattern on Windows; the **split scripts** (`serial_test.py`, `multithreading_test.py`, `multiprocessing_test.py`) are clearer starting points.

## Requirements

- Python 3.x  
- Standard library only (`threading`, `multiprocessing`, etc.)

---

*PDC-SP26-SE — Saad Hussain 23FA-051-SE*
