# Chapter 01: Fundamentals of Parallel Computing in Python


##  Course Information
**Course:** Parallel and Distributed Computing (PDC) 
**Student Name:** abdullah  
**Roll No:** 23FA-016-SE

---

##  Overview
This directory presents the foundational concepts and implementations of Parallel and Distributed Computing using Python. The objective of this chapter is to understand how modern computing systems achieve higher performance by executing tasks concurrently instead of sequentially.

The content is divided into two major sections:
- **Conceptual Understanding** of parallel computing principles
- **Practical Implementation** using Python programs

---

##  Contents

### 🔹 Part 1: Conceptual Foundations
- Importance of Parallel and Distributed Computing 
- Evolution from single-core to multi-core systems 
- Difference between:
  - Serial Execution 
  - Concurrency (Multithreading) 
  - Parallelism (Multiprocessing) 
- Memory sharing models:
  - Threads vs Processes 
- Python limitation: **Global Interpreter Lock (GIL)** 
- Performance concepts like overhead and scalability 

---

### 🔹 Part 2: Practical Implementation
This section includes Python scripts that demonstrate different execution models using the same workload.

####  Workload Description
A CPU-intensive function repeatedly generates random values and stores them in a list. This helps analyze performance differences between execution techniques.

---

##  Implementations

### 1️ Serial Execution
- Runs tasks one after another
- Uses a single CPU core
- Acts as a baseline for comparison

**Result:** Predictable but slower performance

---

### 2️ Multithreading
- Uses multiple threads within one process
- Shares memory between threads
- Limited by Python’s GIL for CPU-bound tasks

**Result:** Slight improvement or sometimes slower due to context switching

---

### 3️ Multiprocessing
- Uses multiple independent processes
- Each process runs on a separate CPU core
- Avoids GIL limitations

**Result:** Significant performance improvement

---

##  Key Observations
- Parallel execution improves performance for heavy workloads 
- Multithreading is not efficient for CPU-bound tasks in Python 
- Multiprocessing is the best approach for utilizing multi-core systems 
- Overhead exists when creating threads/processes 

---

##  Additional Files
- `classes.py` → Object-oriented programming basics 
- `lists.py` → List operations 
- `flow.py` → Control flow examples 
- `file.py`, `dir.py` → File and directory handling 
- `do_something.py` → Core workload function 

---
