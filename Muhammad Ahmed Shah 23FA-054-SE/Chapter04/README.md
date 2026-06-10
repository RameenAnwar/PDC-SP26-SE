# 🧑‍🎓 Student Information

> **Student Name:** M. Ahmed Shah  
> **Roll No:** 23FA-054-SE  

---

# Chapter 04: Distributed Memory and Message Passing Interface (MPI)

## Overview

Welcome to the **Parallel and Distributed Computing (PDC)** documentation for Chapter 04. While previous chapters focused on Shared Memory (Threading) and Multi-Core parallelism (Multiprocessing) confined within a single physical machine, this chapter explores **Distributed Computing using MPI (Message Passing Interface)**.

---

# PART 1: THEORETICAL FOUNDATIONS

## 1. Distributed Memory Architectures

### Cluster Computing Paradigm (Updated Colors)

```mermaid
graph TD

    subgraph Node1["Compute Node 1"]
        CPU1[CPU]
        RAM1[(RAM)]
        CPU1 <--> RAM1
    end

    subgraph Node2["Compute Node 2"]
        CPU2[CPU]
        RAM2[(RAM)]
        CPU2 <--> RAM2
    end

    subgraph Node3["Compute Node N"]
        CPU3[CPU]
        RAM3[(RAM)]
        CPU3 <--> RAM3
    end

    NET["High-Speed Network Switch"]

    Node1 <-->|MPI Messages| NET
    Node2 <-->|MPI Messages| NET
    Node3 <-->|MPI Messages| NET


    %% COLORS
    classDef node fill:#1e3a8a,stroke:#0f172a,color:#ffffff;
    classDef cpu fill:#0f766e,stroke:#064e3b,color:#ffffff;
    classDef ram fill:#7c3aed,stroke:#4c1d95,color:#ffffff;
    classDef net fill:#f97316,stroke:#9a3412,color:#ffffff;

    class CPU1,CPU2,CPU3 cpu;
    class RAM1,RAM2,RAM3 ram;
    class NET net;
    class Node1,Node2,Node3 node;
