Chapter # 2
1. Thread_definition.py
What I learned:
I learned the most basic way to define and launch threads by passing a target function and arguments to the Thread constructor.

How to execute:
Run in cmd: python Thread_definition.py to see 10 threads call the same function and print their assigned numbers.

Use cases:
Quick, simple background tasks that don't require complex object-oriented logic or custom data.

Requirements for execution:
The threading module and the target and args parameters.

Advantages:
The fastest way to implement threading with very little code; excellent for simple parallelization.

Disadvantages:
Harder to manage thread-specific state compared to inheriting from the Thread class.

2. MyThreadClass.py
What I learned:
I learned how to create a custom thread by inheriting from the threading.Thread class and overriding the run() method.

How to execute:
Run in cmd: python MyThreadClass.py to spawn nine custom threads that run and sleep for random durations independently.

Use cases:
Encapsulating complex thread logic into an object-oriented structure for cleaner, more maintainable code.

Requirements for execution:
Defining a class that inherits from Thread and calling the __init__ of the parent class.

Advantages:
Allows you to attach specific data (like name and duration) directly to the thread object for easier management.

Disadvantages:
Requires more boilerplate code compared to just passing a simple function to a standard Thread object.

3. Thread_determine.py
What I learned:
I learned how to name threads and identify them during execution using threading.currentThread().getName().

How to execute:
Run in cmd: python Thread_determine.py to see three different functions start and exit, identifying themselves by name.

Use cases:
Logging and debugging complex multi-threaded apps where you need to know exactly which thread produced a specific error or log.

Requirements for execution:
The name attribute in the Thread constructor and the currentThread() function.

Advantages:
Makes terminal output much more readable; you can tell "Function_A" from "Function_B" immediately.

Disadvantages:
Names are for human readability only; they do not change how the Python interpreter handles the thread logic.

4. MyThreadClass_lock.py
What I learned:
I learned how to use a threading.Lock to enforce "Mutual Exclusion," ensuring only one thread can access a code block at a time.

How to execute:
Run in cmd: python MyThreadClass_lock.py; notice that threads now finish one by one in order because they must wait for the lock.

Use cases:
Protecting shared data (like a bank balance or a shared file) from being modified by two threads at the exact same time.

Requirements for execution:
A global threading.Lock() object and the use of acquire() and release() around critical code.

Advantages:
Completely prevents data corruption by ensuring that only one "worker" is in the sensitive area of the code at once.

Disadvantages:
Significantly slows down the program because it turns parallel execution back into sequential execution while the lock is held.

5. MyThreadClass_lock_2.py
What I learned:
I learned how to minimize the "Critical Section" by acquiring and releasing a lock only for the specific line of code that needs protection, rather than the entire function.

How to execute:
Run in cmd: python MyThreadClass_lock_2.py to see how threads print their start message one-by-one but then sleep simultaneously, making the overall execution faster than a full lock.

Use cases:
Optimizing performance in multi-threaded apps where only a small part of a task (like updating a counter) needs to be synchronized.

Requirements for execution:
A threading.Lock() object and the strategic placement of acquire() and release() calls within the run() method.

Advantages:
Increases efficiency by allowing threads to perform non-sensitive work (like time.sleep) in parallel while still protecting shared resources.

Disadvantages:
If the lock is released too early, you risk data corruption if another thread modifies the data while the first thread is still processing it.

6. Rlock.py
What I learned:
I learned about the "Reentrant Lock" (RLock), which allows the same thread to acquire the lock multiple times without causing a deadlock.

How to execute:
Run in cmd: python Rlock.py to see an adder and remover modify a Box object that uses nested locked methods.

Use cases:
Complex objects where one locked method calls another locked method within the same class.

Requirements for execution:
Replacing a standard Lock with threading.RLock() when recursive or nested locking is needed.

Advantages:
Prevents a thread from "locking itself out" when calling its own synchronized methods.

Disadvantages:
Slightly more overhead than a regular lock; it should only be used when reentrancy is actually required.

7. Semaphore.py
What I learned:
I learned how to use a Semaphore to manage access based on a counter, allowing a specific number of threads to pass.

