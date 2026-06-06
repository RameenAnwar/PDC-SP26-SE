# README – Chapter 06

# Python Parallel Programming Cookbook (Distributed Computing & Remote Execution)

This chapter focuses on **Distributed Computing**, where programs communicate across machines using **Sockets, Pyro4 (Python Remote Objects), and Celery**. These technologies allow applications to execute tasks remotely and build scalable distributed systems.

---

## Chapter 06 Roadmap

```mermaid
graph TD

A[Distributed Computing]

A --> B[Sockets]
A --> C[Pyro4]
A --> D[Celery]

B --> E[client.py]
B --> F[server.py]
B --> G[client2.py]
B --> H[server2.py]
B --> I[addTask.py]
B --> J[addTask_main.py]

C --> K[pyro_server.py]
C --> L[pyro_client.py]
C --> M[chainTopology.py]
C --> N[server_chain_1.py]
C --> O[server_chain_2.py]
C --> P[server_chain_3.py]
C --> Q[client_chain.py]

D --> R[addTask.py]
D --> S[addTask_main.py]
```

---

# SOCKET PROGRAMMING

## Socket Communication Architecture

```mermaid
flowchart LR

Client -->|Request| Server
Server -->|Response| Client
```

---

# client.py

## Overview

Demonstrates a basic socket client.

## Architecture

```mermaid
flowchart LR
Client --> Server
```

## What I Learned

* Creating socket clients
* Connecting to remote servers
* Sending requests

## What This Program Does

1. Creates socket
2. Connects to server
3. Sends message
4. Receives response

## How to Execute

```bash
python client.py
```

## Summary

Shows how a client connects to a socket server.

---

# server.py

## Architecture

```mermaid
flowchart TD

Server --> WaitConnection

WaitConnection --> AcceptClient

AcceptClient --> ProcessRequest

ProcessRequest --> SendResponse
```

## Overview

Demonstrates a basic socket server.

## What I Learned

* Binding sockets
* Listening for clients
* Accepting connections

## Summary

Shows how a socket server handles incoming requests.

---

# client2.py

## Architecture

```mermaid
flowchart LR

Client2 --> FileTransfer
```

## Overview

Advanced socket client implementation.

## What I Learned

* File transfer operations
* Data streaming

## Summary

Demonstrates transferring larger data through sockets.

---

# server2.py

## Architecture

```mermaid
flowchart TD

Client --> Server

Server --> ReceiveFile

ReceiveFile --> SaveFile
```

## Overview

Advanced socket server handling file transfer.

## What I Learned

* Receiving files
* Saving transmitted data

## Summary

Shows server-side file transfer implementation.

---

# addTask.py (Socket)

## Architecture

```mermaid
flowchart LR

Client --> AdditionRequest

AdditionRequest --> Server

Server --> Result
```

## Overview

Remote addition service using sockets.

## What I Learned

* Remote procedure execution
* Data serialization

## Summary

Shows distributed arithmetic processing.

---

# addTask_main.py (Socket)

## Overview

Main controller for remote addition task.

## Summary

Executes remote socket addition service.

---

# PYRO4 (Python Remote Objects)

## Pyro4 Architecture

```mermaid
flowchart LR

Client --> NameServer

NameServer --> RemoteObject

RemoteObject --> Response

Response --> Client
```

---

# pyro_server.py

## Architecture

```mermaid
flowchart TD

PyroServer --> RegisterObject

RegisterObject --> WaitClients
```

## Overview

Creates a Pyro4 server.

## What I Learned

* Remote object registration
* Pyro daemon

## Summary

Hosts remote Python objects.

---

# pyro_client.py

## Architecture

```mermaid
flowchart LR

Client --> RemoteObject

RemoteObject --> Result
```

## Overview

Accesses remote Pyro objects.

## What I Learned

* Remote method invocation
* Object proxies

## Summary

Demonstrates calling remote methods.

---

# chainTopology.py

## Architecture

```mermaid
flowchart LR

Server1 --> Server2

Server2 --> Server3
```

## Overview

