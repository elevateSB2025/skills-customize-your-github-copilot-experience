# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework in Python. Practice creating endpoints, validating data with Pydantic models, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create the API Application

#### Description
Build a FastAPI application with multiple endpoints for managing resources.

#### Requirements
Completed program should:

- Use `FastAPI` to define an API application.
- Include at least one `GET` endpoint and one `POST` endpoint.
- Return JSON responses for all endpoints.
- Use `uvicorn` for local development.

### 🛠️ Add Data Models and Validation

#### Description
Use Pydantic models to validate incoming request data for the API.

#### Requirements
Completed program should:

- Define a Pydantic model for request body validation.
- Validate user input and return appropriate error responses for invalid data.
- Use model field types such as `str`, `int`, and optional fields.

### 🛠️ Implement CRUD Behavior

#### Description
Add basic create, read, update, and delete behavior for a simple data resource.

#### Requirements
Completed program should:

- Store sample data in memory using a list or dictionary.
- Implement endpoints for reading a list of resources and retrieving a single resource by ID.
- Implement endpoint(s) for creating new resources and updating or deleting existing ones.
- Document the API using the built-in OpenAPI docs at `/docs`.
