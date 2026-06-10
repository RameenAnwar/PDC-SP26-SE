# Distributed Computing with Celery, Pyro4, and Socket Programming

## Overview

This project introduces several important concepts used in distributed computing and network programming:

* Socket Programming
* Client-Server Communication
* File Transfer over Networks
* Remote Procedure Calls (RPC)
* Pyro4 Distributed Objects
* Celery Distributed Task Queues
* Asynchronous Task Execution
* Distributed Service Topologies

These technologies are commonly used in cloud computing, distributed applications, microservices, and enterprise systems.

---

# Project Structure

```text
├── addTask.py
├── addTask_main.py
│
├── pyro_server.py
├── pyro_client.py
│
├── chainTopology.py
├── client_chain.py
├── server_chain_1.py
├── server_chain_2.py
├── server_chain_3.py
│
├── server.py
├── client.py
│
├── server2.py
├── client2.py
```

---

# Requirements

## Python Libraries

Install required packages:

```bash
pip install celery
pip install pyamqp
pip install Pyro4
```

## Additional Software

### RabbitMQ

Celery examples require RabbitMQ running locally.

Default broker:

```text
amqp://guest@localhost//
```

or

```text
pyamqp://guest@localhost//
```

---

# Learning Objectives

After completing this chapter, students will be able to:

* Understand distributed systems architecture
* Implement client-server communication
* Transfer files through sockets
* Create remote objects using Pyro4
* Execute distributed tasks with Celery
* Design distributed service chains
* Understand RPC concepts

---

# Section 1: Celery Distributed Task Queue

---

## Files

```text
addTask.py
addTask_main.py
```

---

## Purpose

Demonstrates asynchronous task execution using Celery.

---

## addTask.py

Defines a Celery task:

```python
add(x, y)
```

Returns:

```text
x + y
```

---

## addTask_main.py

Submits the task asynchronously:

```python
add.delay(5,5)
```

Instead of executing immediately, the task is placed into a message queue.

---

## Workflow

```text
Client
   ↓
RabbitMQ Broker
   ↓
Celery Worker
   ↓
Result
```

---

## Learning Outcome

Understand task queues and asynchronous execution.

---

# Section 2: Pyro4 Remote Procedure Calls (RPC)

---

## Files

```text
pyro_server.py
pyro_client.py
```

---

## Purpose

Demonstrates Remote Procedure Calls using Pyro4.

---

## Server

Creates a remote object:

```python
welcomeMessage(name)
```

Returns:

```text
Hi welcome <name>
```

---

## Client

Connects to remote object:

```python
server = Pyro4.Proxy("PYRONAME:server")
```

Calls:

```python
server.welcomeMessage(name)
```

---

## Workflow

```text
Client
   ↓
Name Server
   ↓
Remote Object
   ↓
Response
```

---

## Learning Outcome

Understand distributed object communication.

---

# Section 3: Pyro4 Chain Topology

---

## Files

```text
chainTopology.py
client_chain.py
server_chain_1.py
server_chain_2.py
server_chain_3.py
```

---

## Purpose

Demonstrates communication among multiple distributed services.

---

## Topology

```text
Server 1
   ↓
Server 2
   ↓
Server 3
   ↓
Server 1
```

Circular topology.

---

## Workflow

1. Client sends request to Server 1.
2. Server 1 forwards to Server 2.
3. Server 2 forwards to Server 3.
4. Server 3 forwards back to Server 1.
5. Chain closes and response is returned.

---

## Learning Outcome

Understand distributed service routing and topology design.

---

# Section 4: Socket Programming

---

## Files

```text
server.py
client.py
```

---

## Purpose

Demonstrates basic TCP client-server communication.

---

## Server

* Creates socket
* Waits for connections
* Sends current time

---

## Client

* Connects to server
* Receives current time
* Displays response

---

## Workflow

```text
Client
   ↓
TCP Connection
   ↓
Server
   ↓
Current Time
```

---

## Sample Output

```text
Time connection server:
Mon Nov 20 15:30:01 2023
```

---

## Learning Outcome

Understand basic network communication using sockets.

---

# Section 5: File Transfer using Sockets

---

## Files

```text
server2.py
client2.py
```

---

## Purpose

Demonstrates file transfer between client and server.

---

## Server

1. Waits for client connection.
2. Opens file:

```text
mytext.txt
```

3. Sends file contents.

---

## Client

1. Connects to server.
2. Receives data.
3. Stores data in:

```text
received.txt
```

---

## Workflow

```text
Server
   ↓
Read File
   ↓
Socket Transfer
   ↓
Client
   ↓
Write File
```

---

## Learning Outcome

Understand network-based file transfer.

---

# Communication Models Covered

| Technology | Communication Type          |
| ---------- | --------------------------- |
| Socket     | Low-level TCP communication |
| Pyro4      | Remote Procedure Calls      |
| Celery     | Message Queue System        |

---

# Comparison of Technologies

| Feature             | Socket  | Pyro4   | Celery |
| ------------------- | ------- | ------- | ------ |
| Communication Level | Low     | High    | High   |
| Remote Functions    | No      | Yes     | Yes    |
| Message Queue       | No      | No      | Yes    |
| Distributed Objects | No      | Yes     | No     |
| Asynchronous Tasks  | Limited | Limited | Yes    |

---

# Running the Programs

---

## Celery

Start RabbitMQ.

Start Celery Worker:

```bash
celery -A addTask worker --loglevel=info
```

Run task:

```bash
python addTask_main.py
```

---

## Pyro4

Start Name Server:

```bash
python -m Pyro4.naming
```

Start Server:

```bash
python pyro_server.py
```

Run Client:

```bash
python pyro_client.py
```

---

## Chain Topology

Start Name Server:

```bash
python -m Pyro4.naming
```

Start servers:

```bash
python server_chain_1.py
python server_chain_2.py
python server_chain_3.py
```

Run client:

```bash
python client_chain.py
```

---

## Socket Communication

Start server:

```bash
python server.py
```

Run client:

```bash
python client.py
```

---

## File Transfer

Start file server:

```bash
python server2.py
```

Run client:

```bash
python client2.py
```

---

# Key Concepts Learned

This chapter introduces:

* Distributed Computing
* Client-Server Architecture
* TCP/IP Communication
* Socket Programming
* File Transfer Protocol Concepts
* Remote Procedure Calls (RPC)
* Distributed Objects
* Celery Task Queues
* RabbitMQ Messaging
* Service Discovery
* Distributed Topologies

---

# Real-World Applications

These technologies are used in:

* Cloud Platforms
* Web Services
* Distributed Databases
* Microservices
* Enterprise Systems
* Message Processing Systems
* File Sharing Applications
* Network Monitoring Tools

---

# Conclusion

This project provides practical exposure to several important distributed computing technologies. Through Celery, Pyro4, and Socket Programming, students learn how applications communicate across networks, execute tasks remotely, exchange files, and build scalable distributed systems.

These concepts form the foundation of modern cloud computing, service-oriented architectures, and large-scale distributed applications.
