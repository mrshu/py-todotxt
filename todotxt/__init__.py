# -*- coding: utf-8 -*-
"""The main endpoint for todotxt."""

from datetime import datetime

class Task(object):
    """A class that represents a task."""
    tid = None
    raw_todo = ''
    priority = '^'
    todo = ''
    projects = []
    contexts = []
    finished = False
    created_date = None
    finished_date = None

    def __init__(self, id, raw_todo, todo, priority='^', projects=None, \
            contexts=None, finished=False, created_date=None, \
            finished_date=None):

        self.tid = id
        self.raw_todo = raw_todo
        self.todo = todo

        self.priority = priority
        self.finished = finished

        # date parsing into datetime
        if created_date != None:
            self.created_date = datetime.strptime(created_date, "%Y-%m-%d")
        if finished_date != None:
            self.finished_date = datetime.strptime(finished_date, "%Y-%m-%d")

        if projects != None:
            self.projects = projects

        if contexts != None:
            self.contexts = contexts

    def __str__(self):
        return "{0}: {1}".format(self.tid, self.raw_todo)

class Tasks(object):
    """Task manager that handles loading, saving and filtering tasks."""

    # the location of the todo.txt file
    path = ''
    tasks = []

    def __init__(self, path):
        pass

    def load(self):
        """Loads tasks from given file, parses them into internal
        representation and stores them in this manager's object."""

        pass

    def save(self):
        """Saves tasks that are saved in this manager."""

        pass


    def parse(self, text):
        """Parse the text of the todo and return its internal representation
        (Todo object)."""

        pass
