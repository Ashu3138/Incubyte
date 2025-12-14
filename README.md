# Sweet Shop Management System 🍭

This repository contains a full-stack Sweet Shop Management System built to practice real-world backend and frontend engineering concepts such as authentication, REST APIs, inventory handling, testing, and deployment.

The project focuses on correctness, clarity, and maintainability rather than over-engineering.

---

## Project Overview

The application allows users to browse and purchase sweets from a shop while keeping inventory in sync.  
An admin role is responsible for managing sweets and stock levels.

The system is divided into:
- A **FastAPI backend** that exposes secured REST APIs
- A **React frontend** that consumes these APIs
- A **SQLite database** for persistent storage

---

## Functional Requirements Implemented

### User Authentication
- User registration and login
- JWT-based authentication
- Secure password hashing
- Role-based access control (`USER`, `ADMIN`)

### Sweet & Inventory Management
- View all sweets
- Search sweets by name or category
- Purchase sweets (automatically updates stock)
- Prevent purchase when stock reaches zero
- Admin-only:
  - Add sweets
  - Update sweet details
  - Restock inventory
  - Delete sweets

### Testing
- Backend unit tests using `pytest`
- API testing using FastAPI’s TestClient

---

## Technology Choices

### Backend
- Python
- FastAPI
- SQLAlchemy ORM
- SQLite database
- JWT (python-jose)
- bcrypt for password hashing
- pytest for testing

### Frontend
- React
- Axios for API calls
- Create React App

### Development Tools
- VS Code
- Git & GitHub

---

## Repository Structure

### Backend
