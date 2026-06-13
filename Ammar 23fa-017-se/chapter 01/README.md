# Chapter 1: Getting Started with Parallel Computing and Python

## 1.1 Why Do We Need Parallel Computing?

**The Historical Context**

- Single-Core Era (Pre-2000s): Increase transistors → Higher clock speed → More heat/power → Physical limitations
- Multi-Core Era (2000s-Present): Multiple cores → Parallel execution → Better performance/watt → Scalable performance

**Key Challenges**

| Era | Approach | Limitation |
|-----|----------|------------|
| 1980s-2000s | Increase clock speed (3.5-4 GHz peak) | Power dissipation, heat |
| 2000s-Present | Add more cores (2, 4, 8, 16+ cores) | Software must be parallelized |
| Future | Heterogeneous computing (CPU + GPU) | Programming complexity |

**The Free Lunch is Over**
- Single-core performance improvements have stalled
- Modern CPUs (desktop/laptop) are now quad-core or octa-core standard
- **Consequence:** Software must be redesigned for parallel execution to utilize available hardware

> Key Insight: Parallel computing is no longer optional for high-performance applications—it's a necessity.

---

## 1.2 Flynn's Taxonomy

Flynn's Taxonomy classifies computer architectures based on two independent dimensions:
- **Instruction Stream:** The sequence of instructions executed
- **Data Stream:** The sequence of data being processed

```
Flynn's Taxonomy
├── SISD (Single Instruction, Single Data)
├── SIMD (Single Instruction, Multiple Data)
├── MISD (Multiple Instruction, Single Data)
└── MIMD (Multiple Instruction, Multiple Data)
```

### 1.2.1 SISD (Single Instruction, Single Data)

**Classic Von Neumann Architecture**

CPU Cycle (Fetch-Decode-Execute): Fetch → Decode → Execute → Repeat

**Characteristics:**
- One instruction processes one data element at a time
- Sequential execution (no parallelism)
- Examples: Traditional single-core processors (Intel 8086, ARM Cortex-M)

### 1.2.2 SIMD (Single Instruction, Multiple Data)

```
Control Unit
    │
    ├──> PU 1 (Data 1)
    ├──> PU 2 (Data 2)
    ├──> PU 3 (Data 3)
    └──> PU 4 (Data 4)
```

**Characteristics:**
- One instruction operates on multiple data elements simultaneously
- Data-level parallelism
- Examples: Vector processors (Cray supercomputers), Modern GPUs, CPU SIMD extensions (Intel SSE/AVX, ARM NEON)

**Applications:**
- Image/Video processing
- Matrix operations
- Machine learning inference

### 1.2.3 MISD (Multiple Instruction, Single Data)

```
Memory (Single Data Stream)
    │
    ├──> PU 1 (Instruction 1)
    ├──> PU 2 (Instruction 2)
    └──> PU 3 (Instruction 3)
```

**Characteristics:**
- Multiple instructions operate on the same data
- Rarely used in commercial systems
- **Use Cases:** Fault-tolerant systems, Data encryption (specific niche applications)

### 1.2.4 MIMD (Multiple Instruction, Multiple Data)

```
Processor 1                Processor 2                Processor N
Control Unit 1            Control Unit 2            Control Unit N
    │                          │                          │
    ▼                          ▼                          ▼
PU 1 + Memory 1           PU 2 + Memory 2           PU N + Memory N
    │                          │                          │
    └──────────┬───────────────┴───────────────┬──────────┘
               └─── Interconnect Network ───────┘
```

**Characteristics:**
- Most general and powerful class
- Each processor has its own control unit and memory
- Processors can run different programs on different data
- Examples: Modern multi-core processors (Intel Core i7, AMD Ryzen), Computer clusters, Supercomputers

**Comparison: SIMD vs. MIMD**

| Feature | SIMD | MIMD |
|---------|------|------|
| Control | Single control unit | Multiple control units |
| Parallelism | Data-level | Task/Thread-level |
| Flexibility | Limited | High |
| Complexity | Lower | Higher |
| Programming | Easier for data-parallel problems | More general-purpose |

---

## 1.3 Memory Organization

### Overview of MIMD Memory Architectures

