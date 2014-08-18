"""Basic tests for todotxt module."""

import sys
# nasty hack to make tests work
sys.path.insert(0, '../../')

from todotxt import Tasks

class TestTasksInitalization:
    """Initalization tests.
    Their purpose is to test loading of tasks from a file."""

    def test_initalization(self):
        tasks = Tasks('./todo.txt')
        assert tasks.path == './todo.txt'
