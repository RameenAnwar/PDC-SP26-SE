# 🖧 Chapter 06 – Distributed Computing Experiments
📊 [View Visual Report](./distributed_computing_chapter06.html)
<br>
This repository contains practical experiments for **Chapter 06: Distributed Computing**, covering three major paradigms in Python:

| Paradigm | Description |
|---|---|
| **Pyro4** | Remote object invocation |
| **Celery** | Distributed async task queue |
| **Socket Programming** | Low-level TCP communication |

---

## 📦 Prerequisites

Install required Python packages:

```bash
pip install Pyro4 celery
```

For Celery, a message broker is needed. Use **RabbitMQ** or **Redis**:

```bash
# Redis
pip install redis

# Start Celery worker with Redis
celery -A addTask worker --loglevel=info --broker redis://localhost
```

> Socket experiments require **no extra packages**.

---

## 1️⃣ Pyro4 – Simple Server-Client

### Files
- `pyro_server.py` – Registers a remote object with the Pyro name server
- `pyro_client.py` – Looks up the object and calls its method

### How to Run

```bash
# Step 1: Start the Pyro Name Server
python -m Pyro4.naming

# Step 2: Start the server
python pyro_server.py

# Step 3: Run the client
python pyro_client.py
```

### Sample Output

```
# Name Server
NS running on localhost:9090 (127.0.0.1)
URI = PYRO:Pyro.NameServer@localhost:9090

# Server
Ready. Object uri = PYRO:obj_3908a1f7ca7546238bfb6ad879e148f0@localhost:59945

# Client
What is your name? Ahmed
Hi welcome Ahmed
```

> ✅ Client locates the server via the name server and invokes a remote method seamlessly.

---

## 2️⃣ Pyro4 – Chain of Servers

### Files
- `server_chain_1.py`, `server_chain_2.py`, `server_chain_3.py`
- `client_chain.py`

The servers form a **cyclic chain**: `Server 1 → Server 2 → Server 3 → Server 1`

### How to Run

```bash
# Start name server
python -m Pyro4.naming

# Start each server in separate terminals
python server_chain_1.py
python server_chain_2.py
python server_chain_3.py

# Run the client
python client_chain.py
```

### Sample Output

```
# Server 1
server_1 started
1 forwarding the message to the object 2
Back at 1; the chain is closed!

# Server 2
server_2 started
2 forwarding the message to the object 3

# Server 3
server_3 started
3 forwarding the message to the object 1

# Client
Result = ['passed on from 1', 'passed on from 2', 'passed on from 3', 'complete at 1']
```

> ✅ Messages propagate through the cyclic chain correctly, demonstrating complex distributed workflows.

---

## 3️⃣ Celery – Distributed Add Task

### Files
- `addTask.py` – Defines the Celery app and the `add` task
- `addTask_main.py` – Triggers the task asynchronously

### How to Run

```bash
# Step 1: Start the Celery worker
celery -A addTask worker --loglevel=info

# Step 2: Run the main script
python addTask_main.py
```

### Sample Output

```
[INFO/MainProcess] Connected to amqp://guest@localhost:5672//
[INFO/MainProcess] celery@hostname ready.
[INFO/MainProcess] Received task: addTask.add[abc123]
[INFO/MainProcess] Task addTask.add[abc123] succeeded in 0.001s: 10
```

> ✅ Worker processes `add(5, 5)` and returns `10` asynchronously.

---

## 4️⃣ Socket Programming

### 4.1 Time Client

**Files:** `server.py`, `client.py`

```bash
# Terminal 1
python server.py

# Terminal 2
python client.py
```

**Output:**
```
Time connection server: Wed Dec 24 03:19:37 2025
```

---

### 4.2 File Transfer

**Files:** `server2.py`, `client2.py`, `mytext.txt`

```bash
# Terminal 1
python server2.py

# Terminal 2
python client2.py
```

**Output:**
```
file opened
receiving data...
Data => hello!!!
Successfully get the file
connection closed
```

> ⚠️ Make sure `mytext.txt` exists in the same directory as `server2.py` before running.

---

## 📊 Results Summary

| Experiment | Status | Notes |
|---|---|---|
| Pyro4 Simple Client-Server | ✅ Working | Remote method invocation via name server |
| Pyro4 Chain of Servers | ✅ Working | Cyclic message passing across 3 servers |
| Celery Add Task | ✅ Working | Async task returns correct result |
| Socket Time Client | ✅ Working | TCP connection retrieves server time |
| Socket File Transfer | ⚠️ Fixed | Fails if `mytext.txt` is missing |

---

## 📁 File Structure

```
.
├── pyro_server.py        # Pyro4 simple server
├── pyro_client.py        # Pyro4 simple client
├── server_chain_1.py     # Pyro4 chain server 1
├── server_chain_2.py     # Pyro4 chain server 2
├── server_chain_3.py     # Pyro4 chain server 3
├── client_chain.py       # Pyro4 chain client
├── addTask.py            # Celery task definition
├── addTask_main.py       # Celery task runner
├── server.py             # Socket time server
├── client.py             # Socket time client
├── server2.py            # Socket file transfer server
├── client2.py            # Socket file transfer client
├── mytext.txt            # Sample file for transfer
└── received.txt          # Output file after transfer
```

---

## 🧠 Key Takeaways

- **Pyro4** provides high-level remote object semantics, ideal for object-oriented distributed systems.
- **Celery** offers robust async task queues, suitable for background job processing and microservices.
- **Socket programming** gives low-level control over TCP, essential for understanding network fundamentals.