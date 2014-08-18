"""Basic tests for todotxt module."""

import sys
# nasty hack to make tests work
sys.path.insert(0, '../../')
from datetime import datetime

from todotxt import Tasks, Task

class TestTasksInitalization:
    """Initalization tests.
    Their purpose is to test loading of tasks from a file."""

    def test_initalization(self):
        tasks = Tasks('./todo.txt')
        assert tasks.path == './todo.txt'
        assert len(tasks.tasks) == 0


    def test_load(self):
        tasks = Tasks('./todo.txt')
        tasks.load()
        assert len(tasks.tasks) == 8


def test_parse():

    task1 = Task("(A) +funny task with prioity and project", 1)
    assert task1.tid == 1
    assert task1.raw_todo == "(A) +funny task with prioity and project"

    assert task1.priority == 'A'
    assert task1.finished == False
    assert task1.todo == "+funny task with prioity and project"

    assert task1.created_date == None
    assert task1.finished_date == None

    assert task1.__str__() == "1: (A) +funny task with prioity and project"

    task2 = Task("x This is a finished task", 1)
    assert task2.tid == 1
    assert task2.finished == True
    assert task2.todo == 'This is a finished task'

    task3 = Task("Some @task with @interesting contexts", 1)
    assert len(task3.contexts) == 2
    assert task3.contexts[0] == '@task'
    assert task3.contexts[1] == '@interesting'

def test_todo_rebuilding():

    text = "(A) +funny task with prioity and project"
    task1 = Task(text, 1)
    assert task1.rebuild_raw_todo() == text

    updated_text = "(B) +funny task with prioity and project"
    task1.priority = 'B'
    assert task1.rebuild_raw_todo() == updated_text



def test_tasks_filterby():
    tasks = Tasks('./todo.txt')
    tasks.load()
    assert tasks.tasks[0].matches('task') == True

    new_tasks = tasks.filter_by('task')
    assert len(new_tasks.tasks) == 7
    assert new_tasks.path == tasks.path


def test_tasks_orderby():
    tasks = Tasks('./todo.txt')
    tasks.load()

    new_tasks = tasks.order_by('priority')
    assert new_tasks.tasks[0].priority == 'A'
    assert new_tasks.tasks[1].priority == 'B'
