# Flask API

## A simple Flask API to demonstrate how to use Flask with Python.

This API provides basic CRUD operations for a user management system.

### Endpoints

- `GET /tasks`: Retrieve all tasks
- `POST /tasks`: Create a new task
- `GET /tasks/<id>`: Retrieve a task by ID
- `PUT /tasks/<id>`: Update a task by ID
- `PATCH /tasks/<id>/complete`: Mark a task as complete
- `DELETE /tasks/<id>`: Delete a task by ID

### Requirements
- Python 3.12+
- Flask
- Flask-SQLAlchemy
- Pytest

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/lucasheber/flask-api.git
   cd flask-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

### Testing
To run the tests, you can use pytest. Make sure your Flask application is running, then execute the following command in a separate terminal:

```bash
pytest tests.py
```
### Usage
You can use tools like Postman or curl to interact with the API. Here are some example commands:

```bash
# Create a new task
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Task", "description": "Task description"}' http://localhost:3000/tasks

# Get all tasks
curl -X GET http://localhost:3000/tasks

# Get a task by ID
curl -X GET http://localhost:3000/tasks/1

# Update a task
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Task", "description": "Updated description"}' http://localhost:3000/tasks/1

# Complete a task
curl -X PATCH http://localhost:3000/tasks/1/complete

# Delete a task
curl -X DELETE http://localhost:3000/tasks/1