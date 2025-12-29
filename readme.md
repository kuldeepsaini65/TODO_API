# 📝 To-Do List Web Application (Django – API First)

## Live Link - https://todo.kuldeepsaini.in

This project is a **To-Do List web application** built using **Python and Django**, following an **API-first architecture**.

The application provides **RESTful APIs for CRUD operations** on tasks and uses **Django templates** for rendering the user interface.  
All database operations are handled using **raw SQL** (no ORM).

---

## 🎯 Objective

- Build RESTful APIs for task management (CRUD)
- Render UI using Django templates
- Ensure templates interact with backend **only via APIs**
- Avoid Django ORM and generic ViewSets
- Follow clean, professional backend architecture

---

## 🚀 Features

- Create, view, update, and delete tasks
- RESTful API endpoints for all operations
- API-first design (browser → API → database)
- Custom API Key authentication using middleware
- Raw SQL database access (no ORM)
- Reusable templates for Create & Update
- Clean and readable codebase

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (can be replaced with PostgreSQL/MySQL)
- **Frontend:** Django Templates, Bootstrap, JavaScript (Fetch API)
- **Authentication:** API Key (Custom Middleware)
- **Testing:** pytest

---

## 📂 Project Structure

```
project/
│
|---api
|    |--- views.py       # API Views
|    |--- urls.py        # API Routes
|    |--- middleware.py  # API Auth via API-KEY
|
|
|---- task/
│   ├── views.py          # template views
│   ├── urls.py
│   └── db_con.py         # Raw SQL helpers
│
|
├── templates/
│   └── tasks/
│   |    ├── task_list.html
│   |    ├── task_add.html
│   |    └── task_info.html
│   |
|   |------- base.html          # Base File of all .html files (help for Same UI)
|   |------- docs.html          # Used to mention details of API on the APP itself
|
├── settings.py
├── manage.py
|--- API_DOCUMENTATION.md       # Contain Detaild Documentation of API's
└── README.md
```

---

## 🔐 API Authentication

All API endpoints are protected using an **API Key**.

### Required Header
```
X-API-KEY: kdeep@saini@8865@hello           
```


- API key validation is handled by **custom middleware**
- Authentication is applied **only to `/api/` routes**
- Template-rendered pages remain publicly accessible

---

## 🧩 Database Schema

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    status TEXT
);
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kuldeepsaini65/TODO_API.git
cd TODO_API
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
```

### 3️⃣ Install Dependencies
```bash
pip install -r req.txt
```

### 4️⃣ Run the Server
```bash
python manage.py runserver
```

### 5️⃣ Open in Browser
```
http://127.0.0.1:8000/
```




---

## 📌 Notes for Evaluation

- Django ORM is **not used**
- Generic ViewSets are **not used**
- All CRUD operations are handled via REST APIs
- Templates interact with APIs using JavaScript (Fetch API)
- Code follows clean separation of concerns

---

## 📄 License

This project is created for **learning and evaluation purposes**.
