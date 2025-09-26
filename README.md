# Task Manager Web Application

A modern **one-page web application** for managing projects, which include tasks with deadlines, priorities, and task completion status. Built with **Django 5.2**, **Python 3.13**, and modern front-end technologies like **Bootstrap5** and **HTMX**. 

This application allows users to manage projects and tasks efficiently, with a responsive interface and AJAX-like interactions without page reloads.


## Content

- [Functional](#functional)
- [Installation](#Installation)
- [Stack of the technologies](#stack-of-the-technologies)
- [DB](#db)
- [Demonstration](#demonstation)

## Functional:

- Create and manage projects.
- Add tasks to projects, change their priority, and define deadlines.
- Mark tasks as done.
- Edit or delete projects and tasks.
- Authorization to create projects to the different accounts


## Installation

> **Note:** Before running the project, make sure all line separators in scripts (like `entrypoint.sh`) are set to **LF**. Using CRLF may cause error as "exec ./entrypoint.sh: no such file or directory" in Docker.
> 
1. **Clone the project:**
   ```bash
   git clone https://github.com/KrupkoOleh/crm_django.git

2. **Start Docker containers**:
   ```bash
   docker-compose up --build

3. **Open the website:**
   ```bash
   http://localhost:8000

## Stack of the technologies
1. **Programming Language**: Python (v 3.13)  
2. **Web Framework**: Django (v 5.2)  
3. **Architecture**: Single-page application (SPA) with HTMX
5. **Database**: PostgreSQL 
6. **Code Linting**: Ruff  
7. **Containers and Environment**: Docker + Docker Compose

## DB

![image of the db](https://i.postimg.cc/VL9Z1p7c/image.png)

## Demonstation

![image of the db](https://i.postimg.cc/tThvTcXP/image.png)

![image of the db](https://i.postimg.cc/4xD19121/image.png)

![image of the db](https://i.postimg.cc/ZRV3VPH2/image.png)

![image of the db](https://i.postimg.cc/fk4bKkG1/image.png)



