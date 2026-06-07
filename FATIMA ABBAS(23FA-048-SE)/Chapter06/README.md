# Chapter 06 – Distributed Computing and Network Communication in Python
## Chapter Overview

This chapter introduces different approaches for distributed computing and network communication in Python.

The chapter demonstrates:

- Socket Programming
- Client-Server Communication
- Remote Procedure Calls using Pyro4
- Distributed Task Execution using Celery

---

## Chapter Architecture

```mermaid
graph TD

A[Distributed Computing]

A --> B[Socket Programming]
A --> C[Pyro4]
A --> D[Celery]

B --> E[Client Server Communication]
C --> F[Remote Object Invocation]
D --> G[Distributed Task Queue]
```

---

## Project Structure

```text
Chapter06/
│
├── Celery/
├── Pyro4/
└── Socket/
```

---

# 1. Socket Programming

## Definition

Socket programming enables communication between two computers or processes over a network.

One program acts as a Server and another acts as a Client.

---

## Communication Flow

```mermaid
sequenceDiagram

participant Client
participant Server

Client->>Server: Connection Request
Server->>Client: Accept Connection
Client->>Server: Send Request
Server->>Client: Send Response
Client->>Server: Close Connection
```

---

## Working Process

```mermaid
flowchart TD

A[Create Socket]
B[Bind Address]
C[Listen]
D[Accept Client]
E[Send Data]
F[Close Connection]

A --> B --> C --> D --> E --> F
```

### Advantages

- Easy network communication
- Supports distributed applications
- Fast data exchange

### Disadvantages

- Connection management required
- Error handling can be complex

---

# 2. Pyro4 (Python Remote Objects)

## Definition

Pyro4 allows a Python program to call methods on an object running in another process or machine.

It works similarly to calling local functions, but the execution happens remotely.

---

## Pyro4 Architecture

```mermaid
graph LR

A[Client]

A --> B[Pyro Name Server]

B --> C[Remote Object Server]

C --> D[Execute Method]

D --> A
```

---

## First Example

### Objective

Create a remote server that provides a welcome message and allow clients to invoke it remotely.

### Workflow

```mermaid
flowchart TD

A[Start Name Server]
B[Start Pyro Server]
C[Register Object]
D[Client Lookup]
E[Remote Method Call]
F[Return Result]

A --> B --> C --> D --> E --> F
```

### Advantages

- Simple remote communication
- Object-oriented design
- Easy implementation

### Disadvantages

- Requires Name Server
- Network dependency

---

# 3. Chain Topology using Pyro4

## Definition

Multiple servers are connected in sequence where requests travel through a chain of remote objects.

---

## Architecture

```mermaid
graph LR

A[Client]

A --> B[Server 1]
B --> C[Server 2]
C --> D[Server 3]

D --> E[Result]
```

---

## Workflow

```mermaid
flowchart TD

A[Client Request]
B[Server 1]
C[Server 2]
D[Server 3]
E[Return Final Response]

A --> B --> C --> D --> E
```

### Applications

- Distributed Systems
- Service Chaining
- Microservices Architecture
- Multi-layer Processing

---

# 4. Celery Distributed Tasks

## Definition

Celery is a distributed task queue used for executing background jobs asynchronously.

Instead of waiting for a task to complete, the task is sent to a worker process.

---

## Celery Architecture

```mermaid
graph LR

A[Application]

A --> B[Message Broker]

B --> C[Celery Worker]

C --> D[Execute Task]

D --> E[Return Result]
```

---

## Task Execution Flow

```mermaid
flowchart TD

A[Create Task]
B[Send to Broker]
C[Worker Receives Task]
D[Execute Task]
E[Store Result]

A --> B --> C --> D --> E
```

### Advantages

- Background processing
- Scalable architecture
- Distributed execution
- Improved performance

### Disadvantages

- Additional setup required
- Requires broker service

---

# Comparison

| Feature | Socket | Pyro4 | Celery |
|----------|---------|--------|---------|
| Communication | Low-Level | Remote Objects | Task Queue |
| Complexity | High | Medium | Medium |
| Scalability | Moderate | Good | Excellent |
| Asynchronous | Limited | Possible | Yes |
| Distributed Support | Yes | Yes | Yes |
| Best Use Case | Networking | Remote Method Calls | Background Tasks |

---

# Distributed Computing Model

```mermaid
graph TD

A[Client Application]

A --> B[Socket Server]
A --> C[Pyro4 Server]
A --> D[Celery Worker]

B --> E[Network Communication]
C --> F[Remote Objects]
D --> G[Background Tasks]
```

---

# Learning Outcomes

After completing this chapter, you will be able to:

- Understand distributed computing concepts.
- Build client-server applications using sockets.
- Implement remote method invocation using Pyro4.
- Create chain topology architectures.
- Execute asynchronous tasks using Celery.
- Understand message brokers and workers.
- Design scalable distributed systems.

---

# Requirements

```bash
pip install Pyro4
pip install celery
```

---

# Running Examples

## Socket Server

```bash
python server.py
```

## Socket Client

```bash
python client.py
```

## Pyro4 Name Server

```bash
python -m Pyro4.naming
```

## Pyro4 Server

```bash
python pyro_server.py
```

## Pyro4 Client

```bash
python pyro_client.py
```

## Celery Worker

```bash
celery -A addTask worker --loglevel=info
```

## Execute Task

```bash
python addTask_main.py
```

---

# Final Summary

- Socket Programming provides the foundation of network communication.
- Pyro4 enables remote method invocation and distributed object-oriented programming.
- Celery simplifies asynchronous and distributed task execution.
- Distributed computing improves scalability, responsiveness, and performance.
- These technologies form the basis of modern distributed systems and network applications.# Chapter 06 – Distributed Computing and Network Communication in Python

