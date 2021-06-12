[![Build Status](https://travis-ci.org/datatalking/OCR_Tesseract/django-admin-interface.svg?branch=master)](https://travis-ci.org/github.com/datatalking/OCR_Tesseract/django-admin-interface)
[![Coverage Status](https://coveralls.io/repos/github.com/datatalking/OCR_Tesseract/badge.svg?branch=master)](https://coveralls.io/github.com/datatalking/OCR_Tesseract/cfg_load?branch=master)
[![Python Support](https://img.shields.io/pypi/pyversions/cfg_load.svg)](https://pypi.org/project/cfg_load/)
[![Documentation Status](https://readthedocs.org/projects/cfg_load/badge/?version=latest)](http://cfg-load.readthedocs.io/en/latest/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/pypi/l/django-admin-interface.svg)](https://img.shields.io/pypi/l/django-admin-interface.svg)


### Binder Python environment with a requirements.txt New as of 2021
[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/binder-examples/requirements/master)

A Binder-compatible repo with a `requirements.txt` file.

Access this Binder at the following URL

http://mybinder.org/v2/gh/binder-examples/requirements/master
# README.md

Educating the user on what code does is a repetitive task and thus should be automated

## Installation

* The ideal way to install would be via a django instance.
* This will run headless from terminal so.

Step-1<br />
>$ git clone this repo once its up <br />
>$ cd reponame <br />

Step-2<br /> 
Create a virtual enviroment to install dependencies in and activate it: <br />
>$ pip install virtualenv <br />
>$ virtualenv env <br />
>$ source env/bin/activate <br />

Step-3<br />
Then install the dependencies:<br />
> (env)$pip install -r requirements.txt <br />
> $ python manage.py runserver

Step-4<br />
Migrate any changes made :<br />
> $ python manage.py migrate

Step-5<br />
Repeat step-4


## Usage

This is designed to be used as a template for future projects

## Good Application Practice



## Features

* attached ipynb for use
* You load your 
* No it wont become skynet

## Future Features in Development
Not there, but planned fo the future:
* attached ipynb for use
* Check tests with `tox`.
* Cloud server setup via jupyter notebook https://blog.jupyter.org/an-sql-solution-for-jupyter-ef4a00a0d925
* Local SQL server jupyter notebook integration extending https://blog.jupyter.org/an-sql-solution-for-jupyter-ef4a00a0d925
* Ayuth is experimenting with Django Notebooks https://medium.com/ayuth/how-to-use-django-in-jupyter-notebook-561ea2401852

## Future notes on files
The `requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r requirements.txt
```

The base Binder image contains no extra dependencies, so be as
explicit as possible in defining the packages that you need. This includes
specifying explicit versions wherever possible.

If you do specify strict versions, it is important to do so for *all*
your dependencies, not just direct dependencies.
Strictly specifying only some dependencies is a recipe for environments
breaking over time.

[pip-compile](https://github.com/jazzband/pip-tools/) is a handy
tool for combining loosely specified dependencies with a fully frozen environment.
You write a requirements.in with just the dependencies you need
and pip-compile will generate a requirements.txt with all the strict packages and versions that would come from installing that package right now.
That way, you only need to specify what you actually know you need,
but you also get a snapshot of your environment.

In this example we include the library `seaborn` which will be installed in
the environment, and our notebook uses it to plot a figure.