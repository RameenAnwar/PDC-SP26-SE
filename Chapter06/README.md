# Chapter06 - Python Parallel Programming
# ⚡ Chapter 6 — Python Parallel Programming

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════╗
║          PARALLEL & DISTRIBUTED COMPUTING  ·  CHAPTER 6             ║
║    Remote Objects · Distributed Tasks · Chain Topology              ║
╚══════════════════════════════════════════════════════════════════════╝
```

![Python](https://img.shields.io/badge/Python-3.5%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pyro4](https://img.shields.io/badge/Pyro4-Remote_Objects-FF6B35?style=for-the-badge)
![Celery](https://img.shields.io/badge/Celery-Distributed_Tasks-00C896?style=for-the-badge)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-Message_Broker-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

> *"Distributed objects communicate across machines as if they were local — that's the power of remote object invocation."*

</div>

---

## 📌 Overview

This chapter covers **Python distributed programming** using two powerful frameworks:

- **Pyro4** (Python Remote Objects) — invoke methods on objects living on remote machines
- **Celery** — distribute tasks asynchronously across a worker pool via a message broker

Two practical examples are implemented:

| Example | Framework | Pattern |
|---|---|---|
| Welcome Server | Pyro4 | Basic Remote Object (client ↔ server) |
| Chain Topology | Pyro4 | Distributed Ring / Chain Pattern |
| Add Task | Celery + RabbitMQ | Asynchronous Distributed Task Queue |

---

## 🗂️ Project Structure

```
Chapter6/
│
├── 📁 pyro4_basic/
│   ├── pyro_server.py             # Pyro4 server — exposes welcomeMessage()
│   └── pyro_client.py             # Pyro4 client — calls remote method
│
├── 📁 chain_topology/
│   ├── chainTopology.py           # Chain class — core distributed object
│   ├── chainTopology_cpython-35.pyc  # Compiled bytecode (CPython 3.5)
│   ├── server_chain_1.py          # Node 1 → forwards to Node 2
│   ├── server_chain_2.py          # Node 2 → forwards to Node 3
│   ├── server_chain_3.py          # Node 3 → forwards back to Node 1
│   └── client_chain.py            # Initiates message into the ring
│
├── 📁 celery_tasks/
│   ├── addTask.py                 # Celery task definition: add(x, y)
│   └── addTask_main.py            # Sends task to the worker queue
│
└── README.md                      ← You are here
```

---

## 🎯 Learning Objectives

Upon completing this chapter, students will be able to:

- [ ] Understand **Remote Procedure Call (RPC)** concepts in Python
- [ ] Register and locate remote objects using the **Pyro4 Name Server**
- [ ] Build a **client-server** architecture with Pyro4
- [ ] Implement the **Chain Ring Topology** — a circular distributed pattern
- [ ] Define and dispatch **asynchronous distributed tasks** using Celery
- [ ] Configure a **RabbitMQ message broker** for task queuing
- [ ] Analyze message flow through a distributed ring of servers

---

## 🧠 Core Concepts

### 1. Pyro4 — Python Remote Objects

Pyro4 lets you call methods on Python objects running on **different machines or processes**, using the same syntax as local calls.

```
┌─────────────────────────────────────────────────────────────┐
│                    Pyro4 Architecture                       │
│                                                             │
│   Client             Name Server           Server          │
│   ──────             ───────────           ──────          │
│   Proxy("PYRONAME:server")                                  │
│      │  ──── lookup("server") ──►  URI                     │
│      │  ◄─────────────────── URI ──                        │
│      │                                                      │
│      └─────── direct call via URI ──────► daemon           │
│               ◄──────── return value ─────                 │
└─────────────────────────────────────────────────────────────┘
```

**Key components:**

| Component | Role |
|---|---|
| `Pyro4.Daemon` | Hosts registered objects and handles incoming calls |
| `Pyro4.locateNS()` | Finds the running Name Server |
| `ns.register(name, uri)` | Publishes object under a human-readable name |
| `Pyro4.Proxy("PYRONAME:…")` | Client-side stub that routes calls to the real object |
| `@Pyro4.expose` | Marks methods/classes as callable from remote clients |

---

### 2. Example A — Basic Pyro4 Server & Client

#### `pyro_server.py`
```python
import Pyro4

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        return ("Hi welcome " + str(name))

def startServer():
    server  = Server()
    daemon  = Pyro4.Daemon()          # create the Pyro daemon
    ns      = Pyro4.locateNS()        # find the name server
    uri     = daemon.register(server) # register the object
    ns.register("server", uri)        # publish under name "server"
    print("Ready. Object uri =", uri)
    daemon.requestLoop()              # start serving

