# Fitness API
 
A high-performance REST API built with **FastAPI** for fitness tracking, workout management, and health data.
 
---

## Requirements
 
- Python 3.11+
- pip
---
 
## Installation
 
**1. Clone the repository**
 
```bash
git clone git@github.com:IshtiAhmedTiham/CRUDify.git
```
 
**2. Install dependencies**
 
```bash
pip install "fastapi[standard]"
pip install psycopg2-binary
pip install sqlalchemy
```
 
---
 
## Running the Server
 
```bash
fastapi dev main.py
```
 
**Alternative — Uvicorn directly**
 
```bash
python3 -m uvicorn main:app --reload
```
 
The server will start at `http://127.0.0.1:8000`
The redoc server will start at `http://127.0.0.1:8000`
---
 
## Usage
 
Define routes in `main.py` using FastAPI's method decorators:
 
```python
from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/home")
def home():
    return "This is home page"

---
