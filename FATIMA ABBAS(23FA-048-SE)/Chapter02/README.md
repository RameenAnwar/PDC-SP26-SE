# Chapter02 - Python Parallel Programming
# ============================================================
# CHAPTER 02: THREADING AND SYNCHRONIZATION IN PYTHON
# ============================================================

# ------------------------------------------------------------
# OVERVIEW
# ------------------------------------------------------------
# This chapter explains multithreading in Python using the
# threading module. It focuses on executing multiple tasks
# concurrently and managing shared resources safely using
# synchronization techniques.

# ------------------------------------------------------------
# OBJECTIVES
# ------------------------------------------------------------
# - Understand multithreading
# - Learn thread creation and lifecycle
# - Identify race conditions
# - Apply synchronization mechanisms

# ------------------------------------------------------------
# THREAD EXECUTION FLOW
# ------------------------------------------------------------

#        Main Program
#             │
#     ┌───────┼────────┐
#     │       │        │
#  Thread1  Thread2  Thread3
#     │       │        │
#     └───────┴────────┘
#             │
#        Final Output

# ------------------------------------------------------------
# RACE CONDITION (PROBLEM)
# ------------------------------------------------------------

# Shared Variable = 0

# Thread-1 → Read (0)
# Thread-2 → Read (0)
# Thread-1 → Write (1)
# Thread-2 → Write (1)

# Final Result = 1 (Incorrect, expected 2)

# ------------------------------------------------------------
# LOCK (SOLUTION)
# ------------------------------------------------------------

# Thread-1 → Acquire Lock → Critical Section → Release Lock
# Thread-2 → Wait → Execute after lock is released

# Only one thread accesses shared data at a time

# ------------------------------------------------------------
# RLOCK (REENTRANT LOCK)
# ------------------------------------------------------------

# Thread-1:
#   acquire()
#     acquire() again
#       release()
#         release()

# Same thread can acquire the lock multiple times

# ------------------------------------------------------------
# SEMAPHORE
# ------------------------------------------------------------

# Limit = 2 threads

# Thread-1 → Allowed
# Thread-2 → Allowed
# Thread-3 → Waiting
# Thread-4 → Waiting

# Controls limited access to resources

# ------------------------------------------------------------
# EVENT COMMUNICATION
# ------------------------------------------------------------

# Worker Thread         Waiting Thread
#     │                     │
#   Work Done            wait()
#     │                     │
#   set() --------------> Signal Received → Continue

# ------------------------------------------------------------
# CONDITION VARIABLE
# ------------------------------------------------------------

# Producer → produce data → notify()
# Consumer → wait() → consume data

# Threads wait until a condition is satisfied

# ------------------------------------------------------------
# BARRIER
# ------------------------------------------------------------

# Thread-1 ─┐
# Thread-2 ─┼──> Barrier → Continue together
# Thread-3 ─┘

# All threads must reach the barrier before continuing

# ------------------------------------------------------------
# THREAD LIFECYCLE
# ------------------------------------------------------------

#     ┌──────────┐
#     │  Created │
#     └────┬─────┘
#          │
#          ▼
#     ┌──────────┐
#     │  Started │
#     └────┬─────┘
#          │
#          ▼
#     ┌──────────┐
#     │ Running  │
#     └────┬─────┘
#          │
#   ┌──────┴──────┐
#   │             │
#   ▼             ▼
# Waiting      Terminated
# (Blocked)        │
#   │              │
#   └──────▶───────┘

# Explanation:
# A thread goes through different stages from creation to
# completion. It may pause (waiting) and resume execution.
# ------------------------------------------------------------
# QUEUE (THREAD-SAFE COMMUNICATION)
# ------------------------------------------------------------

# Producer → Queue → Consumer

# put(item) → queue → get(item)

# Safe communication without manual locking

# ------------------------------------------------------------
# FILE DESCRIPTIONS
# ------------------------------------------------------------

# ------------------------------------------------------------
# MULTITHREADING SYSTEM ARCHITECTURE
# ------------------------------------------------------------

#                ┌──────────────────────┐
#                │     Main Process     │
#                └─────────┬────────────┘
#                          │
#        ┌─────────────────┼─────────────────┐
#        │                 │                 │
#  ┌────────────┐   ┌────────────┐   ┌────────────┐
#  │  Thread-1  │   │  Thread-2  │   │  Thread-3  │
#  └─────┬──────┘   └─────┬──────┘   └─────┬──────┘
#        │                │                │
#        └────────┬───────┴────────┬───────┘
#                 │                │
#        ┌───────────────────────────────┐
#        │     Shared Resource/Data      │
#        └──────────────┬────────────────┘
#                       │
#               ┌───────────────┐
#               │ Synchronization│
#               │ Mechanisms     │
#               │ (Lock/Sem/etc) │
#               └───────────────┘

# Explanation:
# Multiple threads operate within a single process and access
# shared resources. Synchronization mechanisms ensure that
# access remains controlled and consistent.

# Thread_definition.py → Basic thread creation
# Thread_determine.py → Thread behavior
# Thread_name_and_processes.py → Thread naming
# MyThreadClass.py → Custom thread implementation
# MyThreadClass_lock.py → Lock usage
# MyThreadClass_lock_2.py → Advanced locking
# Rlock.py → Reentrant lock implementation
# Semaphore.py → Resource control
# Event.py → Thread signaling
# Condition.py → Condition-based synchronization
# Barrier.py → Synchronization checkpoint
# Threading_with_queue.py → Queue-based threading

# ------------------------------------------------------------
# HOW TO RUN
# ------------------------------------------------------------

# python filename.py

# Example:
# python Semaphore.py

# ------------------------------------------------------------
# LEARNING OUTCOMES
# ------------------------------------------------------------

# - Build multithreaded applications
# - Handle synchronization issues
# - Improve performance using concurrency
# - Apply appropriate synchronization tools

# ------------------------------------------------------------
# IMPORTANT NOTES
# ------------------------------------------------------------

# - Always protect shared data
# - Improper synchronization leads to race conditions
# - Python uses GIL (Global Interpreter Lock)

# ------------------------------------------------------------
# CONCLUSION
# ------------------------------------------------------------

# This chapter provides a strong foundation in multithreading
# and synchronization, essential for developing efficient and
# scalable software systems.

# ============================================================ is main koi achi si represtentaion ky liye diagaram ya graph include
