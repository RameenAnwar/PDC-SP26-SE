# Chapter01 - Python Parallel Programming
# Chapter 01 — Getting Started with Parallel Programming 🚀

## 📌 Overview
This chapter introduces the fundamentals of parallel programming using Python.  
Parallel programming enables multiple tasks to execute simultaneously, improving
program performance, responsiveness, and efficient CPU utilization.

The examples in this chapter demonstrate how to create threads and processes,
manage shared resources, and handle common concurrency issues.

---

## 🎯 Learning Objectives
After completing this chapter, you will be able to:

- Understand the concept of parallel programming
- Differentiate between concurrency and parallelism
- Create and manage threads in Python
- Implement multiprocessing for CPU-bound tasks
- Use synchronization techniques for shared resources
- Prevent race conditions and deadlocks
- Understand Python Global Interpreter Lock (GIL)
- Optimize performance using parallel execution

---

## 📚 Topics Covered
This chapter includes the following topics:

1. Introduction to Parallel Computing  
2. Concurrency vs Parallelism  
3. Threads vs Processes  
4. Python Threading Module  
5. Python Multiprocessing Module  
6. Synchronization Techniques  
7. Locks and Semaphores  
8. Thread Communication using Queue  
9. Race Conditions and Deadlocks  
10. Global Interpreter Lock (GIL)  
11. Performance Optimization  

---

## 🛠️ Requirements
Make sure the following are installed before running the programs:

- Python 3.x  
- threading module (built-in)  
- multiprocessing module (built-in)  
- queue module (built-in)  

No external libraries are required.

---

## 📂 Project Structure


Chapter01/
│
├── README.md
├── thread_definition.py
├── thread_determination.py
├── threading_with_queue.py
├── multiprocessing_example.py
└── synchronization_example.py


### File Description

| File Name | Description |
|-----------|-------------|
| thread_definition.py | Basic thread creation example |
| thread_determination.py | Thread execution demonstration |
| threading_with_queue.py | Thread communication using queue |
| multiprocessing_example.py | Process-based parallel execution |
| synchronization_example.py | Synchronization using locks |

---

## ▶️ How to Run

Navigate to Chapter01 directory:
```bash
cd Chapter01

Run thread example:

python thread_definition.py

Run multiprocessing example:

python multiprocessing_example.py

Run synchronization example:

python synchronization_example.py
📖 Key Concepts
🔹 Parallel Programming

Parallel programming allows multiple computations to run at the same time,
reducing execution time and improving performance.

🔹 Concurrency vs Parallelism
Concurrency	Parallelism
Tasks overlap in time	Tasks run at same time
Single CPU possible	Multiple CPU cores required
Improves responsiveness	Improves performance
🔹 Threads vs Processes
Feature	Threads	Processes
Memory	Shared	Separate
Speed	Faster	Slower
Communication	Easy	Complex
Safety	Less Safe	More Safe
Overhead	Low	High
🔹 Global Interpreter Lock (GIL)

The Global Interpreter Lock (GIL) is a mutex that ensures only one thread
executes Python bytecode at a time. It affects CPU-bound multithreading
but does not impact multiprocessing.

🔹 Synchronization

Synchronization controls access to shared resources to prevent conflicts
between multiple threads or processes.

Common synchronization tools:

Lock
RLock
Semaphore
Queue
Event
⚠️ Common Problems in Parallel Programming
Race Condition

Occurs when multiple threads access shared data simultaneously and modify it.

Deadlock

Occurs when two or more threads wait indefinitely for each other to release resources.

Starvation

Occurs when a thread never gets CPU time due to priority issues.

Livelock

Threads keep responding to each other but never make progress.

🚀 Performance Tips
Use threading for I/O bound tasks
Use multiprocessing for CPU bound tasks
Avoid unnecessary shared variables
Use queues for safe communication
Always release locks properly
📝 Summary

This chapter provided a strong foundation in parallel programming using Python.
We explored threads, processes, synchronization techniques, and communication
mechanisms. We also learned how to avoid common concurrency issues such as
race conditions and deadlocks.

These concepts are essential for building high-performance and scalable
parallel applications.

🔗 References

Teacher Repository
https://github.com/PacktPublishing/Python-Parallel-Programming-Cookbook-Second-Edition

Student Repository
https://github.com/23fa-021-se-lgtm/PDC-SP26-SE

Python Documentation
https://docs.python.org/3/library/threading.html

https://docs.python.org/3/library/multiprocessing.html

👨‍💻 Author

Student: 23FA-048-SE
Course: Parallel and Distributed Computing (PDC)
Semester: Spring 2026
Chapter: 01 - Getting Started with Parallel Programming
