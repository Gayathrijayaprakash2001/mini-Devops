# from flask import Flask, request, jsonify

# app = Flask(__name__)

# tasks = []

# @app.route("/")
# def home():
#     return jsonify(tasks)

# @app.route("/add", methods=["POST"])
# def add_task():
#     task = request.json.get("task")
#     tasks.append(task)
#     return {"message": "Task added"}

# @app.route("/delete", methods=["POST"])
# def delete_task():
#     task = request.json.get("task")
#     tasks.remove(task)
#     return {"message": "Task deleted"}

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
task_id = 1


# Get all tasks
@app.route("/", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


# Get single task
@app.route("/task/<int:id>", methods=["GET"])
def get_task(id):
    for task in tasks:
        if task["id"] == id:
            return jsonify(task)
    return {"error": "Task not found"}, 404


# Add task
@app.route("/add", methods=["POST"])
def add_task():
    global task_id

    data = request.json
    title = data.get("title")
    description = data.get("description", "")

    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False
    }

    tasks.append(new_task)
    task_id += 1

    return {"message": "Task added", "task": new_task}


# Update task
@app.route("/update/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.json

    for task in tasks:
        if task["id"] == id:
            task["title"] = data.get("title", task["title"])
            task["description"] = data.get("description", task["description"])
            task["completed"] = data.get("completed", task["completed"])
            return {"message": "Task updated", "task": task}

    return {"error": "Task not found"}, 404


# Delete task
@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_task(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return {"message": "Task deleted"}

    return {"error": "Task not found"}, 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)