How to execute:
Run in cmd: python Semaphore.py to see a consumer wait for a producer to "release" a permit before it can display the item.

Use cases:
Limiting connections to a database, controlling how many users can download a file at once, or managing a pool of resources.

Requirements for execution:
threading.Semaphore(value) where value is the number of concurrent permits allowed.

Advantages:
Much more flexible than a Lock because it can allow multiple threads (e.g., 3 or 5) instead of just one.

Disadvantages:
More difficult to debug; if a thread forgets to release(), a permit is lost forever, potentially causing a system hang.

8. Barrier.py
What I learned:
I learned how to use a Barrier to synchronize multiple threads, ensuring that all threads reach a specific point in execution before any of them can proceed.

How to execute:
Run in cmd: python Barrier.py to see three "runners" reach the barrier at different times and only finish the race once the last one arrives.

Use cases:
Simulating a race, parallel computing where a phase must finish before the next starts, or multi-player game lobby "ready" checks.

Requirements for execution:
The threading.Barrier object initialized with the exact number of threads that must wait for each other.

Advantages:
Prevents "race conditions" where one part of a program starts too early; very simple to implement for fixed-party synchronization.

Disadvantages:
If one thread fails or crashes before reaching the barrier, all other threads will wait indefinitely (deadlock).

9. Condition.py
What I learned:
I learned how to use a Condition object to allow threads to wait for specific state changes, effectively managing Producer-Consumer relationships.

How to execute:
Run in cmd: python Condition.py to observe a Producer adding items and a Consumer waiting until items are available before removing them.

Use cases:
Inventory management systems, task queues, or any scenario where a thread depends on a specific variable value to proceed.

Requirements for execution:
The threading.Condition object and the use of wait() and notify() methods within a with statement.

Advantages:
More efficient than a basic lock because it allows threads to "sleep" and consume zero CPU power while waiting for a notification.

Disadvantages:
Can lead to complex logic bugs if notify() is called at the wrong time or if wait() is not checked within a loop.

10. Event.py
What I learned:
I learned how to use an Event to communicate between threads using a simple internal "true/false" flag.

How to execute:
Run in cmd: python Event.py to see a consumer thread stop and wait until a producer "sets" the event signal.

Use cases:
Starting multiple background services at once, stopping threads gracefully, or signaling that a setup process is complete.

Requirements for execution:
The threading.Event object and the set(), clear(), and wait() methods.

Advantages:
One of the simplest ways for one thread to signal "GO" or "STOP" to many other threads simultaneously.

Disadvantages:
It is a "binary" signal; it cannot pass data (like a message) between threads, only the fact that an event occurred.

11. Thread_name_and_processes.py
What I learned:
I learned how to verify that all threads created within a script belong to the same Process ID (PID), confirming that threading happens within a single process.

How to execute:
Run in cmd: python Thread_name_and_processes.py to see different thread names printed alongside the OS process ID they are running under.

Use cases:
System monitoring and debugging to ensure that your application is not accidentally spawning heavy new processes when you only intended to use light threads.

Requirements for execution:
The os module to fetch the process ID and a custom thread class to print the identification data.

Advantages:
Provides technical proof of how the operating system handles Python threads versus processes.

Disadvantages:
Since it focuses on identification rather than logic, this script doesn't perform any actual data processing.

12. Threading_with_queue.py
What I learned:
I learned how to use a Queue for thread-safe communication, allowing Producers to send data to multiple Consumers without manually managing locks.

How to execute:
Run in cmd: python Threading_with_queue.py to watch one Producer add random items to a queue while three Consumers compete to pull and process them.

Use cases:
Handling background tasks like email sending, processing web requests, or any system where tasks are produced faster than they can be finished.

Requirements for execution:
The queue.Queue object and the use of put() for producers and get() followed by task_done() for consumers.

Advantages:
Queues are inherently thread-safe; they automatically handle the locking logic for you, making your code much cleaner and less prone to errors.

Disadvantages:
If consumers are slower than the producer, the queue will grow indefinitely and may eventually consume all available system memory.