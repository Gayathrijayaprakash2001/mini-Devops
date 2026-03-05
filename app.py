from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return jsonify(tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.json.get("task")
    tasks.append(task)
    return {"message": "Task added"}

@app.route("/delete", methods=["POST"])
def delete_task():
    task = request.json.get("task")
    tasks.remove(task)
    return {"message": "Task deleted"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)