```
MIMD Architectures
├── Shared Memory
│   ├── UMA (Uniform Memory Access)
│   ├── NUMA (Non-Uniform Memory Access)
│   └── COMA (Cache-Only Memory Architecture)
└── Distributed Memory
    ├── MPP (Massively Parallel Processing)
    └── Cluster of Workstations
```

### 1.3.1 Shared Memory Systems

```
CPU 1 + Cache ──┐
CPU 2 + Cache ──┼── System Bus ── Main Memory
CPU 3 + Cache ──┤
CPU 4 + Cache ──┘
```

**Types of Shared Memory Access:**

| Type | Description | Scalability | Example |
|------|-------------|-------------|---------|
| UMA | Uniform access time for all processors | Poor | Symmetric Multiprocessor (SMP) |
| NUMA | Local memory faster than remote | Good | Modern multi-socket servers |
| COMA | Cache-only memory architecture | Moderate | Specialized systems |
| NoRMA | No remote memory access (message passing) | High | Clusters |

**The Cache Coherency Problem**

```
CPU 1 writes X=10    │    CPU 2 reads X=5 (Stale!)
        ▼            │            ▼
   Cache 1: X=10     │       Cache 2: X=5
        │            │            │
        └──────┬─────┴──────┬─────┘
               ▼            ▼
          Main Memory: X=10
```

**Solutions:**
- Hardware cache coherency protocols (MESI, MOESI)
- Software synchronization mechanisms (locks, barriers)

### 1.3.2 Distributed Memory Systems

```
Node 1 (CPU + Memory) ←→ Interconnection Network ←→ Node 2 (CPU + Memory)
                                 ↕
                          Node N (CPU + Memory)
```

**Message Passing Communication:**

```
Process 1                Process 2
    │                        │
Prepare Data                │
    │                        │
Send Message ───────────────>│
    │                     Receive Message
    │                     Process Data
    │<───────────────────── Send Result
Receive Result              │
```

**Advantages:**
- No cache coherency issues
- Excellent scalability
- Each processor has full memory bandwidth

**Disadvantages:**
- Communication overhead (message passing)
- Complex data distribution required
- Higher programming complexity

### 1.3.3 Massively Parallel Processing (MPP)

| Characteristic | Description |
|----------------|-------------|
| Scale | Hundreds to hundreds of thousands of processors |
| Memory | Distributed memory model |
| Network | Specialized high-speed interconnect |
| Examples | Fugaku (Japan), Summit (USA), Tianhe-2 (China) |

### 1.3.4 Heterogeneous Architectures

```
                    ┌─────────────┐
                    │    CPU      │
                    │ Host/Serial │
                    └──────┬──────┘
                           │ PCIe Bus
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │   GPU    │ │   GPU    │ │   FPGA   │
        │ Device   │ │ Device   │ │ Device   │
        └──────────┘ └──────────┘ └──────────┘
```

**Key Characteristics:**
- CPU + Accelerators (GPU, FPGA, TPU)
- Separate memory spaces (CPU memory vs. device memory)
- Programming models: CUDA (NVIDIA), OpenCL (cross-platform)

---

## 1.4 Parallel Programming Models

### Comparison of Programming Models

```
Parallel Programming Models
├── Shared Memory
│   ├── Threads (Pthreads, OpenMP)
│   └── Shared Variables
├── Distributed Memory
│   ├── Message Passing (MPI)
│   └── PGAS (UPC, Chapel)
└── Hybrid
    ├── MPI + OpenMP
    └── MPI + CUDA
```

### 1.4.1 Shared Memory Model

```
Thread 1 ──┐
Thread 2 ──┼── Shared Memory ── Locks/Semaphores (Synchronization)
Thread 3 ──┘
```

**Features:**
- **Advantages:** Simple communication, natural data sharing
- **Disadvantages:** Race conditions, deadlocks, cache coherency overhead
- **Tools:** `threading` (Python), OpenMP (C/C++/Fortran)

### 1.4.2 Message Passing Model

```
Process 1 (Private Memory) ←→ Send/Recv Messages ←→ Process 2 (Private Memory)
                              ↕
                    Process 3 (Private Memory)
```

