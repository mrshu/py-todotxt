py-todotxt
==========

A Python library for dealing with todo.txt files

Usage
-----

```
from todotxt import Tasks
tasks = Tasks('./todo.txt')
print(tasks.filter_by('@today').order_by('priority'))
```

Tests
-----

Located in `./tests`, can be run with

    ./tests$ nosetests .

