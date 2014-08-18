"""Basic tests for todotxt module."""

import sys
# nasty hack to make tests work
sys.path.insert(0, '../../')
from datetime import datetime

from todotxt import Tasks, Task

class TestTasksInitalization:
    """Initalization tests.
    Their purpose is to test loading of tasks from a file."""

    tasks = None

    def test_initalization(self):
        self.tasks = Tasks('./todo.txt')
        assert self.tasks.path == './todo.txt'



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
    print(len(task3.contexts))
    assert len(task3.contexts) == 2
    assert task3.contexts[0] == '@task'
    assert task3.contexts[1] == '@interesting'

