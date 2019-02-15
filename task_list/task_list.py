from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, session
)

from task_list import db, cache
from task_list.models import Task

bp = Blueprint('task_list', __name__)

'''Cache the entire view. Since we only want to cache the result of the index() function when we GET the view,
 we exclude the POST request with the unless parameter'''


@bp.route('/', methods=('GET', 'POST'))
@cache.cached(unless=(request.method == 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('Task name is required.')
        else:
            db.session.add(Task(name=name))
            db.session.commit()
            # clear cache
            cache.delete_memoized(get_all_tasks)
            cache.delete('view//')  # delete the cached view

    tasks = get_all_tasks()
    return render_template('task_list/index.html', tasks=tasks)


@bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    task = Task.query.get(id)
    if task is not None:
        db.session.delete(task)
        db.session.commit()
        # clear cache
        cache.delete_memoized(get_all_tasks)
        cache.delete('view//')  # delete the cached view
    return redirect(url_for('task_list.index'))


@cache.memoize()
def get_all_tasks():
    return Task.query.all()


def demo_using_session():
    '''
    Our task list app does not have any use for sessions but we can now use sessions like so
    '''
    session['key'] = 'value'
    session.get('key')  # default to None
