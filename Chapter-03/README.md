# Chapter 03 – Multiprocessing in Python

## Overview

This chapter introduces **multiprocessing**, a technique that allows multiple processes to run simultaneously using different CPU cores. Unlike threading, multiprocessing can achieve true parallel execution and is especially useful for CPU-intensive tasks.

---

## Objectives

* Understand the concept of processes and multiprocessing
* Learn the difference between threading and multiprocessing
* Implement multiprocessing using Python's `multiprocessing` module
* Analyze performance improvements through parallel execution

---

## Folder Structure

```text
Chapter-03/
│── Code/        # Python multiprocessing programs
│── Output/      # Screenshots of code and execution
│── README.md    # Documentation
```

---

## Key Concepts

| Concept         | Description                                                     |
| --------------- | --------------------------------------------------------------- |
| Process         | An independent program execution unit with its own memory space |
| Multiprocessing | Running multiple processes simultaneously                       |
| CPU Core        | A processing unit capable of executing tasks independently      |
| Parallelism     | Multiple tasks executing at the same time                       |

---

## Visual Analysis (Quick Understanding)

### Single Process Execution

```text
CPU Core
   │
Task1 → Task2 → Task3 → Task4
```

**Result:** Tasks execute one after another, increasing total execution time.

---

### Multiprocessing Execution

```text
Core 1 ── Task1
Core 2 ── Task2
Core 3 ── Task3
Core 4 ── Task4

        ↓

 All Tasks Execute in Parallel
```

**Result:** Tasks run simultaneously across multiple CPU cores, reducing execution time.

---

## Threading vs Multiprocessing

| Feature        | Threading       | Multiprocessing  |
| -------------- | --------------- | ---------------- |
| Execution Unit | Thread          | Process          |
| Memory         | Shared          | Separate         |
| Parallelism    | Limited         | True Parallelism |
| Best For       | I/O-bound Tasks | CPU-bound Tasks  |
| Performance    | Moderate        | High             |

---

## Performance Insight

```text
Execution Time

Sequential Processing      ████████████████ 100%

Multiprocessing            ██████ 40-60%
```

**Observation:** Multiprocessing significantly reduces execution time by utilizing multiple CPU cores.

---

## Implementation Summary

* Created multiple processes using Python's `multiprocessing` module.
* Executed tasks in parallel on separate CPU cores.
* Compared execution time with sequential execution.
* Observed improved performance for CPU-intensive operations.

---

## Output

The **Output/** folder contains:

* Screenshots of multiprocessing code
* Program execution results
* Performance comparison outputs
* Process creation and execution screenshots

---

## Learning Outcome

After completing this chapter, I was able to:

* Understand the architecture of multiprocessing.
* Create and manage multiple processes in Python.
* Differentiate between threading and multiprocessing.
* Identify situations where multiprocessing provides better performance.

---

## Real-World Applications

* Scientific Computing
* Data Analysis
* Machine Learning Training
* Image and Video Processing
* Large-scale Simulations
* High-Performance Computing (HPC)

---

## Conclusion

Multiprocessing is a powerful technique for improving the performance of CPU-intensive applications. By distributing work across multiple CPU cores, programs can execute tasks in parallel, leading to faster execution and better resource utilization. This chapter provides the foundation for building high-performance parallel applications in Python.