if __name__ == "__main__":
    startServer()
```

#### `pyro_client.py`
```python
import Pyro4

name   = input("What is your name? ").strip()
server = Pyro4.Proxy("PYRONAME:server")   # lookup by name
print(server.welcomeMessage(name))        # remote method call
```

**How to run:**
```bash
# Terminal 1 — start Pyro4 Name Server
python -m Pyro4.naming

# Terminal 2 — start the server
python pyro_server.py

# Terminal 3 — run the client
python pyro_client.py
```

---

### 3. Example B — Chain Topology (Ring Pattern)

This example demonstrates a **distributed ring** where a message circulates through three Pyro4 server nodes, each forwarding it to the next, until it arrives back at the origin.

```
┌─────────────────────────────────────────────────────────────────┐
│                   Chain Ring Topology                           │
│                                                                 │
│         client_chain.py                                         │
│               │                                                 │
│               ▼                                                 │
│        ┌─────────────┐                                          │
│        │  Server  1  │ ──────────────────────────►             │
│        │  (Node 1)   │                             │            │
│        └─────────────┘                             │            │
│               ▲                             ┌─────────────┐    │
│               │                             │  Server  2  │    │
│               │                             │  (Node 2)   │    │
│        ┌─────────────┐                      └─────────────┘    │
│        │  Server  3  │ ◄──────────────────────────             │
│        │  (Node 3)   │                                          │
│        └─────────────┘                                          │
│                                                                 │
│  Message travels: 1 → 2 → 3 → 1  (ring closed)                 │
└─────────────────────────────────────────────────────────────────┘
```

#### `chainTopology.py` — The Core Distributed Object
```python
import Pyro4

@Pyro4.expose
class Chain(object):
    def __init__(self, name, current_server):
        self.name = name
        self.current_serverName = current_server
        self.current_server = None

    def process(self, message):
        # Lazy-connect to the next server in the chain
        if self.current_server is None:
            self.current_server = Pyro4.core.Proxy(
                "PYRONAME:example.chainTopology." + self.current_serverName
            )
        if self.name in message:
            # Message came back to origin — ring complete
            print("Back at %s; the chain is closed!" % self.name)
            return ["complete at " + self.name]
        else:
            print("%s forwarding to %s" % (self.name, self.current_serverName))
            message.append(self.name)
            result = self.current_server.process(message)
            result.insert(0, "passed on from " + self.name)
            return result
```

#### Server nodes — each is identical except for node IDs:

| File | Current Node | Next Node | Pyro Name |
|---|---|---|---|
| `server_chain_1.py` | `"1"` | `"2"` | `example.chainTopology.1` |
| `server_chain_2.py` | `"2"` | `"3"` | `example.chainTopology.2` |
| `server_chain_3.py` | `"3"` | `"1"` | `example.chainTopology.3` |

#### `client_chain.py` — Initiates the ring
```python
import Pyro4

obj = Pyro4.core.Proxy("PYRONAME:example.chainTopology.1")
print("Result=%s" % obj.process(["hello"]))
```

**How to run (5 terminals):**
```bash
# Terminal 1 — Pyro4 Name Server
python -m Pyro4.naming

# Terminal 2, 3, 4 — three chain nodes (any order)
python server_chain_1.py
python server_chain_2.py
python server_chain_3.py

# Terminal 5 — trigger the ring
python client_chain.py
```

**Expected output (across server terminals):**
```
# Server 1:
1 forwarding the message to the object 2

# Server 2:
2 forwarding the message to the object 3

# Server 3:
3 forwarding the message to the object 1

# Server 1 (again — ring closed):
Back at 1; the chain is closed!

# Client:
Result=['passed on from 1', 'passed on from 2', 'passed on from 3', 'complete at 1']
```

---

### 4. Example C — Celery Distributed Task Queue

Celery dispatches tasks to **worker processes** (potentially on different machines) via a **message broker** (RabbitMQ).

```
┌──────────────────────────────────────────────────────────────┐
│                 Celery Architecture                          │
│                                                              │
│  addTask_main.py                                             │
│       │                                                      │
│       │  add.delay(5, 5)                                     │
│       ▼                                                      │
│  ┌──────────┐    publish    ┌──────────────┐                 │
│  │  Client  │ ────────────► │   RabbitMQ   │                 │
│  │  (main)  │               │   (broker)   │                 │
│  └──────────┘               └──────────────┘                 │
│                                    │  consume                │
│                                    ▼                         │
│                             ┌──────────────┐                 │
│                             │ Celery Worker│                 │
│                             │  add(5, 5)   │                 │
│                             │  → result 10 │                 │
│                             └──────────────┘                 │
└──────────────────────────────────────────────────────────────┘
```

#### `addTask.py` — Task Definition
```python
from celery import Celery

