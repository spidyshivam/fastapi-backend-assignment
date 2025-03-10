# Async User CRUD API

A FastAPI application with asynchronous Tortoise-ORM for managing users in a PostgreSQL database. This project implements full CRUD operations (Create, Read, Update, Delete) for a `User` resource using a REST API.

## Features
- **Framework**: FastAPI with async support
- **Database**: PostgreSQL with asyncpg driver
- **ORM**: Tortoise-ORM for async database interactions
- **Endpoints**:
  - `GET /users`: List all users
  - `GET /users/{id}`: Retrieve a user by ID
  - `POST /users`: Create a new user
  - `PUT /users/{id}`: Update an existing user
  - `DELETE /users/{id}`: Delete a user

## Prerequisites
- **Python**: 3.11 or higher
- **PostgreSQL**: Installed locally or accessible via a cloud service (e.g., Neon Serverless Postgres)
- **Postman**: Recommended for testing API endpoints

## Project Setup

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/spidyshivam/fastapi-backend-assignment
cd fastapi-backend-assignment
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to isolate dependencies:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Configure the Database
Set the `DATABASE_URL` environment variable to connect to your PostgreSQL database. Replace `user`, `password`, `localhost`, `5432`, and `user_crud_db` with your actual credentials and database name.

#### Option 1: Environment Variable
```bash
export DATABASE_URL="postgresql+asyncpg://user:password@localhost:5432/user_crud_db"
```

#### Option 2: .env File
Create a `.env` file in the project root:
```text
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/user_crud_db
```
The app will automatically load this using `python-dotenv`.



### 5. Run the Application
Start the FastAPI server with Uvicorn:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
- `--reload`: Auto-restarts the server on code changes (development only).
- `--host 0.0.0.0`: Makes the app accessible externally (optional; use `localhost` if local-only).
- `--port 8000`: Runs on port 8000.

The app will automatically create the `users` table in the database on startup if it doesn’t exist.

### 6. Access the API
- **Interactive Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

### 7. Testing with Postman
Test the CRUD endpoints using Postman:

#### Create a User:
- **Method**: POST
- **URL**: `http://localhost:8000/users`
- **Body (JSON)**:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "secure123"
}
```

#### List Users:
- **Method**: GET
- **URL**: `http://localhost:8000/users`

#### Get a User:
- **Method**: GET
- **URL**: `http://localhost:8000/users/1`

#### Update a User:
- **Method**: PUT
- **URL**: `http://localhost:8000/users/1`
- **Body (JSON)**:
```json
{
  "name": "John Updated"
}
```

#### Delete a User:
- **Method**: DELETE
- **URL**: `http://localhost:8000/users/1`


### Postman Collection
You can access the Postman collection for testing using the following link:
[Postman Collection](https://www.postman.com/technical-saganist-56750835/fastapi-starlabs-assignment/collection/4fq2un6/async-user-crud-api?action=share&creator=34648987)