**Features:**
- **Advantages:** Scalable, no shared memory conflicts
- **Disadvantages:** Explicit communication, data duplication
- **Tools:** MPI (MPICH, OpenMPI), `mpi4py` (Python)

### 1.4.3 Data-Parallel Model

```
Large Dataset
    │
    ▼
Split into Chunks
    │
    ├──> Task 1 (Chunk 1)
    ├──> Task 2 (Chunk 2)
    ├──> Task 3 (Chunk 3)
    └──> Task N (Chunk N)
    │
    ▼
Combine Results
```

**Applications:**
- Array operations (NumPy)
- GPU computing (CUDA/OpenCL)
- MapReduce (Hadoop, Spark)

### 1.4.4 Designing a Parallel Program

**Four-Stage Design Process:**

```
1. Task Decomposition → 2. Task Assignment → 3. Agglomeration → 4. Mapping
         ↑                                                    │
         └────────────────────────────────────────────────────┘
                              (Iterate)
```

| Phase | Description | Key Question |
|-------|-------------|--------------|
| Decomposition | Break problem into smaller tasks | What can run in parallel? |
| Assignment | Distribute tasks among processes | How to balance the load? |
| Agglomeration | Group tasks for efficiency | Is communication overhead high? |
| Mapping | Assign tasks to processors | Which processor runs what? |

**Load Balancing Strategies:**

```
Load Balancing
├── Static (Determined at compile time)
│   ├── Domain Decomposition
│   └── Regular Grid Problems
└── Dynamic (Determined at runtime)
    ├── Task Pool
    ├── Manager/Worker
    └── Work Stealing
```

---

## 1.5 Evaluating Parallel Program Performance

### 1.5.1 Speedup

**Definition:**
```
S(p) = T(1) / T(p)
```

Where:
- T(1) = Execution time on 1 processor
- T(p) = Execution time on p processors

| Speedup Type | Condition | Interpretation |
|--------------|-----------|----------------|
| Linear/Ideal | S = p | Perfect scaling |
| Real | S < p | Some overhead |
| Superlinear | S > p | Better than ideal (caching effects) |

### 1.5.2 Efficiency

**Definition:**
```
E(p) = S(p) / p = T(1) / (p × T(p))
```

**Interpretation:**
- E = 1.0 → Perfect utilization
- E = 0.5 → 50% of processors idle/waiting
- E << 1 → Poor parallelization

### 1.5.3 Amdahl's Law

```
Serial Portion (Cannot be parallelized) ──┐
                                          ├── Total Program
Parallel Portion (Can be distributed) ───┘
```

**Formula:**
```
S = 1 / (1 - P + P/N)
```

Where:
- P = Parallelizable fraction
- N = Number of processors

**Practical Example:**

| Parallel Fraction | Max Speedup (∞ processors) |
|-------------------|----------------------------|
| 90% | 10x |
| 95% | 20x |
| 99% | 100x |
| 99.9% | 1000x |

**Amdahl's Law Impact:**
```
100% Program
├── 90% Parallel → Distributed to N cores
└── 10% Serial → Single core only
         │
         ▼
Maximum 10x speedup possible
```

> Key Insight: Even with infinite processors, performance is limited by the serial portion!

### 1.5.4 Gustafson's Law

**Formula:**
```
S(N) = N - α(N - 1)
```

Where:
- N = Number of processors
- α = Serial fraction

**Philosophical Difference:**
- **Amdahl:** Fixed problem size, faster execution
- **Gustafson:** Fixed execution time, larger problems

**Gustafson's Insight:**
```
Time Budget: 1 hour
├── 1 Processor: Solve size X
└── 1000 Processors: Solve size 1000X
         │
         ▼
Same time, larger problem
```

---

## 1.6 Introducing Python

### Why Python for Parallel Computing?

| Feature | Benefit |
|---------|---------|
| Readable syntax | Faster development |
| Rich libraries | NumPy, SciPy, multiprocessing, asyncio |
| Glue language | Integrate C/C++/Fortran for performance |
| Large community | Extensive documentation and support |

### 1.6.1 Python Syntax Basics

**Variables and Assignment:**

