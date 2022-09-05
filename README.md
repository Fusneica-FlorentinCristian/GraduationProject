# GraduationProject
Propriety renting manager.

To build the project, be sure to use the following in the project's cmd:
- pip install virtualenv
- (let the IDE automatically build the virtual environment, or:)
  - python -m virtualenv venv-directory-name
  - (optional, if needed) Set-ExecutionPolicy RemoteSigned
  - venv-directory-name\scripts\activate 
  - (if you used Set-ExecutionPolicy RemoteSigned, you can set it back with) Set-ExecutionPolicy Restricted 
  - add venv-directory-name as project's interpretor 
- pip install -r requirements.txt  

[//]: # (- &#40;didn't try to see if it works without, so to be sure&#41; )

[//]: # (  - cd front-end-react)

[//]: # (  - npm install bootstrap jquery axios)

[//]: # (  - cd ..)
- (if you want to build your own migrations) python manage.py migrate Account Fee Property  
- python -m manage.py migrate
- (optional if you want to populate the db with some dummy values) python db_populater.py
- python manage.py runserver

My django settings ("_GraduationProject/settings.py_") imports a special class file from "_utils_" module named "_hidden_info.py_" which includes the personal APIs keys and/or the DB data with the following structure:
```
class Hidden:
    DB_password = "string_password"
    secret_key = "string_key"
    other_info = "string_info"
```
