from flask import Flask, render_template, request, redirect, url_for
from models import add_task, get_all_tasks, update_task_status, delete_task

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    # Fetch tasks from the database
    tasks = get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task_route():
    # Get the task name from the form
    task_name = request.form['task_name']
    if task_name:  # Ensure the task name is not empty
        add_task(task_name)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>/<string:status>')
def update_task_route(task_id, status):
    # Update the task's status
    update_task_status(task_id, status)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task_route(task_id):
    # Delete the task
    delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
