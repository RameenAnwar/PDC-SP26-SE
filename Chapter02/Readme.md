# Chapter02 - Python Parallel Programming

\# Python Threading and Synchronization – Chapter 02



\## Overview



This repository contains a collection of Python programs that demonstrate the fundamentals of \*\*multithreading\*\*, \*\*thread synchronization\*\*, and \*\*concurrency control\*\* using Python’s built-in `threading` module.



The project is designed for:



\* Students learning Operating Systems and Concurrent Programming

\* Beginners exploring Python multithreading

\* University lab work and assignments

\* Practical understanding of synchronization mechanisms

\* Developers interested in thread communication and resource sharing



Each file demonstrates a different synchronization primitive or threading concept such as:



\* Thread Creation

\* Thread Naming

\* Thread Joining

\* Locks (`Lock`)

\* Reentrant Locks (`RLock`)

\* Semaphores

\* Events

\* Conditions

\* Barriers

\* Queues

\* Producer–Consumer Problems



\---



\# Technologies Used



\* \*\*Programming Language:\*\* Python 3

\* \*\*Core Library:\*\* `threading`

\* \*\*Additional Modules:\*\*



&#x20; \* `queue`

&#x20; \* `time`

&#x20; \* `random`

&#x20; \* `logging`

&#x20; \* `os`



\---



\# Project Structure



```bash

Chapter02/

│

├── Barrier.py

├── Condition.py

├── Event.py

├── MyThreadClass.py

├── MyThreadClass\_lock.py

├── MyThreadClass\_lock\_2.py

├── Rlock.py

├── Semaphore.py

├── Thread\_definition.py

├── Thread\_determine.py

├── Thread\_name\_and\_processes.py

├── Threading\_with\_queue.py

└── README.md

```



\---



\# Concepts Covered



| Concept                   | Description                             |

| ------------------------- | --------------------------------------- |

| Multithreading            | Running multiple threads simultaneously |

| Synchronization           | Controlling thread execution order      |

| Race Condition Prevention | Protecting shared resources             |

| Producer-Consumer Problem | Communication between threads           |

| Locking Mechanisms        | Preventing concurrent access conflicts  |

| Queue-Based Communication | Safe data exchange between threads      |

| Thread Coordination       | Synchronizing multiple threads          |



\---



\# File Explanations



\## 1. Thread\_definition.py



\### Purpose



Demonstrates the most basic way of creating and executing threads in Python.



\### Key Features



\* Uses `threading.Thread`

\* Passes arguments to threads

\* Starts and joins threads



\### Working



A simple function `my\_func()` is executed by multiple threads.

Each thread prints its thread number.



\### Important Concepts



\* Thread creation

\* Thread execution

\* Thread joining



\### Example Output



```bash

my\_func called by thread N°0

my\_func called by thread N°1

...

```



\---



\## 2. Thread\_determine.py



\### Purpose



Shows how to create threads with custom names and determine currently running threads.



\### Key Features



\* Uses `currentThread()`

\* Displays thread names

\* Simulates concurrent execution using `sleep()`



\### Working



Three functions run simultaneously:



\* function\_A

\* function\_B

\* function\_C



Each thread prints:



\* starting state

\* exiting state



\### Important Concepts



\* Thread naming

\* Concurrent execution

\* Thread lifecycle



\---



\## 3. Thread\_name\_and\_processes.py



\### Purpose



Demonstrates thread naming and thread execution inside a process.



\### Key Features



\* Custom thread class

\* Inheritance from `Thread`

\* Thread identification



\### Working



Two custom thread objects are created and executed.

Each thread prints its thread name.



\### Important Concepts



\* Thread subclassing

\* Object-oriented threading

\* Process and thread relation



\---



\## 4. MyThreadClass.py



\### Purpose



Demonstrates advanced thread creation using a custom thread class.



\### Key Features



\* Thread inheritance

\* Random execution duration

\* Parallel execution

\* Execution time calculation



\### Working



Nine threads are created.

Each thread:



1\. Starts execution

2\. Sleeps for random duration

3\. Finishes execution



