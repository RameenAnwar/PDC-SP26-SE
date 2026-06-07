# Chapter 02 – Threading and Concurrency in Python

## Overview

This chapter focuses on **threading and concurrency**, allowing multiple tasks to run seemingly at the same time within a single process. It highlights how threads improve responsiveness and performance, especially for I/O-bound tasks.

---

## Objectives

* Understand the concept of threads
* Learn how concurrency works in Python
* Implement multithreading using built-in libraries
* Compare threading with sequential execution

---

## Folder Structure

```
Chapter-02/
│── Code/        # Python threading programs
│── Output/      # Screenshots of code and execution
│── README.md    # Documentation
```

---

## Key Concepts

| Concept        | Description                                     |
| -------------- | ----------------------------------------------- |
| Thread         | Smallest unit of execution within a process     |
| Concurrency    | Multiple tasks progressing at the same time     |
| Multithreading | Running multiple threads in one program         |
| I/O-bound Task | Tasks waiting for input/output (files, network) |

---

## Visual Analysis (Quick Understanding)

### Thread Execution Flow

```
Main Program
     │
 ┌───┼───────────────┐
 │   │               │
Thread-1        Thread-2        Thread-3
 │                │               │
 └──────→ Running Concurrently ←──┘
```

---

### Sequential vs Threading

```
Sequential:
Task1 → Task2 → Task3 → Task4  (Slow)

Threading:
Task1 ┐
Task2 ├──→ Concurrent Execution → Faster
Task3 ┤
Task4 ┘
```

---

## Performance Insight

| Execution Type | Speed  | CPU Usage | Best For        |
| -------------- | ------ | --------- | --------------- |
| Sequential     | Slow   | Low       | Simple tasks    |
| Threading      | Faster | Moderate  | I/O-bound tasks |

---

## Implementation Summary

* Created multiple threads using Python threading module
* Executed tasks concurrently
* Observed improved responsiveness compared to sequential execution
* Learned thread creation, start, and join operations

---

## Output

All results are stored in the **Output/** folder:

* Thread execution screenshots
* Code implementation results
* Observations of concurrent behavior

---

## Learning Outcome

* Strong understanding of threading and concurrency
* Ability to implement multithreaded programs
* Knowledge of when to use threading effectively

---

## Conclusion

Threading allows efficient execution of multiple tasks within a single program. It is especially useful for I/O-bound operations and improves performance by utilizing waiting time effectively.
