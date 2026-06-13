# Chapter 06: Distributed Task Queues and Remote Object Communication

## Preface

Welcome to the academic documentation for Chapter 06 of the Parallel and Distributed Computing (PDC) course. This final chapter explores distributed application architectures, where work is delegated across independent services and machines. 

We cover three distributed computing approaches: **Celery** for asynchronous distributed task queues, **Pyro5** for transparent remote object invocation, and **Socket Programming** for low-level network communication. Together, these form the foundation of real-world distributed system design.

---

## Index of Topics

### Section 1: Distributed Systems Theory
1. [The Distributed Application Model](#1-the-distributed-application-model)
2. [Asynchronous Task Queues with Celery](#2-asynchronous-task-queues-with-celery)
    - [Brokers and Workers](#brokers-and-workers)
    - [Task Routing and Result Backends](#task-routing-and-result-backends)
3. [Remote Procedure Calls with Pyro5](#3-remote-procedure-calls-with-pyro5)
    - [The Name Server](#the-name-server)
    - [Chain Topology Pattern](#chain-topology-pattern)
4. [Socket-Level Communication](#4-socket-level-communication)
    - [TCP Sockets and Connection Lifecycle](#tcp-sockets-and-connection-lifecycle)
    - [File Transfer over Sockets](#file-transfer-over-sockets)

### Section 2: Code Implementations
5. [Celery Task Definition and Dispatch](#5-celery-task-definition-and-dispatch)
6. [Pyro5 Basic Client-Server Communication](#6-pyro5-basic-client-server-communication)
7. [Pyro5 Chained Topology](#7-pyro5-chained-topology)
8. [Socket Server and Client](#8-socket-server-and-client)
9. [File Transfer via Sockets](#9-file-transfer-via-sockets)
10. [Local Execution Guide](#10-local-execution-guide)

---

# SECTION 1: DISTRIBUTED SYSTEMS THEORY

## 1. The Distributed Application Model

In a distributed system, components run on physically separate machines and communicate over a network. Unlike shared-memory systems (threads) or isolated-memory systems (multiprocessing on one machine), distributed architectures must handle:

- **Network Latency:** Data transfer over TCP/IP introduces milliseconds of delay compared to nanoseconds for memory access.
- **Partial Failures:** A remote service may crash independently without affecting the caller — unless handled explicitly.
- **Serialization:** All data exchanged between services must be converted into a transmittable byte format and reconstructed by the receiver.

Distributed patterns like task queues, remote procedure calls, and socket servers each solve different classes of these problems.

## 2. Asynchronous Task Queues with Celery

Celery is a production-grade distributed task queue framework for Python. It decouples the submission of work from its execution, allowing applications to offload long-running or CPU-intensive tasks to a pool of background worker processes.

### Brokers and Workers

The architecture consists of three roles:
- **Producer:** The application that creates and submits task messages.
- **Broker:** A message queue service (such as RabbitMQ, Redis, or SQLite) that stores submitted tasks until a worker picks them up.
- **Worker:** An independent Celery process that polls the broker, executes tasks, and stores results in a result backend.

This separation allows workers to be scaled horizontally — simply run more worker processes to handle higher throughput.

### Task Routing and Result Backends

Tasks are defined as decorated Python functions using `@app.task`. When a producer calls `.delay()` or `.apply_async()` on a task, a serialized message is placed on the broker queue. Workers pick up these messages asynchronously and store results in the configured backend (database, cache, or memory).

## 3. Remote Procedure Calls with Pyro5

Pyro5 (Python Remote Objects) enables a client application to call methods on an object that lives in a completely separate process or machine, as if it were a local object. The network communication is handled transparently by the Pyro5 runtime.

### The Name Server

Pyro5 includes a Name Server, a lightweight directory service that maps human-readable names to network addresses. Servers register their objects with a name like `example.server`, and clients look up the URI from the Name Server at runtime. This eliminates hardcoded IP address dependencies.

### Chain Topology Pattern

A chain topology is a distributed design pattern where multiple servers are linked sequentially. A client sends a request to the first server in the chain, which processes it and forwards it to the next server, and so on. The final server returns the result back through the chain. This is useful for pipeline processing workflows.

## 4. Socket-Level Communication

Python's `socket` module provides direct access to the operating system's TCP/IP networking stack, enabling the lowest-level form of network communication available.

### TCP Sockets and Connection Lifecycle

A TCP connection follows this lifecycle:
1. The **server** binds to a local IP address and port, then listens for incoming connections.
2. The **client** initiates a connection using the server's address and port.
3. After the three-way handshake, a bidirectional data channel is established.
4. Both sides can send and receive byte streams until one closes the connection.

### File Transfer over Sockets

Sockets can transfer arbitrary binary data, including file contents. The sender reads the file in chunks and transmits each chunk over the socket. The receiver writes each received chunk to a local output file, reconstructing the original content.

---

# SECTION 2: CODE IMPLEMENTATIONS

## 5. Celery Task Definition and Dispatch

**Script name:** `Celery/addTask.py` (task definition) and `Celery/addTask_main.py` (dispatcher)

The task is defined with the `@app.task` decorator and uses a local SQLite-backed broker for zero-dependency operation on Windows.

```python
# addTask.py
from celery import Celery

app = Celery('tasks',
             broker='sqla+sqlite:///celerydb.sqlite',
             backend='db+sqlite:///results.sqlite')

@app.task
def add(x, y):
    return x + y
```

```python
# addTask_main.py
from addTask import add

if __name__ == '__main__':
    result = add.delay(4, 6)
    print('Task submitted. Result:', result.get(timeout=10))
```

**Expected Console Output:**
```text
Task submitted. Result: 10
```

The worker processes the addition asynchronously and returns the result through the SQLite result backend.

---

## 6. Pyro5 Basic Client-Server Communication

**Script names:** `Pyro4/First Example/pyro_server.py` and `pyro_client.py`

The server registers a Python object with the Pyro5 daemon, making its methods remotely callable. The client locates and invokes those methods through the Pyro5 proxy.

```python
# pyro_server.py
import Pyro5.api

@Pyro5.api.expose
class GreetingMaker:
    def get_fortune(self, name):
        return f"Hello, {name}! Distributed greetings from Pyro5."

daemon = Pyro5.api.Daemon()
ns = Pyro5.api.locate_ns()
uri = daemon.register(GreetingMaker)
ns.register("example.greeting", uri)
print("Server ready.")
daemon.requestLoop()
```

```python
# pyro_client.py
import Pyro5.api

ns = Pyro5.api.locate_ns()
uri = ns.lookup("example.greeting")
with Pyro5.api.Proxy(uri) as greeting_maker:
    print(greeting_maker.get_fortune("Wasay"))
```

**Expected Console Output (client):**
```text
Hello, Wasay! Distributed greetings from Pyro5.
```

---

## 7. Pyro5 Chained Topology

**Script names:** `Pyro4/Second Example/chainTopology.py`, `server_chain_1.py`, `server_chain_2.py`, `server_chain_3.py`, `client_chain.py`

The chain topology connects three Pyro5 servers in sequence. The client sends a message to `server_chain_1`, which forwards it to `server_chain_2`, which forwards it to `server_chain_3`. Each server appends its identity to the message before forwarding.

```python
# chainTopology.py
import Pyro5.api

@Pyro5.api.expose
class Chain:
    def __init__(self, name, next_uri=None):
        self.name = name
        self.next_uri = next_uri

    def process(self, message):
        message.append(self.name)
        if self.next_uri:
            with Pyro5.api.Proxy(self.next_uri) as next_node:
                return next_node.process(message)
        return message
```

**Expected Console Output (client):**
```text
Result chain: ['server_chain_1', 'server_chain_2', 'server_chain_3']
```

---

## 8. Socket Server and Client

**Script names:** `socket/server.py` and `socket/client.py`

A basic TCP echo-style exchange between two Python processes on the same machine using `localhost`.

```python
# server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 10000))
server_socket.listen(1)
print("Server listening on port 10000...")

connection, address = server_socket.accept()
print(f"Connected from: {address}")

while True:
    data = connection.recv(1024)
    if not data:
        break
    print(f"Received: {data.decode()}")
    connection.sendall(data)

connection.close()
```

```python
# client.py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 10000))
client_socket.sendall(b'Hello from client')
data = client_socket.recv(1024)
print(f"Received back: {data.decode()}")
client_socket.close()
```

**Expected Console Output (client):**
```text
Received back: Hello from client
```

---

## 9. File Transfer via Sockets

**Script names:** `socket/server2.py` and `socket/client2.py`

This pair demonstrates binary file transfer using raw TCP sockets. The client reads a local text file and transmits its contents as a byte stream. The server receives the bytes and writes them to a new output file.

```python
# client2.py
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 60000))
    with open('mytext.txt', 'rb') as f:
        data = f.read(1024)
        while data:
            s.sendall(data)
            data = f.read(1024)
print("File sent successfully.")
```

```python
# server2.py
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 60000))
    s.listen(1)
    conn, addr = s.accept()
    with conn, open('received.txt', 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
print("File received and saved.")
```

**Expected Console Output:**
```text
# Server terminal:
File received and saved.

# Client terminal:
File sent successfully.
```

---

## 10. Local Execution Guide

Each sub-section requires running multiple terminal windows simultaneously. Follow the sequence below:

### Celery Setup
```bash
# Terminal 1 - Start the Celery worker:
cd Chapter06/code/Celery
celery -A addTask worker --loglevel=info

# Terminal 2 - Dispatch tasks:
python addTask_main.py
```

### Pyro5 First Example
```bash
# Terminal 1 - Start the Pyro5 Name Server:
python -m Pyro5.nameserver

# Terminal 2 - Start the server:
cd Chapter06/code/Pyro4/First\ Example
python pyro_server.py

# Terminal 3 - Run the client:
python pyro_client.py
```

### Pyro5 Chain Topology
```bash
# Terminal 1 - Name Server:
python -m Pyro5.nameserver

# Terminals 2, 3, 4 - Start each chain server:
python server_chain_1.py
python server_chain_2.py
python server_chain_3.py

# Terminal 5 - Run the client:
python client_chain.py
```

### Socket Communication
```bash
# Terminal 1 - Start the socket server:
python server.py

# Terminal 2 - Run the client:
python client.py
```

### File Transfer
```bash
# Terminal 1 - Start the file server:
python server2.py

# Terminal 2 - Send the file:
python client2.py
```