```python
# Multiple assignment
x, y, z = 1, 2, 3

# Increment operators
x += 5   # x = x + 5
y -= 2   # y = y - 2

# String operations
message = "Hello"
message += " World!"   # String concatenation
```

**Data Types:**

```python
# Lists (mutable)
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list[0] = 10

# Tuples (immutable)
my_tuple = (1, 2, 3)   # Cannot modify

# Dictionaries (key-value pairs)
my_dict = {'name': 'Python', 'version': 3.9}
my_dict['author'] = 'Guido'

# Sets (unique elements)
my_set = {1, 2, 3, 3, 4}   # {1, 2, 3, 4}
```

**Flow Control:**

```python
# Conditional
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# For loop
for i in range(10):
    print(f"Iteration {i}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

**Functions:**

```python
def calculate(x, y, operation='add'):
    """Documentation string"""
    if operation == 'add':
        return x + y
    elif operation == 'multiply':
        return x * y
    else:
        raise ValueError("Unknown operation")

# Lambda functions (anonymous)
square = lambda x: x ** 2
```

**List Comprehensions:**

```python
# Traditional
squares = []
for i in range(10):
    squares.append(i ** 2)

# List comprehension (Pythonic)
squares = [i ** 2 for i in range(10)]

# With condition
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
```

### 1.6.2 Classes and OOP

```python
class ParallelWorker:
    """Example class for parallel computing"""
    
    # Class variable (shared across instances)
    task_count = 0
    
    def __init__(self, worker_id):
        # Instance variables
        self.worker_id = worker_id
        self.results = []
        ParallelWorker.task_count += 1
    
    def process(self, data):
        """Process data (to be implemented by subclasses)"""
        raise NotImplementedError
    
    def __str__(self):
        return f"Worker {self.worker_id}"
    
    @classmethod
    def get_task_count(cls):
        return cls.task_count
    
    @staticmethod
    def is_valid_data(data):
        return data is not None

# Inheritance
class GPUWorker(ParallelWorker):
    def __init__(self, worker_id, device_id):
        super().__init__(worker_id)
        self.device_id = device_id
    
    def process(self, data):
        # GPU-specific processing
        return data * 2
```

### 1.6.3 Exception Handling

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        result = None
    except TypeError:
        print("Error: Invalid type!")
        result = None
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed")
    return result
```

### 1.6.4 File Operations

```python
# Writing to file
with open('output.txt', 'w') as f:
    f.write("Hello Parallel World!\n")
    f.write("Writing multiple lines")

# Reading from file
with open('output.txt', 'r') as f:
    content = f.read()
    print(content)

# Reading line by line (memory efficient for large files)
with open('large_file.txt', 'r') as f:
    for line in f:
        process_line(line)
```

### 1.6.5 Installing Packages with pip

```bash
# Install a package
pip install numpy

# Install specific version
pip install numpy==1.19.0

# Upgrade package
pip install --upgrade numpy

# Uninstall package
pip uninstall numpy

# List installed packages
pip list

# Install from requirements file
pip install -r requirements.txt
```

---

## 1.7 Python Parallel Programming: Processes and Threads

### 1.7.1 The Global Interpreter Lock (GIL)

**GIL Mechanism:**

```
Python Thread 1 ──┐
Python Thread 2 ──┼── Global Interpreter Lock (GIL)
Python Thread 3 ──┘
         │
         ▼
Execute Python Bytecode
         │
         ▼
Release GIL
         │
         ▼
Next Thread Acquires GIL
```

**GIL Impact:**

| Operation Type | GIL Impact | Solution |
|----------------|------------|----------|
| CPU-bound | Severely limited | Use multiprocessing |
| I/O-bound | Minimal impact | Use threading or asyncio |
| C extensions | Release GIL | NumPy, SciPy operations |

### 1.7.2 Processes vs. Threads

**Process Memory:**

```
Process 1                    Process 2
Memory Space 1               Memory Space 2
├── Code                     ├── Code
├── Data                     ├── Data
├── Stack                    ├── Stack
└── Heap                     └── Heap
```

**Thread Memory:**

```
Process
├── Shared Memory (Code, Data, Heap)
├── Thread 1 Stack
├── Thread 2 Stack
└── Thread 3 Stack
```

### 1.7.3 Detailed Comparison

