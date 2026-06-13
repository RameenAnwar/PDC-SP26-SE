# Chapter 6: Distributed Python

Welcome to the comprehensive guide and documentation for **Chapter 6: Distributed Python**. This repository contains practical implementations, architectural explanations, step-by-step setup guides, and runtime outputs for building distributed systems in Python.

---

## Quick Installation & Dependencies Setup

Before running the codes, make sure you have all the required Python packages and external systems configured.

| Component / Topic | Required Library | Installation Command | Notes |
| :--- | :--- | :--- | :--- |
| **Python Sockets** | *None (Built-in)* | Already included in standard Python | Uses built-in `socket` module |
| **Celery Core** | `celery` | `pip install celery` | Asynchronous distributed task queue |
| **Celery Windows Pool** | `eventlet` | `pip install eventlet` | Required on Windows for worker execution |
| **Remote Method Invocation** | `Pyro4` | `pip install Pyro4` | Python Remote Objects library |

### Step-by-Step Dependency Installation

Open your terminal or command prompt and run the following commands:

```bash
# 1. Upgrade pip to ensure smooth installations
python -m pip install --upgrade pip

# 2. Install Pyro4 for Remote Method Invocation (RMI)
pip install Pyro4

# 3. Install Celery and eventlet (mandatory for Windows users)
pip install celery eventlet
```

