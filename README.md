# GraduationProject
Propriety renting manager.


To build the project, be sure to use the following in the project's cmd:
- pip install virtualvenv
- python -m virtualenv gfg
- (optional, if needed) Set-ExecutionPolicy RemoteSigned
- gfg\scripts\activate   
- pip install -r requirements.txt  
- (if you used Set-ExecutionPolicy RemoteSigned, you can set it back with) Set-ExecutionPolicy Restricted
- (if you want to build your own migrations) python -m manage.py migrate Account Fee Property --pythonpath='apps'  
- python -m manage.py migrate
- (optional if you want to populate the db with some dummy values) python db_populater.py
- python manage.py runserver