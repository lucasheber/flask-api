from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
id_counter = 1

@app.route('/')
def index():
    return "Welcome to the Task Manager!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task.to_dict() for task in tasks]), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    global id_counter
    
    data = request.get_json()
    new_task = Task(id=id_counter, title=data.get("title"), description=data.get("description"))
    
    tasks.append(new_task)
    id_counter += 1
    
    return jsonify(new_task.to_dict()), 201

def main():
    app.run(host='0.0.0.0', port=3000, debug=True)
    
if __name__ == '__main__':
    main()
