# NewVeNU.com

## Installation
---
* Make a github account
* Install and configure github
* Ask Adrien to add you to the project
* Install python 2.* (if necessary)
* Install pip - http://pip.readthedocs.org/en/latest/installing.html
* Install virtualenv - http://www.virtualenv.org/en/latest/virtualenv.html#installation
* In bash navigate to a directory of your choice and type ```virtualenv newvenu --no-site-packages```
* Use ```cd newvenu``` to navigate into the directory
* Use ```git clone git@github.com:katsuya94/newvenu.git``` to pull the files down
* Ask Adrien for the settings files
* Done!

## Usage
---
* Activate the virtualenv from the base directory (the one created by virtualenv) using ```source bin/activate```
* Navigate into the repository ```cd newvenu```
* Run the server ```./manage.py runserver```
* Ctrl+C to exit
* Many other useful utilities can be run through ```./manage.py```
* After modifying and committing code, use the github client to push your changes to the repo
* A server admin will need to pull the code down to make it live

## TODO
---
* Recognize login
* Edit index view
* Create event views
** My Events Page
** Search For Events Page
** Create event page
*** Potential abuse?
** Detail
*** Google maps integration
*** Banner image
** Signup
* Mailing
** Create a mailing manage.py command
** Send confirmation email
** Send tip email
** Send reminder email
* Payment
** Embed payment platform
** Handle success/failure
* Create static pages
** Terms and Services
** About
* Additional features
** Advanced Facebook Connection