> [!NOTE]
> **Celery Broker Setup:** Celery requires a message broker like **RabbitMQ** or **Redis** to send and receive messages.
> *   For **RabbitMQ** (Default): Install it from the [Official RabbitMQ Website](https://www.rabbitmq.com/download.html). Ensure it's running locally on `amqp://guest@localhost//`.
> *   For **Redis**: Run Redis on your machine and change the broker URL in `addTask.py` to `redis://localhost:6379/0`.

---

## Table of Contents
1. [Introducing Distributed Computing](#1-introducing-distributed-computing)
2. [Types of Distributed Applications](#2-types-of-distributed-applications)
   - [Client-Server Applications & Architecture](#client-server-applications--architecture)
   - [TCP/IP Client-Server Communications](#tcpip-client-server-communications)
   - [Multi-Level (N-Tier) Applications](#multi-level-n-tier-applications)
3. [Using the Python Socket Module](#3-using-the-python-socket-module)
   - [Example 1: Basic Date-Time Server & Client](#example-1-basic-date-time-server--client)
   - [Example 2: File Transfer Server & Client](#example-2-file-transfer-server--client)
4. [Distributed Task Management with Celery](#4-distributed-task-management-with-celery)
5. [Remote Method Invocation (RMI) with Pyro4](#5-remote-method-invocation-rmi-with-pyro4)
   - [Example 1: Basic Pyro4 Welcome Server](#example-1-basic-pyro4-welcome-server)
   - [Example 2: Implementing Chain Topology](#example-2-implementing-chain-topology)

---

## 1. Introducing Distributed Computing

**Distributed computing** is a field of computer science that studies distributed systems. A *distributed system* is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another. The components interact with each other in order to achieve a common goal.

```mermaid
graph TD
    %% Styling definitions for clear visual contrast
    classDef clientClass fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px,stroke-dasharray: 5 5,color:#0D47A1;
    classDef lbClass fill:#FFF3E0,stroke:#FB8C00,stroke-width:2px,color:#E65100;
    classDef serverClass fill:#E8F5E9,stroke:#4CAF50,stroke-width:2px,color:#1B5E20;
    classDef dbClass fill:#EDE7F6,stroke:#5E35B1,stroke-width:2px,color:#4A148C;

    User([👤 User Client Application]) <--> |HTTP / TCP| LoadBalancer{🔀 Load Balancer}
    LoadBalancer <--> |Route Request| Server1[🖥️ Server Node A]
    LoadBalancer <--> |Route Request| Server2[🖥️ Server Node B]
    LoadBalancer <--> |Route Request| Server3[🖥️ Server Node C]
    
    Server1 <--> |Fetch / Write| DB[(💾 Shared Central Database)]
    Server2 <--> |Fetch / Write| DB
    Server3 <--> |Fetch / Write| DB

    class User clientClass;
    class LoadBalancer lbClass;
    class Server1,Server2,Server3 serverClass;
    class DB dbClass;
```

### Key Motivations:
*   **Resource Sharing:** Sharing hardware, software, or data resources seamlessly.
*   **Scalability:** The ability to handle growing amounts of work by adding resources (Horizontal vs. Vertical scaling).
*   **Fault Tolerance & Reliability:** If one server node fails, the remaining nodes can continue to operate without system downtime.
*   **Concurrency:** Multiple processing units running simultaneously to execute tasks much faster.

---

## 2. Types of Distributed Applications

Distributed systems are designed in various shapes and structures depending on operational requirements.

### Client-Server Applications & Architecture
In a client-server architecture, tasks or workloads are partitioned between the providers of a service, called **servers**, and service requesters, called **clients**.

```mermaid
sequenceDiagram
    autonumber
    actor Client as 💻 Client (Requestor)
    actor Server as 🖥️ Server (Provider)
    
    Note over Client,Server: Connection established via TCP/IP
    Client->>Server: 1. Send Service Request (e.g., Get Resource)
    activate Server
    Note over Server: Processes request,<br/>queries data & performs<br/>necessary computation
    Server-->>Client: 2. Send Service Response (Requested Data)
    deactivate Server
```

### TCP/IP Client-Server Communications
Communication is established using standard network protocols. 
*   **TCP (Transmission Control Protocol):** Connection-oriented, guarantees packet delivery, ensures packet ordering, and handles error checking.
*   **IP (Internet Protocol):** Directs packets to the correct host using IP addressing.

### Multi-Level (N-Tier) Applications
An N-tier application separates the presentation, application processing, and data management functions into isolated logical and physical tiers.

```mermaid
graph LR
    classDef pClass fill:#E0F7FA,stroke:#00ACC1,stroke-width:2px,color:#006064;
    classDef lClass fill:#FFFDE7,stroke:#FDD835,stroke-width:2px,color:#F57F17;
    classDef dClass fill:#FFEBEE,stroke:#E53935,stroke-width:2px,color:#B71C1C;

    ClientTier[🎨 Presentation Tier<br/>Web Browser / GUI Client] <--> AppTier[⚙️ Application Logic Tier<br/>Python Server / APIs]
    AppTier <--> DataTier[💾 Data Storage Tier<br/>Databases / File System]

    class ClientTier pClass;
    class AppTier lClass;
    class DataTier dClass;
```

---

## 3. Using the Python Socket Module

The `socket` module in Python provides direct access to the BSD socket interface. Sockets allow communication between two different processes on the same or different machines.

### Example 1: Basic Date-Time Server & Client

This implementation demonstrates a simple server that listens on a port, accepts client connections, sends the current server time, and closes the connection.

#### Architecture Flowchart:
```mermaid
sequenceDiagram
    autonumber
    participant Server as 🖥️ Server (server.py)
    participant Client as 💻 Client (client.py)
    
    Note over Server: 1. Bind to Local Host:9999 & Listen
    Client->>Server: 2. TCP Connection Request (socket.connect)
    Note over Server: 3. Connection Accepted (accepts socket connection)
    Server->>Client: 4. Send Current Server Date-Time (ASCII encoded bytes)
    Note over Server: 5. Server Closes socket
    Note over Client: 6. Client Decodes data & prints output
    Client-->>Client: Connection Closed
```

#### Code Files:
*   **Server Code:** [server.py](Codes/socket/server.py)
*   **Client Code:** [client.py](Codes/socket/client.py)

#### Output Screenshot:
<p align="center">
  <img src="Output/client.py.png" alt="Socket Date-Time Client Output" width="80%" />
</p>

---

### Example 2: File Transfer Server & Client

This implementation demonstrates sending a file (`mytext.txt`) from a server to a client upon request.

#### Architecture Flowchart:
```mermaid
sequenceDiagram
    autonumber
    participant Server as 🖥️ Server (server2.py)
    participant Client as 💻 Client (client2.py)
    
    Note over Server: 1. Listen on Port 60000
    Client->>Server: 2. Connects & Sends 'HelloServer!' message
    Note over Server: 3. Read 'mytext.txt' in binary mode
    Server->>Client: 4. Send File Data in 1024-byte buffer chunks
    Server->>Client: 5. Send Termination String "->Thank you for connecting"
    Note over Client: 6. Client writes incoming data to 'received.txt'
    Note over Client: 7. Connection closed successfully
```

#### Code Files:
*   **Server Code:** [server2.py](Codes/socket/server2.py)
*   **Client Code:** [client2.py](Codes/socket/client2.py)

#### Output Screenshot:
<p align="center">
  <img src="Output/client2.py.png" alt="Socket File Transfer Output" width="80%" />
</p>

---

## 4. Distributed Task Management with Celery

**Celery** is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation but supports scheduling as well.

### Celery Architecture Diagram:
```mermaid
graph LR
    classDef clientClass fill:#E0F2F1,stroke:#009688,stroke-width:2px,color:#004D40;
    classDef brokerClass fill:#ECEFF1,stroke:#607D8B,stroke-width:2px,color:#263238;
    classDef workerClass fill:#FFF3E0,stroke:#FF9800,stroke-width:2px,color:#E65100;
    classDef backendClass fill:#EDE7F6,stroke:#673AB7,stroke-width:2px,color:#311B92;

    Client[💻 Client App<br/>addTask_main.py] -->|1. Delay/Apply Async| Broker{🔀 Message Broker<br/>RabbitMQ / Redis}
    Broker -->|2. Pull Tasks| Worker[⚙️ Celery Worker<br/>addTask.py]
    Worker -->|3. Store Results| Backend[(💾 Result Backend<br/>Database / Redis)]

    class Client clientClass;
    class Broker brokerClass;
    class Worker workerClass;
    class Backend backendClass;
```

### Windows Setup & Execution
On Windows, Celery needs a compatible event pool execution method. You can run Celery on Windows using `eventlet` or `gevent` pool solo.

1.  **Start RabbitMQ Server** (Broker must be running).
2.  **Start Celery Worker Node:**
    ```bash
    celery -A addTask worker --loglevel=info -P solo
    ```
3.  **Run Client App** to queue tasks:
    ```bash
    python addTask_main.py
    ```

#### Code Files:
*   **Task Definition:** [addTask.py](Codes/Celery/addTask.py)
*   **Main Runner:** [addTask_main.py](Codes/Celery/addTask_main.py)

#### Output Screenshot:
<p align="center">
  <img src="Output/celery.png" alt="Celery Distributed Task Worker Output" width="80%" />
</p>

---

## 5. Remote Method Invocation (RMI) with Pyro4

**Pyro4** (Python Remote Objects) is a library that enables you to build applications in which objects can talk to each other over the network, with minimal programming effort. You can just write normal Python classes and Pyro will make them callable remotely.

### Example 1: Basic Pyro4 Welcome Server

#### Pyro4 Communication Architecture:
```mermaid
sequenceDiagram
    autonumber
    participant NameServer as 🔍 Pyro Name Server (pyro4-ns)
    participant Daemon as 🖥️ Server Daemon (pyro_server.py)
    participant Client as 💻 Client Proxy (pyro_client.py)
    
    Note over NameServer: Start Name Server (pyro4-ns)
    Daemon->>NameServer: 1. Register "server" object with its URI
    Client->>NameServer: 2. Query/Lookup "server"
    NameServer-->>Client: 3. Return object URI
    Client->>Daemon: 4. Invoke Remote Method: welcomeMessage(name)
    Daemon-->>Client: 5. Return "Hi welcome [name]" result
```

#### Running the Example:
1.  **Start Pyro4 Name Server** in a separate terminal:
    ```bash
    pyro4-ns
    ```
2.  **Start Pyro4 Server Daemon**:
    ```bash
    python pyro_server.py
    ```
3.  **Run Pyro4 Client**:
    ```bash
    python pyro_client.py
    ```

#### Code Files:
*   **Pyro4 Server:** [pyro_server.py](Codes/Pyro4/First%20Example/pyro_server.py)
*   **Pyro4 Client:** [pyro_client.py](Codes/Pyro4/First%20Example/pyro_client.py)

#### Output Screenshot:
<p align="center">
  <img src="Output/pyro_client.png" alt="Pyro4 RMI Welcome Example Output" width="80%" />
</p>

---

### Example 2: Implementing Chain Topology

In this configuration, a message is routed through a series of servers (forming a chain or ring topology). Each server adds its identifier to the message and forwards it to the next server in the chain until the chain is closed (i.e., a server detects that the message has returned to the originator).

#### Chain Topology Flowchart:
```mermaid
graph TD
    classDef clClass fill:#E0F7FA,stroke:#00ACC1,stroke-width:2px,color:#006064;
    classDef s1Class fill:#E8F5E9,stroke:#4CAF50,stroke-width:2px,color:#1B5E20;
    classDef s2Class fill:#FFF3E0,stroke:#FF9800,stroke-width:2px,color:#E65100;
    classDef s3Class fill:#EDE7F6,stroke:#673AB7,stroke-width:2px,color:#311B92;

    Client[💻 Client client_chain.py] -->|1. Process Msg| Server1[🖥️ Server 1]
    Server1 -->|2. Forward Msg| Server2[🖥️ Server 2]
    Server2 -->|3. Forward Msg| Server3[🖥️ Server 3]
    Server3 -->|4. Detect Loop & Complete Chain| Server1
    Server1 -->|5. Return Accumulated Result Array| Client

    class Client clClass;
    class Server1 s1Class;
    class Server2 s2Class;
    class Server3 s3Class;
```

#### Running the Example:
1.  Start `pyro4-ns` name server.
2.  Run the three servers in three separate terminal windows:
    ```bash
    python server_chain_1.py
    ```
    ```bash
    python server_chain_2.py
    ```
    ```bash
    python server_chain_3.py
    ```
3.  Run the client chain runner to trigger the sequence:
    ```bash
    python client_chain.py
    ```

#### Code Files:
*   **Topology Definition:** [chainTopology.py](Codes/Pyro4/Second%20Example/chainTopology.py)
*   **Client Runner:** [client_chain.py](Codes/Pyro4/Second%20Example/client_chain.py)
*   **Server 1:** [server_chain_1.py](Codes/Pyro4/Second%20Example/server_chain_1.py)
*   **Server 2:** [server_chain_2.py](Codes/Pyro4/Second%20Example/server_chain_2.py)
*   **Server 3:** [server_chain_3.py](Codes/Pyro4/Second%20Example/server_chain_3.py)

#### Output Screenshot:
<p align="center">
  <img src="Output/client_chain.py.png" alt="Chain Topology Execution Output" width="80%" />
</p>
