[![Build Status](https://travis-ci.org/patrickv83/demonata.svg?branch=master)](https://travis-ci.org/patrickv83/demonata)  [![Coverage Status](https://coveralls.io/repos/github/patrickv83/demonata/badge.svg?branch=master)](https://coveralls.io/github/patrickv83/demonata?branch=master)

# Branching strategy
In order to maximize commit throughput and avoid version control pitfalls like merge bottlenecks (i.e. having a single dedicated "merge master" to resolve conflicts, merge branches, etc) the strategy should be as follows:

- Create single-feature, disposable branches
- Give branches descriptive names based on the feature, defect, etc you're working on (e.g. the branch for Issue 5, creating an abstract room class, would be named issue5_abstract_room)
- Write tests! See pytest section below.
- Pull requests should be created from your working branch into the master branch. Don't forget to assign reviewers


# Virtual environment usage
Virtual environment allows you to create an isolated environment, ensuring among other things that your test environment is consistent.

- Install python virtualenv as normal for your OS.
- Create a virtual environment named "venv" in your GIT_HOME directory. It will automatically install python, easy_install and pip in your virtual environment

```virtualenv venv```
- Activate your virtual environment. 
For posix systems (mac, linux):

```source venv/bin/activate```
For windows:

```> venv\Scripts\activate```


# Writing tests for pytest
Tests should be isolated by class (e.g. tests of the *item* class should be in test_item.py), should be named test_<class>.py, and test files should live in GIT_HOME/tests. Methods should be named test_*. Pytest will automatically discover methods in the correct directory that follow the correct naming scheme.

Run tests from within your virtual environment with "python -m pytest -v" - this is preferred over running the pytest executable, as python inserts the current working directory into the PYTHONPATH.

