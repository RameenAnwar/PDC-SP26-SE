# Parallel & Distributed Computing (PDC)
## Chapter 06: Distributed Task Queues and Remote Object Communication

## Course & Submission Details
- **Course Title:** Parallel and Distributed Computing (PDC)
- **Student Name:** Zaid Bhatti
- **Roll Number:** 23FA-014-SE
- **Chapter Focus:** Distributed Task Queues (Celery), Remote Objects (Pyro5), and Sockets

---

## 1. Overview of Distributed Architectures

Distributed systems consist of independent software components running on separate machines that coordinate their actions by passing messages over a network. This chapter explores three common distributed computing patterns: **Celery** for distributed task queues, **Pyro5** for remote procedure calls, and low-level **Socket Programming** for direct byte-level network communication.

---

## 2. Technical Discussion & Architectural Foundations

### Asynchronous Task Queues (Celery)
Celery is a task queue framework that decouples task submission from execution. This allows applications to run long-running or CPU-intensive tasks asynchronously in the background.
- **Producer:** The client application that submits tasks.
- **Broker:** A message queue service (e.g., Redis, RabbitMQ, or SQLite) that stores task messages.
- **Worker:** An independent process that polls the broker, runs the tasks, and writes results to a backend.

### Remote Object Invocation (Pyro5)
Pyro5 (Python Remote Objects) allows an application to invoke methods on a Python object that lives in a completely different process or machine, as if it were a local object.
- **Name Server:** A directory service that maps human-readable names to network URIs, allowing dynamic lookup.
- **Chain Topology:** A pattern where servers are linked in a pipeline. A request passes sequentially through the servers, each adding its contribution before returning the final result to the client.

### Socket-Level Communication
The `socket` module provides direct access to the operating system's TCP/IP networking stack. Sockets handle data transmission at the byte level, requiring explicit serialization, buffering, and protocol handling.

---

## 3. Practical Implementation Analysis

### Celery Task Queue Setup
The task is defined using Celery's `@app.task` decorator. We configure a local SQLite database broker to run on Windows without external service dependencies.

**Task Definition (`Celery/addTask.py`):**
```python
from celery import Celery

app = Celery('tasks',
             broker='sqla+sqlite:///celerydb.sqlite',
             backend='db+sqlite:///results.sqlite')

@app.task
def add(x, y):
    return x + y
```

**Task Dispatcher (`Celery/addTask_main.py`):**
```python
from addTask import add

if __name__ == '__main__':
    result = add.delay(4, 6)
    print('Task submitted. Result:', result.get(timeout=10))
```

---

### Pyro5 Basic Communication
The server registers a Python object with a Pyro5 daemon, registering its URI with the Name Server. The client queries the Name Server to obtain a proxy object and call its methods remotely.

**Server (`Pyro4/First Example/pyro_server.py`):**
```python
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

**Client (`Pyro4/First Example/pyro_client.py`):**
```python
import Pyro5.api

ns = Pyro5.api.locate_ns()
uri = ns.lookup("example.greeting")
with Pyro5.api.Proxy(uri) as greeting_maker:
    print(greeting_maker.get_fortune("Zaid"))
```

---

### Pyro5 Chain Topology
Three separate servers are connected in a chain configuration. The client calls `server_chain_1`, which forwards the call to `server_chain_2`, which in turn calls `server_chain_3`. Each server appends its name to a message list.

**Common Class (`Pyro4/Second Example/chainTopology.py`):**
```python
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

---

### Socket Connection Echo
Demonstrates basic TCP communication using standard IP addresses and ports to transfer strings between client and server.

**Server (`socket/server.py`):**
```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 10000))
server_socket.listen(1)
print("Server listening...")

connection, address = server_socket.accept()
while True:
    data = connection.recv(1024)
    if not data:
        break
    connection.sendall(data)
connection.close()
```

---

### File Transfer over Sockets
The client reads a text file and transmits its bytes over a TCP connection. The server receives the bytes and writes them to a new output file.

**Client (`socket/client2.py`):**
```python
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 60000))
    with open('mytext.txt', 'rb') as f:
        data = f.read(1024)
        while data:
            s.sendall(data)
            data = f.read(1024)
```

**Server (`socket/server2.py`):**
```python
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
```

---

## 4. Local Execution Guide

Distributed applications require multiple terminal sessions to run concurrently:

### Celery Execution
```bash
# Terminal 1 - Start the worker daemon
celery -A addTask worker --loglevel=info

# Terminal 2 - Run the submit script
python addTask_main.py
```

### Pyro5 Name Server and Objects
```bash
# Terminal 1 - Start the name server
python -m Pyro5.nameserver

# Terminal 2 - Start the object server
python pyro_server.py

# Terminal 3 - Run the client proxy
python pyro_client.py
```

### Socket and File Transfer
```bash
# Terminal 1 - Run the server listener
python server.py

# Terminal 2 - Execute the client sender
python client.py
```
