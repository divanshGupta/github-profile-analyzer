# GitHub Analyzer API

A backend service built with Flask that analyzes GitHub user profiles and repositories.
This project demonstrates clean backend architecture, API design, caching, logging, and error handling.

---

## 🚀 Features

* Fetch GitHub user profile data
* Analyze top repositories based on stars
* In-memory caching for performance optimization
* Structured logging for debugging and monitoring
* Centralized error handling
* Clean layered architecture (Routes → Services → Utils)

---

## 🧱 Architecture

```
Client → Routes → Services → External API (GitHub)
```

### Layers:

* **Routes** → Handle HTTP requests/responses
* **Services** → Business logic & GitHub API calls
* **Utils** → Helpers (cache, logging, calculations)

---

## 📦 Tech Stack

* Python
* Flask
* Requests
* Logging module

---

## ⚙️ Setup & Run

```bash
git clone <your-repo-url>
cd project
pip install -r requirements.txt
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### 1. Get User Profile

```
GET /user/<username>
```

### 2. Get Top Repositories

```
GET /user/<username>/repos?limit=5
```

---

## ⚡ Key Backend Concepts Implemented

* Separation of concerns (clean architecture)
* Caching with TTL (performance optimization)
* API response standardization
* Error handling strategy
* Logging for observability
* External API integration

---

## 🔮 Future Improvements

* Redis caching
* Docker containerization
* Rate-limit retry strategy
* Authentication support

---

## 📌 Author

Divyansh Gupta
Frontend Developer transitioning into Backend Engineering