The total execution time is displayed.



\### Important Concepts



\* Parallel execution

\* Thread scheduling

\* Performance measurement

\* Concurrent processing



\### Example Topics Learned



\* Why threads improve responsiveness

\* Difference between sequential and concurrent execution



\---



\## 5. MyThreadClass\_lock.py



\### Purpose



Demonstrates synchronization using a standard `Lock`.



\### Key Features



\* Shared lock object

\* Critical section protection

\* Sequential access to shared resource



\### Working



Each thread acquires the lock before execution.

Only one thread can execute the critical section at a time.



\### Important Concepts



\* Mutual exclusion

\* Critical sections

\* Lock acquisition and release

\* Race condition prevention



\### Synchronization Flow



```text

Thread acquires lock

&#x20;     ↓

Critical section executes

&#x20;     ↓

Thread releases lock

```



\---



\## 6. MyThreadClass\_lock\_2.py



\### Purpose



Demonstrates partial locking and reduced critical section size.



\### Key Features



\* Lock acquired only for protected operations

\* Non-critical work executed outside lock



\### Working



The lock protects only the printing operation.

The sleeping operation happens outside the lock.



\### Important Concepts



\* Optimized synchronization

\* Reduced lock contention

\* Improved concurrency



\### Educational Value



Shows why locks should protect only critical code instead of entire execution.



\---



\## 7. Semaphore.py



\### Purpose



Demonstrates thread synchronization using a `Semaphore`.



\### Key Features



\* Producer-consumer communication

\* Semaphore signaling

\* Thread blocking and waking



\### Working



\* Consumer waits for data

\* Producer generates random item

\* Producer releases semaphore

\* Consumer resumes execution



\### Important Concepts



\* Semaphores

\* Resource signaling

\* Inter-thread communication

\* Synchronization primitives



\### Example Flow



```text

Consumer waits

&#x20;     ↓

Producer creates item

&#x20;     ↓

Semaphore released

&#x20;     ↓

Consumer consumes item

```



\---



\## 8. Event.py



\### Purpose



Demonstrates synchronization using `threading.Event`.



\### Key Features



\* Event signaling

\* Producer-consumer model

\* Event wait mechanism



\### Working



\* Producer generates random items

\* Event is triggered using `set()`

\* Consumer waits using `wait()`

\* Consumer processes item after notification



\### Important Concepts



\* Event-based synchronization

\* Thread notification

\* Blocking threads until event occurs



\### Functions Used



| Function        | Purpose                          |

| --------------- | -------------------------------- |

| `event.wait()`  | Blocks thread until event occurs |

| `event.set()`   | Signals event                    |

| `event.clear()` | Resets event                     |



\---



\## 9. Condition.py



\### Purpose



Demonstrates synchronization using `Condition` variables.



\### Key Features



\* Producer-consumer implementation

\* Shared resource management

\* Wait and notify operations



\### Working



\* Producer adds items

\* Consumer removes items

\* Producer waits if list becomes full

\* Consumer waits if list becomes empty



\### Important Concepts



\* Condition variables

\* Wait-notify mechanism

\* Shared buffer management

\* Thread coordination



\### Condition Operations



| Method               | Purpose                 |

| -------------------- | ----------------------- |

| `condition.wait()`   | Pauses thread           |

| `condition.notify()` | Wakes waiting thread    |

| `with condition`     | Acquires condition lock |



\---



\## 10. Barrier.py



\### Purpose



Demonstrates synchronization using a `Barrier`.



\### Key Features



\* Multiple thread coordination

\* Synchronization checkpoint

\* Thread waiting mechanism



\### Working



Three runners reach a finish line.

Each thread waits at the barrier until all threads arrive.



\### Important Concepts



\* Barrier synchronization

\* Coordinated thread execution

\* Group thread synchronization



\### Real-World Analogy



A race cannot continue until all runners reach the checkpoint.



\---



\## 11. Rlock.py



\### Purpose



Demonstrates usage of `RLock` (Reentrant Lock).



\### Key Features



\* Nested locking support

\* Recursive locking

\* Shared resource modification



\### Working



