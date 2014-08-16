# -*- coding: utf-8 -*-
"""The main endpoint for todotxt."""

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
