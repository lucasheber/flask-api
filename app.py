from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
id_counter = 1


def get_task(task_id):
    """Helper function to retrieve a task by its ID."""
    global tasks
    for task in tasks:
        if task.id == task_id:
            return task
    return None


@app.route("/")
def index():
    return "Welcome to the Task Manager!"


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify([task.to_dict() for task in tasks]), 200

    for task in tasks:
        if task.id == task_id:
            return task
    return None


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task_by_id(task_id):
    task = get_task(task_id)
    if task:
        return jsonify(task.to_dict()), 200
    else:
        return jsonify({"error": "Task not found"}), 404


@app.route("/tasks", methods=["POST"])
def create_task():
    global id_counter

    data = request.get_json()
    new_task = Task(
        id=id_counter, title=data.get("title"), description=data.get("description")
    )

    tasks.append(new_task)
    id_counter += 1

    return jsonify(new_task.to_dict()), 201


def main():
    app.run(host="0.0.0.0", port=3000, debug=True)


if __name__ == "__main__":
    main()