## Chapter Overview

This chapter introduces different approaches for distributed computing and network communication in Python.

The chapter demonstrates:

- Socket Programming
- Client-Server Communication
- Remote Procedure Calls using Pyro4
- Distributed Task Execution using Celery

---

## Chapter Architecture

```mermaid
graph TD

A[Distributed Computing]

A --> B[Socket Programming]
A --> C[Pyro4]
A --> D[Celery]

B --> E[Client Server Communication]
C --> F[Remote Object Invocation]
D --> G[Distributed Task Queue]
```

---

## Project Structure

```text
Chapter06/
│
├── Celery/
├── Pyro4/
└── Socket/
```

---

# 1. Socket Programming

## Definition

Socket programming enables communication between two computers or processes over a network.

One program acts as a Server and another acts as a Client.

---

## Communication Flow

```mermaid
sequenceDiagram

participant Client
participant Server

Client->>Server: Connection Request
Server->>Client: Accept Connection
Client->>Server: Send Request
Server->>Client: Send Response
Client->>Server: Close Connection
```

---

## Working Process

```mermaid
flowchart TD

A[Create Socket]
B[Bind Address]
C[Listen]
D[Accept Client]
E[Send Data]
F[Close Connection]

A --> B --> C --> D --> E --> F
```

### Advantages

- Easy network communication
- Supports distributed applications
- Fast data exchange

### Disadvantages

- Connection management required
- Error handling can be complex

---

# 2. Pyro4 (Python Remote Objects)

## Definition

Pyro4 allows a Python program to call methods on an object running in another process or machine.

It works similarly to calling local functions, but the execution happens remotely.

---

## Pyro4 Architecture

```mermaid
graph LR

A[Client]

A --> B[Pyro Name Server]

B --> C[Remote Object Server]

C --> D[Execute Method]

D --> A
```

---

## First Example

### Objective

Create a remote server that provides a welcome message and allow clients to invoke it remotely.

### Workflow

```mermaid
flowchart TD

A[Start Name Server]
B[Start Pyro Server]
C[Register Object]
D[Client Lookup]
E[Remote Method Call]
F[Return Result]

A --> B --> C --> D --> E --> F
```

### Advantages

- Simple remote communication
- Object-oriented design
- Easy implementation

### Disadvantages

- Requires Name Server
- Network dependency

---

# 3. Chain Topology using Pyro4

## Definition

Multiple servers are connected in sequence where requests travel through a chain of remote objects.

---

## Architecture

```mermaid
graph LR

A[Client]

A --> B[Server 1]
B --> C[Server 2]
C --> D[Server 3]

D --> E[Result]
```

---

## Workflow

```mermaid
flowchart TD

A[Client Request]
B[Server 1]
C[Server 2]
D[Server 3]
E[Return Final Response]

A --> B --> C --> D --> E
```

### Applications

- Distributed Systems
- Service Chaining
- Microservices Architecture
- Multi-layer Processing

---

# 4. Celery Distributed Tasks

## Definition

Celery is a distributed task queue used for executing background jobs asynchronously.

Instead of waiting for a task to complete, the task is sent to a worker process.

---

## Celery Architecture

```mermaid
graph LR

A[Application]

A --> B[Message Broker]

B --> C[Celery Worker]

C --> D[Execute Task]

D --> E[Return Result]
```

---

## Task Execution Flow

```mermaid
flowchart TD

A[Create Task]
B[Send to Broker]
C[Worker Receives Task]
D[Execute Task]
E[Store Result]

A --> B --> C --> D --> E
```

### Advantages

- Background processing
- Scalable architecture
- Distributed execution
- Improved performance

### Disadvantages

- Additional setup required
- Requires broker service

---

# Comparison

| Feature | Socket | Pyro4 | Celery |
|----------|---------|--------|---------|
| Communication | Low-Level | Remote Objects | Task Queue |
| Complexity | High | Medium | Medium |
| Scalability | Moderate | Good | Excellent |
| Asynchronous | Limited | Possible | Yes |
| Distributed Support | Yes | Yes | Yes |
| Best Use Case | Networking | Remote Method Calls | Background Tasks |

---

# Distributed Computing Model

```mermaid
graph TD

A[Client Application]

A --> B[Socket Server]
A --> C[Pyro4 Server]
A --> D[Celery Worker]

B --> E[Network Communication]
C --> F[Remote Objects]
D --> G[Background Tasks]
```

---

# Learning Outcomes

After completing this chapter, you will be able to:

- Understand distributed computing concepts.
- Build client-server applications using sockets.
- Implement remote method invocation using Pyro4.
- Create chain topology architectures.
- Execute asynchronous tasks using Celery.
- Understand message brokers and workers.
- Design scalable distributed systems.

---

# Requirements

```bash
pip install Pyro4
pip install celery
```

---

# Running Examples

## Socket Server

```bash
python server.py
```

## Socket Client

```bash
python client.py
```

## Pyro4 Name Server

```bash
python -m Pyro4.naming
```

## Pyro4 Server

```bash
python pyro_server.py
```

## Pyro4 Client

```bash
python pyro_client.py
```

## Celery Worker

```bash
celery -A addTask worker --loglevel=info
```

## Execute Task

```bash
python addTask_main.py
```

---

# Final Summary

- Socket Programming provides the foundation of network communication.
- Pyro4 enables remote method invocation and distributed object-oriented programming.
- Celery simplifies asynchronous and distributed task execution.
- Distributed computing improves scalability, responsiveness, and performance.
- These technologies form the basis of modern distributed systems and network applications.
