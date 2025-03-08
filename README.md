# FastAPI User Management API

## 🚀 About This Project
This is a **FastAPI-based User Management API** that allows you to:
- **Retrieve users** (all or by username).
- **Create, update, and delete users**.
- **Support full and partial user updates using PUT and PATCH requests**.
- **Enforce validation rules** using Pydantic.

---

## 🛠️ Features
- ✅ **GET `/users`** → Fetch all users (with a limit parameter).
- ✅ **GET `/users/{username}`** → Retrieve a user by username.
- ✅ **POST `/create-user`** → Create a new user.
- ✅ **DELETE `/user/{username}`** → Delete a user.
- ✅ **PUT `/user`** → Update a user completely.
- ✅ **PATCH `/user`** → Update a user partially.

---

## 📌 Installation & Setup

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/fastapi-user-management.git
cd fastapi-user-management
```

### 2️⃣ **Install Dependencies**
```sh
pip install fastapi pydantic uvicorn
```

### 3️⃣ **Run the API Server**
```sh
uvicorn app:app --reload
```

This starts the FastAPI server on **`http://127.0.0.1:8000`**.

---

## 🔍 API Endpoints

### 📥 **Retrieve All Users**
#### **GET** `/users?limit=5`
Fetch a list of users (default limit is 30).

```json
[
  {"username": "alice", "date_joined": "2023-01-15", "location": "New York", "email": "alice@example.com", "is_active": true, "age": 22}
]
```

### 🔍 **Retrieve a Single User**
#### **GET** `/users/{username}`
Fetch user details by username.

### ➕ **Create a New User**
#### **POST** `/create-user`
##### **Request Body:**
```json
{
  "username": "new_user",
  "date_joined": "2024-03-01",
  "location": "Paris",
  "email": "newuser@example.com",
  "is_active": true,
  "age": 30
}
```

### 🗑️ **Delete a User**
#### **DELETE** `/user/{username}`
Deletes a user from the database.

### 🔄 **Update a User (Full Update)**
#### **PUT** `/user`
Replaces all user data.

### ✏️ **Update a User (Partial Update)**
#### **PATCH** `/user`
Updates only the specified fields (e.g., email, location).

---

## 📜 License
This project is **MIT Licensed**. You are free to use and modify it.

---

### 📧 Contact
For any issues, reach out via [GitHub Issues](https://github.com/your-username/fastapi-user-management/issues).

---
