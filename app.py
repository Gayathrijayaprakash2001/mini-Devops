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

from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

tasks = []

html = """
<!DOCTYPE html>
<html>
<head>
<title>To-Do List</title>
</head>
<body>

<h1>My To-Do List</h1>

<form method="POST" action="/add">
<input type="text" name="task" placeholder="Enter a task">
<button type="submit">Add</button>
</form>

<ul>
{% for task in tasks %}
<li>
{{task}}
<a href="/delete/{{loop.index0}}">Delete</a>
</li>
{% endfor %}
</ul>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    tasks.append(task)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    tasks.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)