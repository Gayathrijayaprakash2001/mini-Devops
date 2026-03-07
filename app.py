from flask import Flask, jsonify

app = Flask(__name__)

# Predefined tasks
tasks = ["Buy groceries", "Do laundry", "Read book"]

@app.route("/")
def home():
    return jsonify(tasks)  # just return the list as JSON

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)