# Chapter 5 - Asynchronous Programming in Python

Course materials for **Parallel and Distributed Computing (PDC)**. This chapter focuses on asynchronous execution using `asyncio` and task pooling with `concurrent.futures`.

Repository path: [PDC-SP26-SE / Saad Hussain 23FA-051-SE / Chapter 5](https://github.com/saadh472/PDC-SP26-SE/tree/main/Saad%20Hussain%2023FA-051-SE/Chapter%205).

## Folder structure

| Folder | Purpose |
|--------|---------|
| [`Code`](Code) | Python source files for Chapter 5 asynchronous programming examples. |
| [`Output Screenshot`](<Output Screenshot>) | Output screenshots for the matching Python examples. |

## What is in this chapter

| File | Description | Output |
|------|-------------|--------|
| [`Code/asyncio_event_loop.py`](Code/asyncio_event_loop.py) | Creates an event loop manually and schedules tasks with `call_soon()` and `call_later()`. | [`Screenshot`](<Output Screenshot/asyncio_event_loop.png>) |
| [`Code/asyncio_coroutine.py`](Code/asyncio_coroutine.py) | Simulates a finite state machine with asynchronous coroutines and `await`. | [`Screenshot`](<Output Screenshot/asyncio_coroutine.png>) |
| [`Code/asyncio_task_manipulation.py`](Code/asyncio_task_manipulation.py) | Runs factorial, Fibonacci, and binomial coefficient computations concurrently with `asyncio.Task`. | [`Screenshot`](<Output Screenshot/asyncio_task_manipulation.png>) |
| [`Code/asyncio_and_futures.py`](Code/asyncio_and_futures.py) | Uses asyncio futures, callbacks, and `asyncio.gather()` to return coroutine results. | [`Screenshot`](<Output Screenshot/asyncio_and_futures.png>) |
| [`Code/concurrent_futures_pooling.py`](Code/concurrent_futures_pooling.py) | Compares sequential execution, thread pooling, and process pooling with `concurrent.futures`. | [`Screenshot`](<Output Screenshot/concurrent_futures_pooling.png>) |

## How to run

From this directory (`Chapter 5`):

```bash
cd Code
python asyncio_event_loop.py
python asyncio_coroutine.py
python asyncio_task_manipulation.py
python concurrent_futures_pooling.py
```

The futures example expects two command-line arguments:

```bash
python asyncio_and_futures.py 10 5
```

On Windows, use `python` or `py` depending on your Python installation.

## Concepts covered

- Creating and controlling an `asyncio` event loop.
- Defining and awaiting coroutines.
- Scheduling concurrent tasks with `asyncio.create_task()`.
- Combining asynchronous work with `asyncio.gather()`.
- Using futures and done callbacks.
- Comparing sequential execution with thread and process pools.

## Requirements

- Python 3.x
- Standard library only (`asyncio`, `concurrent.futures`, `time`, `random`, etc.)

---

*PDC-SP26-SE - Saad Hussain 23FA-051-SE*