| Aspect | Process | Thread |
|--------|---------|--------|
| Memory | Separate address space | Shared address space |
| Creation | Expensive (fork/exec) | Cheap (fast context) |
| Communication | IPC (pipes, queues, shared memory) | Direct (shared variables) |
| Synchronization | Less critical | Critical (locks needed) |
| Crash impact | Other processes unaffected | Can crash entire process |
| Python GIL | No GIL contention | GIL contention |
| Overhead | High | Low |
| Use case | CPU-bound tasks | I/O-bound tasks |

### 1.7.4 Performance Comparison Example

**Task:** Append random numbers to lists (10M elements × 10 executions)

**do_something.py:**
```python
import random

def do_something(count, out_list):
    for i in range(count):
        out_list.append(random.random())
```

**Serial Implementation (serial_test.py):**
```python
from do_something import *
import time

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000
    n_exec = 10
    
    for i in range(n_exec):
        out_list = list()
        do_something(size, out_list)
    
    print(f"Serial time: {time.time() - start_time:.2f} seconds")
```

**Multithreading Implementation (multithreading_test.py):**
```python
from do_something import *
import time
import threading

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000
    threads = 10
    jobs = []
    
    for i in range(threads):
        out_list = list()
        thread = threading.Thread(target=do_something, 
                                  args=(size, out_list))
        jobs.append(thread)
    
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    
    print(f"Multithreading time: {time.time() - start_time:.2f} seconds")
```

**Multiprocessing Implementation (multiprocessing_test.py):**
```python
from do_something import *
import time
import multiprocessing

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000
    procs = 10
    jobs = []
    
    for i in range(procs):
        out_list = list()
        process = multiprocessing.Process(target=do_something,
                                          args=(size, out_list))
        jobs.append(process)
    
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    
    print(f"Multiprocessing time: {time.time() - start_time:.2f} seconds")
```

**Results (Intel i7 / 8GB RAM):**

| Implementation | Execution Time | Notes |
|----------------|----------------|-------|
| Serial | ~25.43 seconds | Baseline |
| Multithreading | ~26.17 seconds | Slightly slower due to GIL |
| Multiprocessing | ~18.93 seconds | ~25% faster |

### 1.7.5 When to Use What

```
Identify Task Type
        │
        ▼
   CPU-bound or I/O-bound?
        │
    ┌───┴───┐
    ▼       ▼
CPU-bound  I/O-bound
    │       │
    ▼       ▼
Use        Use
multipro-  threading
cessing    or asyncio
                │
                ▼
           I/O Pattern?
                │
        ┌───────┴───────┐
        ▼               ▼
    Network/File       Mixed
        │               │
        ▼               ▼
    asyncio           threading
(High concurrency)   (Simpler API)
```

### 1.7.6 Best Practices Summary

| Scenario | Recommended Approach |
|----------|---------------------|
| CPU-intensive calculations | multiprocessing or concurrent.futures.ProcessPoolExecutor |
| Many network connections | asyncio (for Python 3.5+) |
| I/O with low concurrency | threading |
| Data parallelism (arrays) | NumPy (uses C extensions) |
| GPU computing | CUDA/OpenCL via PyCUDA, Numba |
| Distributed computing | MPI via mpi4py |

---

## Chapter Summary

**Key Takeaways:**

1. Parallel computing is essential for modern performance
2. MIMD architecture dominates current systems
3. Memory organization affects programming complexity
4. Amdahl's Law reminds us that serial code limits scalability
5. Python's GIL makes multiprocessing preferable for CPU-bound tasks
6. Choose the right concurrency model based on your task type

---

## Exercises

1. **Identify the Architecture:** Classify your personal computer according to Flynn's Taxonomy and memory organization.

2. **Amdahl's Law Calculation:** If 80% of a program is parallelizable, what is the maximum speedup achievable on a 4-core processor?

3. **Code Analysis:** Modify the performance comparison example to use `multiprocessing.Pool` instead of creating individual processes.

4. **Research:** Investigate the difference between `fork` and `spawn` process creation methods on different operating systems.

5. **Practical:** Write a function that downloads 100 web pages concurrently using both `threading` and `asyncio`. Compare the performance.