A `Box` object manages item count.

Threads:



\* add items

\* remove items



The same thread can acquire the lock multiple times safely.



\### Important Concepts



\* Reentrant locks

\* Nested synchronization

\* Deadlock prevention



\### Difference Between Lock and RLock



| Lock                                             | RLock                                  |

| ------------------------------------------------ | -------------------------------------- |

| Cannot be acquired multiple times by same thread | Same thread can acquire multiple times |

| Simpler                                          | More flexible                          |

| May cause deadlock in nested locking             | Prevents self-deadlock                 |



\---



\## 12. Threading\_with\_queue.py



\### Purpose



Demonstrates thread-safe communication using `Queue`.



\### Key Features



\* Producer-consumer architecture

\* Automatic synchronization

\* Multi-consumer handling



\### Working



\* Producer generates random items

\* Items stored in queue

\* Multiple consumers process queue items



\### Important Concepts



\* Queue synchronization

\* Thread-safe data structures

\* Task distribution

\* Parallel consumption



\### Queue Advantages



\* Built-in synchronization

\* Safe data sharing

\* No manual locking required



\---



\# Synchronization Mechanisms Summary



| Mechanism | Purpose                         |

| --------- | ------------------------------- |

| Lock      | Protect critical section        |

| RLock     | Reentrant locking               |

| Semaphore | Resource counting and signaling |

| Event     | Thread notification             |

| Condition | Wait-notify synchronization     |

| Barrier   | Synchronize multiple threads    |

| Queue     | Thread-safe communication       |



\---



\# How to Run the Programs



\## Step 1 – Install Python



Download and install Python 3:



```bash

https://www.python.org/downloads/

```



\---



\## Step 2 – Clone Repository



```bash

git clone <repository-url>

```



\---



\## Step 3 – Navigate to Project Folder



```bash

cd Chapter02

```



\---



\## Step 4 – Run Any File



Example:



```bash

python Barrier.py

```



or



```bash

python Semaphore.py

```



\---



\# Learning Outcomes



After completing this project, students will understand:



\* How threads work in Python

\* How concurrency improves execution

\* Synchronization techniques

\* Race condition prevention

\* Thread communication models

\* Producer-consumer implementation

\* Queue-based synchronization

\* Locking mechanisms

\* Barrier and semaphore operations



\---



\# Real-World Applications



These concepts are used in:



\* Operating Systems

\* Web Servers

\* Banking Systems

\* Real-Time Systems

\* Multiplayer Games

\* Chat Applications

\* Task Scheduling Systems

\* Distributed Systems

\* Data Processing Pipelines

\* Background Services



\---



\# Advantages of Multithreading



\* Better CPU utilization

\* Faster execution

\* Improved responsiveness

\* Parallel task processing

\* Efficient resource usage



\---



\# Challenges in Multithreading



\* Race conditions

\* Deadlocks

\* Starvation

\* Synchronization complexity

\* Shared resource conflicts



\---



\# Best Practices



\* Keep critical sections small

\* Avoid unnecessary locking

\* Use queues for communication

\* Release locks properly

\* Avoid nested locks unless required

\* Prefer thread-safe structures



\---



\# Educational Importance



This project is highly suitable for:



\* University lab tasks

\* Final Year Project preparation

\* Operating Systems courses

\* Parallel Computing subjects

\* Python concurrency learning

\* Interview preparation



\---



\# Future Improvements



Possible enhancements include:



\* Thread pools

\* Async programming examples

\* Deadlock detection

\* Multiprocessing examples

\* GUI-based threading demos

\* Real-time monitoring dashboard

\* Logging improvements

\* Performance benchmarking



\---



\# Conclusion



This project provides a complete practical introduction to Python multithreading and synchronization mechanisms. It demonstrates how multiple threads interact, communicate, and safely share resources using different synchronization tools provided by Python.



The repository is ideal for students, beginners, and developers who want hands-on experience with concurrent programming concepts.



\---



\# Author



Developed for educational and learning purposes in Python concurrency and synchronization.



\---



\# License



This project is open-source and free to use for educational purposes.


