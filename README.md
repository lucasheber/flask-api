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
   git clone <repository-url>
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
