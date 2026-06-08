#  Python Multiprocessing – Complete README (Chapter 3)

> A comprehensive guide covering how Python runs multiple processes at the same time — with pipes, queues, and process management.

##  Table of Contents

1. [Introduction](#1-introduction)
2. [Spawning Processes](#2-spawning-processes)
3. [Naming Processes](#3-naming-processes)
4. [Worker Functions (myFunc)](#4-worker-functions-myfunc)
5. [Pipes – Two-Way Communication](#5-pipes--two-way-communication)
6. [Queues – Multi-Way Communication](#6-queues--multi-way-communication)
7. [Killing Processes](#7-killing-processes)
8. [Quick Reference](#8-quick-reference)
9. [Conclusion](#9-conclusion)

---

## 1. Introduction

Normally, a Python program runs one thing at a time — step 1, then step 2, then step 3. But sometimes you want your program to do multiple things at the same time, using all the power of your computer's CPU cores. That is where multiprocessing comes in.

Python has a built-in module called `multiprocessing` that lets you run multiple tasks in separate processes at the same time. Each task runs in its own process.

### When is multiprocessing actually useful?

- You need to process 10,000 images and want to use all CPU cores
- You are doing heavy mathematical calculations
- You want to process a huge file in chunks
- Your program is CPU-bound and needs true parallel execution

### How is multiprocessing different from threading?

| Aspect | Threading | Multiprocessing |
|--------|-----------|-----------------|
| Memory | All threads share memory | Each process has its own memory |
| GIL | Limited by GIL | No GIL limitation |
| Best for | Waiting tasks (network, files) | Heavy calculations (CPU work) |
| Crash safety | One crash can break everything | One crash won't affect others |

> **One important thing to know:** Unlike threading, multiprocessing actually uses multiple CPU cores at the same time. But because each process has its own memory, they cannot see each other's variables. They need special tools to communicate — like pipes and queues.

---

## 2. Spawning Processes

**File:** `spawning_processes.py`

### What is Spawning?

Spawning means creating a new process. Think of it like a parent giving birth to a child process. The child process runs separately from the parent.

### How does spawning work?

| Step | What you do | What happens |
|------|-------------|--------------|
| 1 | Define a function | You write the work the process should do |
| 2 | Create a Process object | Python prepares a new process |
| 3 | Call `.start()` | The process begins running |
| 4 | Call `.join()` (optional) | Your program waits for it to finish |

### Key concepts to understand

**What is process isolation?**
Each process has its own memory. If one process changes a variable, other processes cannot see that change. This is good for safety but bad for communication.

**What happens when you start a process?**
The child process loads its own Python interpreter and starts running. The parent process keeps running at the same time. They run truly in parallel.

**What is the difference between creating and starting?**
Creating just sets up the process. Starting actually runs it. This separation gives you control — you can create many processes first, then start them all at once.

---
**output:
C:\Users\LAPTOP LAB>"C:/Users/LAPTOP LAB/AppData/Local/Programs/Python/Python312/python.exe" "c:/Users/LAPTOP LAB/OneDrive - Higher Educatior
ommission/Desktop/PDC-SP26-CS/23fa-052-cs-sara/chap3/spawning_processes.py"
calling myFunc from process n°: 0
calling myFunc from process n°: 1
output from myFunc is :0
calling myFunc from process n°: 2
output from myFunc is :0
output from myFunc is :1
calling myFunc from process n°: 3
output from myFunc is :0
output from myFunc is :1
output from myFunc is :2
calling myFunc from process n°: 4
output from myFunc is :0
output from myFunc is :1
output from myFunc is :2
output from myFunc is :3
calling myFunc from process n°: 5
output from myFunc is :0
output from myFunc is :1
output from myFunc is :2
output from myFunc is :3
output from myFunc is :4

C:\Users\LAPTOP LAB>
## 3. Naming Processes

**File:** `naming_processes.py`

### Why should you name your processes?

By default, Python gives processes boring names like `Process-1`, `Process-2`, `Process-3`. When something goes wrong and you are reading error logs, those names tell you nothing.

| Default Name | Custom Name |
|--------------|-------------|
| Process-1 | ImageResizer |
| Process-2 | DataProcessor |
| Process-3 | LogWriter |

-  Without names: *Error in Process-2* — which one failed?
-  With names: *Error in DataProcessor* — you know immediately.

### What are the benefits of naming?

| Benefit | Explanation |
|---------|-------------|
| Debugging | Errors clearly tell you which process failed |
| Logging | Logs become readable and meaningful |
| Monitoring | System tools show helpful names |
| Targeted shutdown | You can stop specific processes by name |

> **Simple rule:** Always give your processes meaningful names. Your future self will thank you when something breaks at 2 AM.

---

## 4. Worker Functions (myFunc)

**File:** `myFunc.py`

### What is a worker function?

A worker function (also called target function) contains the actual work that a process should do. It is the "job description" for the process.

### Why put worker functions in a separate file?

| Without separate file | With myFunc separate file |
|-----------------------|--------------------------|
| Spawning code is messy | Spawning code stays clean |
| Hard to reuse the same work | Same work can be used by many scripts |
| Difficult to test | Easy to test the function alone |
| Everything mixed together | Clear separation of concerns |

### Simple analogy

| Part | Role |
|------|------|
| myFunc (worker function) | The recipe — WHAT to cook |
| Spawning code | The manager — WHEN and HOW to cook |

> **Design principle:** Separation of concerns — keep your work logic separate from your process management logic. This makes your code cleaner, more reusable, and easier to test.

---
output:

NameError: name 'myFunc' is not defined
## 5. Pipes – Two-Way Communication

**File:** `communicating_with_pipe.py`

### What is a pipe?

A pipe is like a physical pipe connecting two people. One person puts a message in one end, and the other person gets it from the other end. It connects exactly two processes.

### How does a pipe work?

| Operation | What it does |
|-----------|--------------|
| `send(data)` | Put data into the pipe |
| `recv()` | Take data out of the pipe (waits if nothing is there) |

### Characteristics of a pipe

| Characteristic | Explanation |
|----------------|-------------|
| Exactly 2 participants | Only two processes can use a pipe |
| Bidirectional | Both processes can send and receive |
| FIFO order | First message in = first message out |
| Blocking | If pipe is empty, `recv()` waits |
| Low overhead | Very fast and simple |

### When should you use a pipe?

| Use Case | Why pipe is good |
|----------|-----------------|
| Parent talking to one child | Perfect for two-way conversation |
| Request-response pattern | One asks, the other answers |
| Simple data streaming | Continuous flow of information |
| Low-latency needs | Minimal performance cost |

> **Real world analogy:** A walkie-talkie conversation between two people. Only two people can talk, and they take turns. Simple and effective.

---
output:
C:\Users\LAPTOP LAB>"C:/Users/LAPTOP LAB/AppData/Local/Programs/Python/Python312/python.exe" "c:/Users/LAPTOP LAB/OneDrive - Higher Education C
ommission/Desktop/PDC-SP26-CS/23fa-052-cs-sara/chap3/communicating_with_pipe.py"

0
1

4

9

16
25
36
49
64
81
End

C:\Users\LAPTOP LAB>
## 6. Queues – Multi-Way Communication

**File:** `communicating_with_queue.py`

### What is a queue?

A queue is like a waiting line at a coffee shop. Many customers (producers) place orders, and many baristas (consumers) take orders and fulfill them. The queue handles everything automatically.

### How is a queue different from a pipe?

| Aspect | Pipe | Queue |
|--------|------|-------|
| Number of senders | Exactly 2 | Unlimited |
| Number of receivers | Exactly 2 | Unlimited |
| Complexity | Simple | Still simple but more powerful |
| Best for | Two-way conversation | Work distribution |

### Key operations

| Operation | What it does |
|-----------|--------------|
| `put(item)` | Add item to queue (waits if full) |
| `get()` | Remove and return item (waits if empty) |
| `put_nowait()` | Add item — fails if full |
| `get_nowait()` | Remove item — fails if empty |

### The producer-consumer pattern

```
Producer(s) ──put──> [ QUEUE ] ──get──> Consumer(s)
```

| Role | Responsibility |
|------|---------------|
| Producer | Creates work and adds it to the queue |
| Consumer | Takes work from the queue and processes it |
| Queue | The buffer that holds waiting work |

### When should you use a queue?

| Use Case | Why queue is good |
|----------|------------------|
| Many workers need tasks | Queue distributes work automatically |
| Collecting results from many processes | Multiple producers, one consumer |
| Logging from multiple processes | Many writers, one reader |
| Load balancing | Workers take next available task |

> **Real world analogy:** A restaurant kitchen. Many waiters put orders in (producers). Many cooks take orders (consumers). The ticket rail holds orders waiting to be made (the queue). Everything runs smoothly without chaos.

---
output:
C:\Users\LAPTOP LAB>"C:/Users/LAPTOP LAB/AppData/Local/Programs/Python/Python312/python.exe" "c:/Users/LAPTOP LAB/OneDrive - Higher Education Commission/Desktop/PDC-SP26-CS/23fa-052-cs-sara/chap3/communicating_with_queue.p

Process Producer : item 12 appended to queue producer-1
The size of queue is 1
Process Producer : item 125 appended to queue producer-1
The size of queue is 2
Process Producer : item 167 appended to queue producer-1
Process Consumer : item 12 popped

The size of queue is 2
Process Producer : item 162 appended to queue producer-1
The size of queue is 3
Process Producer : item 106 appended to queue producer-1
The size of queue is 4
Process Producer : item 256 appended to queue producer-1
Process Consumer : item 125 popped

The size of queue is 4
Process Producer : item 219 appended to queue producer-1
The size of queue is 5
Process Producer : item 60 appended to queue producer-1
Process Consumer : item 167 popped

The size of queue is 5
Process Producer : item 112 appended to queue producer-1
The size of queue is 6
Process Producer : item 146 appended to queue producer-1
The size of queue is 7
Process Consumer : item 162 popped

Process Consumer : item 106 popped

Process Consumer : item 256 popped

Process Consumer : item 219 popped

Process Consumer : item 60 popped

Process Consumer : item 112 popped

Process Consumer : item 146 popped

the queue is empty

C:\Users\LAPTOP LAB>]

from by consumer-2

from by consumer-2

from by consumer-2

from by consumer-2

from by consumer-2

from by consumer-2

from by consumer-2

from by consumer-2

from by consumer-2

from by consumer-2
## 7. Killing Processes

**File:** `killing_processes.py`

### What does killing a process mean?

Killing means force-stopping a process from outside. Like pulling the plug on a machine. The process does not get a chance to clean up or finish its work.

### Two ways to kill a process

| Method | What it does | Is it gentle? |
|--------|--------------|---------------|
| `.terminate()` | Asks politely to stop | Yes — process can clean up |
| `.kill()` | Cuts power immediately | No — no cleanup possible |

### Why is killing risky?

| Risk | Explanation |
|------|-------------|
| Data loss | Unwritten data disappears forever |
| File corruption | Partially written files become unusable |
| Resource leaks | Files, network connections stay open |
| Zombie processes | Child processes become orphaned |

### What is graceful shutdown (the right way)?

| Step | Action |
|------|--------|
| 1 | Send a message: "Please stop when you are done" |
| 2 | Process finishes its current task |
| 3 | Process saves everything and closes files |
| 4 | Process exits on its own |

> **Why graceful shutdown is better:** No data loss, no corruption, no leaks.

### When is killing acceptable?

| Situation | Okay to kill? |
|-----------|---------------|
| Process is frozen (not responding) |  Yes — last resort |
| Testing on your own computer |  Yes |
| Production system with customer data |  No |
| Database is being updated |  No |
| Normal operation | No — always try graceful first |

> **Simple rule:** Always try graceful shutdown first. Only kill if the process is completely frozen.

---
output:
C:\Users\LAPTOP LAB>"C:/Users/LAPTOP LAB/AppData/Local/Programs/Python/Python312/python.exe" "c:/Users/LAPTOP LAB/OneDrive - Higher Education Commission/Desktop/PDC-SP26-CS/23fa-052-cs-sara/chap3/killing_processes.py"
Process before execution: <Process name='Process-1' parent=27024 initial> False
Process running: <Process name='Process-1' pid=19828 parent=27024 started> True
Process terminated: <Process name='Process-1' pid=19828 parent=27024 started> True
Process joined: <Process name="Process-1' pid=19828 parent=27024 stopped exitcode =- SIGTERM> False
Process exit code: -15

C:\Users\LAPTOP LAB>I
## 8. Quick Reference

### File-to-Concept Mapping

| File | Main Concept | What problem it solves |
|------|--------------|------------------------|
| `spawning_processes.py` | Creating processes | How to run tasks in parallel across CPU cores |
| `naming_processes.py` | Process names | How to identify which process is which |
| `myFunc.py` | Worker functions | How to keep work logic separate and reusable |
| `communicating_with_pipe.py` | Pipe communication | How two processes can talk to each other |
| `communicating_with_queue.py` | Queue communication | How many processes can share work |
| `killing_processes.py` | Process termination | How to stop processes (and why to be careful) |

### Which tool should you use?

| What you need | Use this | Why |
|---------------|----------|-----|
| Create a new process | Spawning | Gives you isolated parallel execution |
| Identify processes in logs | Naming | Turns confusing errors into clear ones |
| Reusable work logic | Separate myFunc file | Cleaner code, easier testing |
| Two processes talking | Pipe | Simple, fast, low overhead |
| Many processes sharing work | Queue | Automatic safety, fair distribution |
| Stop a frozen process | Graceful shutdown then `.terminate()` | Prevents data loss |

### Do's and Don'ts

|  Do | Don't |
|-------|---------|
| Always name your processes | Use default Process-1, Process-2 names |
| Use queues for most communication | Try to share variables directly (won't work) |
| Implement graceful shutdown | Kill processes without trying to stop nicely |
| Keep worker functions separate | Embed work logic inside spawning code |
| Use pipes for simple two-way chat | Use pipes when you have many processes |

---

## 9. Conclusion

You have now gone through the core concepts of Python multiprocessing — from creating your first process all the way to understanding pipes, queues, and safe process termination.

### What you learned

| Topic | Core understanding |
|-------|--------------------|
| Spawning | Creating separate processes that run truly in parallel |
| Naming | Giving processes meaningful names for debugging |
| Worker functions | Keeping work logic separate from process management |
| Pipes | Two-way communication for exactly two processes |
| Queues | Safe, automatic communication for many processes |
| Killing | Forceful termination — and why to avoid it |

> **One-line summary:** Processes run separately with their own memory, need pipes or queues to talk to each other, and should be stopped gracefully — not killed — whenever possible.

### What makes multiprocessing different from threading

| If you need... | Use threading | Use multiprocessing |
|----------------|---------------|---------------------|
| To wait for network or files |  Best choice | Too heavy |
| To do heavy calculations |  Limited by GIL | Best choice |
| To share memory easily | Easy |  Need IPC |
| To protect against crashes |  One crash kills all |  Isolated |

---

