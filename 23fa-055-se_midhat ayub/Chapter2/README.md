# Python Threading – Study Notes

> These notes cover how Python uses threads, locks, and other tools to run multiple tasks at the same time without things going wrong.

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Thread Definition](#2-thread-definition)
3. [Thread Determine](#3-thread-determine)
4. [Thread Name and Processes](#4-thread-name-and-processes)
5. [MyThreadClass – Basic Custom Thread](#5-mythreadclass--basic-custom-thread)
6. [MyThreadClass with Lock](#6-mythreadclass-with-lock)
7. [MyThreadClass with Lock 2](#7-mythreadclass-with-lock-2)
8. [Barrier](#8-barrier)
9. [Condition](#9-condition)
10. [Event](#10-event)
11. [Rlock](#11-rlock)
12. [Semaphore](#12-semaphore)
13. [Threading with Queue](#13-threading-with-queue)
14. [Conclusion](#14-conclusion)

---

## 1. Introduction

Normally, a Python program runs one thing at a time — step 1, then step 2, then step 3. But sometimes you want your program to do multiple things at the same time. That is where **threading** comes in.

Python has a built-in module called `threading` that lets you run multiple tasks inside the same program at the same time. Each task runs in its own **thread**.

**When is threading actually useful?**

- You are downloading something and want to show a progress bar at the same time
- Your program is waiting for a file or a network reply and you do not want it to sit there doing nothing
- You want to handle multiple users or tasks without making everyone wait in a line

> **One important thing to know:** Python has something called the **GIL (Global Interpreter Lock)**. Because of this, threads do not truly run side by side for heavy calculations. But for tasks that involve waiting — like reading files or getting data from the internet — threading works really well.

---

## 2. Thread Definition

**File:** `Thread_definition.py`

### Concepts Covered

**What is a Thread?**
A thread is the smallest unit of work inside a program. Think of a thread like a worker — you assign it a job, tell it to start, and wait for it to finish. Multiple threads can exist inside the same program and run at the same time.

**What is the `threading` module?**
It is Python's built-in tool for creating and managing threads. You do not need to install anything — it comes with Python.

**How does a thread start and stop?**
A thread does not start the moment you create it. You have to explicitly tell it to start. And if you want your main program to wait for a thread to finish before moving on, you have to tell it that too. Without this, the main program might end before the thread even gets to run.

**What is the difference between creating a thread and running it?**
Creating a thread just sets it up. Running it is a separate step. This distinction matters because it gives you control over exactly when work begins.

---

## 3. Thread Determine

**File:** `Thread_determine.py`

### Concepts Covered

**How do you know if a thread is still running?**
Once you start threads, your program keeps moving. You need a way to check — is this thread still doing its work, or has it already finished? Python gives you tools to check this at any point.

**What is thread status?**
Every thread has a status — it is either alive (still running) or dead (finished). Knowing this helps you decide what to do next in your program.

**How many threads are running at once?**
At any moment, your program might have several threads active at the same time. You can ask Python to count them or list them all. This is very useful when debugging.

**What is the current thread?**
From inside any function, you can ask "which thread is running this code right now?" This helps you understand the flow of your program when multiple threads are involved.

---

## 4. Thread Name and Processes

**File:** `Thread_name_and_processes.py`

### Concepts Covered

**What is a Process?**
A process is your whole running program. It has its own memory and its own resources. When you open Chrome, that is one process. When you open a calculator, that is another process. They do not share anything with each other.

**What is the relationship between a Thread and a Process?**
Threads live inside a process. One process can have many threads. All those threads share the same memory of that process. This is why threads can talk to each other easily — but it also means they can interfere with each other if you are not careful.

**Why should you name your threads?**
By default, Python gives threads boring names like Thread-1, Thread-2 and so on. When something goes wrong and you are reading logs, those names tell you nothing. Giving threads meaningful names — like "DownloadThread" or "UIThread" — makes your life much easier when debugging.

**What is the main thread?**
Every Python program starts with one thread already running. That is called the main thread. Any thread you create yourself is a child thread that runs alongside it.

---

## 5. MyThreadClass – Basic Custom Thread

**File:** `MyThreadClass.py`

### Concepts Covered

**What is Object-Oriented Threading?**
Instead of just passing a function to a thread, you can build your own thread class. This is the object-oriented way of doing threading. It gives your thread its own data, its own behavior, and makes your code much cleaner when threads need to do complex things.

**What is Inheritance in this context?**
Your custom thread class inherits from Python's built-in `Thread` class. This means your class automatically gets all the thread features — start, join, status checking — and you just add your own logic on top.

**What is the `run()` method?**
This is the heart of your custom thread. Whatever you write inside `run()` is what the thread will do when it starts. It is like writing the job description for your worker.

**Why should you never call `run()` directly?**
This is a very common beginner mistake. If you call `run()` directly, Python does not create a new thread — it just runs the code in the current thread like a normal function call. The whole point of threading is lost. Always use `start()`.

---

## 6. MyThreadClass with Lock

**File:** `MyThreadClass_lock.py`

### Concepts Covered

**What is a Race Condition?**
This is one of the most important bugs in concurrent programming. It happens when two or more threads try to read and change the same data at the same time, and the final result depends on which thread got there first. The result becomes unpredictable and wrong.

**Why does a race condition happen?**
Even a simple operation like `counter += 1` is actually multiple steps at the CPU level — read the value, add 1, write it back. If two threads do this at the same time, they can both read the old value, both add 1, and both write back the same result. You added twice but only got one increment.

**What is a Lock?**
A Lock is a tool that ensures only one thread can access a shared resource at a time. Before a thread touches the shared data, it must acquire the lock. All other threads trying to acquire the same lock are forced to wait. When the thread is done, it releases the lock and the next thread can go.

**What is the `with` statement for locks?**
It is the safe way to use a lock. It automatically acquires the lock when you enter and releases it when you leave — even if your code crashes in the middle. Without this, a crash inside a locked section would leave the lock locked forever, freezing your whole program.

**What is Thread Safety?**
A piece of code is called thread-safe if it works correctly even when multiple threads run it at the same time. Using locks is one of the main ways to make code thread-safe.

---

## 7. MyThreadClass with Lock 2

**File:** `MyThreadClass_lock_2.py`

### Concepts Covered

**What happens when you need more than one Lock?**
Real programs often have multiple shared resources, and each resource needs its own lock. This is normal and expected. But it introduces a new danger — deadlock.

**What is a Deadlock?**
A deadlock is when two or more threads are each waiting for a lock that the other one is holding. Neither can move forward. Neither can release what the other needs. The program freezes forever. No error is shown — the program just stops responding.

**How does a deadlock happen?**
Thread A takes Lock 1 and then tries to take Lock 2. At the same time, Thread B takes Lock 2 and then tries to take Lock 1. Now A is waiting for B to release Lock 2, and B is waiting for A to release Lock 1. Both wait forever.

**How do you prevent a deadlock?**
The simplest and most reliable rule is lock ordering — always acquire multiple locks in the same fixed order across all threads. If every thread always grabs Lock 1 before Lock 2, a deadlock simply cannot occur.

**What is the difference between a deadlock and a race condition?**
A race condition gives you wrong results but the program keeps running. A deadlock freezes the program completely. Both are serious bugs but they look and feel different.

---

## 8. Barrier

**File:** `Barrier.py`

### Concepts Covered

**What is a Barrier?**
A Barrier is a synchronization point in your program. When a thread reaches a Barrier, it stops and waits. It does not continue until every other thread in the group has also reached that same point. Once all threads arrive, they are all released together at the same time.

**What is Phase Synchronization?**
Some parallel programs work in stages — all threads do Phase 1, then all move to Phase 2, then Phase 3. A Barrier enforces this. It makes sure no thread jumps ahead to the next phase while others are still finishing the current one.

**Why is a Barrier useful?**
Without a Barrier, faster threads would race ahead and start working on the next phase using incomplete results from slower threads. The Barrier guarantees that all results from the current phase are ready before anyone moves on.

**Real world analogy:**
Think of a group project where everyone must finish their section before the team meets to combine everything. The meeting is the Barrier — nobody combines their work until everyone is done with their part.

---

## 9. Condition

**File:** `Condition.py`

### Concepts Covered

**What is a Condition?**
A Condition is an advanced synchronization tool that combines a lock with the ability to wait and send signals. It lets threads communicate about whether certain conditions in your program are true or not.

**What is the Producer-Consumer Problem?**
This is one of the most classic problems in concurrent programming. One thread (the producer) creates data. Another thread (the consumer) uses that data. The challenge is — what does the consumer do when there is no data yet? It should not keep checking constantly (that wastes CPU). It should sleep and wake up only when the producer has something ready.

**What does "wait" mean in threading?**
When a thread calls wait on a Condition, two things happen — it releases the lock it was holding, and it goes to sleep. This is important because if it just held the lock and did nothing, no other thread could get in to produce the data it is waiting for.

**What does "notify" mean in threading?**
When the producer is ready, it sends a notification. This wakes up the sleeping consumer. The consumer then re-acquires the lock and continues from where it left off.

**Why use Condition instead of just a loop checking a variable?**
Constantly looping and checking (called busy-waiting or spinning) wastes CPU. A Condition makes the thread truly sleep and uses zero CPU while waiting. It only wakes up when there is actually something to do.

---

## 10. Event

**File:** `Event.py`

### Concepts Covered

**What is an Event?**
An Event is the simplest way for one thread to send a signal to other threads. Think of it like a flag — it is either up or down. One thread raises the flag, and all threads waiting for the flag to go up are immediately released.

**What is the difference between set and unset?**
An Event starts in the unset state — the flag is down. Any thread that calls `wait()` on it will pause. When another thread calls `set()`, the flag goes up, and all paused threads wake up and continue. You can also lower the flag again with `clear()` and reuse the same event.

**How is Event different from Condition?**
Both are signaling tools, but Event is simpler. With an Event, you just say "go" or "not yet." With a Condition, you can be much more specific — you can pass information, check a variable, wake only one thread, and so on. Use Event for simple on/off signals, and Condition for more complex communication.

**What is the use case for Event?**
Events are great for startup scenarios — for example, multiple worker threads waiting for some initialization to complete before they all start working. One thread does the setup and then fires the event. All workers wake up at once and begin.

---

## 11. Rlock

**File:** `Rlock.py`

### Concepts Covered

**What is Reentrancy?**
A reentrant lock is one that the same thread can acquire more than once without getting stuck. Normal locks do not allow this — if a thread tries to acquire a lock it already holds, it waits for itself forever (deadlock). An RLock solves this.

**When does a thread need to acquire the same lock twice?**
This happens in recursive functions — a function that calls itself. If the function acquires a lock, then calls itself again, the second call tries to acquire the same lock. With a normal Lock, this deadlocks. With an RLock, it works fine because Python remembers it is the same thread.

**What is the release count rule?**
With an RLock, every `acquire()` must be matched with a `release()`. If a thread acquires the lock 3 times, it must release it 3 times before other threads can get in. This keeps things balanced and predictable.

**When should you use RLock instead of Lock?**
Use RLock when your code has recursive functions or nested function calls that all need the same lock. If your code is straightforward and a function only needs the lock once, a regular Lock is simpler and preferred.

---

## 12. Semaphore

**File:** `Semaphore.py`

### Concepts Covered

**What is a Semaphore?**
A Semaphore is a generalized lock. A regular Lock allows exactly 1 thread at a time. A Semaphore allows any number you choose — 2, 5, 10, whatever makes sense for your situation. It keeps a counter internally. Every time a thread enters, the counter goes down. Every time a thread leaves, it goes back up. When the counter hits zero, all new threads must wait.

**What problem does a Semaphore solve?**
Some resources can handle more than one user at a time, but not unlimited users. A database might support 10 concurrent connections. A printer might handle 3 jobs at once. A Semaphore lets you set exactly how many threads can use that resource at the same time, protecting it from being overwhelmed.

**What is the difference between a Semaphore and a Lock?**
A Lock is just a Semaphore with a limit of 1. Conceptually they are the same thing — a Semaphore is just more flexible. Use a Lock when you need exclusive access. Use a Semaphore when you want to allow a specific limited number of concurrent accesses.

**What is a Bounded Semaphore?**
Python also has a `BoundedSemaphore` which adds a safety check — it raises an error if you try to release more times than you acquired. This prevents bugs where you accidentally release too many times and let more threads in than you intended.

---

## 13. Threading with Queue

**File:** `Threading_with_queue.py`

### Concepts Covered

**What is a Queue in threading?**
A Queue is a thread-safe data structure for passing data between threads. One thread puts items in, another thread takes items out. It follows the FIFO rule — First In, First Out — meaning items come out in the same order they went in.

**What does thread-safe mean here?**
Thread-safe means the Queue handles all the internal locking for you. You do not have to write a single lock yourself. Two threads can put and get at the same time without corrupting the data or causing race conditions. The Queue takes care of all of that internally.

**What is the Producer-Consumer pattern?**
This is the design pattern that Queue is built for. One thread (producer) creates work and puts it in the queue. One or more threads (consumers) take work out and process it. The queue acts as the buffer between them. If the producer is faster, the queue fills up. If the consumer is faster, it waits for more items. They never need to talk to each other directly.

**What is task tracking?**
A Queue can also track whether all the work has actually been completed — not just removed from the queue, but fully processed. A thread signals when it is done with an item, and the queue can wait until every single item has been marked done before moving on.

**Why is Queue better than a shared list with a lock?**
You could technically share a list between threads and protect it with a lock, but that is error-prone. You have to remember to lock every access, every time. A Queue wraps all of that up safely and gives you a clean, simple interface. It is the right tool for this job and the professional approach.

---

## 14. Conclusion

You have now gone through the full journey — from creating your first thread all the way to understanding locks, semaphores, events, conditions, barriers, and queues. These are the real concepts that Python programmers must understand when writing programs that do many things at the same time.

### Quick reference 

| File | Main Concept | What problem it solves |
|------|-------------|------------------------|
| `Thread_definition` | Creating threads | How to run tasks in parallel |
| `Thread_determine` | Thread status | How to monitor running threads |
| `Thread_name_and_processes` | Threads vs Processes | How to identify and organize threads |
| `MyThreadClass` | Custom thread class | How to build reusable thread objects |
| `MyThreadClass_lock` | Lock, Race Condition | How to protect shared data |
| `MyThreadClass_lock_2` | Deadlock, Multiple Locks | How to safely use more than one lock |
| `Barrier` | Phase Synchronization | How to make all threads wait at one point |
| `Condition` | Wait and Notify | How threads communicate about data readiness |
| `Event` | Simple Signaling | How to send a go signal between threads |
| `Rlock` | Reentrant Locking | How to lock safely in recursive functions |
| `Semaphore` | Controlled Access | How to limit concurrent access to a resource |
| `Threading_with_queue` | Producer-Consumer | How to safely pass data between threads |

### Which tool should you use?

- Need only 1 thread at a time? → Use a **Lock**
- Same thread needs to lock more than once? → Use an **RLock**
- Want to allow a limited number of threads in? → Use a **Semaphore**
- Need a simple "start now" signal? → Use an **Event**
- Need threads to wait and notify each other? → Use a **Condition**
- Need all threads to meet at one point before continuing? → Use a **Barrier**
- Need to pass data between threads safely? → Use a **Queue**

---

