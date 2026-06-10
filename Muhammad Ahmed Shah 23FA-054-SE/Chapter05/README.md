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
This chapter explores concurrency using:
- `asyncio` (cooperative multitasking)
- `concurrent.futures` (thread/process-based parallelism)

It demonstrates:
- Coroutine execution model
- Event loop scheduling
- Futures and callbacks
- Thread vs Process execution comparison

---

## Files (Detailed)
- `asyncio_coroutine.py` — Modern coroutine state machine using `async/await`
- `asyncio_event_loop.py` — Event loop with delayed callbacks (`call_later`)
- `asyncio_task_manipulation.py` — Concurrent execution of tasks (factorial, fibonacci, binomial)
- `asyncio_and_futures.py` — Future object handling with async completion
- `concurrent_futures_pooling.py` — Comparison of sequential, thread pool, and process pool execution

---

## Modernization Notes
- Replaced `@asyncio.coroutine` and `yield from` with `async def` and `await`
- Replaced `get_event_loop()` with `asyncio.run()`
- Improved readability and performance
- Compatible with Python 3.7+

---

## Quick Run Examples
```bash
python Chap-5/Files/asyncio_task_manipulation.py
python Chap-5/Files/concurrent_futures_pooling.py
