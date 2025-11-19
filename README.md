# Flask User Management API

This is a simple REST API built using Flask for managing users (CRUD).

## Features
- Create user (POST)
- Get all users (GET)
- Get single user (GET)
- Update user (PUT)
- Delete user (DELETE)

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run the API
python app.py

### 3. Test with Postman or cURL
GET http://127.0.0.1:5000/users
POST http://127.0.0.1:5000/users
PUT http://127.0.0.1:5000/users/<id>
DELETE http://127.0.0.1:5000/users/<id>