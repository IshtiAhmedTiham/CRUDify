# This is Fastapi project

## Installation

```bash
pip install "fastapi[standard]"

```

## Project Description
```bash
git clone git@github.com:ishtiahmed00/fitness.git
```

## Usage of fastapi
```python
from fastapi import FastAPI 
app = FastAPI()
@app.method("path")
```

## Run fastapi
fastapi dev main.py

#another way to run
python3 -m uvicorn main:app --reload