# 📘 To-Do List API Documentation

Base URL:
```
http://127.0.0.1:8000/api/
```

All endpoints accept and return **JSON** data.

---

## 🔐 Authentication

All API endpoints are protected using **API Key Authentication**.

### Required Header
```
X-API-KEY: kdeep@saini@8865@hello
```

Authentication is handled using a **custom Django middleware** and is applied only to `/api/` routes.
Other Routes can freely Operate without Auth.
---

## 📌 1. Get All Tasks

### Endpoint
```
GET /api/tasks/
```

### Headers
```
X-API-KEY: kdeep@saini@8865@hello
```

### Success Response (200)
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "title": "Task One",
      "description": "Demo task",
      "due_date": "2025-12-28",
      "status": "PENDING"
    }
  ]
}
```

---

## 📌 2. Get Task by ID

### Endpoint
```
GET /api/tasks/<id>
```

### Headers
```
X-API-KEY: kdeep@saini@8865@hello
```

### Success Response (200)
```json
{
  "status": "success",
  "data": {
    "id": 1,
    "title": "Task One",
    "description": "Demo task",
    "due_date": "2025-12-28",
    "status": "PENDING"
  }
}
```

---

## 📌 3. Create Task

### Endpoint
```
POST /api/tasks/create/
```

### Headers
```
Content-Type: application/json
X-API-KEY: kdeep@saini@8865@hello
```

### Request Body
```json
{
  "title": "New Task",
  "description": "Task description",
  "due_date": "2025-12-30",
  "status": "PENDING"
}
```

### Success Response
```json
{
  "status": "success",
  "message": "Task created successfully"
}
```

---

## 📌 4. Update Task

### Endpoint
```
PUT /api/tasks/update/<id>
```

### Headers
```
Content-Type: application/json
X-API-KEY: kdeep@saini@8865@hello
```

### Request Body
```json
{
  "title": "Updated Task",
  "description": "Updated description",
  "due_date": "2025-12-31",
  "status": "COMPLETED"
}
```

### Success Response
```json
{
  "status": "success",
  "message": "Task updated successfully"
}
```

---

## 📌 5. Delete Task

### Endpoint
```
DELETE /api/tasks/delete/<id>
```

### Headers
```
X-API-KEY: kdeep@saini@8865@hello
```

### Success Response
```json
{
  "status": "success",
  "message": "Task deleted successfully"
}
```

---

## ❌ Error Responses

### Unauthorized (401)
```json
{
  "status": "error",
  "message": "API key missing or invalid"
}
```

### Not Found (404)
```json
{
  "status": "error",
  "message": "Task not found"
}
```

---

## ✅ Design Principles

- RESTful API design
- API-first architecture
- Raw SQL database access (no ORM)
- Middleware-based authentication
- Clear separation of concerns
- No Login Or User Accounts

---

## 📌 Notes

- APIs are consumed directly by browser using JavaScript (Fetch API)
- Django views only render HTML templates


---

## 📄 Conclusion
This API provides a clean and scalable backend for managing tasks, And i hope its fully compliant with the assignment Instructions.