Defines chain communication topology.

## What I Learned

* Distributed service chaining
* Message forwarding

## Summary

Creates a linked service architecture.

---

# server_chain_1.py

## Architecture

```mermaid
flowchart LR

Client --> Server1

Server1 --> Server2
```

## Overview

First node in Pyro chain.

## Summary

Receives and forwards requests.

---

# server_chain_2.py

## Architecture

```mermaid
flowchart LR

Server1 --> Server2

Server2 --> Server3
```

## Overview

Middle node in chain topology.

## Summary

Processes and forwards requests.

---

# server_chain_3.py

## Architecture

```mermaid
flowchart LR

Server2 --> Server3

Server3 --> Response
```

## Overview

Final node in chain.

## Summary

Generates final output.

---

# client_chain.py

## Architecture

```mermaid
flowchart LR

Client --> Server1

Server1 --> Server2

Server2 --> Server3

Server3 --> Client
```

## Overview

Client for chain topology.

## What I Learned

* Multi-hop communication

## Summary

Shows end-to-end distributed execution.

---

# CELERY DISTRIBUTED TASK QUEUE

## Celery Architecture

```mermaid
flowchart TD

Application --> Broker

Broker --> Worker1
Broker --> Worker2
Broker --> Worker3

Worker1 --> Results
Worker2 --> Results
Worker3 --> Results
```

---

# addTask.py (Celery)

## Overview

Defines Celery asynchronous task.

## What I Learned

* Celery tasks
* Delayed execution

## What This Program Does

1. Defines task
2. Registers with Celery
3. Waits for execution

## Summary

Shows asynchronous task definition.

---

# addTask_main.py (Celery)

## Architecture

```mermaid
flowchart LR

User --> CeleryTask

CeleryTask --> Broker

Broker --> Worker

Worker --> Result
```

## Overview

Submits Celery task for execution.

## What I Learned

* Task scheduling
* Worker processing

## Summary

Demonstrates distributed task execution.

---

# Distributed Communication Comparison

```mermaid
graph LR

Socket --> DirectConnection

Pyro4 --> RemoteObjects

Celery --> TaskQueue
```

---

# Chapter Components Distribution

```mermaid
pie title Chapter 06 Technologies

"Socket Programming" : 45
"Pyro4" : 35
"Celery" : 20
```

---

# Distributed Request Flow

```mermaid
flowchart LR

Client --> Network

Network --> Service

Service --> Result

Result --> Client
```

---

# Technology Comparison

| Technology | Communication Style  | Best For                |
| ---------- | -------------------- | ----------------------- |
| Socket     | Low-level networking | Custom protocols        |
| Pyro4      | Remote Objects       | Distributed Python apps |
| Celery     | Task Queues          | Background processing   |

---

# Evolution of Parallel Computing

```mermaid
graph LR

Threads --> Multiprocessing

Multiprocessing --> MPI

MPI --> AsyncIO

AsyncIO --> DistributedSystems
```

---

# FINAL CHAPTER SUMMARY

## Key Concepts Learned

* Socket Programming
* Client-Server Communication
* File Transfer
* Pyro4 Remote Objects
* Distributed Service Chaining
* Celery Task Queues
* Asynchronous Distributed Processing

---

## Overall Understanding

Chapter 06 introduces **Distributed Computing Technologies** in Python.

The examples demonstrate:

* Network communication using sockets
* Remote method invocation with Pyro4
* Distributed service topologies
* Asynchronous task execution with Celery
* Building scalable distributed systems

These technologies are commonly used in:

* Microservices
* Cloud Computing
* Distributed Systems
* Background Job Processing
* Enterprise Applications
* Network Services

---

## Learning Journey

```mermaid
graph LR

Chapter2[Threads]
--> Chapter3[Multiprocessing]

Chapter3
--> Chapter4[MPI]

Chapter4
--> Chapter5[AsyncIO]

Chapter5
--> Chapter6[Distributed Computing]
```

**Chapter 06 completes the journey from local parallelism to fully distributed computing systems.**
