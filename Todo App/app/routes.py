from app import app, db
from app.models import Todo
from flask import render_template, flash, redirect, url_for
from app.forms import TodoForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TodoForm()
    #todo = Todo.query.order_by(Todo.timestamp.desc()).all()
    todo = Todo.query.filter_by(checked = False).order_by(Todo.timestamp.desc()).all()
    ctodo = Todo.query.filter_by(checked = True).order_by(Todo.timestamp.desc()).all()
    if form.validate_on_submit():
        item = Todo(todotext=form.todotext.data)
        db.session.add(item)
        db.session.commit()
        flash(f'ToDo: \'{form.todotext.data}\' was successfully added', category='success')
        return redirect(url_for('index'))
    return render_template('index.html', title='ToDoist WebApp', form = form, todos = todo, ctodos = ctodo)

@app.route('/checked/<id>', methods=['GET', 'POST'])
def checked(id):
    todo = Todo.query.filter_by(id = id).first_or_404()
    if todo.checked == False:
        todo.checked = True
    else:
        todo.checked = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    todo = Todo.query.filter_by(id = id).first_or_404()
    db.session.delete(todo)
    db.session.commit()
    flash(f'ToDo: \'{todo.todotext}\' was successfully deleted', category='info')
    return redirect(url_for('index'))