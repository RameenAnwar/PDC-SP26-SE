# Chapter 01: Fundamentals of Parallel Computing in Python

[![Course](https://img.shields.io/badge/Course-Parallel%20%26%20Distributed%20Computing-blue)](#)
[![Language](https://img.shields.io/badge/Language-Python-3776AB)](#)
[![Level](https://img.shields.io/badge/Level-Intermediate-orange)](#)
[![Focus](https://img.shields.io/badge/Focus-Parallel%20Computing-red)](#)
[![Author](https://img.shields.io/badge/Author-Yahya%20Shahzad-green)](#)

---

## Course Information
**Course:** Parallel and Distributed Computing (PDC) 
**Student Name:** Yahya Shahzad 
**Roll No:** 23FA-023-SE 

---

## Overview

This directory presents the foundational concepts and implementations of Parallel and Distributed Computing using Python. The objective of this chapter is to understand how modern computing systems achieve higher performance by executing tasks concurrently instead of sequentially.

The content is divided into two major sections:
- Conceptual understanding of parallel computing principles 
- Practical implementation using Python programs 

---

## Contents

### Part 1: Conceptual Foundations

This section explains the core ideas required to understand parallel computing systems.

- Importance of Parallel and Distributed Computing 
- Evolution from single-core to multi-core systems 
- Difference between:
  - Serial Execution 
  - Concurrency (Multithreading) 
  - Parallelism (Multiprocessing) 
- Memory sharing models:
  - Threads vs Processes 
- Python limitation: Global Interpreter Lock (GIL) 
- Performance concepts like overhead and scalability 

---

### Part 2: Practical Implementation

This section includes Python scripts that demonstrate different execution models using the same workload.

#### Workload Description
A CPU-intensive function repeatedly generates random values and stores them in a list. This helps analyze performance differences between execution techniques.

---

## Implementations

### Serial Execution
File: `serial_execution.py`

- Runs tasks one after another  
- Uses a single CPU core  
- Acts as a baseline for comparison  

Result: Predictable but slower performance  

---

### Multithreading
File: `multithreading.py`

- Uses multiple threads within one process  
- Shares memory between threads  
- Limited by Python’s GIL for CPU-bound tasks  

Result: Slight improvement or sometimes slower due to context switching  

---

### Multiprocessing
File: `multiprocessing.py`

- Uses multiple independent processes  
- Each process runs on a separate CPU core  
- Avoids GIL limitations  

Result: Significant performance improvement  

---

## Key Observations

- Parallel execution improves performance for heavy workloads  
- Multithreading is not efficient for CPU-bound tasks in Python  
- Multiprocessing is the best approach for utilizing multi-core systems  
- Overhead exists when creating threads/processes  

---

## Additional Files

- [`classes.py`](./classes.py) → Object-oriented programming basics  
- [`lists.py`](./lists.py) → List operations  
- [`flow.py`](./flow.py) → Control flow examples  
- [`file.py`](./file.py) → File handling  
- [`dir.py`](./dir.py) → Directory handling  
- [`do_something.py`](./do_something.py) → Core workload function  
