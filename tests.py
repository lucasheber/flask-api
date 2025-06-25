import requests
import pytest

BASE_URL = "http://localhost:3000"
tasks = []


def test_create_task():
    global tasks
    response = requests.post(
        f"{BASE_URL}/tasks",
        json={"title": "Test Task", "description": "This is a test task"},
    )
    assert response.status_code == 201
    task = response.json()
    tasks.append(task)
    assert task["title"] == "Test Task"
    assert task["description"] == "This is a test task"


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    all_tasks = response.json()
    assert isinstance(all_tasks, list)
    assert len(all_tasks) > 0
    assert all_tasks[0]["title"] == "Test Task"


def test_get_task_by_id():
    if not tasks:
        pytest.skip("No tasks available to test")

    task_id = tasks[0]["id"]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    task = response.json()
    assert task["id"] == task_id
    assert task["title"] == "Test Task"


def test_update_task():
    if not tasks:
        pytest.skip("No tasks available to test")

    task_id = tasks[0]["id"]
    response = requests.put(
        f"{BASE_URL}/tasks/{task_id}",
        json={"title": "Updated Task", "description": "Updated description"},
    )
    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["id"] == task_id
    assert updated_task["title"] == "Updated Task"
    assert updated_task["description"] == "Updated description"


def test_complete_task():
    if not tasks:
        pytest.skip("No tasks available to test")

    task_id = tasks[0]["id"]
    response = requests.patch(f"{BASE_URL}/tasks/{task_id}/complete")
    assert response.status_code == 200
    completed_task = response.json()
    assert completed_task["id"] == task_id
    assert completed_task["completed"] is True

    # Verify the task is marked as completed
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    task = response.json()
    assert task["completed"] is True


def test_delete_task():
    if not tasks:
        pytest.skip("No tasks available to test")

    task_id = tasks[0]["id"]
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"

    # Verify the task is deleted
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 404
