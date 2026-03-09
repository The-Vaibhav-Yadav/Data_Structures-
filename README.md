# Data Structures & Algorithms Lab Implementations

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A comprehensive collection of fundamental data structures and classic algorithm lab implementations. This repository serves as a practical reference for academic coursework, demonstrating how core CS concepts are built from scratch utilizing Python object-oriented patterns without relying on specialized external libraries.

## Table of Contents
- [Tech Stack & Architecture](#tech-stack--architecture)
- [Prerequisites](#prerequisites)
- [Installation & Local Setup](#installation--local-setup)
- [Usage & Running the App](#usage--running-the-app)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing Guidelines](#contributing-guidelines)
- [License and Contact](#license-and-contact)

## Tech Stack & Architecture

- **Primary Technologies**: Python (Standard Library only)
- **Concepts**: Linked Lists, Stacks, Queues, Trees, Graph Traversals.

**High-Level Architecture**:
Each laboratory session is partitioned into specific files or folders.
- **Lab 1**: Object-oriented implementations of custom `Singly Linked Lists` (Nodes) with arbitrary large integer manipulation mechanics.
- **Lab 2/3**: Explores foundational Stack and Queue principles alongside classic search tasks like the `8-puzzle` problem utilizing heuristic graph traversal.
- **Lab 4/5**: Builds recursive parsing strategies utilizing binary trees (Inorder, Preorder, Postorder traversals natively mapping roots and leaves).

## Prerequisites
Don't assume your environment handles arbitrary Python arrays; you simply need a base interpreter install.
- **Python**: Version 3.8+ or higher natively tracked.

## Installation & Local Setup

Running the environment requires a simple bash traversal mapping to the execution contexts natively:

```bash
git clone https://github.com/The-Vaibhav-Yadav/Data_Structures-.git
cd Data_Structures-
```
No environment variables (`.env`) or explicit API keys are mandated for executing standard logic.

## Usage & Running the App

To run any of the specific laboratory experiments, just point your python interpreter sequentially to the script mapped natively in your base structure.

Startup commands for traversing standard linked list configurations:
```bash
python3 lab1th.py
```

**Code snippet details internally parsed**:
```python
# Utilizing node pointers to track sequential lists gracefully
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
```

## Testing
Currently, the codebase outputs logic testing directly to standard output (`stdout`). Future iterations can leverage unit tests dynamically parsing matrices properly.
```bash
python3 -m unittest
```
**Types of Tests**: Unit testing mappings focusing explicitly on testing the output boundaries traversed natively. 

## Deployment
Academic algorithmic repositories are traditionally deployed internally on logical execution frames and not normally ported to production. We recommend containerizing via standard Python baseline containers if orchestrating cloud endpoints dynamically mapping CI boundaries.

## Contributing Guidelines
We welcome strict pull requests for feature additions!
- **Branching Strategy**: Use standard Trunk-based iterations (`feature/linked-list-reversal`).
- **Commit Standards**: Use Conventional Commits (`fix: array indexing bounding`).
- **Code Style**: Use standardized formatting referencing PEP-8 native guidelines dynamically.

## License and Contact
**License**: MIT 
**Author**: Vaibhav Yadav (https://github.com/The-Vaibhav-Yadav)
