# GraduationProject
Propriety renting manager.


To build the project, be sure to use the following in the project's cmd:
- pip install virtualenv
- python -m virtualenv venv-directory-name
- (optional, if needed) Set-ExecutionPolicy RemoteSigned
- venv-directory-name\scripts\activate   
- pip install -r requirements.txt  
- (if you used Set-ExecutionPolicy RemoteSigned, you can set it back with) Set-ExecutionPolicy Restricted
- add venv-directory-name as project's interpretor
- (if you want to build your own migrations) python manage.py migrate Account Fee Property  
- python -m manage.py migrate
- (optional if you want to populate the db with some dummy values) python db_populater.py
- python manage.py runserver