app = Celery('addTask', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
```

#### `addTask_main.py` — Send Task Asynchronously
```python
import addTask

if __name__ == '__main__':
    result = addTask.add.delay(5, 5)
    # result is an AsyncResult object
    # call result.get() to block and retrieve the value
```

**How to run:**
```bash
# Step 1 — Install & start RabbitMQ
# Linux:
sudo apt-get install rabbitmq-server
sudo systemctl start rabbitmq-server

# macOS:
brew install rabbitmq
brew services start rabbitmq

# Step 2 — Install Celery
pip install celery

# Step 3 — Start the Celery worker (in Chapter6 directory)
celery -A addTask worker --loglevel=info

# Step 4 — Send the task
python addTask_main.py
```

---

## ⚙️ Installation

### Prerequisites

```bash
python --version       # Python 3.5+ required
pip install Pyro4      # Remote object framework
pip install celery     # Distributed task queue
```

### Full `requirements.txt`
```
Pyro4>=4.82
serpent>=1.40          # Pyro4 serialization dependency
celery>=5.3.0
amqp>=5.1.0
```

```bash
pip install -r requirements.txt
```

---

## 🔁 Message Flow Diagrams

### Chain Topology — Step by Step

```
client_chain.py
   │
   └─► Node 1.process(["hello"])
             │  "1" not in message → append "1" → forward
             └─► Node 2.process(["hello", "1"])
                       │  "2" not in message → append "2" → forward
                       └─► Node 3.process(["hello", "1", "2"])
                                 │  "3" not in message → append "3" → forward
                                 └─► Node 1.process(["hello", "1", "2", "3"])
                                           │  "1" IS in message → RING CLOSED
                                           └─► return ["complete at 1"]
                                 ◄── ["complete at 1"]
                                 insert → ["passed on from 3", "complete at 1"]
                       ◄── ["passed on from 3", "complete at 1"]
                       insert → ["passed on from 2", "passed on from 3", "complete at 1"]
             ◄── ["passed on from 2", ...]
             insert → ["passed on from 1", "passed on from 2", "passed on from 3", "complete at 1"]
   ◄── Final Result
```

---

## ⚠️ Common Issues & Fixes

| Problem | Cause | Fix |
|---|---|---|
| `NamingError: unknown name` | Name Server not running | Run `python -m Pyro4.naming` first |
| `ConnectionRefusedError` | Server not started | Start all server nodes before client |
| Celery worker idle | RabbitMQ not running | Start RabbitMQ service |
| `ImportError: No module named Pyro4` | Package missing | `pip install Pyro4` |
| Ring never closes | Wrong next_server IDs | Verify `1→2→3→1` chain in server files |
| `.pyc` file mismatch | CPython 3.5 bytecode | Regenerate with `python -m compileall chainTopology.py` |

---

## 📚 References

| Resource | Link |
|---|---|
| Pyro4 Documentation | https://pyro4.readthedocs.io |
| Celery Documentation | https://docs.celeryq.dev |
| RabbitMQ Getting Started | https://www.rabbitmq.com/getstarted.html |
| *Python Parallel Programming Cookbook* | Giancarlo Zaccone, Packt |

---

## 🏗️ Course Context

```
Parallel & Distributed Computing
│
├── Chapter 1  — Introduction to Parallel Computing
├── Chapter 2  — Parallel Architectures & Hardware
├── Chapter 3  — Distributed Systems Fundamentals
├── Chapter 4  — Message Passing Interface (MPI)
├── Chapter 5  — OpenMP & Shared Memory Parallelism
├── Chapter 6  — Python Parallel Programming  ◄ YOU ARE HERE
│               ├── Pyro4 Remote Objects
│               ├── Chain Ring Topology
│               └── Celery Distributed Tasks
├── Chapter 7  — GPU Computing with CUDA
└── Chapter 8  — Cloud & Large-Scale Distributed Systems
```

---

## 👨‍💻 Course Info

| Field | Details |
|---|---|
| **Course** | Parallel & Distributed Computing |
| **Chapter** | 6 — Python Parallel Programming |
| **Frameworks** | Pyro4 · Celery · RabbitMQ |
| **Python** | 3.5+ (bytecode: CPython 3.5) |
| **Pattern** | Remote Object Invocation · Chain Ring Topology · Task Queue |

---

<div align="center">

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Chapter 6  ·  Python Parallel Programming
  Pyro4 Remote Objects  ·  Celery Task Queue
  Parallel & Distributed Computing Course
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

*Three servers. One ring. Zero shared memory.*

</div>
