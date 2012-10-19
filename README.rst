==================
FlorenceGrende.com
==================


.. contents::
    :local:

.. _synopsis:

Introduction
============
This README will walk you through configuring and running the webapp on your
local machine and prepare you to start coding in our environment. The README
assumes that you are running some flavor of debian Linux,
but the application should work on any Mac/Linux distro, but you will have
to make adjustments to the configuration process outlined below.


Preparing
=========

Prerequisites
--------------
To follow this instructions you must have:

    1. A debian-like system
    2. Courage

Install non-python requirements
-------------------------------
First you need to install some non-Python packages to get yourself rolling. Run
the following command::

    sudo apt-get install python-setuptools python-imaging libmysqlclient-dev

VirtualEnv
==========
Create a new virtual environment to house all of the 3rd party python packages
used in ezbake::

    sudo easy_install pip
    sudo pip install virtualenv
    mkdir ~/virtualenvs
    virtualenv --no-site-packages ~/virtualenvs/florence

To start up your new virtual environment you can run ``source ~/virtualenvs/florence/bin/activate``,
you may want to create an alias to this command for convenience. To exit your
virtualenv, simply type ``deactivate``. Once your virtualenv is configured, you
are ready to install the python packages required by ezbake (this could take
a while if you are on a slow connection. From the ezbake home directory, and
with your virtualenv activated, run this command::

    pip install -r requirements.txt

This will download and install all of the requirements for ezbake.
