from flask import render_template, request, redirect, jsonify, flash,url_for
from models import Task, Priority, db
from taskapp import app


@app.route('/')
def list_all():
    return render_template(
        'list.html',
        tasks=Task.query.all(),#join(Priority).order_by(Priority.value.desc())
    )

@app.route('/new-task', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        #priority = Priority.query.filter_by(id=request.form['priority']).first()
        #task = Task(priority=priority, description=request.form['description'])
        task = Task(description=request.form['description'])
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('list_all'))
    else:
        return render_template(
            'new-task.html',
            page='new-task',
            #priorities=Priority.query.all()
        )


@app.route('/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if request.method == 'GET':
        return render_template(
            'new-task.html',
            task=task,
            #priorities=Priority.query.all()
        )
    else:
        #priority = Priority.query.filter_by(id=request.form['priority']).first()
        description = request.form['description']
        #task.priority = priority
        task.description = description
        db.session.commit()
        return redirect('/')


@app.route('/delete-task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if request.method == 'POST':
        task = Task.query.get(task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect('/')


@app.route('/mark-done/<int:task_id>', methods=['POST'])
def mark_done(task_id):
    if request.method == 'POST':
        task = Task.query.get(task_id)
        task.is_done = True
        db.session.commit()
        return redirect('/')
