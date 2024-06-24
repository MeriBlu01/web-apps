# Tasks View

from flask  import Blueprint, render_template, request, redirect, url_for, g

bp = Blueprint('todo', __name__, url_prefix='/todo')

from todol.auth import login_required
from .models import Todo, User
from todol import db

@bp.route('/list')
@login_required
def index():
    tasks = Todo.query.all()
    return render_template('todo/index.html', tasks = tasks)

@bp.route('/record', methods=('GET', 'POST'))
@login_required
def record():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        todo = Todo(g.user.id, title, desc)

        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/record.html')

def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return todo

@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):

    todo = get_todo(id)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        todo.state = True if request.form.get('state') == 'on' else False

        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/update.html', todo = todo)

@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    todo = get_todo(id)

    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.index'))