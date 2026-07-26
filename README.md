# 🚀 CRUDify

[![GitHub license](https://shields.io)](https://github.com)
[![Python Version](https://shields.io)](https://www.python.org)

**CRUDify** is a modern and powerful backend project built to demonstrate advanced security implementation and multi-database system architectures. It combines solid coding practices with production-ready features.

---

## ✨ Key Features

* **🔐 Advanced Authentication System** - Secure user sign-up, login, and token-based authentication. *(Available on the `master` branch)*

* **🗄️ Multi-Database Support** - Advanced configuration capable of handling multiple databases seamlessly. *(Explore this on the `feature/multidatabase-support` branch)*

* **⚡ Clean Architecture** - Organized, scalable, and easy-to-maintain folder structure.

---

## 🛠️ Tech Stack

* **Language:** Python 🐍
* **Framework:** FastAPI
* **Database:** SQLite / PostgreSQL
* **Authentication:** JWT (JSON Web Tokens)

---

## 🌿 Repository Branches

This repository is structured into separate branches to showcase different architectural ideas:

1. **`master`** (Main Branch): Contains the production-ready code with the full **Authentication System**.

2. **`feature/multidatabase-support`**: An independent experimental branch showcasing **multi-database connectivity**.

---

## 🚀 Getting Started 

### 1. Clone the Repository
```bash
git clone git@github.com:IshtiAhmedTiham/CRUDify.git
cd CRUDify
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
fastapi dev main.py

**Another way to run**
python3 -m uvicorn main:app --reload
```

---

## 📝 Project Roadmap

- [x] Build core CRUD functionalities
- [x] Implement and merge `feature/auth-system` into master
- [x] Separate and configure `feature/multidatabase-support` branch

---

*Feel free to open an Issue or submit a Pull Request if you have any questions or suggestions!*
