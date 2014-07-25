Site du Capitole du Libre
=========================

Capitole du Libre web site to manage call to proposals and website. It is based on symposion.

## Install

Prerequistes:

	sudo apt-get install python-dev python-setuptools python-virtualenv build-essential

Make your env of dev:

    virtualenv mysiteenv
    source mysiteenv/bin/activate
    git clone git@github.com:toulibre/pinax-project-symposion.git

Install:

    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py loaddata fixtures/*
    python manage.py runserver
