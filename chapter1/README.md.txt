Chapter # 1
1. dir.py
What I learned:
I learned basic of if else and list and for loop

How to execute:
Run in cmd : Python dir.py to see how python differentiate between +ve, -ve and zero and also to see the sum of the lists.

Use cases:
Basic data validation and simple mathematical transformations of list-based data sets.

Requirements for execution:
A standard Python installation, no external modules or libraries are necessary.

Advantages:
Extremely lightweight and fast; it demonstrates the core foundation of almost every functional Python script.

Disadvantages:
The logic is static; if you want to check different numbers, you must manually edit the script or use input.

2. lists.py
What I learned:
I learned the differences between mutable lists, unchangeable tuples, and key-value pairs in dictionaries.

How to execute:
Run in cmd: python lists.py to see how to access and modify items in a list and how to update values in a dictionary.

Use cases:
Storing collections of data, mapping unique keys to values (like a dictionary), and grouping related items together.

Requirements for execution:
Standard Python installation; utilizes built-in data structures without needing imports.

Advantages:
Highly flexible; lists can hold different data types at once, and dictionaries offer extremely fast data retrieval.

Disadvantages:
Tuples cannot be modified after creation, which can be restrictive if the data needs to change.

3. do_something.py
What I learned:
I learned how to create a reusable helper function that utilizes the random module to populate a list with decimal numbers.

How to execute:
This file is a module; it is executed by being imported into other scripts like serial_test.py or multiprocessing_test.py using **from do_something import ***.

Use cases:
Generating large datasets for performance testing, simulations, or any task requiring a high volume of random data.

Requirements for execution:
The Python random module (built-in) and another script to call the function.

Advantages:
Follows the "Don't Repeat Yourself" (DRY) principle by keeping specific logic in a single, manageable file.

Disadvantages:
It does not perform any action when run by itself; it strictly acts as a dependency for other programs.

4. flow.py
What I learned:
I learned three core control flow tools: if/elif/else for logic, for loops for lists, and while loops for conditional repetition.

How to execute:
Run in cmd: python flow.py to see the results of logical checks and two different ways to calculate numerical sums.

Use cases:
Automation scripts, data filtering, and creating loops that run until a specific goal or condition is reached.

Requirements for execution:
Proper indentation of code blocks, which is required for Python to identify the scope of loops and conditions.

Advantages:
Comprehensive; it covers all the primary ways to control the "flow" or direction of a program's execution.

Disadvantages:
while loops can cause the program to hang in an "infinite loop" if the counter variable is not updated correctly.

5. classes.py
What I learned:
I learned how to create classes, use the __init__ constructor, and the difference between shared class variables and instance-specific variables.

How to execute:
Run in cmd: python classes.py to see how modifying a class-level variable affects all objects, while instance variables remain unique to each one.

Use cases:
Building structured applications like student databases, banking systems, or any program that models real-world objects through inheritance.

Requirements for execution:
A standard Python installation and an understanding of the self argument used within class methods.

Advantages:
Promotes code reusability and organization; inheritance allows a new class to take on the properties of an existing one.

Disadvantages:
Can become complex and harder to debug as the hierarchy of inherited classes grows deeper.

6. file.py
What I learned:
I learned the basics of file I/O, specifically how to open, write text to, close, and read back from a .txt file.

How to execute:
Run in cmd: python file.py to generate a file named test.txt and see its contents printed to the console.

Use cases:
Saving user logs, storing configuration settings, or exporting reports and data for later use.

Requirements for execution:
Standard file system write permissions and the built-in open() function.

Advantages:
Provides data persistence, meaning your data is saved on the hard drive even after the program is closed.

Disadvantages:
Using the 'w' mode overwrites the file every time the script runs, which can lead to accidental data loss.

7. serial_test.py
What I learned:
I learned how to measure the execution time of a task when it is performed sequentially (one after the other).

How to execute:
Run in cmd: python serial_test.py to execute the random number task 10 times in a single sequence.

Use cases:
Baseline performance testing or simple scripts where tasks must be completed in a specific, linear order.

Requirements for execution:
The time module for benchmarking and the do_something.py file located in the same folder.

Advantages:
The logic is straightforward and easy to debug because only one thing happens at a time.

Disadvantages:
Very slow for heavy workloads as it only uses one CPU core, leaving the rest of the processor's power idle.

8. multiprocessing_test.py
What I learned:
I learned how to use the multiprocessing module to run tasks on separate CPU cores for true parallelism.

How to execute:
Run in cmd: python multiprocessing_test.py to see the performance difference when the CPU handles 10 tasks at once on 10 cores.

Use cases:
CPU-intensive tasks like image processing, heavy data analysis, or complex mathematical simulations.

Requirements for execution:
The if __name__ == "__main__": block to safely manage process creation on different operating systems.

Advantages:
Bypasses the GIL, allowing the program to run significantly faster by using all available CPU power.

Disadvantages:
Higher memory (RAM) usage because each process creates its own independent memory space.

9. multithreading_test.py
What I learned:
I learned how to use the threading module to attempt running multiple tasks simultaneously within the same memory space.

How to execute:
Run in cmd: python multithreading_test.py to see 10 threads start and process data at the same time.

Use cases:
Tasks involving waiting (I/O bound), such as downloading multiple files, web scraping, or keeping a user interface responsive.

Requirements for execution:
The threading library and the use of .start() and .join() to manage the thread lifecycle.

Advantages:
Threads are "lightweight" and share memory, making them efficient for tasks that don't require heavy CPU calculation.

Disadvantages:
Due to Python's Global Interpreter Lock (GIL), it does not provide true parallelism for CPU-heavy math tasks.

10. thread_and_processes.py
What I learned:
I learned how to compare the performance of threading and multiprocessing side-by-side within a single script.

How to execute:
Run in cmd: python thread_and_processes.py to see a direct time comparison between the two different concurrency methods.

Use cases:
Performance benchmarking and determining which execution method is best for a specific type of workload.

Requirements for execution:
Importing both threading and multiprocessing modules and sufficient system resources to handle the heavy load.

Advantages:
Provides a clear, empirical view of how different system architectures (threads vs processes) handle the same data.

Disadvantages:
The script is resource-heavy because it runs a massive workload twice (once for each method).

