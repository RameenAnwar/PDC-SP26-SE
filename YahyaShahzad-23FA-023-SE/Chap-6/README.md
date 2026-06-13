# Chapter 06 — Distributed Tasks & RPC
[![Course](https://img.shields.io/badge/Course-Parallel%20%26%20Distributed%20Computing-blue)](#)
[![Language](https://img.shields.io/badge/Language-Python-3776AB)](#)
[![Level](https://img.shields.io/badge/Level-Intermediate-orange)](#)
[![Focus](https://img.shields.io/badge/Focus-Parallel%20Computing-red)](#)
[![Author](https://img.shields.io/badge/Author-Yahya%20Shahzad-green)](#)

---

##  Course Information
**Course:** Parallel and Distributed Computing (PDC) 
**Student Name:** Yahya Shahzad 
**Roll No:** 23FA-023-SE

---

## Overview
- Covers simple distributed communication techniques: raw `socket` TCP clients/servers, `Celery` task queue examples (brokered async tasks), and `Pyro4` RPC-style services including a chain topology. Each example includes the minimal steps to run locally and common deployment caveats.

Files (detailed)
- `socket/server.py` / `socket/client.py` — basic TCP server that sends the current time; `client` receives and prints it.
- `socket/server2.py` / `socket/client2.py` — file-transfer style example; server sends a file, client writes `received.txt`.
- `socket/addTask.py`, `socket/addTask_main.py` — toy task-dispatch over sockets (illustrative only).
- `Celery/addTask.py`, `Celery/addTask_main.py` — defines a Celery `add` task and a small launcher that calls `add.delay(5,5)`; requires a message broker (RabbitMQ/Redis) and worker processes.
- `Pyro4/First Example/pyro_server.py`, `pyro_client.py` — simple RPC service that returns a welcome message.
- `Pyro4/Second Example/*` — chain of Pyro servers (`chainTopology`) forwarding messages along a ring/chain to demonstrate service composition.

Run & examples
- Socket server (local test):
```bash
python Chapter06/socket/server.py
python Chapter06/socket/client.py
```
- File transfer example:
```bash
python Chapter06/socket/server2.py
python Chapter06/socket/client2.py
```
- Celery (requires broker & worker):
```bash
# start worker (in project root)
celery -A Chapter06.Celery.addTask worker --loglevel=info
# in another shell, invoke task
python Chapter06/Celery/addTask_main.py
```
- Pyro4 (start name server first):
```bash
pyro4-ns
python Chapter06/Pyro4/First\ Example/pyro_server.py
python Chapter06/Pyro4/First\ Example/pyro_client.py
```

Architecture diagrams
```mermaid
flowchart LR
  subgraph Socket
    Cl[Client] -->|TCP| Srv[Server]
  end

  subgraph Celery
    Producer[App] -->|push task| Broker[(RabbitMQ/Redis)]
    Broker -->|deliver| Worker[Celery Worker]
    Worker -->|result| Backend[(optional result backend)]
  end

  subgraph Pyro4_Chain
    Client -->|lookup| NameServer[Pyro NameServer]
    NameServer --> P1[Server 1]
    P1 --> P2[Server 2] --> P3[Server 3]
  end
```

Notes & caveats
- `socket` examples are synchronous and blocking; adapt to non-blocking or threaded servers for concurrent clients.
- Celery requires external infrastructure (broker). For local testing install RabbitMQ or use Redis as a broker.
- Pyro4 depends on a running name server (`pyro4-ns`) and network accessibility; use local hostnames for single-machine tests.
