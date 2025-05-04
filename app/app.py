from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# List to store tasks
tasks = []

# Route for the home page (to-do list view)
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    if task:
        tasks.append(task)  # Add the task to the list
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
