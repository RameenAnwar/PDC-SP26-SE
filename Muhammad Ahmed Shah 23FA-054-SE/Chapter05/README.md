# Chapter 05 — Async Programming & Futures
[![Course](https://img.shields.io/badge/Course-Parallel%20%26%20Distributed%20Computing-blue)](#)
[![Language](https://img.shields.io/badge/Language-Python-3776AB)](#)
[![Level](https://img.shields.io/badge/Level-Intermediate-orange)](#)
[![Focus](https://img.shields.io/badge/Focus-Parallel%20Computing-red)](#)
[![Author](https://img.shields.io/badge/Author-M.%20Ahmed%20Shah-green)](#)

---

## Course Information
**Course:** Parallel and Distributed Computing (PDC)  
**Student Name:** M. Ahmed Shah  
**Roll No:** 23FA-054-SE  

---

## Overview
This chapter explains Python concurrency using:
- `asyncio` (cooperative multitasking via event loop)
- `concurrent.futures` (parallel execution using threads/processes)

It covers:
- Coroutines
- Event Loop scheduling
- Futures
- Callbacks
- Thread vs Process execution

---

## Files Overview
- `asyncio_coroutine.py` → async/await based coroutine flow
- `asyncio_event_loop.py` → event loop + delayed callbacks
- `asyncio_task_manipulation.py` → concurrent task execution
- `asyncio_and_futures.py` → Future object handling
- `concurrent_futures_pooling.py` → performance comparison

---

## Modernization Notes
- `yield from` replaced with `await`
- `@asyncio.coroutine` removed
- `asyncio.run()` used instead of manual event loop
- Fully compatible with Python 3.7+

---

## Architecture Diagram

```mermaid
flowchart LR

    Loop[Event Loop]

    TaskA[Coroutine Task A]
    TaskB[Coroutine Task B]
    Callback[call_later Callback]

    Executors[Executors]
    ThreadPool[ThreadPoolExecutor]
    ProcessPool[ProcessPoolExecutor]

    Loop --> TaskA
    Loop --> TaskB
    Loop --> Callback
    Loop --> Executors

    Executors --> ThreadPool
    Executors --> ProcessPool

    classDef loop fill:#1e3a8a,stroke:#0f172a,color:#ffffff;
    classDef task fill:#0f766e,stroke:#064e3b,color:#ffffff;
    classDef callback fill:#f97316,stroke:#9a3412,color:#ffffff;
    classDef executor fill:#7c3aed,stroke:#4c1d95,color:#ffffff;

    class Loop loop;
    class TaskA,TaskB task;
    class Callback callback;
    class Executors,ThreadPool,ProcessPool executor;
