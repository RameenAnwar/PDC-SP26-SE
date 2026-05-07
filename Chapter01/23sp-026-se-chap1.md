# Python Scripts Documentation

## FILE 1 — classes.py

### What Does It Do
Demonstrates Object-Oriented Programming (OOP) using MyClass and AnotherClass.

### How To Run
python classes.py

### Key Concepts
- Class vs instance variables
- Inheritance
- Variable shadowing
- Dynamic attributes

### Pros
- Clear OOP example
- Shows common pitfalls
- Beginner-friendly

### Cons
- No user input
- No error handling
- No constructor arguments

---

## FILE 2 — dir.py

### What Does It Do
Checks number type and sums a list.

### How To Run
python dir.py

### Concepts Demonstrated
Conditional logic (if / elif / else)
Looping through list elements
Accumulator/sum pattern

### Pros
Extremely easy to understand
Shows foundational control flow structures
Simple to modify inputs

### Cons
All data is hardcoded
No interactive input
No functions; the code executes at module level
---

## FILE 3 — dosomething.py

### What Does It Do
Generates random numbers into a list.

### Concepts Demonstrated
Creating reusable helper functions
Using Python’s random module
Appending values to lists in loops
Mutating lists passed by reference

### Pros
Clean and modular design
Works seamlessly across multiple test files
Easy-to-read logic

### Cons
Modifies lists in place instead of returning data
No validation for incorrect values (e.g., negative count)
Only generates floats; no type flexibility

---

## FILE 4 — flie.py

### What Does It Do
Demonstrates file read/write.

### How To Run
python flie.py

### Concepts Demonstrated
Writing to a file using open(..., "w")
Writing text with f.write()
Closing files manually
Reading entire file content using f.read()

### Pros
Simple demonstration of both writing and reading
Easy starting point for file-handling exercises
Clear and minimal code

### Cons
File name is fixed
No error handling
Uses outdated manual open/close instead of with open()
Filename contains a typo (“flie”)

---

## FILE 5 — flow.py

### What Does It Do
Shows if, for, and while usage.

### How To Run
python flow.py

### Concepts Demonstrated
Conditional branching
List iteration with a for loop
Using while loops with counters
Accumulator technique

### Pros
Combines several fundamental constructs into one file
Easy to understand and well-commented
Useful reference for beginners

### Cons
Hardcoded values
No functions; everything runs directly
No user prompts

## FILE 6 — lists.py

### What Does It Do
This script showcases Python’s main built-in data structures:

Lists
Dictionaries
Tuples

It also illustrates indexing, modification, and basic built-in functions.

### How To Run
python lists.py

### Concepts Demonstrated
Creating and updating lists
Using negative indexing
Working with dictionaries
Understanding tuple immutability
Storing built-in functions inside variables

### Pros
Demonstrates three essential data structures at once
Highlights Python-specific features like negative indexing
Shows that functions are first-class objects

### Cons
No user interaction
Some expressions are evaluated but not printed
No exception handling

---

## FILE 7 — multiprocessingtest.py

### What Does It Do
This file runs a performance test using Python’s multiprocessing module. It launches 10 separate processes, each generating 10 million random values, and measures the total execution time.
### How To Run
python multiprocessingtest.py

### Concepts Demonstrated
Creating processes using multiprocessing.Process
True parallelism across CPU cores
Measuring performance with time.time()
Proper use of the if __name__ == "__main__" block

### Pros
Achieves genuine parallel execution
Avoids GIL limitations
Ideal for CPU-demanding workloads

### Cons
Each process has its own memory (no shared out_list)
Higher startup overhead than threads
Generated data is discarded after each process finishes
---

## FILE 8 — multithreadingtest.py

### What Does It Do
This program measures how Python threads perform when generating large sets of random numbers. It creates 10 threads and records how long the task takes.

### How To Run
python multithreadingtest.py

### Concepts Demonstrated
Thread creation with threading.Thread
Shared memory model of threads
Execution time measurement
Safe entry using if __name__ == "__main__"

### Pros
Threads share memory, simplifying data handling
Lower overhead than processes
Good for I/O-bound tasks

### Cons
Python's GIL restricts parallel CPU execution
Contains a logic bug (function is executed immediately instead of passed as target)
Often slower than multiprocessing for CPU-heavy tasks
---

## FILE 9 — serialtest.py

### What Does It Do
This script runs the do_something function 10 times consecutively. Each iteration generates 10 million random numbers. It measures how long the full serial run takes..

### How To Run
python serialtest.py

### Concepts Demonstrated
Serial execution
Benchmarking with the time module
Loop-based repetition
Importing from external modules

### Pros
Predictable and easy-to-follow execution
Very easy to debug
Useful baseline for comparing concurrency models

### Cons
Slowest method for large workloads
No parallelism whatsoever
Not optimized for performance
---

## FILE 10 — threadandprocesses.py

### What Does It Do
This script compares the performance of threading and multiprocessing in one place. It runs do_something using 10 threads, then repeats the task with 10 processes. A serialized version is included but commented out.

### How To Run
python threadandprocesses.py

### Key Concepts
Direct comparison of threading vs multiprocessing
Shared vs isolated memory models
Timing execution for both methods
Scaling via a NUM_WORKERS constant

### Pros
Combines all concurrency models in one script
Easy to compare performance results side-by-side
Good learning tool for understanding when to choose each model

### Cons
Inherits same threading bug as multithreadingtest.py
Serial section disabled by default
out_list reused across runs, which can mix output
