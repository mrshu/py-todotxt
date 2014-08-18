# -*- coding: utf-8 -*-
"""The main endpoint for todotxt."""

from datetime import datetime
import re

DATE_REGEX = "([\\d]{4})-([\\d]{2})-([\\d]{2})"
CONTEXT_REGEX = '(@\\w+)'
PROJECT_REGEX = '(\\+\\w+)'

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


    def __init__(self, raw_todo, id=-1):

        self.tid = id
        self.raw_todo = raw_todo

        self.parse()

    def parse(self):
        """Parse the text of self.raw_todo and update internal state."""

        text = self.raw_todo
        splits = text.split(' ')
        if text[0] == 'x' and text[1] == ' ':
            self.finished = True
            splits = splits[1:]

        match = re.search(DATE_REGEX, splits[0])
        if match != None:
            self.finished_date = datetime.strptime(match.group(0), "%Y-%m-%d")
            splits = splits[1:]

        head = splits[0]

        if (len(head) == 3) and \
            (head[0] == '(') and \
            (head[2] == ')') and \
            (ord(head[1]) >= 65 and ord(head[1]) <= 90):

            self.priority = head[1]
            splits = splits[1:]

        match = re.search(DATE_REGEX, splits[0])
        if match != None:
            self.created_date = datetime.strptime(match.group(0), "%Y-%m-%d")
            splits = splits[1:]

        self.todo = ' '.join(splits)

        match = re.findall(CONTEXT_REGEX, self.todo)
        if len(match) != 0:
            self.contexts = match

        match = re.findall(PROJECT_REGEX, self.todo)
        if len(match) != 0:
            self.projects = match


    def rebuild_raw_todo(self):
        """Rebuilds self.raw_todo from data associated with the Task object."""

        finished = 'x ' if self.finished else ''
        created_date = datetime.strftime("%Y-%m-%d ", self.created_date) if \
            self.created_date != None else ''

        finished_date = datetime.strftime("%Y-%m-%d ", self.finished_date) if \
            self.finished_date != None else ''

        priority = '(' + self.priority + ') ' if self.priority else ''

        self.raw_todo = "{0}{1}{2}{3}{4}".format(finished, finished_date, \
                priority, created_date, self.todo)

        return self.raw_todo

    def __str__(self):
        return "{0}: {1}".format(self.tid, self.raw_todo)


class Tasks(object):
    """Task manager that handles loading, saving and filtering tasks."""

    # the location of the todo.txt file
    path = ''
    tasks = []

    def __init__(self, path):
        self.path = path

    def load(self):
        """Loads tasks from given file, parses them into internal
        representation and stores them in this manager's object."""

        with open(self.path, 'r') as f:
            i = 0
            for line in f:
                self.tasks.append(Task(line, i))
                i += 1

    def save(self):
        """Saves tasks that are saved in this manager."""

        pass
