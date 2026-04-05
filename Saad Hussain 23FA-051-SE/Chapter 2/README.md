# Chapter 2 — Threading & Synchronization in Python

Course materials for **Parallel and Distributed Computing (PDC)**. This chapter focuses on **threads**, **identifying and naming threads**, and **synchronization primitives** used to coordinate access to shared state and to signal between producers and consumers.

Repository path: [PDC-SP26-SE / Saad Hussain 23FA-051-SE](https://github.com/saadh472/PDC-SP26-SE/tree/main/Saad%20Hussain%2023FA-051-SE).

## What’s in this folder

### Thread basics

| File | Description |
|------|-------------|
| [`Code/Thread_definition.py`](Code/Thread_definition.py) | Creates threads with `target` and `args`; sequential `start`/`join` per iteration (runs one thread at a time in practice). |
| [`Code/Thread_determine.py`](Code/Thread_determine.py) | Named threads running different functions; demonstrates overlapping execution and `join()`. |
| [`Code/Thread_name_and_processes.py`](Code/Thread_name_and_processes.py) | Subclass of `Thread` with a custom `run()`; prints thread-oriented messages. |
| [`Code/MyThreadClass.py`](Code/MyThreadClass.py) | Nine worker threads with random sleep durations; prints process ID and timing. |

### Locks

| File | Description |
|------|-------------|
| [`Code/MyThreadClass_lock.py`](Code/MyThreadClass_lock.py) | `threading.Lock()`: critical section wraps print + sleep (lock held for full duration). |
| [`Code/MyThreadClass_lock_2.py`](Code/MyThreadClass_lock_2.py) | Same pattern but lock only around the first print (shorter critical section). |
| [`Code/Rlock.py`](Code/Rlock.py) | Re-entrant lock (`RLock`) protecting nested `add`/`remove` calls on a shared `Box` counter. |

### Coordination & producer–consumer patterns

| File | Description |
|------|-------------|
| [`Code/Semaphore.py`](Code/Semaphore.py) | `Semaphore(0)` handoff: consumer blocks until producer `release()` after producing an item (logged). |
| [`Code/Event.py`](Code/Event.py) | `threading.Event` between producer and consumer; `set()` / `clear()` around shared list access. |
| [`Code/Condition.py`](Code/Condition.py) | `Condition` with `wait()` / `notify()` when buffer is empty or full (bounded list). |
| [`Code/Barrier.py`](Code/Barrier.py) | `Barrier`: runners wait until all reach the barrier (“race” demo). |
| [`Code/Threading_with_queue.py`](Code/Threading_with_queue.py) | `queue.Queue`: producer thread(s) and consumer thread(s); **note**: consumer loops `while True` and never exits—fine for a quick demo, not for a clean shutdown without extra logic. |

## How to run

From this directory (`Chapter 2`):

```bash
cd Code
python Thread_determine.py
python MyThreadClass.py
python Semaphore.py
```

Run any script the same way. Some demos use **logging** to stdout; others use **plain prints**.

## Concepts covered

- **`threading.Thread`**: `start`, `join`, `name`, `currentThread()`.
- **Locks**: `Lock` vs `RLock` for mutual exclusion.
- **Signaling**: `Semaphore`, `Event`, `Condition`, `Barrier`.
- **Queues**: thread-safe `queue.Queue` for passing work between threads.

## Requirements

- Python 3.x  
- Standard library (`threading`, `queue`, `logging`, etc.)

---

*PDC-SP26-SE — Saad Hussain 23FA-051-SE*
