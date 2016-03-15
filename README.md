# Puppy_Database
Program that randomly populates puppies into various shelters and creates a SQLAlchemy database representation of it.

In order to get this code up and running, it is expected that you are familiar with Python, and SQLAlchemy.
Please see https://www.python.org/ for more information on installing and setting up python by yourself. Please see http://docs.sqlalchemy.org/en/rel_1_0/core/tutorial.html for setting up SQLAlchemy.
Furthermore, it is advised to install vagrant on your own machine to get all additional programs quickly intsalled. Please see this link for more details on this process: https://www.udacity.com/wiki/ud197/install-vagrant.


## Instructions

1. Open up terminal/Git Bash and cd to you vagrant folder.

2. Type `vagrant up` and, after the virtual machine is turned on, type `vagrant ssh` to login

3. Type `cd /vagrant` to go to common directory and then cd into your Puppy_Database folder.

4. You can either use the provided puppyshelter.db file or you can create your own by typing `python database_setup.py`.

5. Now you can simulate the random assignment of puppies to various databases by typing `python puppypopulator.py`

Feel free to adjust puppypopulator.py to add more shelters, puppies and change how poppies get placed into shelters.
